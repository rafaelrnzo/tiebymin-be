import uuid
from sqlalchemy import Column, DateTime, UUID, Text, Integer
from datetime import datetime
from app.db.session import Base

class AnalysisFeedbackModel(Base):
    __tablename__ = "analysis_feedback"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    analysis_result_id = Column(UUID(as_uuid=True), nullable=False)
    feedback_type = Column(Text, nullable=False)
    feedback_comment = Column(Text, nullable=True)
    user_rating = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)