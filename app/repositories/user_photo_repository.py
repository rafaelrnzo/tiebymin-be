import uuid
import os
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime
from abc import ABC, abstractmethod

from app.schemas.user_photo import UserPhoto, UserPhotoCreate, UserPhotoUpdate
from app.models.user_photo import UserPhotoModel

class UserPhotoRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[UserPhoto]:
        pass

    @abstractmethod
    def get_by_id(self, photo_id: uuid.UUID) -> Optional[UserPhoto]:
        pass

    @abstractmethod
    def get_by_analysis_result_id(self, analysis_result_id: uuid.UUID) -> List[UserPhoto]:
        pass

    @abstractmethod
    def create(self, photo_data: UserPhotoCreate) -> UserPhoto:
        pass

    @abstractmethod
    def update(self, photo_id: uuid.UUID, photo_data: UserPhotoUpdate) -> Optional[UserPhoto]:
        pass

    @abstractmethod
    def delete(self, photo_id: uuid.UUID) -> bool:
        pass

class UserPhotoRepositoryImpl(UserPhotoRepository):
    def __init__(self, db_session: Session):
        self.db = db_session
        self.base_photo_url = f"{os.getenv('SUPABASE_URL')}/storage/v1/object/public/{os.getenv('SUPABASE_PHOTO_BUCKET')}"
    
    def _add_full_url(self, file_path: str) -> str:
        if file_path:
            return f"{self.base_photo_url}/{file_path}"
        return ""

    def get_all(self) -> List[UserPhoto]:
        results = self.db.query(UserPhotoModel).order_by(UserPhotoModel.uploaded_at.desc()).all()
        for item in results:
            item.file_path = self._add_full_url(item.file_path)
        return results

    def get_by_id(self, photo_id: uuid.UUID) -> Optional[UserPhoto]:
        result = self.db.query(UserPhotoModel).filter(UserPhotoModel.id == photo_id).first()
        if result:
            result.file_path = self._add_full_url(result.file_path)
        return result

    def get_by_analysis_result_id(self, analysis_result_id: uuid.UUID) -> List[UserPhoto]:
        results = self.db.query(UserPhotoModel).filter(UserPhotoModel.analysis_result_id == analysis_result_id).all()
        for item in results:
            item.file_path = self._add_full_url(item.file_path)
        return results

    def create(self, photo_data: UserPhotoCreate) -> UserPhoto:
        db_photo = UserPhotoModel(**photo_data.dict())
        self.db.add(db_photo)
        self.db.commit()
        self.db.refresh(db_photo)
        db_photo.file_path = self._add_full_url(db_photo.file_path)
        return db_photo

    def update(self, photo_id: uuid.UUID, photo_data: UserPhotoUpdate) -> Optional[UserPhoto]:
        db_photo = self.db.query(UserPhotoModel).filter(UserPhotoModel.id == photo_id).first()
        if db_photo:
            update_data = photo_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_photo, key, value)
            self.db.commit()
            self.db.refresh(db_photo)
            db_photo.file_path = self._add_full_url(db_photo.file_path)
        return db_photo

    def delete(self, photo_id: uuid.UUID) -> bool:
        db_photo = self.db.query(UserPhotoModel).filter(UserPhotoModel.id == photo_id).first()
        if db_photo:
            self.db.delete(db_photo)
            self.db.commit()
            return True
        return False