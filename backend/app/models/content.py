"""
Content Models
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class TopicRequest(BaseModel):
    """
    Request model.
    """

    subject: str = Field(
        ...,
        examples=["chemistry"],
    )

    level: str = Field(
        ...,
        examples=["ss3"],
    )

    topic: str = Field(
        ...,
        examples=["electrolysis"],
    )


class TopicResponse(BaseModel):
    """
    Response model.
    """

    content: dict[str, Any]