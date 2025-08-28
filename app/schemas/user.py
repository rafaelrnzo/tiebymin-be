import uuid
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr = Field(..., example="jane.doe@example.com")
    first_name: str = Field(..., example="Jane")
    last_name: Optional[str] = Field(None, example="Doe")
    phone: Optional[str] = Field(None, example="081234567890")
    google_id: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRegistration(UserBase):
    password: str = Field(..., min_length=8)

class UserCreate(UserBase):
    password_hash: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: uuid.UUID
    email_verified_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        orm_mode = True