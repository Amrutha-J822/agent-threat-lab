"""Pydantic models for versioned API responses."""

from datetime import datetime

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Canonical health payload for `/api/v1` routes."""

    status: str = Field(examples=["healthy"])
    service: str = Field(examples=["agent-threat-lab"])
    checked_at: datetime


class EchoRequest(BaseModel):
    """Body for the echo demo endpoint."""

    message: str = Field(min_length=1, max_length=500, examples=["hello"])


class EchoResponse(BaseModel):
    """Echo response with a server-side timestamp."""

    echo: str
    received_at: datetime
