"""
Gemini LLM client (Day 5)
Primary model: Gemini Flash 2.5
"""

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Safe model list (keep for future fallback)
PRIMARY_MODEL = "gemini-2.5-flash"
FALLBACK_MODELS = [
    "gemini-1.5-flash-latest",
    "gemini-1.5-pro-latest"
]


def generate_answer(query: str, context: list[str]) -> str:
    prompt = f"""
You are an enterprise customer support assistant.
Answer the question using ONLY the context provided.
If the answer is not present, say you do not have enough information.

Context:
{chr(10).join(context)}

Question:
{query}

Answer:
"""

    # Try primary model first
    try:
        response = client.models.generate_content(
            model=PRIMARY_MODEL,
            contents=prompt
        )
        return response.text.strip()
    except Exception:
        pass

    # Try fallbacks
    for model in FALLBACK_MODELS:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )
            return response.text.strip()
        except Exception:
            continue

    # Final safety
    raise RuntimeError("All Gemini models failed")
