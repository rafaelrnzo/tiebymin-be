
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import uuid

from db.supabase_db import supabase 
from services.supabase.supabase_upload_photo import upload_photo_to_supabase
from services.analysis.face_shape_services import face_shape_service
from services.analysis.bmi_services import BMIService
from services.analysis.color_tone_services import ColorToneService
router = APIRouter(prefix="/v1/analysis", tags=["Analysis"])

@router.post("/face-shape")
async def upload_then_analyze_from_supabase(
    tinggi_badan: float = Form(...),
    berat_badan: float = Form(...),
    umur: int = Form(...),
    body_shape_type: str = Form(...),
    foto_wajah: UploadFile = File(...)
):
    analysis_result_id = uuid.uuid4()
    color_tone_service = ColorToneService()

    try:
        print("Mulai mengunggah foto ke Supabase...")
        uploaded_path = await upload_photo_to_supabase(
            file=foto_wajah,
            analysis_result_id=analysis_result_id,
            photo_type="face"
        )
        print(f"Foto berhasil diunggah ke path: {uploaded_path}")

        print(f"Mengunduh foto dari {uploaded_path} untuk analisis...")
        response_bytes = supabase.storage.from_("user-photos").download(uploaded_path)
        
        if response_bytes is None:
            raise HTTPException(
                status_code=404, 
                detail="File tidak ditemukan di Supabase setelah diunggah."
            )
        print("Foto berhasil diunduh dari Supabase.")
        
        print("Memulai analisis bentuk wajah...")
        face_shape_result = face_shape_service.predict(image_bytes=response_bytes)
        print("Analisis bentuk wajah selesai.")
        
        bmi_result = BMIService.calculate_bmi(weight_kg=berat_badan, height_cm=tinggi_badan)
        color_tone = color_tone_service.detect(image_bytes=response_bytes)
        
        return {
            "message": "Upload and analysis from Supabase successful",
            "analysis_result_id": analysis_result_id,
            "supabase_path": uploaded_path,
            "face_shape_result": face_shape_result,
            "bmi_result": bmi_result,
            "color_tone": color_tone,
            "body_shape_type": body_shape_type,
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")