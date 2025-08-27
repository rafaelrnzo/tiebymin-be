import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from app.schemas.payment import Payment, PaymentCreate, PaymentUpdate
from app.models.payment import PaymentModel

class PaymentRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Payment]:
        pass

    @abstractmethod
    def get_by_id(self, payment_id: uuid.UUID) -> Optional[Payment]:
        pass

    @abstractmethod
    def create(self, payment_data: PaymentCreate) -> Payment:
        pass

    @abstractmethod
    def update(self, payment_id: uuid.UUID, payment_data: PaymentUpdate) -> Optional[Payment]:
        pass

    @abstractmethod
    def delete(self, payment_id: uuid.UUID) -> bool:
        pass

class PaymentRepositoryImpl(PaymentRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[Payment]:
        return self.db.query(PaymentModel).order_by(PaymentModel.created_at.desc()).all()

    def get_by_id(self, payment_id: uuid.UUID) -> Optional[Payment]:
        return self.db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()

    def create(self, payment_data: PaymentCreate) -> Payment:
        db_payment = PaymentModel(**payment_data.dict())
        self.db.add(db_payment)
        self.db.commit()
        self.db.refresh(db_payment)
        return db_payment

    def update(self, payment_id: uuid.UUID, payment_data: PaymentUpdate) -> Optional[Payment]:
        db_payment = self.db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
        if db_payment:
            update_data = payment_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_payment, key, value)
            self.db.commit()
            self.db.refresh(db_payment)
        return db_payment

    def delete(self, payment_id: uuid.UUID) -> bool:
        db_payment = self.db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
        if db_payment:
            self.db.delete(db_payment)
            self.db.commit()
            return True
        return False