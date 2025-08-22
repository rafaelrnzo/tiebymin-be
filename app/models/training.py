from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.db.base import Base

class TrainingPair(Base):
    __tablename__ = "training_pairs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pair_id = Column(String(20), unique=True, nullable=False)
    topic = Column(String(255))
    category = Column(String(255))
    duration_seconds = Column(Integer)
    score = Column(Integer)
    user_prompt = Column(Text)
    system_prompt = Column(Text)
    target_audience = Column(String(255))
    content_style = Column(String(255))
    status = Column(String(20), default="queue")
    created_at = Column(DateTime)
    created_by = Column(String(100), default="SYSTEM")
    updated_at = Column(DateTime)
    updated_by = Column(String(100), default="SYSTEM")
    deleted_at = Column(DateTime)
    hashtags = relationship("TrainingPairHashtag", back_populates="training_pair", cascade="all, delete-orphan", lazy="joined")
    hook_variants = relationship("HookVariant", back_populates="training_pair", cascade="all, delete-orphan", lazy="joined")
    scenes = relationship("Scene", back_populates="training_pair", cascade="all, delete-orphan", lazy="joined")
    review_actions = relationship("ReviewAction", back_populates="training_pair", cascade="all, delete-orphan", lazy="joined")

class TrainingPairHashtag(Base):
    __tablename__ = "training_pair_hashtags"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    training_pair_id = Column(UUID(as_uuid=True), ForeignKey("training_pairs.id", ondelete="CASCADE"))
    hashtag = Column(String(100), nullable=False)  # Store hashtag as string directly
    created_at = Column(DateTime)
    created_by = Column(String(100), default="SYSTEM")
    updated_at = Column(DateTime)
    updated_by = Column(String(100), default="SYSTEM")
    deleted_at = Column(DateTime)
    training_pair = relationship("TrainingPair", back_populates="hashtags", lazy="joined")

class HookVariant(Base):
    __tablename__ = "hook_variants"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    training_pair_id = Column(UUID(as_uuid=True), ForeignKey("training_pairs.id", ondelete="CASCADE"))
    hook_variant = Column(Integer)
    scene_number = Column(Integer)
    scene_type = Column(String(100))
    timestamp = Column(String(50))
    text_overlay = Column(Text)
    voiceover = Column(Text)
    visual = Column(Text)
    tip = Column(Text)
    order_index = Column(Integer)
    created_at = Column(DateTime)
    created_by = Column(String(100), default="SYSTEM")
    updated_at = Column(DateTime)
    updated_by = Column(String(100), default="SYSTEM")
    deleted_at = Column(DateTime)
    training_pair = relationship("TrainingPair", back_populates="hook_variants", lazy="joined")

class Scene(Base):
    __tablename__ = "scenes"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    training_pair_id = Column(UUID(as_uuid=True), ForeignKey("training_pairs.id", ondelete="CASCADE"))
    scene_number = Column(Integer)
    scene_type = Column(String(100))
    timestamp = Column(String(50))
    text_overlay = Column(Text)
    voiceover = Column(Text)
    visual = Column(Text)
    tip = Column(Text)
    order_index = Column(Integer)
    created_at = Column(DateTime)
    created_by = Column(String(100), default="SYSTEM")
    updated_at = Column(DateTime)
    updated_by = Column(String(100), default="SYSTEM")
    deleted_at = Column(DateTime)
    training_pair = relationship("TrainingPair", back_populates="scenes", lazy="joined")
