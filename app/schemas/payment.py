import uuid
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from decimal import Decimal

class PaymentBase(BaseModel):
    order_id: uuid.UUID
    payment_gateway: str = Field(..., example="midtrans")
    gateway_transaction_id: str
    status: str = Field(..., example="PENDING")
    amount: Decimal
    payment_details: Optional[Dict[str, Any]] = None

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    status: Optional[str] = None
    paid_at: Optional[datetime] = None

class Payment(PaymentBase):
    id: uuid.UUID
    created_at: datetime
    paid_at: Optional[datetime] = None

    class Config:
        orm_mode = True