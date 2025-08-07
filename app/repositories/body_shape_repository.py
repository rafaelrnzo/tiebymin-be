import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException

from schemas.body_shape import BodyShape, BodyShapeCreate
from db.supabase_db import supabase

class BodyShapeRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[BodyShape]:
        pass

    @abstractmethod
    def get_by_id(self, shape_id: uuid.UUID) -> Optional[BodyShape]:
        pass

    @abstractmethod
    def create(self, shape_data: BodyShapeCreate) -> BodyShape:
        pass

    @abstractmethod
    def update(self, shape_id: uuid.UUID, shape_data: BodyShapeCreate) -> Optional[BodyShape]:
        pass

    @abstractmethod
    def delete(self, shape_id: uuid.UUID) -> bool:
        pass

class SupabaseBodyShapeRepository(BodyShapeRepository):
    TABLE_NAME = "body_shapes"

    def get_all(self) -> List[BodyShape]:
        response = supabase.table(self.TABLE_NAME).select("*").order("name").execute()
        if not response.data:
            return []
        return [BodyShape(**item) for item in response.data]

    def get_by_id(self, shape_id: uuid.UUID) -> Optional[BodyShape]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("id", str(shape_id)).execute()
        if not response.data:
            return None
        return BodyShape(**response.data[0])

    def create(self, shape_data: BodyShapeCreate) -> BodyShape:
        response = supabase.table(self.TABLE_NAME).insert(shape_data.dict()).execute()
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create body shape in Supabase.")
        return BodyShape(**response.data[0])

    def update(self, shape_id: uuid.UUID, shape_data: BodyShapeCreate) -> Optional[BodyShape]:
        response = supabase.table(self.TABLE_NAME).update(shape_data.dict()).eq("id", str(shape_id)).execute()
        if not response.data:
            return None
        return BodyShape(**response.data[0])

    def delete(self, shape_id: uuid.UUID) -> bool:
        response = supabase.table(self.TABLE_NAME).delete().eq("id", str(shape_id)).execute()
        return bool(response.data)