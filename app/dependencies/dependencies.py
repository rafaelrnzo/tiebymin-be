import os
from typing import Type, Optional
from sqlalchemy.orm import Session
from db.postgres_db import SessionLocal

# BMI Imports
from repositories.bmi_repository import (
    SupabaseBMIRepository, 
    PostgresBMIRepository
)
# Body Shape Imports
from repositories.body_shape_repository import SupabaseBodyShapeRepository
# Face Shape Imports
from repositories.face_shape_repository import SupabaseFaceShapeRepository

def create_repository_provider(
    supabase_repo_class: Type, 
    postgres_repo_class: Optional[Type] = None
):
    def get_repository():
        db_type = os.getenv("DB_TYPE", "supabase")
        if db_type == "postgres":
            if not postgres_repo_class:
                raise NotImplementedError(f"PostgreSQL not implemented for {supabase_repo_class.__name__}")
            db: Session = SessionLocal()
            return postgres_repo_class(db_session=db)
        return supabase_repo_class()
    return get_repository

get_bmi_repository = create_repository_provider(
    supabase_repo_class=SupabaseBMIRepository,
    postgres_repo_class=PostgresBMIRepository
)

get_body_shape_repository = create_repository_provider(
    supabase_repo_class=SupabaseBodyShapeRepository
)

get_face_shape_repository = create_repository_provider(
    supabase_repo_class=SupabaseFaceShapeRepository
)