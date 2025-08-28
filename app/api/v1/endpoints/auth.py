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

@router.post("/register")
def register_user(
    user_data: UserRegistration,
    user_repo: UserRepository = Depends(get_user_repository),
):
    """Register a new user and return access token"""
    existing_user = user_repo.get_by_email(user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user_data.password)

    user_to_create = UserCreate(
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=getattr(user_data, 'last_name', None),
        phone=getattr(user_data, 'phone', None),
        google_id=getattr(user_data, 'google_id', None),
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
            "last_name": new_user.last_name
        }
    }

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

@router.get("/google/login")
def google_login(request: Request, response: Response):
    """Initiate Google OAuth login"""
    user_agent = request.headers.get("user-agent", "").lower()
    
    if "swagger" in user_agent or request.headers.get("accept") == "application/json":
        return login_google(response, return_url=True)
    else:
        return login_google(response, return_url=False)

@router.get("/google/callback")
def google_callback(
    request: Request, 
    code: str = None,
    state: str = None,
    error: str = None,
    user_repo: UserRepository = Depends(get_user_repository)
):
    """Handle Google OAuth callback"""
    if error:
        raise HTTPException(status_code=400, detail=f"Google OAuth error: {error}")
    
    if not code or not state:
        raise HTTPException(status_code=400, detail="Missing authorization code or state parameter")
    
    return callback_google(request, code, state, user_repo)

@router.get("/me", response_model=UserSchema)
async def read_current_user(current_user: UserSchema = Depends(get_current_user)):
    """Get current authenticated user"""
    return current_user