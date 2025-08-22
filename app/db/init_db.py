
from loguru import logger
from app.db.session import engine
from app.db.base import Base


def init_db() -> None:
    """Initialize database - create all tables."""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise
