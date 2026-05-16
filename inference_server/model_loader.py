import os

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM
)


from shared.s3_utils import download_model

download_model()
print("Loading model...")

MODEL_PATH = "/code/models/tinyllama-weights"


print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

print("Model loaded successfully")
