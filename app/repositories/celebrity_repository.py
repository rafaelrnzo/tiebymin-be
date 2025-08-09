import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from schemas.celebrity import Celebrity, CelebrityCreate
from db.supabase_db import supabase

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
    def update(self, celebrity_id: uuid.UUID, celebrity_data: CelebrityCreate) -> Optional[Celebrity]:
        pass

    @abstractmethod
    def delete(self, celebrity_id: uuid.UUID) -> bool:
        pass
    
    @abstractmethod
    def find_id_by_match(
        self, face_shape_id: uuid.UUID, color_analysis_id: uuid.UUID
    ) -> Optional[uuid.UUID]:
        pass

class SupabaseCelebrityRepository(CelebrityRepository):
    TABLE_NAME = "celebrities"
    
    def find_id_by_match(
        self, face_shape_id: uuid.UUID, color_analysis_id: uuid.UUID
    ) -> Optional[uuid.UUID]:
        if not face_shape_id or not color_analysis_id:
            return None

        response = (
            supabase.table(self.TABLE_NAME)
            .select("id")
            .eq("faceshape_id", str(face_shape_id))
            .eq("color_analysis_id", str(color_analysis_id))
            .limit(1) 
            .execute()
        )

        if response.data:
            return uuid.UUID(response.data[0]['id'])
        
        return None

    def _prepare_data(self, pydantic_model: BaseModel) -> dict:
        data_dict = pydantic_model.dict(exclude_none=True)
        for key, value in data_dict.items():
            if isinstance(value, uuid.UUID):
                data_dict[key] = str(value)
        return data_dict

    def get_all(self) -> List[Celebrity]:
        response = supabase.table(self.TABLE_NAME).select("*").order("name").execute()
        return [Celebrity(**item) for item in response.data] if response.data else []

    def get_by_id(self, celebrity_id: uuid.UUID) -> Optional[Celebrity]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("id", str(celebrity_id)).execute()
        return Celebrity(**response.data[0]) if response.data else None

    def create(self, celebrity_data: CelebrityCreate) -> Celebrity:
        data_to_insert = self._prepare_data(celebrity_data)
        response = supabase.table(self.TABLE_NAME).insert(data_to_insert).execute()
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create celebrity.")
        return Celebrity(**response.data[0])

    def update(self, celebrity_id: uuid.UUID, celebrity_data: CelebrityCreate) -> Optional[Celebrity]:
        data_to_update = self._prepare_data(celebrity_data)
        response = supabase.table(self.TABLE_NAME).update(data_to_update).eq("id", str(celebrity_id)).execute()
        return Celebrity(**response.data[0]) if response.data else None

    def delete(self, celebrity_id: uuid.UUID) -> bool:
        response = supabase.table(self.TABLE_NAME).delete().eq("id", str(celebrity_id)).execute()
        return bool(response.data)