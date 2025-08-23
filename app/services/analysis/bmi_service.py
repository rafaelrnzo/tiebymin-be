from typing import Optional
from repositories.bmi_repository import BMICategoryRepository
from schemas.bmi import BMICategory

class BMIService:
    def __init__(self, bmi_repo: BMICategoryRepository):
        self.bmi_repo = bmi_repo

    def classify_bmi(self, bmi: float) -> Optional[BMICategory]:
        return self.bmi_repo.find_by_bmi_value(bmi)

    def calculate_bmi(self, weight_kg: float, height_cm: float) -> dict:
        if height_cm <= 0:
            raise ValueError("Height must be a positive number.")
        
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        
        category_record = self.classify_bmi(bmi)

        return {
            "weight_kg": weight_kg,
            "height_cm": height_cm,
            "bmi": round(bmi, 2),
            "category": category_record.dict() if category_record else None
        }
