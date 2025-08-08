import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from schemas.user_photo import UserPhoto, UserPhotoCreate
from db.supabase_db import supabase

class UserPhotoRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[UserPhoto]:
        pass

    @abstractmethod
    def get_by_id(self, photo_id: uuid.UUID) -> Optional[UserPhoto]:
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

    def _prepare_data(self, pydantic_model: BaseModel) -> dict:
        data_dict = pydantic_model.dict(exclude_none=True)
        for key, value in data_dict.items():
            if isinstance(value, uuid.UUID):
                data_dict[key] = str(value)
        return data_dict

    def get_all(self) -> List[UserPhoto]:
        response = supabase.table(self.TABLE_NAME).select("*").order("uploaded_at", desc=True).execute()
        return [UserPhoto(**item) for item in response.data] if response.data else []

    def get_by_id(self, photo_id: uuid.UUID) -> Optional[UserPhoto]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("id", str(photo_id)).execute()
        return UserPhoto(**response.data[0]) if response.data else None

    def create(self, photo_data: UserPhotoCreate) -> UserPhoto:
        data_to_insert = self._prepare_data(photo_data)
        response = supabase.table(self.TABLE_NAME).insert(data_to_insert).execute()
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create user photo record.")
        return UserPhoto(**response.data[0])

    def update(self, photo_id: uuid.UUID, photo_data: UserPhotoCreate) -> Optional[UserPhoto]:
        data_to_update = self._prepare_data(photo_data)
        response = supabase.table(self.TABLE_NAME).update(data_to_update).eq("id", str(photo_id)).execute()
        return UserPhoto(**response.data[0]) if response.data else None

    def delete(self, photo_id: uuid.UUID) -> bool:
        response = supabase.table(self.TABLE_NAME).delete().eq("id", str(photo_id)).execute()
        return bool(response.data)