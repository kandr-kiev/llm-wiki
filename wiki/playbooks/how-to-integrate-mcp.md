---
type: playbook
title: "How to Integrate MCP — Step-by-Step"
description: Actionable runbook for implementing Model Context Protocol: build MCP servers, connect clients, and expose tools to AI applications
created: 2026-07-08
updated: 2026-07-08
tags: [playbook, mcp, reference, automation, configuration]
sources: [raw/articles/model-context-protocol-intro-architecture.md]
confidence: high
links: [model-context-protocol, ai-agent-frameworks, hermes-agent]
---

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
        "capabilities": {
            "elicitation": {}  # Client supports user interaction requests
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
            "tools": {"listChanged": True},  # Supports tools + notifications
            "resources": {}  # Also supports resources
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

## Phase 5: Client Primitives

### Step 5.1 — Sampling (request LLM completions)

```python
# Server requests LLM completion from client
@server.create_message()
async def create_message(messages: list[Message], max_tokens: int) -> SamplingMessage:
    """Server asks client to generate text using its LLM."""
    return await client.create_message(messages, max_tokens)
```

### Step 5.2 — Elicitation (request user input)

```python
@server.create_elicitation()
async def create_elicitation(
    action: str,
    description: str,
    user_input: dict | None
) -> ElicitationResult:
    """Server asks user for confirmation or additional info."""
    return await client.create_elicitation(action, description, user_input)
```

## Phase 6: Real-Time Notifications

### Step 6.1 — Tool list change notifications

```python
# Server sends notification when tools change
async def notify_tools_changed():
    await server.send_notification(
        "notifications/tools/list_changed",
        {}  # No params needed
    )
    # Client receives notification and refreshes tool list
```

### Step 6.2 — Notification checklist

- [ ] No `id` field (notifications don't expect response)
- [ ] Server declared `listChanged: True` in capabilities
- [ ] Client handles notification and refreshes registry
- [ ] Works for tools, resources, and prompts

## Phase 7: Transport Layer

### Step 7.1 — Stdio transport (local)

```python
# Server configuration for Claude Desktop
# ~/.config/claude-desktop/config.json or equivalent
{
    "mcpServers": {
        "my-server": {
            "command": "python",
            "args": ["/path/to/my_server.py"]
        }
    }
}
```

### Step 7.2 — Streamable HTTP transport (remote)

```python
# Server configuration for remote deployment
{
    "mcpServers": {
        "sentry-server": {
            "url": "https://mcp.sentry.io",
            "headers": {
                "Authorization": "Bearer YOUR_API_KEY"
            }
        }
    }
}
```

## Phase 8: Production Checklist

### Step 8.1 — Security

- [ ] API keys stored securely (not hardcoded)
- [ ] HTTP transport uses TLS/HTTPS
- [ ] OAuth tokens obtained via proper auth flow
- [ ] Tool input validation (JSON Schema enforced)
- [ ] Rate limiting on remote servers

### Step 8.2 — Monitoring

- [ ] Log all tool calls (name, arguments, result)
- [ ] Track latency per primitive type
- [ ] Monitor notification delivery success rate
- [ ] Alert on connection failures

### Step 8.3 — Testing

```bash
# Test with MCP Inspector
mcp-inspector python my_server.py

# Verify tool discovery
# 1. Check tools/list returns expected tools
# 2. Check tools/call executes correctly
# 3. Check resources/list and resources/read
# 4. Check prompts/list and prompts/get
# 5. Verify notifications fire when tools change
```

## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Connection fails | Protocol version mismatch | Check MCP spec version compatibility |
| Tools not showing | Server didn't declare tools capability | Verify `capabilities.tools` in init response |
| Tool call fails | Wrong argument types | Check JSON Schema matches actual input |
| No notifications | Server didn't declare `listChanged` | Add `"listChanged": True` to tools capability |
| HTTP auth fails | Wrong token format | Use `Bearer` prefix, verify OAuth flow |
| Stdio timeout | Server crashes on startup | Check stderr logs, verify Python/Node version |

## Key References

- `[[model-context-protocol]]` — MCP protocol overview
- `[[ai-agent-frameworks]]` — Frameworks that use MCP
- `[[model-context-protocol-intro-architecture]]` — Hermes Agent MCP integration
- [MCP Specification](https://modelcontextprotocol.io/specification/latest)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
