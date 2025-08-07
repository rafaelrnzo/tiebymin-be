from sqlalchemy import Column, String, Boolean, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.db.db import Base  # pastikan Base diimpor dari deklarasi declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    google_id = Column(String, unique=True, nullable=True, comment='nullable for non-Google users')
    password_hash = Column(String, nullable=True, comment='nullable for Google users')
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    profile_picture_url = Column(String, nullable=True)
    email_verified_at = Column(TIMESTAMP, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, nullable=False, default=True)
