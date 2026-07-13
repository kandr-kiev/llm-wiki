# Інструкція для Master — Керування LLM Wiki

> Повний посібник з використання вікі: запити, команди, автоматизація, діагностика.
> Останнє оновлення: 2026-07-13

---

## 📐 Архітектура системи

```
┌─────────────────────────────────────────────────────────────┐
│  MASTER (Ви)                                                │
│  Куратор. Формулює запити, затверджує зміни, визначає       │
│  напрямок розвитку бази знань.                              │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  AGENT (Архіваріус)                                         │
│  Виконує: збір → інтеграція → лінтинг → логірування        │
│  Навички: llm-wiki, wiki-indexer, wiki-content-creation,    │
│           wiki-maintenance, wiki-doctor, wiki-autonomous    │
└──────────────────────────┬──────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
   ШАР 1 (Сирці)     ШАР 2 (Знання)    ШАР 3 (Правила)
   raw/              wiki/             SCHEMA.md
   (immutable)       (mutable)         (конвенції)
```

### Три шари — що є що:

| Шар | Шлях | Призначення | Хто редагує |
|-----|------|-------------|-------------|
| **1 — Сирці** | `raw/` | Незмінні джерела (статті, папери, транскрипти) | Agent тільки (зберігає) |
| **2 — Знання** | `wiki/` | Синтезовані сторінки (concept, entity, comparison...) | Agent (створює/оновлює) |
| **3 — Правила** | `SCHEMA.md` | Теги, типи, конвенції валідації | Master + Agent |

---

## 🗣️ Запити до Agent — що писати

### 🔍 Пошук та запитання

| Запит | Що зробить | Приклад |
|-------|-----------|---------|
| `"Що wiki знає про [тема]?"` | Пошук по index.md → читання релевантних сторінок → синтез відповіді | `Що wiki знає про RAG?` |
| `"Зібери все про [тема]"` | Глибокий пошук по всім `.md` файлам → синтез з цитуванням джерел | `Зібери все про LoRA` |
| `"Порівняй [A] vs [B]"` | Створить або знайде comparison-сторінку | `Порівняй vLLM vs TGI` |
| `"Що нового про [тема]?"` | Перевірить log.md за останній час → знайде оновлені сторінки | `Що нового про AI agents?` |

### ✍️ Створення контенту

| Запит | Що зробить | Приклад |
|-------|-----------|---------|
| `"Додай цю статтю: [URL]"` | web_extract → raw/articles/ → створить wiki-сторінки → оновить index.md | `Додай цю статтю: https://...` |
| `"Створи playbook про [тема]"` | Створить детальний runbook з кроками, таблицями, troubleshooting | `Створи playbook про deployment LLM` |
| `"Створи synthesis про [тема]"` | Поєднає 3+ джерела → новий синтез з висновками | `Створи synthesis про AI agents 2026` |
| `"Збери N статей про [тема]"` | web_search → web_extract → raw/ → інтеграція | `Збери 5 статей про quantization` |
| `"Створи entity про [компанія/модель]"` | Створить сторінку з фактами, продуктами, інфраструктурою | `Створи entity про Mistral AI` |

### 🛠️ Обслуговування та діагностика

| Запит | Що зробить | Приклад |
|-------|-----------|---------|
| `"Перевір стан wiki"` | Запускає wiki_doctor.py → структурований звіт | `Перевір стан wiki` |
| `"Запусти лінт"` | `python3 tools/wiki_lint.py` → список помилок | `Запусти лінт` |
| `"Знайди дублікати"` | Пошук `_N` суфіксів, однакових slug | `Знайди дублікати` |
| `"Онови теги"` | Синхронізує SCHEMA.md ↔ wiki_lint.py APPROVED_TAGS | `Онови теги` |
| `"Аудит індексу"` | Перевірить index.md на дублікати, пропущені сторінки | `Аудит індексу` |

---

