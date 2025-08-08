import uuid
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class UserPhotoBase(BaseModel):
    analysis_result_id: uuid.UUID
    photo_type: str = Field(..., example="face")
    file_path: str
    original_filename: str
    file_size: int
    mime_type: str
    is_processed: bool = Field(False)
    analysis_metadata: Optional[Dict[str, Any]] = None
    processed_at: Optional[datetime] = None

class UserPhotoCreate(UserPhotoBase):
    pass

class UserPhoto(UserPhotoBase):
    id: uuid.UUID
    uploaded_at: datetime

    class Config:
        orm_mode = True