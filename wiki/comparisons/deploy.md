---
title: "deploy"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - gemini
  - vector-database
---

# deploy

> **Source:** local-ai-education-proagentworkflowsdeploymd-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/.agent/workflows/deploy.md ingested: 2026-07-20 sha256: a42fbd392a022759c9c70056b90ff47795ecf8fb685d1d3805c56ef8d4618ba6 blog_source: local:...
> **Sources:**
>   - local-ai-education-proagentworkflowsdeploymd-2026-07-20.md
> **Links:**
- [[database setup]]
- [[add lesson]]
- [[Local LLM Wiki — Повна архітектурна документація]]
- [[Інтеграція Graphify з LLM-WIKI: стратегія, теорія, техніка, рекомендації]]
- [[Agent Skills Patterns]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/.agent/workflows/deploy.md
ingested: 2026-07-20
sha256: a42fbd392a022759c9c70056b90ff47795ecf8fb685d1d3805c56ef8d4618ba6
blog_source: local:unknown
---
---
description: Деплой на хостинг
---
Цей робочий процес описує кроки для завантаження проекту на живий хостинг (наприклад, InfinityFree).
1. Підготуйте файли:
- Переконайтеся, що `config.js` містить правильний API ключ для Gemini (якщо він не прихований на бекенді).
- Перевірте `smtp_config.php` на наявність правильних налаштувань пошти.
- Налаштуйте `api.php` для продакшн бази даних.
2. Завантажте файли через FTP:
- Використовуйте FileZilla або аналогічний клієнт.
- Завантажте вміст папки проекту в `htdocs` або відповідну директорію.
3. Налаштуйте базу даних на хостингу:
- Створіть БД через панель керування хостингом.
- Імпортуйте `database.sql`.
4. Перевірте працездатність:
- Відкрийте URL вашого сайту.
- Спробуйте зареєструватися та пройти тест, щоб перевірити зв'язок з БД та Email.

## Summary

See Key Findings for full content.

## Related Articles

- [[database setup]]
- [[add lesson]]
- [[Local LLM Wiki — Повна архітектурна документація]]
- [[Інтеграція Graphify з LLM-WIKI: стратегія, теорія, техніка, рекомендації]]
- [[Agent Skills Patterns]]
