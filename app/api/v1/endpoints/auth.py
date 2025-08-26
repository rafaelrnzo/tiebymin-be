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
    existing_user = user_repo.get_by_email(user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user_data.password)

    # Gunakan UserCreate, bukan UserRegistration
    user_to_create = UserCreate(
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        phone=user_data.phone,
        google_id=user_data.google_id,
        password_hash=hashed_password,
    )

    new_user = user_repo.create(user_to_create)
    return new_user


@router.post("/login")
async def login_user(user_login: UserLogin, user_repo: UserRepository = Depends(get_user_repository)):
    user = user_repo.get_by_email(user_login.email)
    if not user or not verify_password(user_login.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/google/login")
def google_login(response: Response):
    return login_google(response)

@router.get("/google/callback")
def google_callback(request: Request, code: str, state: str, user_repo: UserRepository = Depends(get_user_repository)):
    return callback_google(request, code, state, user_repo)

@router.get("/me", response_model=UserSchema)
async def read_current_user(current_user: UserSchema = Depends(get_current_user)):
    return current_user
