# 🔍 Multi-LLM Model Discovery Toolkit

> Instantly inspect, enumerate, and verify available models across major LLM providers using your own API credentials.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-Supported-green)
![Gemini](https://img.shields.io/badge/Google%20Gemini-Supported-orange)
![Groq](https://img.shields.io/badge/Groq-Supported-red)
![Anthropic](https://img.shields.io/badge/Claude-Supported-purple)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---

## ✨ Why This Exists

Every LLM provider exposes dozens of model identifiers, aliases, previews, legacy versions, and organization-specific deployments.

When building applications, you must know the **exact model string** accepted by the API:

```python
model="gpt-4o"
model="gemini-2.5-flash"
model="claude-sonnet-4"
```

Unfortunately, documentation can lag behind production deployments.

This toolkit directly queries provider infrastructure to discover:

* ✅ Available models
* ✅ Deprecated models
* ✅ Account-authorized models
* ✅ Ownership metadata
* ✅ Context windows (where available)
* ✅ Provider-specific capabilities

---

# 🌐 Supported Providers

| Provider         | Discovery Method | Status |
| ---------------- | ---------------- | ------ |
| Google Gemini    | Google GenAI SDK | ✅      |
| OpenAI           | Models API       | ✅      |
| Groq             | Models Endpoint  | ✅      |
| Anthropic Claude | Models Endpoint  | ✅      |

---

# 📂 Project Structure

```text
.
├── gemini_models.py
├── openai_models.py
├── groq_models.py
├── anthropic_models.py
└── README.md
```

### File Overview

| File                  | Description                         |
| --------------------- | ----------------------------------- |
| `gemini_models.py`    | Enumerates available Gemini models  |
| `openai_models.py`    | Lists all OpenAI-accessible models  |
| `groq_models.py`      | Discovers active Groq-hosted models |
| `anthropic_models.py` | Retrieves available Claude models   |
| `README.md`           | Documentation                       |

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-llm-model-discovery.git

cd multi-llm-model-discovery
```

## Install Dependencies

```bash
pip install google-genai openai groq anthropic
```

Or:

```bash
pip install -r requirements.txt
```

---

# 🔑 Authentication

The scripts automatically read API credentials from environment variables.

## Linux / macOS

```bash
export GEMINI_API_KEY="YOUR_KEY"
export OPENAI_API_KEY="YOUR_KEY"
export GROQ_API_KEY="YOUR_KEY"
export ANTHROPIC_API_KEY="YOUR_KEY"
```

## Windows PowerShell

```powershell
$env:GEMINI_API_KEY="YOUR_KEY"
$env:OPENAI_API_KEY="YOUR_KEY"
$env:GROQ_API_KEY="YOUR_KEY"
$env:ANTHROPIC_API_KEY="YOUR_KEY"
```

---

# 🚀 Usage

---

## 🧬 Google Gemini

Discover active Gemini deployments and inspect model metadata.

```bash
python gemini_models.py
```

### Example Output

```text
gemini-2.5-flash
gemini-2.5-pro
gemini-2.5-flash-lite
...
```

---

## 🧠 OpenAI

Retrieve every model accessible to your account or organization.

```bash
python openai_models.py
```

### Example Output

```text
gpt-5
gpt-5-mini
gpt-5-nano
gpt-4o
text-embedding-3-large
...
```

---

## ⚡ Groq

Enumerate high-speed open-weight models deployed on Groq LPUs.

```bash
python groq_models.py
```

### Example Output

```text
llama-4-scout
llama-4-maverick
mixtral-8x7b
gemma2-9b-it
...
```

---

## 🦅 Anthropic Claude

List active Claude models and associated metadata.

```bash
python anthropic_models.py
```

### Example Output

```text
claude-opus-4
claude-sonnet-4
claude-haiku-4
...
```

---

# 📊 Use Cases

### API Exploration

Verify which models are available before deployment.

### CI/CD Validation

Ensure model identifiers remain valid after provider updates.

### Cost Optimization

Compare available models before selecting inference targets.

### Multi-Provider Applications

Automatically discover supported models across vendors.

### Research & Benchmarking

Build model comparison pipelines without manually maintaining lists.

---

# Example Workflow

```bash
python openai_models.py

python gemini_models.py

python groq_models.py

python anthropic_models.py
```

Use the resulting identifiers directly:

```python
response = client.responses.create(
    model="gpt-5",
    input="Hello world"
)
```

---

# 🛡️ Notes

* No scraping is performed.
* Uses only official SDKs.
* Requires valid API credentials.
* Results depend on your account permissions and provider availability.
* Returned model lists may change without notice as vendors add or retire deployments.

---

# 🤝 Contributing

Pull requests, bug reports, and provider expansions are welcome.

Potential future additions:

* Azure OpenAI
* AWS Bedrock
* Cohere
* Mistral
* DeepSeek
* Together AI
* OpenRouter

---

# 📜 License

MIT License

Feel free to use, modify, and distribute.
