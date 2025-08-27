from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from app.schemas.product import Product, ProductCreate, ProductUpdate
from app.repositories.product_repository import ProductRepository
from app.dependencies.dependencies import get_product_repository

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(
    product_data: ProductCreate,
    repo: ProductRepository = Depends(get_product_repository)
):
    return repo.create(product_data)

@router.get("/", response_model=List[Product])
def get_all_products(
    repo: ProductRepository = Depends(get_product_repository)
):
    return repo.get_all()

@router.get("/{product_id}", response_model=Product)
def get_product_by_id(
    product_id: uuid.UUID,
    repo: ProductRepository = Depends(get_product_repository)
):
    db_product = repo.get_by_id(product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/{product_id}", response_model=Product)
def update_product(
    product_id: uuid.UUID,
    product_data: ProductUpdate,
    repo: ProductRepository = Depends(get_product_repository)
):
    updated_product = repo.update(product_id, product_data)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: uuid.UUID,
    repo: ProductRepository = Depends(get_product_repository)
):
    if not repo.delete(product_id):
        raise HTTPException(status_code=404, detail="Product not found")
    return