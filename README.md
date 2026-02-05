# Agentic Customer Support Assistant (RAG-based)

A production-style, multi-agent customer support assistant built using
Retrieval-Augmented Generation (RAG), deterministic policy handling,
human escalation, analytics logging, and a Streamlit UI.

The system is designed to **work even when LLM APIs are unavailable**,
making it reliable, auditable, and enterprise-ready.

---

## 🚀 Key Features

- Multi-agent architecture (Knowledge, Policy, Escalation, Analytics)
- Retrieval-Augmented Generation (RAG) using FAISS
- SentenceTransformers for local embeddings
- Gemini LLM integration with safe fallback
- Deterministic policy & compliance handling
- Human-in-the-loop escalation with ticketing
- Analytics logging for observability
- Streamlit-based interactive UI
- Source-aware answers with document citations

---

## 🧠 Architecture Overview

User Query
↓
Intent Classification
↓
Agent Router
↓
+-------------------------------+
| Knowledge Agent (RAG + LLM) |
| Policy Agent (Rules-based) |
| Escalation Agent (Human) |
+-------------------------------+
↓
Analytics Agent (Logging)


---

## 🧰 Tech Stack

- Language: Python
- Embeddings: SentenceTransformers
- Vector Store: FAISS
- LLM: Google Gemini (optional)
- UI: Streamlit
- Document Parsing: pdfplumber, python-docx
- Analytics: JSONL logging
- Environment: virtualenv

---

## 📁 Project Structure

agentic-customer-success-bot/
├── app/
│ └── streamlit_app.py
├── src/
│ ├── agents/
│ ├── rag/
│ ├── ingestion/
│ ├── llm/
│ └── main.py
├── data/
│ ├── knowledge_base/
│ ├── vector_store/
│ └── analytics/
├── requirements.txt
└── README.md


---

## 🖥️ Run the Application

### CLI
```bash
python src/main.py
Streamlit UI
python -m streamlit run app/streamlit_app.py
⚠️ LLM Availability Note
The system automatically uses Gemini LLM when API quota is available

If quota is exhausted, it falls back to retrieval-only answers

No code changes are required when tokens are restored

This ensures graceful degradation in production.

🎯 Example Queries
What is the leave policy?

What happens if an employee violates discipline rules?

I want to talk to HR

📊 Analytics
All queries, intents, and routing decisions are logged to:

data/analytics/query_logs.jsonl
This helps identify:

Common user questions

Knowledge gaps

Agent usage distribution

🏁 Project Highlights
LLM-optional architecture

Enterprise-safe compliance handling

Human escalation support

Observability and auditability

Clean, modular, and extensible design


---
