from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class TrainingPairHashtagBase(BaseModel):
    hashtag: str

class TrainingPairHashtagCreate(TrainingPairHashtagBase):
    pass

class TrainingPairHashtagOut(TrainingPairHashtagBase):
    id: UUID
    training_pair_id: UUID
    created_at: Optional[datetime]
    created_by: Optional[str]
    updated_at: Optional[datetime]
    updated_by: Optional[str]
    
    model_config = {"from_attributes": True}

class HookVariantBase(BaseModel):
    hook_variant: Optional[int]
    scene_number: Optional[int]
    scene_type: Optional[str]
    timestamp: Optional[str]
    text_overlay: Optional[str]
    voiceover: Optional[str]
    visual: Optional[str]
    tip: Optional[str]
    order_index: Optional[int]

class HookVariantCreate(HookVariantBase):
    pass

class HookVariantOut(HookVariantBase):
    id: UUID
    created_at: Optional[datetime]
    created_by: Optional[str]
    updated_at: Optional[datetime]
    updated_by: Optional[str]
    
    model_config = {"from_attributes": True}

class HookVariantUpdate(BaseModel):
    hook_variant: Optional[int] = None
    scene_number: Optional[int] = None
    scene_type: Optional[str] = None
    timestamp: Optional[str] = None
    text_overlay: Optional[str] = None
    voiceover: Optional[str] = None
    visual: Optional[str] = None
    tip: Optional[str] = None

class SceneBase(BaseModel):
    scene_number: Optional[int]
    scene_type: Optional[str]
    timestamp: Optional[str]
    text_overlay: Optional[str]
    voiceover: Optional[str]
    visual: Optional[str]
    tip: Optional[str]
    order_index: Optional[int]

class SceneCreate(SceneBase):
    pass

class SceneOut(SceneBase):
    id: UUID
    created_at: Optional[datetime]
    created_by: Optional[str]
    updated_at: Optional[datetime]
    updated_by: Optional[str]
    
    model_config = {"from_attributes": True}

class SceneUpdate(BaseModel):
    scene_number: Optional[int] = None
    scene_type: Optional[str] = None
    timestamp: Optional[str] = None
    text_overlay: Optional[str] = None
    voiceover: Optional[str] = None
    visual: Optional[str] = None
    tip: Optional[str] = None

class TrainingPairBase(BaseModel):
    pair_id: str
    topic: Optional[str]
    category: Optional[str]
    duration_seconds: Optional[int]
    score: Optional[int]
    user_prompt: Optional[str]
    system_prompt: Optional[str]
    target_audience: Optional[str]
    content_style: Optional[str]

class TrainingPairCreate(TrainingPairBase):
    hashtags: Optional[List[str]] = None  # List of hashtag strings
    hook_variants: Optional[List[HookVariantCreate]] = None
    scenes: Optional[List[SceneCreate]] = None

class TrainingPairUpdate(BaseModel):
    pair_id: Optional[str] = None
    topic: Optional[str] = None
    category: Optional[str] = None
    duration_seconds: Optional[int] = None
    score: Optional[int] = None
    user_prompt: Optional[str] = None
    system_prompt: Optional[str] = None
    target_audience: Optional[str] = None
    content_style: Optional[str] = None
    status: Optional[str] = None

class TrainingPairOut(TrainingPairBase):
    id: UUID
    status: str
    created_at: Optional[datetime]
    created_by: Optional[str]
    updated_at: Optional[datetime]
    updated_by: Optional[str]
    
    hashtags: Optional[List[TrainingPairHashtagOut]] = None
    hook_variants: Optional[List[HookVariantOut]] = None
    scenes: Optional[List[SceneOut]] = None
    
    model_config = {"from_attributes": True}

class UserPromptUpdate(BaseModel):
    user_prompt: str
