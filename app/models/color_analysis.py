import uuid
from sqlalchemy import Column, Boolean, DateTime, UUID, Text, JSON
from datetime import datetime
from app.db.session import Base

class ColorAnalysisModel(Base):
    __tablename__ = "color_analysis"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, nullable=False)
    penjelasan_color_analysis = Column(Text, nullable=False)
    make_up_tips = Column(Text, nullable=False)
    tips_warna_kulit_pakaian = Column(Text, nullable=False)
    best_colour = Column(JSON, nullable=False)
    worst_colour = Column(JSON, nullable=False)
    neutral_colour = Column(JSON, nullable=False)
    best_colour_combination = Column(JSON, nullable=False)
    personality = Column(Text, nullable=False)
    karakteristik = Column(Text, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    color_tips_summary = Column(Text, nullable=True)