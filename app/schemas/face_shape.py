import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FaceShapeBase(BaseModel):
    name: str = Field(..., example="Oval")
    penjelasan_face_shape: str = Field(..., example="Considered the ideal face shape.")
    karakteristik: str = Field(..., example="Forehead is slightly wider than the chin.")
    tips_bentuk_wajah: str = Field(..., example="Most hairstyles work well with this shape.")
    illustration_url: Optional[str] = Field(None, example="https://example.com/oval.jpg")
    is_active: bool = Field(True)
    face_tips_summary: Optional[str] = Field(None, example="Choose hairstyles that highlight your cheekbones.")
    
class FaceShapeCreate(FaceShapeBase):
    pass

class FaceShape(FaceShapeBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True