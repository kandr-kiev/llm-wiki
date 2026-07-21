# Roadmap — Розвиток LLM Wiki Knowledge Base

> Стратегічний план еволюції системи знань: від стабілізації до автономного інтелекту.
> Створено: 2026-07-12

---

## 📊 Поточний стан (Baseline)

| Параметр | Значення | Коментар |
|----------|---------|----------|
| Сторінок wiki | 1204 | Зростання з 407 до 1204 (×3) |
| Сирців (raw/) | 1774 | Зростання з 591 до 1774 (×3) |
| Скриптів | 23 | Зросло з 15 до 23 |
| Cron задач | 3 | Зменшено з 6 до 3 (50% economy) |
| Тегів taxonomy | 262 | Зросло з 184 до 262 (APPROVED_TAGS) |
| ERROR лінтингу | 0 | Виправлено wiki_doctor — [CLEAN] статус |
| WARN лінтингу | 0 | Tag drift виправлено |

### 🔴 Критичні проблеми (Blockers)

**Всі виправлені станом на 2026-07-11:**

1. ✅ **Frontmatter** — wiki_doctor [CLEAN], 0 ERROR
2. ✅ **Теги** — APPROVED_TAGS уніфіковано в utils.py (262 теги)
3. ✅ **index.md** — оновлюється інтегратором автоматично
4. ✅ **SHA256 drift** — fix_sha256.py виправив 158+ файлів

---

## 🗺️ Фази розвитку

### Phase 1: Stabilization ✅ ЗАВЕРШЕНА

**Мета:** Базова інфраструктура працює стабільно.

**Результати:**
- ✅ Структура wiki з 3 шарів
- ✅ 1200+ wiki-сторінок (з 400+)
- ✅ 3 autonomous cron jobs (50% economy: 6→3)
- ✅ wiki_doctor + wiki_lint
- ✅ RSS/GitHub/Local monitoring
- ✅ Integrator pipeline
- ✅ Central utils: utils.py (SHA256, frontmatter, tags)

**Час:** July 10-12, 2026
**Поточний стан:** 2026-07-11 — Central utilities, 158 false-positives fixed

---

### Phase 2: Quality ✅ ЗАВЕРШЕНА

**Мета:** Виправити системні проблеми якості.

**Результати (2026-07-11):**
| # | Задача | Статус |
|---|--------|--------|
| 2.1 | Виправити frontmatter | ✅ wiki_doctor [CLEAN] |
| 2.2 | Синхронізувати теги | ✅ APPROVED_TAGS у utils.py (262) |
| 2.3 | Регенерувати index.md | ✅ Автоматично інтегратором |
| 2.4 | Виправити broken wikilinks | ✅ wiki_doctor auto-cure |
| 2.5 | Fix SHA256 drift | ✅ fix_sha256.py (158+ файлів) |
| 2.6 | Вилучити дублікати `_N` | ✅ cleanup_duplicates.py |
| 2.7 | Виправити raw без frontmatter | ✅ |

**Критерій успіху:** `wiki_doctor.py cure` → `[CLEAN]` статус, 0 ERROR ✅ Досягнуто

---

### Phase 3: Intelligence 📋 ЗАПЛАНИВАНА

**Мета:** Система починає "думати" — пропонує, що шукати далі.

#### 3.1 Semantic Relevance Scoring
**Проблема:** Поточний integrator використовує keyword-based scoring (3-2-1 бали).
**Рішення:** LLM-based relevance assessment для кожної нової статті.

```python
# Поточний підхід (keyword-based)
score = sum(keyword_weights[word] for word in text.split())
# 3 points: gpt, claude, llama, openai
# 2 points: transformer, rag, fine-tuning
# 1 point: python, docker

# Новий підхід (LLM-based)
prompt = """Оціни релевантність статті для AI/LLM wiki (1-10):
[article content]
Відповідь: тільки число."""
score = llm_score(prompt)
```

#### 3.2 Knowledge Gap Detection
**Мета:** Автоматично виявляти пробіли в знаннях.

```python
# Tag graph analysis (вже є у wiki-maintenance)
# Знайти теги з 1 сторінкою → пропонувати джерела
# Знайти ізоляторні сторінки (0 wikilinks) → пропонувати зв'язки
# Знайти co-occurrence patterns → пропонувати synthesis
```

#### 3.3 Auto-Suggestion Engine
**Мета:** Agent пропонує Master'у: "Що шукати далі".

```
📌 Auto-suggestion (щотижня):

На основі tag graph analysis:
• `xai` — тільки 1 сторінка, але co-occurs з `llm` 5x → знайти джерела
• `multimodal` — тільки 1 сторінка, co-occurs з `diffusion` 3x → synthesis
• `biomedical` — 0 сторінок, але згадується в 3 raw файлах → ingest

📌 Cross-reference recommendations:
• `llm-quantization.md` має 0 inbound links → додати посилання з `gpt`, `llama`
• `vllm.md` не посилається на `inference-chip.md` → додати link
```

#### 3.4 Contextual Recall
**Мета:** Система нагадує про застарілі теми.

```python
# Weekly: session_search() → знайти старі запити
# Для кожного запиту → перевірити, чи оновлено wiki-сторінку
# Якщо ні → flag для review
```

