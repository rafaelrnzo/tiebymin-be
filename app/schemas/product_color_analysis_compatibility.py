import uuid
from pydantic import BaseModel, Field
from datetime import datetime

class ProductColorAnalysisCompatibilityBase(BaseModel):
    product_color_id: uuid.UUID
    color_analysis_id: uuid.UUID
    compatibility_score: int = Field(..., ge=1, le=10)
    compatibility_reason: str

class ProductColorAnalysisCompatibilityCreate(ProductColorAnalysisCompatibilityBase):
    pass

class ProductColorAnalysisCompatibility(ProductColorAnalysisCompatibilityBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        orm_mode = True