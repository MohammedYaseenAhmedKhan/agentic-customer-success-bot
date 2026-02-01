"""
FAISS vector store for document embeddings
"""

import faiss
import numpy as np


class VectorStore:
    def __init__(self, embedding_dim: int):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.documents = []

    def add(self, embedding, document: str):
        self.index.add(np.array([embedding]).astype("float32"))
        self.documents.append(document)

    def search(self, query_embedding, top_k=3):
        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"), top_k
        )
        return [self.documents[i] for i in indices[0]]