## ⚙️ Команди через terminal — безпосередній доступ

### Лінтинг та діагностика

```bash
# Повна діагностика (6 шарів)
python3 tools/wiki_doctor.py diagnose

# Діагностика + автоматичне лікування
python3 tools/wiki_doctor.py cure

# Класичний лінт
python3 tools/wiki_lint.py

# Перевірка SHA256 хешів
python3 scripts/verify_sha256.py /workspace/llm-wiki --fix
```

### Пошук та аналіз

```bash
# Знайти сторінки за ключовим словом
search_files "transformer" path="/workspace/llm-wiki/wiki" file_glob="*.md"

# Знайти сторінки за тегом
search_files "tags:.*quantization" path="/workspace/llm-wiki/wiki" file_glob="*.md"

# Статистика
find wiki/ -name "*.md" -not -name "README.md" | wc -l    # кількість сторінок
find raw/ -name "*.md" | wc -l                              # кількість сирців
du -sh wiki/ raw/ tools/                                    # розміри

# Знайти сторінки без wikilinks (ізоляти)
grep -L "\[\[" wiki/concepts/*.md wiki/entities/*.md
```

### Індексація

```bash
# Перегенерувати index.md з нуля
python3 tools/regenerate_index.py

# Перевірити, чи всі сторінки в індексі
python3 tools/check_index_completeness.py
```

---

## 🤖 Автоматизація — Cron Jobs

### Поточні задачі (6 штук)

| Назва | Частота | Що робить | Статус |
|-------|---------|-----------|--------|
| **RSS Feed Monitor** | 2× на добу (00:00, 12:00) | Моніторинг RSS-каналів → збір нових статей | ✅ Активна |
| **GitHub Release Monitor** | 2× на добу (02:00, 14:00) | Моніторинг релізів AI/LLM репозиторіїв | ✅ Активна |
| **Local File Monitor** | 2× на добу (04:00, 16:00) | Сканування локальних директорій | ✅ Активна |
| **Wiki Integrator** | 2× на добу (06:00, 18:00) | raw/ → wiki/ (класифікація, генерація) | ✅ Активна |
| **Wiki Raw Scanner** | Кожні 6 годин | Перевірка нових файлів у raw/ | ✅ Активна |
| **Wiki Weekly Digest** | Щопонеділка 09:00 | Повний аудит якості wiki | ✅ Активна |

### Як працює піплайн:

```
RSS/GitHub/Local → raw/articles/*.md → integrator.py → wiki/{type}/*.md
     ↓                  ↓                   ↓              ↓
  Monitor          SHA256 verified    Classify +      Index + Log
  every 2-6h       Immutable          Generate        Updated
```

### Керування Cron Jobs

```
# Подивитись всі задачі
cronjob(action='list')

# Створити нову задачу
cronjob(action='create', schedule='every 4h', prompt='...')

# Зупинити задачу
cronjob(action='pause', job_id='...')

# Перезапустити задачу
cronjob(action='resume', job_id='...')
```

---

## 📋 Структура wiki-сторінок

### Типи сторінок

| Тип | Призначення | Приклад |
|-----|-----------|---------|
| **concept** | Повторно використовувані знання (методи, теорії) | `llm-quantization`, `prompt-engineering` |
| **entity** | Конкретні речі (моделі, компанії, люди) | `openai`, `mistral`, `gpt-4` |
| **comparison** | Порівняння альтернатив | `vllm-vs-tgi`, `lora-vs-qlora` |
| **playbook** | Покрокові інструкції | `how-to-deploy-llm`, `how-to-fine-tune` |
| **synthesis** | Інтеграція 3+ джерел | `ai-agents-2026-synthesis` |
| **query** | Зафіксовані відповіді на FAQ | `llm-deployment-qa` |
| **reference** | Конфігурації, шаблони, статичні дані | `llm-deployment-configs` |

### Frontmatter — обов'язкові поля

