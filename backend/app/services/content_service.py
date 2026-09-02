"""
Content Service

Provides methods for discovering and loading
educational lesson content.
"""

from __future__ import annotations

import json
from pathlib import Path


class ContentService:
    """
    Service for discovering available educational content.
    """

    PROJECT_ROOT = Path(__file__).resolve().parents[3]
    CONTENT_DIR = PROJECT_ROOT / "content"

    @classmethod
    def get_subjects(cls) -> list[str]:
        """
        Return all available subjects.
        """

        if not cls.CONTENT_DIR.exists():
            return []

        return sorted(
            folder.name for folder in cls.CONTENT_DIR.iterdir() if folder.is_dir()
        )

    @classmethod
    def get_levels(
        cls,
        subject: str,
    ) -> list[str]:
        """
        Return available levels for a subject.
        """

        subject_path = cls.CONTENT_DIR / subject.lower()

        if not subject_path.exists():
            return []

        return sorted(
            folder.name for folder in subject_path.iterdir() if folder.is_dir()
        )

    @classmethod
    def get_topics(
        cls,
        subject: str,
        level: str,
    ) -> list[str]:
        """
        Return available topics.
        """

        level_path = cls.CONTENT_DIR / subject.lower() / level.lower()

        if not level_path.exists():
            return []

        return sorted(file.stem for file in level_path.glob("*.json"))

    @classmethod
    def get_topic(
        cls,
        subject: str,
        level: str,
        topic: str,
    ) -> dict | None:
        """
        Load a lesson JSON file.

        Returns:
            dict | None
        """

        file_path = (
            cls.CONTENT_DIR / subject.lower() / level.lower() / f"{topic.lower()}.json"
        )

        if not file_path.exists():
            return None

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)
