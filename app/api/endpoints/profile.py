from fastapi import APIRouter, Depends, UploadFile, HTTPException
from app.services.minio_service import MinioService
from app.models.user_model import User
from app.dependencies.auth import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies.db import get_db

router = APIRouter()
minio_service = MinioService()

@router.post("/profile/picture")
async def upload_profile_picture(
    file: UploadFile,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    # Read file content
    file_content = await file.read()
    
    # Upload to Minio
    profile_url = minio_service.upload_profile_picture(
        file_content,
        file.content_type
    )
    
    # Update user profile
    current_user.profile_picture_url = profile_url
    await db.commit()
    
    return {"profile_picture_url": profile_url}
