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

    def get_recommendations(self, analysis_result_id: uuid.UUID) -> Dict[str, List[Dict[str, Any]]]:
        analysis_result = self.user_analysis_repo.get_by_id(analysis_result_id)
        if not analysis_result:
            return {"hijab": [], "clothes": []}

        all_products = self.product_repo.get_all()
        face_compat_data = self.face_shape_compat_repo.get_all()
        body_compat_data = self.body_shape_compat_repo.get_all()
        color_compat_data = self.color_analysis_compat_repo.get_all()
        bmi_compat_data = self.bmi_compat_repo.get_all()
        
        face_scores = {(item.product_id, item.face_shape_id): item.compatibility_score for item in face_compat_data}
        body_scores = {(item.product_id, item.body_shape_id): item.compatibility_score for item in body_compat_data}
        color_scores = {(item.product_color_id, item.color_analysis_id): item.compatibility_score for item in color_compat_data}
        bmi_scores = {(item.product_id, item.bmi_category_id): item.compatibility_score for item in bmi_compat_data}

        ranked_hijabs = []
        ranked_clothes = []

        for product in all_products:
            total_score = 0
            product_dict = product.dict()

            if product.category.lower() == 'hijab':
                score1 = face_scores.get((product.id, analysis_result.face_shape_id), 0)
                # Omitting color score for simplicity as it requires a more complex lookup
                total_score = score1
                if total_score > 0:
                    product_dict['total_compatibility_score'] = total_score
                    ranked_hijabs.append(product_dict)
            
            elif product.category.lower() == 'clothes':
                score1 = body_scores.get((product.id, analysis_result.body_shape_id), 0)
                score2 = bmi_scores.get((product.id, analysis_result.bmi_category_id), 0)
                total_score = score1 + score2
                if total_score > 0:
                    product_dict['total_compatibility_score'] = total_score
                    ranked_clothes.append(product_dict)
        
        sorted_hijabs = sorted(ranked_hijabs, key=lambda p: p['total_compatibility_score'], reverse=True)
        sorted_clothes = sorted(ranked_clothes, key=lambda p: p['total_compatibility_score'], reverse=True)

        return {
            "hijab": sorted_hijabs[:3],
            "clothes": sorted_clothes[:3]
        }