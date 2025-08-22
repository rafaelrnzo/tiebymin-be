from typing import List, Optional, Tuple
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.models.evaluation import (
    AIModel,
    TrainingPairSet,
    GeneratedTrainingPair,
    UserPreference
)
from app.repositories.base import BaseRepository
from app.utils.serializers import to_dict

class AIModelRepository(BaseRepository[AIModel]):
    """Repository untuk operasi database pada AI models"""
    
    def __init__(self, db: Session):
        super().__init__(AIModel, db)
    
    async def get_baseline_model(self) -> Optional[AIModel]:
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                select(AIModel).filter(
                    AIModel.is_baseline == True,
                    AIModel.deleted_at.is_(None)
                )
            )
            return result.scalar_one_or_none()
        else:
            return self.db.query(AIModel).filter(
                AIModel.is_baseline == True,
                AIModel.deleted_at.is_(None)
            ).first()
    
    async def get_fine_tuned_model(self) -> Optional[AIModel]:
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                select(AIModel).filter(
                    AIModel.is_fine_tuned == True,
                    AIModel.deleted_at.is_(None)
                )
            )
            return result.scalar_one_or_none()
        else:
            return self.db.query(AIModel).filter(
                AIModel.is_fine_tuned == True,
                AIModel.deleted_at.is_(None)
            ).first()

class TrainingPairSetRepository(BaseRepository[TrainingPairSet]):
    """Repository untuk operasi database pada training pair sets"""
    
    def __init__(self, db: Session):
        super().__init__(TrainingPairSet, db)
    
    async def get_by_id(self, id: str) -> Optional[TrainingPairSet]:
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                select(TrainingPairSet).filter(
                    TrainingPairSet.id == id,
                    TrainingPairSet.deleted_at.is_(None)
                )
            )
            return result.scalar_one_or_none()
        else:
            return self.db.query(TrainingPairSet).filter(
                TrainingPairSet.id == id,
                TrainingPairSet.deleted_at.is_(None)
            ).first()
    
    async def get_by_pair_id(self, pair_id: str) -> Optional[TrainingPairSet]:
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                select(TrainingPairSet).filter(
                    TrainingPairSet.pair_id == pair_id,
                    TrainingPairSet.deleted_at.is_(None)
                )
            )
            return result.scalar_one_or_none()
        else:
            return self.db.query(TrainingPairSet).filter(
                TrainingPairSet.pair_id == pair_id,
                TrainingPairSet.deleted_at.is_(None)
            ).first()

