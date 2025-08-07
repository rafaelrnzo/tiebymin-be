import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException
from schemas.product import Product, ProductCreate
from db.supabase_db import supabase

class ProductRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, product_id: uuid.UUID) -> Optional[Product]:
        pass

    @abstractmethod
    def create(self, product_data: ProductCreate) -> Product:
        pass

    @abstractmethod
    def update(self, product_id: uuid.UUID, product_data: ProductCreate) -> Optional[Product]:
        pass

    @abstractmethod
    def delete(self, product_id: uuid.UUID) -> bool:
        pass

class SupabaseProductRepository(ProductRepository):
    TABLE_NAME = "products"

    def get_all(self) -> List[Product]:
        response = supabase.table(self.TABLE_NAME).select("*").order("name").execute()
        return [Product(**item) for item in response.data] if response.data else []

    def get_by_id(self, product_id: uuid.UUID) -> Optional[Product]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("id", str(product_id)).execute()
        return Product(**response.data[0]) if response.data else None

    def create(self, product_data: ProductCreate) -> Product:
        response = supabase.table(self.TABLE_NAME).insert(product_data.dict()).execute()
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create product.")
        return Product(**response.data[0])

    def update(self, product_id: uuid.UUID, product_data: ProductCreate) -> Optional[Product]:
        response = supabase.table(self.TABLE_NAME).update(product_data.dict()).eq("id", str(product_id)).execute()
        return Product(**response.data[0]) if response.data else None

    def delete(self, product_id: uuid.UUID) -> bool:
        response = supabase.table(self.TABLE_NAME).delete().eq("id", str(product_id)).execute()
        return bool(response.data)