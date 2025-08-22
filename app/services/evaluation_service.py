from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from typing import List, Optional
from uuid import UUID
from datetime import datetime
import random
from app.repositories.evaluation import (
    AIModelRepository,
    TrainingPairSetRepository,
    GeneratedTrainingPairRepository,
    UserPreferenceRepository
)
from app.schemas.evaluation import (
    EvaluationComparisonResponse,
    UserPreferenceCreate,
    UserPreferenceResponse,
    EvaluationProgressResponse,
    EvaluationPairResponse,
    TrainingPairSetResponse
)
from app.models.evaluation import UserPreference, TrainingPairSet
from app.utils.serializers import to_dict

class EvaluationService:
    def __init__(self, db: Session):
        self.db = db
        self.ai_model_repo = AIModelRepository(db)
        self.training_pair_set_repo = TrainingPairSetRepository(db)
        self.generated_training_pair_repo = GeneratedTrainingPairRepository(db)
        self.user_preference_repo = UserPreferenceRepository(db)
    
    async def get_evaluation_comparison(self, pair_id: str) -> Optional[EvaluationComparisonResponse]:
        """
        Mendapatkan perbandingan training pair dari baseline dan fine-tuned model
        untuk training pair set yang sama
        """
        # Get training pair set
        training_pair_set = await self.training_pair_set_repo.get_by_pair_id(pair_id)
        if not training_pair_set:
            return None
        
        baseline_pair, fine_tuned_pair = await self.generated_training_pair_repo.get_comparison_pairs(str(training_pair_set.id))
        
        if not baseline_pair or not fine_tuned_pair:
            return None
        
        return EvaluationComparisonResponse(
            training_pair_a=baseline_pair,
            training_pair_b=fine_tuned_pair,
            training_pair_set=training_pair_set
        )
    
    async def get_random_evaluation_comparison(self) -> Optional[EvaluationComparisonResponse]:
        """
        Mendapatkan perbandingan training pair secara random
        """
        baseline_pair, fine_tuned_pair = await self.generated_training_pair_repo.get_random_comparison_pairs()
        
        if not baseline_pair or not fine_tuned_pair:
            return None
        
        # Get training pair set
        training_pair_set = await self.training_pair_set_repo.get_by_id(str(baseline_pair.training_pair_set_id))
        if not training_pair_set:
            return None
        
        return EvaluationComparisonResponse(
            training_pair_a=baseline_pair,
            training_pair_b=fine_tuned_pair,
            training_pair_set=training_pair_set
        )
    
    async def create_user_preference(self, user_id: Optional[UUID], preference_data: UserPreferenceCreate) -> UserPreferenceResponse:
        """
        Menyimpan preferensi user untuk training pair tertentu
        """
        user_preference = UserPreference(
            user_id=user_id,
            training_pair_set_id=preference_data.training_pair_set_id,
            selected_training_pair_id=preference_data.selected_training_pair_id,
            preference_reason=preference_data.preference_reason,
            created_at=datetime.now(),
            created_by=str(user_id) if user_id else "ANONYMOUS"
        )
        
        self.db.add(user_preference)
        
        # Update review status of training pair set
        if isinstance(self.db, AsyncSession):
            await self.db.execute(
                text("""
                    UPDATE training_pair_sets 
                    SET review_status = 'REVIEWED', 
                        reviewed_at = :reviewed_at, 
                        reviewed_by = :reviewed_by,
                        updated_at = :updated_at
                    WHERE id = :training_pair_set_id
                """),
                {
                    "reviewed_at": datetime.now(),
                    "reviewed_by": str(user_id) if user_id else "ANONYMOUS",
                    "updated_at": datetime.now(),
                    "training_pair_set_id": preference_data.training_pair_set_id
                }
            )
        else:
            # For sync session
            training_pair_set = self.db.query(TrainingPairSet).filter(
                TrainingPairSet.id == preference_data.training_pair_set_id
            ).first()
            if training_pair_set:
                training_pair_set.review_status = "REVIEWED"
                training_pair_set.reviewed_at = datetime.now()
                training_pair_set.reviewed_by = str(user_id) if user_id else "ANONYMOUS"
                training_pair_set.updated_at = datetime.now()
        
        if isinstance(self.db, AsyncSession):
            await self.db.commit()
            await self.db.refresh(user_preference)
        else:
            self.db.commit()
            self.db.refresh(user_preference)
        
        return UserPreferenceResponse.from_orm(user_preference)
    
    async def get_evaluation_progress(self, user_id: UUID) -> EvaluationProgressResponse:
        """
        Mendapatkan progress evaluasi untuk user tertentu
        """
        if isinstance(self.db, AsyncSession):
            # Get total training pair sets (only QUEUE ones)
            result = await self.db.execute(
                text("SELECT COUNT(*) FROM training_pair_sets WHERE deleted_at IS NULL AND review_status = 'QUEUE'")
            )
            total_training_pair_sets = result.scalar()
            
            # Get evaluated training pair sets by user
            result = await self.db.execute(
                text("SELECT COUNT(DISTINCT training_pair_set_id) FROM user_preferences WHERE user_id = :user_id AND deleted_at IS NULL"),
                {"user_id": user_id}
            )
            evaluated_training_pair_sets = result.scalar()
        else:
            # Get total training pair sets (only QUEUE ones)
            total_training_pair_sets = self.db.query(TrainingPairSet).filter(
                TrainingPairSet.deleted_at.is_(None),
                TrainingPairSet.review_status == "QUEUE"
            ).count()
            
            # Get evaluated training pair sets by user
            evaluated_training_pair_sets = self.db.query(UserPreference.training_pair_set_id).filter(
                UserPreference.user_id == user_id,
                UserPreference.deleted_at.is_(None)
            ).distinct().count()
        
        remaining_pairs = total_training_pair_sets - evaluated_training_pair_sets
        progress_percentage = (evaluated_training_pair_sets / total_training_pair_sets * 100) if total_training_pair_sets > 0 else 0
        
        return EvaluationProgressResponse(
            total_pairs=total_training_pair_sets,
            evaluated_pairs=evaluated_training_pair_sets,
            remaining_pairs=remaining_pairs,
            progress_percentage=progress_percentage
        )
    
    async def get_user_preferences(self, user_id: UUID) -> List[UserPreferenceResponse]:
        """
        Mendapatkan semua preferensi user
        """
        preferences = await self.user_preference_repo.get_by_user_id(str(user_id))
        return [UserPreferenceResponse.from_orm(pref) for pref in preferences]
    
    async def get_evaluation_pair_for_ui(self, pair_id: Optional[str] = None) -> Optional[EvaluationPairResponse]:
        """
        Mendapatkan data evaluasi untuk UI dengan informasi tambahan
        """
        if pair_id:
            comparison = await self.get_evaluation_comparison(pair_id)
        else:
            comparison = await self.get_random_evaluation_comparison()
        
        if not comparison:
            return None
        
        # Get total available pairs
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                text("SELECT COUNT(*) FROM training_pair_sets WHERE deleted_at IS NULL")
            )
            total_available_pairs = result.scalar()
        else:
            total_available_pairs = self.db.query(TrainingPairSet).filter(
                TrainingPairSet.deleted_at.is_(None)
            ).count()
        
        # Get current pair index (simplified - in real implementation might need more complex logic)
        current_pair_index = 1  # This would need to be calculated based on actual position
        
        return EvaluationPairResponse(
            training_pair_set=comparison.training_pair_set,
            script_a=comparison.training_pair_a,
            script_b=comparison.training_pair_b,
            total_available_pairs=total_available_pairs,
            current_pair_index=current_pair_index
        )
    
    async def get_reviewed_training_pairs(self, user_id: UUID) -> List[TrainingPairSetResponse]:
        """
        Mendapatkan training pair yang sudah direview oleh user
        """
        if isinstance(self.db, AsyncSession):
            result = await self.db.execute(
                text("""
                    SELECT DISTINCT tps.* 
                    FROM training_pair_sets tps
                    INNER JOIN user_preferences up ON tps.id = up.training_pair_set_id
                    WHERE up.user_id = :user_id 
                    AND up.deleted_at IS NULL 
                    AND tps.deleted_at IS NULL
                    AND tps.review_status = 'REVIEWED'
                    ORDER BY tps.reviewed_at DESC
                """),
                {"user_id": user_id}
            )
            reviewed_pairs = result.fetchall()
            return [TrainingPairSetResponse.from_orm(pair) for pair in reviewed_pairs]
        else:
            # For sync session
            reviewed_pairs = self.db.query(TrainingPairSet).join(UserPreference).filter(
                UserPreference.user_id == user_id,
                UserPreference.deleted_at.is_(None),
                TrainingPairSet.deleted_at.is_(None),
                TrainingPairSet.review_status == "REVIEWED"
            ).order_by(TrainingPairSet.reviewed_at.desc()).all()
            return [TrainingPairSetResponse.from_orm(pair) for pair in reviewed_pairs] 