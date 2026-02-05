from agents.intent_agent import classify_intent
from router import route_intent
from agents.knowledge_agent import KnowledgeAgent
from agents.policy_agent import PolicyAgent
from ingestion.pdf_loader import load_pdfs
from ingestion.docx_loader import load_docx
from ingestion.chunker import chunk_documents


def load_knowledge_base():
    """
    Loads and chunks all PDF and DOCX documents
    from the knowledge base directory.
    """
    pdf_docs = load_pdfs("data/knowledge_base")
    docx_docs = load_docx("data/knowledge_base")

    all_docs = pdf_docs + docx_docs
    return chunk_documents(all_docs)


# Load documents once at startup
DOCUMENTS = load_knowledge_base()

# Initialize agents
knowledge_agent = KnowledgeAgent(DOCUMENTS)
policy_agent = PolicyAgent()


def handle_user_query(user_query: str) -> dict:
    intent = classify_intent(user_query)
    agent = route_intent(intent)

    if agent == "Policy / Compliance Agent":
        return policy_agent.handle(user_query)

    if agent == "Knowledge Retrieval Agent":
        return knowledge_agent.handle(user_query)

    # Escalation (placeholder for Day 9)
    return {
        "agent": "Escalation Agent",
        "query": user_query,
        "answer": (
            "Your query requires further assistance. "
            "It has been escalated to the appropriate team."
        ),
        "sources": ["Support Escalation"]
    }


if __name__ == "__main__":
    while True:
        query = input("\nEnter customer query (type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        print(handle_user_query(query))
