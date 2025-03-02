import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))



model_name = 'gemini-1.5-pro-latest' # or whatever model name is shown from the list_models() method.

model = genai.GenerativeModel(model_name)

def get_coding_help(user_input):
    prompt = f"""
    You are a coding tutor. Help the user with their coding questions.
    User: {user_input}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

def coding_chatbot():
    print("Welcome to the Coding Tutor Chatbot! Type 'exit' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = get_coding_help(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    coding_chatbot()