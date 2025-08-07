# services/bmi_service.py

class BMIService:
    @staticmethod
    def classify_bmi(bmi: float) -> str:
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25.0:
            return "Normal weight"
        elif 25.0 <= bmi < 30.0:
            return "Overweight"
        else:
            return "Obesity"

    @staticmethod
    def calculate_bmi(weight_kg: float, height_cm: float) -> dict:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        category = BMIService.classify_bmi(bmi)

        return {
            "weight_kg": weight_kg,
            "height_cm": height_cm,
            "bmi": round(bmi, 2),
            "category": category
        }
