---
type: playbook
title: How to Use Hermes Agent
description: Practical guide for using Hermes Agent framework — setup, configuration, daily operations
tags: [hermes-agent, setup, configuration, workflow, tutorial]
sources: []
confidence: high
links: [hermes-agent, agentskills-io, honcho, atropos]
created: 2026-07-21
updated: 2026-07-21
---
# How to Use Hermes Agent

## Quick Start

### Installation

```bash
# Install via pip
pip install hermes-agent

# Or via npm (if available)
npm install -g hermes-agent
```

### Configuration

Create `~/.hermes/config.yaml`:

```yaml
# Backend selection
backend: docker  # local, docker, ssh, daytona, singularity, modal

# Model configuration
model:
  provider: openai  # or ollama, vllm, llama.cpp
  name: hermes-4-36b  # or any OpenAI-compatible endpoint
  
# Memory settings
memory:
  honcho_enabled: true
  fts5_enabled: true
  vector_store: true
  
# Skills
skills:
  auto_create: true  # enable autonomous skill creation
  agentskills_io: true  # enable cross-framework skills
  
# Messaging (optional)
messaging:
  telegram:
    enabled: false
    bot_token: "YOUR_BOT_TOKEN"
```

## Daily Operations

### Starting a Session

```bash
# CLI mode
hermes

# TUI mode (full terminal UI)
hermes --tui

# Specific profile
hermes -p my-profile
```

### Slash Commands

| Command | Description |
|---------|-------------|
| `/model <name>` | Switch model dynamically |
| `/skill` | List/manage skills |
| `/memory` | View/edit memory |
| `/background` | Spawn background session |
| `/goal <description>` | Set completion contract |
| `/learn` | Convert workflow to skill |
| `/journey` | Visualize agent's memory |

### Creating Skills

When agent completes a complex workflow (5+ tool calls), it can auto-create skills:

**Trigger conditions:**
1. **Complexity:** 5+ sequential tool calls
2. **Dead-end resolution:** Multiple failed approaches → one success
3. **Human correction:** User corrects agent's trajectory

**Skill structure:**
```
~/.hermes/skills/my-skill/
├── SKILL.md          # Main skill file
├── scripts/          # Optional scripts
├── references/       # Optional references
└── assets/           # Optional assets
```

## Advanced Usage

### Multi-Backend Setup

```yaml
# Switch backends with one line
backend: modal  # local, docker, ssh, daytona, singularity, modal
```

### Profile Isolation

```bash
# Create isolated profiles
hermes -p code-reviewer
hermes -p web-researcher
hermes -p infra-monitor
```

Each profile has:
- Separate `HERMES_HOME`
- Independent config files
- Isolated SQLite databases
- Separate skills and memory

### MCP Integration

```yaml
# Connect to MCP servers
mcp:
  servers:
    - name: filesystem
      command: npx
      args: [-y, "@modelcontextprotocol/server-filesystem", /path]
    - name: github
      command: npx
      args: [-y, "@modelcontextprotocol/server-github"]
```

### Cron Scheduling

```yaml
# Natural language cron
cron:
  jobs:
    - name: daily-digest
      schedule: "0 9 * * *"  # daily at 9am
      prompt: "Generate daily digest from log.md"
```

## Best Practices

### Skill Management

1. **Auto-create:** Let agent auto-create skills for complex workflows
2. **Manual review:** Review skills before they're committed
3. **Regular cleanup:** Remove stale skills periodically
4. **Cross-tool:** Write skills in agentskills.io format for portability

### Memory Management

1. **Honcho:** Keep messaging active — Honcho needs messages to reason
2. **FTS5:** Use for cross-session recall ("what did I do last Tuesday?")
3. **Skills:** Store procedural knowledge in SKILL.md files
4. **USER.md:** Maintain user preferences and patterns

### Security

1. **Docker backend:** Use for production/security-sensitive tasks
2. **Read-only FS:** Enable read-only root filesystem
3. **PID limits:** Set process ID limits
4. **Namespace isolation:** Use container namespaces

### Performance

1. **Context caching:** Stabilize prompts to reduce token burn by up to 95%
2. **Local models:** Use Ollama/vLLM for local inference
3. **Background sessions:** Use `/background` for long tasks
4. **Skill reuse:** Query skills instead of zero-shot reasoning

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Model not loading | Check `~/.hermes/config.yaml` provider settings |
| Skills not created | Verify `skills.auto_create: true` |
| Honcho not working | Ensure active messaging — Honcho needs messages |
| MCP not connecting | Check server command and args |
| Backend not switching | Verify backend is installed (e.g., Docker) |

### Getting Help

- **Docs:** https://hermes-agent.nousresearch.com/docs
- **GitHub:** https://github.com/NousResearch/hermes-agent
- **Community:** Telegram, Discord channels

## Related

- [[hermes-agent]]
- [[agentskills-io]]
- [[honcho]]
- [[atropos]]
- [[hermes-knowledge-storage]]
