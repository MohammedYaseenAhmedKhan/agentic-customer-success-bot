# Developer Notes

## Environment Setup
- Python 3.10+
- Virtual environment required
- On Windows, prefer `python -m pip` and `python -m streamlit`

## Common Issues & Fixes

### Import Errors
- Always import modules via `src.<module>`
- Ensure `__init__.py` exists in all packages

### Vector Store Issues
- If document schema or chunk structure changes:
  - Delete `data/vector_store/index.faiss`
  - Delete `data/vector_store/documents.pkl`
  - Re-run ingestion

### LLM Token Limits
- Gemini API usage is optional
- System automatically falls back to retrieval-only answers
- No action required when tokens are exhausted

## Git Hygiene
- Do NOT commit FAISS indexes or analytics logs
- These are runtime artifacts
- `.gitignore` handles exclusions

## Recommended Commands
```bash
python src/main.py
python -m streamlit run app/streamlit_app.py
