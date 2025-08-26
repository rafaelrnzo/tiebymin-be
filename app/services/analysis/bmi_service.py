from typing import Optional, Dict, Any
from app.repositories.bmi_repository import BMICategoryRepository
from app.models.bmi_categories import BMICategoryModel


class BMIService:
    def __init__(self, bmi_repo: BMICategoryRepository):
        self.bmi_repo = bmi_repo

    def classify_bmi(self, bmi: float) -> Optional[BMICategoryModel]:
        """Find BMI category based on value (returns ORM model)."""
        return self.bmi_repo.find_by_bmi_value(bmi)

    def calculate_bmi_value(self, weight_kg: float, height_cm: float) -> float:
        """Calculate BMI value (just the number)."""
        if height_cm <= 0:
            raise ValueError("Height must be a positive number.")
        height_m = height_cm / 100
        return round(weight_kg / (height_m ** 2), 2)

    def calculate_bmi(self, weight_kg: float, height_cm: float) -> Dict[str, Any]:
        """Calculate BMI and return structured dict with category details."""
        bmi = self.calculate_bmi_value(weight_kg, height_cm)
        category_record = self.classify_bmi(bmi)

        return {
            "weight_kg": weight_kg,
            "height_cm": height_cm,
            "bmi": bmi,
            "bmi_category_id": str(category_record.id) if category_record else None,
            "category": {
                "id": str(category_record.id),
                "kategori": category_record.kategori,
                "tips_fashion": category_record.tips_fashion,
                "bmi_tips_summary": category_record.bmi_tips_summary
            } if category_record else None
        }
