#Multi-LLM API Model Discovery Scripts

A collection of lightweight Python utility scripts designed to programmatically inspect, query, and discover active models across major LLM provider platforms.

Because LLM APIs are stateless, developers must explicitly pass target strings (e.g., `gemini-2.5-flash`, `gpt-4o`) to execute generations. These scripts eliminate guesswork by querying the foundational infrastructure endpoints of **Google Gemini**, **OpenAI**, **Groq**, and **Anthropic (Claude)** to report exactly which model architectures are live, deprecated, or authorized under your respective API credentials.

---

## 📂 Repository Architecture

```````````text
├── gemini_models.py      # Inspects Gemini metadata and lists active Google GenAI models
├── openai_models.py      # Fetches all accessible models and developer ownership via OpenAI API
├── groq_models.py        # Lists ultra-fast open-weights instances hosted on Groq hardware
├── anthropic_models.py   # Uses Anthropic's endpoints to scan available Claude profiles
└── README.md             # Repository documentation and startup guide
```

---

## 🛠️ Installation & Setup

Ensure you have **Python 3.10+** installed. Follow the steps below to initialize your environment.

### 1. Clone the Repository

``````````bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Install Official SDK Dependencies

Install the required platform libraries using pip:

`````````bash
pip install google-genai openai groq anthropic
```

### 3. Configure API Environment Credentials

The scripts are optimized to automatically detect auth tokens directly from your system environment variables. Export the keys relevant to the services you intend to query:

**macOS / Linux Terminal:**

````````bash
export GEMINI_API_KEY="your_gemini_api_key_here"
export OPENAI_API_KEY="your_openai_api_key_here"
export GROQ_API_KEY="your_groq_api_key_here"
export ANTHROPIC_API_KEY="your_anthropic_api_key_here"
```

**Windows PowerShell:**

```````powershell
$env:GEMINI_API_KEY="your_gemini_api_key_here"
$env:OPENAI_API_KEY="your_openai_api_key_here"
$env:GROQ_API_KEY="your_groq_api_key_here"
$env:ANTHROPIC_API_KEY="your_anthropic_api_key_here"
```

---

## 🚀 Execution & Script Breakdown

### 🧬 Google Gemini Discovery (`gemini_models.py`)

Utilizes the updated standard `google-genai` SDK to run an explicit configuration check against a specific target baseline (`gemini-2.5-flash`) to parse structural limits before printing the full valid key roster.

```bash
python gemini_models.py
```

### 🧠 OpenAI Discovery (`openai_models.py`)

Queries OpenAI infrastructure to output every generation engine, baseline system model, and embedding mechanism currently accessible by your subscription level or organization tier.

`````bash
python openai_models.py
` ` `

### ⚡ Groq Discovery (`groq_models.py`)

Polls Groq's API client to return the exact open-weights matrices (e.g., Llama, Mixtral, Gemma) running live on LPU inference hardware along with their deployment health flags.

````bash
python groq_models.py
` ` `

### 🦅 Anthropic Claude Discovery (`anthropic_models.py`)

Exposes Anthropic's model management system to list active Claude variations alongside exact window dimensions and maximum input tokens.

```bash
python anthropic_models.py
` ` `
```

---

> **Note:** The ` ` ` in the code blocks above are shown with spaces to avoid rendering issues here. Replace each ` ` ` with ` ``` ` (no spaces) when you paste into your actual `README.md` file.
