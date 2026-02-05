"""
Policy / Compliance Agent

Handles sensitive HR and compliance-related queries
using deterministic, rule-based responses.
NO LLM is used here.
"""

class PolicyAgent:
    def __init__(self):
        # Deterministic policy rules
        self.policy_rules = {
            "discipline": (
                "Employees who violate disciplinary rules may face actions "
                "ranging from verbal warnings to written warnings, suspension, "
                "or termination depending on the severity and frequency of the violation."
            ),
            "termination": (
                "Termination may occur in cases of serious misconduct, repeated "
                "policy violations, or breach of company ethics and conduct standards."
            ),
            "discrimination": (
                "The organization maintains a zero-tolerance policy toward "
                "discrimination and harassment. Any confirmed incident will result "
                "in strict disciplinary action."
            ),
            "attendance": (
                "Repeated attendance violations such as frequent late arrivals "
                "or unapproved absences may lead to disciplinary action as outlined "
                "in the attendance policy."
            ),
        }

    def handle(self, query: str) -> dict:
        query_lower = query.lower()

        for keyword, response in self.policy_rules.items():
            if keyword in query_lower:
                return {
                    "agent": "Policy / Compliance Agent",
                    "query": query,
                    "answer": response,
                    "sources": ["Company HR Policy Rules"]
                }

        # Default safe response
        return {
            "agent": "Policy / Compliance Agent",
            "query": query,
            "answer": (
                "This policy-related query requires further review. "
                "Please consult HR or official company documentation."
            ),
            "sources": ["HR Review Required"]
        }
