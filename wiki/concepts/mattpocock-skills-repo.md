---
title: Matt Pocock Skills Repo
type: concept
tags: [skills, agent-skills, engineering, productivity, claude-code, codex]
sources: [raw/articles/mattpocock-skills-readme.md, raw/articles/mattpocock-skills-all-skills.md]
confidence: high
links: [lukesdevlab-youtube-repo, llm-wiki, agent-skills-standard]
created: 2026-07-24
updated: 2026-07-24
description: Auto-filled by Wiki Doctor
---

# Matt Pocock Skills Repo

> **Джерело:** [github.com/mattpocock/skills](https://github.com/mattpocock/skills)
> **Опис:** 183k⭐ agent skills для реальних інженерів

## Визначення

Набір agent skills від Matt Pocock для Claude Code, Codex та інших AI-агентів. Skills орієнтовані на реальну інженерну практику, а не "vibe coding". Працюють з будь-якою моделлю.

## Ключові категорії

### Engineering Skills

| Skill | Опис |
|---|---|
| **tdd** | Test-driven development (red-green-refactor loop) |
| **domain-modeling** | Побудова та уточнення domain model |
| **codebase-design** | Дисципліна для дизайну deep modules |
| **code-review** | Two-axis review (Standards + Spec) |
| **resolving-merge-conflicts** | Розв'язання merge conflicts по hunk |
| **prototype** | Швидке прототипування |
| **research** | Інженерне дослідження |
| **triage** | Тріаж issue tracker |
| **to-spec** | Перетворення issue на spec |
| **to-tickets** | Перетворення spec на tickets |
| **improve-codebase-architecture** | Покращення архітектури |
| **wayfinder** | Навігація по кодовій базі |

### Productivity Skills

| Skill | Опис |
|---|---|
| **grill-me** | Інтерв'ю для уточнення плану/дизайну |
| **grill-with-docs** | Grill-me + CONTEXT.md + ADRs |
| **grilling** | Model-invoked grilling loop |
| **handoff** | Компактизація conversation для handoff |
| **teach** | Навчання нових навичок |
| **writing-great-skills** | Reference для writing skills |

### Personal Skills

| Skill | Опис |
|---|---|
| **obsidian-vault** | Obsidian vault management |
| **edit-article** | Редагування статей |

### Misc Skills

| Skill | Опис |
|---|---|
| **setup-pre-commit** | Setup pre-commit hooks |
| **scaffold-exercises** | Scaffold exercises |
| **migrate-to-shoehorn** | Migration to shoehorn |
| **git-guardrails-claude-code** | Git guardrails для Claude Code |

### In-Progress

- **writing-shape** — Writing shape
- **writing-fragments** — Writing fragments
- **writing-beats** — Writing beats
- **wizard** — Wizard
- **to-questionnaire** — To questionnaire
- **setup-ts-deep-modules** — TypeScript deep modules
- **loop-me** — Loop me
- **claude-handoff** — Claude handoff
- **batch-grill-me** — Batch grill me

## Філософія

### Problem 1: The Agent Didn't Do What I Want

**Рішення:** Grilling session — agent задає детальні питання перед початком роботи.

```markdown
# Grill Session
- Що будуємо?
- Які обмеження?
- Які компроміси?
- Як перевірити success?
```

### Problem 2: The Agent Is Way Too Verbose

**Рішення:** Shared language через CONTEXT.md та ADRs.

```markdown
# CONTEXT.md
- Domain language
- Key decisions
- Architecture choices
- Naming conventions
```

### Problem 3: The Code Doesn't Work

**Рішення:** TDD skill + feedback loops.

```markdown
# TDD Rules
1. Red → Green → Refactor
2. One seam per test
3. No implementation coupling
4. Vertical slices, not horizontal
```

### Problem 4: We Built A Ball Of Mud

**Рішення:** Domain modeling + codebase design disciplines.

## Установка

### Через skills.sh

```bash
npx skills@latest add mattpocock/skills
```

### Як Claude Code plugin

```bash
claude plugin marketplace add mattpocock/skills
claude plugin install mattpocock-skills@mattpocock
```

### Через /setup-matt-pocock-skills

```bash
/setup-matt-pocock-skills
# Вибираєш:
# 1. Issue tracker (GitHub, Linear, local files)
# 2. Labels для triage
# 3. Path для збереження docs
```

## Зв'язки

- **lukesdevlab-youtube-repo** — репозиторій з промптами та конфігами
- **llm-wiki** — LLM Wiki для knowledge management
- **agent-skills-standard** — стандарт для agent skills

## Джерела

- [mattpocock/skills](https://github.com/mattpocock/skills) — GitHub репозиторій
- [skills.sh](https://skills.sh/mattpocock/skills) — Skills installer
- [README.md](raw/articles/mattpocock-skills-readme.md) — README репозиторію
- [All SKILL.md](raw/articles/mattpocock-skills-all-skills.md) — Всі skills файли

## Citations

[1] https://github.com/mattpocock/skills
[2] https://skills.sh/mattpocock/skills
[3] https://www.aihero.dev/s/skills-newsletter
