import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BodyShapeBase(BaseModel):
    name: str = Field(..., example="Apple")
    penjelasan_body_shape: str = Field(..., example="Characterized by a larger upper body and narrower hips.")
    karakteristik: str = Field(..., example="Broad shoulders, full bust, and narrow hips.")
    tips_body_shape: str = Field(..., example="Wear A-line dresses to balance proportions.")
    link_picture: str = Field(..., example="https://example.com/apple-body-shape.jpg")
    is_active: bool = Field(True)

class BodyShapeCreate(BodyShapeBase):
    pass

class BodyShapeUpdate(BaseModel):
    name: Optional[str] = None
    penjelasan_body_shape: Optional[str] = None
    karakteristik: Optional[str] = None
    tips_body_shape: Optional[str] = None
    link_picture: Optional[str] = None
    is_active: Optional[bool] = None

class BodyShape(BodyShapeBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True