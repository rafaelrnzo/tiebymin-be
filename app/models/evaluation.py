from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.db.base import Base

class AIModel(Base):
    """Model untuk menyimpan informasi model AI yang akan dievaluasi"""
    __tablename__ = "ai_models"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    version = Column(String(50), nullable=False)
    model_type = Column(String(100), nullable=False)
    is_baseline = Column(Boolean, default=False)
    is_fine_tuned = Column(Boolean, default=False)
    created_at = Column(DateTime)
    created_by = Column(String(100), default="SYSTEM")
    updated_at = Column(DateTime)
    updated_by = Column(String(100), default="SYSTEM")
    deleted_at = Column(DateTime)
    
    # Relationships
    generated_training_pairs = relationship("GeneratedTrainingPair", back_populates="model")

class TrainingPairSet(Base):
    """Training pair set sebagai parent table"""
    __tablename__ = "training_pair_sets"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pair_id = Column(String(20), unique=True, nullable=False)
    user_prompt = Column(Text)
    system_prompt = Column(Text)
    review_status = Column(String(50), default="QUEUE")  # QUEUE, REVIEWED, SKIPPED
    reviewed_at = Column(DateTime)
    reviewed_by = Column(String(100))
    created_at = Column(DateTime)
    created_by = Column(String(100), default="SYSTEM")
    updated_at = Column(DateTime)
    updated_by = Column(String(100), default="SYSTEM")
    deleted_at = Column(DateTime)
    
    # Relationships
    generated_training_pairs = relationship("GeneratedTrainingPair", back_populates="training_pair_set", cascade="all, delete-orphan")
    user_preferences = relationship("UserPreference", back_populates="training_pair_set", cascade="all, delete-orphan")

class GeneratedTrainingPair(Base):
    """Training pair yang dihasilkan oleh model"""
    __tablename__ = "generated_training_pairs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    training_pair_set_id = Column(UUID(as_uuid=True), ForeignKey("training_pair_sets.id", ondelete="CASCADE"))
    ai_model_id = Column(UUID(as_uuid=True), ForeignKey("ai_models.id", ondelete="CASCADE"))
    prompt = Column(Text, nullable=False)
    topic = Column(String(255))
    category = Column(String(255))
    duration_seconds = Column(Integer)
    score = Column(Integer)
    target_audience = Column(String(255))
    content_style = Column(String(255))
    created_at = Column(DateTime)
    created_by = Column(String(100), default="SYSTEM")
    updated_at = Column(DateTime)
    updated_by = Column(String(100), default="SYSTEM")
    deleted_at = Column(DateTime)
    
    # Relationships
    training_pair_set = relationship("TrainingPairSet", back_populates="generated_training_pairs")
    model = relationship("AIModel", back_populates="generated_training_pairs")
    generated_hook_variants = relationship("GeneratedHookVariant", back_populates="training_pair", cascade="all, delete-orphan")
    generated_scenes = relationship("GeneratedScene", back_populates="training_pair", cascade="all, delete-orphan")
    user_preferences = relationship("UserPreference", back_populates="selected_training_pair", cascade="all, delete-orphan")

class GeneratedHookVariant(Base):
    """Hook variant yang dihasilkan oleh model"""
    __tablename__ = "generated_hook_variants"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    training_pair_id = Column(UUID(as_uuid=True), ForeignKey("generated_training_pairs.id", ondelete="CASCADE"))
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
    
    # Relationships
    training_pair = relationship("GeneratedTrainingPair", back_populates="generated_hook_variants")

class GeneratedScene(Base):
    """Scene yang dihasilkan oleh model"""
    __tablename__ = "generated_scenes"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    training_pair_id = Column(UUID(as_uuid=True), ForeignKey("generated_training_pairs.id", ondelete="CASCADE"))
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
    
    # Relationships
    training_pair = relationship("GeneratedTrainingPair", back_populates="generated_scenes")

class UserPreference(Base):
    """Pilihan user untuk training pair mana yang lebih baik"""
    __tablename__ = "user_preferences"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"))
    training_pair_set_id = Column(UUID(as_uuid=True), ForeignKey("training_pair_sets.id", ondelete="CASCADE"))
    selected_training_pair_id = Column(UUID(as_uuid=True), ForeignKey("generated_training_pairs.id", ondelete="CASCADE"))
    preference_reason = Column(Text)
    created_at = Column(DateTime)
    created_by = Column(String(100), default="SYSTEM")
    updated_at = Column(DateTime)
    updated_by = Column(String(100), default="SYSTEM")
    deleted_at = Column(DateTime)
    
    # Relationships
    user = relationship("User", back_populates="user_preferences")
    training_pair_set = relationship("TrainingPairSet", back_populates="user_preferences")
    selected_training_pair = relationship("GeneratedTrainingPair", back_populates="user_preferences") 