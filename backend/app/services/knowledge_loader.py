"""
Knowledge Loader Service
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any


class KnowledgeLoader:
    """
    Loads educational content.
    """

    logger = logging.getLogger(__name__)

    PROJECT_ROOT = Path(__file__).resolve().parents[3]

    CONTENT_DIR = PROJECT_ROOT / "content"

    @classmethod
    def get_topic(
        cls,
        subject: str,
        level: str,
        topic: str,
    ) -> dict[str, Any]:
        lesson_path = (
            cls.CONTENT_DIR / subject.lower() / level.lower() / f"{topic.lower()}.json"
        )

        cls.logger.info("Loading lesson: %s", lesson_path)

        if not lesson_path.exists():
            raise FileNotFoundError(f"Lesson '{topic}' not found.")

        try:
            with lesson_path.open(
                "r",
                encoding="utf-8",
            ) as file:
                return json.load(file)

        except json.JSONDecodeError as error:
            raise ValueError("Invalid lesson JSON.") from error

    @classmethod
    def topic_exists(
        cls,
        subject: str,
        level: str,
        topic: str,
    ) -> bool:
        lesson_path = (
            cls.CONTENT_DIR / subject.lower() / level.lower() / f"{topic.lower()}.json"
        )

        return lesson_path.exists()
