import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import os
import shutil
import folder_paths
import random
import numpy as np

class SmolLM2Node:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_id = "gokaygokay/SmolLM2-Prompt-Enhance"
        self.tokenizer_id = "HuggingFaceTB/SmolLM2-135M-Instruct"
        self.model = None
        self.tokenizer = None
        
        # Setup model directory in ComfyUI
        self.model_dir = os.path.join(folder_paths.models_dir, "smollm2")
        self.ensure_model_directory()
    
    def ensure_model_directory(self):
        """Create model directory if it doesn't exist and add to folder_paths"""
        if not os.path.exists(self.model_dir):
            os.makedirs(self.model_dir, exist_ok=True)
        
        # Register the model directory with ComfyUI
        if not hasattr(folder_paths, "smollm2_model_path"):
            folder_paths.add_model_folder_path("smollm2", self.model_dir)
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 2**32 - 1}),  # Fixed seed range
                "random_seed": ("BOOLEAN", {"default": False}),
                "max_new_tokens": ("INT", {"default": 256, "min": 1, "max": 1024}),
                "repetition_penalty": ("FLOAT", {"default": 1.2, "min": 0.1, "max": 10.0}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.1, "max": 2.0}),
                "top_p": ("FLOAT", {"default": 0.9, "min": 0.0, "max": 1.0}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"
    CATEGORY = "marduk191/SmolLM2-Prompt-Enhance"

    def load_models(self):
        if self.model is None:
            print("Loading SmolLM2 models...")
            
            # Set Transformers cache directory to ComfyUI models directory
            os.environ['TRANSFORMERS_CACHE'] = self.model_dir
            
            try:
                self.tokenizer = AutoTokenizer.from_pretrained(
                    self.tokenizer_id,
                    cache_dir=self.model_dir,
                    local_files_only=False
                )
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_id,
                    cache_dir=self.model_dir,
                    local_files_only=False
                ).to(self.device)
                
                print("SmolLM2 models loaded successfully!")
            except Exception as e:
                print(f"Error loading models: {str(e)}")
                raise e

    def generate(self, prompt, seed, random_seed, max_new_tokens, repetition_penalty, temperature, top_p):
        self.load_models()
        
        # Handle random seed
        if random_seed:
            seed = random.randint(0, 2**32 - 1)  # Fixed random seed range
        
        # Set random states
        seed = int(seed)  # Ensure seed is an integer
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
        
        messages = [{"role": "user", "content": prompt}]
        input_text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        
        inputs = self.tokenizer.encode(input_text, return_tensors="pt").to(self.device)
        
        outputs = self.model.generate(
            inputs,
            max_new_tokens=max_new_tokens,
            repetition_penalty=float(repetition_penalty),
            do_sample=True,
            temperature=float(temperature),
            top_p=float(top_p)
        )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Extract just the assistant's response
        response = response.split("assistant\n")[-1].strip()
        
        return (response,)

# Node registration
NODE_CLASS_MAPPINGS = {
    "SmolLM2 Text Generator": SmolLM2Node
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SmolLM2 Text Generator": "SmolLM2 Text Generator"
}
