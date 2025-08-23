from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import uuid

from app.schemas.face_shape import FaceShape, FaceShapeCreate, FaceShapeUpdate
from app.repositories.face_shape_repository import FaceShapeRepository
from app.dependencies.dependencies import get_face_shape_repository

router = APIRouter(prefix="/face-shapes", tags=["Face Shapes"])

@router.post("/", response_model=FaceShape, status_code=status.HTTP_201_CREATED)
def create_face_shape(
    shape_data: FaceShapeCreate,
    repo: FaceShapeRepository = Depends(get_face_shape_repository)
):
    return repo.create(shape_data)

@router.get("/", response_model=List[FaceShape])
def get_all_face_shapes(
    repo: FaceShapeRepository = Depends(get_face_shape_repository)
):
    return repo.get_all()

@router.get("/{shape_id}", response_model=FaceShape)
def get_face_shape_by_id(
    shape_id: uuid.UUID,
    repo: FaceShapeRepository = Depends(get_face_shape_repository)
):
    db_shape = repo.get_by_id(shape_id)
    if db_shape is None:
        raise HTTPException(status_code=404, detail="Face shape not found")
    return db_shape

@router.put("/{shape_id}", response_model=FaceShape)
def update_face_shape(
    shape_id: uuid.UUID,
    shape_data: FaceShapeUpdate,
    repo: FaceShapeRepository = Depends(get_face_shape_repository)
):
    updated_shape = repo.update(shape_id, shape_data)
    if updated_shape is None:
        raise HTTPException(status_code=404, detail="Face shape not found")
    return updated_shape

@router.delete("/{shape_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_face_shape(
    shape_id: uuid.UUID,
    repo: FaceShapeRepository = Depends(get_face_shape_repository)
):
    if not repo.delete(shape_id):
        raise HTTPException(status_code=404, detail="Face shape not found")
    return