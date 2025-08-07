import uuid
from fastapi import UploadFile, HTTPException
from db.supabase_db import supabase

async def upload_photo_to_supabase(file: UploadFile, analysis_result_id: uuid.UUID, photo_type: str) -> str:
    try:
        folder = f"analysis/{analysis_result_id}/{photo_type}"
        filename = f"{uuid.uuid4()}_{file.filename}"
        path = f"{folder}/{filename}"

        content = await file.read()

        response = supabase.storage.from_("user-photos").upload(
            path, content, {"content-type": file.content_type}
        )

        if hasattr(response, "status_code") and response.status_code >= 400:
            raise HTTPException(status_code=500, detail="Upload to Supabase failed")

        return path

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload error: {str(e)}")
