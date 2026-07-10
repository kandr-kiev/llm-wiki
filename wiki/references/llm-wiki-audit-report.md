---
title: "Аудит LLM Wiki Системи"
type: reference
category: "system-audit"
tags: [llm-wiki, reference]
  - audit
  - system-integrity
  - wiki-maintenance
  - cron
  - scripts
  - integrator
  - monitors
created: 2026-07-10
status: completed

---
# Аудит LLM Wiki Системи

**Дата:** 2026-07-10
**Статус:** ✅ Завершено
**Огляд:** Повний аудит активних скриптів, цілісності wiki та cron-завдань.

---

## Фаза 1: Active Скрипти

### Знайдені проблеми та фікси

| Скрипт | Баг | Статус |
|--------|-----|--------|
| `integrator.py` | `/tmp/` → `.processed` | ✅ ВИПРАВЛЕНО |
| `github_release_monitor.py` | `/tmp/` → `.processed` | ✅ ВИПРАВЛЕНО |
| `local_file_monitor.py` | `/tmp/` → `.processed` | ✅ ВИПРАВЛЕНО |
| `local_monitor.py` | `/tmp/` → `.processed` | ✅ ВИПРАВЛЕНО |
| `github_monitor.py` | `/tmp/` → `.processed` | ✅ ВИПРАВЛЕНО |
| `wiki_lint.py` | Дублікат тегу `search` | ✅ ВИПРАВЛЕНО |

### Синтаксична валідація

| Скрипт | py_compile |
|--------|:----------:|
| `integrator.py` | ✅ 0 помилок |
| `rss_monitor.py` | ✅ 0 помилок |
| `github_release_monitor.py` | ✅ 0 помилок |
| `local_file_monitor.py` | ✅ 0 помилок |
| `local_monitor.py` | ✅ 0 помилок |
| `github_monitor.py` | ✅ 0 помилок |
| `wiki_lint.py` | ✅ 0 помилок |

---

## Фаза 2: Wiki Система

### Структура

| Категорія | Сторінок |
|-----------|:--------:|
| `wiki/comparisons/` | 78 |
| `wiki/concepts/` | 68 |
| `wiki/entities/` | 44 |
| `wiki/playbooks/` | 14 |
| `wiki/synthesis/` | 7 |
| `wiki/queries/` | 3 |
| `wiki/references/` | 1 |
| `wiki/templates/` | 8 |
| **Разом** | **222** |

### Цілісність

| Перевірка | Результат |
|-----------|-----------|
| Broken wikilinks | **0** ✅ |
| Missing sources | **0** ✅ |
| Missing frontmatter | **0** ✅ |
| Empty pages | **0** ✅ |
| SHA256 drift (88 raw sources) | **0** ✅ |
| APPROVED_TAGS дублікати | **1** → видалено ✅ |
| `index.md` цілісність | ✅ 222 записів |
| `.processed` файли | 1 (32 байта — порожній) |

---

## Фаза 3: Cron-завдання

### Аналіз prompt-ів

Усі 4 проблемні завдання виконують **простий запуск скриптів через terminal**:

| Завдання | Prompt | Навички потрібні? |
|----------|--------|:-----------------:|
| RSS Feed Monitor | `python3 tools/rss_monitor.py` | ❌ Ні |
| GitHub Release Monitor | `python3 tools/github_release_monitor.py` | ❌ Ні |
| Local File Monitor | `python3 tools/local_file_monitor.py` | ❌ Ні |
| Wiki Integrator | `python3 tools/integrator.py` | ❌ Ні |

### Фінальний стан

| Завдання | Модель | Навички | Розклад | Статус |
|----------|:------:|:-------:|--------|:------:|
| Wiki Raw Scanner | ✅ qwen3.6-35b | ✅ wiki-indexer, llm-wiki | every 360m | ⏸️ |
| Wiki Weekly Digest | ✅ qwen3.6-35b | ✅ llm-wiki, wiki-indexer | 0 9 * * 1 | ⏸️ |
| RSS Feed Monitor | ✅ qwen3.6-35b | — | 0 0,12 * * * | ⏸️ |
| GitHub Release Monitor | ✅ qwen3.6-35b | — | 0 2,14 * * * | ⏸️ |
| Local File Monitor | ✅ qwen3.6-35b | — | 0 4,16 * * * | ⏸️ |
| Wiki Integrator | ✅ qwen3.6-35b | — | 0 6,18 * * * | ⏸️ |

**Усі 6 завдань закріплені на `qwen3.6-35b-a3b` + `custom:llama-server`, залишаються на паузі.**

---

## Підсумок

| Фаза | Загальний статус |
|------|:----------------:|
| Фаза 1: Active скрипти | ✅ **6 багів виправлено** |
| Фаза 2: Wiki система | ✅ **1 дублікат виправлено, цілісність OK** |
| Фаза 3: Cron-завдання | ✅ **4 закріплено, всі на паузі** |

**Критичних проблем не виявлено.** Система готова до запуску.
