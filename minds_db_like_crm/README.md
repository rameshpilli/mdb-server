# MindsDB CRM Example

This directory contains helper scripts for running a MindsDB agent that acts like a CRM assistant. It uses the built in `litellm_server.py` FastAPI server and the `run_mcp_agent.py` interactive CLI.

## Required Environment Variables

Set the following variables before starting the server or CLI:

- `MCP_HOST` – host of the running MCP server (e.g. `127.0.0.1`)
- `MCP_PORT` – port of the MCP server (e.g. `47337`)
- `AGENT_NAME` – name of the registered agent to use
- `PROJECT_NAME` – project that contains the agent (defaults to `mindsdb`)
- `HOST` – address for the FastAPI server to bind to (default `0.0.0.0`)
- `PORT` – port for the FastAPI server (default `8000`)

You can place these values in a `.env` file and load them with `source .env`.

## Starting the FastAPI Server

Run `litellm_server.py` with your agent and MCP details:

```bash
python mindsdb/interfaces/agents/litellm_server.py \
    --agent "$AGENT_NAME" \
    --project "$PROJECT_NAME" \
    --mcp-host "$MCP_HOST" \
    --mcp-port "$MCP_PORT" \
    --host "$HOST" \
    --port "$PORT"
```

This exposes an OpenAI compatible `/v1/chat/completions` endpoint backed by your MCP agent.

## Using the Interactive CLI

You can talk to the agent from a terminal using `run_mcp_agent.py`:

```bash
python mindsdb/interfaces/agents/run_mcp_agent.py \
    --agent "$AGENT_NAME" \
    --project "$PROJECT_NAME" \
    --host "$MCP_HOST" \
    --port "$MCP_PORT"
```

When started without `--query` the program enters interactive mode. Type natural language prompts or prefix a statement with `sql:` to run a raw SQL command through the MCP server.

### Example Commands

```
> What are my top leads this week?
> sql: SELECT id, name FROM leads LIMIT 5
```

The first line sends a regular prompt to the agent. The second issues a direct SQL query using the registered `query` tool.