```yaml
---
title: "Назва сторінки"
type: concept | entity | comparison | playbook | synthesis | query | reference
description: "Однорядковий опис"
created: 2026-07-12
updated: 2026-07-12
tags: [tag1, tag2, tag3]
sources: [raw/articles/source.md]
confidence: high | medium | low
links: [related-page-1, related-page-2]
---
```

**Правила frontmatter:**
- `tags` — ТИЛЬКИ з taxonomy в SCHEMA.md (184 теги)
- `confidence` — `high` (підтверджено джерелами), `medium` (одне джерело), `low` (гіпотеза)
- `sources` — лише реальні файли на диску
- `links` — мінімум 2 wikilinks на сторінку

---

## 🚨 Поточні проблеми системи (2026-07-12)

| Проблема | Серйозність | Кількість | Як виправити |
|----------|------------|-----------|-------------|
| **Missing frontmatter** | 🔴 ERROR | ~20 файлів | `wiki_doctor.py cure` |
| **Tag drift** | 🟡 WARN | 24 теги не в SCHEMA.md | Оновити SCHEMA.md + wiki_lint.py |
| **Index metadata** | 🟡 WARN | index.md без "Last updated" | Регенерувати index.md |
| **Raw frontmatter** | 🔴 ERROR | 1 файл | Додати frontmatter вручну |
| **Page size >200** | 🟡 WARN | 2 файли (playbook/synthesis) | Не критично |

### Статистика на сьогодні:

| Показник | Значення |
|----------|---------|
| Сторінки wiki | 407 |
| Сирі джерела (raw/) | 591 |
| Скриптів інфраструктури | 15 |
| Тегів у taxonomy | 184 |
| Cron задач | 6 |
| ERROR лінтингу | ~20 |
| WARN лінтингу | 4 |

---

## 🔄 Роадмап розвитку системи

### Phase 1: Stabilization (✅ Done)
- [x] Базова структура wiki
- [x] 400+ сторінок
- [x] 6 cron jobs
- [x] Лінтинг + Doctor
- [x] Autonomous monitoring

### Phase 2: Quality (🔄 In Progress)
- [ ] Виправити 20 ERROR frontmatter
- [ ] Синхронізувати 24 теги
- [ ] Регенерувати index.md
- [ ] Виправити broken wikilinks
- [ ] Fix SHA256 drift

### Phase 3: Intelligence (📋 Planned)
- [ ] Semantic relevance scoring (замість keyword-based)
- [ ] Knowledge gap detection (tag graph analysis)
- [ ] Auto-suggestion: "що шукати далі"
- [ ] Cross-reference recommendations

### Phase 4: Recall (📋 Planned)
- [ ] Weekly session_search для "forgotten context"
- [ ] Перевірка оновлення старих тем
- [ ] Автоматична актуалізація застарілих сторінок

### Phase 5: Advanced Automation (📋 Planned)
- [ ] Multi-agent collection (розділення збирач/синтезатор)
- [ ] LLM-based classification (замість rule-based)
- [ ] Automated synthesis generation
- [ ] Integration with Obsidian Sync (headless mode)

### Phase 6: Analytics (📋 Planned)
- [ ] Growth metrics (сторінки/тиждень, теги/місяць)
- [ ] Coverage analysis (які теми покриті, які ні)
- [ ] Quality score (confidence distribution, link density)
- [ ] Trend detection (які теми зростають)

---

## 📌 Золоті правила

