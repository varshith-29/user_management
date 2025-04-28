from functools import lru_cache
from app.services.minio_service import MinioService

@lru_cache()
def get_minio_service() -> MinioService:
    return MinioService()
