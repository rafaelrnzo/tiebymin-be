from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func, and_
from app.models.training import TrainingPair, TrainingPairHashtag, HookVariant, Scene
from typing import Optional, List, Tuple

class TrainingPairRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, training_pair_id) -> Optional[TrainingPair]:
        result = await self.db.execute(select(TrainingPair).where(TrainingPair.id == training_pair_id))
        return result.unique().scalar_one_or_none()

    async def create(self, training_pair: TrainingPair) -> TrainingPair:
        self.db.add(training_pair)
        await self.db.commit()
        await self.db.refresh(training_pair)
        return training_pair

    async def update(self, training_pair_id, update_data: dict) -> Optional[TrainingPair]:
        result = await self.db.execute(select(TrainingPair).where(TrainingPair.id == training_pair_id))
        obj = result.unique().scalar_one_or_none()
        if not obj:
            return None
        for key, value in update_data.items():
            setattr(obj, key, value)
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def get_training_queue_paginated(self, page: int = 1, size: int = 10) -> Tuple[List[TrainingPair], int]:
        """Get training pairs with pagination (for queue display)."""
        offset = (page - 1) * size
        
        # Get total count
        count_result = await self.db.execute(
            select(func.count(TrainingPair.id)).where(
                TrainingPair.deleted_at.is_(None),
                TrainingPair.status == "QUEUE"
            )
        )
        total_items = count_result.scalar()
        
        # Get paginated data
        query = (
            select(TrainingPair)
            .where(
                TrainingPair.deleted_at.is_(None),
                TrainingPair.status == "QUEUE"
            )
            .order_by(TrainingPair.created_at.desc())
            .offset(offset)
            .limit(size)
        )
        
        result = await self.db.execute(query)
        training_pairs = result.unique().scalars().all()
        
        return training_pairs, total_items

    async def get_training_pairs_by_status_paginated(self, status: str, page: int = 1, size: int = 10) -> Tuple[List[TrainingPair], int]:
        """Get training pairs by status with pagination."""
        offset = (page - 1) * size
        # Get total count
        count_result = await self.db.execute(
            select(func.count(TrainingPair.id)).where(
                TrainingPair.deleted_at.is_(None),
                TrainingPair.status == status
            )
        )
        total_items = count_result.scalar()
        # Get paginated data
        query = (
            select(TrainingPair)
            .where(
                TrainingPair.deleted_at.is_(None),
                TrainingPair.status == status
            )
            .order_by(TrainingPair.created_at.desc())
            .offset(offset)
            .limit(size)
        )
        result = await self.db.execute(query)
        training_pairs = result.unique().scalars().all()
        return training_pairs, total_items

    async def get_rejected_training_pairs_paginated(self, page: int = 1, size: int = 10) -> Tuple[List[TrainingPair], int]:
        """Get rejected training pairs with pagination."""
        return await self.get_training_pairs_by_status_paginated("REJECTED", page, size)

    async def get_approved_training_pairs_paginated(self, page: int = 1, size: int = 10) -> Tuple[List[TrainingPair], int]:
        """Get approved training pairs with pagination."""
        return await self.get_training_pairs_by_status_paginated("APPROVED", page, size)

class TrainingPairHashtagRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, hashtag_id) -> Optional[TrainingPairHashtag]:
        result = await self.db.execute(select(TrainingPairHashtag).where(TrainingPairHashtag.id == hashtag_id))
        return result.unique().scalar_one_or_none()

    async def create(self, hashtag: TrainingPairHashtag) -> TrainingPairHashtag:
        self.db.add(hashtag)
        await self.db.commit()
        await self.db.refresh(hashtag)
        return hashtag

    async def update(self, hashtag_id, update_data: dict) -> Optional[TrainingPairHashtag]:
        result = await self.db.execute(select(TrainingPairHashtag).where(TrainingPairHashtag.id == hashtag_id))
        obj = result.unique().scalar_one_or_none()
        if not obj:
            return None
        for key, value in update_data.items():
            setattr(obj, key, value)
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def get_by_training_pair_id(self, training_pair_id) -> List[TrainingPairHashtag]:
        """Get all hashtags for a specific training pair."""
        result = await self.db.execute(
            select(TrainingPairHashtag).where(
                TrainingPairHashtag.training_pair_id == training_pair_id,
                TrainingPairHashtag.deleted_at.is_(None)
            )
        )
        return result.unique().scalars().all()

    async def delete_by_training_pair_id(self, training_pair_id):
        """Delete all hashtags for a specific training pair."""
        result = await self.db.execute(
            select(TrainingPairHashtag).where(
                TrainingPairHashtag.training_pair_id == training_pair_id,
                TrainingPairHashtag.deleted_at.is_(None)
            )
        )
        hashtags = result.unique().scalars().all()
        for hashtag in hashtags:
            hashtag.deleted_at = func.now()
        self.db.add_all(hashtags)
        await self.db.commit()

class HookVariantRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, hook_variant_id) -> Optional[HookVariant]:
        result = await self.db.execute(select(HookVariant).where(HookVariant.id == hook_variant_id))
        return result.unique().scalar_one_or_none()

    async def create(self, hook_variant: HookVariant) -> HookVariant:
        self.db.add(hook_variant)
        await self.db.commit()
        await self.db.refresh(hook_variant)
        return hook_variant

    async def update(self, hook_variant_id, update_data: dict) -> Optional[HookVariant]:
        result = await self.db.execute(select(HookVariant).where(HookVariant.id == hook_variant_id))
        obj = result.unique().scalar_one_or_none()
        if not obj:
            return None
        for key, value in update_data.items():
            setattr(obj, key, value)
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj

class SceneRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, scene_id) -> Optional[Scene]:
        result = await self.db.execute(select(Scene).where(Scene.id == scene_id))
        return result.unique().scalar_one_or_none()

    async def create(self, scene: Scene) -> Scene:
        self.db.add(scene)
        await self.db.commit()
        await self.db.refresh(scene)
        return scene

    async def update(self, scene_id, update_data: dict) -> Optional[Scene]:
        result = await self.db.execute(select(Scene).where(Scene.id == scene_id))
        obj = result.unique().scalar_one_or_none()
        if not obj:
            return None
        for key, value in update_data.items():
            setattr(obj, key, value)
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj
