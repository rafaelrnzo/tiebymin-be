import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime

from app.schemas.user_analysis_result import UserAnalysisResult, UserAnalysisResultCreate, UserAnalysisResultUpdate
from app.models.user_analysis_result import UserAnalysisResultModel

class UserAnalysisResultRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[UserAnalysisResult]:
        pass

    @abstractmethod
    def get_by_id(self, result_id: uuid.UUID) -> Optional[UserAnalysisResult]:
        pass

    @abstractmethod
    def create(self, result_data: UserAnalysisResultCreate) -> UserAnalysisResult:
        pass

    @abstractmethod
    def update(self, result_id: uuid.UUID, result_data: UserAnalysisResultUpdate) -> Optional[UserAnalysisResult]:
        pass

    @abstractmethod
    def delete(self, result_id: uuid.UUID) -> bool:
        pass

class UserAnalysisResultRepositoryImpl(UserAnalysisResultRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[UserAnalysisResult]:
        return self.db.query(UserAnalysisResultModel).order_by(UserAnalysisResultModel.created_at.desc()).all()

    def get_by_id(self, result_id: uuid.UUID) -> Optional[UserAnalysisResult]:
        return self.db.query(UserAnalysisResultModel).filter(UserAnalysisResultModel.id == result_id).first()

    def create(self, result_data: UserAnalysisResultCreate) -> UserAnalysisResult:
        db_result = UserAnalysisResultModel(**result_data.dict())
        self.db.add(db_result)
        self.db.commit()
        self.db.refresh(db_result)
        return db_result

    def update(self, result_id: uuid.UUID, result_data: UserAnalysisResultUpdate) -> Optional[UserAnalysisResult]:
        db_result = self.db.query(UserAnalysisResultModel).filter(UserAnalysisResultModel.id == result_id).first()
        if db_result:
            update_data = result_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_result, key, value)
            self.db.commit()
            self.db.refresh(db_result)
        return db_result

    def delete(self, result_id: uuid.UUID) -> bool:
        db_result = self.db.query(UserAnalysisResultModel).filter(UserAnalysisResultModel.id == result_id).first()
        if db_result:
            self.db.delete(db_result)
            self.db.commit()
            return True
        return False