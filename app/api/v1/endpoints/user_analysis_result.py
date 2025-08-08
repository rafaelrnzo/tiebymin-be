from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from schemas.user_analysis_result import UserAnalysisResult, UserAnalysisResultCreate
from repositories.user_analysis_result_repository import UserAnalysisResultRepository
from dependencies.dependencies import get_user_analysis_result_repository

router = APIRouter(prefix="/user-analysis-results", tags=["User Analysis Results"])

@router.post("/", response_model=UserAnalysisResult, status_code=status.HTTP_201_CREATED)
def create_user_analysis_result(
    result_data: UserAnalysisResultCreate,
    repo: UserAnalysisResultRepository = Depends(get_user_analysis_result_repository)
):
    return repo.create(result_data)

@router.get("/", response_model=List[UserAnalysisResult])
def get_all_user_analysis_results(
    repo: UserAnalysisResultRepository = Depends(get_user_analysis_result_repository)
):
    return repo.get_all()

@router.get("/{result_id}", response_model=UserAnalysisResult)
def get_user_analysis_result_by_id(
    result_id: uuid.UUID,
    repo: UserAnalysisResultRepository = Depends(get_user_analysis_result_repository)
):
    db_result = repo.get_by_id(result_id)
    if db_result is None:
        raise HTTPException(status_code=404, detail="User analysis result not found")
    return db_result

@router.put("/{result_id}", response_model=UserAnalysisResult)
def update_user_analysis_result(
    result_id: uuid.UUID,
    result_data: UserAnalysisResultCreate,
    repo: UserAnalysisResultRepository = Depends(get_user_analysis_result_repository)
):
    updated_result = repo.update(result_id, result_data)
    if updated_result is None:
        raise HTTPException(status_code=404, detail="User analysis result not found")
    return updated_result

@router.delete("/{result_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_analysis_result(
    result_id: uuid.UUID,
    repo: UserAnalysisResultRepository = Depends(get_user_analysis_result_repository)
):
    if not repo.delete(result_id):
        raise HTTPException(status_code=404, detail="User analysis result not found")
    return