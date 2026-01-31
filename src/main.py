"""
Entry point for the Agentic Customer Success Bot.
Coordinates intent detection, routing, and agent execution.

"""
"""
Main entry point for the Agentic Customer Success Bot.

This module:
- Takes user input from terminal
- Classifies intent using the Intent Agent
- Prints the detected intent
"""

from agents.intent_agent import classify_intent


def handle_user_query(user_query: str) -> dict:
    """
    Orchestrates processing of a user query.
    """
    intent = classify_intent(user_query)

    return {
        "query": user_query,
        "detected_intent": intent
    }


if __name__ == "__main__":
    print("Agentic Customer Success Bot")
    print("Type your query and press Enter (type 'exit' to quit)")
    print("-" * 50)

    while True:
        user_query = input(">> ")

        if user_query.lower().strip() == "exit":
            print("Exiting bot. Goodbye!")
            break

        result = handle_user_query(user_query)
        print(result)
        print("-" * 50)
