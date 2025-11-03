from openai import OpenAI
import json
from config import GEMINI_API_KEY

client = OpenAI(
    api_key= GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Goku.
    You are acting on behalf of Goku who is 25 years old Tech enthusiatic and 
    principle engineer. Your main tech stack is JS and Python and You are leaning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, Whats up!

    (100 - 150 examples)
"""

response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role":"user", "content": "who are you?" }
        ]
    )


print("Response:", response.choices[0].message.content)