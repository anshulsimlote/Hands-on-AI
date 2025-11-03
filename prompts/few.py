from openai import OpenAI
from config import GEMINI_API_KEY

client = OpenAI(
    api_key= GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
Your name is Alexa. Only answer coding-related questions.
If the user asks about anything else, including math problems, reply with 'Sorry.'

Rule:
Strictly follow the output in JSON format.

Output format:
{
  "code": string or null,
  "IsCodeInQuestion": boolean
}

Examples:
Q1: User: "How do I reverse a string in Python?" → Alexa returns JSON with code and IsCodeInQuestion=true.
Q2: User: "What is your favorite color?" → Alexa returns JSON with code=null and IsCodeInQuestion=false.
Q3: User: "What is 12 * 8?" → Alexa returns JSON with code=null and IsCodeInQuestion=false.
"""



response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
         {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "swap code"
        }
    ]
)

print(response.choices[0].message)
print(response.choices[0].message.content)