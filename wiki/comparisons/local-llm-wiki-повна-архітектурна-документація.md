---
title: "Local LLM Wiki — Повна архітектурна документація"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - architecture
  - integration
  - llama
  - llm
  - open-source
  - pytorch
  - rag
  - synthesis
---
# Local LLM Wiki — Повна архітектурна документація

> **Source:** architecture-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: local:///workspace/llm-wiki/docs/ARCHITECTURE.md ingested: 2026-07-10 sha256: 4857bd2bc8041d1a7b683dc17d187474a7b111115f1c39f7168dbafc8725afb9 blog_source: local --- # Local LLM Wiki —...
> **Sources:**
>   - architecture-2026-07-10.md
> **Links:**
- [[local-llm-wiki-algorithm]]
- [[local-llm-wiki-agent-contract]]
- [[llm-wiki-audit-report]]
- [[how-to-maintain-wiki-integrity]]
- [[hermes-knowledge-storage]]

## Key Findings

---
source_url: local:///workspace/llm-wiki/docs/ARCHITECTURE.md
ingested: 2026-07-10
sha256: 4857bd2bc8041d1a7b683dc17d187474a7b111115f1c39f7168dbafc8725afb9
blog_source: local
---
# Local LLM Wiki — Повна архітектурна документація
> **Дата останнього оновлення:** 2026-07-09
> **Версія системи:** 4.0.0
> **Статус:** Production
---
## Зміст
1. [Термінологічна база](#1-термінологічна-база)
2. [Загальна архітектура](#2-загальна-архітектура)
3. [Скрипти інфраструктури](#3-скрипти-інфраструктури)
4. [Діаграма зв'язків між компонентами](#4-діаграма-звязків-між-компонентами)
5. [Неявні припущення та архітектурні рішення](#5-неявні-припущення-та-архітектурні-рішення)
6. [Поточна статистика системи](#6-поточна-статистика-системи)
---
## 1. Термінологічна база
| Термін | Визначення | Приклад використання |
|--------|-----------|---------------------|
| **Сканування** (Scan) | Процес виявлення нових джерел у вхідних директоріях (`raw/`) | RSS-сканування, моніторинг файлів |
| **Інтеграція** (Integration) | Автоматичне перетворення сирого джерела на сторінку вікі з класифікацією та тегуванням | Запуск `integrator.py` |
| **Лінтинг** (Linting) | Перевірка структурної цілісності вікі: frontmatter, брукен-лінки, SHA256-дрейф | Запуск `wiki_lint.py` |
| **Сире джерело** (Raw source) | Необроблений контент, збережений як доказ — неизмінний після інгестації | `raw/articles/filename.md` |
| **Синтез** (Synthesis) | Сторінка вікі, створена на основі аналізу сирого джерела | `wiki/concepts/*.md` |
| **Frontmatter** | YAML-блок на початку файлу з метаданими (тип, теги, дати, джерела) | `---\ntype: concept\n---` |
| **Вікілінк** (Wikilink) | Посилання на іншу сторінку вікі у форматі `[[slug]]` | `[[karpathy-llm-wiki-2026]]` |
| **SHA256-дрейф** | Розбіжність між обчисленим хешем тіла файлу та збереженим хешем | `sha256: abc123...` ≠ обчислений |
| **Tag map** | Мапінг тегів → назви сторінок, використовується для пошуку зв'язків | `{"llm-wiki": ["llm-wiki.md", "rag.md"]}` |
| **Processed tracker** | База даних, що відслідковує, які raw-файли вже інтегровані | `/tmp/llm-wiki-rss.db` |
| **Index** | Каталог-навігація, що містить усі сторінки вікі з категорізацією | `wiki/index.md` |
| **Log** | Журнал дій append-only, фіксує всі операції | `log.md` |
---
## 2. Загальна архітектура
### 2.1 Тришарова модель
```
┌─────────────────────────────────────────────────────────────────────┐
│ ШАР 1: СИРІ ДЖЕРЕЛА (Immutable) │
│ raw/articles/ raw/papers/ raw/transcripts/ raw/assets/ │
│ → Ніколи не редагуються після збереження │
└─────────────────────────────────────────────────────────────────────┘
↓ сканування
┌─────────────────────────────────────────────────────────────────────┐
│ ШАР 2: СИНТЕЗ (Mutable) │
│ wiki/concepts/ wiki/entities/ wiki/comparisons/ │
│ wiki/playbooks/ wiki/synthesis/ wiki/queries/ │
│ wiki/references/ wiki/templates/ │
│ → Редагуються агентами на основі сирого шару │
└─────────────────────────────────────────────────────────────────────┘
↓ лінтинг
┌────────────────────

## Summary

─────────────────────────────────────────────────┐
│ ШАР 3: ОПЕРАЦІЇ (Tooling) │
│ SCHEMA.md ARCHITECTURE.md ALGORITHM.md AGENT.md │
│ tools/ index.md log.md │
│ → Керують процесом, визначають правила │
└─────────────────────────────────────────────────────────────────────┘
```
### 2.2 Потоки даних
```
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ External │ │ RSS/File/ │ │ Integrator │ │ Wiki Pages │
│ Sources │───▶│ GitHub │───▶│ (auto) │───▶│ (wiki/) │
│ (URL, PDF, │ │ Monitor │ │ │ │ │
│ paste) │ │ (cron) │ │ │ │ │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
│
├─ index.md (оновлення)
├─ log.md (запис)
└─ processed.db (трекинг)
```
---
## 3. Скрипти інфраструктури
### 3.6 `tools/github_monitor.py` — Моніторинг GitHub репозиторіїв
**Роль:** Відслідковування нових релізів та тегів у ключових AI/LLM репозиторіях через GitHub REST API.
**Алгоритм виконання:**
```
1. ІНІЦІАЛІЗАЦІЯ
├─ Завантажити REPOS (7 репозиторіїв: HuggingFace, PyTorch, LangChain, vLLM, Ollama, llama.cpp, Cloudflare, OpenAI, Anthropic)
├─ Завантажити RAW_DIR (raw/articles/), LOG_FILE (log.md), DB_FILE (.processed/github_tags.txt)
2. SCAN_REPO(repo_name, api_url)
│
├─ 2.1. GET api_url/releases (або /tags)
├─ 2.2. Для кожного release/tag:
│ ├─ tag = release.tag_name
│ ├─ is_new_release(tag)? → Перевірка DB_FILE
│ ├─ Ні → skip
│ └─ Так:
│ ├─ Download release notes
│ ├─ convert_html_to_markdown()
│ ├─ compute_sha256(content)
│ ├─ Write raw file → raw/articles/
│ ├─ Append to log.md
│ └─ Save tag to DB_FILE
└─ Повернути {new_releases, skipped}
```
**Ключові особливості:**
- Моніторить 7+ ключових AI/LLM репозиторіїв
- Використовує GitHub REST API без токену (60 req/h limit)
- SQLite-free: простий текстовий DB для теґів
- Автоматична конвертація HTML → Markdown
### 3.7 `tools/local_monitor.py` — Моніторинг локальних директорій
**Роль:** Відслідковування нових та змінених файлів у локальних директоріях користувача.
**Алгоритм виконання:**
```
1. ІНІЦІАЛІЗАЦІЯ
├─ Завантажити MONITORED_DIRS (workspace, /workspace/projects)
├─ Завантажити DB_FILE (.processed/local_hashes.txt)
2. SCAN_DIR(directory)
│
├─ 2.1. Пройтись по всіх *.md файлах
├─ 2.2. Compute SHA256(file_content)
├─ 2.3. Перевірити DB_FILE:
│ ├─ Немає → new_file
│ ├─ Є, hash збігається → skip
│ └─ Є, hash не збігається → modified
├─ 2.4. Оновити DB_FILE
└─ Повернути {new_files, modified, skipped}
```
**Ключові особливості:**
- Хешує вміст файлу (не metadata)
- Крос-платформений polling-підхід
- Налаштовувані MONITORED_DIRS
### 3.8 `tools/check_new_raw.py` — Перевірка нових raw-файлів
**Роль:** Порівняння raw/ директорії з wiki/sources/ для виявлення необроблених джерел.
**Алгоритм виконання:**
```
1. SCAN raw/**/*.md → raw_files set
2. SCAN wiki/sources/**/*.md → wiki_files set
3. new_raw = raw_files - wiki_files
4. Для кожного raw_file:
├─ compute_correct_sha256(raw_file)
├─ Порівняти зі stored sha256 у frontmatter
└─ Flag MISMATCH якщо розбіжність
5. Повернути report: {new_raw, h

## Related Articles

- [[local-llm-wiki-algorithm]]
- [[local-llm-wiki-agent-contract]]
- [[llm-wiki-audit-report]]
- [[how-to-maintain-wiki-integrity]]
- [[hermes-knowledge-storage]]
