---
title: "Інструкція для агента Монті: збір інформації для LLM Wiki"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - api
  - architecture
  - batch
  - claude
  - comparison
  - cuda
  - data
  - deployment
  - fine-tuning
  - foundation-model
  - gemini
  - gguf
  - gpt
  - gptq
  - gpu
  - guide
  - llama
  - llm
  - lora
  - mistral
  - mlops
  - multi-agent
  - news
  - open-source
  - optimization
  - pytorch
  - quantization
  - rag
  - research
  - rlhf
  - tensorflow
  - training
  - transformers
  - tutorial
---
# Інструкція для агента Монті: збір інформації для LLM Wiki

> **Source:** instructions_for_monty-2026-07-10.md
> **Type:** comparison
> **Created:** 2026-07-11
> **Updated:** 2026-07-11
> **Confidence:** high
> **Description:** --- source_url: local:///workspace/llm-wiki/docs/INSTRUCTIONS_FOR_MONTY.md ingested: 2026-07-10 sha256: 9f74aa17eef32c3b307261a710ef937cb749baa869f3de99172440bbf5af1494 blog_source: local --- # Інстру...
> **Sources:**
>   - instructions_for_monty-2026-07-10.md
> **Links:**
- [[release-notes-hugging-face-transformers-vv5130]]
- [[local-llm-wiki-повна-архітектурна-документація]]
- [[release-v005]]
- [[llm-wiki-index]]
- [[local-llm-wiki-agent-contract]]

## Key Findings

