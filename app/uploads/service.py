import boto3

from app.core.config import AWS_BUCKET_NAME

s3 = boto3.client("s3")


async def upload_to_s3(file):

    s3.upload_fileobj(
        file.file,
        AWS_BUCKET_NAME,
        file.filename,
    )

    return f"https://{AWS_BUCKET_NAME}.s3.amazonaws.com/{file.filename}"