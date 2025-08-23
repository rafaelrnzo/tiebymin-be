import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CelebrityBase(BaseModel):
    name: str = Field(..., example="Jane Doe")
    picture_url: str = Field(..., example="https://example.com/celebrity.jpg")
    description: str = Field(..., example="An acclaimed actress known for her versatile roles.")
    similarity_text: str = Field(..., example="You have a similar jawline and warm skin tone.")
    faceshape_id: Optional[uuid.UUID] = None
    color_analysis_id: Optional[uuid.UUID] = None

class CelebrityCreate(CelebrityBase):
    pass

class CelebrityUpdate(BaseModel):
    name: Optional[str] = None
    picture_url: Optional[str] = None
    description: Optional[str] = None
    similarity_text: Optional[str] = None
    faceshape_id: Optional[uuid.UUID] = None
    color_analysis_id: Optional[uuid.UUID] = None

class Celebrity(CelebrityBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True