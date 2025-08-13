import uuid
import os
from dotenv import load_dotenv
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from datetime import datetime

from schemas.user_photo import UserPhoto, UserPhotoCreate
from db.supabase_db import supabase

load_dotenv()


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
    def update(self, photo_id: uuid.UUID, photo_data: UserPhotoCreate) -> Optional[UserPhoto]:
        pass

    @abstractmethod
    def delete(self, photo_id: uuid.UUID) -> bool:
        pass


class SupabaseUserPhotoRepository(UserPhotoRepository):
    TABLE_NAME = "user_photos"

    def __init__(self):
        supabase_url = os.getenv("SUPABASE_URL")
        bucket_name = os.getenv("SUPABASE_PHOTO_BUCKET")
        if not supabase_url or not bucket_name:
            raise ValueError("SUPABASE_URL and SUPABASE_PHOTO_BUCKET must be set in .env file")
        
        self.base_photo_url = f"{supabase_url}/storage/v1/object/public/{bucket_name}"

    def _add_full_url_to_item(self, item: dict) -> dict:
        if item and 'file_path' in item and item['file_path']:
            item['file_path'] = f"{self.base_photo_url}/{item['file_path']}"
        return item

    def _prepare_data(self, pydantic_model: BaseModel) -> dict:
        data_dict = pydantic_model.dict(exclude_none=True)
        for key, value in data_dict.items():
            if isinstance(value, uuid.UUID):
                data_dict[key] = str(value)
            elif isinstance(value, datetime):
                data_dict[key] = value.isoformat()
        return data_dict
    
    def get_all(self) -> List[UserPhoto]:
        response = supabase.table(self.TABLE_NAME).select("*").order("uploaded_at", desc=True).execute()
        if not response.data:
            return []
        
        processed_data = [self._add_full_url_to_item(item) for item in response.data]
        return [UserPhoto(**item) for item in processed_data]

    def get_by_id(self, photo_id: uuid.UUID) -> Optional[UserPhoto]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("id", str(photo_id)).limit(1).execute()
        if not response.data:
            return None
            
        processed_item = self._add_full_url_to_item(response.data[0])
        return UserPhoto(**processed_item)

    def get_by_analysis_result_id(self, analysis_result_id: uuid.UUID) -> List[UserPhoto]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("analysis_result_id", str(analysis_result_id)).execute()
        if not response.data:
            return []
            
        processed_data = [self._add_full_url_to_item(item) for item in response.data]
        return [UserPhoto(**item) for item in processed_data]

    def create(self, photo_data: UserPhotoCreate) -> UserPhoto:
        data_to_insert = self._prepare_data(photo_data)
        response = supabase.table(self.TABLE_NAME).insert(data_to_insert).execute()
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create user photo record.")
            
        processed_item = self._add_full_url_to_item(response.data[0])
        return UserPhoto(**processed_item)

    def update(self, photo_id: uuid.UUID, photo_data: UserPhotoCreate) -> Optional[UserPhoto]:
        data_to_update = self._prepare_data(photo_data)
        response = supabase.table(self.TABLE_NAME).update(data_to_update).eq("id", str(photo_id)).execute()
        if not response.data:
            return None
            
        processed_item = self._add_full_url_to_item(response.data[0])
        return UserPhoto(**processed_item)

    def delete(self, photo_id: uuid.UUID) -> bool:
        response = supabase.table(self.TABLE_NAME).delete().eq("id", str(photo_id)).execute()
        return bool(response.data)