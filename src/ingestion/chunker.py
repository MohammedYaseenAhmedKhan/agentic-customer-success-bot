"""
Text Chunker
Splits text into overlapping chunks
"""

def chunk_documents(
    documents: list[dict],
    chunk_size: int = 500,
    overlap: int = 100
) -> list[str]:

    chunks = []

    for doc in documents:
        text = doc["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]

            chunks.append(
                f"[{doc['source']} | Page {doc['page']}] {chunk}"
            )

            start = end - overlap

    return chunks
