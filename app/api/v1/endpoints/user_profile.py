from fastapi import APIRouter, Depends, Query, HTTPException, status
import uuid
from typing import Dict, Any, List

from app.schemas.user import User as UserSchema
from app.schemas.user_profile import UserInfo, PaginatedAnalysisHistory, AnalysisHistoryItem, ChangePasswordRequest
from app.repositories.user_analysis_result_repository import UserAnalysisResultRepository
from app.repositories.user_repository import UserRepository
from app.dependencies.dependencies import get_user_analysis_result_repository, get_user_repository
from app.api.v1.endpoints.auth import get_current_user, verify_password, get_password_hash

router = APIRouter(prefix="/user-profile", tags=["User Profile"])

@router.get("/user-info", response_model=UserInfo)
def get_user_info(current_user: UserSchema = Depends(get_current_user)):
    return UserInfo(
        user_id=current_user.id,
        user_full_name=f"{current_user.first_name} {current_user.last_name}",
        user_first_name=current_user.first_name
    )

@router.get("/analysis-history", response_model=PaginatedAnalysisHistory)
def get_analysis_history(
    current_user: UserSchema = Depends(get_current_user),
    repo: UserAnalysisResultRepository = Depends(get_user_analysis_result_repository),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    total_items = repo.count_by_user_id(user_id=current_user.id)
    history_items_db = repo.get_by_user_id_paginated(user_id=current_user.id, skip=skip, limit=limit)
    
    formatted_items = [
        AnalysisHistoryItem(
            analysis_id=item.id,
            analysis_date=item.analyzed_at.strftime("%d %B %Y, %H:%M")
        ) for item in history_items_db
    ]

    return PaginatedAnalysisHistory(
        total_items=total_items,
        items=formatted_items,
        limit=limit,
        skip=skip
    )

@router.put("/change-password", status_code=status.HTTP_204_NO_CONTENT)
def change_password(
    request: ChangePasswordRequest,
    current_user: UserSchema = Depends(get_current_user),
    repo: UserRepository = Depends(get_user_repository)
):
    if not current_user.password_hash:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not have a password set (e.g., signed up with Google).",
        )

    if not verify_password(request.old_password, current_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect old password",
        )
    
    new_hashed_password = get_password_hash(request.new_password)
    
    success = repo.update_password(
        user_id=current_user.id,
        new_password_hash=new_hashed_password
    )
    
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
        
    return