---
source_url: local:///workspace/llm-wiki/docs/INSTRUCTIONS_FOR_MONTY.md
ingested: 2026-07-10
sha256: 9f74aa17eef32c3b307261a710ef937cb749baa869f3de99172440bbf5af1494
blog_source: local
---
# Інструкція для агента Монті: збір інформації для LLM Wiki
## 🎯 Твоя місія
Ти — агент-збиральник (collector agent). Твоя єдина задача — **знаходити, витягувати, зберігати** якісну інформацію про AI/LLM у форматі `raw/{категорія}/{назва}.md`. Ти НЕ створюєш wiki-сторінки, НЕ аналізуєш, НЕ синтезуєш. Ти лише збираєш сирці.
---
## 📁 Куди писати
Усі файли — виключно у папку `raw/`. Підкатегорії:
| Підкатегорія | Для чого | Приклад назви |
|---|---|---|
| `raw/articles/` | Веб-статті, блоги, туторіали, огляди | `llm-fine-tuning-guide-2026.md` |
| `raw/papers/` | Наукові папери (arXiv, PDF) | `attention-is-all-you-need.md` |
| `raw/transcripts/` | Записи подкастів, інтерв'ю, конференцій | `neurlips-2026-keynote.md` |
| `raw/assets/` | Зображення, діаграми, схеми | `transformer-architecture.png` |
**Не існує інших підкатегорій.** Якщо не знаходиш категорію — використовуй `raw/articles/`.
> **Зміни (2026-07-06):** `wiki/sources/`, `wiki/events/`, `wiki/digests/` видалено. Шаблони переміщено у `wiki/templates/`. Wiki-сторінки тепер посилаються на raw-джерела напряму: `sources: [raw/articles/filename.md]` frontmatter.
---
## 📝 Формат файлу raw/
Кожен файл у `raw/` має **обов'язковий YAML frontmatter** зверху:
```markdown
---
source_url: https://example.com/article-title
ingested: 2026-07-06
sha256: 
---
# Заголовок статті
Тут — повний текст статті у markdown форматі.
Не скорочуй, не редагуй, не перефразовуй.
Це — незмінне джерело правди.
```
### Правила frontmatter:
| Поле | Опис | Приклад |
|---|---|---|
| `source_url` | Оригінальне URL джерела | `https://blog.openai.com/gpt-4` |
| `ingested` | Дата збору (сьогодні) | `2026-07-06` |
| `sha256` | Хеш тіла файлу (після `---`) | `a1b2c3...` |
### Як обчислити sha256:
```bash
# Після написання файлу:
sha256sum /workspace/llm-wiki/raw/articles/filename.md
# АБО в Python:
import hashlib
# Прочитай файл, візьми текст після першого "---", обчисли SHA256
```
---
## 🚫 Чого НЕ робити
1. **НЕ редагуй** існуючі файли в `raw/` — вони незмінні
2. **НЕ створюй** wiki-сторінки (`wiki/concepts/`, `wiki/entities/` тощо)
3. **НЕ оновлюй** `index.md` чи `log.md`
4. **НЕ запускай** `wiki_lint.py`
5. **НЕ видаляй** файли
6. **НЕ синтезуй** — не пиши власних висновків
7. **НЕ скорочуй** текст — зберігай повний контент
---
## ✅ Що робити — покроково
### Крок 1: Знайти джерело
Використовуй `web_search` для пошуку актуальної інформації:
```python
from hermes_tools import web_search
# Приклад: знайти статтю про fine-tuning
result = web_search("LoRA fine-tuning LLM 2026 guide", limit=5)
```
### Крок 2: Витягти контент
Використовуй `web_extract` для перетворення URL у markdown:
```python
from hermes_tools import web_extract
# Витягнути повний текст
result = web_extract(urls=["https://blog.example.com/article"])
# result["results"][0]["content"] 

## Summary

— markdown текст
```
**Для arXiv паперів:** `web_extract` працює з PDF — просто передай URL.
### Крок 3: Зберегти у raw/
```python
from hermes_tools import write_file
import hashlib
from datetime import date
content = result["results"][0]["content"]
filename = "llm-fine-tuning-guide-2026.md"
# Обчислити sha256 тіла (після frontmatter)
sha256 = hashlib.sha256(content.encode()).hexdigest()
# Створити повний файл
full_content = f"""---
source_url: https://blog.example.com/article
ingested: {date.today().isoformat()}
sha256: {sha256}
---
{content}
"""
write_file(f"/workspace/llm-wiki/raw/articles/{filename}", full_content)
```
### Крок 4: Перевірити
```bash
# Переконатися що файл існує
ls -la /workspace/llm-wiki/raw/articles/filename.md
# Перевірити що frontmatter правильний
head -10 /workspace/llm-wiki/raw/articles/filename.md
```
---
## 🎯 Які джерела шукати
### Пріоритет 1 — Офіційні джерела
| Джерело | Що шукати | URL |
|---|---|---|
| **OpenAI Blog** | GPT-4, GPT-5, o-series, research | `blog.openai.com` |
| **Anthropic Blog** | Claude, AI safety, RLHF | `www.anthropic.com/research` |
| **Google DeepMind Blog** | Gemini, AlphaFold, research | `deepmind.google/research` |
| **Meta AI Blog** | Llama, open-weight моделі | `ai.meta.com/blog` |
| **Mistral Blog** | Mistral моделі, open-weight | `mistral.ai/news` |
| **Qwen Blog** | Qwen моделі, open-weight | `qwenlm.github.io` |
| **arXiv** | Наукові папери | `arxiv.org` |
### Пріоритет 2 — Інструменти та фреймворки
| Джерело | Що шукати | URL |
|---|---|---|
| **LangChain Blog** | RAG, agents, LCEL | `blog.langchain.dev` |
| **LlamaIndex Blog** | RAG, data connectors | `blog.llamaindex.ai` |
| **Hugging Face Blog** | Transformers, datasets, spaces | `huggingface.co/blog` |
| **vLLM Blog** | Serving, optimization | `docs.vllm.ai` |
| **Ollama Blog** | Local deployment | `ollama.com/blog` |
| **CrewAI Blog** | Multi-agent systems | `docs.crewai.com/blog` |
### Пріоритет 3 — Аналітика та огляди
| Джерело | Що шукати | URL |
|---|---|---|
| **The Batch (DeepLearning.AI)** | AI новини, огляди | `www.deeplearning.ai/the-batch` |
| **Simon Willison Blog** | LLM інструменти, API | `simonwillison.net` |
| **Jay Alammar Blog** | Візуальні пояснення, архітектури | `jalammar.github.io` |
| **Sebastian Raschka Blog** | ML, LLM training | `rasbt.github.io` |
| **Chip Huyen Blog** | ML production, MLOps | `chiphuyen.com` |
### Пріоритет 4 — Документація
| Джерело | Що шукати | URL |
|---|---|---|
| **PyTorch Docs** | Training, optimization | `pytorch.org/docs` |
| **TensorFlow Docs** | Model serving, TPU | `tensorflow.org/docs` |
| **CUDA Docs** | GPU optimization | `docs.nvidia.com/cuda` |
| **NVIDIA AI Docs** | TensorRT-LLM, Triton | `docs.nvidia.com/deeplearning` |
---
## 📊 Скільки збирати
**Рекомендація:** 3-5 якісних джерел за сесію.
Якісні критерії:
- ✅ Текст повний (не обрізаний, не truncated)
- ✅ Є чіткий заголовок і структура
- ✅ Є дата публікації
- ✅ URL живий і доступний
- ❌ Не копірайт-статті без тексту

## Related Articles

- [[release-notes-hugging-face-transformers-vv5130]]
- [[local-llm-wiki-повна-архітектурна-документація]]
- [[release-v005]]
- [[llm-wiki-index]]
- [[local-llm-wiki-agent-contract]]
