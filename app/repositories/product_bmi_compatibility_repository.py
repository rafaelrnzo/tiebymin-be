import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel  
from schemas.product_bmi_compatibility import ProductBmiCompatibility, ProductBmiCompatibilityCreate
from db.supabase_db import supabase

class ProductBmiCompatibilityRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ProductBmiCompatibility]:
        pass

    @abstractmethod
    def get_by_id(self, compatibility_id: uuid.UUID) -> Optional[ProductBmiCompatibility]:
        pass

    @abstractmethod
    def create(self, compatibility_data: ProductBmiCompatibilityCreate) -> ProductBmiCompatibility:
        pass

    @abstractmethod
    def update(self, compatibility_id: uuid.UUID, compatibility_data: ProductBmiCompatibilityCreate) -> Optional[ProductBmiCompatibility]:
        pass

    @abstractmethod
    def delete(self, compatibility_id: uuid.UUID) -> bool:
        pass

class SupabaseProductBmiCompatibilityRepository(ProductBmiCompatibilityRepository):
    TABLE_NAME = "product_bmi_compatibility"

    def _prepare_data(self, pydantic_model: BaseModel) -> dict:
        data_dict = pydantic_model.dict()
        for key, value in data_dict.items():
            if isinstance(value, uuid.UUID):
                data_dict[key] = str(value)
        return data_dict

    def get_all(self) -> List[ProductBmiCompatibility]:
        response = supabase.table(self.TABLE_NAME).select("*").execute()
        return [ProductBmiCompatibility(**item) for item in response.data] if response.data else []

    def get_by_id(self, compatibility_id: uuid.UUID) -> Optional[ProductBmiCompatibility]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("id", str(compatibility_id)).execute()
        return ProductBmiCompatibility(**response.data[0]) if response.data else None

    def create(self, compatibility_data: ProductBmiCompatibilityCreate) -> ProductBmiCompatibility:
        data_to_insert = self._prepare_data(compatibility_data)
        response = supabase.table(self.TABLE_NAME).insert(data_to_insert).execute()
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create product BMI compatibility.")
        return ProductBmiCompatibility(**response.data[0])

    def update(self, compatibility_id: uuid.UUID, compatibility_data: ProductBmiCompatibilityCreate) -> Optional[ProductBmiCompatibility]:
        data_to_update = self._prepare_data(compatibility_data)
        response = supabase.table(self.TABLE_NAME).update(data_to_update).eq("id", str(compatibility_id)).execute()
        return ProductBmiCompatibility(**response.data[0]) if response.data else None

    def delete(self, compatibility_id: uuid.UUID) -> bool:
        response = supabase.table(self.TABLE_NAME).delete().eq("id", str(compatibility_id)).execute()
        return bool(response.data)