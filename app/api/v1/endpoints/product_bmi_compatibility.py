from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from schemas.product_bmi_compatibility import ProductBmiCompatibility, ProductBmiCompatibilityCreate
from repositories.product_bmi_compatibility_repository import ProductBmiCompatibilityRepository
from dependencies import get_product_bmi_compatibility_repository

router = APIRouter(prefix="/product-bmi-compatibility", tags=["Product BMI Compatibility"])

@router.post("/", response_model=ProductBmiCompatibility, status_code=status.HTTP_201_CREATED)
def create_product_bmi_compatibility(
    compatibility_data: ProductBmiCompatibilityCreate,
    repo: ProductBmiCompatibilityRepository = Depends(get_product_bmi_compatibility_repository)
):
    return repo.create(compatibility_data)

@router.get("/", response_model=List[ProductBmiCompatibility])
def get_all_product_bmi_compatibilities(
    repo: ProductBmiCompatibilityRepository = Depends(get_product_bmi_compatibility_repository)
):
    return repo.get_all()

@router.get("/{compatibility_id}", response_model=ProductBmiCompatibility)
def get_product_bmi_compatibility_by_id(
    compatibility_id: uuid.UUID,
    repo: ProductBmiCompatibilityRepository = Depends(get_product_bmi_compatibility_repository)
):
    db_compatibility = repo.get_by_id(compatibility_id)
    if db_compatibility is None:
        raise HTTPException(status_code=404, detail="Product BMI compatibility not found")
    return db_compatibility

@router.put("/{compatibility_id}", response_model=ProductBmiCompatibility)
def update_product_bmi_compatibility(
    compatibility_id: uuid.UUID,
    compatibility_data: ProductBmiCompatibilityCreate,
    repo: ProductBmiCompatibilityRepository = Depends(get_product_bmi_compatibility_repository)
):
    updated_compatibility = repo.update(compatibility_id, compatibility_data)
    if updated_compatibility is None:
        raise HTTPException(status_code=404, detail="Product BMI compatibility not found")
    return updated_compatibility

@router.delete("/{compatibility_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_bmi_compatibility(
    compatibility_id: uuid.UUID,
    repo: ProductBmiCompatibilityRepository = Depends(get_product_bmi_compatibility_repository)
):
    if not repo.delete(compatibility_id):
        raise HTTPException(status_code=404, detail="Product BMI compatibility not found")
    return