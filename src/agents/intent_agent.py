"""
Intent Classification Agent
Determines which agent should handle the user query
"""

def classify_intent(query: str) -> str:
    query = query.lower()

    # Policy / compliance related queries
    if any(word in query for word in [
        "discipline",
        "termination",
        "violation",
        "discrimination",
        "harassment",
        "attendance issue",
        "misconduct"
    ]):
        return "policy_query"

    # Knowledge-based queries
    if any(word in query for word in [
        "leave",
        "policy",
        "benefits",
        "working hours",
        "attendance"
    ]):
        return "knowledge_query"

    # Everything else
    return "general_query"
