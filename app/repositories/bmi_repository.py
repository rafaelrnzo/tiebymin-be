import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from decimal import Decimal

from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.schemas.bmi import BMICategoryCreate, BMICategoryUpdate
from app.models.bmi_categories import BMICategoryModel

def _schema_to_dict(data) -> dict:
    if hasattr(data, "model_dump"):
        return data.model_dump()
    if hasattr(data, "dict"):
        return data.dict()
    return dict(data)


class BMICategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[BMICategoryModel]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: uuid.UUID) -> Optional[BMICategoryModel]:
        pass

    @abstractmethod
    def create(self, category_data: BMICategoryCreate) -> BMICategoryModel:
        pass

    @abstractmethod
    def update(
        self, category_id: uuid.UUID, category_data: BMICategoryUpdate
    ) -> Optional[BMICategoryModel]:
        pass

    @abstractmethod
    def delete(self, category_id: uuid.UUID) -> bool:
        pass

    @abstractmethod
    def find_by_bmi_value(self, bmi_value: float) -> Optional[BMICategoryModel]:
        pass


class BMICategoryRepositoryImpl(BMICategoryRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[BMICategoryModel]:
        return (
            self.db.query(BMICategoryModel)
            .order_by(BMICategoryModel.min_bmi.asc())
            .all()
        )

    def get_by_id(self, category_id: uuid.UUID) -> Optional[BMICategoryModel]:
        return (
            self.db.query(BMICategoryModel)
            .filter(BMICategoryModel.id == category_id)
            .first()
        )

    def create(self, category_data: BMICategoryCreate) -> BMICategoryModel:
        payload = _schema_to_dict(category_data)
        db_obj = BMICategoryModel(**payload)
        try:
            self.db.add(db_obj)
            self.db.commit()
            self.db.refresh(db_obj)
            return db_obj
        except Exception:
            self.db.rollback()
            raise

    def update(
        self, category_id: uuid.UUID, category_data: BMICategoryUpdate
    ) -> Optional[BMICategoryModel]:
        db_obj = (
            self.db.query(BMICategoryModel)
            .filter(BMICategoryModel.id == category_id)
            .first()
        )
        if not db_obj:
            return None

        payload = _schema_to_dict(category_data)
        if hasattr(category_data, "model_dump"):
            payload = category_data.model_dump(exclude_unset=True)
        elif hasattr(category_data, "dict"):
            payload = category_data.dict(exclude_unset=True)

        for k, v in payload.items():
            setattr(db_obj, k, v)

        try:
            self.db.commit()
            self.db.refresh(db_obj)
            return db_obj
        except Exception:
            self.db.rollback()
            raise

    def delete(self, category_id: uuid.UUID) -> bool:
        db_obj = (
            self.db.query(BMICategoryModel)
            .filter(BMICategoryModel.id == category_id)
            .first()
        )
        if not db_obj:
            return False
        try:
            self.db.delete(db_obj)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise

    def find_by_bmi_value(self, bmi_value: float) -> Optional[BMICategoryModel]:
        bmi_dec = Decimal(str(bmi_value))

        return (
            self.db.query(BMICategoryModel)
            .filter(
                BMICategoryModel.is_active.is_(True),
                BMICategoryModel.min_bmi <= bmi_dec,
                or_(
                    BMICategoryModel.max_bmi >= bmi_dec,
                    BMICategoryModel.max_bmi.is_(None),
                ),
            )
            .order_by(BMICategoryModel.min_bmi.asc())
            .first()
        )
