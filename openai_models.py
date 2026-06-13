from openai import OpenAI

client = OpenAI()
try:
    models_page = client.models.list()
    print(f"{'Model ID':<40} | {'Owned By'}")
    print("-" * 60)
    for model in models_page.data:
        print(f"{model.id:<40} | {model.owned_by}")
except Exception as e:
    print(f"An error occurred: {e}")