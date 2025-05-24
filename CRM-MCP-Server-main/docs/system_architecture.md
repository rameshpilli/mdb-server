# System Architecture Overview

## Components

### 1. Model Context Protocol (MCP)
- Handles all model interactions
- Manages context and tool execution
- Provides OAuth authentication for model access

### 2. Cohere Compass Integration
- Semantic search capabilities
- Document indexing and retrieval
- Real-time context enhancement

### 3. Local Document Store
- Location: `/docs` directory
- Supports markdown and text files
- Used for storing internal documentation
- Accessible via document search tool

## Configuration

### Environment Variables
- `LLM_MODEL`: Model identifier
- `COHERE_INDEX_NAME`: Index for semantic search
- `LLM_BASE_URL`: Base URL for model endpoint

### Security
- OAuth2 authentication for model access
- Bearer token for Cohere API
- Local file system security

## Deployment
- Supports both local and Kubernetes deployment
- Configuration via environment variables
- Logging to both CSV and file outputs

## Architecture Options

The initial architecture routed Chainlit through FastAPI to `mcp_bridge` and then to the individual tools.

MindsDB now includes an MCP Langchain agent that works with the SQL agent. This provides a more direct path from Chainlit to the underlying data.

### Switching Approaches
1. Copy `.env.example` to `.env` and supply any credentials. Environment variables are left blank by default.
2. Start the MCP Langchain agent to use the new flow.
3. Launch the FastAPI application if you prefer the original `mcp_bridge` pipeline.
