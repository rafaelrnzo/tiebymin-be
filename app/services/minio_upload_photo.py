import uuid
import boto3  # pyright: ignore[reportMissingImports]
from fastapi import UploadFile, HTTPException
from app.core.config import settings

# Gunakan settings dari pydantic, bukan os.getenv lagi
s3_client = boto3.client(
    "s3",
    endpoint_url=settings.MINIO_ENDPOINT,
    aws_access_key_id=settings.MINIO_ACCESS_KEY,
    aws_secret_access_key=settings.MINIO_SECRET_KEY,
)

async def upload_photo_to_minio(
    file: UploadFile, 
    analysis_result_id: uuid.UUID, 
    photo_type: str
) -> str:
    try:
        folder = f"analysis/{analysis_result_id}/{photo_type}"
        original_filename = file.filename or "untitled"
        filename = f"{uuid.uuid4()}_{original_filename}"
        path = f"{folder}/{filename}"

        content = await file.read()
        await file.seek(0)

        s3_client.put_object(
            Bucket=settings.BUCKET_NAME,
            Key=path,
            Body=content,
            ContentType=file.content_type
        )
        return path
    except Exception as e:
        print(f"Upload error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during original file upload.")

async def upload_processed_photo_to_minio(
    image_bytes: bytes, 
    analysis_result_id: uuid.UUID, 
    original_filename: str
) -> str:
    try:
        folder = f"analysis/{analysis_result_id}/processed"
        filename = f"annotated_{uuid.uuid4()}_{original_filename}.png"
        path = f"{folder}/{filename}"

        s3_client.put_object(
            Bucket=settings.BUCKET_NAME,
            Key=path,
            Body=image_bytes,
            ContentType="image/png"
        )
        return path
    except Exception as e:
        print(f"Processed photo upload error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during processed file upload.")
