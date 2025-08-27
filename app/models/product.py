import uuid
from sqlalchemy import Column, Boolean, DateTime, UUID, Integer, Text, Numeric, JSON
from datetime import datetime
from app.db.session import Base

class ProductModel(Base):
    __tablename__ = "products"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    original_price = Column(Numeric(10, 2), nullable=False)
    current_price = Column(Numeric(10, 2), nullable=False)
    discount_percentage = Column(Numeric(5, 2), nullable=True)
    average_rating = Column(Numeric(3, 2), nullable=False, default=0)
    total_reviews = Column(Integer, nullable=False, default=0)
    size_range = Column(Text, nullable=False)
    brand = Column(Text, nullable=True)
    category = Column(Text, nullable=False)
    product_link = Column(Text, nullable=False)
    images = Column(JSON, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    stock_quantity = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)