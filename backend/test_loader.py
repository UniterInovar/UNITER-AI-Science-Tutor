"""
Simple loader test.
"""

from backend.app.services.knowledge_loader import (
    KnowledgeLoader,
)


lesson = KnowledgeLoader.get_topic(
    subject="chemistry",
    level="ss3",
    topic="electrolysis",
)

print("=" * 60)
print("Topic:", lesson["topic"])
print("Definition:", lesson["definition"])
print("=" * 60)