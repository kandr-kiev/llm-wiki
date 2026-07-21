# Local LLM Wiki — Повна архітектурна документація

> **Дата останнього оновлення:** 2026-07-14
> **Версія системи:** 7.0.0
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
| **Вікілінк** (Wikilink) | Посилання на іншу сторінку вікі у форматі `[[slug]]` | `[[llm-wiki]]` |
| **SHA256-дрейф** | Розбіжність між обчисленим хешем тіла файлу та збереженим хешем | `sha256: abc123...` ≠ обчислений |
| **Tag map** | Мапінг тегів → назви сторінок, використовується для пошуку зв'язків | `{"llm-wiki": ["llm-wiki.md", "rag.md"]}` |
| **Processed tracker** | База даних, що відслідковує, які raw-файли вже інтегровані | `/tmp/llm-wiki-rss.db` |
| **Central utilities** | Модуль `utils.py` — єдине джерело правди для хешування, frontmatter, тегів та статусів | `tools/utils.py` |
| **Index** | Каталог-навігація, що містить усі сторінки вікі з категорізацією | `wiki/index.md` |
| **Log** | Журнал дій append-only, фіксує всі операції | `log.md` |

---

## 2. Загальна архітектура

### 2.1 Тришарова модель

```
┌─────────────────────────────────────────────────────────────────────┐
│                 ШАР 1: СИРІ ДЖЕРЕЛА (Immutable)                     │
│  raw/articles/  raw/papers/  raw/transcripts/  raw/assets/          │
│  → Ніколи не редагуються після збереження                            │
└─────────────────────────────────────────────────────────────────────┘
                              ↓ сканування
┌─────────────────────────────────────────────────────────────────────┐
│               ШАР 1.5: ПРОМІЖНИЙ КЕШ (.processed/)                   │
│  HTML→MD конверсія, 14 файлів, НЕ в git                             │
│  → Проміжна ланка між raw/ і wiki/                                   │
└─────────────────────────────────────────────────────────────────────┘
                              ↓ інтеграція
┌─────────────────────────────────────────────────────────────────────┐
│                    ШАР 2: СИНТЕЗ (Mutable)                           │
│  wiki/concepts/  wiki/entities/  wiki/comparisons/                   │
│  wiki/playbooks/  wiki/synthesis/  wiki/queries/                     │
│  wiki/references/  wiki/templates/                                   │
│  → Редагуються агентами на основі сирого шару                        │
└─────────────────────────────────────────────────────────────────────┘
                              ↓ лінтинг
┌─────────────────────────────────────────────────────────────────────┐
│                    ШАР 3: ОПЕРАЦІЇ (Tooling)                         │
│  SCHEMA.md  ARCHITECTURE.md  ALGORITHM.md  AGENT.md                  │
│  tools/  index.md  log.md                                            │
│  → Керують процесом, визначають правила                              │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Потоки даних

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  External    │    │  RSS/File/   │    │  Integrator  │    │  Wiki Pages  │
│  Sources     │───▶│  GitHub      │───▶│  (auto)      │───▶│  (wiki/)     │
│  (URL, PDF,  │    │  Monitor     │    │              │    │              │
│   paste)     │    │  (cron)      │    │              │    │              │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
                                                        │
                                                        ├─ index.md (оновлення)
                                                        ├─ log.md (запис)
                                                        └─ processed.db (трекинг)
```

---

## 3. Скрипти інфраструктури

### 3.1 `tools/utils.py` — Центральна бібліотека утиліт

**Роль:** Єдине джерело правди для хешування, frontmatter, тегів та статусів. Усі інструменти залежать від цього модулю.

**Ключові функції:**

| Функція | Призначення | Повертає |
|---------|-------------|----------|
| `split_frontmatter(content)` | Парсинг frontmatter (find-based) | `{fm, body, raw}` |
| `compute_sha256(content)` | Хешування тіла файлу (NO .strip()) | hex digest |
| `parse_simple_yaml(fm_text)` | Парсинг YAML frontmatter | dict |
| `verify_file_hash(filepath)` | Перевірка хешу одного файлу | `{status, stored, computed}` |
| `check_raw_integrity(raw_dir)` | Сканування raw/ → звіт | `{total, ok, mismatch, no_hash, no_fm}` |
| `fix_file_hash(filepath)` | Оновлення хешу у frontmatter | bool |
| `build_frontmatter(data)` | Генератор frontmatter для нових файлів | YAML string |
| `slugify(text)` | Уніфікована генерація slug | string |
| `APPROVED_TAGS` | Словник валідних тегів (262 шт.) | dict |
| `print_status(status, msg)` | Канонічний формат статусу для cron | — |

**Ключові особливості:**
- `compute_sha256()` НЕ виконує `.strip()` — байтова точність
- `rglob('**/*.md')` — рекурсивне сканування піддиректорій
- `os.path.isdir()` перед скануванням — resilient до відсутніх директорій
- `APPROVED_TAGS` — єдине джерело тегів (замість дублювання в `wiki_lint.py` та `integrator.py`)
- `build_frontmatter()` — fallback-логіка для GitHub-релізів

### 3.2 `tools/github_monitor.py` — Моніторинг GitHub репозиторіїв

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
   │   ├─ tag = release.tag_name
   │   ├─ is_new_release(tag)? → Перевірка DB_FILE
   │   ├─ Ні → skip
   │   └─ Так:
   │       ├─ Download release notes
   │       ├─ convert_html_to_markdown()
   │       ├─ compute_sha256(content)
   │       ├─ Write raw file → raw/articles/
   │       ├─ Append to log.md
   │       └─ Save tag to DB_FILE
   └─ Повернути {new_releases, skipped}
```

**Ключові особливості:**
- Моніторить 7+ ключових AI/LLM репозиторіїв
- Використовує GitHub REST API без токену (60 req/h limit)
- SQLite-free: простий текстовий DB для теґів
- Автоматична конвертація HTML → Markdown

### 3.3 `tools/local_monitor.py` — Моніторинг локальних директорій

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
   │   ├─ Немає → new_file
   │   ├─ Є, hash збігається → skip
   │   └─ Є, hash не збігається → modified
   ├─ 2.4. Оновити DB_FILE
   └─ Повернути {new_files, modified, skipped}
```

