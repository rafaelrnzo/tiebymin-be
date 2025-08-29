import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from app.schemas.celebrity import Celebrity, CelebrityCreate, CelebrityUpdate
from app.models.celebrity import CelebrityModel

class CelebrityRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Celebrity]:
        pass

    @abstractmethod
    def get_by_id(self, celebrity_id: uuid.UUID) -> Optional[Celebrity]:
        pass

    @abstractmethod
    def create(self, celebrity_data: CelebrityCreate) -> Celebrity:
        pass

    @abstractmethod
    def update(self, celebrity_id: uuid.UUID, celebrity_data: CelebrityUpdate) -> Optional[Celebrity]:
        pass

    @abstractmethod
    def delete(self, celebrity_id: uuid.UUID) -> bool:
        pass
    
    @abstractmethod
    def find_id_by_match(self, face_shape_id: uuid.UUID, color_analysis_id: uuid.UUID) -> Optional[uuid.UUID]:
        pass

class CelebrityRepositoryImpl(CelebrityRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[Celebrity]:
        return self.db.query(CelebrityModel).order_by(CelebrityModel.name).all()

    def get_by_id(self, celebrity_id: uuid.UUID) -> Optional[Celebrity]:
        return self.db.query(CelebrityModel).filter(CelebrityModel.id == celebrity_id).first()

    def create(self, celebrity_data: CelebrityCreate) -> Celebrity:
        db_celebrity = CelebrityModel(**celebrity_data.dict())
        self.db.add(db_celebrity)
        self.db.commit()
        self.db.refresh(db_celebrity)
        return db_celebrity

    def update(self, celebrity_id: uuid.UUID, celebrity_data: CelebrityUpdate) -> Optional[Celebrity]:
        db_celebrity = self.db.query(CelebrityModel).filter(CelebrityModel.id == celebrity_id).first()
        if db_celebrity:
            update_data = celebrity_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_celebrity, key, value)
            self.db.commit()
            self.db.refresh(db_celebrity)
        return db_celebrity

    def delete(self, celebrity_id: uuid.UUID) -> bool:
        db_celebrity = self.db.query(CelebrityModel).filter(CelebrityModel.id == celebrity_id).first()
        if db_celebrity:
            self.db.delete(db_celebrity)
            self.db.commit()
            return True
        return False

    def find_id_by_match(self, face_shape_id: uuid.UUID, color_analysis_id: uuid.UUID) -> Optional[uuid.UUID]:
        celebrity = self.db.query(CelebrityModel).filter(
            CelebrityModel.faceshape_id == face_shape_id,
            CelebrityModel.color_analysis_id == color_analysis_id
        ).first()
        
        return celebrity.id if celebrity else None