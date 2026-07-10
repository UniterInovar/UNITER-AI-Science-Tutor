"""
Health API endpoints.
"""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(
    tags=["Health"],
)


@router.get("/health")
async def health() -> dict[str, str]:
    """
    Health check endpoint.
    """

    return {
        "status": "healthy",
        "service": "UNITER AI Science Tutor API",
    }