**Ключові особливості:**
- Хешує вміст файлу (не metadata)
- Крос-платформений polling-підхід
- Налаштовувані MONITORED_DIRS

### 3.4 `tools/check_new_raw.py` — Перевірка нових raw-файлів

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
5. Повернути report: {new_raw, hash_mismatches}
```

### 3.5 `tools/cleanup_duplicates.py` — Видалення дублікатів

**Роль:** Знаходження та видалення дублікатів wiki-сторінок з суфіксами `_1`, `_2`, `_3`, `_4`.

**Алгоритм виконання:**

```
1. SCAN wiki/**/*.md → згрупувати по base name
2. Для кожної групи:
   ├─ Якщо base version існує → delete all _N versions
   ├─ Якщо base version НЕ існує → rename highest _N to base, delete rest
3. Dry-run за замовчуванням
4. --apply для фактичного видалення/перейменування
```

### 3.6 `tools/promote_fallback_to_base.py` — Промоція fallback у base

**Роль:** Промоція `_1`, `_2`, `_3`, `_4` файлів у базові версії коли base не існує.

**Алгоритм виконання:**

```
1. SCAN wiki/**/*.md → згрупувати по base name
2. Для кожної групи без base:
   ├─ Find highest _N (напр., _4)
   ├─ Rename _N → base
   └─ Delete rest _1, _2, _3
3. --apply для фактичної дії
```

### 3.7 `tools/verify_hashes.py` — Верифікація хешів

**Роль:** Перевірка коректності всіх SHA256 хешів у raw файлах.

**Алгоритм виконання:**

```
1. SCAN raw/**/*.md
2. Для кожного файлу:
   ├─ compute_correct_sha256(body)
   ├─ Extract stored sha256 з frontmatter
   ├─ Порівняти → OK або MISMATCH
   └─ Flag all mismatches
3. Повернути: {all_ok: bool, mismatches: list}
```

### 3.8 `tools/verify_full_mapping.py` — Верифікація повного мапінгу

**Роль:** Перевірка повного мапінгу raw → wiki sources.

**Алгоритм виконання:**

```
1. SCAN raw/**/*.md → raw_files set
2. SCAN wiki/sources/**/*.md → wiki_files set
3. missing_in_wiki = raw_files - wiki_files
4. extra_in_wiki = wiki_files - raw_files
5. Повернути: {missing, extra, raw_count, wiki_count}
```

### 3.9 `tools/rss_monitor.py` — RSS-сканер

**Роль:** Моніторинг RSS/Atom-каналів для виявлення нових статей.

**Алгоритм виконання:**

```
1. ІНІЦІАЛІЗАЦІЯ
   ├─ Завантажити RSS_URLS (список URL-адрес RSS-каналів)
   ├─ Завантажити DB_PATH (/tmp/llm-wiki-rss.db)
   ├─ Ініціалізувати базу даних:
   │   ├─ Таблиця processed_urls (url TEXT PRIMARY KEY, fetched_at TIMESTAMP)
   │   └─ Таблиця processed_feeds (feed_url TEXT PRIMARY KEY, last_etag TEXT, last_modified TEXT)

2. SCAN_FEED(feed_url)
   │
   ├─ 2.1. GET feed_url з HTTP-заголовками:
   │   ├─ If-None-Match: last_etag (з DB)
   │   └─ If-Modified-Since: last_modified (з DB)
   │
   ├─ 2.2. Якщо 304 Not Modified → return [] (nothing new)
   │
   ├─ 2.3. Parse XML feed:
   │   ├─ Extract items (entries)
   │   ├─ Для кожного item:
   │   │   ├─ url = item.link
   │   │   ├─ title = item.title
   │   │   ├─ published = item.published / item.updated
   │   │   └─ content = item.content / item.summary
   │   │
   │   ├─ 2.4. Для кожного item:
   │   │   ├─ is_already_fetched(url)? → Так: skip
   │   │   └─ Ні: додати до new_items
   │   │
   │   ├─ 2.5. Зберегти етикетку:
   │   │   ├─ last_etag → DB
   │   │   └─ last_modified → DB
   │   │
   │   └─ Повернути new_items (необроблені)

3. FETCH_ARTICLE(url)
   │
   ├─ 3.1. GET url → HTML
   ├─ 3.2. convert_html_to_markdown(html)
   ├─ 3.3. Визначити тип:
   │   ├─ arXiv → raw/papers/
   │   ├─ YouTube transcript → raw/transcripts/
   │   └─ інше → raw/articles/
   │
   ├─ 3.4. Generate filename:
   │   ├─ arXiv: arxiv{paper_id}.md
   │   ├─ YouTube: youtube_{video_id}_{date}.md
   │   └─ інше: {title_slug}_{date}.md
   │
   ├─ 3.5. Write raw file з frontmatter:
   │   ├─ source_url: {url}
   │   ├─ ingested: {date}
   │   └─ sha256: {hash of body}
   │
   ├─ 3.6. Mark url as fetched в DB
   └─ Повернути raw_path

4. MAIN()
   ├─ Для кожного feed_url:
   │   ├─ scan_feed(feed_url)
   │   ├─ Для кожного new_item:
   │   │   ├─ fetch_article(item.url)
   │   │   └─ print(f"Saved: {raw_path}")
   │   └─ print(f"Feed: {feed_url} — {len(new_items)} new")
   └─ Exit 0 (нові знайдено) або Exit 1 (нічого нового)
