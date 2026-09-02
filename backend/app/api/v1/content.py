"""
Content API

Provides endpoints for educational content.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from backend.app.models.content import (
    TopicRequest,
    TopicResponse,
)

from backend.app.services.content_service import (
    ContentService,
)

from backend.app.services.knowledge_loader import (
    KnowledgeLoader,
)

router = APIRouter(
    prefix="/content",
    tags=["Content"],
)


# ==========================================================
# Subjects
# ==========================================================


@router.get(
    "/subjects",
    summary="Get available subjects",
)
def get_subjects() -> dict:
    """
    Returns all available subjects.
    """

    return {"subjects": ContentService.get_subjects()}


# ==========================================================
# Levels
# ==========================================================


@router.get(
    "/subjects/{subject}",
    summary="Get levels for a subject",
)
def get_levels(subject: str) -> dict:
    """
    Returns available levels.
    """

    levels = ContentService.get_levels(subject)

    if not levels:
        raise HTTPException(
            status_code=404,
            detail="Subject not found.",
        )

    return {
        "subject": subject,
        "levels": levels,
    }


# ==========================================================
# Topics
# ==========================================================


@router.get(
    "/topics/{subject}/{level}",
    summary="Get available topics",
)
def get_topics(
    subject: str,
    level: str,
) -> dict:
    """
    Returns available topics.
    """

    topics = ContentService.get_topics(
        subject,
        level,
    )

    if not topics:
        raise HTTPException(
            status_code=404,
            detail="No topics found.",
        )

    return {
        "subject": subject,
        "level": level,
        "topics": topics,
    }


# ==========================================================
# Retrieve Lesson
# ==========================================================


@router.post(
    "/topic",
    response_model=TopicResponse,
    summary="Retrieve lesson content",
)
def get_topic(
    request: TopicRequest,
) -> TopicResponse:
    """
    Retrieve lesson content.
    """

    try:
        lesson = KnowledgeLoader.get_topic(
            subject=request.subject,
            level=request.level,
            topic=request.topic,
        )

        return TopicResponse(
            content=lesson,
        )

    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Topic not found.",
        )

    except ValueError:
        raise HTTPException(
            status_code=500,
            detail="Invalid lesson file.",
        )
