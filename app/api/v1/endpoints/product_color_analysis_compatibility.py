from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from schemas.product_color_analysis_compatibility import ProductColorAnalysisCompatibility, ProductColorAnalysisCompatibilityCreate
from repositories.product_color_analysis_compatibility_repository import ProductColorAnalysisCompatibilityRepository
from dependencies.dependencies import get_product_color_analysis_compatibility_repository

router = APIRouter(prefix="/product-color-analysis-compatibility", tags=["Product Color Analysis Compatibility"])

@router.post("/", response_model=ProductColorAnalysisCompatibility, status_code=status.HTTP_201_CREATED)
def create_product_color_analysis_compatibility(
    compatibility_data: ProductColorAnalysisCompatibilityCreate,
    repo: ProductColorAnalysisCompatibilityRepository = Depends(get_product_color_analysis_compatibility_repository)
):
    return repo.create(compatibility_data)

@router.get("/", response_model=List[ProductColorAnalysisCompatibility])
def get_all_product_color_analysis_compatibilities(
    repo: ProductColorAnalysisCompatibilityRepository = Depends(get_product_color_analysis_compatibility_repository)
):
    return repo.get_all()

@router.get("/{compatibility_id}", response_model=ProductColorAnalysisCompatibility)
def get_product_color_analysis_compatibility_by_id(
    compatibility_id: uuid.UUID,
    repo: ProductColorAnalysisCompatibilityRepository = Depends(get_product_color_analysis_compatibility_repository)
):
    db_compatibility = repo.get_by_id(compatibility_id)
    if db_compatibility is None:
        raise HTTPException(status_code=404, detail="Product color analysis compatibility not found")
    return db_compatibility

@router.put("/{compatibility_id}", response_model=ProductColorAnalysisCompatibility)
def update_product_color_analysis_compatibility(
    compatibility_id: uuid.UUID,
    compatibility_data: ProductColorAnalysisCompatibilityCreate,
    repo: ProductColorAnalysisCompatibilityRepository = Depends(get_product_color_analysis_compatibility_repository)
):
    updated_compatibility = repo.update(compatibility_id, compatibility_data)
    if updated_compatibility is None:
        raise HTTPException(status_code=404, detail="Product color analysis compatibility not found")
    return updated_compatibility

@router.delete("/{compatibility_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_color_analysis_compatibility(
    compatibility_id: uuid.UUID,
    repo: ProductColorAnalysisCompatibilityRepository = Depends(get_product_color_analysis_compatibility_repository)
):
    if not repo.delete(compatibility_id):
        raise HTTPException(status_code=404, detail="Product color analysis compatibility not found")
    return