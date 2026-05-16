import boto3
import os

s3 = boto3.client("s3")

AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

MODEL_PREFIX = "tinyllama-weights/"
MODEL_DIR = "/code/models/tinyllama-weights"


def download_model():

    os.makedirs(MODEL_DIR, exist_ok=True)

    response = s3.list_objects_v2(
        Bucket=AWS_BUCKET_NAME,
        Prefix=MODEL_PREFIX,
    )

    for obj in response.get("Contents", []):

        key = obj["Key"]

        if key.endswith("/"):
            continue

        filename = key.split("/")[-1]

        local_path = os.path.join(MODEL_DIR, filename)

        print(f"Downloading {key} -> {local_path}")

        s3.download_file(
            AWS_BUCKET_NAME,
            key,
            local_path,
        )

    print("Model downloaded")

