from agents.intent_agent import classify_intent
from router import route_intent
from agents.knowledge_agent import KnowledgeAgent
from agents.policy_agent import PolicyAgent
from agents.escalation_agent import EscalationAgent
from agents.analytics_agent import AnalyticsAgent
from ingestion.pdf_loader import load_pdfs
from ingestion.docx_loader import load_docx
from ingestion.chunker import chunk_documents


def load_knowledge_base():
    pdf_docs = load_pdfs("data/knowledge_base")
    docx_docs = load_docx("data/knowledge_base")
    return chunk_documents(pdf_docs + docx_docs)


# Load documents once
DOCUMENTS = load_knowledge_base()

# Initialize agents
knowledge_agent = KnowledgeAgent(DOCUMENTS)
policy_agent = PolicyAgent()
escalation_agent = EscalationAgent()
analytics_agent = AnalyticsAgent()


def handle_user_query(user_query: str) -> dict:
    intent = classify_intent(user_query)
    agent_name = route_intent(intent)

    # Log analytics (OBSERVE ONLY)
    analytics_agent.log_event(
        query=user_query,
        intent=intent,
        agent=agent_name
    )

    if agent_name == "Policy / Compliance Agent":
        return policy_agent.handle(user_query)

    if agent_name == "Knowledge Retrieval Agent":
        return knowledge_agent.handle(user_query)

    return escalation_agent.handle(user_query)


if __name__ == "__main__":
    while True:
        query = input("\nEnter customer query (type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        print(handle_user_query(query))
