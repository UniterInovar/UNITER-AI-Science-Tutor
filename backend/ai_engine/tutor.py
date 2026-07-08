"""
AI Tutor Engine

Handles student questions and retrieves knowledge.
"""

from __future__ import annotations

from subjects.chemistry import get_topic


class ScienceTutor:
    """
    Basic AI Science Tutor.
    """

    def answer(
        self,
        subject: str,
        topic: str,
    ):
        """
        Answer a student's question.

        Args:
            subject: Subject name.
            topic: Topic requested.

        Returns:
            Dictionary containing the topic information,
            or an error message.
        """

        subject = subject.lower().strip()

        if subject == "chemistry":

            result = get_topic(topic)

            if result:
                return result

            return "Topic not found."

        return "Subject not supported yet."