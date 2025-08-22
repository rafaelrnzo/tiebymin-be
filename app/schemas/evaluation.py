from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID

class TrainingPairSetBase(BaseModel):
    pair_id: str
    user_prompt: Optional[str] = None
    system_prompt: Optional[str] = None
    review_status: Optional[str] = "QUEUE"
    reviewed_at: Optional[datetime] = None
    reviewed_by: Optional[str] = None

class TrainingPairSetResponse(TrainingPairSetBase):
    id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True

class GeneratedHookVariantBase(BaseModel):
    hook_variant: Optional[int] = None
    scene_number: Optional[int] = None
    scene_type: Optional[str] = None
    timestamp: Optional[str] = None
    text_overlay: Optional[str] = None
    voiceover: Optional[str] = None
    visual: Optional[str] = None
    tip: Optional[str] = None
    order_index: Optional[int] = None

class GeneratedHookVariantResponse(GeneratedHookVariantBase):
    id: UUID
    training_pair_id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True

class GeneratedSceneBase(BaseModel):
    scene_number: Optional[int] = None
    scene_type: Optional[str] = None
    timestamp: Optional[str] = None
    text_overlay: Optional[str] = None
    voiceover: Optional[str] = None
    visual: Optional[str] = None
    tip: Optional[str] = None
    order_index: Optional[int] = None

class GeneratedSceneResponse(GeneratedSceneBase):
    id: UUID
    training_pair_id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True

class GeneratedTrainingPairBase(BaseModel):
    prompt: str
    topic: Optional[str] = None
    category: Optional[str] = None
    duration_seconds: Optional[int] = None
    score: Optional[int] = None
    target_audience: Optional[str] = None
    content_style: Optional[str] = None

class GeneratedTrainingPairResponse(GeneratedTrainingPairBase):
    id: UUID
    training_pair_set_id: UUID
    ai_model_id: UUID
    created_at: datetime
    generated_hook_variants: List[GeneratedHookVariantResponse] = []
    generated_scenes: List[GeneratedSceneResponse] = []
    
    class Config:
        from_attributes = True

class EvaluationComparisonResponse(BaseModel):
    training_pair_a: GeneratedTrainingPairResponse
    training_pair_b: GeneratedTrainingPairResponse
    training_pair_set: TrainingPairSetResponse
    
    class Config:
        from_attributes = True

class UserPreferenceCreate(BaseModel):
    training_pair_set_id: UUID
    selected_training_pair_id: UUID
    preference_reason: Optional[str] = None

class UserPreferenceResponse(BaseModel):
    id: UUID
    user_id: Optional[UUID] = None
    training_pair_set_id: UUID
    selected_training_pair_id: UUID
    preference_reason: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

class EvaluationPairResponse(BaseModel):
    """
    Response khusus untuk UI evaluasi dengan informasi yang lebih detail
    """
    training_pair_set: TrainingPairSetResponse
    script_a: GeneratedTrainingPairResponse
    script_b: GeneratedTrainingPairResponse
    total_available_pairs: int
    current_pair_index: int
    
    class Config:
        from_attributes = True

class EvaluationProgressResponse(BaseModel):
    """
    Response untuk progress evaluasi
    """
    total_pairs: int
    evaluated_pairs: int
    remaining_pairs: int
    progress_percentage: float
    
    class Config:
        from_attributes = True 