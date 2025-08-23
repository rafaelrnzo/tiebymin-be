import uuid
from pydantic import BaseModel, Field
from datetime import datetime

class ProductFaceShapeCompatibilityBase(BaseModel):
    product_id: uuid.UUID
    face_shape_id: uuid.UUID
    compatibility_score: int = Field(..., ge=1, le=10)
    compatibility_reason: str

class ProductFaceShapeCompatibilityCreate(ProductFaceShapeCompatibilityBase):
    pass

class ProductFaceShapeCompatibilityUpdate(BaseModel):
    product_id: uuid.UUID | None = None
    face_shape_id: uuid.UUID | None = None
    compatibility_score: int | None = Field(None, ge=1, le=10)
    compatibility_reason: str | None = None

class ProductFaceShapeCompatibility(ProductFaceShapeCompatibilityBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        orm_mode = True