1. **Ніколи не редагуй `raw/`** — це незмінні джерела. Виправлення йдуть у wiki-сторінки.
2. **Завжди оновлюй `index.md`** — без цього wiki деградує.
3. **Завжди оновлюй `log.md`** — це історія змін. Використовуй `patch`, ніколи `write_file`.
4. **Не створюй дублікатів** — перевіряй `index.md` та `search_files` перед створенням.
5. **Кожен файл має frontmatter** — без цього лінт не пройде.
6. **Теги тільки з taxonomy** — додавай нові теги до `SCHEMA.md` спочатку, потім до `wiki_lint.py`.
7. **Сторінки >200 рядків** — розділяй на підтеми з cross-links.
8. **Мінімум 2 wikilinks** — кожна сторінка має посилатись на інші.
9. **Confidence — завжди** — `high`, `medium` або `low` для кожної сторінки.
10. **Попереджай про масові зміни** — якщо інтеграція торкнеться 10+ сторінок, повідом Master.

---

## 🎯 Чек-лист: перші кроки нового Master

- [ ] 1. Прочитати README.md — загальне розуміння
- [ ] 2. Прочитати SCHEMA.md — теги, типи, правила
- [ ] 3. Запустити `wiki_doctor.py diagnose` — поточний стан здоров'я
- [ ] 4. Запустити `wiki_lint.py` — конкретні помилки
- [ ] 5. `cronjob(action='list')` — що автоматизовано
- [ ] 6. `read_file("log.md", offset=last-30)` — останні дії
- [ ] 7. `read_file("index.md")` — що вже є в базі
- [ ] 8. `search_files("ваша-тема")` — перевірити наявність контенту

---

## 💬 Приклади запитів з реальних сесій

Ось конкретні запити, які ви вже використовували — як шаблони для майбутнього:

| Ваш запит | Що я зробив | Результат |
|-----------|-------------|-----------|
| `"додай в блоки інструментів короткий опис що робить кожний"` | Оновив HTML-діаграму: додав іконки, назви, описи для 15 інструментів | `architecture/llm-wiki-architecture.html` v6.1.1 |
| `"проаналізуй ці помилки: openai/clip — 404, meta-llama/llama — 404"` | Виявив архівовані репозиторії, пропонувати видалити | Список REPOS зменшено з 21 → 19 |
| `"так"` (підтвердження видалення) | Видалив `openai/clip` та `meta-llama/llama` з `github_release_monitor.py` | Commit `02af2d3` → `origin/main` |
| `"не прийшо, чекаю на доповідь"` | MEDIA: не працює через Docker vs Windows — шукав токен бота | Проблема з MEDIA: шляхами, знайдено рішення |
| `"та зайшов у цикл, спробуй інший підхід"` | Перейшов до прямої відправки через Telegram Bot API | MEDIA: шлях як фінальне рішення |
| `"коміть і пуш, потім подивлюсь"` | Git commit + push з оновленою діаграмою | Commit `81cc79e` → `origin/main` |

---

## 🔀 Розширені сценарії — комбіновані запити

Один запит може виконати кілька дій одночасно:

| Сценарій | Запит | Що відбудеться |
|----------|-------|----------------|
| **Дослідження + документування** | `"Досліджи RAG, порівняй з vector DB, створи playbook"` | Пошук → аналіз → створення concept + comparison + playbook |
| **Аудит + фікс** | `"Перевір стан wiki і виправ критичні помилки"` | wiki_doctor.py diagnose → cure → звіт |
| **Моніторинг + інтеграція** | `"Збери всі нові релізи OpenAI за останній тиждень і інтегруй"` | github_release.py → raw/ → integrator.py → wiki/ |
| **Оновлення + рефакторинг** | `"Онови інструкцію для Master і додай приклади з реальних сесій"` | read_file → patch → commit → push |
| **Повний аудит** | `"Зроби повний аудит: лінт, доктор, індекс, статистика, cron"` | Запуск всіх інструментів → консолідований звіт |
| **Пошук пробілів** | `"Які теми в AI/LLM найгірше покриті в нашій базі?"` | Аналіз tag graph → виявлення відсутніх категорій → рекомендації |

---

## 🏷️ Як додати новий тег

Покрокова інструкція додавання нового тегу до taxonomy:

