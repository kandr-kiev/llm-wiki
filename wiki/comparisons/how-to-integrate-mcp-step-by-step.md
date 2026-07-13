---
title: "How to Integrate MCP — Step-by-Step"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - application
  - architecture
  - async
  - automation
  - claude
  - data
  - deployment
  - foundation-model
  - llm
  - machine-learning
  - playbook
  - prompt-tuning
  - real-time
  - review
  - search
  - security
  - tool
  - use-case
  - vector-database
---
# How to Integrate MCP — Step-by-Step

> **Source:** how-to-integrate-mcp.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- type: playbook title: "How to Integrate MCP — Step-by-Step" description: Actionable runbook for implementing Model Context Protocol: build MCP servers, connect clients, and expose tools to AI appl...
> **Sources:**
>   - how-to-integrate-mcp.md
> **Links:**
- [[how-to-integrate-mcp]]
- [[how-to-use-cloudflare-workers-ai]]
- [[how-to-engineer-prompts]]
- [[how-to-build-ai-agents]]
- [[how-to-evaluate-llm-models]]

## Key Findings


# How to Integrate MCP — Step-by-Step
Actionable runbook for implementing the Model Context Protocol: building MCP servers, connecting clients, and exposing tools/resources/prompts to AI applications.
## Prerequisites
- Python 3.10+ or Node.js 18+
- Understanding of JSON-RPC 2.0
- An MCP-compatible host (Claude Code, Claude Desktop, VS Code, or custom client)
## Phase 1: MCP Architecture Overview
### Step 1.1 — Understand the three participants
| Participant | Role | Example |
|---|---|---|
| **MCP Host** | AI application that coordinates MCP clients | Claude Code, Claude Desktop, VS Code |
| **MCP Client** | Maintains connection to one MCP server | ClientSession (Python SDK) |
| **MCP Server** | Provides context (tools, resources, prompts) | Filesystem server, Sentry server, custom |
### Step 1.2 — Choose transport layer
| Transport | Use Case | Auth |
|---|---|---|
| **Stdio** | Local processes on same machine | None (process isolation) |
| **Streamable HTTP** | Remote servers, many clients | OAuth, API keys, bearer tokens |
## Phase 2: Build Your First MCP Server (Python)
### Step 2.1 — Install SDK
```bash
pip install mcp
```
### Step 2.2 — Create a basic server
```python
from mcp.server import Server
from mcp.types import Tool, TextContent
server = Server("my-mcp-server")
@server.tool()
async def get_weather(location: str, units: str = "metric") -> list[TextContent]:
"""Get current weather for a location."""
# Replace with actual API call
temperature = 22 if units == "metric" else 72
return [TextContent(type="text", text=f"{temperature}°{ 'C' if units == 'metric' else 'F'} in {location}")]
@server.list_tools()
async def list_tools() -> list[Tool]:
return [
Tool(
name="get_weather",
description="Get current weather for a location",
inputSchema={
"type": "object",
"properties": {
"location": {"type": "string", "description": "City name"},
"units": {"type": "string", "enum": ["metric", "imperial"], "default": "metric"}
},
"required": ["location"]
}
)
]
if __name__ == "__main__":
import asyncio
from mcp.server.stdio import stdio_server
asyncio.run(stdio_server(server))
```
### Step 2.3 — Test with MCP Inspector
```bash
# Install Inspector
npm install -g @modelcontextprotocol/inspector
# Run your server with Inspector
mcp-inspector python my_server.py
```
## Phase 3: Lifecycle Management
### Step 3.1 — Connection initialization
```python
# Client sends initialize request
init_request = {
"jsonrpc": "2.0",
"id": 1,
"method": "initialize",
"params": {
"protocolVersion": "2025-06-18",
"capabil

## Summary

ities": {
"elicitation": {} # Client supports user interaction requests
},
"clientInfo": {
"name": "example-client",
"version": "1.0.0"
}
}
}
# Server responds with capabilities
init_response = {
"jsonrpc": "2.0",
"id": 1,
"result": {
"protocolVersion": "2025-06-18",
"capabilities": {
"tools": {"listChanged": True}, # Supports tools + notifications
"resources": {} # Also supports resources
},
"serverInfo": {
"name": "my-mcp-server",
"version": "1.0.0"
}
}
}
# Client sends ready notification
ready_notification = {
"jsonrpc": "2.0",
"method": "notifications/initialized"
}
```
### Step 3.2 — Capability negotiation checklist
- [ ] Protocol version compatible?
- [ ] Server supports required primitives (tools/resources/prompts)?
- [ ] Client supports required features (elicitation/sampling)?
- [ ] If incompatible → terminate connection
## Phase 4: Server Primitives
### Step 4.1 — Tools (executable functions)
```python
@server.list_tools()
async def list_tools() -> list[Tool]:
return [
Tool(
name="search_database",
description="Search the database for records",
inputSchema={
"type": "object",
"properties": {
"query": {"type": "string"},
"limit": {"type": "integer", "default": 10}
},
"required": ["query"]
}
),
Tool(
name="create_record",
description="Create a new database record",
inputSchema={
"type": "object",
"properties": {
"table": {"type": "string"},
"data": {"type": "object"}
},
"required": ["table", "data"]
}
)
]
@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
if name == "search_database":
results = db.search(arguments["query"], arguments.get("limit", 10))
return [TextContent(type="text", text=json.dumps(results))]
elif name == "create_record":
record_id = db.create(arguments["table"], arguments["data"])
return [TextContent(type="text", text=f"Created record: {record_id}")]
```
### Step 4.2 — Resources (data sources)
```python
@server.list_resources()
async def list_resources() -> list[Resource]:
return [
Resource(
uri="db://schema/users",
name="Users table schema",
description="Schema definition for the users table",
mimeType="application/json"
)
]
@server.read_resource()
async def read_resource(uri: str) -> str:
if uri == "db://schema/users":
return json.dumps({
"table": "users",
"columns": ["id", "name", "email", "created_at"]
})
raise ValueError(f"Unknown resource: {uri}")
```
### Step 4.3 — Prompts (reusable templates)
```python
@server.list_prompts()
async def list_prompts() -> list[Prompt]:
return [
Prompt(
name="code_review",
description="Template for code review requests",
arguments=[
PromptArgument(
name="file_path",
description="Path to the file to review",
required=True
)
]
)
]
@server.get_prompt()
async def get_prompt(name: str, arguments: dict | None) -> PromptMessage:
if name == "code_review":
file_path = arguments["file_path"]
return PromptMessage(
role="user",
content=TextContent(
type="text",
text=f"Review this file for security vulnerabilities:\n\n{file_path}"
)
)
```
## Phase 5: Client

## Related Articles

- [[how-to-integrate-mcp]]
- [[how-to-use-cloudflare-workers-ai]]
- [[how-to-engineer-prompts]]
- [[how-to-build-ai-agents]]
- [[how-to-evaluate-llm-models]]
