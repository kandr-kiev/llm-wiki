---
title: "БЕЗМЕЖЖЯ (BEZMEZHIA)"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - backend
  - data
  - llm
---

# БЕЗМЕЖЖЯ (BEZMEZHIA)

> **Source:** local-bezmezhzhiareadmemd-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/bezmezhzhia/README.md ingested: 2026-07-20 sha256: 3dd31d5359a61b369dfce5058d5f4d3d6be281842bafb8622de94f57f45da860 blog_source: local:unknown --- # БЕЗМЕЖЖЯ...
> **Sources:**
>   - local-bezmezhzhiareadmemd-2026-07-20.md
> **Links:**
- [[безмежжя-детальний-план-реалізації]]
- [[безмежжя-проектно-технічний-документ-v10]]
- [[безмежжя-глибокий-аналіз-та-альтернативна-версія]]
- [[глибокий-аудит-ігрового-дизайну-безмежжя-v60]]
- [[add-lesson]]

## Key Findings

---
source_url: file:///workspace/Projects/bezmezhzhia/README.md
ingested: 2026-07-20
sha256: 3dd31d5359a61b369dfce5058d5f4d3d6be281842bafb8622de94f57f45da860
blog_source: local:unknown
---
# БЕЗМЕЖЖЯ (BEZMEZHIA)
**Метафізична MMO-структура з процедурною генерацією квестів.**
Гравець — Могутня Сутність (М.С.) у симуляції. 4 риси, 4 способи бачення світу. 
Мета — баланс 25/25/25/25 (Просвітлення).
---
## Структура
```
bezmezhzhia/
├── src/
│ ├── core/ # Ядро гри
│ ├── cli/ # CLI-інтерфейс
│ ├── db/ # База даних
│ └── backend/ # Go-сервер (Фаза 2)
├── tests/ # Тести та симуляції
├── data/ # Шаблони квестів, візії
└── docs/ # Документація
```
## Швидкий старт
```bash
# Встановити залежності
pip install -r requirements.txt
# Запустити прототип
python -m src.cli
# Запустити симуляцію
python tests/simulation/run_simulation.py
```
## Етапи
1. **Прототип ядра** — CLI з балансом, квестами, Бардо
2. **Backend + DB** — Go + PostgreSQL + Redis
3. **Unity-клієнт** — графічний інтерфейс
4. **Розширення** — 22 шляхи, тіні, LLM-генерація
5. **Мультиплеєр** — Асинхронний (Ехо, Резонанс, Асоціативний)
6. **Продакшн** — K8s, Kafka, ClickHouse
## Документація
- [Глибокий аналіз](01_DEEP_ANALYSIS.md) — аудит + альтернативна версія
- [План реалізації](02_IMPLEMENTATION_PLAN.md) — етапи, архітектура, тести
## Ліцензія
MIT

## Summary

See Key Findings for full content.

## Related Articles

- [[безмежжя-детальний-план-реалізації]]
- [[безмежжя-проектно-технічний-документ-v10]]
- [[безмежжя-глибокий-аналіз-та-альтернативна-версія]]
- [[глибокий-аудит-ігрового-дизайну-безмежжя-v60]]
- [[add-lesson]]
