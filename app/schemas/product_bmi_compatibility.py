import uuid
from pydantic import BaseModel, Field
from datetime import datetime

class ProductBmiCompatibilityBase(BaseModel):
    product_id: uuid.UUID
    bmi_category_id: uuid.UUID
    compatibility_score: int = Field(..., ge=1, le=10)
    compatibility_reason: str

class ProductBmiCompatibilityCreate(ProductBmiCompatibilityBase):
    pass

class ProductBmiCompatibility(ProductBmiCompatibilityBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        orm_mode = True