from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/bmi",
    tags=["BMI Classification"]
)

class BMIInput(BaseModel):
    weight_kg: float = Field(..., ge=0.1, description="Berat badan dalam kilogram (kg)")
    height_cm: float = Field(..., ge=30, description="Tinggi badan dalam centimeter (cm)")

def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obesity"

@router.post("/calculate")
async def calculate_bmi(data: BMIInput):
    try:
        height_m = data.height_cm / 100  # Konversi dari cm ke meter
        bmi_value = data.weight_kg / (height_m ** 2)
        category = classify_bmi(bmi_value)

        return {
            "weight_kg": data.weight_kg,
            "height_cm": data.height_cm,
            "bmi": round(bmi_value, 2),
            "category": category,
            "gender": "Female"  # Hardcoded, ubah kalau perlu dinamis
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Terjadi kesalahan: {str(e)}")
