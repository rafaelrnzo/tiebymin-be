from typing import Optional
from fastapi import APIRouter, Depends, Request, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr
from fastapi.responses import RedirectResponse, JSONResponse
from urllib.parse import urlencode
import httpx

from app.repositories.user_repository import UserRepository
from app.dependencies.dependencies import get_user_repository
from app.schemas.user import User as UserSchema, UserLogin, UserCreate
from app.services.auth.token_service import get_current_user, create_access_token
from app.services.auth.google_service import login_google, callback_google
from app.utils.password_utils import verify_password, get_password_hash
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["Authentication"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")


class UserRegistrationOptional(BaseModel):
    email: EmailStr
    first_name: str
    last_name: Optional[str] = None
    password: str
    phone: Optional[str] = None


@router.post("/register")
def register_user(
    user_data: UserRegistrationOptional,
    user_repo: UserRepository = Depends(get_user_repository),
):
    existing_user = user_repo.get_by_email(user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user_data.password)

    user_to_create = UserCreate(
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name or "",
        phone=user_data.phone,
        google_id=None,
        password_hash=hashed_password,
    )

    new_user = user_repo.create(user_to_create)
    token = create_access_token({"sub": str(new_user.id)})

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": new_user.id,
            "email": new_user.email,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
        },
    }

@router.get("/google/login", tags=["Auth"])
async def google_login():

    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": settings.google_redirect(),
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent",
    }
    google_auth_url = f"https://accounts.google.com/o/oauth2/auth?{urlencode(params)}"
    return RedirectResponse(url=google_auth_url)


@router.get("/google/callback", tags=["Auth"])
async def google_callback(request: Request, code: str, state: str = None):

    token_url = "https://oauth2.googleapis.com/token"
    userinfo_url = "https://www.googleapis.com/oauth2/v3/userinfo"

    async with httpx.AsyncClient() as client:
        token_data = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.google_redirect(),
            "grant_type": "authorization_code",
        }
        token_resp = await client.post(token_url, data=token_data)
        token_json = token_resp.json()

        if "error" in token_json:
            return JSONResponse(token_json, status_code=400)

        access_token = token_json.get("access_token")

        headers = {"Authorization": f"Bearer {access_token}"}
        userinfo_resp = await client.get(userinfo_url, headers=headers)
        userinfo = userinfo_resp.json()

    return {
        "access_token": access_token,
        "user": userinfo,
    }