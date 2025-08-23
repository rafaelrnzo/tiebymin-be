import uuid
from sqlalchemy import Column, DateTime, UUID, Text, Integer, Boolean
from datetime import datetime
from app.db.session import Base

class ProductColorModel(Base):
    __tablename__ = "product_colors"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), nullable=False)
    color_name = Column(Text, nullable=False)
    hex_color = Column(Text, nullable=False)
    color_image_url = Column(Text, nullable=True)
    is_available = Column(Boolean, nullable=False, default=True)
    stock_quantity = Column(Integer, nullable=False, default=0)