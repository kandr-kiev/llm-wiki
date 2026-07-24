---
title: "🧠 MCP від нуля до production"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - api
  - async
  - claude
  - data
  - foundation-model
  - library
  - llm
  - multi-agent
  - nlp
  - open-source
  - prompt-tuning
  - review
  - search
  - security
  - streaming
  - tool
---

# 🧠 MCP від нуля до production

> **Source:** local-ai-education-promcp-course-uamd-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/mcp-course-ua.md ingested: 2026-07-20 sha256: 5aade94757026e368934af12bcf743352082b84db23e55c2e3ec496048a7aca2 blog_source: local:unknown --...
> **Sources:**
>   - local-ai-education-promcp-course-uamd-2026-07-20.md
> **Links:**
- [[agent-skills-patterns]]
- [[add-lesson]]
- [[deploy]]
- [[how-to-integrate-mcp-step-by-step]]
- [[how-to-use-cloudflare-workers-ai]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/mcp-course-ua.md
ingested: 2026-07-20
sha256: 5aade94757026e368934af12bcf743352082b84db23e55c2e3ec496048a7aca2
blog_source: local:unknown
---
# 🧠 MCP від нуля до production
### 3-тижневий практичний курс для Python-розробника
> **Аудиторія:** Python-розробник із досвідом від 1 року, базовими знаннями async/await та REST API. 
> **Мета:** Самостійно проектувати, реалізовувати, захищати та публікувати MCP-сервери production-рівня. 
> **Формат:** Щодня ~90 хвилин теорії + практики. Pet-project на кожен тиждень.
---
## 📐 Архітектура курсу
```
Тиждень 1 → Фундамент (архітектура MCP, FastMCP, перший сервер)
Тиждень 2 → Безпека (OAuth 2.0, токени, авторизація)
Тиждень 3 → Production (тестування, observability, публікація)
```
---
# 📅 ТИЖДЕНЬ 1 — Архітектура MCP і перший сервер
## Концепція тижня
Model Context Protocol — це стандартизований протокол взаємодії між LLM-клієнтами (Claude, Cursor, etc.) та зовнішніми джерелами даних/інструментами. На відміну від прямих API-викликів, MCP надає уніфікований інтерфейс через три примітиви:
```
┌─────────────────────────────────────────────────────────┐
│ MCP Server │
│ │
│ ┌──────────┐ ┌──────────┐ ┌──────────────────┐ │
│ │Resources │ │ Tools │ │ Prompts │ │
│ │(read-only│ │(side │ │(reusable │ │
│ │ context) │ │ effects) │ │ templates) │ │
│ └──────────┘ └──────────┘ └──────────────────┘ │
└─────────────────────────────────────────────────────────┘
▲ ▲
│ JSON-RPC 2.0 │
MCP Client MCP Client
(Claude Desktop) (Cursor IDE)
```
### Три примітиви MCP
| Примітив | Призначення | Аналогія |
|----------|-------------|----------|
| **Resources** | Статичні або динамічні дані, доступні для читання | `GET /api/data` |
| **Tools** | Функції з побічними ефектами | `POST /api/action` |
| **Prompts** | Параметризовані шаблони для LLM | Jinja2-темплейти |
---
## День 1–2 — Теорія та середовище
### Що вивчаємо
- Специфікація MCP: transport layers (stdio, SSE, HTTP Streaming)
- Lifecycle: `initialize → capabilities negotiation → requests`
- Встановлення та структура проєкту
### Практика
```bash
# Створюємо віртуальне середовище
python -m venv .venv && source .venv/bin/activate
# Встановлюємо FastMCP
pip install fastmcp
# Перевіряємо
python -c "import fastmcp; print(fastmcp.__version__)"
```
```
mcp-course/
├── week1/
│ ├── server.py # Основний сервер
│ ├── resources/
│ │ └── files.py # Resource handlers
│ ├── tools/
│ │ └── actions.py # Tool handlers
│ ├── prompts/
│ │ └── templates.py # Prompt handlers
│ └── tests/
│ └── test_server.py
├── pyproject.toml
└── README.md
```
---
## День 3–4 — Resources та Tools
### Resources: read-only контекст
```python
# resources/files.py
from fastmcp import FastMCP
from pathlib import Path
mcp = FastMCP("file-explorer")
@mcp.resource("file://{path}")
async def read_file(path: str) -> str:
"""Читає файл та повертає його вміст як контекст для LLM."""
file_path = Path(path)
# ВАЖЛИВО: завжди валідуємо шлях
if not file_path.exists():
rais

## Summary

e FileNotFoundError(f"Файл не знайдено: {path}")
if not file_path.is_file():
raise ValueError(f"Шлях не є файлом: {path}")
# Захист від path traversal
resolved = file_path.resolve()
allowed_base = Path("/safe/data/dir").resolve()
if not str(resolved).startswith(str(allowed_base)):
raise PermissionError("Доступ поза дозволеною директорією заборонено")
return resolved.read_text(encoding="utf-8")
@mcp.resource("db://users/{user_id}")
async def get_user(user_id: int) -> dict:
"""Повертає дані користувача з БД."""
# Тут буде реальний запит до БД
return {"id": user_id, "name": "John Doe", "role": "admin"}
```
### Tools: дії зі побічними ефектами
```python
# tools/actions.py
from fastmcp import FastMCP
from pydantic import BaseModel, Field
import httpx
mcp = FastMCP("action-tools")
class CreateTaskInput(BaseModel):
title: str = Field(..., min_length=1, max_length=255, description="Назва задачі")
priority: int = Field(default=1, ge=1, le=5, description="Пріоритет від 1 до 5")
tags: list[str] = Field(default_factory=list)
@mcp.tool()
async def create_task(input: CreateTaskInput) -> dict:
"""
Створює нову задачу в системі управління проєктами.
Повертає ID створеної задачі та посилання на неї.
"""
# Pydantic автоматично валідує вхідні дані
async with httpx.AsyncClient() as client:
response = await client.post(
"https://api.example.com/tasks",
json=input.model_dump(),
timeout=10.0
)
response.raise_for_status()
return response.json()
@mcp.tool()
async def search_codebase(
query: str,
file_extension: str = ".py",
max_results: int = 10
) -> list[dict]:
"""Шукає в кодовій базі за запитом."""
# Проста реалізація grep-подібного пошуку
results = []
from pathlib import Path
import re
for filepath in Path(".").rglob(f"*{file_extension}"):
content = filepath.read_text(encoding="utf-8", errors="ignore")
if re.search(query, content, re.IGNORECASE):
lines = [
{"line": i + 1, "content": line}
for i, line in enumerate(content.splitlines())
if re.search(query, line, re.IGNORECASE)
]
results.append({"file": str(filepath), "matches": lines})
if len(results) >= max_results:
break
return results
```
---
## День 5 — Prompts
```python
# prompts/templates.py
from fastmcp import FastMCP
mcp = FastMCP("prompt-library")
@mcp.prompt()
def code_review(
code: str,
language: str = "python",
focus: str = "security"
) -> str:
"""
Генерує структурований промпт для code review.
LLM отримає готовий шаблон із підставленими параметрами.
"""
return f"""
Проведи детальний code review наступного {language}-коду з фокусом на {focus}.
## Код для аналізу
```{language}
{code}
```
## Що перевірити
1. **Безпека**: SQL-ін'єкції, XSS, CSRF, path traversal, незахищені secrets
2. **Продуктивність**: N+1 запити, відсутні індекси, витоки пам'яті
3. **Читабельність**: назви змінних, коментарі, структура
4. **Тестованість**: чи легко написати тести
## Формат відповіді
- 🔴 КРИТИЧНО: (блокери для production)
- 🟡 ВАЖЛИВО: (потрібно виправити до merge)
- 🟢 ПОРАДА: (рекомендації для покращення)
"""
@mcp.prompt()
def

## Related Articles

- [[agent-skills-patterns]]
- [[add-lesson]]
- [[deploy]]
- [[how-to-integrate-mcp-step-by-step]]
- [[how-to-use-cloudflare-workers-ai]]
