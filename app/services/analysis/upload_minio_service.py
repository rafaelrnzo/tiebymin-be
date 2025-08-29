from minio import Minio
from minio.error import S3Error
import os

from app.core.config import settings
minio_client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False
)

if not minio_client.bucket_exists(settings.MINIO_BUCKET):
    minio_client.make_bucket(settings.MINIO_BUCKET)


def upload_photo_to_minio(file_path: str, object_name: str = None) -> str:
    try:
        if not object_name:
            object_name = os.path.basename(file_path)

        file_size = os.stat(file_path).st_size

        minio_client.put_object(
            bucket_name=settings.MINIO_BUCKET,
            object_name=object_name,
            data=open(file_path, "rb"),
            length=file_size,
        )

        print(f"✅ Berhasil upload {object_name} ke bucket {settings.MINIO_BUCKET}")
        return f"http://{settings.MINIO_ENDPOINT}/{settings.MINIO_BUCKET}/{object_name}"

    except S3Error as e:
        print(f"❌ Gagal upload: {e}")
        return None
