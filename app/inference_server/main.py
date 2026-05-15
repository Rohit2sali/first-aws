from fastapi import FastAPI
from pydantic import BaseModel

from model_loader import tokenizer, model

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.post("/generate")
def generate(data: PromptRequest):

    inputs = tokenizer(
        data.prompt,
        return_tensors="pt"
    )

    output = model.generate(
        **inputs,
        max_new_tokens=50
    )

    response = tokenizer.decode(
        output[0],
        skip_special_tokens=True
    )

    return {
        "response": response
    }
