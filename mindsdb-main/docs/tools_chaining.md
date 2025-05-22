---
title: Tools Chaining with SQLAgent
sidebarTitle: Tools Chaining
---

This guide explains how MindsDB converts natural language requests into SQL queries using the `SQLAgent` and `MindsDBSQLToolkit`.

## Building a SQLAgent

`SQLAgent` lives in `mindsdb.interfaces.skills.sql_agent` and requires the name of the database it should query. Optionally, you can restrict access by providing an `allowed_tables` list. When instantiated, the agent uses `MindsDBSQLToolkit` to interact with the database.

## Tools exposed by MindsDBSQLToolkit

`MindsDBSQLToolkit` exposes a set of tools used during the text2SQL process:

- `sql_db_list_tables` – list tables from the selected database, limited to `allowed_tables` when provided.
- `sql_db_schema` – return the schema for specific tables with a `sample_rows_limit` that controls how many example rows are shown.
- `sql_db_query` – execute an arbitrary SQL query and return the result.
- `mindsdb_sql_parser_tool` – help the agent craft or check SQL statements before execution.

## Flow of a natural prompt

1. A user prompt is passed to the `SQLAgent`.
2. The agent determines which tool to call. It may start with `sql_db_list_tables` or `sql_db_schema` to understand the structure of the allowed tables.
3. The agent uses `mindsdb_sql_parser_tool` to generate a valid SQL statement based on the prompt and schema information.
4. Finally, `sql_db_query` executes the generated SQL on the target database and returns the result to the caller.

### Important parameters

- `database`: name of the connected data source.
- `allowed_tables`: list of tables that the agent may access.
- `sample_rows_limit`: controls how many rows are returned when the schema tool provides sample data.

Using these tools in sequence enables MindsDB to transform conversational language into actionable SQL queries that run against your databases.
