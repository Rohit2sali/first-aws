from app.inference.service import generate_response


def process_chat(prompt: str):
    response = generate_response(prompt)
    # response = "Test response"
    return response
