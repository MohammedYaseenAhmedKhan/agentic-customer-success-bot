"""
Knowledge Retrieval Agent
Uses RAG + LLM to answer product-related questions.
"""

from rag.retriever import Retriever
from llm.gemini_client import generate_answer


class KnowledgeAgent:
    def __init__(self, documents: list[str]):
        self.retriever = Retriever(documents)

    def handle(self, query: str) -> dict:
        relevant_docs = self.retriever.retrieve(query)
        answer = generate_answer(query, relevant_docs)

        return {
            "agent": "Knowledge Retrieval Agent",
            "query": query,
            "answer": answer,
            "sources": relevant_docs
        }
