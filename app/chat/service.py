import requests

# INFERENCE_URL = "http://localhost:9000/generate"
INFERENCE_URL = "http://inference-server:9000/generate"

def process_chat(prompt: str):

    response = requests.post(
        INFERENCE_URL,
        json={
            "prompt": prompt
        }
    )

    data = response.json()

    return data["response"]
