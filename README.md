# LLM Wiki

> Persistent knowledge base for AI/LLM systems. Karpathy pattern. Open Knowledge Format v0.1.

## Що це

Це твоя **персистентна база знань** про AI/LLM, побудована за патерном Karpathy. На відміну від RAG (який щоразу шукає знання з нуля), wiki компілює знання один раз і тримає їх актуальними. Кожна нова стаття розширює всю базу — це compounding effect.

**Архітектура з 5 шарів:**

```
Шар 0: raw/          — незмінні джерела (сирці)
Шар 1: .processed/   — проміжний кеш HTML→MD (не в git)
Шар 2: wiki/         — синтезовані сторінки (concept, entity, comparison...)
Шар 3: graphify-out/ — структурний граф (nodes/edges/communities)
Шар 4: SCHEMA.md     — правила та конвенції
```

## Ролі

- **Master (ви)** — куратор, затверджує зміни, формулює запити
- **Agent (Архіваріус/Монті)** — збирач, інтегратор, лінтер

Ти — **куратор**. Агент — **збирач**.

## Архітектура

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ШАР 3: Graphify-OUT (Структурний граф)            │
│  graph.json  graph.html  GRAPH_REPORT.md  (1365 nodes, 6289 edges) │
│  wiki_graph_generator.py → з wikilinks [[slug]]                    │
└──────────────────┬──────────────────────────────────────────────────┘
                   │ wikilinks → edges
┌──────────────────▼──────────────────────────────────────────────────┐
│                    ШАР 2: WIKI (Синтезовані сторінки)                 │
│  wiki/  (1366 .md файлів)                                           │
│  concepts/ entities/ comparisons/ synthesis/ digests/               │
│  Index: index.md  |  Lint: wiki_lint.py  |  Cure: wiki_doctor.py   │
└──────────────────┬──────────────────────────────────────────────────┘
                   │ content extraction
┌──────────────────▼──────────────────────────────────────────────────┐
│                    ШАР 1: .PROCESSED (Проміжний кеш)                 │
│  .processed/  (HTML→MD конвертація, не в git)                       │
└──────────────────┬──────────────────────────────────────────────────┘
                   │ raw source
┌──────────────────▼──────────────────────────────────────────────────┐
│                    ШАР 0: RAW (Незмінні джерела)                     │
│  raw/articles/  raw/papers/  raw/transcripts/  (1961 файли)         │
│  RSS feeds  •  GitHub repos  •  Local files  •  Telegram            │
└─────────────────────────────────────────────────────────────────────┘

              ШАР 4: SCHEMA.md (правила, конвенції, APPROVED_TAGS)
```

### Pipeline автоматизації

```
RSS/GitHub/Local → raw/ (immutable) → integrator → wiki/ (mutable)
                        │                                      │
                        ▼                                      ▼
                  .processed/                    wiki_graph_generator → graph.json
                  (HTML→MD)                                           │
                                                                      ▼
                                                              graphify_bridge.py → cross-references
```

## Швидкий старт

| Документ | Мова | Призначення |
|----------|------|-------------|
| [Архітектура](docs/ARCHITECTURE.md) | UA | Повна архітектурна документація |
| [Алгоритм](docs/ALGORITHM.md) | EN | Ingest / Query / Lint workflows |
| [Agent Contract](AGENTS.md) | EN | Операцийний контракт агента |
| [Schema](SCHEMA.md) | EN | Теги, типи, валідація |
| [Roadmap](docs/ROADMAP.md) | EN | План розвитку системи |
| [Wiki Doctor](docs/wiki-doctor.md) | EN | 6-layer diagnostic & auto-cure |
| [Інструкція для Монті](docs/INSTRUCTIONS_FOR_MONTY.md) | UA | Як збирати сирі джерела |
| [Інструкція для Master](docs/MASTER_INSTRUCTIONS.md) | UA | Як керувати wiki |

## Структура

| Шлях | Призначення |
|------|-------------|
| `raw/` | Сирі джерела (immutable, 1961 файли) |
| `wiki/` | Синтезовані сторінки (mutable, 1366 файлів) |
| `.processed/` | Проміжний кеш HTML→MD (не в git) |
| `graphify-out/` | Структурний граф (graph.json, 1365 nodes) |
| `tools/` | Скрипти інфраструктури (24 шт.) |
| `docs/` | Документація |
| `architecture/` | SVG/HTML діаграми архітектури |
| `outputs/` | Згенеровані звіти (не в git) |
| `.obsidian/` | Obsidian vault конфігурація |
| `SCHEMA.md` | Структурний контракт (ядро) |
| `AGENTS.md` | Контракт агента |

## Статистика

| Показник | Значення |
|----------|---------|
| Сторінки wiki | **1366** |
| Сирі джерела | **1961** |
| Скрипти | **24** |
| Nodes графа | **1365** |
| Edges графа | **6289** |
| Communities | **16** |
| Тегів (taxonomy) | **262** |
| ERROR лінтингу | **0** [CLEAN] |
| Obsidian плагінів | **3** (dataview, git, templater) |
| Крон-задач | **3** (Source Monitor, Wiki Integrator, Wiki Doctor) |

## Граф знань

Граф згенеровано з реальних wikilinks між wiki-сторінками.

| Метрика | Значення |
|---------|---------|
| Avg edges/node | 4.61 |
| Top tag | `llm-wiki` (136) |
| Top type | `comparison` (1129) |
| Most linked | "Automating Ai Away" (91 inbound) |

**Генератор:** `python3 tools/wiki_graph_generator.py`
**Bridge:** `python3 tools/graphify_bridge.py --auto-fix`

## Команди

| Що сказати | Що зробить |
|------------|------------|
| `"Перевір стан wiki"` | Запускає лінт, показує issues |
| `"Додай цю статтю: [URL]"` | Зберігає у raw/, створює wiki-сторінки |
| `"Збери 5 статей про [тема]"` | Запускає агента для збору |
| `"Створи synthesis про [тема]"` | Поєднує існуючі джерела |
| `"Створи comparison [A] vs [B]"` | Порівняння двох сутностей |
| `"Що wiki знає про [тема]?"` | Пошук та синтез з існуючих сторінок |
| `"Запусти лінт"` | `python3 tools/wiki_lint.py` |
| `"Запусти doctor"` | `python3 tools/wiki_doctor.py` |
| `"Перевір граф"` | `python3 tools/wiki_graph_generator.py` |
| `"Онови bridge"` | `python3 tools/graphify_bridge.py --auto-fix` |

## Важливі правила

1. **Ніколи не редагуй `raw/`** — це незмінні джерела
2. **Завжди оновлюй `index.md`** — без цього wiki деградує
3. **Завжди оновлюй `log.md`** — це історія змін
4. **Не створюй дублікатів** — перевіряй `index.md` перед створенням
5. **Кожен файл має frontmatter** — без цього лінт не пройде
6. **Теги тільки з taxonomy** — додавай нові теги до `SCHEMA.md` спочатку
7. **Сторінки >200 рядків** — розділяй на підтеми
8. **wiki/comparisons/ — в git** — це синтезовані сторінки, не кеш

## Зовнішні інструменти

- **Obsidian** — відкриває папку як vault, `[[wikilinks]]` працюють як клікабельні посилання
- **GitHub** — версіонування, історія змін, спільна робота
- **Graphify CLI** — `graphify extract`, `graphify query`, `graphify cluster-only`
- **Hermes Agent** — autonomous knowledge management agent

---

**Wiki — це compounding knowledge. Кожна нова стаття робить всю базу ціннішою.**
