---
title: Local Setup Guide
sidebarTitle: Setup
---

This guide explains how to set up a local development environment for MindsDB.

## Create a virtual environment

```bash
python -m venv mindsdb-venv
source mindsdb-venv/bin/activate
```

## Install MindsDB in editable mode

Navigate to the `mindsdb-main` directory and install the package:

```bash
cd mindsdb-main
pip install -e .
```

## Load environment variables

Store your configuration in a `.env` file and load it before starting the server:

```bash
source .env
```

## Start MindsDB with a custom engine

Launch the server using your custom engine configuration:

```bash
python -m mindsdb --config custom_engine.yaml
```

## Example SQL workflow

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

CREATE MODEL nl_sql_model
PREDICT 'sql'
USING engine = 'custom_llm';

SELECT sql
FROM nl_sql_model
WHERE question = 'Show top 10 clients by revenue';

EXECUTE IN snowflake_conn <sql>;
```

You can automate the last step by creating a view or pipeline that passes the generated SQL directly to the data source.

## Test the Snowflake connection

Run the helper script to verify that your `.env` configuration works:

```bash
cd mindsdb-main
python scripts/snowflake_test.py
```

The script loads environment variables, obtains an OAuth token for your LLM
endpoint, generates a SQL statement from a natural language question and then
executes it against Snowflake using MindsDB.
