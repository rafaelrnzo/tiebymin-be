# app/routers/auth.py
from typing import Optional
from fastapi import APIRouter, Depends, Request, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr

from app.repositories.user_repository import UserRepository
from app.dependencies.dependencies import get_user_repository
from app.schemas.user import User as UserSchema, UserLogin, UserCreate
from app.services.auth.token_service import get_current_user, create_access_token
from app.utils.password_utils import verify_password, get_password_hash
from app.core.config import settings

# Import the stateless version
from app.services.auth.google_service_stateless import (
    login_google_stateless as login_google, 
    callback_google_stateless as callback_google
)

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

@router.get("/google/login")
def google_login(request: Request, response: Response):
    ua = request.headers.get("user-agent", "").lower()
    accept = request.headers.get("accept", "").lower()
    is_swagger_like = "swagger" in ua or "application/json" in accept

    return login_google(request, response, return_url=is_swagger_like)

@router.get("/google/callback", name="callback_google")
def google_callback(
    request: Request,
    code: Optional[str] = None,
    state: Optional[str] = None,
    error: Optional[str] = None,
    user_repo: UserRepository = Depends(get_user_repository),
):
    if error:
        raise HTTPException(status_code=400, detail=f"Google OAuth error: {error}")
    if not code:
        raise HTTPException(status_code=400, detail="Missing authorization code")

    return callback_google(request, code, user_repo)

@router.get("/me", response_model=UserSchema)
async def read_current_user(current_user: UserSchema = Depends(get_current_user)):
    return current_user