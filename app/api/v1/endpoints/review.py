from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps.auth import get_current_user
from app.db.session import get_db
from app.repositories.review import ReviewActionRepo
from app.schemas.review import ReviewSummary, ReviewActionCreate, ReviewActionOut
from app.models.user import User
from app.services.review_service import ReviewService

router = APIRouter()

@router.get("/summary", response_model=ReviewSummary)
async def get_review_summary(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    repo = ReviewActionRepo(db)
    summary = await repo.get_summary()
    return ReviewSummary(**summary)

@router.post("/approve", response_model=ReviewActionOut)
async def approve_review(
    data: ReviewActionCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    service = ReviewService(db)
    return await service.create_review_action("APPROVED", data, current_user)

@router.post("/reject", response_model=ReviewActionOut)
async def reject_review(
    data: ReviewActionCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    service = ReviewService(db)
    return await service.create_review_action("REJECTED", data, current_user)

@router.post("/skip", response_model=ReviewActionOut)
async def skip_review(
    data: ReviewActionCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    service = ReviewService(db)
    return await service.create_review_action("SKIPPED", data, current_user) 