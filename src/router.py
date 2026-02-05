"""
Intent Router
Maps intents to responsible agents
"""

def route_intent(intent: str) -> str:
    if intent == "policy_query":
        return "Policy / Compliance Agent"

    if intent == "knowledge_query":
        return "Knowledge Retrieval Agent"

    # Default fallback
    return "Escalation Agent"
