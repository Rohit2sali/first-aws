from app.inference.model_loader import load_model


def generate_response(prompt: str):

    tokenizer, model = load_model()

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

    output = model.generate(
        **inputs,
        max_new_tokens=50,
    )

    response = tokenizer.decode(
        output[0],
        skip_special_tokens=True,
    )

    return response
