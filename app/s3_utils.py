import boto3
import os

def download_model_from_s3(bucket_name, model_key, local_path):
    if not os.path.exists(local_path):
        print(f"🚀 Downloading model from S3: {model_key}...")
        s3 = boto3.client('s3')
        s3.download_file(bucket_name, model_key, local_path)
        print("✅ Download complete.")
    else:
        print("📦 Model already exists locally.")