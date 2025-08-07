from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from schemas.color_analysis import ColorAnalysis, ColorAnalysisCreate
from repositories.color_analysis_repository import ColorAnalysisRepository
from dependencies.dependencies import get_color_analysis_repository

router = APIRouter(prefix="/v1/color-analysis", tags=["Color Analysis"])

@router.post("/", response_model=ColorAnalysis, status_code=status.HTTP_201_CREATED)
def create_color_analysis(
    analysis_data: ColorAnalysisCreate,
    repo: ColorAnalysisRepository = Depends(get_color_analysis_repository)
):
    return repo.create(analysis_data)

@router.get("/", response_model=List[ColorAnalysis])
def get_all_color_analyses(
    repo: ColorAnalysisRepository = Depends(get_color_analysis_repository)
):
    return repo.get_all()

@router.get("/{analysis_id}", response_model=ColorAnalysis)
def get_color_analysis_by_id(
    analysis_id: uuid.UUID,
    repo: ColorAnalysisRepository = Depends(get_color_analysis_repository)
):
    db_analysis = repo.get_by_id(analysis_id)
    if db_analysis is None:
        raise HTTPException(status_code=404, detail="Color analysis not found")
    return db_analysis

@router.put("/{analysis_id}", response_model=ColorAnalysis)
def update_color_analysis(
    analysis_id: uuid.UUID,
    analysis_data: ColorAnalysisCreate,
    repo: ColorAnalysisRepository = Depends(get_color_analysis_repository)
):
    updated_analysis = repo.update(analysis_id, analysis_data)
    if updated_analysis is None:
        raise HTTPException(status_code=404, detail="Color analysis not found")
    return updated_analysis

@router.delete("/{analysis_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_color_analysis(
    analysis_id: uuid.UUID,
    repo: ColorAnalysisRepository = Depends(get_color_analysis_repository)
):
    if not repo.delete(analysis_id):
        raise HTTPException(status_code=404, detail="Color analysis not found")
    return