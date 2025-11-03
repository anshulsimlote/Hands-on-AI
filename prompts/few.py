from openai import OpenAI
from config import GEMINI_API_KEY

client = OpenAI(
    api_key= GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
SYSTEM_PROMPT = (
    "Your name is Alexa. Only answer coding-related questions. "
    "If the user asks about anything else, including math problems, reply with 'Sorry.' "
    "Example"
    "Q: User: 'How do I reverse a string in Python?' → Alexa explains the Python code. "
    "Q: User: 'What's your favorite color?' → Alexa: 'Sorry.' "
    "Q: example: User: 'What is 12 * 8?' → Alexa: 'Sorry.'"
)


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
         {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "2+2"
        }
    ]
)

print(response.choices[0].message)
print(response.choices[0].message.content)