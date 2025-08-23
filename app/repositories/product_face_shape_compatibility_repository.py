import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from app.schemas.product_face_shape_compatibility import ProductFaceShapeCompatibility, ProductFaceShapeCompatibilityCreate, ProductFaceShapeCompatibilityUpdate
from app.models.product_face_shape_compatibility import ProductFaceShapeCompatibilityModel

class ProductFaceShapeCompatibilityRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ProductFaceShapeCompatibility]:
        pass

    @abstractmethod
    def get_by_id(self, compatibility_id: uuid.UUID) -> Optional[ProductFaceShapeCompatibility]:
        pass

    @abstractmethod
    def create(self, compatibility_data: ProductFaceShapeCompatibilityCreate) -> ProductFaceShapeCompatibility:
        pass

    @abstractmethod
    def update(self, compatibility_id: uuid.UUID, compatibility_data: ProductFaceShapeCompatibilityUpdate) -> Optional[ProductFaceShapeCompatibility]:
        pass

    @abstractmethod
    def delete(self, compatibility_id: uuid.UUID) -> bool:
        pass

class ProductFaceShapeCompatibilityRepositoryImpl(ProductFaceShapeCompatibilityRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[ProductFaceShapeCompatibility]:
        return self.db.query(ProductFaceShapeCompatibilityModel).order_by(ProductFaceShapeCompatibilityModel.created_at.desc()).all()

    def get_by_id(self, compatibility_id: uuid.UUID) -> Optional[ProductFaceShapeCompatibility]:
        return self.db.query(ProductFaceShapeCompatibilityModel).filter(ProductFaceShapeCompatibilityModel.id == compatibility_id).first()

    def create(self, compatibility_data: ProductFaceShapeCompatibilityCreate) -> ProductFaceShapeCompatibility:
        db_compatibility = ProductFaceShapeCompatibilityModel(**compatibility_data.dict())
        self.db.add(db_compatibility)
        self.db.commit()
        self.db.refresh(db_compatibility)
        return db_compatibility

    def update(self, compatibility_id: uuid.UUID, compatibility_data: ProductFaceShapeCompatibilityUpdate) -> Optional[ProductFaceShapeCompatibility]:
        db_compatibility = self.db.query(ProductFaceShapeCompatibilityModel).filter(ProductFaceShapeCompatibilityModel.id == compatibility_id).first()
        if db_compatibility:
            update_data = compatibility_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_compatibility, key, value)
            self.db.commit()
            self.db.refresh(db_compatibility)
        return db_compatibility

    def delete(self, compatibility_id: uuid.UUID) -> bool:
        db_compatibility = self.db.query(ProductFaceShapeCompatibilityModel).filter(ProductFaceShapeCompatibilityModel.id == compatibility_id).first()
        if db_compatibility:
            self.db.delete(db_compatibility)
            self.db.commit()
            return True
        return False