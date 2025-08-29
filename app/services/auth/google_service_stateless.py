# app/services/auth/google_service_stateless.py
import uuid
import secrets
import requests
from urllib.parse import urlencode
from fastapi import HTTPException, Request, Response
from fastapi.responses import RedirectResponse

from app.core.config import settings
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.utils.password_utils import get_password_hash
from app.services.auth.token_service import create_access_token

GOOGLE_AUTH_URI = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URI = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URI = "https://www.googleapis.com/oauth2/v3/userinfo"
SCOPES = ["openid", "email", "profile"]

def build_google_url() -> str:
    """Build Google OAuth authorization URL without state"""
    if not settings.GOOGLE_CLIENT_ID:
        raise HTTPException(status_code=500, detail="Google Client ID not configured")
        
    # Use a fixed redirect URI
    redirect_uri = "http://localhost:8000/v1/auth/google/callback"
    
    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent",
    }
    
    return f"{GOOGLE_AUTH_URI}?{urlencode(params)}"

def login_google_stateless(response: Response, return_url: bool = False):
    """Initiate Google OAuth login without state parameter"""
    try:
        url = build_google_url()
        
        if return_url:
            return {
                "google_oauth_url": url,
                "message": "Copy this URL and open it in your browser to authenticate with Google"
            }
        
        return RedirectResponse(url=url, status_code=302)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to initiate Google login: {str(e)}")

def callback_google_stateless(request: Request, code: str, user_repo: UserRepository):
    """Handle Google OAuth callback without state validation"""
    try:
        # Use fixed redirect URI to match what we sent to Google
        redirect_uri = "http://localhost:8000/v1/auth/google/callback"
        
        token_data = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": redirect_uri,
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
                    last_name=userinfo.get("family_name", "") or "",
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
            redirect_url = f"{settings.GOOGLE_POST_LOGIN_REDIRECT}?access_token={jwt_token}&token_type=bearer"
            return RedirectResponse(url=redirect_url, status_code=302)
        else:
            return {
                "access_token": jwt_token, 
                "token_type": "bearer",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name
                }
            }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error during Google authentication: {str(e)}")