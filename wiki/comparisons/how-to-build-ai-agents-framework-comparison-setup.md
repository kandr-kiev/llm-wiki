---
title: "How to Build AI Agents — Framework Comparison & Setup"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - analysis
  - api
  - architecture
  - async
  - automation
  - comparison
  - cost
  - docker
  - edge
  - evaluation
  - fine-tuning
  - foundation-model
  - framework
  - gpt
  - integration
  - llm
  - machine-learning
  - multi-agent
  - news
  - playbook
  - real-time
  - research
  - security
  - streaming
  - tool
  - use-case
  - workflow
---
# How to Build AI Agents — Framework Comparison & Setup

> **Source:** how-to-build-ai-agents.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- type: playbook title: "How to Build AI Agents — Framework Comparison & Setup" description: Actionable runbook for selecting and implementing AI agent frameworks: LangGraph, CrewAI, AutoGen, and ot...
> **Sources:**
>   - how-to-build-ai-agents.md
> **Links:**
- [[how-to-build-ai-agents]]
- [[ai-agent-frameworks]]
- [[ai-agent-frameworks-2026]]
- [[how-to-integrate-mcp]]
- [[how-to-choose-ai-coding-assistants]]

## Key Findings


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
# Build 

## Summary

graph
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
process=Process.sequential, # or Process.hierarchical
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
process=Process.hierarchical, # Manager delegates to workers
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
coder = Conversab

## Related Articles

- [[how-to-build-ai-agents]]
- [[ai-agent-frameworks]]
- [[ai-agent-frameworks-2026]]
- [[how-to-integrate-mcp]]
- [[how-to-choose-ai-coding-assistants]]
