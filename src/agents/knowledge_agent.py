"""
Knowledge Retrieval Agent

Handles product / documentation related queries using
RAG (Retriever + LLM with safe fallback).
"""

from rag.retriever import Retriever
from llm.gemini_client import generate_answer


class KnowledgeAgent:
    def __init__(self, documents: list[str]):
        self.retriever = Retriever(documents)

    def handle(self, query: str) -> dict:
        # Step 1: Retrieve relevant documents
        relevant_docs = self.retriever.retrieve(query)

        # Step 2: Try LLM-based answer generation
        try:
            answer = generate_answer(query, relevant_docs)
        except Exception:
            # Safe fallback when LLM is unavailable
            answer = (
                "LLM generation is temporarily unavailable.\n\n"
                "Relevant information found:\n"
                + " ".join(relevant_docs)
            )

        # Step 3: Return structured response
        return {
            "agent": "Knowledge Retrieval Agent",
            "query": query,
            "answer": answer,
            "sources": relevant_docs
        }
