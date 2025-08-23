import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from app.schemas.product_color_analysis_compatibility import ProductColorAnalysisCompatibility, ProductColorAnalysisCompatibilityCreate, ProductColorAnalysisCompatibilityUpdate
from app.models.product_color_analysis_compatibility import ProductColorAnalysisCompatibilityModel

class ProductColorAnalysisCompatibilityRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ProductColorAnalysisCompatibility]:
        pass

    @abstractmethod
    def get_by_id(self, compatibility_id: uuid.UUID) -> Optional[ProductColorAnalysisCompatibility]:
        pass

    @abstractmethod
    def create(self, compatibility_data: ProductColorAnalysisCompatibilityCreate) -> ProductColorAnalysisCompatibility:
        pass

    @abstractmethod
    def update(self, compatibility_id: uuid.UUID, compatibility_data: ProductColorAnalysisCompatibilityUpdate) -> Optional[ProductColorAnalysisCompatibility]:
        pass

    @abstractmethod
    def delete(self, compatibility_id: uuid.UUID) -> bool:
        pass

class ProductColorAnalysisCompatibilityRepositoryImpl(ProductColorAnalysisCompatibilityRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[ProductColorAnalysisCompatibility]:
        return self.db.query(ProductColorAnalysisCompatibilityModel).order_by(ProductColorAnalysisCompatibilityModel.created_at.desc()).all()

    def get_by_id(self, compatibility_id: uuid.UUID) -> Optional[ProductColorAnalysisCompatibility]:
        return self.db.query(ProductColorAnalysisCompatibilityModel).filter(ProductColorAnalysisCompatibilityModel.id == compatibility_id).first()

    def create(self, compatibility_data: ProductColorAnalysisCompatibilityCreate) -> ProductColorAnalysisCompatibility:
        db_compatibility = ProductColorAnalysisCompatibilityModel(**compatibility_data.dict())
        self.db.add(db_compatibility)
        self.db.commit()
        self.db.refresh(db_compatibility)
        return db_compatibility

    def update(self, compatibility_id: uuid.UUID, compatibility_data: ProductColorAnalysisCompatibilityUpdate) -> Optional[ProductColorAnalysisCompatibility]:
        db_compatibility = self.db.query(ProductColorAnalysisCompatibilityModel).filter(ProductColorAnalysisCompatibilityModel.id == compatibility_id).first()
        if db_compatibility:
            update_data = compatibility_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_compatibility, key, value)
            self.db.commit()
            self.db.refresh(db_compatibility)
        return db_compatibility

    def delete(self, compatibility_id: uuid.UUID) -> bool:
        db_compatibility = self.db.query(ProductColorAnalysisCompatibilityModel).filter(ProductColorAnalysisCompatibilityModel.id == compatibility_id).first()
        if db_compatibility:
            self.db.delete(db_compatibility)
            self.db.commit()
            return True
        return False