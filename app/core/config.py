from typing import Optional, List, Union
from fastapi import Request
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings
import json
import os 
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/v1"
    PROJECT_NAME: str = "Tiebymin BE V2 - Production"

    DATABASE_URL: str
    SYNC_DATABASE_URL: str
    MODEL_PATH: Optional[str] = None 

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    GOOGLE_CLIENT_ID: str  # Required
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str 
    GOOGLE_POST_LOGIN_REDIRECT: Optional[str] = None  # Not set in your .env
    ENVIRONMENT: str = "production"
    
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    BUCKET_NAME: str = "user-photos"  # default kalau tidak ada di .env
    
    MODEL_LANDMARK_PATH: Optional[str] = None 

    BACKEND_CORS_ORIGINS: Union[str, List[str]] = [
        "http://localhost:3001", 
        "http://localhost:3000", 
        "http://localhost:3002", 
        "https://tiebymin-ai.vercel.app"
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
    
    def google_redirect(self, request: Request = None) -> str:
        if request:
            host = request.headers.get("host", "localhost:8000")
            scheme = "https" if request.url.scheme == "https" else "http"
            return f"{scheme}://{host}/v1/auth/google/callback"
        
        return self.GOOGLE_REDIRECT_URI


settings = Settings()