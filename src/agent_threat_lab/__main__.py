"""Run the API with: python -m agent_threat_lab (after `pip install -e .`)."""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "agent_threat_lab.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
