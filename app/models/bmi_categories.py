import uuid
from sqlalchemy import Column, Boolean, DateTime, UUID, Text, Numeric
from datetime import datetime
from app.db.session import Base

class BMICategoryModel(Base):
    __tablename__ = "bmi_categories"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    kategori = Column(Text, nullable=False)
    min_bmi = Column(Numeric(4, 2), nullable=False)
    max_bmi = Column(Numeric(4, 2), nullable=True)
    tips_fashion = Column(Text, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    bmi_tips_summary = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)