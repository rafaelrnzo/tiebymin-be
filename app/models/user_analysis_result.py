import uuid
from sqlalchemy import Column, Boolean, DateTime, UUID, JSON
from datetime import datetime
from app.db.session import Base

class UserAnalysisResultModel(Base):
    __tablename__ = "user_analysis_results"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    face_shape_id = Column(UUID(as_uuid=True), nullable=True)
    body_shape_id = Column(UUID(as_uuid=True), nullable=True)
    color_analysis_id = Column(UUID(as_uuid=True), nullable=True)
    bmi_category_id = Column(UUID(as_uuid=True), nullable=True)
    celebrity_id = Column(UUID(as_uuid=True), nullable=True)
    analysis_details = Column(JSON, nullable=True)
    is_final_result = Column(Boolean, nullable=False, default=False)
    analyzed_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)