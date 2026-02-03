"""
PDF Loader
Extracts text page-wise from PDFs
"""

import pdfplumber
from pathlib import Path


def load_pdfs(pdf_dir: str) -> list[dict]:
    documents = []

    for pdf_path in Path(pdf_dir).glob("*.pdf"):
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    documents.append({
                        "text": text,
                        "source": pdf_path.name,
                        "page": page_num + 1
                    })

    return documents
