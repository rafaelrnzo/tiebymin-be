from fastapi import APIRouter
from app.api.v1.endpoints import user, auth, bmi, body_shape, celebrity, face_shape, color_analysis, user_photo,user_analysis_result, analysis_feedback, product_bmi_compatibility, product_body_shape_compatibility, product_color_analysis_compatibility, product_color, product_face_shape_compatibility, analysis, color_analysis, order, promo_code, product, user_profile

api_router = APIRouter()

# Core Feature Endpoints
api_router.include_router(auth.router)
api_router.include_router(analysis.router)
api_router.include_router(user_profile.router)
# CRUD Endpoints
api_router.include_router(user.router)
api_router.include_router(bmi.router)
api_router.include_router(body_shape.router)
api_router.include_router(celebrity.router)
api_router.include_router(face_shape.router)
api_router.include_router(color_analysis.router)
api_router.include_router(user_photo.router)
api_router.include_router(user_analysis_result.router)
api_router.include_router(analysis_feedback.router)
api_router.include_router(product_bmi_compatibility.router)
api_router.include_router(product_body_shape_compatibility.router)
api_router.include_router(product_color_analysis_compatibility.router)
api_router.include_router(product_color.router)
api_router.include_router(product_face_shape_compatibility.router)
api_router.include_router(color_analysis.router)
api_router.include_router(order.router)
api_router.include_router(promo_code.router)
api_router.include_router(product.router)
