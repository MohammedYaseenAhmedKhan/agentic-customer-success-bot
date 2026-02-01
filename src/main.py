"""
Main entry point for the Agentic Customer Success Bot.
"""

from agents.intent_agent import classify_intent
from router import route_intent


def handle_user_query(user_query: str) -> dict:
    intent = classify_intent(user_query)
    assigned_agent = route_intent(intent)

    return {
        "query": user_query,
        "detected_intent": intent,
        "routed_to": assigned_agent
    }


if __name__ == "__main__":
    user_query = input("Enter customer query: ")
    result = handle_user_query(user_query)
    print(result)
