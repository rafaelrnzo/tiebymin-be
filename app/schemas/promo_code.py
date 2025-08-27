import uuid
from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime
from decimal import Decimal

class PromoCodeBase(BaseModel):
    code: str = Field(..., example="HEMAT2025")
    description: str = Field(..., example="Discount for new year.")
    discount_type: Literal["PERCENTAGE", "FIXED_AMOUNT"]
    discount_value: Decimal
    max_usage: Optional[int] = None
    usage_per_user: int = Field(1)
    is_active: bool = Field(True)
    start_date: datetime
    end_date: datetime

class PromoCodeCreate(PromoCodeBase):
    pass

class PromoCodeUpdate(BaseModel):
    description: Optional[str] = None
    discount_type: Optional[Literal["PERCENTAGE", "FIXED_AMOUNT"]] = None
    discount_value: Optional[Decimal] = None
    max_usage: Optional[int] = None
    usage_per_user: Optional[int] = None
    is_active: Optional[bool] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class PromoCode(PromoCodeBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True