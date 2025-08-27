import uuid
from sqlalchemy import Column, DateTime, UUID, Text, Integer, Boolean, Numeric
from datetime import datetime
from app.db.session import Base

class PromoCodeModel(Base):
    __tablename__ = "promo_codes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(Text, unique=True, nullable=False)
    description = Column(Text, nullable=False)
    discount_type = Column(Text, nullable=False)
    discount_value = Column(Numeric, nullable=False)
    max_usage = Column(Integer, nullable=True)
    usage_per_user = Column(Integer, nullable=False, default=1)
    is_active = Column(Boolean, nullable=False, default=True)
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)