```

**Ключові особливості:**
- Використовує HTTP caching (ETag, Last-Modified) для мінімізації трафіку
- Підтримує стандарт RSS 2.0 та Atom 1.0
- Автоматична класифікація за URL (arXiv, YouTube, інше)
- SQLite-база для трекингу оброблених URL

### 3.10 `tools/local_file_monitor.py` — Моніторинг локальних директорій

**Роль:** Відслідковування змін у локальних директоріях, що містять сирі дані.

**Алгоритм виконання:**

```
1. ІНІЦІАЛІЗАЦІЯ
   ├─ Завантажити WATCH_DIRS (список директорій для моніторингу)
   ├─ Завантажити DB_PATH (/tmp/llm-wiki-local.db)
   ├─ Ініціалізувати базу:
   │   └─ Таблиця file_hashes (file_path TEXT PRIMARY KEY, file_hash TEXT, watched_at TIMESTAMP)
   │
   ├─ 2. Для кожної директорії в WATCH_DIRS:
   │   ├─ Пройтись по всіх *.md файлах
   │   ├─ Compute SHA256(file_content)
   │   ├─ Порівняти з DB:
   │   │   ├─ Немає в DB → new_file (додати до new_files)
   │   │   ├─ Є в DB, hash збігається → skip
   │   │   └─ Є в DB, hash не збігається → modified_file (додати до modified_files)
   │   └─ Оновити DB: file_path → file_hash, watched_at
   │
   └─ Повернути {new_files, modified_files, skipped}
```

**Ключові особливості:**
- Хешує вміст файлу, а не metadata (модифікація, розмір)
- Користувач може вказати custom директорії через аргументи CLI
- Використовує polling-підхід (не inotify) для крос-платформеності

### 3.11 `tools/github_release_monitor.py` — Моніторинг GitHub релізів

**Роль:** Відслідковування нових релізів та ассетів на GitHub.

**Алгоритм виконання:**

```
1. ІНІЦІАЛІЗАЦІЯ
   ├─ Завантажити REPOS (список owner/repo пар)
   ├─ Завантажити GITHUB_TOKEN (з env або config)
   ├─ Завантажити DB_PATH (/tmp/llm-wiki-github.db)
   ├─ Ініціалізувати базу:
   │   └─ Таблиця releases (repo TEXT, tag TEXT PRIMARY KEY, released_at TIMESTAMP)

2. CHECK_REPO(repo)
   │
   ├─ 2.1. GET /repos/{owner}/{repo}/releases
   │   └─ Headers: Authorization: Bearer ***
   │
   ├─ 2.2. Для кожного release:
   │   ├─ tag = release.tag_name
   │   ├─ released_at = release.published_at
   │   ├─ is_already_seen(repo, tag)? → Так: skip
   │   └─ Ні:
   │       ├─ Download assets (if configured)
   │       ├─ Save asset to raw/assets/
   │       ├─ Create source note to raw/articles/
   │       └─ Mark as seen in DB
   │
   └─ Повернути {new_releases, assets_downloaded}
```

**Ключові особливості:**
- Підтримує GitHub REST API v3
- Автоматичне завантаження ассетів (binaries, docs)
- Трекинг через tag name + repo

### 3.12 `tools/wiki_lint.py` — Перевірка структурної цілісності

**Роль:** Сканування всієї вікі та виявлення проблем: брукен-лінки, відсутній frontmatter, SHA256-дрейф, невалідні теги.

**Алгоритм виконання:**

```
1. SCAN_ALL_WIKI_PAGES()
   ├─ Пройтись по wiki/**/*.md (крім README)
   ├─ Для кожного файлу:
   │   ├─ Прочитати вміст
   │   ├─ validate_frontmatter(content)
   │   ├─ validate_required_fields(frontmatter)
   │   ├─ validate_tags(frontmatter.tags)
   │   ├─ extract_wikilinks(content)
   │   ├─ check_in_index(file_path)
   │   ├─ compute_sha256(body)
   │   ├─ check_sha256_drift(stored_sha, computed_sha)
   │   ├─ check_line_count(content)
   │   └─ check_confidence(content)
   │
   └─ Повернути list of issues

2. validate_frontmatter(content)
   ├─ Чи починається з "---"?
   ├─ Чи є закриваючий "---"?
   ├─ Чи парситься як YAML?
   └─ Повернути {valid: bool, error: str|None}

3. validate_required_fields(frontmatter)
   ├─ Перевірка наявності: type, title, description, created, updated, tags, sources, confidence, links
   ├─ Перевірка type: має бути в VALID_TYPES
   ├─ Перевірка dates: формат YYYY-MM-DD
   └─ Повернути список відсутніх полів

4. validate_tags(tags)
   ├─ Для кожного tag:
   │   └─ Чи є в APPROVED_TAGS (з SCHEMA.md)?
   └─ Повернути список невалідних тегів

5. extract_wikilinks(content)
   ├─ Regex: \[\([^\]]+\)\]
   ├─ Для кожного wikilink:
   │   └─ Чи існує файл wiki/{type}/{slug}.md?
   └─ Повернути список брукен-посилань

6. compute_sha256(body)
   ├─ Body = content після frontmatter (після другого "---")
   └─ hashlib.sha256(body.encode()).hexdigest()

7. check_sha256_drift(stored_sha, computed_sha)
   ├─ Чи збігаються?
   └─ Ні → drift detected

8. check_line_count(content)
   ├─ lines = content.count('\n') + 1
   ├─ lines > 200 → flag
   └─ Повернути {lines, over_threshold}

9. check_confidence(content)
   ├─ confidence = frontmatter.get("confidence")
   ├─ confidence == "low" → review needed
   ├─ contested == true → review needed
   └─ Повернути list

10. MAIN()
    ├─ SCAN_ALL_WIKI_PAGES()
    ├─ Generate report (console + outputs/lint-report.md)
    ├─ Повернути summary: {total_issues, critical, warnings, info}
    └─ Exit 0 (завжди, навіть при проблемах — не блокує пайплайн)
