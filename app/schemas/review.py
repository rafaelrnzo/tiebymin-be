from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class ReviewActionBase(BaseModel):
    action: str
    notes: Optional[str] = None

class ReviewActionCreate(BaseModel):
    training_pair_id: UUID
    notes: Optional[str] = None

class ReviewActionUpdate(ReviewActionBase):
    pass

class ReviewActionOut(ReviewActionBase):
    id: UUID
    training_pair_id: UUID
    user_id: Optional[UUID]
    created_at: Optional[datetime]
    created_by: Optional[str]
    updated_at: Optional[datetime]
    updated_by: Optional[str]

    model_config = {"from_attributes": True}

class ReviewSummary(BaseModel):
    queue: int
    approved: int
    rejected: int
    reviewed: int
    progress_percent: int
