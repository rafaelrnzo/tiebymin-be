import os
from .s3_client import s3_client

BUCKET_NAME = os.getenv("S3_BUCKET", "user-photos")

def upload_file(file_path: str, object_name: str = None) -> str:
    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        s3_client.upload_file(file_path, BUCKET_NAME, object_name)
        url = f"{s3_client.meta.endpoint_url}/{BUCKET_NAME}/{object_name}"
        print(f"✅ Berhasil upload {object_name} ke bucket {BUCKET_NAME}")
        return url
    except Exception as e:
        raise RuntimeError(f"❌ Gagal upload {file_path}: {str(e)}")
