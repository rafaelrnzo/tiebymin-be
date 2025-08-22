from app.repositories.user import UserRepo
from app.core.security import verify_password, get_password_hash, create_access_token
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from datetime import timedelta, datetime, timezone
from app.core.config import settings

class AuthService:

    def __init__(self, db: AsyncSession):
        self.user = UserRepo(db)

    async def register_user(self, username: str, password: str, email: str, full_name: Optional[str] = None, team: Optional[str] = None) -> Optional[User]:
        # Check if username already exists
        existing = await self.user.get_by_username(username)
        if existing:
            return None
        hashed_password = get_password_hash(password)
        user = User(
            username=username,
            full_name=full_name,
            team=team,
            email=email,
            password=hashed_password
        )
        return await self.user.create(user)

    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Authenticate user with username and password."""
        user = await self.user.get_by_username(username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    async def create_access_token_for_user(self, user: User):
        """Create JWT access token for authenticated user and return token + expires_at."""
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.now(timezone.utc) + expires_delta
        token = create_access_token(subject=user.username, expires_delta=expires_delta)
        return token, expire.isoformat()

    async def login_for_access_token(self, username: str, password: str) -> Optional[dict]:
        """Authenticate user and return access token."""
        user = await self.authenticate_user(username, password)
        if not user:
            return None
        token, expires_at = await self.create_access_token_for_user(user)
        return {
            "access_token": token,
            "token_type": "bearer",
            "expires_at": expires_at,
            "user": user
        }

    async def get_user(self, user_id) -> Optional[User]:
        return await self.user.get_by_id(user_id)

    async def update_profile(self, user_id: str, profile_data: dict) -> Optional[User]:
        """Update user profile information."""
        return await self.user.update_profile(user_id, profile_data)

    async def change_password(self, user_id: str, current_password: str, new_password: str) -> Optional[User]:
        """Change user password with current password verification."""
        user = await self.user.get_by_id(user_id)
        if not user:
            return None
        
        # Verify current password
        if not verify_password(current_password, user.password):
            return None
        
        # Hash new password
        hashed_new_password = get_password_hash(new_password)
        
        # Update password
        return await self.user.update_password(user_id, hashed_new_password)

    async def reset_password_by_email(self, email: str, new_password: str) -> Optional[User]:
        """Reset password by email (for admin or forgot password functionality)."""
        user = await self.user.get_by_email(email)
        if not user:
            return None
        
        # Hash new password
        hashed_new_password = get_password_hash(new_password)
        
        # Update password
        return await self.user.update_password(str(user.id), hashed_new_password)
