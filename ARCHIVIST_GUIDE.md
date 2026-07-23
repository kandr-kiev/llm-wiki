---
title: Архітектурний протокол та керівництво оператора
type: reference
category: references
tags: [architecture, audit, archivist, guidelines, system-integrity]
created: 2026-07-23
updated: 2026-07-23
confidence: high
---

# 📘 ЛК "Архітектурний протокол та керівництво оператора" (LLM Wiki)

**Для кого:** Профіль "Архіваріус" та оператори системи.
**Мета:** Стандартизація процесів, усунення дублювання, підвищення якості даних та оптимізація графа знань.
**Статус:** Актуальний | **Останній аудит:** 2026-07-23

---

## 1. 🏗️ Архітектура системи (5 шарів)

Система LLM Wiki будується за принципом конвеєра даних. Кожен шар має чітку відповідальність.

| ШАРОК | КОМПОНЕНТИ | ВІДПОВІДАЛЬНІСТЬ |
|:---:|:---|:---|
| **1. Ingestion** | `source_monitor.py` (RSS+GitHub), `inbox_router.py` (/towiki) | Збір "сирого" контенту в `raw/articles/`. Дедуплікація (SHA256). |
| **2. Processing** | `integrator.py` | Трансформація `raw/` → `wiki/` (концепти, сутності, порівняння). |
| **3. Graph** | `wiki_graph_generator.py`, `graphify_bridge.py` | Побудова `graph.json` на основі wikilinks. Синхронізація графа з контентом. |
| **4. Quality** | `wiki_doctor.py`, `wiki_lint.py`, `fix_broken_wikilinks.py`, `tools/tag_sync.py` | Діагностика, фікс хешів, перевірка індексу, виправлення посилань, синхронізація тегів. |
| **5. Consumption** | `AGENTS.md` (Graph-First Protocol), `SCHEMA.md`, `tools/approved_tags.json` | Пошук контексту через BFS, формування відповідей. SCHEMA.md — єдине джерело істини для тегів та конвенцій. `tools/approved_tags.json` — JSON-файл з APPROVED_TAGS (завантажується tools/utils.py). |

---

## 2. ⚠️ Критичні проблеми (Audit Findings)

Під час аудит було виявлено 4 критичні дублі та 3 ризики якості.

### 🔴 Критичні дублі (Needing Immediate Removal)
Ці скрипти **застаріли** і їх функціонал повністю покритий `source_monitor.py` та `inbox_router.py`.

| Файл | Статус | Чому видаляти |
|:---|:---|:---|
| `rss_monitor.py` | ❌ Duplicated | `source_monitor.py` моніторить 27+ RSS фідів. |
| `github_monitor.py` | ❌ Duplicated | `source_monitor.py` моніторить GitHub Issues/PRs. |
| `github_release_monitor.py` | ❌ Duplicated | `source_monitor.py` моніторить GitHub Releases. |
| `local_file_monitor.py` | ❌ Duplicated | `inbox_router.py` класифікує та обробляє локальні файли краще. |

### 🟡 Ризики якості (Needs Attention)
1.  **Monolith Risk:** `integrator.py` (2365 рядків) та `wiki_doctor.py` (1023 рядки) — це "боги" коду. Будь-яка зміна може зламати іншу функцію.
2.  **Tag Drift:** `tools/utils.py` містить список `APPROVED_TAGS`, який може розійтись із `SCHEMA.md`. SCHEMA.md — єдине джерело істини. Синхронізація через `tag_sync.py`.
3.  **Orphan Nodes:** 1361 нод у графі не мають зв'язків (orphan). Це "мертві" сторінки, які знижують якість графа.

---

## 3. 🛠️ План дій (Action Plan)

### Фаза 1: Очищення (Clean-up)
1.  **Видалити:** `tools/rss_monitor.py`, `tools/github_monitor.py`, `tools/github_release_monitor.py`, `tools/local_file_monitor.py`.
2.  **Перевірити:** Переконайся, що `source_monitor.py` покриває всі фіді з видалених скриптів (порівняй списки RSS).
3.  **Оновити:** `index.md` — видалити посилання на видалені скрипти.

### Фаза 2: Стабілізація (Stabilization)
1.  **Tag Sync:** Запусти `python3 tools/tag_sync.py --check` для перевірки, `--apply` для синхронізації `APPROVED_TAGS` з `SCHEMA.md`.
2.  **Wiki Doctor Refactor:** Розбий `wiki_doctor.py` на менші модулі (diagnostics vs auto-fix).
3.  **Orphan Cleanup:** Запусти `wiki_doctor.py --diagnose`, щоб отримати список orphan-нод. Пройдись по них вручну та додай базові wikilinks.

### Фаза 3: Граф-Перший (Graph-First)
1.  **AGENTS.md:** Переконайся, що протокол "Graph-First" інжектується в SOUL.md кожного агента.
2.  **Cron:** Залишити `graphify-scan` (every 6h) та `weekly audit`.

---

## 4. 🔄 Регламент роботи (Standard Operating Procedures)

### 4.1. Інгест (Ingestion)
*   **RSS/GitHub:** Запускається автоматично (`source_monitor.py`). Результат — `raw/articles/`.
*   **Ручний завантажений файл:** Кинь у `/workspace/towiki/`. `inbox_router.py` перемістить його в `raw/` з frontmatter.
*   **Правило:** Ніколи не редагуй файли в `raw/` після інгесту. `raw/` — це Ground Truth.

### 4.2. Обробка (Processing)
1.  Перевір `raw/` на наявність нових файлів (`check_new_raw.py`).
2.  Запусти `integrator.py --dry-run` (перевірка).
3.  Запусти `integrator.py` (генерація wiki).
4.  Запусти `wiki_doctor.py --diagnose` (перевірка якості).

### 4.3. Запит (Querying)
**Завжди слідуй протоколу AGENTS.md:**
1.  Завантаж `graph.json`.
2.  Знайди seed-ноду (тема запиту).
3.  BFS(depth=2) → знайди community.
4.  Завантаж топ-5 wiki-сторінок.
5.  Синтезуй відповідь.
6.  *Fallback:* Якщо граф 0 results → `wiki/index.md`.

---

## 5. 📊 Ключові метрики (Current State)

*   **Wiki Pages:** 203 (OKF v0.1 compliant)
*   **Raw Articles:** 2053
*   **Graph Nodes:** 1485
*   **Graph Edges:** 6280
*   **Communities:** 16
*   **RSS Feeds:** 27 (моніторяться через `source_monitor.py`)
*   **GitHub Repos:** 15+ (моніторяться через `source_monitor.py`)
*   **Approved Tags:** 286 (SCHEMA.md ↔ approved_tags.json ↔ tools/utils.py)
*   **Orphan Nodes:** 1485 (потребують graphify bridge fix — Фаза 3)

---

## 6. 🚀 Найкращі практики (Best Practices)

1.  **Wiki Links:** Кожна сторінка wiki повинна мати мінімум 2 outbound wikilinks.
2.  **Tags:** Використовуй тільки затверджені теги з `SCHEMA.md` (root). Синхронізація з `tools/utils.py::APPROVED_TAGS` через `tag_sync.py`.
3.  **Frontmatter:** Кожна сторінка wiki має YAML frontmatter.
4.  **Index:** Кожна нова сторінка додається в `wiki/index.md`.
5.  **Log:** Кожна дія фіксується в `log.md`.
6.  **Graph:** Граф — це скелет. Wiki — це м'ясо. Без графа пошук сліпий.

---

**Документ підтримується в актуальному стані. Останній аудит: 2026-07-23.**
