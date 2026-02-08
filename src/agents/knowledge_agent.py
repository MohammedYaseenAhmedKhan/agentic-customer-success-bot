"""
Knowledge Retrieval Agent

Responsibilities:
- Perform semantic retrieval over enterprise documents
- Optionally invoke LLM for answer synthesis
- Always return source citations
- Gracefully degrade when LLM is unavailable
"""
from src.rag.retriever import Retriever
from src.llm.gemini_client import generate_answer


class KnowledgeAgent:
    def __init__(self, documents: list[dict]):
        self.retriever = Retriever(documents)

    def handle(self, query: str) -> dict:
        retrieved_chunks = self.retriever.retrieve(query)
        context = [chunk["content"] for chunk in retrieved_chunks]

        try:
            answer = generate_answer(query, context)
        except Exception:
            answer = (
                "LLM is temporarily unavailable.\n\n"
                "Relevant information found:\n"
                + " ".join(context)
            )

        sources = [
            f"{chunk['source']} (Page {chunk['page']})"
            for chunk in retrieved_chunks
        ]

        return {
            "agent": "Knowledge Retrieval Agent",
            "query": query,
            "answer": answer,
            "sources": list(set(sources))
        }
