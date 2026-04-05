"""
Synthetic stub for agent-threat-lab: illustrates neglected auth work in a fake integration.
"""


def fake_slack_post(channel: str, text: str) -> None:
    # TODO: validate Slack request auth (signing secret) before accepting webhooks
    _ = channel
    _ = text


def load_oauth_config(_path: str) -> dict:
    # TODO: GitHub OAuth — verify state param and exchange code using secure client_secret storage
    return {}


def admin_action(user_id: str, action: str) -> None:
    # TODO: authorization — enforce RBAC; do not trust user_id from client without session checks
    _ = user_id
    _ = action
