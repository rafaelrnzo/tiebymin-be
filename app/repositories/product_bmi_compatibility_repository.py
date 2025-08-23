import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from app.schemas.product_bmi_compatibility import ProductBmiCompatibility, ProductBmiCompatibilityCreate, ProductBmiCompatibilityUpdate
from app.models.product_bmi_compatibility import ProductBmiCompatibilityModel

class ProductBmiCompatibilityRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ProductBmiCompatibility]:
        pass

    @abstractmethod
    def get_by_id(self, compatibility_id: uuid.UUID) -> Optional[ProductBmiCompatibility]:
        pass

    @abstractmethod
    def create(self, compatibility_data: ProductBmiCompatibilityCreate) -> ProductBmiCompatibility:
        pass

    @abstractmethod
    def update(self, compatibility_id: uuid.UUID, compatibility_data: ProductBmiCompatibilityUpdate) -> Optional[ProductBmiCompatibility]:
        pass

    @abstractmethod
    def delete(self, compatibility_id: uuid.UUID) -> bool:
        pass

class ProductBmiCompatibilityRepositoryImpl(ProductBmiCompatibilityRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[ProductBmiCompatibility]:
        return self.db.query(ProductBmiCompatibilityModel).order_by(ProductBmiCompatibilityModel.created_at.desc()).all()

    def get_by_id(self, compatibility_id: uuid.UUID) -> Optional[ProductBmiCompatibility]:
        return self.db.query(ProductBmiCompatibilityModel).filter(ProductBmiCompatibilityModel.id == compatibility_id).first()

    def create(self, compatibility_data: ProductBmiCompatibilityCreate) -> ProductBmiCompatibility:
        db_compatibility = ProductBmiCompatibilityModel(**compatibility_data.dict())
        self.db.add(db_compatibility)
        self.db.commit()
        self.db.refresh(db_compatibility)
        return db_compatibility

    def update(self, compatibility_id: uuid.UUID, compatibility_data: ProductBmiCompatibilityUpdate) -> Optional[ProductBmiCompatibility]:
        db_compatibility = self.db.query(ProductBmiCompatibilityModel).filter(ProductBmiCompatibilityModel.id == compatibility_id).first()
        if db_compatibility:
            update_data = compatibility_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_compatibility, key, value)
            self.db.commit()
            self.db.refresh(db_compatibility)
        return db_compatibility

    def delete(self, compatibility_id: uuid.UUID) -> bool:
        db_compatibility = self.db.query(ProductBmiCompatibilityModel).filter(ProductBmiCompatibilityModel.id == compatibility_id).first()
        if db_compatibility:
            self.db.delete(db_compatibility)
            self.db.commit()
            return True
        return False