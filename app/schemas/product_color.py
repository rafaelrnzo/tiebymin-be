import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductColorBase(BaseModel):
    product_id: uuid.UUID
    color_name: str = Field(..., example="Midnight Blue")
    hex_color: str = Field(..., example="#003366")
    color_image_url: Optional[str] = Field(None, example="https://example.com/blue-shirt.jpg")
    is_available: bool = Field(True)
    stock_quantity: int = Field(0)

class ProductColorCreate(ProductColorBase):
    pass

class ProductColor(ProductColorBase):
    id: uuid.UUID

    class Config:
        orm_mode = True