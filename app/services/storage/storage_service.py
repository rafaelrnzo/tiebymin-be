import os
from .s3_client import s3_client

MINIO_BUCKET = os.getenv("S3_BUCKET", "user-photos")

def upload_file(file_path: str, object_name: str = None) -> str:
    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        s3_client.upload_file(file_path, MINIO_BUCKET, object_name)
        url = f"{s3_client.meta.endpoint_url}/{MINIO_BUCKET}/{object_name}"
        print(f"✅ Berhasil upload {object_name} ke bucket {MINIO_BUCKET}")
        return url
    except Exception as e:
        raise RuntimeError(f"❌ Gagal upload {file_path}: {str(e)}")
