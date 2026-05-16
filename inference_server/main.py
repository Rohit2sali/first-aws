from fastapi import FastAPI
from pydantic import BaseModel

from model_loader import tokenizer, model

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.post("/generate")
def generate(data: PromptRequest):
    print("Starting inference app...")

    inputs = tokenizer(
        data.prompt,
        return_tensors="pt"
    )

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=10
        )

    response = tokenizer.decode(
        output[0],
        skip_special_tokens=True
    )

    return {
        "response": response
    }
