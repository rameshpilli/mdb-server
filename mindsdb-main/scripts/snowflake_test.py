import os
import asyncio
import logging
import json
from dotenv import load_dotenv
import httpx
import mindsdb_sdk

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


async def fetch_oauth_token():
    """Retrieve an OAuth token using environment variables."""
    oauth_endpoint = os.getenv("LLM_OAUTH_ENDPOINT")
    client_id = os.getenv("LLM_OAUTH_CLIENT_ID")
    client_secret = os.getenv("LLM_OAUTH_CLIENT_SECRET")
    grant_type = os.getenv("LLM_OAUTH_GRANT_TYPE", "client_credentials")
    scope = os.getenv("LLM_OAUTH_SCOPE", "read")

    if not all([oauth_endpoint, client_id, client_secret]):
        logger.error("OAuth variables not fully configured")
        return None

    data = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope,
    }

    async with httpx.AsyncClient(verify=False, timeout=30.0) as client:
        logger.info("Requesting OAuth token...")
        response = await client.post(
            oauth_endpoint,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        if response.status_code == 200:
            token = response.json().get("access_token")
            if token:
                token_preview = token[:10] + "..." if len(token) > 10 else token
                logger.info("Received token: %s", token_preview)
                return token
        logger.error("OAuth request failed: %s", response.text)
        return None


async def llm_generate_sql(token: str, question: str) -> str | None:
    """Use the LLM API to turn a question into SQL."""
    llm_model = os.getenv("LLM_MODEL")
    llm_base_url = os.getenv("LLM_BASE_URL")
    supports_temperature = os.getenv("LLM_SUPPORTS_TEMPERATURE", "false").lower() == "true"

    if not llm_base_url:
        logger.error("LLM base URL not configured")
        return None

    payload = {
        "model": llm_model,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": question},
        ],
        "max_tokens": 4000,
    }
    if supports_temperature:
        payload["temperature"] = 0.7

    async with httpx.AsyncClient(verify=False, timeout=60.0) as client:
        logger.info("Sending LLM request with payload: %s", json.dumps(payload))
        response = await client.post(
            llm_base_url,
            json=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            },
        )

        if response.status_code == 200:
            result = response.json()
            choices = result.get("choices")
            if choices:
                choice = choices[0]
                if "message" in choice and "content" in choice["message"]:
                    return choice["message"]["content"]
                if "content" in choice:
                    return choice["content"]
        logger.error("LLM request failed: %s", response.text)
        return None


async def run_query(sql: str):
    """Connect to MindsDB and execute the SQL against Snowflake."""
    server = mindsdb_sdk.connect()
    snowflake_db = server.create_database(
        engine="snowflake",
        name="snowflake_test",
        connection_args={
            "user": os.getenv("SNOWFLAKE_USER"),
            "password": os.getenv("SNOWFLAKE_PASSWORD"),
            "account": os.getenv("SNOWFLAKE_ACCOUNT"),
            "database": os.getenv("SNOWFLAKE_DATABASE"),
            "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
            "schema": os.getenv("SNOWFLAKE_SCHEMA"),
        },
    )
    result = snowflake_db.query(sql).fetch()
    logger.info("Query result: %s", result)


async def main():
    load_dotenv()

    token = await fetch_oauth_token()
    if not token:
        logger.error("Failed to obtain OAuth token")
        return

    question = "What is the Snowflake version? Respond with SQL only."
    sql = await llm_generate_sql(token, question)
    if not sql:
        logger.error("Failed to get SQL from LLM")
        return

    logger.info("Running SQL: %s", sql)
    await run_query(sql)


if __name__ == "__main__":
    asyncio.run(main())
