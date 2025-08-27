from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.repositories.user_repository import UserRepository, UserRepositoryImpl
from app.repositories.bmi_repository import BMICategoryRepositoryImpl, BMICategoryRepository
from app.repositories.body_shape_repository import BodyShapeRepositoryImpl, BodyShapeRepository
from app.repositories.celebrity_repository import CelebrityRepositoryImpl, CelebrityRepository
from app.repositories.face_shape_repository import FaceShapeRepositoryImpl, FaceShapeRepository
from app.repositories.color_analysis_repository import ColorAnalysisRepository, ColorAnalysisRepositoryImpl
from app.repositories.user_photo_repository import UserPhotoRepository, UserPhotoRepositoryImpl
from app.repositories.user_analysis_result_repository import UserAnalysisResultRepository, UserAnalysisResultRepositoryImpl
from app.repositories.analysis_feedback_repository import AnalysisFeedbackRepository, AnalysisFeedbackRepositoryImpl
# from app.repositories.analysis_session_repository import AnalysisSessionRepository, AnalysisSessionRepositoryImpl
from app.repositories.product_bmi_compatibility_repository import ProductBmiCompatibilityRepository, ProductBmiCompatibilityRepositoryImpl
from app.repositories.product_body_shape_compatibility_repository import ProductBodyShapeCompatibilityRepository, ProductBodyShapeCompatibilityRepositoryImpl
from app.repositories.product_color_analysis_compatibility_repository import ProductColorAnalysisCompatibilityRepository, ProductColorAnalysisCompatibilityRepositoryImpl
from app.repositories.product_color_repository import ProductColorRepository, ProductColorRepositoryImpl
from app.repositories.product_face_shape_compatibility_repository import ProductFaceShapeCompatibilityRepository, ProductFaceShapeCompatibilityRepositoryImpl
from app.repositories.order_repository import OrderRepository, OrderRepositoryImpl
from app.repositories.promo_code_repository import PromoCodeRepository, PromoCodeRepositoryImpl
from app.repositories.product_repository import ProductRepository, ProductRepositoryImpl
# from app.repositories.guest_user_repository import GuestUserRepository, GuestUserRepositoryImpl


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepositoryImpl(db_session=db)

# def get_guest_user_repository(db: Session = Depends(get_db)) -> GuestUserRepository:
#     return GuestUserRepositoryImpl(db_session=db)

def get_bmi_repository(db: Session = Depends(get_db)) -> BMICategoryRepository:
    return BMICategoryRepositoryImpl(db_session=db)

def get_body_shape_repository(db: Session = Depends(get_db)) -> BodyShapeRepository:
    return BodyShapeRepositoryImpl(db_session=db)

def get_celebrity_repository(db: Session = Depends(get_db)) -> CelebrityRepository:
    return CelebrityRepositoryImpl(db_session=db)

def get_face_shape_repository(db: Session = Depends(get_db)) -> FaceShapeRepository:
    return FaceShapeRepositoryImpl(db_session=db)

def get_color_analysis_repository(db: Session = Depends(get_db)) -> ColorAnalysisRepository:
    return ColorAnalysisRepositoryImpl(db_session=db)

def get_user_photo_repository(db: Session = Depends(get_db)) -> UserPhotoRepository:
    return UserPhotoRepositoryImpl(db_session=db)

def get_analysis_feedback_repository(db: Session = Depends(get_db)) -> AnalysisFeedbackRepository:
    return AnalysisFeedbackRepositoryImpl(db_session=db)

def get_user_analysis_result_repository(db: Session = Depends(get_db)) -> UserAnalysisResultRepository:
    return UserAnalysisResultRepositoryImpl(db_session=db)

# def get_analysis_session_repository(db: Session = Depends(get_db)) -> AnalysisSessionRepository:
#     return AnalysisSessionRepositoryImpl(db_session=db)

def get_product_repository(db: Session = Depends(get_db)) -> ProductRepository:
    return ProductRepositoryImpl(db_session=db)

def get_promo_code_repository(db: Session = Depends(get_db)) -> PromoCodeRepository:
    return PromoCodeRepositoryImpl(db_session=db)

def get_order_repository(db: Session = Depends(get_db)) -> OrderRepository:
    return OrderRepositoryImpl(db_session=db)

def get_product_face_shape_compatibility_repository(db: Session = Depends(get_db)) -> ProductFaceShapeCompatibilityRepository:
    return ProductFaceShapeCompatibilityRepositoryImpl(db_session=db)

def get_product_color_repository(db: Session = Depends(get_db)) -> ProductColorRepository:
    return ProductColorRepositoryImpl(db_session=db)

def get_product_color_analysis_compatibility_repository(db: Session = Depends(get_db)) -> ProductColorAnalysisCompatibilityRepository:
    return ProductColorAnalysisCompatibilityRepositoryImpl(db_session=db)

def get_product_body_shape_compatibility_repository(db: Session = Depends(get_db)) -> ProductBodyShapeCompatibilityRepository:
    return ProductBodyShapeCompatibilityRepositoryImpl(db_session=db)

def get_product_bmi_compatibility_repository(db: Session = Depends(get_db)) -> ProductBmiCompatibilityRepository:
    return ProductBmiCompatibilityRepositoryImpl(db_session=db)