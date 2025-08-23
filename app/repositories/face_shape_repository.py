import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.schemas.face_shape import FaceShape, FaceShapeCreate, FaceShapeUpdate
from app.models.face_shape import FaceShapeModel

class FaceShapeRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[FaceShape]:
        pass

    @abstractmethod
    def get_by_id(self, shape_id: uuid.UUID) -> Optional[FaceShape]:
        pass

    @abstractmethod
    def create(self, shape_data: FaceShapeCreate) -> FaceShape:
        pass

    @abstractmethod
    def update(self, shape_id: uuid.UUID, shape_data: FaceShapeUpdate) -> Optional[FaceShape]:
        pass

    @abstractmethod
    def delete(self, shape_id: uuid.UUID) -> bool:
        pass
    
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[FaceShape]:
        pass

class FaceShapeRepositoryImpl(FaceShapeRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[FaceShape]:
        return self.db.query(FaceShapeModel).order_by(FaceShapeModel.name).all()

    def get_by_id(self, shape_id: uuid.UUID) -> Optional[FaceShape]:
        return self.db.query(FaceShapeModel).filter(FaceShapeModel.id == shape_id).first()

    def create(self, shape_data: FaceShapeCreate) -> FaceShape:
        db_shape = FaceShapeModel(**shape_data.dict())
        self.db.add(db_shape)
        self.db.commit()
        self.db.refresh(db_shape)
        return db_shape

    def update(self, shape_id: uuid.UUID, shape_data: FaceShapeUpdate) -> Optional[FaceShape]:
        db_shape = self.db.query(FaceShapeModel).filter(FaceShapeModel.id == shape_id).first()
        if db_shape:
            update_data = shape_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_shape, key, value)
            self.db.commit()
            self.db.refresh(db_shape)
        return db_shape

    def delete(self, shape_id: uuid.UUID) -> bool:
        db_shape = self.db.query(FaceShapeModel).filter(FaceShapeModel.id == shape_id).first()
        if db_shape:
            self.db.delete(db_shape)
            self.db.commit()
            return True
        return False

    def get_by_name(self, name: str) -> Optional[FaceShape]:
        return self.db.query(FaceShapeModel).filter(FaceShapeModel.name.ilike(name)).first()