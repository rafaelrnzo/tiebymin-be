from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.training import TrainingPairRepo, TrainingPairHashtagRepo
from app.schemas.training import TrainingPairOut, TrainingPairCreate
from app.schemas.web_response import WebResponse, Paging
from app.utils.response_helpers import success_response
from typing import List
import math
from datetime import datetime
from app.repositories.training import HookVariantRepo, SceneRepo
from app.schemas.training import HookVariantOut, SceneOut
from app.schemas.review import ReviewActionOut
from app.models.training import TrainingPair, TrainingPairHashtag

class TrainingService:
    
    def __init__(self, db: AsyncSession):
        self.training = TrainingPairRepo(db)
        self.hashtag_repo = TrainingPairHashtagRepo(db)

    async def create_training_pair(self, data: TrainingPairCreate, user) -> TrainingPairOut:
        """
        Create a new training pair with hashtags as strings.
        """
        # Create training pair
        training_pair = TrainingPair(
            pair_id=data.pair_id,
            topic=data.topic,
            category=data.category,
            duration_seconds=data.duration_seconds,
            score=data.score,
            user_prompt=data.user_prompt,
            system_prompt=data.system_prompt,
            target_audience=data.target_audience,
            content_style=data.content_style,
            created_at=datetime.utcnow(),
            created_by=user.username,
            updated_at=datetime.utcnow(),
            updated_by=user.username
        )
        
        created_training_pair = await self.training.create(training_pair)
        
        # Create hashtags if provided
        if data.hashtags:
            for hashtag_str in data.hashtags:
                hashtag = TrainingPairHashtag(
                    training_pair_id=created_training_pair.id,
                    hashtag=hashtag_str,
                    created_at=datetime.utcnow(),
                    created_by=user.username,
                    updated_at=datetime.utcnow(),
                    updated_by=user.username
                )
                await self.hashtag_repo.create(hashtag)
        
        return TrainingPairOut.model_validate(created_training_pair)

    async def get_training_queue(self, page: int = 1, size: int = 10) -> WebResponse[List[TrainingPairOut]]:
        """
        Get paginated training pairs queue with prev/next navigation support.
        """
        # Get paginated data from repository
        training_pairs, total_items = await self.training.get_training_queue_paginated(page, size)
        
        # Calculate pagination info
        total_pages = math.ceil(total_items / size) if total_items > 0 else 0
        
        # Convert to schema
        training_pair_list = [TrainingPairOut.model_validate(tp) for tp in training_pairs]
        
        # Create pagination object
        paging = Paging(
            page=page,
            size=size,
            totalItems=total_items,
            totalPages=total_pages
        )
        
        # Return success response with pagination
        return success_response(
            data=training_pair_list,
            paging=paging
        )

    async def update_user_prompt(self, training_pair_id, user_prompt: str, user) -> TrainingPairOut:
        update_data = {
            "user_prompt": user_prompt,
            "updated_at": None,
            "updated_by": None
        }
        update_data["updated_at"] = datetime.utcnow()
        update_data["updated_by"] = user.username
        updated = await self.training.update(training_pair_id, update_data)
        if not updated:
            raise ValueError("TrainingPair not found")
        return TrainingPairOut.model_validate(updated)

    async def update_hook_variant(self, hook_variant_id, data, user):
        update_data = {}
        if data.hook_variant is not None:
            update_data["hook_variant"] = data.hook_variant
        if data.scene_number is not None:
            update_data["scene_number"] = data.scene_number
        if data.scene_type is not None:
            update_data["scene_type"] = data.scene_type
        if data.timestamp is not None:
            update_data["timestamp"] = data.timestamp
        if data.text_overlay is not None:
            update_data["text_overlay"] = data.text_overlay
        if data.voiceover is not None:
            update_data["voiceover"] = data.voiceover
        if data.visual is not None:
            update_data["visual"] = data.visual
        if data.tip is not None:
            update_data["tip"] = data.tip
        update_data["updated_at"] = datetime.utcnow()
        update_data["updated_by"] = user.username
        repo = HookVariantRepo(self.training.db)
        updated = await repo.update(hook_variant_id, update_data)
        if not updated:
            raise ValueError("HookVariant not found")
        return HookVariantOut.model_validate(updated)

    async def update_scene(self, scene_id, data, user):
        update_data = {}
        if data.scene_number is not None:
            update_data["scene_number"] = data.scene_number
        if data.scene_type is not None:
            update_data["scene_type"] = data.scene_type
        if data.timestamp is not None:
            update_data["timestamp"] = data.timestamp
        if data.text_overlay is not None:
            update_data["text_overlay"] = data.text_overlay
        if data.voiceover is not None:
            update_data["voiceover"] = data.voiceover
        if data.visual is not None:
            update_data["visual"] = data.visual
        if data.tip is not None:
            update_data["tip"] = data.tip
        update_data["updated_at"] = datetime.utcnow()
        update_data["updated_by"] = user.username
        repo = SceneRepo(self.training.db)
        updated = await repo.update(scene_id, update_data)
        if not updated:
            raise ValueError("Scene not found")
        return SceneOut.model_validate(updated)

    async def get_training_pairs_by_status(self, status: str, page: int = 1, size: int = 10):
        """
        Get paginated training pairs by status with their review data.
        """
        if status == "REJECTED":
            training_pairs, total_items = await self.training.get_rejected_training_pairs_paginated(page, size)
        elif status == "APPROVED":
            training_pairs, total_items = await self.training.get_approved_training_pairs_paginated(page, size)
        else:
            raise ValueError(f"Unsupported status: {status}")
        
        # For each training pair, get the latest review action
        result = []
        for tp in training_pairs:
            # Find the latest review action
            review_data = None
            if tp.review_actions:
                status_reviews = [ra for ra in tp.review_actions if ra.action == status]
                if status_reviews:
                    # Get the latest by created_at
                    latest = max(status_reviews, key=lambda ra: ra.created_at or 0)
                    # Include all review fields except created/updated/deleted
                    review_data = {
                        "id": latest.id,
                        "action": latest.action,
                        "notes": latest.notes,
                        "user": {
                            "username": latest.user.username if latest.user else None,
                            "team": latest.user.team if latest.user else None
                        } if latest.user else None
                    }
            # Only include training pair fields, not hooks/scenes
            exclude_fields = {"hook_variants", "scenes", "hashtags"}
            if status == "REJECTED":
                exclude_fields.add("system_prompt")
            
            tp_data = TrainingPairOut.model_validate(tp).model_dump(exclude=exclude_fields)
            result.append({
                **tp_data,
                "review": review_data
            })
        # Pagination info
        paging = Paging(
            page=page,
            size=size,
            totalItems=total_items,
            totalPages=math.ceil(total_items / size) if total_items > 0 else 0
        )
        return success_response(data=result, paging=paging)

    async def get_rejected_training_pairs(self, page: int = 1, size: int = 10):
        """
        Get paginated rejected training pairs with their review notes.
        """
        return await self.get_training_pairs_by_status("REJECTED", page, size)

    async def get_training_pair_by_id(self, training_pair_id: str):
        """
        Get training pair by ID with all related data.
        """
        training_pair = await self.training.get_by_id(training_pair_id)
        if not training_pair:
            raise ValueError("TrainingPair not found")
        
        # Return the same format as get_training_queue
        return TrainingPairOut.model_validate(training_pair)

    async def get_approved_training_pairs(self, page: int = 1, size: int = 10):
        """
        Get paginated approved training pairs with their review notes.
        """
        return await self.get_training_pairs_by_status("APPROVED", page, size)