**Критерій успіху:** Agent щотижня генерує auto-suggestion report з 5+ recommendations.

**Timebox:** 2-3 тижні.

---

### Phase 4: Advanced Automation 📋 ЗАПЛАНИВАНА

**Мета:** Розділити ролі, зменшити моноліт.

#### 4.1 Multi-Agent Collection Pattern
**Розділення:**
- **Collector Agent:** web_search → web_extract → raw/ (без reasoning)
- **Synthesizer Agent:** raw/ → wiki/ (з reasoning, cross-references)
- **Maintainer Agent:** лінтинг, repair, cleanup (periodic)

```
Collector → raw/ → Synthesizer → wiki/ → Maintainer → health check
   (fast)      (immutable)     (slow)     (mutable)    (periodic)
```

**Переваги:**
- Collector може бути швидкою моделлю (менше токенів)
- Synthesizer — потужна модель (якість синтезу)
- Maintainer — простий скрипт (мінімальні витрати)

#### 4.2 Automated Synthesis Generation
**Мета:** Автоматично створювати synthesis-сторінки коли знайдено 3+ статті на тему.

```python
# Trigger: >3 нових файлів з однаковими тегами за тиждень
# Action: запустити synthesis generation
# Input: всі raw файли з тегом
# Output: wiki/synthesis/topic-synthesis.md
```

#### 4.3 Obsidian Sync Integration
**Мета:** Real-time синхронізація між сервером та Obsidian Desktop.

```bash
# Setup obsidian-headless
npm install -g obsidian-headless
ob login --email <email> --password <pass>
ob sync-create-remote --name "LLM Wiki"
cd /workspace/llm-wiki
ob sync-setup --vault <vault-id>
ob sync --continuous  # systemd service
```

**Критерій успіху:** Зміни в wiki/ з'являються в Obsidian Desktop протягом 5 секунд.

**Timebox:** 1 тиждень (Obsidian Sync) + 2 тижні (multi-agent).

---

### Phase 5: Analytics 📋 ЗАПЛАНИВАНА

**Мета:** Вимірювати стан системи, виявляти тренди.

#### 5.1 Growth Metrics
```python
# Щодня/тиждень:
- new_pages (додавання)
- updated_pages (оновлення)
- deleted_pages (архівування)
- orphan_pages (втрачені зв'язки)
- avg_links_per_page (середня кількість wikilinks)
- tag_distribution (розподіл тегів)
```

#### 5.2 Coverage Analysis
```python
# Які теми покриті, які ні?
- AI/ML Core: 48 tagів → скільки мають ≥2 сторінки?
- Applications: 18 tagів → скільки мають ≥1 сторінку?
- Missing: теги з 0 сторінок → candidate для вилучення з taxonomy
```

#### 5.3 Quality Score
```python
# Композитний score для кожної сторінки:
score = (
    has_frontmatter * 20 +
    has_confidence * 10 +
    outbound_links_count * 5 +
    inbound_links_count * 5 +
    source_count * 5 +
    recency_bonus  # recent updates
)
# Pages з score < 50 → flag для review
```

#### 5.4 Trend Detection
```python
# Які теми зростають?
- tag_usage_over_time (які теги з'являються частіше)
- new_entity_frequency (скільки нових компаній/моделей)
- synthesis_frequency (скільки synthesis створено)
```

**Критерій успіху:** Weekly analytics report з графіками та трендами.

**Timebox:** 2 тижні.

---

### Phase 6: Ecosystem 📋 ЗАПЛАНИВАНА

**Мета:** Інтеграція з зовнішніми системами.

| Інтеграція | Призначення | Статус |
|-----------|------------|--------|
| **GitHub API** | Автоматичне створення issues для low-quality pages | 📋 Planned |
| **Slack/Discord** | Notifications про нові статті, alerts | 📋 Planned |
| **Web Dashboard** | Візуалізація графа знань, метрик | 📋 Planned |
| **Wiki Dashboard UI** | Повноцінний UI — центр керування LLM-Wiki (статистика, лінтинг, інгест, cron) | 💡 Ідея |
| **API Endpoint** | REST API для запитів до wiki | 📋 Planned |
| **Browser Extension** | "Add to Wiki" кнопка в браузері | 📋 Planned |
| **Email Digest** | Щотижневий digest на email | 📋 Planned |

---

## 📈 Метрики успіху

| Фаза | KPI | Ціль |
|------|-----|------|
| **P1** | wiki_doctor `[CLEAN]` | ✅ Досягнуто |
| **P2** | 0 ERROR лінтингу | 0 |
| **P3** | Auto-suggestions/тиждень | ≥5 |
| **P4** | Token cost per ingest | -50% |
| **P5** | Quality Score avg | ≥70 |
| **P6** | External integrations | ≥3 |

---

## 🔄 Зворотний зв'язок

Цей roadmap — living document. Оновлюється при:
- Зміні пріоритетів Master
- Виявленні критичних проблем
- З'ясуванні нових можливостей
- Зміні архітектури Hermes Agent

**Останнє оновлення:** 2026-07-21
**Наступний аудит:** 2026-08-21
