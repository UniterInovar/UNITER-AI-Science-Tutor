"""
Test Topic Matcher
"""

from backend.app.ai.topic_matcher import TopicMatcher


question = "Please explain electrolysis."

result = TopicMatcher.find_topic(question)

print(result)
