"""
FAISS persistent vector store
"""

import faiss
import pickle
import os


VECTOR_DIR = "data/vector_store"
INDEX_PATH = os.path.join(VECTOR_DIR, "index.faiss")
DOCS_PATH = os.path.join(VECTOR_DIR, "documents.pkl")


def save_index(index, documents):
    os.makedirs(VECTOR_DIR, exist_ok=True)

    faiss.write_index(index, INDEX_PATH)

    with open(DOCS_PATH, "wb") as f:
        pickle.dump(documents, f)


def load_index():
    if not os.path.exists(INDEX_PATH) or not os.path.exists(DOCS_PATH):
        return None, None

    index = faiss.read_index(INDEX_PATH)

    with open(DOCS_PATH, "rb") as f:
        documents = pickle.load(f)

    return index, documents
