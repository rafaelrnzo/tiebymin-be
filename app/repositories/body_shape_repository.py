import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.body_shape import BodyShape, BodyShapeCreate, BodyShapeUpdate
from app.models.body_shape import BodyShapeModel

class BodyShapeRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[BodyShape]:
        pass

    @abstractmethod
    def get_by_id(self, shape_id: uuid.UUID) -> Optional[BodyShape]:
        pass

    @abstractmethod
    def create(self, shape_data: BodyShapeCreate) -> BodyShape:
        pass

    @abstractmethod
    def update(self, shape_id: uuid.UUID, shape_data: BodyShapeUpdate) -> Optional[BodyShape]:
        pass

    @abstractmethod
    def delete(self, shape_id: uuid.UUID) -> bool:
        pass
    
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[BodyShape]:
        pass

class BodyShapeRepositoryImpl(BodyShapeRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[BodyShape]:
        return self.db.query(BodyShapeModel).order_by(BodyShapeModel.name).all()

    def get_by_id(self, shape_id: uuid.UUID) -> Optional[BodyShape]:
        return self.db.query(BodyShapeModel).filter(BodyShapeModel.id == shape_id).first()

    def create(self, shape_data: BodyShapeCreate) -> BodyShape:
        db_shape = BodyShapeModel(**shape_data.dict())
        self.db.add(db_shape)
        self.db.commit()
        self.db.refresh(db_shape)
        return db_shape

    def update(self, shape_id: uuid.UUID, shape_data: BodyShapeUpdate) -> Optional[BodyShape]:
        db_shape = self.db.query(BodyShapeModel).filter(BodyShapeModel.id == shape_id).first()
        if db_shape:
            update_data = shape_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_shape, key, value)
            self.db.commit()
            self.db.refresh(db_shape)
        return db_shape

    def delete(self, shape_id: uuid.UUID) -> bool:
        db_shape = self.db.query(BodyShapeModel).filter(BodyShapeModel.id == shape_id).first()
        if db_shape:
            self.db.delete(db_shape)
            self.db.commit()
            return True
        return False

    def get_by_name(self, name: str) -> Optional[BodyShape]:
        return self.db.query(BodyShapeModel).filter(BodyShapeModel.name.ilike(name)).first()