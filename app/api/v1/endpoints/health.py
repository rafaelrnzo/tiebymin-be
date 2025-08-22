
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.api.deps import get_db
from app.schemas.health import HealthResponse

router = APIRouter()


@router.get("/", response_model=HealthResponse)
async def health_check(db: Session = Depends(get_db)) -> HealthResponse:
    """Health check endpoint."""
    try:
        # Test database connection
        db.execute(text("SELECT 1"))
        return HealthResponse(
            status="healthy",
            message="Service is running properly",
            database_status="connected"
        )
    except Exception as e:
        return HealthResponse(
            status="unhealthy",
            message=f"Service is experiencing issues: {str(e)}",
            database_status="disconnected"
        )
