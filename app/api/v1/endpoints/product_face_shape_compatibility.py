from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from schemas.product_face_shape_compatibility import ProductFaceShapeCompatibility, ProductFaceShapeCompatibilityCreate
from repositories.product_face_shape_compatibility_repository import ProductFaceShapeCompatibilityRepository
from dependencies import get_product_face_shape_compatibility_repository

router = APIRouter(prefix="/product-face-shape-compatibility", tags=["Product Face Shape Compatibility"])

@router.post("/", response_model=ProductFaceShapeCompatibility, status_code=status.HTTP_201_CREATED)
def create_product_face_shape_compatibility(
    compatibility_data: ProductFaceShapeCompatibilityCreate,
    repo: ProductFaceShapeCompatibilityRepository = Depends(get_product_face_shape_compatibility_repository)
):
    return repo.create(compatibility_data)

@router.get("/", response_model=List[ProductFaceShapeCompatibility])
def get_all_product_face_shape_compatibilities(
    repo: ProductFaceShapeCompatibilityRepository = Depends(get_product_face_shape_compatibility_repository)
):
    return repo.get_all()

@router.get("/{compatibility_id}", response_model=ProductFaceShapeCompatibility)
def get_product_face_shape_compatibility_by_id(
    compatibility_id: uuid.UUID,
    repo: ProductFaceShapeCompatibilityRepository = Depends(get_product_face_shape_compatibility_repository)
):
    db_compatibility = repo.get_by_id(compatibility_id)
    if db_compatibility is None:
        raise HTTPException(status_code=404, detail="Product face shape compatibility not found")
    return db_compatibility

@router.put("/{compatibility_id}", response_model=ProductFaceShapeCompatibility)
def update_product_face_shape_compatibility(
    compatibility_id: uuid.UUID,
    compatibility_data: ProductFaceShapeCompatibilityCreate,
    repo: ProductFaceShapeCompatibilityRepository = Depends(get_product_face_shape_compatibility_repository)
):
    updated_compatibility = repo.update(compatibility_id, compatibility_data)
    if updated_compatibility is None:
        raise HTTPException(status_code=404, detail="Product face shape compatibility not found")
    return updated_compatibility

@router.delete("/{compatibility_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_face_shape_compatibility(
    compatibility_id: uuid.UUID,
    repo: ProductFaceShapeCompatibilityRepository = Depends(get_product_face_shape_compatibility_repository)
):
    if not repo.delete(compatibility_id):
        raise HTTPException(status_code=404, detail="Product face shape compatibility not found")
    return