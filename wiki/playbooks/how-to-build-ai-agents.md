---
type: playbook
title: "How to Build AI Agents — Framework Comparison & Setup"
description: Actionable runbook for selecting and implementing AI agent frameworks: LangGraph, CrewAI, AutoGen, and other 2026 frameworks
created: 2026-07-08
updated: 2026-07-08
tags: [playbook, agent-workflow, automation, reference, configuration]
sources: [raw/articles/ai-agent-frameworks-2026.md]
confidence: high
links: [ai-agent-frameworks, model-context-protocol, hermes-agent]
---

# How to Build AI Agents — Framework Comparison & Setup

Actionable runbook for selecting and implementing AI agent frameworks. Covers LangGraph, CrewAI, AutoGen, and the 2026 landscape.

## Prerequisites

- Python 3.10+
- API keys for target LLM (OpenAI, Anthropic, or local LLM)
- Understanding of agentic AI concepts (reasoning loops, tool use, state management)

## Phase 1: Framework Comparison Matrix

### Step 1.1 — Side-by-side comparison

| Criteria | LangGraph | CrewAI | AutoGen |
|---|---|---|---|
| **Architecture** | State machine (nodes, edges, cycles) | Role-playing (roles, goals, backstories) | Conversational (group chat, speaking orders) |
| **Control Level** | Maximum — explicit state management | Moderate — role-based delegation | High — group chat coordination |
| **Learning Curve** | Steep | Gentle | Moderate |
| **Token Cost** | Baseline | 3-5x more (multi-agent) | Baseline-Medium |
| **Determinism** | High (explicit state) | Low (non-deterministic) | Medium |
| **Production Ready** | Yes (persistence, streaming, HITL) | Prototyping | Yes (Docker sandbox) |
| **Ecosystem** | Massive (every provider, DB, tool) | Good defaults | Microsoft/Azure |
| **Multi-Agent** | Simple to complex | Built-in collaboration | Group chat patterns |

### Step 1.2 — Decision framework

```
Is your workflow complex with explicit state requirements?
  ├── YES → LangGraph
  └── NO
      Is your team non-technical or needs quick prototyping?
        ├── YES → CrewAI
        └── NO
            Do you need multi-agent code execution?
              ├── YES → AutoGen
              └── NO → LangGraph (maximum control)
```

## Phase 2: Setup LangGraph

### Step 2.1 — Install dependencies

```bash
pip install langgraph langchain langchain-openai
```

### Step 2.2 — Build a simple agent state machine

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

# Define agent state
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    tool_output: str
    iteration: int

# Define nodes
def research_node(state: AgentState) -> dict:
    """Research node: gather information."""
    return {
        "messages": [{"role": "assistant", "content": "Researching..."}],
        "iteration": state.get("iteration", 0) + 1
    }

def tool_node(state: AgentState) -> dict:
    """Tool execution node."""
    return {
        "tool_output": "Results from external API",
        "iteration": state.get("iteration", 0) + 1
    }

def analyze_node(state: AgentState) -> dict:
    """Analysis node: process results."""
    return {
        "messages": [{"role": "assistant", "content": "Analysis complete"}]
    }

# Build graph
workflow = StateGraph(AgentState)
workflow.add_node("research", research_node)
workflow.add_node("tool", tool_node)
workflow.add_node("analyze", analyze_node)

# Define edges
workflow.add_edge("research", "tool")
workflow.add_edge("tool", "analyze")
workflow.add_edge("analyze", END)

# Set entry point
workflow.set_entry_point("research")

# Compile with persistence
graph = workflow.compile(checkpointer=None)
```

### Step 2.3 — Add human-in-the-loop

```python
from langgraph.checkpoint.memory import MemorySaver

# Add persistence for human-in-the-loop
checkpointer = MemorySaver()
graph = workflow.compile(checkpointer=checkpointer)

# Run with interruption for human approval
config = {"configurable": {"thread_id": "agent-session-1"}}
result = graph.invoke({"messages": [{"role": "user", "content": "Research X"}]}, config=config)
```

### Step 2.4 — Add streaming

```python
# Stream tool outputs in real-time
for event in graph.stream({"messages": [{"role": "user", "content": "Research X"}]}, config):
    for node_name, node_output in event.items():
        print(f"[{node_name}] {node_output}")
```

## Phase 3: Setup CrewAI

### Step 3.1 — Install dependencies

```bash
pip install crewai crewai-tools
```

### Step 3.2 — Build a role-based agent team

```python
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Define agents with roles, goals, and backstories
researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments in AI",
    backstory="""You're an expert at finding and analyzing
    the latest AI research, news, and trends.""",
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role="Tech Content Strategist",
    goal="Craft compelling content on tech advancements",
    backstory="""You're a content strategist who creates
    engaging articles about AI and technology.""",
    verbose=True,
    allow_delegation=True
)

