from app.inference.model_loader import tokenizer, model


def generate_response(prompt: str):

    inputs = tokenizer(prompt, return_tensors="pt")

    output = model.generate(
        **inputs,
        max_new_tokens=50,
    )

    response = tokenizer.decode(
        output[0],
        skip_special_tokens=True,
    )

    return response