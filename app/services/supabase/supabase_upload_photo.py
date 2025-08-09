import uuid
from fastapi import UploadFile, HTTPException
from db.supabase_db import supabase

async def upload_photo_to_supabase(
    file: UploadFile, 
    analysis_result_id: uuid.UUID, 
    photo_type: str
) -> str:
    try:
        folder = f"analysis/{analysis_result_id}/{photo_type}"
        original_filename = file.filename if file.filename else "untitled"
        filename = f"{uuid.uuid4()}_{original_filename}"
        path = f"{folder}/{filename}"

        content = await file.read()
        await file.seek(0)

        supabase.storage.from_("user-photos").upload(
            path, content, {"content-type": file.content_type}
        )
        return path
    except Exception as e:
        print(f"Upload error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during original file upload.")

async def upload_processed_photo_to_supabase(
    image_bytes: bytes, 
    analysis_result_id: uuid.UUID, 
    original_filename: str
) -> str:
    try:
        folder = f"analysis/{analysis_result_id}/processed"
        filename = f"annotated_{uuid.uuid4()}_{original_filename}.png"
        path = f"{folder}/{filename}"

        supabase.storage.from_("user-photos").upload(
            path, image_bytes, {"content-type": "image/png"}
        )
        return path
    except Exception as e:
        print(f"Processed photo upload error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during processed file upload.")