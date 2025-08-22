from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    username: str
    full_name: Optional[str] = None
    email: str
    team: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(UserBase):
    pass

class ProfileUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    team: Optional[str] = None

class PasswordReset(BaseModel):
    current_password: str
    new_password: str

class PasswordResetRequest(BaseModel):
    email: EmailStr

class UserOut(UserBase):
    id: UUID
    created_at: Optional[datetime]
    created_by: Optional[str]
    updated_at: Optional[datetime]
    updated_by: Optional[str]
    # Review statistics
    total_reviewed: Optional[int] = 0
    total_approved: Optional[int] = 0
    total_rejected: Optional[int] = 0
    contribution_percent: Optional[int] = 0

    class Config:
        from_attributes = True

class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserOut
