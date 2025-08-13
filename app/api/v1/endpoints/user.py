from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from schemas.user import User, UserCreate, UserUpdate
from repositories.user_repository import UserRepository
from dependencies.dependencies import get_user_repository

router = APIRouter(prefix="/v1/users", tags=["Users"])

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(
    user_data: UserCreate,
    repo: UserRepository = Depends(get_user_repository)
):
    db_user = repo.get_by_email(user_data.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    return repo.create(user_data)

@router.get("/", response_model=List[User])
def get_all_users(
    repo: UserRepository = Depends(get_user_repository)
):
    return repo.get_all()

@router.get("/{user_id}", response_model=User)
def get_user_by_id(
    user_id: uuid.UUID,
    repo: UserRepository = Depends(get_user_repository)
):
    db_user = repo.get_by_id(user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=User)
def update_user(
    user_id: uuid.UUID,
    user_data: UserUpdate,
    repo: UserRepository = Depends(get_user_repository)
):
    updated_user = repo.update(user_id, user_data)
    if updated_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: uuid.UUID,
    repo: UserRepository = Depends(get_user_repository)
):
    if not repo.delete(user_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return