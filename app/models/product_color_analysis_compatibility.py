import uuid
from sqlalchemy import Column, DateTime, UUID, Text, Integer
from datetime import datetime
from app.db.session import Base

class ProductColorAnalysisCompatibilityModel(Base):
    __tablename__ = "product_color_analysis_compatibility"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_color_id = Column(UUID(as_uuid=True), nullable=False)
    color_analysis_id = Column(UUID(as_uuid=True), nullable=False)
    compatibility_score = Column(Integer, nullable=False)
    compatibility_reason = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)