### Крок 1: Додати до SCHEMA.md
```markdown
# У секції тегів додати новий запис:
| your-new-tag | Опис тегу | category-name |
```

### Крок 2: Синхронізувати з wiki_lint.py
```python
# У tools/wiki_lint.py оновити APPROVED_TAGS:
APPROVED_TAGS = {
    ...
    "your-new-tag": {
        "description": "Опис тегу",
        "category": "category-name"
    },
}
```

### Крок 3: Застосувати до існуючих сторінок
```bash
# Вручну або через Agent:
"Застосуй тег 'your-new-tag' до всіх сторінок про [тема]"
```

### Крок 4: Перевірити
```bash
# Перевірка:
python3 tools/wiki_lint.py
# Перевірити, що новий тег валідний
```

### Приклад: додавання тегу `"speculative-decoding"`
```markdown
# SCHEMA.md:
| speculative-decoding | Speculative decoding methods | inference-optimization |

# wiki_lint.py:
"speculative-decoding": {
    "description": "Speculative decoding methods",
    "category": "inference-optimization"
},
```

---

## ⚠️ Типові помилки та як їх уникнути

### MEDIA: шляхи не працюють
**Проблема:** MEDIA:/workspace/... — це Docker-шляхи, але gateway на хості (Windows) їх не бачить.
**Рішення:** Використовувати Telegram Bot API напряму або webhook.
**Коли трапляється:** Коли потрібно надіслати зображення/файл у Telegram зсередини Docker.

### Rate limit GitHub API
**Проблема:** 403 Forbidden — ліміт API GitHub вичерпано.
**Рішення:** Використовувати GITHUB_TOKEN для аутентифікації (6000 req/h замість 60 req/h).
**Коли трапляється:** При інтенсивному скануванні багатьох репозиторіїв.

### SHA256 drift
**Проблема:** Хеш тіла файлу не збігається з хешем у frontmatter.
**Рішення:** `python3 tools/wiki_doctor.py cure` — автоматичне виправлення.
**Коли трапляється:** Після редагування файлів вручну або через write_file.

### Дублікати сторінок
**Проблема:** Кілька файлів з однаковим slug (напр., `rag.md`, `rag_1.md`, `rag_2.md`).
**Рішення:** `python3 tools/cleanup_duplicates.py --apply` — видалення дублікатів.
**Коли трапляється:** При повторному створенні сторінки без перевірки index.md.

### Архівовані репозиторії
**Проблема:** 404 Not Found для репозиторіїв, які більше не існують.
**Рішення:** Видалити з REPOS списку в `github_release_monitor.py` або `github_monitor.py`.
**Коли трапляється:** При моніторингу репозиторіїв, що були архівовано/переміщено.

### Frontmatter missing
**Проблема:** Файл без YAML frontmatter — лінт не пройде.
**Рішення:** Додати frontmatter вручну або через `build_frontmatter()` з utils.py.
**Коли трапляється:** При створенні файлів поза стандартним піплайном.

---

## 🐙 Як додати новий репозиторій до моніторингу

### Для github_release_monitor.py (релізи)
1. Відкрити `tools/github_release_monitor.py`
2. Додати в список `REPOS` (line 42-71):
```python
REPOS = [
    ...
    "owner/repo",  # новий репозиторій
    ...
]
```
3. Commit та push.

### Для github_monitor.py (issues/PRs)
1. Відкрити `tools/github_monitor.py`
2. Додати в список `REPOS` (line 41-60):
```python
REPOS = [
    ...
    "owner/repo",  # новий репозиторій
    ...
]
```
3. Commit та push.

### Як перевірити
```bash
# Запустити монітор вручну:
python3 tools/github_release_monitor.py
python3 tools/github_monitor.py

# Перевірити результат:
ls -la raw/articles/ | grep gh-
```

### Як видалити репозиторій
1. Видалити рядок з REPOS списку
2. Commit та push
3. (Опціонально) Видалити старі raw-файли:
```bash
rm raw/articles/gh-owner-repo-*.md
```

