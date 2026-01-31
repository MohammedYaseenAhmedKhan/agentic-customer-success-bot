"""
Intent Classification Agent

Responsible for identifying the type of customer query
so that it can be routed to the correct specialized agent.
"""

from typing import Literal


SUPPORTED_INTENTS = [
    "product_question",
    "billing_issue",
    "bug_report",
    "feature_request",
    "general_support"
]


def classify_intent(user_query: str) -> Literal[
    "product_question",
    "billing_issue",
    "bug_report",
    "feature_request",
    "general_support"
]:
    """
    Classifies the intent of a customer query using simple rule-based logic.
    This can later be replaced by an LLM-based classifier.
    """

    query = user_query.lower()

    if any(word in query for word in ["bill", "payment", "invoice", "refund", "charged"]):
        return "billing_issue"

    if any(word in query for word in ["error", "bug", "crash", "issue", "problem"]):
        return "bug_report"

    if any(word in query for word in ["feature", "add", "request", "improve"]):
        return "feature_request"

    if any(word in query for word in ["how", "what", "where", "guide", "usage"]):
        return "product_question"

    return "general_support"
