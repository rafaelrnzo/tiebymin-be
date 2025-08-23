import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from app.schemas.product_color import ProductColor, ProductColorCreate, ProductColorUpdate
from app.models.product_color import ProductColorModel

class ProductColorRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ProductColor]:
        pass

    @abstractmethod
    def get_by_id(self, color_id: uuid.UUID) -> Optional[ProductColor]:
        pass

    @abstractmethod
    def create(self, color_data: ProductColorCreate) -> ProductColor:
        pass

    @abstractmethod
    def update(self, color_id: uuid.UUID, color_data: ProductColorUpdate) -> Optional[ProductColor]:
        pass

    @abstractmethod
    def delete(self, color_id: uuid.UUID) -> bool:
        pass

class ProductColorRepositoryImpl(ProductColorRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[ProductColor]:
        return self.db.query(ProductColorModel).order_by(ProductColorModel.color_name).all()

    def get_by_id(self, color_id: uuid.UUID) -> Optional[ProductColor]:
        return self.db.query(ProductColorModel).filter(ProductColorModel.id == color_id).first()

    def create(self, color_data: ProductColorCreate) -> ProductColor:
        db_color = ProductColorModel(**color_data.dict())
        self.db.add(db_color)
        self.db.commit()
        self.db.refresh(db_color)
        return db_color

    def update(self, color_id: uuid.UUID, color_data: ProductColorUpdate) -> Optional[ProductColor]:
        db_color = self.db.query(ProductColorModel).filter(ProductColorModel.id == color_id).first()
        if db_color:
            update_data = color_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_color, key, value)
            self.db.commit()
            self.db.refresh(db_color)
        return db_color

    def delete(self, color_id: uuid.UUID) -> bool:
        db_color = self.db.query(ProductColorModel).filter(ProductColorModel.id == color_id).first()
        if db_color:
            self.db.delete(db_color)
            self.db.commit()
            return True
        return False