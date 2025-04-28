import pytest
from httpx import AsyncClient
from io import BytesIO
from PIL import Image
import asyncio

@pytest.mark.asyncio
async def test_upload_profile_picture(async_client: AsyncClient, authenticated_user):
    # Create a test image
    img = Image.new('RGB', (100, 100), color = 'red')
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    response = await async_client.post(
        "/api/profile/picture",
        files={"file": ("test.png", img_byte_arr, "image/png")},
        headers={"Authorization": f"Bearer {authenticated_user['access_token']}"}
    )

    assert response.status_code == 200
    assert "profile_picture_url" in response.json()
    assert response.json()["profile_picture_url"].startswith("http://")

@pytest.mark.asyncio
async def test_upload_invalid_file_type(async_client: AsyncClient, authenticated_user):
    response = await async_client.post(
        "/api/profile/picture",
        files={"file": ("test.txt", b"test content", "text/plain")},
        headers={"Authorization": f"Bearer {authenticated_user['access_token']}"}
    )

    assert response.status_code == 400
