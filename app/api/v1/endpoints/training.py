from fastapi import APIRouter, Depends, Query, Body, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps.auth import get_current_user
from app.services.training_service import TrainingService
from app.schemas.training import TrainingPairOut, UserPromptUpdate, HookVariantUpdate, HookVariantOut, SceneUpdate, SceneOut
from app.schemas.web_response import WebResponse
from app.db.session import get_db
from app.models.user import User
from typing import List
from app.services.export_service import export_training_jsonl
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/queue", response_model=WebResponse[List[TrainingPairOut]])
async def get_training_queue(
    page: int = Query(1, ge=1, description="Page number (starts from 1)"),
    size: int = Query(10, ge=1, le=100, description="Number of items per page"),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get training pairs queue with pagination.
    Supports prev/next navigation through page parameter.
    """
    training_service = TrainingService(db)
    return await training_service.get_training_queue(page=page, size=size)

@router.patch("/{training_pair_id}/user-prompt", response_model=TrainingPairOut)
async def update_user_prompt(
    training_pair_id: str,
    data: UserPromptUpdate = Body(...),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update user_prompt for a training pair.
    """
    if not data.user_prompt:
        raise HTTPException(status_code=400, detail="user_prompt is required")
    service = TrainingService(db)
    try:
        return await service.update_user_prompt(training_pair_id, data.user_prompt, current_user)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/hooks/{hook_variant_id}", response_model=HookVariantOut)
async def update_hook_variant(
    hook_variant_id: str,
    data: HookVariantUpdate = Body(...),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update hook variant (type, text, voiceover, tip).
    """
    service = TrainingService(db)
    try:
        return await service.update_hook_variant(hook_variant_id, data, current_user)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/scenes/{scene_id}", response_model=SceneOut)
async def update_scene(
    scene_id: str,
    data: SceneUpdate = Body(...),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update scene (title, text, voiceover).
    """
    service = TrainingService(db)
    try:
        return await service.update_scene(scene_id, data, current_user)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/rejected", response_model=WebResponse[List[dict]])
async def get_rejected_training_pairs(
    page: int = Query(1, ge=1, description="Page number (starts from 1)"),
    size: int = Query(10, ge=1, le=100, description="Number of items per page"),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get rejected training pairs with review notes (no hooks or scenes).
    """
    training_service = TrainingService(db)
    return await training_service.get_rejected_training_pairs(page=page, size=size)

@router.get("/approved", response_model=WebResponse[List[dict]])
async def get_approved_training_pairs(
    page: int = Query(1, ge=1, description="Page number (starts from 1)"),
    size: int = Query(10, ge=1, le=100, description="Number of items per page"),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get approved training pairs with review notes (no hooks or scenes).
    """
    training_service = TrainingService(db)
    return await training_service.get_approved_training_pairs(page=page, size=size)

@router.get("/export/jsonl")
async def export_training_jsonl_endpoint(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Export all approved training data to a JSONL file (one line per item) and return as download.
    """
    output_path = "training.jsonl"
    await export_training_jsonl(output_path, db)
    return FileResponse(output_path, media_type="application/jsonl", filename="training.jsonl")

@router.get("/{training_pair_id}", response_model=TrainingPairOut)
async def get_training_pair_by_id(
    training_pair_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get training pair by ID with all related data (hooks, scenes, hashtags).
    """
    training_service = TrainingService(db)
    try:
        return await training_service.get_training_pair_by_id(training_pair_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
