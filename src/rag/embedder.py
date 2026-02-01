"""
Embedding utility for Knowledge Retrieval Agent
"""

from sentence_transformers import SentenceTransformer

# lightweight model (fast + interview-safe)
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(text: str):
    return model.encode(text)
