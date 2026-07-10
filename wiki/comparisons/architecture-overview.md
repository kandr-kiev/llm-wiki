---
title: "Architecture overview"
type: comparison
tags: [architecture, comparison]
description: Comparison page for Architecture overview

sources: []
links: []
description: Comparison page for Architecture overview

links: []
confidence: medium
created: 2026-07-08
updated: 2026-07-08
contested: false

---
# Architecture overview

> **Source:** model-context-protocol-intro-architecture.md
> **Type:** comparison
> **Created:** 2026-07-08

## Key Findings

---
source_url: https://modelcontextprotocol.io/docs/getting-started/intro
ingested: 2026-07-04
sha256: 55dbd0cbbe61a5d02aa850ca11d907ae68c99b52c0e39752aabb51d7d058e798
---
> ## Documentation Index
>
> Fetch the complete documentation index at: 
>
> Use this file to discover all available pages before exploring further.
[Model Context Protocol home page![light logo](https://mintcdn.com/mcp/2BMHnlNW5OqOohXZ/logo/light.svg?fit=max&auto=format&n=2BMHnlNW5OqOohXZ&q=85&s=a5ac61ce77858fb1ddaf6de761c39499)![dark logo](https://mintcdn.com/mcp/2BMHnlNW5OqOohXZ/logo/dark.svg?fit=max&auto=format&n=2BMHnlNW5OqOohXZ&q=85&s=1227cb7feb8344f9f6288c6b5b0a6d80)](/)
[Documentation](/docs/getting-started/intro)[Extensions](/extensions/overview)[Specification](/specification/2025-11-25)[Registry](/registry/about)[SEPs](/seps)[Community](/community/contributing)
About MCP
# Architecture overview
This overview of the Model Context Protocol (MCP) discusses its [scope](#scope) and [core concepts](#concepts-of-mcp), and provides an [example](#example) demonstrating each core concept. Because MCP SDKs abstract away many concerns, most developers will likely find the [data layer protocol](#data-layer-protocol) section to be the most useful. It discusses how MCP servers can provide context to an AI application. For specific implementation details, please refer to the documentation for your [language-specific SDK](/docs/sdk).
## [​](#scope) Scope
The Model Context Protocol includes the following projects:
* [MCP Specification](https://modelcontextprotocol.io/specification/latest): A specification of MCP that outlines the implementation requirements for clients and servers.
* [MCP SDKs](/docs/sdk): SDKs for different programming languages that implement MCP.
* **MCP Development Tools**: Tools for developing MCP servers and clients, including the [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
* [MCP Reference Server Implementations](https://github.com/modelcontextprotocol/servers): Reference implementations of MCP servers.
MCP focuses solely on the protocol for context exchange—it does not dictate how AI applications use LLMs or manage the provided context.
## [​](#concepts-of-mcp) Concepts of MCP
### [​](#participants) Participants
MCP follows a client-server architecture where an MCP host — an AI application like [Claude Code](https://www.anthropic.com/claude-code) or [Claude Desktop](https://www.claude.ai/download) — establishes connections to one or more MCP servers. The MCP host accomplishes this by creating one MCP client for each MCP server. Each MCP client maintains a dedicated connection with its corresponding MCP server. Local MCP servers that use the STDIO transport typically serve a single MCP client, whereas remote MCP servers that use the Streamable HTTP transport will typically serve many MCP clients. The key participants in the MCP architecture are:
* **MCP Host**: The AI application that coordinates and manages one or multiple MCP clients
* 

## Summary

**MCP Client**: A component that maintains a connection to an MCP server and obtains context from an MCP server for the MCP host to use
* **MCP Server**: A program that provides context to MCP clients
**For example**: Visual Studio Code acts as an MCP host. When Visual Studio Code establishes a connection to an MCP server, such as the [Sentry MCP server](https://docs.sentry.io/product/sentry-mcp/), the Visual Studio Code runtime instantiates an MCP client object that maintains the connection to the Sentry MCP server. When Visual Studio Code subsequently connects to another MCP server, such as the [local filesystem server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem), the Visual Studio Code runtime instantiates an additional MCP client object to maintain this connection. Note that **MCP server** refers to the program that serves context data, regardless of where it runs. MCP servers can execute locally or remotely. For example, when Claude Desktop launches the [filesystem server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem), the server runs locally on the same machine because it uses the STDIO transport. This is commonly referred to as a “local” MCP server. The official [Sentry MCP server](https://docs.sentry.io/product/sentry-mcp/) runs on the Sentry platform, and uses the Streamable HTTP transport. This is commonly referred to as a “remote” MCP server.
### [​](#layers) Layers
MCP consists of two layers:
* **Data layer**: Defines the JSON-RPC based protocol for client-server communication, including lifecycle management, and core primitives, such as tools, resources, prompts and notifications.
* **Transport layer**: Defines the communication mechanisms and channels that enable data exchange between clients and servers, including transport-specific connection establishment, message framing, and authorization.
Conceptually the data layer is the inner layer, while the transport layer is the outer layer.
#### [​](#data-layer) Data layer
The data layer implements a [JSON-RPC 2.0](https://www.jsonrpc.org/) based exchange protocol that defines the message structure and semantics. This layer includes:
* **Lifecycle management**: Handles connection initialization, capability negotiation, and connection termination between clients and servers
* **Server features**: Enables servers to provide core functionality including tools for AI actions, resources for context data, and prompts for interaction templates from and to the client
* **Client features**: Enables servers to ask the client to sample from the host LLM, elicit input from the user, and log messages to the client
* **Utility features**: Supports additional capabilities like notifications for real-time updates and progress tracking for long-running operations
#### [​](#transport-layer) Transport layer
The transport layer manages communication channels and authentication between clients and servers. It handles connection establishment, message

## Related Articles

- 
- [[how-to-engineer-prompts]]
- [[how-to-use-cloudflare-workers-ai]]
- [[ai-agent-frameworks]]
- [[applying-massive-language-models-in-the-real-world-with-cohere-2026-07-07]]
