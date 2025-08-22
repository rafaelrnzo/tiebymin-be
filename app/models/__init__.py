# Import all models to ensure they are registered with SQLAlchemy
from .user import User
from .training import TrainingPair, TrainingPairHashtag
from .evaluation import AIModel, TrainingPairSet, GeneratedTrainingPair, GeneratedHookVariant, GeneratedScene, UserPreference

__all__ = [
    "User",
    "TrainingPair", 
    "TrainingPairHashtag",
    "AIModel",
    "TrainingPairSet",
    "GeneratedTrainingPair",
    "GeneratedHookVariant", 
    "GeneratedScene",
    "UserPreference"
]

