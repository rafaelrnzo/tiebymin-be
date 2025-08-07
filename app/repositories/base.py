from abc import ABC, abstractmethod
from typing import List, Optional
import uuid
from schemas.bmi import BMICategory, BMICategoryCreate

class BMICategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[BMICategory]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: uuid.UUID) -> Optional[BMICategory]:
        pass

    @abstractmethod
    def create(self, category: BMICategoryCreate) -> BMICategory:
        pass

    @abstractmethod
    def update(self, category_id: uuid.UUID, category_data: BMICategoryCreate) -> Optional[BMICategory]:
        pass

    @abstractmethod
    def delete(self, category_id: uuid.UUID) -> bool:
        pass