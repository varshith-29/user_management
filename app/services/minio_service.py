from minio import Minio
from minio.error import S3Error
from fastapi import HTTPException
import uuid
from app.dependencies.config import get_settings
from PIL import Image
import io

class MinioService:
    def __init__(self):
        self.settings = get_settings()
        self.client = Minio(
            self.settings.minio_url,
            access_key=self.settings.minio_root_user,
            secret_key=self.settings.minio_root_password,
            secure=self.settings.minio_secure
        )
        self._ensure_bucket_exists()

    def _ensure_bucket_exists(self):
        try:
            if not self.client.bucket_exists(self.settings.minio_bucket):
                self.client.make_bucket(self.settings.minio_bucket)
        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"Minio error: {str(e)}")

    def upload_profile_picture(self, file_content: bytes, content_type: str) -> str:
        try:
            # Validate and optimize image
            image = Image.open(io.BytesIO(file_content))
            if image.format.lower() not in ['jpeg', 'jpg', 'png']:
                raise HTTPException(status_code=400, detail="Only JPEG and PNG images are allowed")
            
            # Resize image if too large
            max_size = (800, 800)
            image.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Convert to bytes
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format=image.format)
            img_byte_arr = img_byte_arr.getvalue()

            # Generate unique filename
            file_name = f"{uuid.uuid4()}.{image.format.lower()}"
            
            # Upload to Minio
            self.client.put_object(
                self.settings.minio_bucket,
                file_name,
                io.BytesIO(img_byte_arr),
                len(img_byte_arr),
                content_type
            )
            
            # Return the URL
            return f"http://{self.settings.minio_url}/{self.settings.minio_bucket}/{file_name}"

        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")
