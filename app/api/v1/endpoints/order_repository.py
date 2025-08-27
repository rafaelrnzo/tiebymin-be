import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from app.schemas.order import Order, OrderCreate, OrderUpdate
from app.models.order import OrderModel

class OrderRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Order]:
        pass

    @abstractmethod
    def get_by_id(self, order_id: uuid.UUID) -> Optional[Order]:
        pass

    @abstractmethod
    def create(self, order_data: OrderCreate) -> Order:
        pass

    @abstractmethod
    def update(self, order_id: uuid.UUID, order_data: OrderUpdate) -> Optional[Order]:
        pass

    @abstractmethod
    def delete(self, order_id: uuid.UUID) -> bool:
        pass

class OrderRepositoryImpl(OrderRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[Order]:
        return self.db.query(OrderModel).order_by(OrderModel.created_at.desc()).all()

    def get_by_id(self, order_id: uuid.UUID) -> Optional[Order]:
        return self.db.query(OrderModel).filter(OrderModel.id == order_id).first()

    def create(self, order_data: OrderCreate) -> Order:
        db_order = OrderModel(**order_data.dict())
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order

    def update(self, order_id: uuid.UUID, order_data: OrderUpdate) -> Optional[Order]:
        db_order = self.db.query(OrderModel).filter(OrderModel.id == order_id).first()
        if db_order:
            update_data = order_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_order, key, value)
            self.db.commit()
            self.db.refresh(db_order)
        return db_order

    def delete(self, order_id: uuid.UUID) -> bool:
        db_order = self.db.query(OrderModel).filter(OrderModel.id == order_id).first()
        if db_order:
            self.db.delete(db_order)
            self.db.commit()
            return True
        return False