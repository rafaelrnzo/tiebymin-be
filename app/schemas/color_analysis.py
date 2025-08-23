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
    personality: str = Field(..., example="Creative, warm, and approachable.")
    karakteristik: str = Field(..., example="Low contrast between hair, skin, and eyes.")
    is_active: bool = Field(True)
    color_tips_summary: Optional[str] = None

class ColorAnalysisCreate(ColorAnalysisBase):
    pass

class ColorAnalysisUpdate(BaseModel):
    name: Optional[str] = None
    penjelasan_color_analysis: Optional[str] = None
    make_up_tips: Optional[str] = None
    tips_warna_kulit_pakaian: Optional[str] = None
    best_colour: Optional[List[str]] = None
    worst_colour: Optional[List[str]] = None
    neutral_colour: Optional[List[str]] = None
    best_colour_combination: Optional[List[List[str]]] = None
    personality: Optional[str] = None
    karakteristik: Optional[str] = None
    is_active: Optional[bool] = None
    color_tips_summary: Optional[str] = None

class ColorAnalysis(ColorAnalysisBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True