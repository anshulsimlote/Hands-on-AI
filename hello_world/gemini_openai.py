from openai import OpenAI
from config import GEMINI_API_KEY

client = OpenAI(
    api_key= GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": "Explain to me how AI works in few words"
        }
    ]
)

print(response.choices[0].message)
print(response.choices[0].message.content)