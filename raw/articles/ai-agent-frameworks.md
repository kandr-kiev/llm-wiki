---
type: concept
title: AI Agent Frameworks
description: Software frameworks for building agentic AI systems: state machines (LangGraph), role-playing teams (CrewAI), and conversational agents (AutoGen).
created: 2026-07-06
updated: 2026-07-06
tags: [agent-workflow, architecture, automation]
sources: [raw/articles/ai-agent-frameworks-2026.md]
confidence: high
contested: false
links: [model-context-protocol, ai-coding-assistants, local-llm-hardware]
---
# AI Agent Frameworks

AI agent frameworks are software development kits (SDKs) that simplify building applications powered by LLMs. They provide structured approaches to creating "agents" — autonomous programs that can understand tasks, make decisions, and use tools to achieve goals.

## What Agent Frameworks Handle

- Reasoning loops (plan → execute → observe → adapt)
- Tool connections and API integrations
- State management across steps
- Error handling and recovery
- Multi-agent coordination

## Three Dominant Patterns (2026)

### 1. State Machine Model (LangChain / LangGraph)
Agent workflows modeled as graphs with nodes (functions), edges (transitions), and state schemas. Handles cycles naturally for retry, gather-more-info, and planning loops.

- **Best for:** Maximum control, production systems, complex workflows
- **Trade-off:** Steep learning curve, verbose for simple cases

### 2. Role-Playing Model (CrewAI)
Agents defined as team members with roles, goals, and backstories. Coordination via sequential or hierarchical (manager) patterns.

- **Best for:** Quick prototyping, intuitive team-based design
- **Trade-off:** Token cost (3-5x more), non-deterministic

### 3. Conversational Model (AutoGen)
Agents participate in group chats with defined speaking orders and termination conditions. Built-in code execution in sandbox.

- **Best for:** Multi-agent code execution, collaborative discussion patterns
- **Trade-off:** Microsoft ecosystem lock-in

## 2026 Landscape

| Framework | Latest (Feb/Mar 2026) | Key Feature |
|---|---|---|
| LangGraph | v0.3.x | PostgresSaver checkpointer, streaming tool outputs |
| CrewAI | v0.95 | Anthropic/Google tool-call routing, async crew runner |
| AutoGen | 1.0 GA | Event-driven architecture, v2 default API |
| Claude Agent SDK | Memory API beta | Built-in memory abstraction |
| OpenAI Agents SDK | Planning module | Structured planning workflows |

## Relationship to Other Concepts

- **MCP:** Agent frameworks can use MCP to expose tools and resources
- **AI Coding Assistants:** Tools like Cursor, Claude Code, and Devin are built on similar agent framework principles
- **Local LLM Hardware:** Frameworks running locally require appropriate GPU/CPU/RAM configuration

## Related Pages

- [[model-context-protocol]] — MCP as standard protocol for agent tool integration
- [[ai-coding-assistants]] — AI coding assistants as specialized agent applications
- [[local-llm-hardware]] — Hardware requirements for local agent inference
- [[llm-wiki]] — LLM Wiki as knowledge base for agent decision-making
