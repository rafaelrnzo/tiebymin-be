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

class ProductBodyShapeCompatibility(ProductBodyShapeCompatibilityBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        orm_mode = True