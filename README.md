# Agentic Customer Support Assistant (RAG-based)

A production-style, multi-agent customer support assistant built using
Retrieval-Augmented Generation (RAG), deterministic policy handling,
human escalation, and analytics logging.

The system is designed to operate **even when LLM APIs are unavailable**,
ensuring reliability, auditability, and enterprise readiness.

---

## 🚀 Key Features
- Multi-agent architecture (Knowledge, Policy, Escalation, Analytics)
- Retrieval-Augmented Generation (RAG) using FAISS
- Local embeddings with SentenceTransformers
- Optional Gemini LLM integration with safe fallback
- Deterministic policy and compliance handling
- Human-in-the-loop escalation via ticketing
- Analytics logging for observability and audits
- Streamlit-based interactive UI
- Source-aware responses with document citations

---

## 🧠 System Architecture

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
- Analytics: JSONL-based logging
- Environment: virtualenv

---

## 📁 Project Structure

agentic-customer-support-bot/
├── app/ # Streamlit UI
├── src/
│ ├── agents/ # Agent implementations
│ ├── rag/ # Retrieval pipeline
│ ├── ingestion/ # Knowledge base ingestion
│ ├── llm/ # LLM integration layer
│ └── main.py # Orchestration entry point
├── data/
│ ├── knowledge_base/
│ ├── vector_store/
│ └── analytics/
├── requirements.txt
└── README.md


---

## ▶️ Running the Application

### CLI mode
```bash
python src/main.py
Streamlit UI
python -m streamlit run app/streamlit_app.py
⚠️ LLM Availability & Fallback Behavior
Uses Gemini LLM when API quota is available

Automatically falls back to retrieval-only answers when quota is exhausted

No code changes required when LLM access is restored

This ensures graceful degradation in production environments.

🎯 Example Queries
What is the leave policy?

What happens if an employee violates discipline rules?

I want to talk to HR

📊 Analytics & Observability
All queries, intents, and routing decisions are logged to:

data/analytics/query_logs.jsonl
This enables:

Identification of common user issues

Knowledge base gap analysis

Agent usage distribution monitoring

Audit and compliance reviews

🧪 Key Learnings
Designing reliable agent routing with deterministic fallbacks

Combining rule-based systems with LLM-driven agents

Handling LLM unavailability gracefully in production

Building observable and auditable AI systems

Structuring multi-agent architectures for extensibility

🏁 Project Highlights
LLM-optional, production-safe design

Enterprise-focused compliance handling

Human escalation support

Clean, modular, and extensible architecture
