"""
Retriever for Knowledge Retrieval Agent
"""

from rag.embedder import embed_text
from rag.vector_store import VectorStore


class Retriever:
    def __init__(self, documents: list[str]):
        self.store = VectorStore(embedding_dim=384)

        for doc in documents:
            embedding = embed_text(doc)
            self.store.add(embedding, doc)

    def retrieve(self, query: str):
        query_embedding = embed_text(query)
        return self.store.search(query_embedding)
