# app/core/settings.py
from typing import Optional, List, Union, TYPE_CHECKING
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings
import json

if TYPE_CHECKING:
    from fastapi import Request

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
    GOOGLE_REDIRECT_URI: Optional[AnyHttpUrl] = None
    GOOGLE_POST_LOGIN_REDIRECT: Optional[AnyHttpUrl] = None
    ENVIRONMENT: str = "production"

    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    BUCKET_NAME: str = "user-photos"

    MODEL_LANDMARK_PATH: Optional[str] = None

    PUBLIC_BASE_URL: Optional[AnyHttpUrl] = None

    GOOGLE_REDIRECT_PATH: str = "/v1/auth/google/callback"

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

    class Config:
        env_file = ".env"
        case_sensitive = True

    def _build_url(self, path: str, base: Optional[str] = None) -> str:
        base = (base or (self.PUBLIC_BASE_URL or "http://localhost:8000")).rstrip("/")
        return f"{base}{path}"

    def google_redirect(self, request: Optional["Request"] = None) -> str:
        if self.GOOGLE_REDIRECT_URI:
            return str(self.GOOGLE_REDIRECT_URI)

        if request is not None:
            return str(request.url_for("callback_google"))

        return self._build_url(self.GOOGLE_REDIRECT_PATH)


settings = Settings()
