# Agentic Customer Support Assistant (RAG-based)

A production-style **Agentic Customer Support Assistant** built using
**Retrieval-Augmented Generation (RAG)**, deterministic policy handling,
human escalation, analytics logging, and a **Streamlit UI**.

The system is designed to **work reliably even when LLM APIs are unavailable**,
making it suitable for real enterprise environments.

---

## 🚀 Key Features

- Multi-agent architecture (Intent, Knowledge, Policy, Escalation, Analytics)
- Retrieval-Augmented Generation (RAG) using FAISS
- Semantic embeddings with SentenceTransformers
- Optional LLM answer synthesis (Gemini) with graceful fallback
- Deterministic policy & compliance handling (no hallucinations)
- Human-in-the-loop escalation support
- Analytics logging for observability
- Streamlit-based interactive UI
- Source-aware answers with document citations

---

## 🧠 System Architecture

User Query
↓
Intent Classification Agent
↓
Intent Router
↓
+--------------------------------------+
| Knowledge Agent (RAG + optional LLM) |
| Policy / Compliance Agent |
| Escalation Agent (Human Handoff) |
+--------------------------------------+
↓
Analytics Agent (Logging & Monitoring)


---

## 🧰 Tech Stack

| Layer | Technology |
|-----|-----------|
| Language | Python |
| Embeddings | SentenceTransformers |
| Vector Store | FAISS |
| LLM | Google Gemini (optional) |
| UI | Streamlit |
| Document Parsing | pdfplumber, python-docx |
| Environment | virtualenv |
| Logging | JSONL |

---

## 📁 Project Structure

agentic-customer-success-bot/
├── app/
│ └── streamlit_app.py
├── src/
│ ├── agents/
│ │ ├── intent_agent.py
│ │ ├── knowledge_agent.py
│ │ ├── policy_agent.py
│ │ ├── escalation_agent.py
│ │ └── analytics_agent.py
│ ├── rag/
│ │ ├── retriever.py
│ │ ├── embedder.py
│ │ └── faiss_store.py
│ ├── ingestion/
│ │ ├── pdf_loader.py
│ │ ├── docx_loader.py
│ │ └── chunker.py
│ └── main.py
├── data/
│ ├── knowledge_base/
│ ├── vector_store/
│ └── analytics/
├── requirements.txt
├── DEVELOPER_NOTES.md
└── README.md


---

## 🖥️ Running the Application

### 1️⃣ Activate Environment
```bash
.\.venv\Scripts\Activate.ps1
2️⃣ Run CLI Version
python src/main.py
3️⃣ Run Streamlit UI
python -m streamlit run app/streamlit_app.py
Open browser at:

http://localhost:8501
💬 Example Queries
What is the leave policy?

What happens if an employee violates discipline rules?

I want to talk to HR

⚠️ LLM Availability & Fallback Design
The system automatically uses Gemini LLM when API quota is available

If tokens are exhausted or API fails:

The system falls back to retrieval-only answers

No crashes

No hallucinations

No code changes are required when tokens are restored

This ensures graceful degradation, which is critical in production systems.

📊 Analytics & Observability
All queries and routing decisions are logged to:

data/analytics/query_logs.jsonl
This enables:

Understanding common user questions

Identifying knowledge gaps

Measuring agent usage distribution

🎯 Design Decisions
Used a multi-agent architecture to avoid overloading a single LLM

Avoided LLMs for policy and compliance queries to prevent hallucinations

Designed the system to function even without LLM availability

Used FAISS locally to keep the system simple and cost-efficient

Clean separation between ingestion, retrieval, reasoning, and UI layers

🏁 Summary
This project demonstrates:

Practical RAG implementation

Agentic system design

Enterprise-safe AI practices

Robust fallback handling

Clean engineering and Git hygiene

It is intended to reflect real-world AI system design, not just a demo.

