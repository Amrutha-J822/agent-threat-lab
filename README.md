# agent-threat-lab

Demo project for **testing only**. It ships synthetic “bad practice” samples under `tests/fixtures/` (a fake repo layout) so you can try scanners, reviews, or tooling without real credentials:

| Item | Location |
|------|----------|
| Hardcoded Slack-style token | `tests/fixtures/slack_env_sample.env` |
| GitHub OAuth `client_secret` in config | `tests/fixtures/github_oauth_config.json` |
| Three TODOs mentioning auth | `tests/fixtures/sample_integration.py` |

All values are placeholders. Do not use this demo in production or substitute real API keys here.

## Python

Requires **Python 3.13+**. From the repo root:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

`pyproject.toml` records `requires-python >= 3.13`.
