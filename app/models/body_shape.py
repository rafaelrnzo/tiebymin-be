import uuid
from sqlalchemy import Column, Boolean, DateTime, UUID, Text
from datetime import datetime
from app.db.session import Base

class BodyShapeModel(Base):
    __tablename__ = "body_shapes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, nullable=False)
    penjelasan_body_shape = Column(Text, nullable=False)
    karakteristik = Column(Text, nullable=False)
    tips_body_shape = Column(Text, nullable=False)
    link_picture = Column(Text, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)