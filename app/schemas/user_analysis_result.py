import uuid
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class UserAnalysisResultBase(BaseModel):
    user_id: uuid.UUID
    face_shape_id: Optional[uuid.UUID] = None
    body_shape_id: Optional[uuid.UUID] = None
    color_analysis_id: Optional[uuid.UUID] = None
    bmi_category_id: Optional[uuid.UUID] = None
    celebrity_id: Optional[uuid.UUID] = None
    analysis_details: Optional[Dict[str, Any]] = None
    is_final_result: bool = Field(False)

class UserAnalysisResultCreate(UserAnalysisResultBase):
    pass

class UserAnalysisResultUpdate(BaseModel):
    face_shape_id: Optional[uuid.UUID] = None
    body_shape_id: Optional[uuid.UUID] = None
    color_analysis_id: Optional[uuid.UUID] = None
    bmi_category_id: Optional[uuid.UUID] = None
    celebrity_id: Optional[uuid.UUID] = None
    analysis_details: Optional[Dict[str, Any]] = None
    is_final_result: Optional[bool] = None

class UserAnalysisResult(UserAnalysisResultBase):
    id: uuid.UUID
    analyzed_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True