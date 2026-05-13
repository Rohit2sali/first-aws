#!/bin/bash
# Sync weights from S3 (If on AWS) or just start (If local)
# python3 -c "from app.s3_utils import download_model_from_s3; ..."

# Start the FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 80