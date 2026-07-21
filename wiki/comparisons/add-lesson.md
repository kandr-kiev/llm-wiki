---
title: "add lesson"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - data
---

# add lesson

> **Source:** local-ai-education-proagentworkflowsadd-lessonmd-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/.agent/workflows/add-lesson.md ingested: 2026-07-20 sha256: fb05729c74d59f6b73c46ade934a1fb86a46695bcc967a8c3b2a767238a9b264 blog_source: lo...
> **Sources:**
>   - local-ai-education-proagentworkflowsadd-lessonmd-2026-07-20.md
> **Links:**
- [[Local LLM Wiki — Повна архітектурна документація]]
- [[grok build ios]]
- [[Local LLM Wiki Algorithm]]
- [[Аудит крон-завдань LLM Wiki — Детальний звіт]]
- [[Agent Skills Patterns]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/.agent/workflows/add-lesson.md
ingested: 2026-07-20
sha256: fb05729c74d59f6b73c46ade934a1fb86a46695bcc967a8c3b2a767238a9b264
blog_source: local:unknown
---
---
description: Додавання нового уроку до курсу
---
Цей робочий процес описує кроки для додавання нового уроку в навчальний план.
1. Відкрийте файл `assets/js/data/lessons.js`.
2. Додайте новий об'єкт до масиву `lessons`. Кожен об'єкт повинен мати таку структуру:
```javascript
{
id: number,
title: "Назва уроку",
content: "Теоретичний матеріал у форматі HTML",
quiz: [
{
question: "Питання?",
options: ["Варіант 1", "Варіант 2", "Варіант 3"],
correct: 0 // індекс правильної відповіді
}
]
}
```
3. Переконайтеся, що `id` є унікальним та йде послідовно.
4. Оновіть загальну кількість уроків у інтерфейсі, якщо це необхідно (зазвичай підтягується автоматично з довжини масиву).
5. Перевірте відображення нового уроку в `index2.html`.

## Summary

See Key Findings for full content.

## Related Articles

- [[Local LLM Wiki — Повна архітектурна документація]]
- [[grok build ios]]
- [[Local LLM Wiki Algorithm]]
- [[Аудит крон-завдань LLM Wiki — Детальний звіт]]
- [[Agent Skills Patterns]]
