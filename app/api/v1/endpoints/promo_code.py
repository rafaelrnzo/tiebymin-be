from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from app.schemas.promo_code import PromoCode, PromoCodeCreate, PromoCodeUpdate
from app.repositories.promo_code_repository import PromoCodeRepository
from app.dependencies.dependencies import get_promo_code_repository

router = APIRouter(prefix="/promo-codes", tags=["Promo Codes"])

@router.post("/", response_model=PromoCode, status_code=status.HTTP_201_CREATED)
def create_promo_code(
    promo_data: PromoCodeCreate,
    repo: PromoCodeRepository = Depends(get_promo_code_repository)
):
    return repo.create(promo_data)

@router.get("/", response_model=List[PromoCode])
def get_all_promo_codes(
    repo: PromoCodeRepository = Depends(get_promo_code_repository)
):
    return repo.get_all()

@router.get("/{promo_id}", response_model=PromoCode)
def get_promo_code_by_id(
    promo_id: uuid.UUID,
    repo: PromoCodeRepository = Depends(get_promo_code_repository)
):
    db_promo = repo.get_by_id(promo_id)
    if db_promo is None:
        raise HTTPException(status_code=404, detail="Promo code not found")
    return db_promo

@router.put("/{promo_id}", response_model=PromoCode)
def update_promo_code(
    promo_id: uuid.UUID,
    promo_data: PromoCodeUpdate,
    repo: PromoCodeRepository = Depends(get_promo_code_repository)
):
    updated_promo = repo.update(promo_id, promo_data)
    if updated_promo is None:
        raise HTTPException(status_code=404, detail="Promo code not found")
    return updated_promo

@router.delete("/{promo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_promo_code(
    promo_id: uuid.UUID,
    repo: PromoCodeRepository = Depends(get_promo_code_repository)
):
    if not repo.delete(promo_id):
        raise HTTPException(status_code=404, detail="Promo code not found")
    return