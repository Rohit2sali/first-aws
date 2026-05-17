import requests

# INFERENCE_URL = "http://localhost:9000/generate"
INFERENCE_URL = "http://inference-server:9000/generate"

def process_chat(prompt: str):

    response = requests.post(
        INFERENCE_URL,
        json={
            "prompt": prompt
        },
        timeout=120
    )

    print(response.status_code)
    print(response.text)

    data = response.json()

    return data["response"]
