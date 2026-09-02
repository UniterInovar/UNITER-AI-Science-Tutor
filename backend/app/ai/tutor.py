"""
AI Tutor

Coordinates topic matching,
content loading,
and response building.
"""

from __future__ import annotations

from backend.app.ai.response_builder import ResponseBuilder
from backend.app.ai.topic_matcher import TopicMatcher
from backend.app.services.content_service import ContentService


class Tutor:
    @staticmethod
    def ask(question: str) -> dict:
        match = TopicMatcher.find_topic(question)

        if match is None:
            return {
                "success": False,
                "message": ("Sorry, I couldn't identify the lesson topic."),
            }

        lesson = ContentService.get_topic(
            subject=match["subject"],
            level=match["level"],
            topic=match["topic"],
        )

        if lesson is None:
            return {
                "success": False,
                "message": "Lesson not found.",
            }

        response = ResponseBuilder.build_student_response(lesson)

        return {
            "success": True,
            "question": question,
            "subject": match["subject"],
            "level": match["level"],
            "response": response,
        }
