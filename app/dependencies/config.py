from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings"""
    # Database settings
    database_url: str = "postgresql+asyncpg://user:password@postgres:5432/myappdb"
    debug: bool = False
    send_real_mail: bool = False
    max_login_attempts: int = 3

    # JWT Settings
    jwt_secret_key: str = "your-secret-key"
    jwt_algorithm: str = "HS256"
    jwt_token_expire_minutes: int = 30

    # Minio Settings
    minio_root_user: str = "minioadmin"
    minio_root_password: str = "minioadmin"
    minio_url: str = "minio:9000"  # Using Docker service name
    minio_bucket: str = "profile-pictures"
    minio_secure: bool = False

    # SMTP Settings
    smtp_server: str = "sandbox.smtp.mailtrap.io"
    smtp_port: int = 2525
    smtp_username: str = ""
    smtp_password: str = ""
    server_base_url: str = "http://localhost:8000/"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
