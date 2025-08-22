from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List
from uuid import UUID

from app.db.session import get_db
from app.services.evaluation_service import EvaluationService
from app.schemas.evaluation import (
    EvaluationComparisonResponse,
    UserPreferenceCreate,
    UserPreferenceResponse,
    EvaluationPairResponse,
    EvaluationProgressResponse,
    TrainingPairSetResponse
)
from app.schemas.web_response import WebResponse
from app.api.deps.auth import get_current_user_optional, get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/compare", response_model=WebResponse[EvaluationComparisonResponse])
async def get_comparison_data(
    pair_id: Optional[str] = Query(
        default=None,
        description="Pair ID spesifik untuk evaluasi. Jika tidak diberikan, akan mengambil secara random"
    ),
    include_progress: bool = Query(
        default=False,
        description="Apakah menyertakan informasi progress evaluasi"
    ),
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user_optional)
):
    """
    Endpoint untuk mendapatkan data perbandingan antara baseline dan fine-tuned model.
    
    **Parameter:**
    - `pair_id`: Pair ID spesifik (opsional, jika tidak ada akan random)
    - `include_progress`: Menyertakan informasi progress evaluasi (default: false)
    
    **Response:**
    - Data perbandingan baseline vs fine-tuned model
    - Progress evaluasi (jika include_progress=true dan user terautentikasi)
    """
    try:
        evaluation_service = EvaluationService(db)
        
        # Mendapatkan data perbandingan
        if pair_id:
            comparison = await evaluation_service.get_evaluation_comparison(pair_id)
        else:
            comparison = await evaluation_service.get_random_evaluation_comparison()
        
        if not comparison:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tidak ada data perbandingan yang ditemukan"
            )
        
        # Jika diminta progress dan user terautentikasi
        if include_progress and current_user:
            progress = await evaluation_service.get_evaluation_progress(current_user.id)
            return WebResponse(
                code=200,
                status="OK",
                data={
                    "comparison": comparison,
                    "progress": progress
                }
            )

        return WebResponse(
            code=200,
            status="OK",
            data=comparison
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )

@router.post("/preference", response_model=WebResponse[UserPreferenceResponse])
async def submit_user_preference(
    preference_data: UserPreferenceCreate,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user_optional)
):
    """
    Endpoint untuk menyimpan preferensi user untuk training pair tertentu.
    
    **Body:**
    - `training_pair_set_id`: ID training pair set
    - `selected_training_pair_id`: ID training pair yang dipilih user
    - `preference_reason`: Alasan preferensi (opsional)
    
    **Response:**
    - Data preferensi yang tersimpan
    """
    evaluation_service = EvaluationService(db)
    
    user_id = current_user.id if current_user else None
    
    try:
        preference = await evaluation_service.create_user_preference(user_id, preference_data)
        return WebResponse(
            code=201,
            status="success",
            message="User preference submitted successfully",
            data=preference
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to submit preference: {str(e)}"
        )

@router.get("/preferences", response_model=WebResponse[List[UserPreferenceResponse]])
async def get_user_preferences(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Endpoint untuk mendapatkan semua preferensi user.
    
    **Response:**
    - List semua preferensi user
    """
    evaluation_service = EvaluationService(db)
    
    preferences = await evaluation_service.get_user_preferences(current_user.id)
    return WebResponse(
        code=200,
        status="success",
        message="User preferences retrieved successfully",
        data=preferences
    )

@router.get("/progress", response_model=WebResponse[EvaluationProgressResponse])
async def get_evaluation_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Endpoint untuk mendapatkan progress evaluasi user.
    
    **Response:**
    - Progress evaluasi user
    """
    evaluation_service = EvaluationService(db)
    
    progress = await evaluation_service.get_evaluation_progress(current_user.id)
    return WebResponse(
        code=200,
        status="success",
        message="Evaluation progress retrieved successfully",
        data=progress
    )

@router.get("/pair", response_model=WebResponse[EvaluationPairResponse])
async def get_evaluation_pair(
    pair_id: Optional[str] = Query(
        default=None,
        description="Pair ID spesifik untuk evaluasi. Jika tidak diberikan, akan mengambil secara random"
    ),
    db: Session = Depends(get_db)
):
    """
    Endpoint untuk mendapatkan data evaluasi untuk UI dengan informasi tambahan.
    
    **Parameter:**
    - `pair_id`: Pair ID spesifik (opsional, jika tidak ada akan random)
    
    **Response:**
    - Data evaluasi dengan informasi tambahan untuk UI
    """
    evaluation_service = EvaluationService(db)
    
    evaluation_pair = await evaluation_service.get_evaluation_pair_for_ui(pair_id)
    
    if not evaluation_pair:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tidak ada data evaluasi yang ditemukan"
        )
    
    return WebResponse(
        code=200,
        status="success",
        message="Evaluation pair data retrieved successfully",
        data=evaluation_pair
    )

@router.get("/reviewed", response_model=WebResponse[List[TrainingPairSetResponse]])
async def get_reviewed_training_pairs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Endpoint untuk mendapatkan training pair yang sudah direview oleh user.
    
    **Response:**
    - List training pair yang sudah direview
    """
    evaluation_service = EvaluationService(db)
    
    reviewed_pairs = await evaluation_service.get_reviewed_training_pairs(current_user.id)
    return WebResponse(
        code=200,
        status="success",
        message="Reviewed training pairs retrieved successfully",
        data=reviewed_pairs
    ) 