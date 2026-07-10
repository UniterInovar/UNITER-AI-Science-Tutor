"""
Topic Matcher

Matches a student's question to an available lesson topic.
Supports exact topic matching and keyword matching.
"""

from __future__ import annotations

import re

from backend.app.services.content_service import ContentService


class TopicMatcher:
    """
    Matches natural-language questions to lesson topics.
    """

    # Words that don't help identify the lesson topic
    STOP_WORDS = {
        "what",
        "is",
        "are",
        "the",
        "a",
        "an",
        "please",
        "explain",
        "define",
        "teach",
        "me",
        "about",
        "tell",
        "give",
        "lesson",
        "notes",
        "note",
        "on",
        "of",
        "for",
        "to",
        "how",
        "can",
        "you",
    }

    @staticmethod
    def clean_question(question: str) -> str:
        """
        Clean the student's question.
        """

        question = question.lower()

        question = re.sub(r"[^\w\s]", "", question)

        return question

    @classmethod
    def extract_keywords(cls, question: str) -> list[str]:
        """
        Remove common words and return useful keywords.
        """

        question = cls.clean_question(question)

        words = question.split()

        keywords = [
            word
            for word in words
            if word not in cls.STOP_WORDS
        ]

        return keywords

    @classmethod
    def find_topic(cls, question: str) -> dict | None:
        """
        Find the lesson that best matches the student's question.
        """

        cleaned_question = cls.clean_question(question)

        keywords = cls.extract_keywords(question)

        subjects = ContentService.get_subjects()

        # -------------------------------------
        # First try exact topic matching
        # -------------------------------------

        for subject in subjects:

            levels = ContentService.get_levels(subject)

            for level in levels:

                topics = ContentService.get_topics(subject, level)

                for topic in topics:

                    topic_lower = topic.lower()

                    pattern = r"\b" + re.escape(topic_lower) + r"\b"

                    if re.search(pattern, cleaned_question):

                        return {
                            "subject": subject,
                            "level": level,
                            "topic": topic,
                            "match_type": "exact",
                        }

        # -------------------------------------
        # Keyword matching
        # -------------------------------------

        for subject in subjects:

            levels = ContentService.get_levels(subject)

            for level in levels:

                topics = ContentService.get_topics(subject, level)

                for topic in topics:

                    topic_words = topic.lower().split()

                    matches = sum(
                        1
                        for keyword in keywords
                        if keyword in topic_words
                    )

                    if matches > 0:

                        return {
                            "subject": subject,
                            "level": level,
                            "topic": topic,
                            "match_type": "keyword",
                        }

        return None