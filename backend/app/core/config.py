"""
Application configuration.

Central location for application settings.
"""

from __future__ import annotations

from pathlib import Path


class Settings:
    """Application settings."""

    APP_NAME = "UNITER AI Science Tutor"

    APP_VERSION = "0.1.0"

    APP_DESCRIPTION = (
        "AI-powered science education platform for " "students, teachers and schools."
    )

    API_PREFIX = "/api/v1"

    PROJECT_ROOT = Path(__file__).resolve().parents[3]

    DATABASE_URL = f"sqlite:///{PROJECT_ROOT / 'uniter.db'}"

    LOG_LEVEL = "INFO"

    LOG_FILE = PROJECT_ROOT / "logs" / "backend.log"


settings = Settings()
