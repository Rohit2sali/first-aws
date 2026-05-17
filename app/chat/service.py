import requests

# INFERENCE_URL = "http://localhost:9000/generate"
INFERENCE_URL = "http://inference-server:9000/generate"

def process_chat(prompt: str):
    data = {
        "prompt": prompt
    }
    for attempt in range(5):
        try:
            response = requests.post(
                INFERENCE_URL,
                json=data,
                timeout=120
            )

            print(response.status_code)
            print(response.text)
        
            data = response.json()
        
            return data["response"]

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")

            # last attempt
            if attempt == 4:
                raise Exception("Inference server unavailable after retries")

            time.sleep(3)
