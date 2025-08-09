from typing import Optional
from repositories.bmi_repository import BMICategoryRepository
from schemas.bmi import BMICategory
import uuid

class BMIService:
    def __init__(self, bmi_repo: BMICategoryRepository):
        self.bmi_repo = bmi_repo

    def calculate_bmi_value(self, weight_kg: float, height_cm: float) -> float:
        if height_cm <= 0:
            raise ValueError("Height must be a positive number.")
        
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        return round(bmi, 2)

    def get_bmi_category_id(self, bmi: float) -> Optional[uuid.UUID]:
        return self.bmi_repo.find_category_id_by_bmi_value(bmi)