from sqlalchemy import Column, String, DateTime, Text, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    full_name = Column(String(100))
    team = Column(String(100))
    password = Column(Text, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime)
    created_by = Column(String(100), default="SYSTEM")
    updated_at = Column(DateTime)
    updated_by = Column(String(100), default="SYSTEM")
    deleted_at = Column(DateTime)
    # Relationship to review actions
    review_actions = relationship("ReviewAction", back_populates="user", cascade="all, delete-orphan", lazy="joined")
    # Relationship to user preferences for evaluation
    user_preferences = relationship("UserPreference", back_populates="user", cascade="all, delete-orphan", lazy="joined")

class ReviewAction(Base):
    __tablename__ = "review_actions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    training_pair_id = Column(UUID(as_uuid=True), ForeignKey("training_pairs.id", ondelete="CASCADE"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"))
    action = Column(String(20), CheckConstraint("action IN ('APPROVED', 'REJECTED', 'SKIPPED', 'QUEUE')"))
    notes = Column(Text)
    created_at = Column(DateTime)
    created_by = Column(String(100), default="SYSTEM")
    updated_at = Column(DateTime)
    updated_by = Column(String(100), default="SYSTEM")
    deleted_at = Column(DateTime)
    training_pair = relationship("TrainingPair", back_populates="review_actions", lazy="joined")
    user = relationship("User", back_populates="review_actions", lazy="joined")
