# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch

# class ChatModel:
#     def __init__(self, model_path: str):
#         print(f"Loading model from {model_path}...")
#         self.tokenizer = AutoTokenizer.from_pretrained(model_path)
#         self.model = AutoModelForCausalLM.from_pretrained(
#             model_path,
#             torch_dtype=torch.float32, # CPU-friendly
#             device_map="cpu"
#         )

#     def generate_response(self, message: str):
#         # Formatting for TinyLlama Chat template
#         prompt = f"<|system|>\nYou are a helpful assistant.</s>\n<|user|>\n{message}</s>\n<|assistant|>\n"
        
#         inputs = self.tokenizer(prompt, return_tensors="pt").to("cpu")
#         outputs = self.model.generate(
#             **inputs, 
#             max_new_tokens=150, 
#             do_sample=True, 
#             temperature=0.7, 
#             top_k=50
#         )
        
#         full_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
#         # Extract only the assistant's part
#         return full_text.split("<|assistant|>")[-1].strip()

# # Initialize as a singleton to avoid reloading on every request
# # Path should match where s3_utils.py saves the weights
# llm = ChatModel("./models/tinyllama-weights")


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

            print("Downloading model from S3...")
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