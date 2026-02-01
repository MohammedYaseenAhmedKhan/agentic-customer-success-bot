from agents.intent_agent import classify_intent
from router import route_intent
from agents.knowledge_agent import KnowledgeAgent

# sample internal docs
DOCUMENTS = [
    "Users can reset their password from the account settings page.",
    "Subscriptions are billed monthly.",
    "Users can upgrade plans from the billing dashboard."
]

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
