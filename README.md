# Multi-LLM API Model Discovery Scripts

A collection of lightweight Python utility scripts designed to programmatically inspect, query, and discover active models across major LLM provider platforms. 

Because LLM APIs are stateless, developers must explicitly pass target strings (e.g., `gemini-2.5-flash`, `gpt-4o`) to execute generations. These scripts eliminate guesswork by querying the foundational infrastructure endpoints of **Google Gemini**, **OpenAI**, **Groq**, and **Anthropic (Claude)** to report exactly which model architectures are live, deprecated, or authorized under your respective API credentials.

---

## 📂 Repository Architecture

```text
├── gemini_models.py      # Inspects Gemini metadata and lists active Google GenAI models
├── openai_models.py      # Fetches all accessible models and developer ownership via OpenAI API
├── groq_models.py        # Lists ultra-fast open-weights instances hosted on Groq hardware
├── anthropic_models.py   # Uses Anthropic's endpoints to scan available Claude profiles
└── README.md             # Repository documentation and startup guide
