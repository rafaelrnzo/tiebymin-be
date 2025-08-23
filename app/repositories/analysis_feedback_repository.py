import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime

from app.schemas.analysis_feedback import AnalysisFeedback, AnalysisFeedbackCreate, AnalysisFeedbackUpdate
from app.models.analysis_feedback import AnalysisFeedbackModel

class AnalysisFeedbackRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[AnalysisFeedback]:
        pass

    @abstractmethod
    def get_by_id(self, feedback_id: uuid.UUID) -> Optional[AnalysisFeedback]:
        pass

    @abstractmethod
    def create(self, feedback_data: AnalysisFeedbackCreate) -> AnalysisFeedback:
        pass

    @abstractmethod
    def update(self, feedback_id: uuid.UUID, feedback_data: AnalysisFeedbackUpdate) -> Optional[AnalysisFeedback]:
        pass

    @abstractmethod
    def delete(self, feedback_id: uuid.UUID) -> bool:
        pass

class AnalysisFeedbackRepositoryImpl(AnalysisFeedbackRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[AnalysisFeedback]:
        return self.db.query(AnalysisFeedbackModel).order_by(AnalysisFeedbackModel.created_at.desc()).all()

    def get_by_id(self, feedback_id: uuid.UUID) -> Optional[AnalysisFeedback]:
        return self.db.query(AnalysisFeedbackModel).filter(AnalysisFeedbackModel.id == feedback_id).first()

    def create(self, feedback_data: AnalysisFeedbackCreate) -> AnalysisFeedback:
        db_feedback = AnalysisFeedbackModel(**feedback_data.dict())
        self.db.add(db_feedback)
        self.db.commit()
        self.db.refresh(db_feedback)
        return db_feedback

    def update(self, feedback_id: uuid.UUID, feedback_data: AnalysisFeedbackUpdate) -> Optional[AnalysisFeedback]:
        db_feedback = self.db.query(AnalysisFeedbackModel).filter(AnalysisFeedbackModel.id == feedback_id).first()
        if db_feedback:
            update_data = feedback_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_feedback, key, value)
            self.db.commit()
            self.db.refresh(db_feedback)
        return db_feedback

    def delete(self, feedback_id: uuid.UUID) -> bool:
        db_feedback = self.db.query(AnalysisFeedbackModel).filter(AnalysisFeedbackModel.id == feedback_id).first()
        if db_feedback:
            self.db.delete(db_feedback)
            self.db.commit()
            return True
        return False