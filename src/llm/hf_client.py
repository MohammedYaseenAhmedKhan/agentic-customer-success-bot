"""
Hugging Face LLM client (Free tier)
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}


def generate_answer(query: str, context: list[str]) -> str:
    prompt = f"""
Answer the question using the context below.

Context:
{" ".join(context)}

Question:
{query}

Answer:
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.2
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 503:
        return "Model is loading. Please try again in a few seconds."

    response.raise_for_status()
    result = response.json()

    if isinstance(result, list):
        return result[0]["generated_text"]

    return result["generated_text"]
