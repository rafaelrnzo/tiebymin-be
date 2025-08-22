
from pydantic import BaseModel
from typing import Optional


class HealthResponse(BaseModel):
    """Health check response schema."""

    status: str
    message: str
    database_status: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "status": "healthy",
                "message": "Service is running properly",
                "database_status": "connected",
            }
        }
