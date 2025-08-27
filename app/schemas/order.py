import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class OrderBase(BaseModel):
    user_id: uuid.UUID
    analysis_result_id: Optional[uuid.UUID] = None
    status: str = Field(..., example="AWAITING_PAYMENT")
    original_amount: Decimal
    discount_amount: Decimal = Field(0)
    final_amount: Decimal

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    analysis_result_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    
class Order(OrderBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True