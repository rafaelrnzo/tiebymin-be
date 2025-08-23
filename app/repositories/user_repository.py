import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate, UserUpdate
from app.models.user import User

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

class UserRepositoryImpl(UserRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[User]:
        return self.db.query(User).order_by(User.created_at.desc()).all()

    def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user_data: UserCreate) -> User:
        db_user = User(**user_data.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user_id: uuid.UUID, user_data: UserUpdate) -> Optional[User]:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            update_data = user_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_user, key, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: uuid.UUID) -> bool:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return True
        return False
    
    def update_google_id(self, user_id: uuid.UUID, google_id: str):
        db_user = self.get_by_id(user_id)
        if not db_user:
            return None
        db_user.google_id = google_id
        self.db.commit()
        self.db.refresh(db_user)
        return db_user