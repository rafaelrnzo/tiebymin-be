# app/core/settings.py
from typing import Optional, List, Union
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings
import json

class Settings(BaseSettings):
    API_V1_STR: str = "/v1"
    PROJECT_NAME: str = "Tiebymin BE V2 - Production"

    DATABASE_URL: str
    SYNC_DATABASE_URL: str
    MODEL_PATH: Optional[str] = None

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str  # Make this required, not optional
    GOOGLE_POST_LOGIN_REDIRECT: Optional[AnyHttpUrl] = None
    ENVIRONMENT: str = "production"

    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    BUCKET_NAME: str = "user-photos"

    MODEL_LANDMARK_PATH: Optional[str] = None

    PUBLIC_BASE_URL: Optional[AnyHttpUrl] = None

    BACKEND_CORS_ORIGINS: Union[str, List[str]] = [
        "http://localhost:3001",
        "http://localhost:3000",
        "http://localhost:3002",
        "https://tiebymin-ai.vercel.app",
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v

    @validator("GOOGLE_REDIRECT_URI", pre=True)
    @classmethod
    def build_google_redirect_uri(cls, v, values):
        if v:
            return v
        
        public_base = values.get("PUBLIC_BASE_URL")
        api_v1 = values.get("API_V1_STR", "/v1")
        
        if public_base:
            base_url = str(public_base).rstrip("/")
            return f"{base_url}{api_v1}/auth/google/callback"
        
        return "http://localhost:8000/v1/auth/google/callback"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()