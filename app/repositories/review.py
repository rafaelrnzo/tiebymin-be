from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import ReviewAction
from typing import Optional
from sqlalchemy import func, select, and_, not_, exists
from app.models.training import TrainingPair
from uuid import UUID

class ReviewActionRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, review_action_id) -> Optional[ReviewAction]:
        result = await self.db.execute(select(ReviewAction).where(ReviewAction.id == review_action_id))
        return result.unique().scalar_one_or_none()

    async def create(self, review_action: ReviewAction) -> ReviewAction:
        self.db.add(review_action)
        await self.db.commit()
        await self.db.refresh(review_action)
        return review_action

    async def get_user_review_stats(self, user_id: UUID) -> dict:
        """Get review statistics for a specific user."""
        # Get total reviews by user
        total_reviewed_stmt = select(func.count()).select_from(ReviewAction).where(
            ReviewAction.user_id == user_id,
            ReviewAction.deleted_at.is_(None),
            ReviewAction.action.in_(["APPROVED", "REJECTED"])
        )
        total_reviewed_result = await self.db.execute(total_reviewed_stmt)
        total_reviewed = total_reviewed_result.scalar() or 0

        # Get approved reviews by user
        approved_stmt = select(func.count()).select_from(ReviewAction).where(
            ReviewAction.user_id == user_id,
            ReviewAction.deleted_at.is_(None),
            ReviewAction.action == "APPROVED"
        )
        approved_result = await self.db.execute(approved_stmt)
        approved = approved_result.scalar() or 0

        # Get rejected reviews by user
        rejected_stmt = select(func.count()).select_from(ReviewAction).where(
            ReviewAction.user_id == user_id,
            ReviewAction.deleted_at.is_(None),
            ReviewAction.action == "REJECTED"
        )
        rejected_result = await self.db.execute(rejected_stmt)
        rejected = rejected_result.scalar() or 0

        # Get total training pairs (for contribution percentage)
        total_training_pairs_stmt = select(func.count()).select_from(TrainingPair).where(
            TrainingPair.deleted_at.is_(None)
        )
        total_training_pairs_result = await self.db.execute(total_training_pairs_stmt)
        total_training_pairs = total_training_pairs_result.scalar() or 0

        # Calculate contribution percentage
        contribution_percent = int((total_reviewed / total_training_pairs) * 100) if total_training_pairs > 0 else 0

        return {
            'total_reviewed': total_reviewed,
            'total_approved': approved,
            'total_rejected': rejected,
            'contribution_percent': contribution_percent
        }

    async def get_summary(self) -> dict:
        # Summary berdasarkan status pada TrainingPair
        queue_stmt = select(func.count()).select_from(TrainingPair).where(
            TrainingPair.deleted_at.is_(None),
            TrainingPair.status == "QUEUE"
        )
        queue_result = await self.db.execute(queue_stmt)
        queue = queue_result.scalar() or 0

        approved_stmt = select(func.count()).select_from(TrainingPair).where(
            TrainingPair.deleted_at.is_(None),
            TrainingPair.status == "APPROVED"
        )
        approved_result = await self.db.execute(approved_stmt)
        approved = approved_result.scalar() or 0

        rejected_stmt = select(func.count()).select_from(TrainingPair).where(
            TrainingPair.deleted_at.is_(None),
            TrainingPair.status == "REJECTED"
        )
        rejected_result = await self.db.execute(rejected_stmt)
        rejected = rejected_result.scalar() or 0

        total_stmt = select(func.count()).select_from(TrainingPair).where(
            TrainingPair.deleted_at.is_(None)
        )
        total_result = await self.db.execute(total_stmt)
        total = total_result.scalar() or 0

        reviewed = approved + rejected
        progress_percent = int((reviewed / total) * 100) if total > 0 else 0

        return {
            'queue': queue,
            'approved': approved,
            'rejected': rejected,
            'reviewed': reviewed,
            'progress_percent': progress_percent
        }
