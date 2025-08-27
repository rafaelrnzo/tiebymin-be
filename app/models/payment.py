import uuid
from sqlalchemy import Column, DateTime, UUID, Text, Numeric, JSON
from datetime import datetime
from app.db.session import Base

class PaymentModel(Base):
    __tablename__ = "payments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), nullable=False)
    payment_gateway = Column(Text, nullable=False)
    gateway_transaction_id = Column(Text, unique=True, nullable=False)
    status = Column(Text, nullable=False)
    amount = Column(Numeric, nullable=False)
    payment_details = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    paid_at = Column(DateTime(timezone=True), nullable=True)