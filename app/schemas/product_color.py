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

class ProductColorUpdate(BaseModel):
    product_id: Optional[uuid.UUID] = None
    color_name: Optional[str] = None
    hex_color: Optional[str] = None
    color_image_url: Optional[str] = None
    is_available: Optional[bool] = None
    stock_quantity: Optional[int] = None

class ProductColor(ProductColorBase):
    id: uuid.UUID

    class Config:
        orm_mode = True