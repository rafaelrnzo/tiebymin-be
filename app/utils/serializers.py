import json
import uuid
from datetime import datetime, date
from typing import Any, Optional, Type, Dict, List, Union
from pydantic import BaseModel
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import DeclarativeBase
from app.schemas.training import TrainingPairOut, TrainingPairHashtagOut, HookVariantOut, SceneOut
from app.schemas.user import UserOut
from app.schemas.evaluation import GeneratedTrainingPairResponse, GeneratedHookVariantResponse, GeneratedSceneResponse, UserPreferenceResponse

class CustomJSONEncoder(json.JSONEncoder):
    """
    Custom JSON encoder that handles special data types like UUID and datetime.
    """
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

def _serialize_sqlalchemy_obj(obj: Any, output_model: Optional[Type[BaseModel]] = None) -> Any:
    """
    Convert SQLAlchemy model instances to dictionaries or Pydantic models.
    If output_model is provided, the SQLAlchemy model will be converted to that Pydantic model.
    """
    if isinstance(obj, uuid.UUID):
        return str(obj)
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if obj is None or isinstance(obj, (str, int, float, bool, dict)):
        return obj
    if isinstance(obj, (list, tuple, set)):
        return [_serialize_sqlalchemy_obj(item, output_model) for item in obj]
    if hasattr(obj, '__table__') or isinstance(obj.__class__, DeclarativeMeta):
        model_to_use = None
        if output_model:
            model_to_use = output_model
        else:
            model_name = obj.__class__.__name__
            model_mappings = {
                "User": "UserResponse",
                "TrainingPair": "TrainingPairOut",
                "Hashtag": "HashtagOut",
                "HookVariant": "HookVariantOut",
                "Scene": "SceneOut",
                "ReviewAction": "ReviewActionOut"
            }
            schema_name = model_mappings.get(model_name)
            if schema_name:
                try:
                    if model_name == "User":
                        from app.schemas.user import UserResponse
                        model_to_use = UserResponse
                    elif model_name in ["TrainingPair", "Hashtag", "HookVariant", "Scene"]:
                        from app.schemas.training import TrainingPairOut, HashtagOut, HookVariantOut, SceneOut
                        if model_name == "TrainingPair":
                            model_to_use = TrainingPairOut
                        elif model_name == "Hashtag":
                            model_to_use = HashtagOut
                        elif model_name == "HookVariant":
                            model_to_use = HookVariantOut
                        elif model_name == "Scene":
                            model_to_use = SceneOut
                    elif model_name == "ReviewAction":
                        from app.schemas.review import ReviewActionOut
                        model_to_use = ReviewActionOut
                except ImportError:
                    pass
        if model_to_use:
            return model_to_use.model_validate(obj).model_dump()
        result = {}
        for c in obj.__table__.columns:
            value = getattr(obj, c.name)
            if isinstance(value, uuid.UUID):
                result[c.name] = str(value)
            elif isinstance(value, (datetime, date)):
                result[c.name] = value.isoformat()
            else:
                result[c.name] = value
        return result
    if hasattr(obj, "__dict__"):
        return {k: _serialize_sqlalchemy_obj(v) for k, v in obj.__dict__.items() if not k.startswith('_')}
    return str(obj)

def to_dict(obj: Any, output_model: Optional[Type[BaseModel]] = None) -> Any:
    """
    Public helper to convert SQLAlchemy model instances (or other complex
    objects) into plain Python dictionaries that are JSON-serialisable. This is
    essentially a thin wrapper around the internal `_serialize_sqlalchemy_obj`
    so that other modules can safely import `to_dict` without needing intimate
    knowledge of this module's internals.

    Parameters
    ----------
    obj: Any
        The object to be serialised.
    output_model: Optional[Type[BaseModel]]
        If supplied, the object will first be parsed/validated into the given
        Pydantic model class before being converted into a dictionary.
    """
    return _serialize_sqlalchemy_obj(obj, output_model)

def serialize_model(model: DeclarativeBase, exclude_fields: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Serialize SQLAlchemy model to dictionary.
    
    Args:
        model: SQLAlchemy model instance
        exclude_fields: List of field names to exclude from serialization
        
    Returns:
        Dictionary representation of the model
    """
    if exclude_fields is None:
        exclude_fields = []
    
    result = {}
    for column in model.__table__.columns:
        if column.name not in exclude_fields:
            value = getattr(model, column.name)
            result[column.name] = value
    
    return result

def serialize_models(models: List[DeclarativeBase], exclude_fields: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    """
    Serialize list of SQLAlchemy models to list of dictionaries.
    
    Args:
        models: List of SQLAlchemy model instances
        exclude_fields: List of field names to exclude from serialization
        
    Returns:
        List of dictionary representations of the models
    """
    return [serialize_model(model, exclude_fields) for model in models]

def get_schema_for_model(model_name: str):
    """
    Get the appropriate Pydantic schema for a model name.
    
    Args:
        model_name: Name of the model
        
    Returns:
        Pydantic schema class
    """
    schema_mapping = {
        "User": UserOut,
        "TrainingPair": TrainingPairOut,
        "TrainingPairHashtag": TrainingPairHashtagOut,
        "HookVariant": HookVariantOut,
        "Scene": SceneOut,
        "AIModel": GeneratedTrainingPairResponse,
        "GeneratedTrainingPair": GeneratedTrainingPairResponse,
        "GeneratedHookVariant": GeneratedHookVariantResponse,
        "GeneratedScene": GeneratedSceneResponse,
        "UserPreference": UserPreferenceResponse,
    }
    
    return schema_mapping.get(model_name)

def serialize_to_schema(model: DeclarativeBase, model_name: str) -> Dict[str, Any]:
    """
    Serialize model using appropriate Pydantic schema.
    
    Args:
        model: SQLAlchemy model instance
        model_name: Name of the model to determine schema
        
    Returns:
        Dictionary representation using Pydantic schema
    """
    schema_class = get_schema_for_model(model_name)
    if schema_class:
        return schema_class.model_validate(model).model_dump()
    else:
        return serialize_model(model) 