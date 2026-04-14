"""
HTTP API surface for agent-threat-lab.

Includes intentional duplicate routes (same behavior, different paths) for scanner /
review drills, plus a small versioned API with consistent models.
"""

from datetime import datetime, timezone

from fastapi import APIRouter, FastAPI

from agent_threat_lab import __version__
from agent_threat_lab.schemas import EchoRequest, EchoResponse, HealthResponse

app = FastAPI(
    title="Agent Threat Lab API",
    version=__version__,
    description="Demo API: redundant liveness routes + versioned `/api/v1` routes.",
)

# --- Intentionally redundant: five paths, one behavior (liveness JSON) ---


def _legacy_liveness() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health", tags=["legacy-duplicates"])
def health_legacy() -> dict[str, str]:
    return _legacy_liveness()


@app.get("/healthcheck", tags=["legacy-duplicates"])
def healthcheck_legacy() -> dict[str, str]:
    return _legacy_liveness()


@app.get("/ping", tags=["legacy-duplicates"])
def ping_legacy() -> dict[str, str]:
    return _legacy_liveness()


@app.get("/status", tags=["legacy-duplicates"])
def status_legacy() -> dict[str, str]:
    return _legacy_liveness()


@app.get("/alive", tags=["legacy-duplicates"])
def alive_legacy() -> dict[str, str]:
    return _legacy_liveness()


# --- Versioned API: single health concept, structured responses, namespaced routes ---

api_v1 = APIRouter(prefix="/api/v1", tags=["api-v1"])


@api_v1.get("/health", response_model=HealthResponse)
def health_v1() -> HealthResponse:
    return HealthResponse(
        status="healthy",
        service="agent-threat-lab",
        checked_at=datetime.now(timezone.utc),
    )


@api_v1.get("/version")
def version_v1() -> dict[str, str]:
    return {"service": "agent-threat-lab", "version": __version__}


@api_v1.post("/echo", response_model=EchoResponse)
def echo_v1(body: EchoRequest) -> EchoResponse:
    return EchoResponse(
        echo=body.message,
        received_at=datetime.now(timezone.utc),
    )


app.include_router(api_v1)
