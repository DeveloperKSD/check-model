from anthropic import Anthropic

client = Anthropic()
try:
    models_page = client.beta.models.list()
    print(f"{'Model ID':<30} | {'Display Name':<30} | {'Max Input Tokens'}")
    print("-" * 80)
    for model in models_page.data:
        print(f"{model.id:<30} | {model.display_name:<30} | {model.max_input_tokens}")
except Exception as e:
    print(f"An error occurred: {e}")