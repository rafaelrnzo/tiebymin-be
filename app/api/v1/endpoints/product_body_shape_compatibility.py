from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from schemas.product_body_shape_compatibility import ProductBodyShapeCompatibility, ProductBodyShapeCompatibilityCreate
from repositories.product_body_shape_compatibility_repository import ProductBodyShapeCompatibilityRepository
from dependencies.dependencies import get_product_body_shape_compatibility_repository

router = APIRouter(prefix="/product-body-shape-compatibility", tags=["Product Body Shape Compatibility"])

@router.post("/", response_model=ProductBodyShapeCompatibility, status_code=status.HTTP_201_CREATED)
def create_product_body_shape_compatibility(
    compatibility_data: ProductBodyShapeCompatibilityCreate,
    repo: ProductBodyShapeCompatibilityRepository = Depends(get_product_body_shape_compatibility_repository)
):
    return repo.create(compatibility_data)

@router.get("/", response_model=List[ProductBodyShapeCompatibility])
def get_all_product_body_shape_compatibilities(
    repo: ProductBodyShapeCompatibilityRepository = Depends(get_product_body_shape_compatibility_repository)
):
    return repo.get_all()

@router.get("/{compatibility_id}", response_model=ProductBodyShapeCompatibility)
def get_product_body_shape_compatibility_by_id(
    compatibility_id: uuid.UUID,
    repo: ProductBodyShapeCompatibilityRepository = Depends(get_product_body_shape_compatibility_repository)
):
    db_compatibility = repo.get_by_id(compatibility_id)
    if db_compatibility is None:
        raise HTTPException(status_code=404, detail="Product body shape compatibility not found")
    return db_compatibility

@router.put("/{compatibility_id}", response_model=ProductBodyShapeCompatibility)
def update_product_body_shape_compatibility(
    compatibility_id: uuid.UUID,
    compatibility_data: ProductBodyShapeCompatibilityCreate,
    repo: ProductBodyShapeCompatibilityRepository = Depends(get_product_body_shape_compatibility_repository)
):
    updated_compatibility = repo.update(compatibility_id, compatibility_data)
    if updated_compatibility is None:
        raise HTTPException(status_code=404, detail="Product body shape compatibility not found")
    return updated_compatibility

@router.delete("/{compatibility_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_body_shape_compatibility(
    compatibility_id: uuid.UUID,
    repo: ProductBodyShapeCompatibilityRepository = Depends(get_product_body_shape_compatibility_repository)
):
    if not repo.delete(compatibility_id):
        raise HTTPException(status_code=404, detail="Product body shape compatibility not found")
    return