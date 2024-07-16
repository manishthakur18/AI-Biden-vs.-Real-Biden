import openai
from src.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Choose the appropriate model version if available
        messages=[
            {"role": "system", "content": "You are President Biden."},
            {"role": "user", "content": question},
        ],
        max_tokens=150  # Adjust max tokens as per your requirement
    )
    return response.choices[0].message["content"].strip()
