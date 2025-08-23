import uuid
from sqlalchemy import Column, DateTime, UUID, Text, Integer
from datetime import datetime
from app.db.session import Base

class ProductBmiCompatibilityModel(Base):
    __tablename__ = "product_bmi_compatibility"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), nullable=False)
    bmi_category_id = Column(UUID(as_uuid=True), nullable=False)
    compatibility_score = Column(Integer, nullable=False)
    compatibility_reason = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)