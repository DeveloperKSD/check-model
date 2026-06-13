from groq import Groq

client = Groq()
try:
    models_list = client.models.list()
    print(f"{'Model ID':<35} | {'Active Status'}")
    print("-" * 50)
    for model in models_list.data:
        print(f"{model.id:<35} | Active: {getattr(model, 'active', 'N/A')}")
except Exception as e:
    print(f"An error occurred: {e}")