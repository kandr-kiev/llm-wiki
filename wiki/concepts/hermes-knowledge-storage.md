---
type: concept
title: Hermes Knowledge Storage
description: State report of the Hermes Agent knowledge storage system including projects, skills, cron jobs, and cached data.
tags: [hermes, agent-workflow, architecture, knowledge-storage]
sources: []
confidence: high
links: [hermes-agent, honcho, agentskills-io]
created: 2026-07-04
updated: 2026-07-21
---
# Hermes Knowledge Storage — State Report (Updated 2026-07-21)

**Date:** 2026-07-04 → Updated 2026-07-21
**Author:** MONTY (Hermes Agent)
**Status:** Active

## Overview

This document records the current state of the Hermes Agent knowledge storage system, including all projects, skills, cron jobs, and cached data.

## Storage Structure

| Directory | Size | Purpose |
|-----------|------|---------|
| `/workspace` | 781 MB | Main project archive |
| `/root/.hermes/skills` | 45 MB | Skills (68 total, 4 built-in) |
| `/root/.hermes/cache` | 728 KB | Web pages, screenshots, documents |
| `/output` | 20 KB | Digest output (digest + scout) |

## Active Projects

### 1. `weather-digest-v2` — Weather & Space Digest

**Status:** Main active project, under active development.

**Structure:**
```
weather-digest-v2/
├── scout.py              ← Data collection (NOAA, Open-Meteo, air raid, news)
├── render_digest.py      ← Template-first renderer
├── validate_payload.py   ← JSON validator
├── scout.sh              ← Bash wrapper
├── digest-template.md    ← Template (43 placeholders)
├── digest_output.md      ← Final output (Markdown, ~5 KB, 143 lines)
├── scripts/              ← Duplicate/legacy versions
├── tests/                ← Location override tests
├── docs/                 ← Automation plan, requirements, status
└── .hermes/plans/        ← Refactor plan
```

**Current state:** 43 placeholders filled, 10/10 sections present.

### 2. `Projects/AI-Education-Pro` — AI for Everyday Life Course

**Status:** PHP8 + React (Vite) + PostgreSQL. 6 lessons with video, audio, and PDF materials.

**Structure:**
```
AI-Education-Pro/
├── index2.html           ← Landing page
├── api.php               ← API backend
├── database.sql          ← Database schema
├── client/               ← React frontend (Vite + TypeScript)
├── src/                  ← PHP modules (Auth, Config, Database, Progress)
├── data/1-6/             ← 6 lessons (PDF + MP4 + M4A)
├── tests/                ← PHPUnit tests
└── vendor/               ← Composer dependencies
```

### 3. `llm-wiki` — Karpathy's LLM Wiki

**Status:** Obsidian-compatible knowledge base.

```
llm-wiki/
├── .obsidian/            ← Obsidian config
├── ALGORITHM.md
├── ARCHITECTURE.md
├── wiki/
│   ├── comparisons/
│   ├── concepts/         ← LLM Wiki, MCP, OKF
│   ├── entities/
│   ├── queries/
│   └── sources/
├── raw/                  ← Articles, papers, transcripts
└── tools/                ← wiki_lint.py
```

### 4. `weather-digest-fix` — Legacy Fixes

**Status:** Archived copy, not actively used.

### 5. `digest-reference.md` — Reference Digest

**Status:** Example output reference (June 4, 2026).

## Skills Inventory (68 total, 13 categories)

### Built-in (4)

`computer-use`, `dogfood`, `template-first-rendering`, `yuanbao`

### Key Skills by Category

| Category | Notable Skills |
|----------|----------------|
| autonomous-ai-agents | claude-code, codex, hermes-agent, opencode |
| creative | architecture-diagram, ascii-art, baoyu-infographic, odesa-dialect, p5js, manim-video, sketch, songwriting-and-ai-music |
| data-science | jupyter-live-kernel |
| github | github-auth, github-code-review, github-pr-workflow, github-issues |
| mlops | huggingface-hub, llama-cpp, segment-anything-model, weights-and-biases |
| productivity | notion, google-workspace, ocr-and-documents, powerpoint, maps |
| research | arxiv, blogwatcher, llm-wiki, polymarket, weather-space-lunar-digest |
| software-development | hermes-agent-skill-authoring, modern-portfolio-generator, plan, TDD, systematic-debugging |
| testing | digest-qa-agent |

## Cron Jobs (1 active)

| Job ID | Name | Schedule | Status | Next Run |
|--------|------|----------|--------|----------|
| `40ad11075f68` | Daily Weather + Space + Lunar + News Digest | `0 8 * * *` (daily 08:00) | ✅ active | 2026-07-05 08:00 |

**Model:** `openrouter/google/gemini-2.5-pro` (custom:llama)

## Statistics

- **Total files:** ~1500+ (majority are `vendor/` in AI-Education-Pro)
- **Real source files (excluding vendor/):** ~80
- **Active projects:** 5
- **Skills:** 68
- **Cron jobs:** 1
- **Cache:** 728 KB (web pages, screenshots)

## Notes

- Default location: с. Крехаїв, Чернігівська область (50.9, 32.7, Europe/Kiev)
- Output path: `/output/digest_output.md`
- Template-first architecture: all layout changes via `digest-template.md` only
- Full Ukrainian localization for all sections
- No API keys, tokens, or secrets stored in this repository

## Updated 2026-07-21 — New Knowledge Added

Після оновлення знань про Hermes Agent (2026-07-21):

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Wiki pages about Hermes | 4 | **10** | +6 |
| Raw articles about Hermes | 4 | **6** | +2 |
| Concepts | 1 | **8** | +7 |
| Comparisons | 3 | **4** | +1 |
| GitHub stars (Hermes Agent) | unknown | **105,000+** | new |
| agentskills.io adopters | 0 | **11+** | new |
| Terminal backends | 0 | **6** | new |
| Memory layers | 0 | **5** | new |

**Нові концепції додані:**
- `hermes-agent.md` — comprehensive concept
- `nous-research.md` — lab behind Hermes
- `agentskills-io.md` — portable skill standard
- `atropos.md` — distributed RL framework
- `honcho.md` — entity-centric user modeling
- `hermes-agent-vs-openclaw-2026-07-21.md` — comparison
