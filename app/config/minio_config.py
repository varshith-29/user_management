from pydantic_settings import BaseSettings

class MinioSettings(BaseSettings):
    MINIO_ROOT_USER: str = "minioadmin"
    MINIO_ROOT_PASSWORD: str = "minioadmin"
    MINIO_URL: str = "localhost:9000"
    MINIO_BUCKET: str = "profile-pictures"
    MINIO_SECURE: bool = False
    
    class Config:
        env_file = ".env"
