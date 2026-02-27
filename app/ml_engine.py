import torch
from transformers import pipeline

class LLMEngine:

    def __init__(self):
        self.pipe=None

    def load_model(self):
        """Loads the model into memory"""
        print("⏳ Loading TinyLlama... (This might take a minute)")

        model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

        self.pipe = pipeline(
            "text-generation",
            model = model_id,
            torch_dtype = torch.bfloat16, # it saves memory
            device_map="auto" # Automaticaly chooses between GPU and CPU
        )

        print("✅ TinyLlama loaded successfully!")

#Creating chat like format
    def generate(self,prompt: str, max_new_tokens: int = 256):
        
        """Generates text based on the prompt."""
        if not self.pipe:
            raise RuntimeError("Model is not loaded!")
        
        messages = [
            {"role": "system", "content" : "You are an helpful AI Assistant that can answer questions and help with tasks."},
            {"role": "user", "content" : prompt},
        ]

# Apply the Chat template

        prompt_formatted = self.pipe.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        outputs = self.pipe(
            prompt_formatted,
            max_new_tokens = max_new_tokens,
            do_sample = True,
            temperature=0.7,
            top_k=50,
            top_p=0.95
        )

        generated_text = outputs[0]["generated_text"]
# Removes the prompt from the response to be cleaner
        return generated_text[len(prompt_formatted):]

# creating a global instance
llm_engine = LLMEngine()