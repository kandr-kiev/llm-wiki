# Інструкція для Master: керування LLM Wiki

## 🎯 Що таке LLM Wiki

Це твоя **персистентна база знань** про AI/LLM, побудована за патерном Karpathy. На відміну від RAG (який щоразу шукає знання з нуля), wiki компілює знання один раз і тримає їх актуальними. Кожна нова стаття розширює всю базу — це compounding effect.

**Архітектура з 3 шарів:**

```
Шар 1: raw/         — незмінні джерела (сирці)
Шар 2: wiki/        — синтезовані сторінки (concept, entity, comparison...)
Шар 3: SCHEMA.md    — правила та конвенції
```

---

## 👥 Роль агента Монті

Монті — твій **помічник-збиральник**. Він:
- ✅ Знаходить статті та папери
- ✅ Витягує контент з URL
- ✅ Зберігає у `raw/` у правильному форматі
- ❌ НЕ створює wiki-сторінки
- ❌ НЕ аналізує, НЕ синтезує

Ти — **куратор**. Монті — **собиратель**.

---

## 📊 Поточний стан wiki

```
raw/                    — 16 сирців (immutable)
wiki/
├── concepts/           — 12 концептів
├── entities/           — 13 сутностей
├── comparisons/        — 2 порівняння
├── playbooks/          — 3 плейбуки
├── synthesis/          — 1 синтез
├── queries/            — 1 FAQ
├── references/         — 1 reference
└── templates/          — 8 шаблонів

Pages: 37 | Raw: 16 | Lint: 0 errors, 4 warnings (size)
```

---

## 🔧 Як керувати wiki

### 1. Додати нове джерело (ручний режим)

Ти можеш надати мені URL — я витягну, збережу у `raw/`, створю wiki-сторінки, оновлю index.md та log.md.

```
Master: "Додай цю статтю: https://blog.openai.com/gpt-4"
Архівіст: витягну → збережу → створю сторінки → оновлю індекс
```

### 2. Доручити збір Монті

Напиши мені:
```
Master: "Збери 5 статей про LLM inference optimization"
Архівіст: запущу Монті з цим промптом
```

Монті збереже сирці у `raw/`. Потім я (Архівіст) оброблю їх у wiki-сторінки.

### 3. Запитати про щось у wiki

```
Master: "Що wiki знає про LLM quantization?"
Архівіст: прочитаю відповідні сторінки, синтезую відповідь
```

### 4. Запустити лінт

```
Master: "Перевір стан wiki"
Архівіст: запущу wiki_lint.py, покажу issues
```

---

## 🚀 Можливості наповнення wiki

### А. Автоматичний збір (cron)

**Wiki Raw Scanner** — вже активний, працює кожні 2 години.
- Перевіряє `raw/articles/` на нові файли
- Перевіряє SHA256 drift
- Повідомляє про зміни

**Wiki Weekly Digest** — щопонеділка о 09:00.
- Генерує health report
- Перевіряє структуру, цілісність, orphaned pages
- Надсилає звіт у Telegram

### Б. Ручне наповнення — що шукати

#### Пріоритетні теми для наповнення:

| Тема | Чому важливо | Які джерела |
|---|---|---|
| **LLM Security** | Growing concern, few wiki pages | arXiv, blog posts, papers |
| **AI Regulation** | Policy changes, compliance | Gov sites, legal blogs |
| **MLOps Production** | Bridging research → production | Tech blogs, case studies |
| **Multimodal Models** | Next wave after text-only | OpenAI, Google, Meta blogs |
| **Edge AI / Mobile LLM** | On-device inference | Qualcomm, Apple, Samsung |
| **AI Agents in Production** | Real-world deployments | Tech company blogs |
| **Data Engineering for LLM** | Training data pipelines | Hugging Face, Weights & Biases |
| **LLM Evaluation** | Beyond benchmarks, real metrics | Papers, industry reports |
| **AI in Healthcare** | High-impact applications | Medical journals, case studies |
| **AI in Education** | Personalized learning | EdTech blogs, research |

#### Де шукати:

| Тип джерела | Приклади | Як витягти |
|---|---|---|
| **Офіційні блоги** | OpenAI, Anthropic, Google, Meta, Mistral, Qwen | `web_extract` |
| **arXiv** | Наукові папери | `web_extract` (PDF) або `arxiv` skill |
| **Hugging Face** | Models, datasets, papers | `web_extract` |
| **YouTube** | Ток-шоу, конференції | `youtube-content` skill |
| **Podcasts** | Lex Fridman, AI News | `youtube-content` або `web_extract` |
| **GitHub** | Open-source projects | `web_extract` README |
| **Twitter/X** | AI community discussions | `x_search` skill |
| **News** | The Verge, TechCrunch, Ars Technica | `web_search` + `web_extract` |

