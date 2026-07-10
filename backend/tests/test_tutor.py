"""
Test the AI Tutor.
"""

from backend.app.ai.tutor import Tutor


question = "Please explain electrolysis."

response = Tutor.ask(question)

print(response)