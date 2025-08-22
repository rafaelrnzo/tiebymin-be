from fastapi import APIRouter
from app.api.v1.endpoints import health, auth, training, review, evaluation

api_router = APIRouter()

# Include health endpoint
api_router.include_router(health.router, prefix="/health", tags=["health"])
# Include auth endpoints
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
# Include training endpoints
api_router.include_router(training.router, prefix="/training", tags=["training"])
# Include review endpoints
api_router.include_router(review.router, prefix="/review", tags=["review"])
# Include evaluation endpoints
api_router.include_router(evaluation.router, prefix="/evaluation", tags=["evaluation"])
