"""
Logging configuration.
"""

from __future__ import annotations

import logging
from pathlib import Path

from backend.app.core.config import settings


def configure_logging() -> logging.Logger:
    """
    Configure the application logger.
    """

    log_dir = Path(settings.LOG_FILE).parent
    log_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(settings.APP_NAME)

    if logger.handlers:
        return logger

    logger.setLevel(settings.LOG_LEVEL)

    handler = logging.FileHandler(
        settings.LOG_FILE,
        encoding="utf-8",
    )

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
