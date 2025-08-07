from sqlalchemy import Column, ForeignKey, Boolean, TIMESTAMP, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.postgres_db import Base

class UserAnalysisResult(Base):
    __tablename__ = "user_analysis_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    face_shape_id = Column(UUID(as_uuid=True), ForeignKey("face_shapes.id"), nullable=True)
    body_shape_id = Column(UUID(as_uuid=True), ForeignKey("body_shapes.id"), nullable=True)
    color_analysis_id = Column(UUID(as_uuid=True), ForeignKey("color_analysis.id"), nullable=True)
    
    analysis_details = Column(JSON, nullable=True, comment='detailed AI results')
    is_final_result = Column(Boolean, nullable=False, default=False)
    analyzed_at = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)