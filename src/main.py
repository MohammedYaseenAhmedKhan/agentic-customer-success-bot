from agents.intent_agent import classify_intent
from router import route_intent
from agents.knowledge_agent import KnowledgeAgent
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

# Initialize knowledge agent
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
    while True:
        query = input("\nEnter customer query (type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        print(handle_user_query(query))
