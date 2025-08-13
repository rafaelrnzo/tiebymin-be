import uuid
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ColorAnalysisBase(BaseModel):
    name: str = Field(..., example="Warm Autumn")
    penjelasan_color_analysis: str = Field(..., example="A season characterized by warm, muted colors.")
    make_up_tips: str = Field(..., example="Focus on earthy tones like bronze and copper.")
    tips_warna_kulit_pakaian: str = Field(..., example="Wear colors like mustard yellow and olive green.")
    best_colour: List[str] = Field(..., example=["#DAA520", "#BDB76B"])
    worst_colour: List[str] = Field(..., example=["#0000FF", "#FF00FF"])
    neutral_colour: List[str] = Field(..., example=["#F5F5DC", "#A0522D"])
    best_colour_combination: List[List[str]] = Field(..., example=[["#556B2F", "#E2725B"], ["#8B4513", "#FFFDD0"]])
    color_tips_summary: Optional[str] = Field(None, example="Choose colors that complement your warm undertones.")
    personality: str = Field(..., example="Creative, warm, and approachable.")
    karakteristik: str = Field(..., example="Low contrast between hair, skin, and eyes.")
    is_active: bool = Field(True)

class ColorAnalysisCreate(ColorAnalysisBase):
    pass

class ColorAnalysis(ColorAnalysisBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True