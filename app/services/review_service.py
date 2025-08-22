from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.review import ReviewActionRepo
from app.repositories.training import TrainingPairRepo
from app.models.user import ReviewAction, User
from app.schemas.review import ReviewActionCreate, ReviewActionOut
from uuid import uuid4
from datetime import datetime

class ReviewService:
    def __init__(self, db: AsyncSession):
        self.repo = ReviewActionRepo(db)

    async def create_review_action(self, action: str, data: ReviewActionCreate, user: User) -> ReviewActionOut:
        review_action = ReviewAction(
            id=uuid4(),
            training_pair_id=data.training_pair_id,
            user_id=user.id,
            action=action,
            notes=data.notes,
            created_at=datetime.utcnow(),
            created_by=user.username,
            updated_at=datetime.utcnow(),
            updated_by=user.username,
        )
        created = await self.repo.create(review_action)

        # Update status pada TrainingPair
        training_repo = TrainingPairRepo(self.repo.db)
        status_map = {
            "APPROVED": "APPROVED",
            "REJECTED": "REJECTED",
            "SKIPPED": "SKIPPED"
        }
        if action in status_map:
            await training_repo.update(data.training_pair_id, {"status": status_map[action]})

        return ReviewActionOut.model_validate(created) 