---
title: "database setup"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - vector-database
---

# database setup

> **Source:** local-ai-education-proagentworkflowsdatabase-setupmd-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/.agent/workflows/database-setup.md ingested: 2026-07-20 sha256: 9e62f45a343557c07326d1ccd8d0de3864fe140fa2a8ed40e40e334595cf1bf0 blog_source...
> **Sources:**
>   - local-ai-education-proagentworkflowsdatabase-setupmd-2026-07-20.md
> **Links:**
- [[add-lesson]]
- [[local-llm-wiki-повна-архітектурна-документація]]
- [[local-llm-wiki-agent-contract]]
- [[local-llm-wiki-algorithm]]
- [[grok-build-ios]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/.agent/workflows/database-setup.md
ingested: 2026-07-20
sha256: 9e62f45a343557c07326d1ccd8d0de3864fe140fa2a8ed40e40e334595cf1bf0
blog_source: local:unknown
---
---
description: Налаштування бази даних
---
Цей робочий процес описує процес ініціалізації бази даних.
1. Створіть нову базу даних у MySQL (наприклад, `ai_education`).
2. Імпортуйте файл `database.sql`:
- Через phpMyAdmin: оберіть БД -> "Import" -> виберіть `database.sql`.
- Через командний рядок:
```powershell
mysql -u username -p ai_education < database.sql
```
3. Оновіть параметри підключення в `api.php`:
- `$host`
- `$db_name`
- `$username`
- `$password`
4. Перевірте підключення, відкривши `api.php` у браузері (повинна повернутися JSON відповідь про помилку авторизації або успіх, якщо немає критичних помилок PHP).

## Summary

See Key Findings for full content.

## Related Articles

- [[add-lesson]]
- [[local-llm-wiki-повна-архітектурна-документація]]
- [[local-llm-wiki-agent-contract]]
- [[local-llm-wiki-algorithm]]
- [[grok-build-ios]]
