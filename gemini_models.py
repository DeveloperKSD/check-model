import os
from google import genai

client = genai.Client()

print("--- 1. Querying Your Configured Model ---")
target_model = "gemini-2.5-flash"
try:
    model_info = client.models.get(model=target_model)
    print(f"Target Model ID: {model_info.name}")
    print(f"Display Name:    {model_info.display_name}")
    print(f"Input Token Limit:  {model_info.input_token_limit}")
    print(f"Output Token Limit: {model_info.output_token_limit}")
except Exception as e:
    print(f"Error fetching model '{target_model}': {e}")

print("\n--- 2. Listing All Available Gemini Models ---")
try:
    available_models = client.models.list()
    for model in available_models:
        if "generateContent" in model.supported_generation_methods:
            print(f"{model.name:<35} | {model.display_name}")
except Exception as e:
    print(f"Error listing models: {e}")