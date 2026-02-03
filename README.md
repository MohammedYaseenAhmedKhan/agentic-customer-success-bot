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

- Day 1: Project setup and agentic architecture defined ✅
- Day 2: Intent classification agent implemented ✅
- Day 3: Intent-based agent routing logic added ✅
- Day 4: RAG-based Knowledge Retrieval Agent implemented (FAISS + embeddings) ✅


## 🧠 Day 4 – Knowledge Retrieval Agent (RAG)

Implemented a Retrieval-Augmented Generation (RAG) pipeline inside a specialized Knowledge Retrieval Agent.

Key components:
- SentenceTransformer embeddings for semantic understanding
- FAISS vector store for similarity search
- Retriever module to fetch top-k relevant documents
- Agent-level abstraction for knowledge-based queries

This design ensures scalable, explainable, and enterprise-ready document question answering.

## ✅ Progress Update

- Day 5: Integrated Gemini Flash 2.5 for grounded answer generation
- Implemented robust fallback when LLM quota is exhausted
- Validated end-to-end RAG pipeline


