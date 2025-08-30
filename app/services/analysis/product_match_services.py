import uuid
from typing import List, Dict, Any, Optional
from collections import defaultdict

from app.utils import color_utils

from app.repositories.user_analysis_result_repository import UserAnalysisResultRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.product_color_repository import ProductColorRepository
from app.repositories.color_analysis_repository import ColorAnalysisRepository
from app.repositories.product_face_shape_compatibility_repository import ProductFaceShapeCompatibilityRepository
from app.repositories.product_body_shape_compatibility_repository import ProductBodyShapeCompatibilityRepository
from app.repositories.product_bmi_compatibility_repository import ProductBmiCompatibilityRepository


class ProductRecommendationService:
    def __init__(
        self,
        user_analysis_repo: UserAnalysisResultRepository,
        product_repo: ProductRepository,
        product_color_repo: ProductColorRepository,
        color_analysis_repo: ColorAnalysisRepository,
        face_shape_compat_repo: ProductFaceShapeCompatibilityRepository,
        body_shape_compat_repo: ProductBodyShapeCompatibilityRepository,
        bmi_compat_repo: ProductBmiCompatibilityRepository,
    ):
        self.user_analysis_repo = user_analysis_repo
        self.product_repo = product_repo
        self.product_color_repo = product_color_repo
        self.color_analysis_repo = color_analysis_repo
        self.face_shape_compat_repo = face_shape_compat_repo
        self.body_shape_compat_repo = body_shape_compat_repo
        self.bmi_compat_repo = bmi_compat_repo

    def _safe_product_dict(self, product: Any) -> Dict[str, Any]:
        """
        Ambil field penting dari instance ORM product secara aman.
        Tambahkan field lain kalau dibutuhkan (price, images, brand, dll).
        """
        return {
            "id": getattr(product, "id", None),
            "name": getattr(product, "name", None),
            "category": (getattr(product, "category", "") or "").lower(),
            "description": getattr(product, "description", None),
            "price": getattr(product, "price", None),
            "slug": getattr(product, "slug", None),
            "thumbnail_url": getattr(product, "thumbnail_url", None),
        }

    def get_recommendations(self, analysis_result_id: uuid.UUID) -> Dict[str, List[Dict[str, Any]]]:
        # 1) Ambil summary analisis user
        analysis_result = self.user_analysis_repo.get_by_id(analysis_result_id)
        if not analysis_result:
            return {"hijab": [], "clothes": []}

        # 2) Siapkan warna rekomendasi (LAB) dari hasil color analysis
        color_analysis_details = None
        if getattr(analysis_result, "color_analysis_id", None):
            color_analysis_details = self.color_analysis_repo.get_by_id(analysis_result.color_analysis_id)

        recommended_lab_colors: List[List[float]] = []
        if color_analysis_details and getattr(color_analysis_details, "best_colour", None):
            # diasumsikan best_colour adalah list of hex strings
            for hex_code in list(color_analysis_details.best_colour):
                try:
                    rgb = color_utils.hex_to_rgb(hex_code)
                    recommended_lab_colors.append(color_utils.rgb_to_lab(rgb))
                except (ValueError, IndexError, TypeError):
                    continue

        # 3) Ambil seluruh data referensi
        all_products = self.product_repo.get_all()
        all_product_colors = self.product_color_repo.get_all()
        face_compat_data = self.face_shape_compat_repo.get_all()
        body_compat_data = self.body_shape_compat_repo.get_all()
        bmi_compat_data = self.bmi_compat_repo.get_all()

        # 4) Index skor kompatibilitas
        face_scores = {
            (item.product_id, item.face_shape_id): item.compatibility_score
            for item in face_compat_data
        }
        body_scores = {
            (item.product_id, item.body_shape_id): item.compatibility_score
            for item in body_compat_data
        }
        bmi_scores = {
            (item.product_id, item.bmi_category_id): item.compatibility_score
            for item in bmi_compat_data
        }

        # 5) Map warna produk
        product_colors_map: Dict[Any, List[Any]] = defaultdict(list)
        for color in all_product_colors:
            product_colors_map[color.product_id].append(color)

        ranked_hijabs: List[Dict[str, Any]] = []
        ranked_clothes: List[Dict[str, Any]] = []

        # 6) Scoring per produk
        for product in all_products:
            p: Dict[str, Any] = self._safe_product_dict(product)

            # Skip jika id atau kategori tidak valid
            if not p["id"] or not p["category"]:
                continue

            product_available_colors = product_colors_map.get(p["id"], [])

            # Hitung jarak warna (DeltaE) terhadap warna terbaik user -> ambil top 5 terdekat
            product_color_distances: List[Dict[str, Any]] = []
            if recommended_lab_colors and product_available_colors:
                for p_color in product_available_colors:
                    hex_str: Optional[str] = getattr(p_color, "hex_color", None)
                    if not hex_str:
                        continue
                    try:
                        product_rgb = color_utils.hex_to_rgb(hex_str)
                        product_lab = color_utils.rgb_to_lab(product_rgb)
                        min_distance = min(
                            color_utils.calculate_delta_e(product_lab, rec_lab)
                            for rec_lab in recommended_lab_colors
                        )
                        product_color_distances.append(
                            {"hex": hex_str, "distance": float(min_distance)}
                        )
                    except (ValueError, IndexError, TypeError):
                        continue

            sorted_product_colors = sorted(product_color_distances, key=lambda c: c["distance"])
            top_5_colors = [c["hex"] for c in sorted_product_colors[:5]]
            p["color_recommendations"] = top_5_colors

            # Skor kategori
            if p["category"] == "hijab":
                # Face shape only
                face_shape_id = getattr(analysis_result, "face_shape_id", None)
                total_score = face_scores.get((p["id"], face_shape_id), 0)
                if total_score > 0 and top_5_colors:
                    p["total_compatibility_score"] = float(total_score)
                    ranked_hijabs.append(p)

            elif p["category"] == "clothes":
                # Body shape + BMI
                body_shape_id = getattr(analysis_result, "body_shape_id", None)
                bmi_category_id = getattr(analysis_result, "bmi_category_id", None)
                score1 = body_scores.get((p["id"], body_shape_id), 0)
                score2 = bmi_scores.get((p["id"], bmi_category_id), 0)
                total_score = (score1 or 0) + (score2 or 0)
                if total_score > 0:
                    p["total_compatibility_score"] = float(total_score)
                    ranked_clothes.append(p)

        # 7) Urutkan & batasi jumlah hasil
        sorted_hijabs = sorted(ranked_hijabs, key=lambda x: x["total_compatibility_score"], reverse=True)
        sorted_clothes = sorted(ranked_clothes, key=lambda x: x["total_compatibility_score"], reverse=True)

        return {
            "hijab": sorted_hijabs[:3],
            "clothes": sorted_clothes[:3],
        }

