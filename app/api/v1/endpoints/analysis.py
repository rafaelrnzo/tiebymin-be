from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
import uuid
from typing import Dict, Any

from services.analysis.face_shape_services import face_shape_service
from services.analysis.bmi_services import BMIService
from services.analysis.color_tone_services import ColorToneService
from schemas.user_analysis_result import UserAnalysisResultCreate

# Impor repository dan dependency yang dibutuhkan
from repositories.user_analysis_result_repository import UserAnalysisResultRepository
from repositories.face_shape_repository import FaceShapeRepository
from repositories.color_analysis_repository import ColorAnalysisRepository
from dependencies.dependencies import (
    get_user_analysis_result_repository, 
    get_face_shape_repository,
    get_color_analysis_repository
)

router = APIRouter(prefix="/v1/analysis", tags=["Analysis"])

@router.post("/full-analysis")
async def perform_full_analysis(
    user_id: uuid.UUID = Form(...),
    tinggi_badan: float = Form(...),
    berat_badan: float = Form(...),
    umur: int = Form(...),
    body_shape_type: str = Form(...), 
    foto_wajah: UploadFile = File(...),
    
    result_repo: UserAnalysisResultRepository = Depends(get_user_analysis_result_repository),
    face_shape_repo: FaceShapeRepository = Depends(get_face_shape_repository),
    color_analysis_repo: ColorAnalysisRepository = Depends(get_color_analysis_repository)

) -> Dict[str, Any]:
    
    color_tone_service = ColorToneService()

    try:
        file_content = await foto_wajah.read()
        
        face_shape_result = face_shape_service.predict(image_bytes=file_content)
        bmi_result = BMIService.calculate_bmi(weight_kg=berat_badan, height_cm=tinggi_badan)
        color_tone_result = color_tone_service.detect(image_bytes=file_content)

        face_shape_label = face_shape_result.get("label")
        color_analysis_label = color_tone_result.get("category")

        face_shape_record = face_shape_repo.get_by_name(face_shape_label)
        color_analysis_record = color_analysis_repo.get_by_name(color_analysis_label)

        face_shape_id = face_shape_record.id if face_shape_record else None
        color_analysis_id = color_analysis_record.id if color_analysis_record else None
        
        all_analysis_details = {
            "face_shape": face_shape_result,
            "bmi": bmi_result,
            "color_tone": color_tone_result,
            "body_shape_input": body_shape_type,
            "user_input": {"age": umur, "height": tinggi_badan, "weight": berat_badan}
        }

        new_analysis_data = UserAnalysisResultCreate(
            user_id=user_id,
            analysis_details=all_analysis_details,
            is_final_result=True,
            body_shape_id=body_shape_type,
            face_shape_id=face_shape_id,
            color_analysis_id=color_analysis_id,
        )

        created_result = result_repo.create(new_analysis_data)

        return {
            "message": "Analysis completed and results saved successfully.",
            "analysis_result_id": created_result.id
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred during analysis.")