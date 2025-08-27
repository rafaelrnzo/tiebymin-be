import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from app.schemas.promo_code import PromoCode, PromoCodeCreate, PromoCodeUpdate
from app.models.promo_code import PromoCodeModel

class PromoCodeRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[PromoCode]:
        pass

    @abstractmethod
    def get_by_id(self, promo_id: uuid.UUID) -> Optional[PromoCode]:
        pass

    @abstractmethod
    def create(self, promo_data: PromoCodeCreate) -> PromoCode:
        pass

    @abstractmethod
    def update(self, promo_id: uuid.UUID, promo_data: PromoCodeUpdate) -> Optional[PromoCode]:
        pass

    @abstractmethod
    def delete(self, promo_id: uuid.UUID) -> bool:
        pass

class PromoCodeRepositoryImpl(PromoCodeRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[PromoCode]:
        return self.db.query(PromoCodeModel).order_by(PromoCodeModel.created_at.desc()).all()

    def get_by_id(self, promo_id: uuid.UUID) -> Optional[PromoCode]:
        return self.db.query(PromoCodeModel).filter(PromoCodeModel.id == promo_id).first()

    def create(self, promo_data: PromoCodeCreate) -> PromoCode:
        db_promo = PromoCodeModel(**promo_data.dict())
        self.db.add(db_promo)
        self.db.commit()
        self.db.refresh(db_promo)
        return db_promo

    def update(self, promo_id: uuid.UUID, promo_data: PromoCodeUpdate) -> Optional[PromoCode]:
        db_promo = self.db.query(PromoCodeModel).filter(PromoCodeModel.id == promo_id).first()
        if db_promo:
            update_data = promo_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_promo, key, value)
            self.db.commit()
            self.db.refresh(db_promo)
        return db_promo

    def delete(self, promo_id: uuid.UUID) -> bool:
        db_promo = self.db.query(PromoCodeModel).filter(PromoCodeModel.id == promo_id).first()
        if db_promo:
            self.db.delete(db_promo)
            self.db.commit()
            return True
        return False