from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from app.schemas.product_color import ProductColor, ProductColorCreate, ProductColorUpdate
from app.repositories.product_color_repository import ProductColorRepository
from app.dependencies.dependencies import get_product_color_repository

router = APIRouter(prefix="/product-colors", tags=["Product Colors"])

@router.post("/", response_model=ProductColor, status_code=status.HTTP_201_CREATED)
def create_product_color(
    color_data: ProductColorCreate,
    repo: ProductColorRepository = Depends(get_product_color_repository)
):
    return repo.create(color_data)

@router.get("/", response_model=List[ProductColor])
def get_all_product_colors(
    repo: ProductColorRepository = Depends(get_product_color_repository)
):
    return repo.get_all()

@router.get("/{color_id}", response_model=ProductColor)
def get_product_color_by_id(
    color_id: uuid.UUID,
    repo: ProductColorRepository = Depends(get_product_color_repository)
):
    db_color = repo.get_by_id(color_id)
    if db_color is None:
        raise HTTPException(status_code=404, detail="Product color not found")
    return db_color

@router.put("/{color_id}", response_model=ProductColor)
def update_product_color(
    color_id: uuid.UUID,
    color_data: ProductColorUpdate,
    repo: ProductColorRepository = Depends(get_product_color_repository)
):
    updated_color = repo.update(color_id, color_data)
    if updated_color is None:
        raise HTTPException(status_code=404, detail="Product color not found")
    return updated_color

@router.delete("/{color_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_color(
    color_id: uuid.UUID,
    repo: ProductColorRepository = Depends(get_product_color_repository)
):
    if not repo.delete(color_id):
        raise HTTPException(status_code=404, detail="Product color not found")
    return