"""
Agent Router

Routes user queries to the appropriate agent
based on detected intent.
"""

def route_intent(intent: str) -> str:
    """
    Maps intent to the responsible agent.
    """

    if intent == "product_question":
        return "Knowledge Retrieval Agent"

    if intent == "billing_issue":
        return "Billing Support Agent"

    if intent == "bug_report":
        return "Bug Report Agent"

    if intent == "feature_request":
        return "Feature Request Agent"

    return "General Support Agent"
