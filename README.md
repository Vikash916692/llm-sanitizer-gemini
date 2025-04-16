# 🛡️ LLM Input/Output Sanitizer with Gemini
This Python-based chatbot uses Google's Gemini Pro API and sanitizes both user inputs and model outputs to prevent prompt injection and sensitive data leaks.

## 📦 Features
- ✅ Input filtering (removes injection attempts)
- ✅ Output filtering (removes hallucinated sensitive data)
- ✅ Command-line interface (CLI)
- ✅ Gemini Pro integration

## 🚀 Getting Started

### 1. Clone the repo
   
```
git clone https://github.com/Vikash916692/llm-sanitizer-gemini.git
cd llm-sanitizer-gemini
```
### 2. Set up the environment
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add your API key
Create a .env file in the root with:
```
GOOGLE_API_KEY=your-api-key
```

### 5. Run the chatbot
```
python run.py
```
