import uuid
from pydantic import BaseModel, Field, EmailStr
from typing import List
from datetime import datetime

class UserInfo(BaseModel):
    user_id: uuid.UUID
    user_full_name: str
    user_first_name: str

class AnalysisHistoryItem(BaseModel):
    analysis_id: uuid.UUID
    analysis_date: str

class PaginatedAnalysisHistory(BaseModel):
    total_items: int
    items: List[AnalysisHistoryItem]
    limit: int
    skip: int

class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str = Field(..., min_length=8)