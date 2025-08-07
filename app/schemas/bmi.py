import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BMICategoryBase(BaseModel):
    kategori: str = Field(..., example="Normal", description="Nama kategori BMI.")
    min_bmi: float = Field(..., example=18.5, description="Nilai BMI minimum untuk kategori ini.")
    max_bmi: Optional[float] = Field(None, example=24.9, description="Nilai BMI maksimum, bisa kosong untuk kategori teratas.")
    tips_fashion: str = Field(..., example="Kenakan pakaian yang pas di badan untuk menonjolkan siluet.", description="Saran fashion untuk kategori BMI ini.")
    is_active: bool = Field(True, description="Menandakan apakah kategori ini aktif dan digunakan.")

class BMICategoryCreate(BMICategoryBase):
    pass

class BMICategory(BMICategoryBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True