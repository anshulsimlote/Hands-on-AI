from openai import OpenAI
from config import GEMINI_API_KEY

client = OpenAI(
    api_key= GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = "You should only answer coding-related questions. Do not answer anything else. Your name is Alexa. If the user asks something other than coding, just say 'Sorry.'"


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
         {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Python code to translate english to Hindi"
        }
    ]
)

print(response.choices[0].message)
print(response.choices[0].message.content)