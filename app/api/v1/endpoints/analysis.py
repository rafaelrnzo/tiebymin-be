from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
import uuid
from typing import Dict, Any
from datetime import datetime

from services.analysis.face_shape_services import face_shape_service
from services.analysis.bmi_services import BMIService
from services.analysis.color_tone_services import ColorToneService
from services.analysis.face_landmark_service import face_landmark_service
from services.analysis.celebrity_match_services import CelebrityMatchService
from services.supabase.supabase_upload_photo import upload_photo_to_supabase, upload_processed_photo_to_supabase

from schemas.user_analysis_result import UserAnalysisResultCreate
from schemas.user_photo import UserPhotoCreate

from repositories.user_analysis_result_repository import UserAnalysisResultRepository
from repositories.face_shape_repository import FaceShapeRepository
from repositories.color_analysis_repository import ColorAnalysisRepository
from repositories.body_shape_repository import BodyShapeRepository
from repositories.user_photo_repository import UserPhotoRepository
from repositories.bmi_repository import BMICategoryRepository
from repositories.celebrity_repository import CelebrityRepository 

from dependencies.dependencies import (
    get_user_analysis_result_repository,
    get_face_shape_repository,
    get_color_analysis_repository,
    get_body_shape_repository,
    get_user_photo_repository,
    get_bmi_repository,
    get_celebrity_repository
)

router = APIRouter(prefix="/v1/analysis", tags=["Analysis"])

@router.post("/full-analysis")
async def perform_full_analysis(
    user_id: uuid.UUID = Form(...),
    tinggi_badan: float = Form(...),
    berat_badan: float = Form(...),
    umur: int = Form(...),
    body_shape_id: uuid.UUID = Form(...),
    foto_wajah: UploadFile = File(...),

    result_repo: UserAnalysisResultRepository = Depends(get_user_analysis_result_repository),
    face_shape_repo: FaceShapeRepository = Depends(get_face_shape_repository),
    color_analysis_repo: ColorAnalysisRepository = Depends(get_color_analysis_repository),
    body_shape_repo: BodyShapeRepository = Depends(get_body_shape_repository),
    photo_repo: UserPhotoRepository = Depends(get_user_photo_repository),
    bmi_repo: BMICategoryRepository = Depends(get_bmi_repository),
    celebrity_repo: CelebrityRepository = Depends(get_celebrity_repository)

) -> Dict[str, Any]:
    bmi_service = BMIService(bmi_repo=bmi_repo)
    color_tone_service = ColorToneService()
    celebrity_service = CelebrityMatchService(celebrity_repo=celebrity_repo)
    
    file_content = await foto_wajah.read()

    try:
        face_shape_result = face_shape_service.predict(image_bytes=file_content)
        color_tone_result = color_tone_service.detect(image_bytes=file_content)
        
        bmi_value = bmi_service.calculate_bmi_value(weight_kg=berat_badan, height_cm=tinggi_badan)
        bmi_category_id = bmi_service.get_bmi_category_id(bmi_value)

        face_shape_record = face_shape_repo.get_by_name(face_shape_result.get("label"))
        color_analysis_record = color_analysis_repo.get_by_name(color_tone_result.get("category"))
        
        celebrity_id = None
        if face_shape_record and color_analysis_record:
            celebrity_id = celebrity_service.find_celebrity_match_id(
                face_shape_id=face_shape_record.id,
                color_analysis_id=color_analysis_record.id
            )

        analysis_details = {
            "face_shape": face_shape_result,
            "bmi": {"value": bmi_value},
            "color_tone": color_tone_result,
            "user_input": {"age": umur, "height": tinggi_badan, "weight": berat_badan},
            "matched_celebrity_id": str(celebrity_id) if celebrity_id else None
        }

        new_analysis_data = UserAnalysisResultCreate(
            user_id=user_id,
            analysis_details=analysis_details,
            is_final_result=True,
            face_shape_id=face_shape_record.id if face_shape_record else None,
            color_analysis_id=color_analysis_record.id if color_analysis_record else None,
            body_shape_id=body_shape_id,
            bmi_category_id=bmi_category_id,
            celebrity_id=celebrity_id 
        )
        
        created_result = result_repo.create(new_analysis_data)
        analysis_result_id = created_result.id

        original_photo_path = await upload_photo_to_supabase(foto_wajah, analysis_result_id, "face_original")
        original_photo_data = UserPhotoCreate(
            analysis_result_id=analysis_result_id,
            photo_type="face_original",
            file_path=original_photo_path,
            original_filename=foto_wajah.filename,
            file_size=foto_wajah.size,
            mime_type=foto_wajah.content_type
        )
        photo_repo.create(original_photo_data)

        annotated_bytes, blendshape_data = face_landmark_service.analyze_and_annotate(file_content)
        annotated_photo_path = await upload_processed_photo_to_supabase(
            image_bytes=annotated_bytes,
            analysis_result_id=analysis_result_id,
            original_filename=foto_wajah.filename
        )
        annotated_photo_data = UserPhotoCreate(
            analysis_result_id=analysis_result_id,
            photo_type="face_landmarked",
            file_path=annotated_photo_path,
            original_filename=f"annotated_{foto_wajah.filename}",
            file_size=len(annotated_bytes),
            mime_type="image/png",
            is_processed=True,
            analysis_metadata=blendshape_data,
            processed_at=datetime.utcnow()
        )
        photo_repo.create(annotated_photo_data)

        return {
            "message": "Analysis completed and results saved successfully.",
            "analysis_result_id": analysis_result_id
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred during analysis.")
    
@router.post("/face-color-analysis")
async def analyze_face_and_color(
    foto_wajah: UploadFile = File(...),
):
    file_content = await foto_wajah.read()

    try:
        face_shape_result = face_shape_service.predict(image_bytes=file_content)
        color_tone_result = ColorToneService().detect(image_bytes=file_content)

        return {
            "face_shape": face_shape_result, 
            "color_tone": color_tone_result  
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred during face/color analysis."
        )
