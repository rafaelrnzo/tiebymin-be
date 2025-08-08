import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from schemas.face_shape import FaceShape, FaceShapeCreate
from db.supabase_db import supabase

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
    def update(self, shape_id: uuid.UUID, shape_data: FaceShapeCreate) -> Optional[FaceShape]:
        pass

    @abstractmethod
    def delete(self, shape_id: uuid.UUID) -> bool:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[FaceShape]:
        pass

class SupabaseFaceShapeRepository(FaceShapeRepository):
    TABLE_NAME = "face_shapes"

    def get_all(self) -> List[FaceShape]:
        response = supabase.table(self.TABLE_NAME).select("*").order("name").execute()
        return [FaceShape(**item) for item in response.data] if response.data else []

    def get_by_id(self, shape_id: uuid.UUID) -> Optional[FaceShape]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("id", str(shape_id)).execute()
        return FaceShape(**response.data[0]) if response.data else None

    def create(self, shape_data: FaceShapeCreate) -> FaceShape:
        response = supabase.table(self.TABLE_NAME).insert(shape_data.dict()).execute()
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create face shape.")
        return FaceShape(**response.data[0])

    def update(self, shape_id: uuid.UUID, shape_data: FaceShapeCreate) -> Optional[FaceShape]:
        response = supabase.table(self.TABLE_NAME).update(shape_data.dict()).eq("id", str(shape_id)).execute()
        return FaceShape(**response.data[0]) if response.data else None

    def delete(self, shape_id: uuid.UUID) -> bool:
        response = supabase.table(self.TABLE_NAME).delete().eq("id", str(shape_id)).execute()
        return bool(response.data)
        
    def get_by_name(self, name: str) -> Optional[FaceShape]:
        if not name:
            return None
        
        cleaned_name = name.strip()
        response = supabase.table(self.TABLE_NAME).select("*").ilike("name", cleaned_name).limit(1).execute()
        
        if response.data:
            return FaceShape(**response.data[0])
        return None