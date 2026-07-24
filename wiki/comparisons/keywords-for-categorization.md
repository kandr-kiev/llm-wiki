---
title: "── Keywords for categorization ────────────────────────────────────────────"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - alignment
  - api
  - audio-generation
  - awq
  - benchmark
  - claude
  - computer-vision
  - cost
  - cuda
  - deep-learning
  - dpo
  - embedding
  - fine-tuning
  - foundation-model
  - framework
  - gemini
  - gguf
  - gpt
  - gptq
  - gpu
  - image-generation
  - llama
  - llm
  - lora
  - mistral
  - multi-agent
  - multimodal
  - news
  - nlp
  - open-source
  - optimization
  - policy
  - prompt-engineering
  - prompt-tuning
  - qlora
  - quantization
  - rag
  - real-time
  - regulation
  - research
  - retrieval
  - review
  - rlhf
  - security
  - sft
  - software
  - speech-to-text
  - supervised
  - synthesis
  - tool
  - training
  - transformers
  - vector-database
  - video-generation
---

# ── Keywords for categorization ────────────────────────────────────────────

> **Source:** local-weather-space-lunar-digestsrcservicesnewspy-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/weather-space-lunar-digest/src/services/news.py ingested: 2026-07-20 sha256: 1d4b4a2cf057b5914c2e7a054593370ab730997543f880c514ed9fb2920d6e1c blog_source: lo...
> **Sources:**
>   - local-weather-space-lunar-digestsrcservicesnewspy-2026-07-20.md
> **Links:**
- [[news.py]]
- [[kimi-k3]]
- [[v0.23.0]]
- [[qwen-alibaba]]
- [[llm-landscape-multi-source-synthesis]]

## Key Findings

