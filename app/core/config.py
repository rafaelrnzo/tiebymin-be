from typing import Optional, List, Union
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings
import json


class Settings(BaseSettings):
    """Application settings configuration."""

    # Project Information
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "BE-FT"

    # Database Configuration
    DATABASE_URL: str
    SYNC_DATABASE_URL: str

    # Security Configuration
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Environment
    ENVIRONMENT: str = "development"

    # CORS Configuration
    BACKEND_CORS_ORIGINS: Union[str, List[str]] = []

    # External API Keys
    FAL_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            try:
                # Try to parse as JSON array
                return json.loads(v)
            except json.JSONDecodeError:
                # If JSON parsing fails, try comma-separated values
                return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v

    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
