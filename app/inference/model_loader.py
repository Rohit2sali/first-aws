import os

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM
)

from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV")

MODEL_PATH = os.getenv("MODEL_PATH")

tokenizer = None
model = None


def load_model():

    global tokenizer
    global model

    if tokenizer is None or model is None:

        if ENV == "production":

            from app.aws.s3_utils import download_model

            download_model()

        print(f"Loading model from {MODEL_PATH}")

        tokenizer = AutoTokenizer.from_pretrained(
            MODEL_PATH,
            local_files_only=True
        )

        model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH,
            local_files_only=True
        )

        print("Model loaded successfully")

    return tokenizer, model

# import os

# from transformers import (
#     AutoTokenizer,
#     AutoModelForCausalLM
# )

# from dotenv import load_dotenv

# load_dotenv()

# ENV = os.getenv("ENV")

# MODEL_PATH = os.getenv("MODEL_PATH")

# tokenizer = None
# model = None


# def load_model():

#     global tokenizer
#     global model

#     if tokenizer is None or model is None:

#         if ENV == "production":

#             from app.aws.s3_utils import download_model

#             print("Downloading model from S3...")
#             download_model()

#         print(f"Loading model from {MODEL_PATH}")

#         tokenizer = AutoTokenizer.from_pretrained(
#             MODEL_PATH,
#             local_files_only=True
#         )

#         model = AutoModelForCausalLM.from_pretrained(
#             MODEL_PATH,
#             local_files_only=True
#         )

#         print("Model loaded successfully")

#     return tokenizer, model