---
source_url: file:///workspace/Projects/weather-space-lunar-digest/src/services/news.py
ingested: 2026-07-20
sha256: 1d4b4a2cf057b5914c2e7a054593370ab730997543f880c514ed9fb2920d6e1c
blog_source: local:unknown
---
"""News service — fetches and categorizes news from RSS feeds."""
import urllib.request
import xml.etree.ElementTree as ET
import datetime
import re
import sys
import html as html_module
from zoneinfo import ZoneInfo
# ── Keywords for categorization ────────────────────────────────────────────
# Scoring-based: each keyword match adds points. Highest score wins.
WAR_KEYWORDS = [
("фронт", 3), ("атак", 3), ("оборон", 2), ("зСУ", 3), ("російськ", 3),
("росіяни", 3), ("бойов", 3), ("окуп", 3), ("удар", 2), ("дрон", 2),
("ракета", 3), ("ГУР", 2), ("збройн", 2), ("танк", 2), ("артилер", 2),
("піхот", 2), ("контратак", 2), ("позиц", 2), ("лінія", 1), ("деокуп", 2),
("флот", 1), ("авіац", 2), ("бомбард", 2), ("терорист", 2), ("спецопер", 2),
("прикордонн", 2), ("постражд", 2), ("вдарили", 2), ("обстріл", 3),
("ukrainian forces", 3), ("russian forces", 3), ("ukrainian army", 3),
("missile", 3), ("offensive", 2), ("counteroffensive", 3),
("invasion", 3), ("occupation forces", 3), ("kharkiv", 2),
("donetsk", 2), ("zaporizh", 2), ("kherson", 2), ("mykolaiv", 2),
("avdiivka", 2), ("belgorod", 1),
]
GEOPOL_KEYWORDS = [
("переговор", 3), ("санкц", 3), ("посол", 2), ("посольств", 2),
("дипломат", 2), ("МЗС", 2), ("міністерств", 2), ("закордон", 2),
("Брюссел", 2), ("Вашингтон", 2), ("Пекін", 2), ("Нато", 2),
("ЄС", 2), ("Європейськ", 2), ("ООН", 2), ("рада безп", 2),
("саміт", 2), ("угод", 2), ("поставк", 2), ("президент", 1),
("канцлер", 1), ("прем'єр", 1), ("депутат", 1), ("парламент", 1),
("рішенн", 1), ("блок", 1), ("підтримк", 1), ("визнан", 2),
("sanction", 3), ("sanctions", 3), ("embassy", 2), ("ambassador", 2),
("diplomac", 2), ("ministry", 1), ("brussels", 2), ("washington", 2),
("beijing", 2), ("nato", 2), ("eu", 2), ("european", 2),
("united nations", 2), ("security council", 2), ("summit", 2),
("agreement", 1), ("aid", 1), ("support", 1), ("recognition", 2),
("parliament", 1), ("deputy", 1), ("mp", 1), ("government", 1),
("policy", 1), ("trump", 1), ("putin", 1), ("zelenskyy", 1),
("stoltenberg", 1), ("von der leyen", 1), ("biden", 1), ("macron", 1),
("scholz", 1), ("merkel", 1), ("keir", 1), ("starmer", 1),
("ukraine aid", 2), ("peace plan", 2), ("peace summit", 2),
("membership", 2), ("candidate", 1), ("accession", 1),
("visa", 1), ("free visa", 2),
]
ECONO_KEYWORDS = [
("ціна", 3), ("тариф", 3), ("валютн", 3), ("курс", 3), ("гривн", 2),
("банк", 2), ("кредит", 2), ("грош", 2), ("криза", 2), ("ринк", 2),
("торгівл", 2), ("імпорт", 2), ("експорт", 2), ("палив", 2),
("енергетик", 2), ("газов", 2), ("нафтов", 2), ("електроенерг", 2),
("інфляц", 2), ("дефіцит", 2), ("профіцит", 1), ("бюджет", 2),
("субсид", 2), ("пособ", 1), ("пенс", 1), ("заробітн", 1),
("підприємств", 1), ("виробництв", 1), ("грант", 2), ("інвест", 2),
("фонд", 1), ("лікв

## Summary

ідн", 1), ("ставка", 1), ("обліков", 2),
("безгот", 1), ("комун", 1), ("опален", 2), ("ліценз", 1),
("монопол", 1),
]
TECH_KEYWORDS = [
("технолог", 2), ("IT", 3), ("software", 2), ("app", 2), ("AI", 3),
("штучний", 3), ("стартап", 2), ("цифра", 1), ("кібер", 2),
("диджитал", 1), ("програмн", 1), ("сервер", 1), ("дата", 1),
("open sourc", 2), ("блокчейн", 2), ("додаток", 1), ("розробк", 1),
("код", 1), ("інновац", 1), ("онлайн", 1), ("веб", 1), ("мобільн", 1),
("API", 2), ("хмар", 1), ("автоматиз", 1), ("машинн", 2),
("нейрон", 2), ("алгоритм", 1), ("платформ", 1), ("сервіс", 1),
("технопол", 1), ("ШІ", 3), ("агент", 1), ("LLM", 3), ("GPT", 3),
("Claude", 3), ("Gemini", 2), ("Copilot", 2), ("GenAI", 2),
("генератив", 3), ("чат-бот", 2), ("prompt", 2), ("інференс", 2),
("multimodal", 2), (" RLHF", 2), ("open weights", 2),
("open-source model", 2), ("нейромереж", 2), ("transformer", 2),
(" embeddings", 2),
]
LLM_KEYWORDS = [
# ── Model names (all families) ──────────────────────────────────────
("GPT", 3), ("GPT-4", 3), ("GPT-4o", 3), ("GPT-4o mini", 3), ("GPT-5", 3),
("Claude", 3), ("Claude 3", 3), ("Claude 3.5", 3), ("Claude 4", 3),
("Gemini", 3), ("Gemini 2", 3), ("Gemini 2.0", 3),
("Llama", 3), ("Llama 3", 3), ("Llama 3.1", 3), ("Llama 3.2", 3), ("Llama 4", 3),
("Mistral", 3), ("Mistral 7B", 3), ("Mistral Large", 3), ("Mixtral", 3),
("Qwen", 3), ("Qwen2", 3), ("Qwen2.5", 3), ("Qwen3", 3),
("DeepSeek", 3), ("DeepSeek R1", 3), ("DeepSeek V3", 3),
("ChatGLM", 3), ("GLM-4", 3), ("GLM-5", 3),
("Ernie", 3), ("文心一言", 3), ("Tongyi", 3), ("通义千问", 3),
("Yi", 3), ("Yi-34B", 3), ("Yi-Lightning", 3),
("Baichuan", 3), ("Baichuan2", 3),
("Step", 3), ("Step-1", 3), ("StepCoder", 3),
("Hunyuan", 3), ("混元", 3),
("MiniMax", 3), ("abab", 3),
("XVERSE", 3), ("XVERSE-13B", 3),
("Kimi", 3), ("Moonshot", 3),
("01.AI", 3), ("Yuan", 3), ("Yuan2", 3),
("internLM", 3), ("internLM2", 3), ("internLM3", 3),
("Perplexity", 3),
# ── AI Agent frameworks & tools ─────────────────────────────────────
("OpenCode", 3), ("Claude Code", 3), ("Codex CLI", 3), ("Cursor", 3),
("Continue", 3), ("Aider", 3), ("Windsurf", 3), ("Replit Agent", 3),
("Devin", 3), ("SWE-agent", 3), ("OpenDevin", 3),
("CrewAI", 3), ("LangChain", 3), ("LangGraph", 3), ("LlamaIndex", 3),
("AutoGen", 3), ("AutoGPT", 3), ("BabyAGI", 3), ("ChatDev", 3),
("MetaGPT", 3), ("Superagent", 3), ("SmolAgent", 3),
("DSPy", 3), ("Haystack", 3), ("Semantic Kernel", 3),
("Langflow", 3), ("FlowiseAI", 3), ("Dify", 3), ("Flowith", 3),
("n8n", 2), ("Make", 2), ("Zapier", 2), ("Rivet", 2), ("DAGWorks", 2),
("Voyage AI", 3), ("Cohere", 3), ("Together AI", 3), ("Replicate", 3),
("Hugging Face", 3), ("HuggingChat", 3), ("HF Spaces", 2),
# ── Companies & labs ────────────────────────────────────────────────
("OpenAI", 3), ("Anthropic", 3), ("Google DeepMind", 3), ("Meta AI", 3),
("xAI", 3), ("01.AI", 3), ("Moonshot AI", 3), ("Zhipu", 3), ("智谱", 3),
("ByteDance", 3), ("Baidu", 3), ("Alibaba", 3), ("Tencent", 3),
("Perplexity", 3), ("Cha

## Related Articles

- [[news.py]]
- [[kimi-k3]]
- [[v0.23.0]]
- [[qwen-alibaba]]
- [[llm-landscape-multi-source-synthesis]]
