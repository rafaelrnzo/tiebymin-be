import uuid
from pydantic import BaseModel, Field
from datetime import datetime

class ProductBodyShapeCompatibilityBase(BaseModel):
    product_id: uuid.UUID
    body_shape_id: uuid.UUID
    compatibility_score: int = Field(..., ge=1, le=10)
    compatibility_reason: str

class ProductBodyShapeCompatibilityCreate(ProductBodyShapeCompatibilityBase):
    pass

class ProductBodyShapeCompatibilityUpdate(BaseModel):
    product_id: uuid.UUID | None = None
    body_shape_id: uuid.UUID | None = None
    compatibility_score: int | None = Field(None, ge=1, le=10)
    compatibility_reason: str | None = None

class ProductBodyShapeCompatibility(ProductBodyShapeCompatibilityBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        orm_mode = True