# Define tasks
research_task = Task(
    description="Research the latest developments in LLM fine-tuning",
    expected_output="A detailed report on fine-tuning techniques",
    agent=researcher
)

writing_task = Task(
    description="Write an engaging blog post about fine-tuning advances",
    expected_output="A 1000-word blog post with examples",
    agent=writer
)

# Create crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,  # or Process.hierarchical
    verbose=True
)

# Run
result = crew.kickoff()
print(result)
```

### Step 3.3 — Hierarchical crew (manager + workers)

```python
from crewai import Crew, Process

# Manager agent coordinates workers
crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.hierarchical,  # Manager delegates to workers
    verbose=True
)
```

## Phase 4: Setup AutoGen

### Step 4.1 — Install dependencies

```bash
pip install autogen-agentchat
```

### Step 4.2 — Build conversational agents

```python
from autogen import ConversableAgent, GroupChat, GroupChatManager

# Define agents
coder = ConversableAgent(
    name="Coder",
    system_message="You are a Python programmer. Write clean, tested code.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": "YOUR_KEY"}]}
)

reviewer = ConversableAgent(
    name="Reviewer",
    system_message="You are a code reviewer. Check for bugs, security, and style.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": "YOUR_KEY"}]}
)

# Human proxy for approval
human = ConversableAgent(
    name="Human",
    human_input_mode="ALWAYS",  # Always ask user
    llm_config=False
)

# Group chat with speaking orders
groupchat = GroupChat(
    agents=[coder, reviewer, human],
    messages=[],
    max_round=10
)

manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": [{"model": "gpt-4", "api_key": "YOUR_KEY"}]}
)

# Start conversation
coder.initiate_chat(
    manager,
    message="Write a function to sort a list using quicksort"
)
```

### Step 4.3 — Docker sandbox for code execution

```python
from autogen import CodeBlock

# AutoGen 1.0 has built-in Docker sandbox
# Configure code execution
executor = ConversableAgent(
    name="CodeExecutor",
    llm_config=False,
    code_execution_config={
        "work_dir": "coding",
        "use_docker": True  # Safe code execution
    }
)
```

## Phase 5: MCP Integration for Agents

### Step 5.1 — Connect agents to MCP tools

```python
# LangGraph + MCP integration
from mcp import ClientSession

async def mcp_tool_node(state: AgentState) -> dict:
    """Execute MCP tool from within LangGraph."""
    async with ClientSession() as session:
        await session.initialize()
        tools = await session.list_tools()
        # Use discovered tools
        result = await session.call_tool("search_database", {"query": "urgent"})
        return {"tool_output": result.content[0].text}
```

### Step 5.2 — Agent with MCP resources

```python
# Agent can access MCP resources as context
async def mcp_resource_node(state: AgentState) -> dict:
    """Fetch MCP resource for context."""
    async with ClientSession() as session:
        await session.initialize()
        schema = await session.read_resource("db://schema/users")
        return {"messages": [{"role": "assistant", "content": f"DB Schema: {schema}"}]}
```

## Phase 6: Evaluation & Production

### Step 6.1 — Agent evaluation checklist

| Check | Action |
|---|---|
| **Determinism** | Run same input 5 times — do outputs match? |
| **Token budget** | Track tokens per agent cycle |
| **Error handling** | Test with failed tool calls, timeouts |
| **Human oversight** | Verify HITL points work correctly |
| **Persistence** | Test checkpoint restore after crash |
| **Scaling** | Test with 10+ concurrent agent sessions |

### Step 6.2 — Monitoring

```python
# Track agent metrics
import time

start = time.time()
result = graph.invoke(input, config)
elapsed = time.time() - start

print(f"Agent cycle: {elapsed:.2f}s, tokens: {result.get('token_count', 'N/A')}")
```

## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Infinite loop | Cycle not handled in graph | Add max iteration check or break condition |
| High token cost | CrewAI multi-agent overhead | Switch to sequential, reduce agent count |
| Non-deterministic output | CrewAI with multiple agents | Add seed, use LangGraph for determinism |
| Tool call fails | Wrong MCP tool name | Verify tool name from `tools/list` response |
| State not persisting | No checkpointer configured | Add `MemorySaver()` or PostgresSaver |
| Docker sandbox fails | Docker daemon not running | Start Docker, verify permissions |

## Key References

- `[[ai-agent-frameworks]]` — Framework comparison catalog
- `[[model-context-protocol]]` — MCP for agent tool integration
- `[[model-context-protocol-intro-architecture]]` — Hermes Agent architecture
- LangGraph docs: https://langchain-ai.github.io/langgraph/
- CrewAI docs: https://docs.crewai.com/
- AutoGen docs: https://microsoft.github.io/autogen/
