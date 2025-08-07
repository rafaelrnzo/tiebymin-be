# File: repositories/bmi_repository.py

import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

from db.supabase_db import supabase
from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import Column, String, Float, Boolean, DateTime, UUID
from db.postgres_db import Base

from schemas.bmi import BMICategory, BMICategoryCreate


class BMICategoryModel(Base):
    __tablename__ = "bmi_categories"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    kategori = Column(String, nullable=False)
    min_bmi = Column(Float, nullable=False)
    max_bmi = Column(Float, nullable=True)
    tips_fashion = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class BMICategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[BMICategory]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: uuid.UUID) -> Optional[BMICategory]:
        pass

    @abstractmethod
    def create(self, category: BMICategoryCreate) -> BMICategory:
        pass

    @abstractmethod
    def update(self, category_id: uuid.UUID, category_data: BMICategoryCreate) -> Optional[BMICategory]:
        pass

    @abstractmethod
    def delete(self, category_id: uuid.UUID) -> bool:
        pass


class SupabaseBMIRepository(BMICategoryRepository):
    TABLE_NAME = "bmi_categories"

    def get_all(self) -> List[BMICategory]:
        response = supabase.table(self.TABLE_NAME).select("*").order("min_bmi").execute()
        if not response.data:
            return []
        return [BMICategory(**item) for item in response.data]

    def get_by_id(self, category_id: uuid.UUID) -> Optional[BMICategory]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("id", str(category_id)).execute()
        if not response.data:
            return None
        return BMICategory(**response.data[0])

    def create(self, category: BMICategoryCreate) -> BMICategory:
        category_dict = category.dict()
        response = supabase.table(self.TABLE_NAME).insert(category_dict).execute()
        
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create BMI category in Supabase.")
            
        return BMICategory(**response.data[0])

    def update(self, category_id: uuid.UUID, category_data: BMICategoryCreate) -> Optional[BMICategory]:
        response = supabase.table(self.TABLE_NAME).update(category_data.dict()).eq("id", str(category_id)).execute()
        if not response.data:
            return None
        return BMICategory(**response.data[0])

    def delete(self, category_id: uuid.UUID) -> bool:
        response = supabase.table(self.TABLE_NAME).delete().eq("id", str(category_id)).execute()
        return bool(response.data)


class PostgresBMIRepository(BMICategoryRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[BMICategory]:
        return self.db.query(BMICategoryModel).order_by(BMICategoryModel.min_bmi).all()

    def get_by_id(self, category_id: uuid.UUID) -> Optional[BMICategory]:
        return self.db.query(BMICategoryModel).filter(BMICategoryModel.id == category_id).first()

    def create(self, category: BMICategoryCreate) -> BMICategory:
        db_category = BMICategoryModel(**category.dict())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def update(self, category_id: uuid.UUID, category_data: BMICategoryCreate) -> Optional[BMICategory]:
        db_category = self.get_by_id(category_id)
        if db_category:
            for key, value in category_data.dict().items():
                setattr(db_category, key, value)
            self.db.commit()
            self.db.refresh(db_category)
        return db_category

    def delete(self, category_id: uuid.UUID) -> bool:
        db_category = self.get_by_id(category_id)
        if db_category:
            self.db.delete(db_category)
            self.db.commit()
            return True
        return False