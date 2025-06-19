# ai_chatbot.py
import os
from dotenv import load_dotenv
from openai import OpenAI  # New SDK

# Load your .env file
load_dotenv()

# Get the OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")

# Set up OpenAI client to use OpenRouter
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# ✅ Use this model for best free results
MODEL = "mistralai/mistral-7b-instruct"

def ask_chatbot(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful and friendly AI chatbot."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content







# Command-line loop
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! 💛")
            break
        response = ask_chatbot(user_input)
        print("Chatbot:", response)
