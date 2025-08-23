from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from app.schemas.celebrity import Celebrity, CelebrityCreate, CelebrityUpdate
from app.repositories.celebrity_repository import CelebrityRepository
from app.dependencies.dependencies import get_celebrity_repository

router = APIRouter(prefix="/celebrities", tags=["Celebrities"])

@router.post("/", response_model=Celebrity, status_code=status.HTTP_201_CREATED)
def create_celebrity(
    celebrity_data: CelebrityCreate,
    repo: CelebrityRepository = Depends(get_celebrity_repository)
):
    return repo.create(celebrity_data)

@router.get("/", response_model=List[Celebrity])
def get_all_celebrities(
    repo: CelebrityRepository = Depends(get_celebrity_repository)
):
    return repo.get_all()

@router.get("/{celebrity_id}", response_model=Celebrity)
def get_celebrity_by_id(
    celebrity_id: uuid.UUID,
    repo: CelebrityRepository = Depends(get_celebrity_repository)
):
    db_celebrity = repo.get_by_id(celebrity_id)
    if db_celebrity is None:
        raise HTTPException(status_code=404, detail="Celebrity not found")
    return db_celebrity

@router.put("/{celebrity_id}", response_model=Celebrity)
def update_celebrity(
    celebrity_id: uuid.UUID,
    celebrity_data: CelebrityUpdate,
    repo: CelebrityRepository = Depends(get_celebrity_repository)
):
    updated_celebrity = repo.update(celebrity_id, celebrity_data)
    if updated_celebrity is None:
        raise HTTPException(status_code=404, detail="Celebrity not found")
    return updated_celebrity

@router.delete("/{celebrity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_celebrity(
    celebrity_id: uuid.UUID,
    repo: CelebrityRepository = Depends(get_celebrity_repository)
):
    if not repo.delete(celebrity_id):
        raise HTTPException(status_code=404, detail="Celebrity not found")
    return