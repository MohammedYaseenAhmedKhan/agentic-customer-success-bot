"""
Knowledge Retrieval Agent
Uses RAG to answer product-related questions.
"""

from rag.retriever import Retriever


class KnowledgeAgent:
    def __init__(self, documents: list[str]):
        self.retriever = Retriever(documents)

    def handle(self, query: str) -> dict:
        relevant_docs = self.retriever.retrieve(query)

        # LLM placeholder (next step we plug real LLM)
        answer = "Based on the documentation: " + " ".join(relevant_docs)

        return {
            "agent": "Knowledge Retrieval Agent",
            "query": query,
            "answer": answer,
            "sources": relevant_docs
        }