### В. Synthesis — поєднання джерел

Коли у `raw/` накопичиться 5+ джерел на одну тему, я можу створити **synthesis page** — інтегрований аналіз з кількох джерел.

```
Приклад: 5 статей про LoRA → synthesis "LLM Fine-Tuning Landscape 2026"
```

### Г. Comparisons — порівняння

Коли є 2+ джерела про різні моделі/інструменти, створю **comparison page**.

```
Приклад: Llama 3 vs Mistral v3 vs Qwen 2.5 → side-by-side table
```

### Д. Playbooks — практичні інструкції

На основі wiki-контенту створю **playbooks** — покрокові інструкції.

```
Приклад: "How to deploy Llama 3 on RTX 4090" → step-by-step runbook
```

---

## 📋 Твій workflow

### День 1: Визначити пріоритети
1. Подивись `index.md` — що вже є
2. Визнач 3-5 тем, яких не вистачає
3. Надішли мені список — я створю план

### День 2-3: Збір джерел
1. Ти знаходиш цікаві статті/папери
2. Надсилаєш мені URL — я зберігаю у `raw/`
3. АБО доручаєш Монті зібрати за темою

### День 4: Synthesis
1. Я оброблю сирці у wiki-сторінки
2. Створю comparisons та synthesis
3. Оновлю index.md та log.md

### День 5: Review
1. Перевіряємо стан wiki
2. Запускаємо лінт
3. Визначаємо наступні кроки

---

## 🛠️ Команди для тебе

| Команда | Що робить |
|---|---|
| `"Перевір стан wiki"` | Запускає лінт, показує issues |
| `"Додай цю статтю: [URL]"` | Зберігає у raw/, створює wiki-сторінки |
| `"Збери 5 статей про [тема]"` | Запускає Монті для збору |
| `"Створи synthesis про [тема]"` | Поєднує існуючі джерела |
| `"Створи comparison [A] vs [B]"` | Порівняння двох сутностей |
| `"Створи playbook для [завдання]"` | Практична інструкція |
| `"Що wiki знає про [тема]?"` | Пошук та синтез з існуючих сторінок |
| `"Покажи структуру wiki"` | Показує directory tree |
| `"Запусти лінт"` | `python3 tools/wiki_lint.py` |

---

## 📚 Зовнішні інструменти

### Obsidian Integration
Wiki — це звичайна папка з markdown файлами. Відкривай у Obsidian:
- `[[wikilinks]]` працюють як клікабельні посилання
- Graph View візуалізує мережу знань
- Dataview плагін дозволяє query по тегах

### Obsidian Headless (для серверів)
```bash
npm install -g obsidian-headless
ob login --email <email> --password '<password>'
cd /workspace/llm-wiki
ob sync-setup --vault "<vault-id>"
ob sync --continuous
```

### GitHub Integration
```bash
git init
git add .
git commit -m "Initial wiki commit"
git remote add origin git@github.com:user/llm-wiki.git
git push -u origin main
```

---

## ⚠️ Важливі правила

1. **Ніколи не редагуй `raw/`** — це незмінні джерела
2. **Завжди оновлюй `index.md`** — без цього wiki деградує
3. **Завжди оновлюй `log.md`** — це історія змін
4. **Не створюй дублікатів** — перевіряй `index.md` перед створенням
5. **Кожен файл має frontmatter** — без цього лінт не пройде
6. **Теги тільки з taxonomy** — додавай нові теги до `SCHEMA.md` спочатку
7. **Сторінки >200 рядків** — розділяй на підтеми

---

## 🎯 Пріоритети на найближчий тиждень

1. **Розширити entities** — додати 5-10 ключових компаній/моделей
2. **Створити 2-3 synthesis** — поєднати існуючі джерела
3. **Додати 3-5 new playbooks** — практичні інструкції
4. **Заповнити `raw/articles/`** — веб-статті, блоги, огляди
5. **Створити перший weekly digest** — перевірити cron job

---

## 💡 Поради

- **Якісні джерела > кількості.** Краще 3 якісні статті, ніж 10 слабких.
- **Синтез > дублікатів.** Краще об'єднати 3 статті у 1 synthesis, ніж створити 3 дублікати.
- **Посилання > ізольованих сторінок.** Кожна сторінка має посилатися на 2+ інших.
- **Актуальність > досконалості.** Краще опублікувати medium-confidence сторінку, ніж чекати ідеальної.
- **Регулярність > спорадичності.** Краще 5 статей на тиждень, ніж 50 раз на місяць.

---

**Пам'ятай:** Wiki — це compounding knowledge. Кожна нова стаття робить всю базу ціннішою. Починай з малого, рости поступово.