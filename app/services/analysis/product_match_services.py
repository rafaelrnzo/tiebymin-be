import uuid
from typing import List, Dict, Any
from repositories.user_analysis_result_repository import UserAnalysisResultRepository
from repositories.product_repository import ProductRepository
from repositories.product_face_shape_compatibility_repository import ProductFaceShapeCompatibilityRepository
from repositories.product_body_shape_compatibility_repository import ProductBodyShapeCompatibilityRepository
from repositories.product_color_analysis_compatibility_repository import ProductColorAnalysisCompatibilityRepository
from repositories.product_bmi_compatibility_repository import ProductBmiCompatibilityRepository

class ProductRecommendationService:
    def __init__(
        self,
        user_analysis_repo: UserAnalysisResultRepository,
        product_repo: ProductRepository,
        face_shape_compat_repo: ProductFaceShapeCompatibilityRepository,
        body_shape_compat_repo: ProductBodyShapeCompatibilityRepository,
        color_analysis_compat_repo: ProductColorAnalysisCompatibilityRepository,
        bmi_compat_repo: ProductBmiCompatibilityRepository
    ):
        self.user_analysis_repo = user_analysis_repo
        self.product_repo = product_repo
        self.face_shape_compat_repo = face_shape_compat_repo
        self.body_shape_compat_repo = body_shape_compat_repo
        self.color_analysis_compat_repo = color_analysis_compat_repo
        self.bmi_compat_repo = bmi_compat_repo

    def get_recommendations(self, analysis_result_id: uuid.UUID) -> List[Dict[str, Any]]:
        # 1. Ambil hasil analisis pengguna
        analysis_result = self.user_analysis_repo.get_by_id(analysis_result_id)
        if not analysis_result:
            return []

        # 2. Ambil semua produk dan data kompatibilitas
        all_products = self.product_repo.get_all()
        face_compat_data = self.face_shape_compat_repo.get_all()
        body_compat_data = self.body_shape_compat_repo.get_all()
        color_compat_data = self.color_analysis_compat_repo.get_all()
        bmi_compat_data = self.bmi_compat_repo.get_all()
        
        # 3. Buat Peta (Map) untuk pencarian skor yang cepat
        face_scores = {(item.product_id, item.face_shape_id): item.compatibility_score for item in face_compat_data}
        body_scores = {(item.product_id, item.body_shape_id): item.compatibility_score for item in body_compat_data}
        color_scores = {(item.product_color_id, item.color_analysis_id): item.compatibility_score for item in color_compat_data}
        bmi_scores = {(item.product_id, item.bmi_category_id): item.compatibility_score for item in bmi_compat_data}

        # 4. Kalkulasi skor untuk setiap produk
        ranked_products = []
        for product in all_products:
            total_score = 0
            if product.category.lower() == 'hijab':
                score1 = face_scores.get((product.id, analysis_result.face_shape_id), 0)
                # Note: Color compatibility is by product_color_id, this requires a more complex lookup.
                # For simplicity here, we'll omit color score or assume a simplified logic.
                # A proper implementation would need to check all product_colors for the product.
                total_score = score1
            
            elif product.category.lower() == 'clothes':
                score1 = body_scores.get((product.id, analysis_result.body_shape_id), 0)
                score2 = bmi_scores.get((product.id, analysis_result.bmi_category_id), 0)
                total_score = score1 + score2
            
            if total_score > 0:
                product_dict = product.dict()
                product_dict['total_compatibility_score'] = total_score
                ranked_products.append(product_dict)
        
        # 5. Urutkan produk berdasarkan skor tertinggi
        return sorted(ranked_products, key=lambda p: p['total_compatibility_score'], reverse=True)