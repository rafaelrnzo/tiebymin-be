from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from app.schemas.order import Order, OrderCreate, OrderUpdate
from app.repositories.order_repository import OrderRepository
from app.dependencies.dependencies import get_order_repository

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(
    order_data: OrderCreate,
    repo: OrderRepository = Depends(get_order_repository)
):
    return repo.create(order_data)

@router.get("/", response_model=List[Order])
def get_all_orders(
    repo: OrderRepository = Depends(get_order_repository)
):
    return repo.get_all()

@router.get("/{order_id}", response_model=Order)
def get_order_by_id(
    order_id: uuid.UUID,
    repo: OrderRepository = Depends(get_order_repository)
):
    db_order = repo.get_by_id(order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/{order_id}", response_model=Order)
def update_order(
    order_id: uuid.UUID,
    order_data: OrderUpdate,
    repo: OrderRepository = Depends(get_order_repository)
):
    updated_order = repo.update(order_id, order_data)
    if updated_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(
    order_id: uuid.UUID,
    repo: OrderRepository = Depends(get_order_repository)
):
    if not repo.delete(order_id):
        raise HTTPException(status_code=404, detail="Order not found")
    return