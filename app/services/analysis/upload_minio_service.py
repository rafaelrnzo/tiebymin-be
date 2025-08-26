from minio import Minio
from minio.error import S3Error
import os

minio_client = Minio(
    "localhost:9000",         
    access_key="minioadmin",
    secret_key="miniopassword",
    secure=False                 
)

BUCKET_NAME = "user-photos"

if not minio_client.bucket_exists(BUCKET_NAME):
    minio_client.make_bucket(BUCKET_NAME)


def upload_photo_to_minio(file_path: str, object_name: str = None) -> str:
    try:
        if not object_name:
            object_name = os.path.basename(file_path)

        file_size = os.stat(file_path).st_size

        minio_client.put_object(
            bucket_name=BUCKET_NAME,
            object_name=object_name,
            data=open(file_path, "rb"),
            length=file_size,
        )

        print(f"✅ Berhasil upload {object_name} ke bucket {BUCKET_NAME}")
        return f"http://localhost:9000/{BUCKET_NAME}/{object_name}"

    except S3Error as e:
        print(f"❌ Gagal upload: {e}")
        return None
