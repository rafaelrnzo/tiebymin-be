import boto3
import os

# Konfigurasi via ENV agar fleksibel (bisa AWS S3 / MinIO)
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID", "minioadmin")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "miniopassword")
S3_ENDPOINT = os.getenv("S3_ENDPOINT", "http://localhost:9000")  # AWS S3 = None
S3_REGION = os.getenv("S3_REGION", "us-east-1")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    endpoint_url=S3_ENDPOINT,  # kalau pakai AWS S3, set None / hapus
    region_name=S3_REGION
)
