import time


def log_inference(prompt, response, start_time):

    latency = time.time() - start_time

    print("==== Inference Log ====")
    print(f"Prompt: {prompt}")
    print(f"Latency: {latency}")
    print(f"Response length: {len(response)}")