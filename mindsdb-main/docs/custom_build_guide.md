---
title: Custom Build Guide
sidebarTitle: Custom Build
---

This guide explains how to run a local build of MindsDB, connect to Snowflake, and send natural prompts to the server.

## Set up the environment

1. Clone the repository and create a Python virtual environment:

```bash
git clone https://github.com/mindsdb/mindsdb.git
cd mindsdb-main
python -m venv venv
source venv/bin/activate
```

2. Install MindsDB in editable mode and its dependencies:

```bash
pip install -e .
```

3. Copy `.env.example` to `.env` and fill in the values for your LLM and Snowflake credentials.

```bash
cp ../.env.example .env
# edit .env and set SNOWFLAKE_* values
```

## Start the server

Load the environment variables and start MindsDB with the APIs you need:

```bash
source .env
python -m mindsdb --api http,mysql
```

The `--api` flag controls which built‑in APIs are exposed. `http` enables the REST interface and `mysql` starts a MySQL‑compatible endpoint.

## Connect to Snowflake

Once the server is running, create a connection using the credentials from your `.env` file:

```sql
CREATE DATABASE snowflake_conn
WITH ENGINE = 'snowflake',
PARAMETERS = {
    "user":      $SNOWFLAKE_USER,
    "password":  $SNOWFLAKE_PASSWORD,
    "account":   $SNOWFLAKE_ACCOUNT,
    "database":  $SNOWFLAKE_DATABASE,
    "warehouse": $SNOWFLAKE_WAREHOUSE,
    "schema":    $SNOWFLAKE_SCHEMA
};
```

Each connection targets a single database and optional schema. Create additional connections if you need to work with multiple schemas.

## Chat with natural prompts

Send natural language requests to the HTTP API. MindsDB will convert them to SQL using the text‑to‑SQL agent and execute them on the connected database:

```bash
curl -X POST http://127.0.0.1:47334/api/sql \
     -H 'Content-Type: application/json' \
     -d '{"query": "Show top 5 customers by revenue"}'
```

You can achieve the same from Python:

```python
import requests
response = requests.post(
    "http://127.0.0.1:47334/api/sql",
    json={"query": "Show top 5 customers by revenue"}
)
print(response.json())
```

## Where to modify the code

- HTTP and other API routes live under `mindsdb/api`.
- The SQL planner and parser reside in the `mindsdb_sql` package.
- LLM integration and skills are implemented in `mindsdb/interfaces/skills`.

Edit these modules to customize routing logic, SQL generation, or LLM behavior.

## Task: Support multiple Snowflake connections

Extend the configuration so that several sets of Snowflake credentials can be defined and loaded, allowing the server to create multiple connections automatically.
