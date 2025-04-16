import os
import google.generativeai as genai
from dotenv import load_dotenv
from app.sanitizer import sanitize_input, sanitize_output

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(prompt):
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
    response = model.generate_content(prompt)
    return response.text

def run_chat():
    print("Sanitized Gemini Chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        clean_input = sanitize_input(user_input)
        raw_output = get_gemini_response(clean_input)
        clean_output = sanitize_output(raw_output)

        print(f"\nGemini (Sanitized): {clean_output}\n")
