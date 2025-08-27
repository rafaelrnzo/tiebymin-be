import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from app.schemas.product import Product, ProductCreate, ProductUpdate
from app.models.product import ProductModel

class ProductRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, product_id: uuid.UUID) -> Optional[Product]:
        pass

    @abstractmethod
    def create(self, product_data: ProductCreate) -> Product:
        pass

    @abstractmethod
    def update(self, product_id: uuid.UUID, product_data: ProductUpdate) -> Optional[Product]:
        pass

    @abstractmethod
    def delete(self, product_id: uuid.UUID) -> bool:
        pass

class ProductRepositoryImpl(ProductRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[Product]:
        return self.db.query(ProductModel).order_by(ProductModel.name).all()

    def get_by_id(self, product_id: uuid.UUID) -> Optional[Product]:
        return self.db.query(ProductModel).filter(ProductModel.id == product_id).first()

    def create(self, product_data: ProductCreate) -> Product:
        db_product = ProductModel(**product_data.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def update(self, product_id: uuid.UUID, product_data: ProductUpdate) -> Optional[Product]:
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if db_product:
            update_data = product_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_product, key, value)
            self.db.commit()
            self.db.refresh(db_product)
        return db_product

    def delete(self, product_id: uuid.UUID) -> bool:
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if db_product:
            self.db.delete(db_product)
            self.db.commit()
            return True
        return False