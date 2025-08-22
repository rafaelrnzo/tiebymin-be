from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from app.models.user import User
from typing import Optional
from datetime import datetime
from app.core.security import verify_password

class UserRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, user_id) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.id == user_id, User.deleted_at == None))
        return result.unique().scalar_one_or_none()

    async def get_by_username(self, username: str) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.username == username, User.deleted_at == None))
        user = result.unique().scalar_one_or_none()
        return user

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.email == email, User.deleted_at == None))
        user = result.unique().scalar_one_or_none()
        return user

    async def create(self, user: User) -> User:
        # Set timestamps if not provided
        if not user.created_at:
            user.created_at = datetime.utcnow()
        if not user.updated_at:
            user.updated_at = datetime.utcnow()
        
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update_profile(self, user_id: str, update_data: dict) -> Optional[User]:
        """Update user profile information."""
        result = await self.db.execute(select(User).where(User.id == user_id, User.deleted_at == None))
        user = result.unique().scalar_one_or_none()
        if not user:
            return None
        
        # Update fields
        for field, value in update_data.items():
            if value is not None:
                setattr(user, field, value)
        
        user.updated_at = datetime.utcnow()
        user.updated_by = user.username
        
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update_password(self, user_id: str, hashed_password: str) -> Optional[User]:
        """Update user password."""
        result = await self.db.execute(select(User).where(User.id == user_id, User.deleted_at == None))
        user = result.unique().scalar_one_or_none()
        if not user:
            return None
        
        user.password = hashed_password
        user.updated_at = datetime.utcnow()
        user.updated_by = user.username
        
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def authenticate(self, username: str, password: str) -> Optional[User]:
        """Authenticate user with username and plain password."""
        user = await self.get_by_username(username)
        if user and verify_password(password, user.password):
            return user
        return None
