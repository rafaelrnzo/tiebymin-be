import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import or_

from app.schemas.bmi import BMICategory, BMICategoryCreate, BMICategoryUpdate
from app.models.bmi_categories import BMICategoryModel

class BMICategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[BMICategory]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: uuid.UUID) -> Optional[BMICategory]:
        pass

    @abstractmethod
    def create(self, category_data: BMICategoryCreate) -> BMICategory:
        pass

    @abstractmethod
    def update(self, category_id: uuid.UUID, category_data: BMICategoryUpdate) -> Optional[BMICategory]:
        pass

    @abstractmethod
    def delete(self, category_id: uuid.UUID) -> bool:
        pass

    @abstractmethod
    def find_by_bmi_value(self, bmi_value: float) -> Optional[BMICategory]:
        pass

class BMICategoryRepositoryImpl(BMICategoryRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[BMICategory]:
        return self.db.query(BMICategoryModel).order_by(BMICategoryModel.min_bmi).all()

    def get_by_id(self, category_id: uuid.UUID) -> Optional[BMICategory]:
        return self.db.query(BMICategoryModel).filter(BMICategoryModel.id == category_id).first()

    def create(self, category_data: BMICategoryCreate) -> BMICategory:
        db_category = BMICategoryModel(**category_data.dict())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def update(self, category_id: uuid.UUID, category_data: BMICategoryUpdate) -> Optional[BMICategory]:
        db_category = self.db.query(BMICategoryModel).filter(BMICategoryModel.id == category_id).first()
        if db_category:
            update_data = category_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_category, key, value)
            self.db.commit()
            self.db.refresh(db_category)
        return db_category

    def delete(self, category_id: uuid.UUID) -> bool:
        db_category = self.db.query(BMICategoryModel).filter(BMICategoryModel.id == category_id).first()
        if db_category:
            self.db.delete(db_category)
            self.db.commit()
            return True
        return False

    def find_by_bmi_value(self, bmi_value: float) -> Optional[BMICategory]:
        return self.db.query(BMICategoryModel).filter(
            BMICategoryModel.min_bmi <= bmi_value,
            or_(BMICategoryModel.max_bmi >= bmi_value, BMICategoryModel.max_bmi.is_(None))
        ).first()