---

## ⏰ Як працювати з cron

### Подивитись всі задачі
```
cronjob(action='list')
```

### Створити нову задачу
```
# Простий приклад — кожні 4 години:
cronjob(action='create', schedule='every 4h', prompt='Перевір стан wiki')

# З навичками:
cronjob(action='create', schedule='0 9 * * *', prompt='Згенерувати тижневий дайджест', skills=['wiki-maintenance', 'wiki-content-creation'])

# З прив'язкою до моделі (для стабільності):
cronjob(action='create', schedule='every 6h', prompt='...', model={'provider': 'openrouter', 'model': 'qwen3.6-35b-a3b'})
```

### Керування існуючими задачами
```
# Зупинити задачу:
cronjob(action='pause', job_id='...')

# Перезапустити:
cronjob(action='resume', job_id='...')

# Оновити розклад:
cronjob(action='update', job_id='...', schedule='every 12h')

# Видалити задачу:
cronjob(action='remove', job_id='...')

# Запустити вручну:
cronjob(action='run', job_id='...')
```

### Параметри cronjob
| Параметр | Опис | Приклад |
|----------|------|---------|
| `action` | Дія: create, list, update, pause, resume, remove, run | `create` |
| `schedule` | Частота: '30m', 'every 2h', '0 9 * * *', ISO timestamp | `'every 4h'` |
| `prompt` | Текст завдання (self-contained) | `'Перевір стан wiki'` |
| `skills` | Навички для завантаження | `['wiki-maintenance']` |
| `model` | Модель для виконання (опціонально) | `{'provider': 'openrouter', 'model': 'qwen3.6-35b-a3b'}` |
| `deliver` | Куди доставити результат | `'origin'`, `'all'`, `'telegram:chat_id:thread_id'` |
| `name` | Людино-читабельна назва | `'Wiki Weekly Audit'` |

### Поточні задачі
| Назва | Частота | Результат |
|-------|---------|-----------|
| RSS Feed Monitor | 2× на добу (00:00, 12:00) | Нові статті в raw/ |
| GitHub Release Monitor | 2× на добу (02:00, 14:00) | Релізи в raw/ |
| Local File Monitor | 2× на добу (04:00, 16:00) | Зміни в raw/ |
| Wiki Integrator | 2× на добу (06:00, 18:00) | wiki-сторінки з raw/ |
| Wiki Raw Scanner | Кожні 6 годин | Звіт про нові файли |
| Wiki Weekly Digest | Щопонеділка 09:00 | Повний аудит якості |

---

## 🆕 Як створити новий тип сторінки

### Крок 1: Додати тип до SCHEMA.md
```markdown
# У секції VALID_TYPES додати новий тип:
| new-type | Короткий опис | Описує [що саме] |
```

### Крок 2: Оновити валідацію у wiki_lint.py
```python
# У tools/wiki_lint.py оновити VALID_TYPES:
VALID_TYPES = ['concept', 'entity', 'comparison', 'playbook', 'synthesis', 'query', 'reference', 'new-type']
```

### Крок 3: Створити шаблон
```markdown
# wiki/templates/Новий new-type.md:
---
title: "Назва сторінки"
type: new-type
description: "Однорядковий опис"
created: {{date}}
updated: {{date}}
tags: []
sources: []
confidence: medium
links: []
---

# {{title}}

Тут контент...
```

### Крок 4: Оновити index.md
```python
# У tools/regenerate_index.py додати обробку нового типу:
if page_type == 'new-type':
    section = '## 🆕 New Type Pages'
```

### Крок 5: Перевірити
```bash
python3 tools/wiki_lint.py
# Перевірити, що новий тип валідний
```

