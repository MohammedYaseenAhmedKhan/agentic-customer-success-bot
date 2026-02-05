import faiss
from rag.embedder import embed_texts
from rag.faiss_store import save_index, load_index


class Retriever:
    def __init__(self, documents: list[dict]):
        self.k = 3

        index, stored_docs = load_index()

        if index is not None:
            self.index = index
            self.documents = stored_docs
        else:
            self.documents = documents
            embeddings = embed_texts(
                [doc["content"] for doc in documents]
            )

            dim = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dim)
            self.index.add(embeddings)

            save_index(self.index, self.documents)

    def retrieve(self, query: str) -> list[dict]:
        query_embedding = embed_texts([query])
        _, indices = self.index.search(query_embedding, self.k)

        return [self.documents[i] for i in indices[0]]
