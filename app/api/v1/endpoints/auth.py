# app/api/v1/routers/auth.py
import secrets
from fastapi import APIRouter, Depends, Request, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from app.repositories.user_repository import UserRepository
from app.dependencies.dependencies import get_user_repository
from app.schemas.user import User as UserSchema, UserRegistration, UserLogin, UserCreate
from app.services.auth.token_service import get_current_user, create_access_token
from app.services.auth.google_service import login_google, callback_google, build_google_url
from app.utils.password_utils import verify_password, get_password_hash

router = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")


@router.post("/register", response_model=UserSchema)
def register_user(
    user_data: UserRegistration,
    user_repo: UserRepository = Depends(get_user_repository),
):
    existing_user = user_repo.get_by_email(user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user_data.password)
    user_to_create = UserCreate(
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        phone=getattr(user_data, "phone", None),
        google_id=getattr(user_data, "google_id", None),
        password_hash=hashed_password,
    )
    new_user = user_repo.create(user_to_create)
    return new_user


@router.post("/login")
async def login_user(
    user_login: UserLogin,
    user_repo: UserRepository = Depends(get_user_repository),
):
    user = user_repo.get_by_email(user_login.email)
    if not user or not verify_password(user_login.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/debug/google")
def debug_google_config():
    # Helpful for confirming env/config on a running instance
    return {
        "google_client_id": settings.GOOGLE_CLIENT_ID[:20] + "..." if settings.GOOGLE_CLIENT_ID else "NOT SET",
        "google_client_secret": "SET" if settings.GOOGLE_CLIENT_SECRET else "NOT SET",
        "google_redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "cors_origins": settings.BACKEND_CORS_ORIGINS,
        "environment": settings.ENVIRONMENT,
    }


@router.get("/google/test-url")
def test_google_url():
    state = secrets.token_urlsafe(24)
    url = build_google_url(state)
    return {
        "google_oauth_url": url,
        "state": state,
        "instructions": "Copy the google_oauth_url and paste it in your browser to test the OAuth flow manually",
    }


@router.get("/google/login")
def google_login(request: Request, response: Response):
    user_agent = request.headers.get("user-agent", "").lower()
    referer = request.headers.get("referer", "")
    is_swagger_like = "swagger" in user_agent or "/docs" in referer

    # Swagger/Redoc often block or ignore 302 in-UI; return the URL instead
    if is_swagger_like:
        state = secrets.token_urlsafe(24)
        url = build_google_url(state)
        return {
            "message": "Copy this URL and open it in a new browser tab to complete Google OAuth",
            "google_oauth_url": url,
            "note": "Direct redirects don't work well in Swagger UI",
            "state": state,
        }

    return login_google(response)


@router.get("/google/callback")
def google_callback(
    request: Request,
    code: str | None = None,
    state: str | None = None,
    error: str | None = None,
    user_repo: UserRepository = Depends(get_user_repository),
):
    if error:
        raise HTTPException(status_code=400, detail=f"Google OAuth error: {error}")
    if not code or not state:
        raise HTTPException(status_code=400, detail="Missing authorization code or state parameter")

    return callback_google(request, code, state, user_repo)


@router.get("/me", response_model=UserSchema)
async def read_current_user(current_user: UserSchema = Depends(get_current_user)):
    return current_user
