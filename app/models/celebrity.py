import uuid
from sqlalchemy import Column, DateTime, UUID, Text
from datetime import datetime
from app.db.session import Base

class CelebrityModel(Base):
    __tablename__ = "celebrities"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, nullable=False)
    picture_url = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    similarity_text = Column(Text, nullable=False)
    faceshape_id = Column(UUID(as_uuid=True), nullable=True)
    color_analysis_id = Column(UUID(as_uuid=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)