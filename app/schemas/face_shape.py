import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FaceShapeBase(BaseModel):
    name: str = Field(..., example="Oval")
    penjelasan_face_shape: str = Field(..., example="Considered the ideal face shape.")
    karakteristik: str = Field(..., example="Forehead is slightly wider than the chin.")
    tips_bentuk_wajah: str = Field(..., example="Most hairstyles work well with this shape.")
    illustration_url: Optional[str] = None
    is_active: bool = Field(True)

class FaceShapeCreate(FaceShapeBase):
    pass

class FaceShapeUpdate(BaseModel):
    name: Optional[str] = None
    penjelasan_face_shape: Optional[str] = None
    karakteristik: Optional[str] = None
    tips_bentuk_wajah: Optional[str] = None
    illustration_url: Optional[str] = None
    is_active: Optional[bool] = None

class FaceShape(FaceShapeBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True