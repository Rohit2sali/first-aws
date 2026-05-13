from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ChatModel:
    def __init__(self, model_path: str):
        print(f"Loading model from {model_path}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float32, # CPU-friendly
            device_map="cpu"
        )

    def generate_response(self, message: str):
        # Formatting for TinyLlama Chat template
        prompt = f"<|system|>\nYou are a helpful assistant.</s>\n<|user|>\n{message}</s>\n<|assistant|>\n"
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cpu")
        outputs = self.model.generate(
            **inputs, 
            max_new_tokens=150, 
            do_sample=True, 
            temperature=0.7, 
            top_k=50
        )
        
        full_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Extract only the assistant's part
        return full_text.split("<|assistant|>")[-1].strip()

# Initialize as a singleton to avoid reloading on every request
# Path should match where s3_utils.py saves the weights
llm = ChatModel("./models/tinyllama-weights")