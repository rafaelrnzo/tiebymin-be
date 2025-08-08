import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from schemas.user_analysis_result import UserAnalysisResult, UserAnalysisResultCreate
from db.supabase_db import supabase

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
    def update(self, result_id: uuid.UUID, result_data: UserAnalysisResultCreate) -> Optional[UserAnalysisResult]:
        pass

    @abstractmethod
    def delete(self, result_id: uuid.UUID) -> bool:
        pass

class SupabaseUserAnalysisResultRepository(UserAnalysisResultRepository):
    TABLE_NAME = "user_analysis_results"

    def _prepare_data(self, pydantic_model: BaseModel) -> dict:
        data_dict = pydantic_model.dict(exclude_none=True)
        for key, value in data_dict.items():
            if isinstance(value, uuid.UUID):
                data_dict[key] = str(value)
        return data_dict

    def get_all(self) -> List[UserAnalysisResult]:
        response = supabase.table(self.TABLE_NAME).select("*").order("created_at", desc=True).execute()
        return [UserAnalysisResult(**item) for item in response.data] if response.data else []

    def get_by_id(self, result_id: uuid.UUID) -> Optional[UserAnalysisResult]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("id", str(result_id)).execute()
        return UserAnalysisResult(**response.data[0]) if response.data else None

    def create(self, result_data: UserAnalysisResultCreate) -> UserAnalysisResult:
        data_to_insert = self._prepare_data(result_data)
        response = supabase.table(self.TABLE_NAME).insert(data_to_insert).execute()
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create user analysis result.")
        return UserAnalysisResult(**response.data[0])

    def update(self, result_id: uuid.UUID, result_data: UserAnalysisResultCreate) -> Optional[UserAnalysisResult]:
        data_to_update = self._prepare_data(result_data)
        response = supabase.table(self.TABLE_NAME).update(data_to_update).eq("id", str(result_id)).execute()
        return UserAnalysisResult(**response.data[0]) if response.data else None

    def delete(self, result_id: uuid.UUID) -> bool:
        response = supabase.table(self.TABLE_NAME).delete().eq("id", str(result_id)).execute()
        return bool(response.data)