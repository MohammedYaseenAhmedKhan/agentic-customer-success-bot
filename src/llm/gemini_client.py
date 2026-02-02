"""
Gemini LLM client using the NEW google-genai SDK
"""

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_answer(query: str, context: list[str]) -> str:
    prompt = f"""
You are an enterprise customer support assistant.
Answer the question using ONLY the information provided in the context.
If the answer is not present, say you do not have enough information.

Context:
{chr(10).join(context)}

Question:
{query}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-1.5-pro-latest",
        contents=prompt
    )

    return response.text.strip()

