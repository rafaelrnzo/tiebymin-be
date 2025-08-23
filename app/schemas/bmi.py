import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BMICategoryBase(BaseModel):
    kategori: str = Field(..., example="Normal")
    min_bmi: float
    max_bmi: Optional[float] = None
    tips_fashion: str
    is_active: bool = Field(True)
    bmi_tips_summary: Optional[str] = None

class BMICategoryCreate(BMICategoryBase):
    pass

class BMICategoryUpdate(BaseModel):
    kategori: Optional[str] = None
    min_bmi: Optional[float] = None
    max_bmi: Optional[float] = None
    tips_fashion: Optional[str] = None
    is_active: Optional[bool] = None
    bmi_tips_summary: Optional[str] = None

class BMICategory(BMICategoryBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True