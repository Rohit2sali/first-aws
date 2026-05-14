from fastapi import APIRouter, UploadFile, File

from app.uploads.service import upload_to_s3

router = APIRouter(prefix="/upload", tags=["Uploads"])


@router.post("/")
async def upload(file: UploadFile = File(...)):

    url = await upload_to_s3(file)

    return {
        "url": url,
    }