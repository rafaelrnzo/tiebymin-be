# app/services/auth/google_service.py
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
STATE_COOKIE_NAME = "g_state"

def build_google_url(state: str) -> str:
    """Build Google OAuth authorization URL"""
    # 🔥 Validate required settings first
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
    
    print(f"🔥 Google OAuth URL: {GOOGLE_AUTH_URI}?{urlencode(params)}")  # Debug log
    return f"{GOOGLE_AUTH_URI}?{urlencode(params)}"

def login_google(response: Response):
    """Initiate Google OAuth login"""
    try:
        state = secrets.token_urlsafe(24)
        url = build_google_url(state)
        
        print(f"🔥 Redirecting to: {url}")  # Debug log
        
        # Create redirect response with explicit status code 302
        resp = RedirectResponse(url=url, status_code=302)
        resp.set_cookie(
            STATE_COOKIE_NAME, 
            state, 
            httponly=True, 
            max_age=600, 
            samesite="lax",
            secure=False,  # Set to False for localhost testing
            path="/"
        )
        return resp
    except Exception as e:
        print(f"🔥 Error in login_google: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to initiate Google login: {str(e)}")

def callback_google(request: Request, code: str, state: str, user_repo: UserRepository):
    """Handle Google OAuth callback"""
    try:
        # Validate state parameter
        cookie_state = request.cookies.get(STATE_COOKIE_NAME)
        if not cookie_state or cookie_state != state:
            raise HTTPException(status_code=400, detail="Invalid state parameter")

        # Exchange authorization code for access token
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
        
        # Check if token request was successful
        if token_resp.status_code != 200:
            raise HTTPException(
                status_code=400, 
                detail=f"Failed to get access token from Google: {token_resp.text}"
            )
        
        token_json = token_resp.json()
        
        # Check for errors in token response
        if "error" in token_json:
            raise HTTPException(
                status_code=400, 
                detail=f"Google OAuth error: {token_json.get('error_description', token_json['error'])}"
            )

        access_token = token_json.get("access_token")
        if not access_token:
            raise HTTPException(status_code=400, detail="Access token not received from Google")

        # Get user information from Google
        headers = {"Authorization": f"Bearer {access_token}"}
        userinfo_resp = requests.get(GOOGLE_USERINFO_URI, headers=headers, timeout=15)
        
        if userinfo_resp.status_code != 200:
            raise HTTPException(
                status_code=400, 
                detail=f"Failed to get user info from Google: {userinfo_resp.text}"
            )
        
        userinfo = userinfo_resp.json()

        # Validate required user information
        email = userinfo.get("email")
        google_id = userinfo.get("sub")
        
        if not email:
            raise HTTPException(status_code=400, detail="Email not provided by Google")
        if not google_id:
            raise HTTPException(status_code=400, detail="Google ID not provided by Google")

        # Check if user exists
        user = user_repo.get_by_email(email=email)
        
        if not user:
            # Create new user
            user_to_create = UserCreate(
                email=email,
                first_name=userinfo.get("given_name", ""),
                last_name=userinfo.get("family_name", ""),
                google_id=google_id,
                password_hash=get_password_hash(str(uuid.uuid4())),
            )
            user = user_repo.create(user_to_create)
        elif not user.google_id:
            # Update existing user with Google ID
            user_repo.update_google_id(user.id, google_id)
            user.google_id = google_id  # Update the local object as well

        # Create JWT token
        jwt_token = create_access_token(data={"sub": str(user.id)})
        
        # Create response with token and clear state cookie
        if hasattr(settings, 'GOOGLE_POST_LOGIN_REDIRECT') and settings.GOOGLE_POST_LOGIN_REDIRECT:
            redirect_url = f"{settings.GOOGLE_POST_LOGIN_REDIRECT}#access_token={jwt_token}&token_type=bearer"
            resp = RedirectResponse(url=redirect_url, status_code=302)
            resp.delete_cookie(STATE_COOKIE_NAME, samesite="lax")
            return resp
        else:
            # For API response, we can't clear cookies directly, so we'll return the token
            return {"access_token": jwt_token, "token_type": "bearer"}
        
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        # Log the full error for debugging
        print(f"Google OAuth callback error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error during Google authentication: {str(e)}")


# app/routers/auth.py
from fastapi import APIRouter, Depends, Request, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.repositories.user_repository import UserRepository
from app.dependencies.dependencies import get_user_repository
from app.schemas.user import User as UserSchema, UserRegistration, UserLogin, UserCreate
from app.services.auth.token_service import get_current_user, create_access_token
from app.services.auth.google_service import login_google, callback_google
from app.utils.password_utils import verify_password, get_password_hash

router = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")

@router.post("/register", response_model=UserSchema)
def register_user(
    user_data: UserRegistration,
    user_repo: UserRepository = Depends(get_user_repository),
):
    """Register a new user"""
    existing_user = user_repo.get_by_email(user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user_data.password)

    user_to_create = UserCreate(
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        phone=getattr(user_data, 'phone', None),
        google_id=getattr(user_data, 'google_id', None),
        password_hash=hashed_password,
    )

    new_user = user_repo.create(user_to_create)
    return new_user

@router.post("/login")
async def login_user(
    user_login: UserLogin, 
    user_repo: UserRepository = Depends(get_user_repository)
):
    """Login with email and password"""
    user = user_repo.get_by_email(user_login.email)
    if not user or not verify_password(user_login.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

# 🔥 Debug endpoint to check configuration
@router.get("/debug/google")
def debug_google_config():
    """Debug Google OAuth configuration"""
    from app.core.config import settings
    return {
        "google_client_id": settings.GOOGLE_CLIENT_ID[:20] + "..." if settings.GOOGLE_CLIENT_ID else "NOT SET",
        "google_client_secret": "SET" if settings.GOOGLE_CLIENT_SECRET else "NOT SET",
        "google_redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "cors_origins": settings.BACKEND_CORS_ORIGINS,
        "environment": settings.ENVIRONMENT
    }

# 🔥 Debug endpoint to test Google URL generation
@router.get("/google/test-url")
def test_google_url():
    """Test Google OAuth URL generation"""
    state = secrets.token_urlsafe(24)
    url = build_google_url(state)
    return {
        "google_oauth_url": url,
        "state": state,
        "instructions": "Copy the google_oauth_url and paste it in your browser to test the OAuth flow manually"
    }

@router.get("/google/login")
def google_login(response: Response):
    """Initiate Google OAuth login"""
    return login_google(response)

@router.get("/google/callback")
def google_callback(
    request: Request, 
    code: str = None,
    state: str = None,
    error: str = None,
    user_repo: UserRepository = Depends(get_user_repository)
):
    """Handle Google OAuth callback"""
    # 🔥 Add error handling for Google OAuth errors
    if error:
        raise HTTPException(status_code=400, detail=f"Google OAuth error: {error}")
    
    if not code or not state:
        raise HTTPException(status_code=400, detail="Missing authorization code or state parameter")
    
    return callback_google(request, code, state, user_repo)

@router.get("/me", response_model=UserSchema)
async def read_current_user(current_user: UserSchema = Depends(get_current_user)):
    """Get current authenticated user"""
    return current_user