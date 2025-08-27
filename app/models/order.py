import uuid
from sqlalchemy import Column, DateTime, UUID, Text, Numeric
from datetime import datetime
from app.db.session import Base

class OrderModel(Base):
    __tablename__ = "orders"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    analysis_result_id = Column(UUID(as_uuid=True), nullable=True)
    status = Column(Text, nullable=False, default="AWAITING_PAYMENT")
    original_amount = Column(Numeric(10, 2), nullable=False)
    discount_amount = Column(Numeric(10, 2), nullable=False, default=0)
    final_amount = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)