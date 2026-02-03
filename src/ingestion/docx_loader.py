"""
DOCX Loader
Extracts text from .docx files for RAG ingestion
"""

from docx import Document
from pathlib import Path


def load_docx(docx_dir: str) -> list[dict]:
    documents = []

    for docx_path in Path(docx_dir).glob("*.docx"):
        doc = Document(docx_path)

        text = "\n".join(
            p.text for p in doc.paragraphs if p.text.strip()
        )

        if text:
            documents.append({
                "text": text,
                "source": docx_path.name,
                "page": "N/A"
            })

    return documents
