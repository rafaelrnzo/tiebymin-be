# app/services/auth/google_service_v2.py
import uuid
import secrets
import requests
from urllib.parse import urlencode
from fastapi import HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from typing import Dict

from app.core.config import settings
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.utils.password_utils import get_password_hash
from app.services.auth.token_service import create_access_token

GOOGLE_AUTH_URI = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URI = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URI = "https://www.googleapis.com/oauth2/v3/userinfo"
SCOPES = ["openid", "email", "profile"]

# In-memory state storage (use Redis in production)
active_states: Dict[str, bool] = {}

def build_google_url(state: str) -> str:
    """Build Google OAuth authorization URL"""
    if not settings.GOOGLE_CLIENT_ID:
        raise HTTPException(status_code=500, detail="Google Client ID not configured")
    if not settings.GOOGLE_REDIRECT_URI:
        raise HTTPException(status_code=500, detail="Google Redirect URI not configured")
        
    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent",
        "state": state,
    }
    
    return f"{GOOGLE_AUTH_URI}?{urlencode(params)}"

def login_google(response: Response, return_url: bool = False):
    """Initiate Google OAuth login with memory-based state storage"""
    try:
        state = secrets.token_urlsafe(32)  # Longer state for security
        url = build_google_url(state)
        
        # Store state in memory (use Redis in production)
        active_states[state] = True
        
        # Clean old states (keep only last 100)
        if len(active_states) > 100:
            old_states = list(active_states.keys())[:-50]
            for old_state in old_states:
                active_states.pop(old_state, None)
        
        if return_url:
            return {
                "google_oauth_url": url,
                "message": "Copy this URL and open it in your browser to authenticate with Google",
                "state": state
            }
        
        # Still set cookie as backup
        resp = RedirectResponse(url=url, status_code=302)
        resp.set_cookie(
            "g_state_backup", 
            state, 
            httponly=True, 
            max_age=600, 
            samesite="lax",
            secure=False,
            path="/",
        )
        
        print(f"Generated state: {state}")
        print(f"Stored in memory: {state in active_states}")
        
        return resp
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to initiate Google login: {str(e)}")

def callback_google(request: Request, code: str, state: str, user_repo: UserRepository):
    """Handle Google OAuth callback with memory-based state validation"""
    try:
        print(f"Callback received state: {state}")
        print(f"Active states: {list(active_states.keys())[-5:]}")  # Show last 5
        
        # Check if state exists in memory
        if state not in active_states:
            # Fallback to cookie check
            cookie_state = request.cookies.get("g_state_backup")
            if cookie_state != state:
                raise HTTPException(
                    status_code=400, 
                    detail="Invalid or expired state parameter. Please restart the authentication flow."
                )
        
        # Remove used state
        active_states.pop(state, None)

        token_data = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }
        
        token_resp = requests.post(
            GOOGLE_TOKEN_URI, 
            data=token_data, 
            timeout=15,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        
        if token_resp.status_code != 200:
            raise HTTPException(
                status_code=400, 
                detail=f"Failed to get access token from Google: {token_resp.text}"
            )
        
        token_json = token_resp.json()
        
        if "error" in token_json:
            raise HTTPException(
                status_code=400, 
                detail=f"Google OAuth error: {token_json.get('error_description', token_json['error'])}"
            )

        access_token = token_json.get("access_token")
        if not access_token:
            raise HTTPException(status_code=400, detail="Access token not received from Google")

        headers = {"Authorization": f"Bearer {access_token}"}
        userinfo_resp = requests.get(GOOGLE_USERINFO_URI, headers=headers, timeout=15)
        
        if userinfo_resp.status_code != 200:
            raise HTTPException(
                status_code=400, 
                detail=f"Failed to get user info from Google: {userinfo_resp.text}"
            )
        
        userinfo = userinfo_resp.json()

        email = userinfo.get("email")
        google_id = userinfo.get("sub")
        
        if not email:
            raise HTTPException(status_code=400, detail="Email not provided by Google")
        if not google_id:
            raise HTTPException(status_code=400, detail="Google ID not provided by Google")

        user = user_repo.get_by_email(email=email)
        
        if not user:
            try:
                random_password = str(uuid.uuid4())
                password_hash = get_password_hash(random_password)
                
                user_to_create = UserCreate(
                    email=email,
                    first_name=userinfo.get("given_name", ""),
                    last_name=userinfo.get("family_name", ""),
                    google_id=google_id,
                    password_hash=password_hash,
                )
                user = user_repo.create(user_to_create)
            except Exception as e:
                raise HTTPException(
                    status_code=500, 
                    detail=f"Failed to create user account: {str(e)}"
                )
        elif not user.google_id:
            user_repo.update_google_id(user.id, google_id)
            user.google_id = google_id

        jwt_token = create_access_token(data={"sub": str(user.id)})
        
        if hasattr(settings, 'GOOGLE_POST_LOGIN_REDIRECT') and settings.GOOGLE_POST_LOGIN_REDIRECT:
            redirect_url = f"{settings.GOOGLE_POST_LOGIN_REDIRECT}#access_token={jwt_token}&token_type=bearer"
            resp = RedirectResponse(url=redirect_url, status_code=302)
            resp.delete_cookie("g_state_backup", samesite="lax")
            return resp
        else:
            return {"access_token": jwt_token, "token_type": "bearer"}
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error during Google authentication: {str(e)}")