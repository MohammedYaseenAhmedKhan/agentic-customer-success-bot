"""
Text Chunker
Splits documents into overlapping chunks with metadata
"""

def chunk_documents(
    documents: list[dict],
    chunk_size: int = 500,
    overlap: int = 100
) -> list[dict]:

    chunks = []

    for doc in documents:
        text = doc["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append({
                "content": chunk_text,
                "source": doc["source"],
                "page": doc["page"]
            })

            start = end - overlap

    return chunks
