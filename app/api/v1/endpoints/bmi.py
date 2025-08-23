from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from app.schemas.bmi import BMICategory, BMICategoryCreate, BMICategoryUpdate
from app.repositories.bmi_repository import BMICategoryRepository
from app.dependencies.dependencies import get_bmi_repository

router = APIRouter(prefix="/bmi-categories", tags=["BMI Categories"])

@router.post("/", response_model=BMICategory, status_code=status.HTTP_201_CREATED)
def create_bmi_category(
    category_data: BMICategoryCreate, 
    repo: BMICategoryRepository = Depends(get_bmi_repository)
):
    return repo.create(category_data)

@router.get("/", response_model=List[BMICategory])
def get_all_bmi_categories(
    repo: BMICategoryRepository = Depends(get_bmi_repository)
):
    return repo.get_all()

@router.get("/{category_id}", response_model=BMICategory)
def get_bmi_category_by_id(
    category_id: uuid.UUID,
    repo: BMICategoryRepository = Depends(get_bmi_repository)
):
    db_category = repo.get_by_id(category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="BMI Category not found")
    return db_category

@router.put("/{category_id}", response_model=BMICategory)
def update_bmi_category(
    category_id: uuid.UUID,
    category_data: BMICategoryUpdate,
    repo: BMICategoryRepository = Depends(get_bmi_repository)
):
    updated_category = repo.update(category_id, category_data)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="BMI Category not found")
    return updated_category

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bmi_category(
    category_id: uuid.UUID,
    repo: BMICategoryRepository = Depends(get_bmi_repository)
):
    if not repo.delete(category_id):
        raise HTTPException(status_code=404, detail="BMI Category not found")
    return