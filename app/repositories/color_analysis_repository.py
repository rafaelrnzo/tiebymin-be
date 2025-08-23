import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime

from app.schemas.color_analysis import ColorAnalysis, ColorAnalysisCreate, ColorAnalysisUpdate
from app.models.color_analysis import ColorAnalysisModel

class ColorAnalysisRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ColorAnalysis]:
        pass

    @abstractmethod
    def get_by_id(self, analysis_id: uuid.UUID) -> Optional[ColorAnalysis]:
        pass

    @abstractmethod
    def create(self, analysis_data: ColorAnalysisCreate) -> ColorAnalysis:
        pass

    @abstractmethod
    def update(self, analysis_id: uuid.UUID, analysis_data: ColorAnalysisUpdate) -> Optional[ColorAnalysis]:
        pass

    @abstractmethod
    def delete(self, analysis_id: uuid.UUID) -> bool:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[ColorAnalysis]:
        pass

class ColorAnalysisRepositoryImpl(ColorAnalysisRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[ColorAnalysis]:
        return self.db.query(ColorAnalysisModel).order_by(ColorAnalysisModel.name).all()

    def get_by_id(self, analysis_id: uuid.UUID) -> Optional[ColorAnalysis]:
        return self.db.query(ColorAnalysisModel).filter(ColorAnalysisModel.id == analysis_id).first()

    def create(self, analysis_data: ColorAnalysisCreate) -> ColorAnalysis:
        db_analysis = ColorAnalysisModel(**analysis_data.dict())
        self.db.add(db_analysis)
        self.db.commit()
        self.db.refresh(db_analysis)
        return db_analysis

    def update(self, analysis_id: uuid.UUID, analysis_data: ColorAnalysisUpdate) -> Optional[ColorAnalysis]:
        db_analysis = self.db.query(ColorAnalysisModel).filter(ColorAnalysisModel.id == analysis_id).first()
        if db_analysis:
            update_data = analysis_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_analysis, key, value)
            self.db.commit()
            self.db.refresh(db_analysis)
        return db_analysis

    def delete(self, analysis_id: uuid.UUID) -> bool:
        db_analysis = self.db.query(ColorAnalysisModel).filter(ColorAnalysisModel.id == analysis_id).first()
        if db_analysis:
            self.db.delete(db_analysis)
            self.db.commit()
            return True
        return False

    def get_by_name(self, name: str) -> Optional[ColorAnalysis]:
        return self.db.query(ColorAnalysisModel).filter(ColorAnalysisModel.name.ilike(name)).first()