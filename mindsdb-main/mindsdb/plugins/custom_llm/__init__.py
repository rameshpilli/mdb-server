import os
import requests
from typing import Optional

engine = 'custom_llm'

LLM_OPENAI_BASE_URL = os.getenv('LLM_OPENAI_BASE_URL', '').rstrip('/')


def _get_oauth_token() -> str:
    """Return an OAuth token using environment settings.

    This mirrors the behaviour of :func:`_get_oauth_token` from the internal
    `app/client.py` module. If ``MINDSDB_OAUTH_TOKEN`` is already present in the
    environment it is returned directly. Otherwise the function attempts to
    acquire a token using the client credential grant by sending a POST request
    to ``MINDSDB_OAUTH_SERVER`` with ``MINDSDB_OAUTH_CLIENT_ID`` and
    ``MINDSDB_OAUTH_CLIENT_SECRET``.
    """
    token = os.getenv('MINDSDB_OAUTH_TOKEN')
    if token:
        return token

    server = os.getenv('MINDSDB_OAUTH_SERVER')
    client_id = os.getenv('MINDSDB_OAUTH_CLIENT_ID')
    client_secret = os.getenv('MINDSDB_OAUTH_CLIENT_SECRET')
    if not (server and client_id and client_secret):
        raise RuntimeError('OAuth credentials not provided')

    resp = requests.post(
        f'{server}/oauth/token',
        data={'grant_type': 'client_credentials'},
        auth=(client_id, client_secret),
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()
    return data.get('access_token') or data.get('token')


def generate_sql(question: str) -> str:
    """Generate SQL for a natural language question via the LLM service."""
    if not LLM_OPENAI_BASE_URL:
        raise RuntimeError('LLM_OPENAI_BASE_URL is not configured')

    token = _get_oauth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    resp = requests.post(
        LLM_OPENAI_BASE_URL,
        json={'question': question},
        headers=headers,
        timeout=30,
    )
    resp.raise_for_status()
    try:
        return resp.json().get('sql', '')
    except Exception:
        return resp.text
