from fastapi import APIRouter, Depends, HTTPException
import uuid
from typing import List, Any
from services.analysis.product_match_services import ProductRecommendationService

# Impor semua repository yang dibutuhkan oleh service
from repositories.user_analysis_result_repository import UserAnalysisResultRepository
from repositories.product_repository import ProductRepository
from repositories.product_face_shape_compatibility_repository import ProductFaceShapeCompatibilityRepository
from repositories.product_body_shape_compatibility_repository import ProductBodyShapeCompatibilityRepository
from repositories.product_color_analysis_compatibility_repository import ProductColorAnalysisCompatibilityRepository
from repositories.product_bmi_compatibility_repository import ProductBmiCompatibilityRepository
from dependencies.dependencies import (
    get_user_analysis_result_repository, get_product_repository,
    get_product_face_shape_compatibility_repository, get_product_body_shape_compatibility_repository,
    get_product_color_analysis_compatibility_repository, get_product_bmi_compatibility_repository
)

router = APIRouter(prefix="/v1/recommendations", tags=["Product Recommendations"])

@router.get("/{analysis_result_id}", response_model=List[Any])
def get_product_recommendations_from_backend(
    analysis_result_id: uuid.UUID,
    user_analysis_repo: UserAnalysisResultRepository = Depends(get_user_analysis_result_repository),
    product_repo: ProductRepository = Depends(get_product_repository),
    face_shape_compat_repo: ProductFaceShapeCompatibilityRepository = Depends(get_product_face_shape_compatibility_repository),
    body_shape_compat_repo: ProductBodyShapeCompatibilityRepository = Depends(get_product_body_shape_compatibility_repository),
    color_analysis_compat_repo: ProductColorAnalysisCompatibilityRepository = Depends(get_product_color_analysis_compatibility_repository),
    bmi_compat_repo: ProductBmiCompatibilityRepository = Depends(get_product_bmi_compatibility_repository)
):
    # Buat instance service dengan semua repository yang diinjeksi
    service = ProductRecommendationService(
        user_analysis_repo, product_repo, face_shape_compat_repo,
        body_shape_compat_repo, color_analysis_compat_repo, bmi_compat_repo
    )
    
    recommendations = service.get_recommendations(analysis_result_id)
    if not recommendations:
        return []
    
    return recommendations