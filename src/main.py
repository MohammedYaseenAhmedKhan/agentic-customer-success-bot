from agents.intent_agent import classify_intent
from router import route_intent
from agents.knowledge_agent import KnowledgeAgent
from ingestion.pdf_loader import load_pdfs
from ingestion.chunker import chunk_documents


def load_knowledge_base():
    """
    Loads and chunks PDF documents from the knowledge base.
    """
    pdf_documents = load_pdfs("data/knowledge_base")
    documents = chunk_documents(pdf_documents)
    return documents


# Load documents once at startup
DOCUMENTS = load_knowledge_base()

# Initialize agent with PDF-based knowledge
knowledge_agent = KnowledgeAgent(DOCUMENTS)


def handle_user_query(user_query: str) -> dict:
    intent = classify_intent(user_query)
    agent = route_intent(intent)

    if agent == "Knowledge Retrieval Agent":
        return knowledge_agent.handle(user_query)

    return {
        "query": user_query,
        "detected_intent": intent,
        "routed_to": agent
    }


if __name__ == "__main__":
    query = input("Enter customer query: ")
    print(handle_user_query(query))
