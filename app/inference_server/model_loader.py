import os

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM
)

ENV = os.getenv("ENV", "local")

if ENV == "local":

    MODEL_PATH = r"C:\machine learning\models\tinyllama-weights"

else:

    from shared.s3_utils import download_model

    download_model()

    MODEL_PATH = "/code/models/tinyllama-weights"


print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

print("Model loaded successfully")
print("Model loaded successfully")
