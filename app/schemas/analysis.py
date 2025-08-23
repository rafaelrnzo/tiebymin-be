from pydantic import BaseModel
from typing import Optional, Dict
from uuid import UUID
from datetime import datetime


class AnalysisRequest(BaseModel):
    tinggi_badan: float
    berat_badan: float
    umur: int
    body_shape_type: str  # pear, diamond, etc.


class PhotoMetadata(BaseModel):
    id: UUID
    analysis_result_id: UUID
    photo_type: str
    file_path: str
    original_filename: str
    file_size: int
    mime_type: str
    is_processed: bool
    analysis_metadata: Optional[Dict] = {}
    uploaded_at: datetime
    processed_at: Optional[datetime]
