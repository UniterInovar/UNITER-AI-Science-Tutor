"""
Response Builder

Formats lesson content into different response styles.
"""

from __future__ import annotations


class ResponseBuilder:
    """
    Formats lesson content for students.
    """

    @staticmethod
    def build_student_response(lesson: dict) -> dict:
        """
        Build a student-friendly response.
        """

        equations = []

        for equation in lesson.get("equations", []):
            equations.append(
                {
                    "name": equation["name"],
                    "equation": equation["equation"],
                }
            )

        return {
            "topic": lesson.get("topic"),
            "definition": lesson.get("definition"),
            "simple_explanation": lesson.get("simple_explanation"),
            "detailed_explanation": lesson.get("detailed_explanation"),
            "equations": equations,
            "applications": lesson.get("applications", []),
            "exam_tips": lesson.get("exam_tips", []),
            "practice_questions": lesson.get("practice_questions", []),
            "related_topics": lesson.get("related_topics", []),
        }
