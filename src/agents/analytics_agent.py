"""
Analytics / Feedback Agent

Logs user queries, detected intents, and routed agents
for monitoring and future system improvements.
"""

import json
from datetime import datetime
from pathlib import Path


class AnalyticsAgent:
    def __init__(self, log_dir: str = "data/analytics"):
        self.log_path = Path(log_dir) / "query_logs.jsonl"
        Path(log_dir).mkdir(parents=True, exist_ok=True)

    def log_event(self, query: str, intent: str, agent: str):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "query": query,
            "intent": intent,
            "agent": agent
        }

        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")

