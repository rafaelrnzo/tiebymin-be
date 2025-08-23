import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from app.schemas.product_body_shape_compatibility import ProductBodyShapeCompatibility, ProductBodyShapeCompatibilityCreate, ProductBodyShapeCompatibilityUpdate
from app.models.product_body_shape_compatibility import ProductBodyShapeCompatibilityModel

class ProductBodyShapeCompatibilityRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ProductBodyShapeCompatibility]:
        pass

    @abstractmethod
    def get_by_id(self, compatibility_id: uuid.UUID) -> Optional[ProductBodyShapeCompatibility]:
        pass

    @abstractmethod
    def create(self, compatibility_data: ProductBodyShapeCompatibilityCreate) -> ProductBodyShapeCompatibility:
        pass

    @abstractmethod
    def update(self, compatibility_id: uuid.UUID, compatibility_data: ProductBodyShapeCompatibilityUpdate) -> Optional[ProductBodyShapeCompatibility]:
        pass

    @abstractmethod
    def delete(self, compatibility_id: uuid.UUID) -> bool:
        pass

class ProductBodyShapeCompatibilityRepositoryImpl(ProductBodyShapeCompatibilityRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[ProductBodyShapeCompatibility]:
        return self.db.query(ProductBodyShapeCompatibilityModel).order_by(ProductBodyShapeCompatibilityModel.created_at.desc()).all()

    def get_by_id(self, compatibility_id: uuid.UUID) -> Optional[ProductBodyShapeCompatibility]:
        return self.db.query(ProductBodyShapeCompatibilityModel).filter(ProductBodyShapeCompatibilityModel.id == compatibility_id).first()

    def create(self, compatibility_data: ProductBodyShapeCompatibilityCreate) -> ProductBodyShapeCompatibility:
        db_compatibility = ProductBodyShapeCompatibilityModel(**compatibility_data.dict())
        self.db.add(db_compatibility)
        self.db.commit()
        self.db.refresh(db_compatibility)
        return db_compatibility

    def update(self, compatibility_id: uuid.UUID, compatibility_data: ProductBodyShapeCompatibilityUpdate) -> Optional[ProductBodyShapeCompatibility]:
        db_compatibility = self.db.query(ProductBodyShapeCompatibilityModel).filter(ProductBodyShapeCompatibilityModel.id == compatibility_id).first()
        if db_compatibility:
            update_data = compatibility_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_compatibility, key, value)
            self.db.commit()
            self.db.refresh(db_compatibility)
        return db_compatibility

    def delete(self, compatibility_id: uuid.UUID) -> bool:
        db_compatibility = self.db.query(ProductBodyShapeCompatibilityModel).filter(ProductBodyShapeCompatibilityModel.id == compatibility_id).first()
        if db_compatibility:
            self.db.delete(db_compatibility)
            self.db.commit()
            return True
        return False