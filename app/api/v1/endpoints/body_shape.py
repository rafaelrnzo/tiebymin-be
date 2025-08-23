from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from app.schemas.body_shape import BodyShape, BodyShapeCreate, BodyShapeUpdate
from app.repositories.body_shape_repository import BodyShapeRepository
from app.dependencies.dependencies import get_body_shape_repository

router = APIRouter(prefix="/body-shapes", tags=["Body Shapes"])

@router.post("/", response_model=BodyShape, status_code=status.HTTP_201_CREATED)
def create_body_shape(
    shape_data: BodyShapeCreate,
    repo: BodyShapeRepository = Depends(get_body_shape_repository)
):
    return repo.create(shape_data)

@router.get("/", response_model=List[BodyShape])
def get_all_body_shapes(
    repo: BodyShapeRepository = Depends(get_body_shape_repository)
):
    return repo.get_all()

@router.get("/{shape_id}", response_model=BodyShape)
def get_body_shape_by_id(
    shape_id: uuid.UUID,
    repo: BodyShapeRepository = Depends(get_body_shape_repository)
):
    db_shape = repo.get_by_id(shape_id)
    if db_shape is None:
        raise HTTPException(status_code=404, detail="Body shape not found")
    return db_shape

@router.put("/{shape_id}", response_model=BodyShape)
def update_body_shape(
    shape_id: uuid.UUID,
    shape_data: BodyShapeUpdate,
    repo: BodyShapeRepository = Depends(get_body_shape_repository)
):
    updated_shape = repo.update(shape_id, shape_data)
    if updated_shape is None:
        raise HTTPException(status_code=404, detail="Body shape not found")
    return updated_shape

@router.delete("/{shape_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_body_shape(
    shape_id: uuid.UUID,
    repo: BodyShapeRepository = Depends(get_body_shape_repository)
):
    if not repo.delete(shape_id):
        raise HTTPException(status_code=404, detail="Body shape not found")
    return