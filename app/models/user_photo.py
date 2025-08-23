import uuid
from sqlalchemy import Column, Boolean, DateTime, UUID, Integer, Text, JSON
from datetime import datetime
from app.db.session import Base

class UserPhotoModel(Base):
    __tablename__ = "user_photos"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    analysis_result_id = Column(UUID(as_uuid=True), nullable=False)
    photo_type = Column(Text, nullable=False)
    file_path = Column(Text, nullable=False)
    original_filename = Column(Text, nullable=False)
    file_size = Column(Integer, nullable=False)
    mime_type = Column(Text, nullable=False)
    is_processed = Column(Boolean, nullable=False, default=False)
    analysis_metadata = Column(JSON, nullable=True)
    uploaded_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    processed_at = Column(DateTime(timezone=True), nullable=True)