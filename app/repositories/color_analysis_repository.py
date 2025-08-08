import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from schemas.color_analysis import ColorAnalysis, ColorAnalysisCreate
from db.supabase_db import supabase

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
    def update(self, analysis_id: uuid.UUID, analysis_data: ColorAnalysisCreate) -> Optional[ColorAnalysis]:
        pass

    @abstractmethod
    def delete(self, analysis_id: uuid.UUID) -> bool:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[ColorAnalysis]:
        pass

class SupabaseColorAnalysisRepository(ColorAnalysisRepository):
    TABLE_NAME = "color_analysis"

    def get_all(self) -> List[ColorAnalysis]:
        response = supabase.table(self.TABLE_NAME).select("*").order("name").execute()
        return [ColorAnalysis(**item) for item in response.data] if response.data else []

    def get_by_id(self, analysis_id: uuid.UUID) -> Optional[ColorAnalysis]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("id", str(analysis_id)).execute()
        return ColorAnalysis(**response.data[0]) if response.data else None

    def create(self, analysis_data: ColorAnalysisCreate) -> ColorAnalysis:
        response = supabase.table(self.TABLE_NAME).insert(analysis_data.dict()).execute()
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create color analysis.")
        return ColorAnalysis(**response.data[0])

    def update(self, analysis_id: uuid.UUID, analysis_data: ColorAnalysisCreate) -> Optional[ColorAnalysis]:
        response = supabase.table(self.TABLE_NAME).update(analysis_data.dict()).eq("id", str(analysis_id)).execute()
        return ColorAnalysis(**response.data[0]) if response.data else None

    def delete(self, analysis_id: uuid.UUID) -> bool:
        response = supabase.table(self.TABLE_NAME).delete().eq("id", str(analysis_id)).execute()
        return bool(response.data)
        
    def get_by_name(self, name: str) -> Optional[ColorAnalysis]:
        if not name:
            return None

        cleaned_name = name.strip()
        response = supabase.table(self.TABLE_NAME).select("*").ilike("name", cleaned_name).limit(1).execute()

        if response.data:
            return ColorAnalysis(**response.data[0])
        return None