```

|| **Категорії проблем:**
| Критичність | Типи проблем |
|-------------|-------------|
| **Critical** | Відсутній frontmatter, відсутні required fields, брукен-лінки |
| **Warning** | SHA256-дрейф, теги не з таксономії, >200 рядків |
| **Info** | confidence: low, contested: true |

### 3.13 `tools/wiki_doctor.py` — 6-layer diagnostic & auto-cure

**Роль:** Повна діагностика та авто-лікування wiki: брукен-лінки, frontmatter-дрейф, SHA256-дрейф, дублікати, невалідні теги, порожні сторінки.

**Алгоритм виконання:**

```
1. LAYER 1: Broken Wikilinks
   ├─ Regex: \[\[([^\]|#]+)
   ├─ Для кожного wikilink: перевірка існування slug
   ├─ Auto-fix: замінити на існуючий slug або видалити
   └─ Report: {broken_count, fixed_count, removed_count}

2. LAYER 2: Frontmatter Drift
   ├─ Для кожного файлу wiki/**/*.md:
   │   ├─ parse frontmatter
   │   ├─ check required fields (type, title, created, updated, tags, sources)
   │   ├─ check type is in VALID_TYPES
   │   └─ Auto-fix: add missing fields with defaults
   └─ Report: {drifted_count, fixed_count}

3. LAYER 3: SHA256 Drift
   ├─ Для кожного файлу wiki/**/*.md:
   │   ├─ compute sha256(body)
   │   ├─ compare with stored sha256
   │   └─ Auto-fix: update stored sha256
   └─ Report: {drifted_count, fixed_count}

4. LAYER 4: Duplicate Detection
   ├─ SCAN wiki/**/*.md
   ├─ Group by base name (strip _N suffixes)
   ├─ Flag groups with >1 file
   └─ Report: {duplicate_groups, total_duplicates}

5. LAYER 5: Invalid Tags
   ├─ Для кожного файлу: extract tags
   ├─ Compare with SCHEMA.md taxonomy
   ├─ Auto-fix: replace invalid tags with approved ones
   └─ Report: {invalid_count, fixed_count}

6. LAYER 6: Empty Pages
   ├─ Для кожного файлу: check body length
   ├─ Flag pages with <100 chars of body text
   └─ Report: {empty_count, flagged_count}

7. MAIN()
   ├─ Run all 6 layers
   ├─ Generate JSON report → outputs/doctor-report.json
   ├─ Print summary: ERROR/WARN/INFO/Auto-fixable counts
   └─ Exit 0 (always, non-blocking)
```

**Категорії проблем:**
| Критичність | Типи проблем |
|-------------|-------------|
| **ERROR** | Відсутній frontmatter, брукен-лінки, дублікати |
| **WARN** | SHA256-дрейф, невалідні теги, порожні сторінки |
| **INFO** | confidence: low, contested: true |

### 3.14 `tools/standard_report.py` — Форматування звітів для cron

**Роль:** Канонічний формат звітів для всіх крон-моніторів. Використовується rss_monitor, local_file_monitor, github_release_monitor.

**Контракт виводу:**
```python
{
    "status": "ok" | "error" | "warning",
    "summary": "short description",
    "details": "detailed breakdown",
    "timestamp": "YYYY-MM-DD HH:MM UTC",
    "source_job": "job_name"
}
```

### 3.15 `tools/integrator.py` — Автоматичний інтегратор

**Роль:** Головний скрипт перетворення сирого джерела на сторінку вікі. Запускається після сканування для обробки нових raw-файлів.

**Алгоритм виконання:**

```
1. ІНІЦІАЛІЗАЦІЯ
   ├─ Завантажити WIKI_DIR, RAW_DIR, INDEX_FILE, DB_PATH
   ├─ Завантажити APPROVED_TAGS (всі валідні теги з SCHEMA.md)
   ├─ Завантажити TYPE_DIR_MAP (мапінг типів → директорії)
   └─ Завантажити MODEL_KEYWORDS (ключові слова для розпізнавання моделей)

2. BUILD_TAG_MAP()
   ├─ Пройтись по всіх wiki/**/*.md
   ├─ Для кожного файлу:
   │  ├─ Прочитати перші 500 символів (frontmatter)
   │  ├─ Парсити теги з YAML-блоку
   │  ├─ Парсити title з першого H1
   │  └─ Додати до tag_map: tag → [title1, title2, ...]
   └─ Повернути tag_map для подальшого використання

3. PROCESS_RAW_FILES(raw_dir, limit=None)
   │
   ├─ 3.1. build_tag_map() — зчитати існуючі сторінки
   ├─ 3.2. sorted(raw_dir.glob("*.md")) — отримати всі raw файли
   ├─ 3.3. Для кожного raw_file:
   │     │
   │     ├─ 3.3.1. is_already_processed(raw_file)?
   │     │     ├─ Так → skip (збільшити skipped count)
   │     │     └─ Ні → продовжити
   │     │
   │     ├─ 3.3.2. Прочитати raw_content
   │     │
   │     ├─ 3.3.3. extract_title(raw_content)
   │     │     ├─ Спроба 1: прочитати title з frontmatter
   │     │     ├─ Спроба 2: прочитати перший H1 (# title)
   │     │     ├─ Спроба 3: парсити source_url:
   │     │     │   ├─ arXiv → "arXiv:2607.XXXXX"
   │     │     │   └─ інше → slug з URL path
   │     │     └─ ОЧИЩЕННЯ ТИТУЛУ (9 кроків):
   │     │         ├─ Видалити "in YYYY" з кінця
   │     │         ├─ Видалити рокові діапазони "2025–2026"
   │     │         ├─ Видалити "[2026]" з кінця
   │     │         ├─ Видалити "as of MONTH YYYY"
   │     │         ├─ Видалити YYYY-MM-DD з кінця
   │     │         ├─ Видалити окремий рік з кінця
   │     │         ├─ Видалити ", YYYY" з кінця
   │     │         ├─ Видалити зайві пробіли
   │     │         └─ Видалити пунктуацію з кінця
   │     │
   │     ├─ 3.3.4. score_relevance(raw_content, title)
   │     │     ├─ Length bonus: >5000→+5, >2000→+3, >500→+1
   │     │     ├─ Keyword density: 14 технічних слів × max 3 = +42
   │     │     ├─ Technical depth: 14 термінів × 1 = +14
   │     │     ├─ classify_page_type(raw_content, title)
   │     │     │   ├─ comparison: "vs", "versus", "compared", "alternative"
   │     │     │   ├─ playbook: "guide", "how to", "tutorial", "best practices"
   │     │     │   ├─ synthesis: "analysis", "overview", "landscape", "trends"
   │     │     │   └─ default → "concept"
   │     │     └─ Повернути (score, page_type)
   │     │
   │     ├─ 3.3.5. Якщо score < 3 → skip (low relevance)
   │     │
   │     ├─ 3.3.6. extract_tags(raw_content, title)
   │     │     ├─ Прочитати tags з frontmatter raw-файлу
   │     │     ├─ Map слів → тегів (100+ mapping rules)
   │     │     ├─ Завжди додати: llm-wiki, knowledge-base
   │     │     └─ Повернути sorted(tags)
   │     │
   │     ├─ 3.3.7. generate_wiki_page(raw_path, raw_content, title, page_type, tags, tag_map)
   │     │     │
   │     │     ├─ convert_html_to_markdown(raw_content)
   │     │     │   ├─ Extract body/main/article
   │     │     │   ├─ Remove astro-island, script, style, comments
   │     │     │   ├─ Convert HTML → Markdown (h1-h6, bold, italic, links, images, lists, code, blockquotes)
   │     │     │   └─ Clean whitespace, unescape entities
   │     │     │
   │     │     ├─ Перевірка MIN_CONTENT_LENGTH (500 символів)
   │     │     │
   │     │     ├─ find_wikilinks(title, tags, tag_map, content)
   │     │     │   ├─ Content-based: semantic overlap > 3 спільних слів
   │     │     │   ├─ Tag-based: shared tags (score 2)
   │     │     │   ├─ Title-based: substring matches (score 3×overlap)
   │     │     │   └─ Return top 5 links sorted by score
   │     │     │
   │     │     ├─ Safe slug: re.sub(r"[^\w\s-]", "", title.lower()) → hyphenated
   │     │     ├─ Директорія: TYPE_DIR_MAP[page_type]
   │     │     │
   │     │     ├─ DUPLICATE CHECKS (3 рівні):
   │     │     │   ├─ Перевірка: {slug}.md існує? → skip
   │     │     │   ├─ Перевірка: {slug}_*.md існує? → skip
   │     │     │   └─ Перевірка: {slug}_YYYY-MM-DD.md існує? → skip
   │     │     │
   │     │     ├─ GENERATE WIKI CONTENT:
   │     │     │   ├─ Frontmatter: type, title, tags (llm-wiki + knowledge-base + extracted)
   │     │     │   ├─ H1: # {title}
   │     │     │   ├─ Metadata block: Source, Type, Created, Updated, Confidence, Description, Sources, Links
   │     │     │   ├─ ## Key Findings: cleaned_content[:3000]
   │     │     │   ├─ ## Summary: cleaned_content[3000:6000]
   │     │     │   └─ ## Related Articles: [[wikilinks]]
   │     │     │
   │     │     ├─ write_file(wiki_path, wiki_content)
   │     │     └─ Повернути relative path
   │     │
   │     ├─ 3.3.8. Якщо wiki_path успішний:
   │     │     ├─ mark_processed(raw_file) — записати в базу
   │     │     └─ update_index(wiki_path, page_type, title)
   │     │
   │     └─ 3.3.9. Якщо помилка → skip, збільшити skipped count
   │
   └─ Повернути stats: {new_pages, html_conversions, truncations, skipped}

4. MAIN()
   ├─ Parse arguments: --dry-run, --limit
   ├─ process_raw_files(RAW_DIR, limit=args.limit)
   └─ Print summary statistics
```

**Ключові параметри:**
|| Параметр | Значення | Опис |
||----------|----------|------|
|| `MIN_CONTENT_LENGTH` | 500 символів | Мінімальна довжина контенту для створення сторінки |
|| `score_threshold` | 3 | Мінімальний score для обробки |
|| `max_wikilinks` | 5 | Максимум внутрішніх посилань |
|| `title_content_window` | 10,000 символів | Обсяг контенту для аналізу тегів |

---

## 4. Діаграма зв'язків між компонентами

### 4.1 Файлова система

```
/workspace/llm-wiki/
│
├── SCHEMA.md                        ← Структурний контракт (вхід для всіх скриптів)
├── ARCHITECTURE.md                  ← Технічна архітектура
├── ALGORITHM.md                     ← Опис алгоритмів
├── AGENT.md                         ← Операцийний контракт агентів (корінь)
├── CLAUDE.md                        ← Операцийний контракт агентів (legacy shim)
├── index.md                         ← Навігаційний каталог (оновлюється інтегратором)
├── log.md                           ← Журнал дій append-only
│
├── raw/                             ← ШАР 1: Сирі джерела (immutable)
│   ├── articles/                    ← 88 файлів — веб-статті, спеки
│   ├── papers/                      ← 1 файл — академічні папери
│   ├── transcripts/                 ← 1 файл — транскрипти
│   └── assets/                      ← 1 файл — ассети
│
├── wiki/                            ← ШАР 2: Синтез (mutable)
│   ├── concepts/                    ← 61 файлів — концепції, ідеї
│   ├── entities/                    ← 48 файлів — продукти, системи
│   ├── comparisons/                 ← 1060 файлів — порівняння
│   ├── playbooks/                   ← 15 файлів — інструкції
│   ├── synthesis/                   ← 8 файлів — мультиджерельний аналіз
│   ├── queries/                     ← 2 файли — Q&A
│   ├── references/                  ← 2 файли — довідкові дані
│   └── templates/                   ← 8 файлів — шаблони сторінок
│
├── tools/                           ← ШАР 3: Інструменти (central utilities)
│   ├── utils.py                     ← Єдине джерело правди: хеші, frontmatter, теги, статуси
│   ├── integrator.py                ← Інтеграція raw → wiki
│   ├── rss_monitor.py               ← RSS-сканер
│   ├── local_file_monitor.py        ← Моніторинг локальних файлів
│   ├── local_monitor.py             ← Альтернативний локальний монітор
│   ├── github_monitor.py            ← Моніторинг GitHub репозиторіїв
│   ├── github_release_monitor.py    ← Моніторинг GitHub релізів
│   ├── check_new_raw.py             ← Перевірка нових raw-файлів (utils.check_raw_integrity)
│   ├── cleanup_duplicates.py        ← Видалення дублікатів
│   ├── promote_fallback_to_base.py  ← Промоція fallback у base
│   ├── verify_full_mapping.py       ← Верифікація повного мапінгу
│   ├── verify_hashes.py             ← Верифікація хешів (utils.check_raw_integrity)
│   ├── fix_sha256.py                ← Оновлення хешів (вручну)
│   └── wiki_lint.py                 ← Перевірка цілісності (utils.* + APPROVED_TAGS)
│
└── outputs/                         ← Вихідні дані
    └── lint-report.md               ← Результати лінтингу
```

### 4.2 Граф залежностей між скриптами

```
                    ┌─────────────────┐
                    │  External Sources│
                    │  (URL, RSS, Git) │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
     ┌─────────────┐ ┌─────────────┐ ┌──────────────┐
     │  rss_monitor│ │  local_file │ │ github_release│
     │    .py      │ │  _monitor   │ │   _monitor    │
     └──────┬──────┘ └──────┬──────┘ └──────┬───────┘
            │               │               │
            │    raw/       │    raw/       │    raw/
            └───────┬───────┴───────┬───────┘
                    ▼               ▼
            ┌─────────────────────────────┐
            │      integrator.py          │
            │  (raw → wiki + index + log) │
            └──────────────┬──────────────┘
                           │
               ┌───────────┼───────────┐
               ▼           ▼           ▼
         wiki/       index.md      log.md
         (pages)     (catalog)     (journal)
                           │
                           ▼
                   ┌───────────────┐
                   │  wiki_lint.py │
                   │  (health check)│
                   └───────────────┘
                           │
                           ▼
                   outputs/
                   lint-report.md

┌──────────────────────────────────────────────────────────────────────┐
│                        utils.py (CENTRAL HUB)                        │
│                                                                      │
│  check_new_raw.py ──→ check_raw_integrity()                          │
│  verify_hashes.py ──→ check_raw_integrity()                          │
│  wiki_lint.py ──────→ split_frontmatter, compute_sha256, APPROVED_TAGS│
│  rss_monitor.py ────→ build_frontmatter, compute_sha256              │
│  github_release_monitor.py → build_frontmatter, parse_simple_yaml    │
└──────────────────────────────────────────────────────────────────────┘
```

### 4.3 Граф зв'язків між директоріями вікі

```
    concepts/ (61)        entities/ (48)       comparisons/ (1060)
         │                    │                    │
         │  [[wikilinks]]     │  [[wikilinks]]     │  [[wikilinks]]
         ▼                    ▼                    ▼
    ┌──────────────────────────────────────────────────────┐
    │                    wiki/ (1204 total)                  │
    │                                                       │
    │  playbooks/ (15)  synthesis/ (8)  queries/ (2)       │
    │       │                │               │              │
    │       │                │               │              │
    │       └────────────────┴───────────────┘              │
    │                                                       │
    │  references/ (2)  templates/ (8)                      │
    └──────────────────────────────────────────────────────┘
                           │
                           ▼
                    index.md (catalog)
```

### 4.4 База даних трекингу

```
/tmp/llm-wiki-rss.db (SQLite)
├── processed_urls (url TEXT PK, fetched_at TIMESTAMP)
│   → Унікальні URL сиріх джерел
├── processed_feeds (feed_url TEXT PK, last_etag TEXT, last_modified TEXT)
│   → Статус RSS-каналів для HTTP caching
└── (future: processed_files, processed_releases)
```

---

## 5. Неявні припущення та архітектурні рішення

### 5.1 Неявні припущення

| # | Припущення | Опис | Ризик |
|---|-----------|------|-------|
| 1 | **Словник моделей** | `MODEL_KEYWORDS` містить ~1000+ назв моделей LLM як літерал у коді | При появі нової моделі — інтегратор не впізнає її автоматично, але це не критично: тегування працює через word→tag mapping |
| 2 | **HTML-парсинг** | `convert_html_to_markdown` використовує regex, не HTML-парсер | Може ламатися на складних HTML-структурах (nested tables, custom elements). Для більшості статей — працює коректно |
| 3 | **Title stripping** | 9 послідовних regex-кроків для очищення титулу | Може видаляти корисні слова (напр., "2026" як рік видання). Порядок фільтрів: найконкретніші перші |
| 4 | **Tag extraction** | `word_to_tag` mapping — ручний мапінг ~100 слів → теги | Може пропускати нішеві терміни; але base tags (llm-wiki, knowledge-base) завжди додаються |
| 5 | **Relevance scoring** | Threshold score = 3, length bonus max +5 | Дуже короткі, але важливі статті можуть бути пропущені |
| 6 | **Wikilink generation** | Semantic similarity через перетин слів (>3 спільних) | Може генерувати помилкові зв'язки; але обмежено до top-5 |
| 7 | **Duplicate detection** | 3 рівні перевірок (base, suffixed, dated) | Якщо файл видалено вручну, але DB-запис залишився — інтегратор пропустить його |
| 8 | **Page lifecycle** | Перший інгест "виграє" — базовий slug не перезаписується | Не підтримує "виправлення" дублікатів автоматично; потрібна ручна дія |
| 9 | **Wiki page structure** | Фіксована структура: frontmatter → H1 → metadata → Key Findings → Summary → Related | Не підтримує кастомні секції; всі сторінки мають однакову форму |
| 10 | **Index update** | Нова сторінка додається на початок секції, після frontmatter | Не впорядковує алфавітно; перегенерація індексу потрібна для порядку |
| 11 | **SQLite tracking** | База в `/tmp/` — може бути видалена при перезавантаженні | При втраті DB — інтегратор повторно обробить усі raw-файли (дублікати блокуються) |
| 12 | **RSS parsing** | Використовує стандартний XML-парсер | Не обробляє HTML-енкодований контент у RSS-полях |

### 5.2 Архітектурні рішення

| Рішення | Обґрунтування | Альтернатива |
|---------|--------------|-------------|
| Markdown-first | Людиночитабельний, diffable, працює в Obsidian/VS Code/Git | JSON, SQLite, Notion API |
| Raw immutable | Запобігає непомітній псуванню джерел | Mutable raw (risk of silent corruption) |
| Wiki mutable | Дозволяє агенту покращувати синтез з часом | Immutable wiki (потребують повної перегенерації) |
| Index + log mandatory | Запобігає розпаду бази знань | No index (неможливо навігувати) |
| Schema local to repo | Будь-який агент може відновити контекст без зовнішньої пам'яті | External schema server |
| MCP later | Уникає передчасної складності протоколу | MCP from day one |
| Regex HTML→MD | Простота, zero dependencies | BeautifulSoup, Trafilatura |
| SQLite for tracking | Zero-config, portable | Redis, PostgreSQL |
| Fixed page template | Консистентність, легко парсити | Free-form pages (складно автоматизувати) |
| Score-based filtering | Автоматичне відсіювання сміття | Manual review (повільно) |
| First-wins dedup | Простота, не втрачає перший інгест | Last-wins (втрачає ранній контент) |

---

## 6. Поточна статистика системи

### 6.1 Файлова система

| Директорія | Кількість файлів | Тип |
|------------|-----------------|-----|
| `raw/articles/` | 1771 | Сирі статті |
| `raw/papers/` | 1 | Академічні папери |
| `raw/transcripts/` | 1 | Транскрипти |
| `raw/assets/` | 1 | Ассети |
| **Raw total** | **1774** | |
| `.processed/` | 16 | Проміжний кеш HTML→MD (НЕ в git) |
| `wiki/comparisons/` | 1060 | Порівняння |
| `wiki/concepts/` | 61 | Концепції |
| `wiki/entities/` | 48 | Сутності |
| `wiki/playbooks/` | 15 | Інструкції |
| `wiki/synthesis/` | 8 | Синтез |
| `wiki/queries/` | 2 | Q&A |
| `wiki/references/` | 2 | Довідкові |
| `wiki/templates/` | 8 | Шаблони |
| **Wiki total** | **1204** | |
| **Grand total** | **2978** | |
### 6.2 Індекси та журнали

| Елемент | Статус |
|---------|--------|
| `wiki/index.md` | 20 категорій, 40 рядків |
| `log.md` | 116 записів, 279 рядків, append-only |

### 6.3 Бази даних трекингу

| База | Розмір | Вміст |
|------|--------|-------|
| `/tmp/llm-wiki-rss.db` | 3.7 KB | processed_urls, processed_feeds |

### 6.4 Скрипти

| Скрипт | Роль |
|--------|------|
| `utils.py` | Центральна бібліотека: хеші, frontmatter, теги, статуси (єдине джерело правди) |
| `integrator.py` | Інтеграція raw → wiki |
| `rss_monitor.py` | RSS-сканер |
| `local_file_monitor.py` | Моніторинг локальних файлів |
| `github_monitor.py` | Моніторинг GitHub репозиторіїв |
| `github_release_monitor.py` | Моніторинг GitHub релізів |
| `wiki_lint.py` | Перевірка цілісності (залежить від utils.*) |
| `wiki_doctor.py` | 6-layer diagnostic & auto-cure |
| `check_new_raw.py` | Перевірка нових raw-файлів |
| `cleanup_duplicates.py` | Видалення дублікатів |
| `promote_fallback_to_base.py` | Промоція fallback у base |
| `verify_full_mapping.py` | Верифікація повного мапінгу |
| `verify_hashes.py` | Верифікація хешів |
| `fix_sha256.py` | Оновлення хешів (вручну) |
| `source_monitor.py` | Об'єднаний моніторинг (RSS + GitHub + Local) |
| `standard_report.py` | Форматування звітів для cron |
| `newspaper_digest.py` | Щоденний звіт |
| `inbox_router.py` | Маршрутизація inbox |
| `github_repos.py` | Моніторинг GitHub репозиторіїв |
| `test_inbox_router.py` | Тести для inbox_router |
| `test_telegram_links.py` | Тести для telegram-посилань |
| `wiki_slash_commands.py` | Slash-команди для wiki |
| **Всього** | **23 скрипти** | |

### 6.5 Obsidian Vault

| Компонент | Файлів | Роль |
|-----------|--------|------|
| `app.json` | 1 | Основна конфігурація |
| `appearance.json` | 1 | Тема, шрифти |
| `core-plugins.json` | 1 | Ввімкнені ядрові плагіни |
| `community-plugins.json` | 1 | Список плагінів |
| `graph.json` | 1 | Налаштування графу |
| `dataview/data.json` | 1 | Конфіг Dataview |
| `obsidian-git.json` | 1 | Конфіг Git синхронізації |
| `templater-obsidian/data.json` | 1 | Конфіг Templater |
| `templates/` | 4 | Шаблони для Obsidian |
| `themes/llm-wiki-dark.css` | 1 | Кастомна тема |
| **Всього** | **14** | |

### 6.6 Outputs (згенеровані звіти, НЕ в git)

| Файл | Розмір | Призначення |
|------|--------|-------------|
| `outputs/README.md` | 60B | Пояснення директорії |
| `outputs/doctor-report.json` | 43KB | Результати Wiki Doctor |
| `outputs/lint-report.md` | 2.7KB | Результати лінтингу |

### 6.7 Крон-задачі (Hermes Agent)

**Загальні параметри всіх крон-завдань:**
- **Провайдер:** `custom:llama-server` (локальний LLM)
- **Модель:** `qwen3.6-35b-a3b` (закріплена для запобігання drift)
- **Доставка:** `origin` (повернення до чату — Telegram)
- **Мова звітів:** українська
- **Формат виводу:** усі монітори використовують `standard_report.py` з контрактом `{status, summary, details, timestamp, source_job}`

**Архітектура з 3 jobs (замість 6):**

| # | Job | Скрипт | Частота | Що робить |
|---|-----|--------|---------|-----------|
| 1 | **Source Monitor** | `source_monitor.py` | every 6h | RSS + GitHub + Local → raw/articles/ |
| 2 | **Wiki Integrator** | `integrator.py` | every 12h | raw/ → wiki-сторінки |
| 3 | **Wiki Doctor** | `wiki_doctor.py` | every 12h | diagnose → auto-cure → re-diagnose → JSON |

**Економія:** 50% cron-сесій (6 → 3), 50% витрат на LLM.

#### 6.7.1 Source Monitor
- **Частота:** `every 6h` (кожні 6 годин)
- **Навички:** `wiki-indexer`, `llm-wiki`
- **Toolsets:** `terminal`, `skills`, `file`
- **Виконує:** `python3 tools/source_monitor.py`
- **Що робить:** Об'єднує RSS (10 feed), GitHub (26 repos), Local (8 dirs) в одному запуску
- **Вивід:** структурований звіт з полів `status`, `summary`, `details`, `timestamp`, `source_job`
- **Підстави частоти:** 6 годин — оптимальний баланс між свіжістю даних та навантаженням на LLM

#### 6.7.2 Wiki Integrator
- **Частота:** `every 12h` (щодвінадцять годин)
- **Toolsets:** `terminal`, `file`
- **Виконує:** `python3 tools/integrator.py`
- **Що робить:** raw → wiki-сторінки (класифікація, синтез, index.md, log.md)
- **Підстави частоти:** 12 годин — інтеграція після накопичення raw-файлів

#### 6.7.3 Wiki Doctor
- **Частота:** `every 12h` (щодвінадцять годин)
- **Toolsets:** `terminal`, `file`
- **Виконує:** `python3 tools/wiki_doctor.py cure --dry-run`
- **Що робить:** 6-layer діагностика + auto-cure + re-diagnosis → outputs/doctor-report.json
- **Вивід:** console report + JSON (outputs/doctor-report.json) + log.md entry
- **Підстави частоти:** 12 годин — регулярний health-check без зміни файлів (--dry-run)
- **Безпека:** --dry-run гарантує жодних змін файлів; лише звіт про те що БУЛО б виправлено

#### 6.7.4 Нова діаграма виконання

```
Час    Source Monitor    Integrator    Wiki Doctor
─────  ──────────────  ────────────  ─────────────
00:00  ✓               ─             ─
02:00  ─               ─             ─
04:00  ─               ─             ─
06:00  ✓               ✓             ✓
08:00  ─               ─             ─
10:00  ─               ─             ─
12:00  ✓               ─             ─
14:00  ─               ─             ─
16:00  ─               ─             ─
18:00  ✓               ✓             ✓
20:00  ─               ─             ─
22:00  ─               ─             ─
```

#### 6.7.5 Порядок виконання та залежності

```
1. Source Monitor (00:00, 06:00, 12:00, 18:00)
   ↓ запис у raw/articles/
2. Wiki Integrator (06:00, 18:00) — через 0-6h після Source Monitor
   ↓ raw → wiki + index.md + log.md
3. Wiki Doctor (06:00, 18:00) — паралельно з Integrator
   ↓ diagnose → cure → re-diagnose → JSON
```

**Важливо:** Integrator запускається через 0-6h після Source Monitor для накопичення raw-файлів. Wiki Doctor працює паралельно для постійного контролю якості.

#### 6.7.6 Стратегія обробки помилок та backoff

| Помилка | Поведінка | Відновлення |
|---------|-----------|-------------|
| Source Monitor: RSS HTTP 304 | `status: ok`, skip | Наступний запуск через 6 год |
| Source Monitor: мережева відмова | `status: error`, traceback | Автоматичне відновлення |
| Source Monitor: GitHub 403 | `status: error`, список репозиторіїв | Потрібен `GITHUB_TOKEN` |
| Source Monitor: GitHub rate limit | Exponential backoff | Автоматичне відновлення |
| Source Monitor: local dir missing | `status: warning`, skip | Перевірити шляхи |
| Integrator: низький score | `skip`, не помилка | Наступний запуск |
| Integrator: дублікат slug | `skip`, не помилка | Наступний запуск |
| Wiki Doctor: --dry-run | Жодних змін, лише звіт | Безпечно, завжди |
| Lint: проблеми знайдено | `status: ok` (Exit 0) | Ручне виправлення |

**Надійність:** 42/42 тестів PASS — Wiki Doctor auto-cure гарантовано точний. --dry-run mode не змінює жодного файлу.

---

### 6.8 Історія змін системи

| Дата | Фаза | Опис |
|------|------|------|
| 2026-07-04 | Phase 1 | Foundation Pack: структура, schema, architecture, algorithm, initial sources |
| 2026-07-06 | Phase 2 | Consolidation: видалено `wiki/sources/`, `wiki/events/`, `wiki/digests/`; шаблони переміщено |
| 2026-07-07 | Phase 3 | Batch ingest: 52 статті, 19 нових сторінок вікі |
| 2026-07-09 | Phase 4 | Full architecture documentation (this document) |
| 2026-07-09 | Phase 5 | SCHEMA.md docs/ directory added, CLAUDE.md updated, ALGORITHM.md streamlined |
| 2026-07-11 | Phase 7 | Central utilities: `tools/utils.py` created — єдине джерело правди для хешів, frontmatter, тегів та статусів. `check_new_raw.py` та `verify_hashes.py` переведено на `utils.check_raw_integrity()`. 158 false-positive MISMATCH усунуто. `fix_sha256.py` оновлено 158 файлів. `rglob('**/*.md')` замінено `glob('*.md')` для рекурсивного сканування. `APPROVED_TAGS` (262 теги) уніфіковано в `utils.py`. `wiki_lint.py` залежить від `utils.*`. |

### 6.9 Правила якості (з SCHEMA.md)

- Створити сторінку, коли концепція центральна для одного джерела або з'являється в 2+ джерелах
- Оновлювати існуючу сторінку замість створення дублікатів
- Не створювати сторінки для згадок
- Розділяти сторінки понад ~200 рядків
- Кожна концепція/порівняння/Q&A має посилатися мінімум на 2 інші сторінки

### 6.10 Правила посилань

- Використовувати Obsidian-стиль `[[wikilinks]]` для концептуальних посилань
- Використовувати markdown-посилання для raw-шляхів та зовнішніх URL
- Кожна нова сторінка має бути вказана в `index.md`

### 6.11 Сигнали якості

| Сигнал | Значення |
|--------|---------|
| `confidence: high` | Підтверджено кількома надійними джерелами або прямим специфікаційним текстом |
| `confidence: medium` | Ймовірний синтез з одного сильного джерела |
| `confidence: low` | Слабке, суперечливе, виведене або потребує перевірки |
| `contested: true` | Існує непідтверджений конфлікт |

### 6.12 Порядок роботи нового агента

1. Прочитати `AGENT.md`
2. Прочитати `SCHEMA.md`
3. Прочитати `index.md`
4. Прочитати останні записи `log.md`
5. Шукати існуючі сторінки за темою
6. Виконати лише запитану операцію
7. Записати результат в `log.md`