### Приклад: додавання типу `"benchmark"`
```markdown
# SCHEMA.md:
| benchmark | Benchmarks та оцінки моделей | Описує бенчмарки для оцінки LLM |

# wiki/templates/Новий benchmark.md:
---
title: "Назва бенчмарку"
type: benchmark
description: "Однорядковий опис"
created: {{date}}
updated: {{date}}
tags: [benchmark, evaluation]
sources: []
confidence: high
links: []
---

# {{title}}

## Методологія
...

## Результати
...

## Висновки
...
```

---

## 📊 Як переглянути статистику системи

### Швидка статистика
```bash
# Кількість сторінок wiki
find wiki/ -name "*.md" -not -name "README.md" | wc -l

# Кількість сирців
find raw/ -name "*.md" | wc -l

# Кількість скриптів
find tools/ -name "*.py" | wc -l

# Розміри
du -sh wiki/ raw/ tools/
```

### Детальна статистика
```bash
# Запустити wiki_doctor.py для повного звіту
python3 tools/wiki_doctor.py diagnose

# Запустити лінт для детального звіту
python3 tools/wiki_lint.py

# Подивитись останні дії
read_file("log.md", offset=last-30)
```

### Статистика за типами сторінок
```bash
# Кількість сторінок за типом
for type in concept entity comparison playbook synthesis query reference; do
    echo "$type: $(find wiki/$type/ -name '*.md' 2>/dev/null | wc -l)"
done

# Кількість тегів
python3 -c "
import os, re
tags = set()
for f in os.listdir('wiki'):
    d = os.path.join('wiki', f)
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.md'):
                fp = os.path.join(d, fn)
                with open(fp) as fh:
                    content = fh.read()
                    if 'tags: [' in content:
                        start = content.find('tags: [')
                        end = content.find(']', start)
                        if end > start:
                            tag_str = content[start:end+1]
                            m = re.search(r'tags:\s*\[(.*?)\]', tag_str)
                            if m:
                                for t in m.group(1).split(','):
                                    t = t.strip().strip('\"').strip(\"'\")
                                    if t: tags.add(t)
print(f'Unique tags: {len(tags)}')
for t in sorted(tags):
    print(f'  - {t}')
"
```

---

## 📌 Золоті правила

1. **Ніколи не редагуй `raw/`** — це незмінні джерела. Виправлення йдуть у wiki-сторінки.
2. **Завжди оновлюй `index.md`** — без цього wiki деградує.
3. **Завжди оновлюй `log.md`** — це історія змін. Використовуй `patch`, ніколи `write_file`.
4. **Не створюй дублікатів** — перевіряй `index.md` та `search_files` перед створенням.
5. **Кожен файл має frontmatter** — без цього лінт не пройде.
6. **Теги тільки з taxonomy** — додавай нові теги до `SCHEMA.md` спочатку, потім до `wiki_lint.py`.
7. **Сторінки >200 рядків** — розділяй на підтеми з cross-links.
8. **Мінімум 2 wikilinks** — кожна сторінка має посилатись на інші.
9. **Confidence — завжди** — `high`, `medium` або `low` для кожної сторінки.
10. **Попереджай про масові зміни** — якщо інтеграція торкнеться 10+ сторінок, повідом Master.

---

## 🎯 Чек-лист: перші кроки нового Master

- [ ] 1. Прочитати README.md — загальне розуміння
- [ ] 2. Прочитати SCHEMA.md — теги, типи, правила
- [ ] 3. Запустити `wiki_doctor.py diagnose` — поточний стан здоров'я
- [ ] 4. Запустити `wiki_lint.py` — конкретні помилки
- [ ] 5. `cronjob(action='list')` — що автоматизовано
- [ ] 6. `read_file("log.md", offset=last-30)` — останні дії
- [ ] 7. `read_file("index.md")` — що вже є в базі
- [ ] 8. `search_files("ваша-тема")` — перевірити наявність контенту

---

**Wiki — це compounding knowledge. Кожна нова стаття робить всю базу ціннішою.**