class GeneratedTrainingPairRepository(BaseRepository[GeneratedTrainingPair]):
    """Repository untuk operasi database pada generated training pairs"""
    
    def __init__(self, db: Session):
        super().__init__(GeneratedTrainingPair, db)
    
    async def get_by_ai_model_id(self, ai_model_id: str) -> List[GeneratedTrainingPair]:
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                select(GeneratedTrainingPair).filter(
                    GeneratedTrainingPair.ai_model_id == ai_model_id,
                    GeneratedTrainingPair.deleted_at.is_(None)
                )
            )
            return result.scalars().all()
        else:
            return self.db.query(GeneratedTrainingPair).filter(
                GeneratedTrainingPair.ai_model_id == ai_model_id,
                GeneratedTrainingPair.deleted_at.is_(None)
            ).all()
    
    async def get_comparison_pairs(self, training_pair_set_id: str) -> Tuple[Optional[GeneratedTrainingPair], Optional[GeneratedTrainingPair]]:
        """
        Mendapatkan pasangan training pair untuk perbandingan dengan training_pair_set_id yang sama
        """
        # Get baseline model
        baseline_model = await self._get_baseline_model()
        if not baseline_model:
            return None, None
        
        # Get fine-tuned model
        fine_tuned_model = await self._get_fine_tuned_model()
        if not fine_tuned_model:
            return None, None
        
        # Get baseline training pair
        baseline_pair = await self._get_training_pair_by_model_and_set(baseline_model.id, training_pair_set_id)
        
        # Get fine-tuned training pair
        fine_tuned_pair = await self._get_training_pair_by_model_and_set(fine_tuned_model.id, training_pair_set_id)
        
        return baseline_pair, fine_tuned_pair
    
    async def get_random_comparison_pairs(self) -> Tuple[Optional[GeneratedTrainingPair], Optional[GeneratedTrainingPair]]:
        """
        Mendapatkan pasangan training pair secara random untuk perbandingan
        """
        # Get baseline model
        baseline_model = await self._get_baseline_model()
        if not baseline_model:
            return None, None
        
        # Get fine-tuned model
        fine_tuned_model = await self._get_fine_tuned_model()
        if not fine_tuned_model:
            return None, None
        
        # Get random baseline training pair
        baseline_pair = await self._get_random_training_pair_by_model(baseline_model.id)
        if not baseline_pair:
            return None, None
        
        # Get fine-tuned training pair with same training_pair_set_id
        fine_tuned_pair = await self._get_training_pair_by_model_and_set(fine_tuned_model.id, str(baseline_pair.training_pair_set_id))
        
        return baseline_pair, fine_tuned_pair

    async def _get_baseline_model(self) -> Optional[AIModel]:
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                select(AIModel).filter(
                    AIModel.is_baseline == True,
                    AIModel.deleted_at.is_(None)
                )
            )
            return result.scalar_one_or_none()
        else:
            return self.db.query(AIModel).filter(
                AIModel.is_baseline == True,
                AIModel.deleted_at.is_(None)
            ).first()

    async def _get_fine_tuned_model(self) -> Optional[AIModel]:
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                select(AIModel).filter(
                    AIModel.is_fine_tuned == True,
                    AIModel.deleted_at.is_(None)
                )
            )
            return result.scalar_one_or_none()
        else:
            return self.db.query(AIModel).filter(
                AIModel.is_fine_tuned == True,
                AIModel.deleted_at.is_(None)
            ).first()

    async def _get_training_pair_by_model_and_set(self, model_id: str, training_pair_set_id: str) -> Optional[GeneratedTrainingPair]:
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                select(GeneratedTrainingPair)
                .options(
                    selectinload(GeneratedTrainingPair.generated_hook_variants),
                    selectinload(GeneratedTrainingPair.generated_scenes)
                )
                .filter(
                    GeneratedTrainingPair.ai_model_id == model_id,
                    GeneratedTrainingPair.training_pair_set_id == training_pair_set_id,
                    GeneratedTrainingPair.deleted_at.is_(None)
                )
            )
            return result.scalar_one_or_none()
        else:
            return self.db.query(GeneratedTrainingPair).options(
                selectinload(GeneratedTrainingPair.generated_hook_variants),
                selectinload(GeneratedTrainingPair.generated_scenes)
            ).filter(
                GeneratedTrainingPair.ai_model_id == model_id,
                GeneratedTrainingPair.training_pair_set_id == training_pair_set_id,
                GeneratedTrainingPair.deleted_at.is_(None)
            ).first()

    async def _get_random_training_pair_by_model(self, model_id: str) -> Optional[GeneratedTrainingPair]:
        if isinstance(self.db, AsyncSession):
            # Use RANDOM() for PostgreSQL and add LIMIT 1 to ensure single result
            result = await self.db.execute(
                select(GeneratedTrainingPair)
                .options(
                    selectinload(GeneratedTrainingPair.generated_hook_variants),
                    selectinload(GeneratedTrainingPair.generated_scenes)
                )
                .join(TrainingPairSet)
                .filter(
                    GeneratedTrainingPair.ai_model_id == model_id,
                    GeneratedTrainingPair.deleted_at.is_(None),
                    TrainingPairSet.deleted_at.is_(None)
                ).order_by(func.random()).limit(1)
            )
            return result.scalar_one_or_none()
        else:
            return self.db.query(GeneratedTrainingPair).options(
                selectinload(GeneratedTrainingPair.generated_hook_variants),
                selectinload(GeneratedTrainingPair.generated_scenes)
            ).join(TrainingPairSet).filter(
                GeneratedTrainingPair.ai_model_id == model_id,
                GeneratedTrainingPair.deleted_at.is_(None),
                TrainingPairSet.deleted_at.is_(None)
            ).order_by(func.random()).first()

class UserPreferenceRepository(BaseRepository[UserPreference]):
    """Repository untuk operasi database pada user preferences"""
    
    def __init__(self, db: Session):
        super().__init__(UserPreference, db)
    
    async def get_by_user_id(self, user_id: str) -> List[UserPreference]:
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                select(UserPreference).filter(
                    UserPreference.user_id == user_id,
                    UserPreference.deleted_at.is_(None)
                )
            )
            return result.scalars().all()
        else:
            return self.db.query(UserPreference).filter(
                UserPreference.user_id == user_id,
                UserPreference.deleted_at.is_(None)
            ).all()
    
    async def get_by_training_pair_set_id(self, training_pair_set_id: str) -> List[UserPreference]:
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                select(UserPreference).filter(
                    UserPreference.training_pair_set_id == training_pair_set_id,
                    UserPreference.deleted_at.is_(None)
                )
            )
            return result.scalars().all()
        else:
            return self.db.query(UserPreference).filter(
                UserPreference.training_pair_set_id == training_pair_set_id,
                UserPreference.deleted_at.is_(None)
            ).all() 