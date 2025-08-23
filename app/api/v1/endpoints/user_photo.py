from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from app.schemas.user_photo import UserPhoto, UserPhotoCreate, UserPhotoUpdate
from app.repositories.user_photo_repository import UserPhotoRepository
from app.dependencies.dependencies import get_user_photo_repository

router = APIRouter(prefix="/user-photos", tags=["User Photos"])

@router.post("/", response_model=UserPhoto, status_code=status.HTTP_201_CREATED)
def create_user_photo_record(
    photo_data: UserPhotoCreate,
    repo: UserPhotoRepository = Depends(get_user_photo_repository)
):
    return repo.create(photo_data)

@router.get("/", response_model=List[UserPhoto])
def get_all_user_photo_records(
    repo: UserPhotoRepository = Depends(get_user_photo_repository)
):
    return repo.get_all()

@router.get("/{photo_id}", response_model=UserPhoto)
def get_user_photo_record_by_id(
    photo_id: uuid.UUID,
    repo: UserPhotoRepository = Depends(get_user_photo_repository)
):
    db_photo = repo.get_by_id(photo_id)
    if db_photo is None:
        raise HTTPException(status_code=404, detail="User photo record not found")
    return db_photo

@router.get("/analysis/{analysis_result_id}", response_model=List[UserPhoto])
def get_user_photos_by_analysis_id(
    analysis_result_id: uuid.UUID,
    repo: UserPhotoRepository = Depends(get_user_photo_repository)
):
    return repo.get_by_analysis_result_id(analysis_result_id)

@router.put("/{photo_id}", response_model=UserPhoto)
def update_user_photo_record(
    photo_id: uuid.UUID,
    photo_data: UserPhotoUpdate,
    repo: UserPhotoRepository = Depends(get_user_photo_repository)
):
    updated_photo = repo.update(photo_id, photo_data)
    if updated_photo is None:
        raise HTTPException(status_code=404, detail="User photo record not found")
    return updated_photo

@router.delete("/{photo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_photo_record(
    photo_id: uuid.UUID,
    repo: UserPhotoRepository = Depends(get_user_photo_repository)
):
    if not repo.delete(photo_id):
        raise HTTPException(status_code=404, detail="User photo record not found")
    return