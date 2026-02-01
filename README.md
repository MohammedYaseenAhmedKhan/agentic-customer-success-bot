# Agentic Customer Success Bot for SaaS

An agent-based AI system designed to automate and streamline customer support workflows for SaaS applications.  
The system uses intent classification and agent routing to delegate customer queries to specialized agents.

---

## 🚀 Problem Statement

SaaS companies receive a wide range of customer queries such as product questions, billing issues, bug reports, and feature requests.  
Traditional chatbots or simple RAG-based systems treat all queries the same way, which leads to inefficient handling and poor user experience.

---

## 💡 Solution Overview

This project implements an **agentic customer support system** where:
- Each user query is first classified by intent
- A routing layer decides how the query should be handled
- Specialized agents execute task-specific logic
- Responses are returned in structured, enterprise-ready formats

---

## 🧠 High-Level Architecture

User Query
↓
Intent Classification Agent
↓
Agent Router
↓
Specialized Agent


Specialized agents include:
- Knowledge Retrieval Agent (RAG-based)
- Billing & Account Support Agent
- Bug Reporting & Feedback Agent
- General Support Agent

---

## 🏗️ Design Principles

- Separation of concerns between agents
- Modular and extensible architecture
- Transparent routing logic
- Focus on enterprise automation

---

## 🧰 Tech Stack (Planned)

- Python
- LLM (Gemini / OpenAI)
- SentenceTransformers
- FAISS
- Streamlit

---

## 📌 Project Status

- Day 1: Architecture and repository setup ✅
- Next: Intent classification agent

---

## 🔮 Future Enhancements

- CRM or ticketing system integration
- Analytics on support queries
- Confidence-based fallback handling

----

## 🗓️ Development Log

- **Day 2:** Implemented intent classification agent and CLI-based testing.

