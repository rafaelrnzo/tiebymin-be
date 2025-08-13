import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import HTTPException, status

from schemas.user import User, UserCreate, UserUpdate
from db.supabase_db import supabase 
from services.password_services import hash_password, verify_password  

class UserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def create(self, user_data: UserCreate) -> User:
        pass

    @abstractmethod
    def update(self, user_id: uuid.UUID, user_data: UserUpdate) -> Optional[User]:
        pass

    @abstractmethod
    def delete(self, user_id: uuid.UUID) -> bool:
        pass


class SupabaseUserRepository(UserRepository):
    TABLE_NAME = "users"

    def get_all(self) -> List[User]:
        response = supabase.table(self.TABLE_NAME).select("*").order("created_at").execute()
        return [User(**item) for item in response.data] if response.data else []

    def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("id", str(user_id)).execute()
        return User(**response.data[0]) if response.data else None

    def get_by_email(self, email: str) -> Optional[User]:
        response = supabase.table(self.TABLE_NAME).select("*").eq("email", email).limit(1).execute()
        return User(**response.data[0]) if response.data else None

    def create(self, user_data: UserCreate) -> User:
        user_dict = user_data.dict()

        hashed_pw = hash_password(user_data.password)
        del user_dict["password"]
        user_dict["password_hash"] = hashed_pw

        response = supabase.table(self.TABLE_NAME).insert(user_dict).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create user."
            )

        return User(**response.data[0])

    def update(self, user_id: uuid.UUID, user_data: UserUpdate) -> Optional[User]:
        update_dict = user_data.dict(exclude_unset=True)

        if "password" in update_dict:
            update_dict["password_hash"] = hash_password(update_dict["password"])
            del update_dict["password"]

        if not update_dict:
            return self.get_by_id(user_id)

        response = supabase.table(self.TABLE_NAME).update(update_dict).eq("id", str(user_id)).execute()
        return User(**response.data[0]) if response.data else None

    def delete(self, user_id: uuid.UUID) -> bool:
        response = supabase.table(self.TABLE_NAME).delete().eq("id", str(user_id)).execute()
        return bool(response.data)
