import uuid
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ProductBase(BaseModel):
    name: str = Field(..., example="Classic White T-Shirt")
    description: str = Field(..., example="A high-quality cotton t-shirt.")
    original_price: float
    current_price: float
    discount_percentage: Optional[float] = None
    average_rating: float = Field(0)
    total_reviews: int = Field(0)
    size_range: str = Field(..., example="S, M, L, XL")
    brand: Optional[str] = Field(None, example="FashionBrand")
    category: str = Field(..., example="Tops")
    product_link: str = Field(..., example="https://example.com/product/123")
    images: List[str] = Field(..., example=["https://example.com/img1.jpg", "https://example.com/img2.jpg"])
    is_active: bool = Field(True)
    stock_quantity: int = Field(0)
    
class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    original_price: Optional[float] = None
    current_price: Optional[float] = None
    discount_percentage: Optional[float] = None
    average_rating: Optional[float] = None
    total_reviews: Optional[int] = None
    size_range: Optional[str] = None
    brand: Optional[str] = None
    category: Optional[str] = None
    product_link: Optional[str] = None
    images: Optional[List[str]] = None
    is_active: Optional[bool] = None
    stock_quantity: Optional[int] = None

class Product(ProductBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True