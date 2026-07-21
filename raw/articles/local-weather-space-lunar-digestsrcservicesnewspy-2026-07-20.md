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
    ("фонд", 1), ("ліквідн", 1), ("ставка", 1), ("обліков", 2),
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
    ("Perplexity", 3), ("Character.AI", 3), ("Inflection", 3), ("Inflection Pi", 3),
    ("Pi AI", 3), ("Pi-3", 3), ("Pi-3 mini", 3),
    ("Suno", 3), ("Udio", 3), ("ElevenLabs", 3), ("Midjourney", 3),
    ("Stability AI", 3), ("Runway", 3), ("Pika", 3), ("Kling", 3),
    ("Sora", 3), ("Vidu", 3),
    # ── AI Concepts & Terminology ───────────────────────────────────────
    ("LLM", 3), ("large language model", 3), ("language model", 2),
    ("AI agent", 3), ("autonomous agent", 3), ("multi-agent", 3),
    ("agent framework", 3), ("agent platform", 3), ("AI agent", 3),
    ("reasoning model", 3), ("chain of thought", 3), ("CoT", 2),
    ("RLHF", 3), ("RLAIF", 3), ("RLVR", 3), ("PPO", 2),
    ("DPO", 3), ("Direct Preference Optimization", 3),
    ("SFT", 3), ("Supervised Fine-Tuning", 3),
    ("alignment", 2), ("AI alignment", 3), ("alignment tax", 3),
    ("inference", 2), ("inference time", 2), ("inference cost", 2),
    ("context window", 2), ("long context", 2), ("128K", 2),
    ("RAG", 3), ("Retrieval Augmented Generation", 3),
    ("vector database", 2), ("embedding", 2), ("embeddings", 2),
    ("fine-tune", 2), ("fine-tuning", 2), ("LoRA", 3), ("QLoRA", 3),
    ("quantization", 2), ("GGUF", 3), ("GPTQ", 3), ("AWQ", 3),
    ("speculative decoding", 3), ("Mixture of Experts", 3), ("MoE", 3),
    ("dense model", 2), ("parameter count", 2),
    ("billion parameters", 2), ("7B", 2), ("13B", 2), ("34B", 2), ("70B", 2), ("405B", 2),
    ("open weights", 2), ("open-source model", 2), ("open-source LLM", 3),
    ("AI chatbot", 2), ("chatbot", 1),
    ("AI coding", 2), ("code generation", 2), ("code completion", 2),
    ("text-to-image", 2), ("text-to-video", 2), ("image generation", 2),
    ("speech-to-text", 2), ("text-to-speech", 2), ("voice cloning", 2),
    ("prompt engineering", 2), ("prompt injection", 2), ("prompt hacking", 2),
    ("hallucination", 2), ("hallucinate", 2), ("model collapse", 2),
    ("benchmark", 2), ("MMLU", 2), ("HELM", 2), ("ARC", 2), ("GPQA", 2),
    ("AI safety", 2), ("AI risk", 2), ("AI regulation", 2), ("AI policy", 2),
    ("compute", 2), ("GPU", 2), ("TPU", 2), ("H100", 3), ("H200", 3),
    ("NVIDIA", 2), ("CUDA", 2), ("training", 2), ("pre-training", 2),
    ("AI startup", 2), ("AI funding", 2), ("AI investment", 2), ("AI venture", 2),
    ("AI lab", 2), ("AI research", 2), ("AI paper", 2), ("arxiv", 2),
    # ── AI Perception & Multimodal ──────────────────────────────────────
    ("computer vision", 2), ("image recognition", 2), ("object detection", 2),
    ("image generation", 2), ("image editing", 2), ("image-to-text", 2),
    ("video generation", 2), ("video understanding", 2),
    ("speech recognition", 2), ("speech synthesis", 2), ("voice cloning", 2),
    ("audio generation", 2), ("music generation", 2), ("music AI", 2),
    ("multimodal", 2), ("vision-language", 2), ("vision model", 2),
    ("visual reasoning", 2), ("OCR", 2), ("document AI", 2),
    ("image-to-video", 2), ("video-to-video", 2), ("image-to-image", 2),
    ("text-to-3D", 2), ("3D generation", 2), ("neural radiance", 2), ("NeRF", 2),
    # ── AI in Software Development ──────────────────────────────────────
    ("AI coding assistant", 2), ("AI pair programmer", 2),
    ("code review AI", 2), ("code generation", 2), ("code completion", 2),
    ("AI developer tool", 2), ("AI dev tool", 2),
    ("AI for developers", 2), ("developer AI", 2),
    ("AI code review", 2), ("AI code generation", 2),
    ("AI debugger", 2), ("AI refactoring", 2),
    ("AI testing", 2), ("AI test generation", 2),
    ("AI documentation", 2), ("AI doc generator", 2),
    ("AI commit message", 2), ("AI changelog", 2),
    ("AI PR description", 2), ("AI pull request", 2),
    ("AI git", 2), ("AI version control", 2),
    ("AI IDE", 2), ("AI editor", 2),
    ("AI terminal", 2), ("AI CLI", 2),
    ("AI shell", 2), ("AI command", 2),
    ("AI workflow", 2), ("AI automation", 2),
    ("AI pipeline", 2), ("AI orchestration", 2),
    ("AI deployment", 2), ("AI model serving", 2),
    ("AI API", 2), ("AI endpoint", 2),
    ("AI SDK", 2), ("AI library", 2), ("AI toolkit", 2),
    ("AI framework", 2), ("AI platform", 2),
    # ── AI in Healthcare, Science, Education ────────────────────────────
    ("AI healthcare", 2), ("AI medicine", 2), ("AI diagnosis", 2),
    ("AI drug discovery", 2), ("AI biology", 2), ("AI protein", 2),
    ("AI science", 2), ("AI research", 2), ("AI academic", 2),
    ("AI education", 2), ("AI tutoring", 2), ("AI learning", 2),
    ("AI math", 2), ("AI physics", 2), ("AI chemistry", 2),
    # ── AI Security & Ethics ────────────────────────────────────────────
    ("AI security", 2), ("AI safety", 2), ("AI alignment", 2),
    ("AI red team", 2), ("AI jailbreak", 2), ("AI prompt injection", 2),
    ("AI bias", 2), ("AI fairness", 2), ("AI transparency", 2),
    ("AI explainability", 2), ("AI interpretability", 2),
    ("AI copyright", 2), ("AI training data", 2), ("AI data scraping", 2),
    ("AI content policy", 2), ("AI content filter", 2),
    ("AI watermark", 2), ("AI content detection", 2),
    ("AI deepfake", 2), ("AI fake", 2), ("AI synthetic media", 2),
    # ── AI Business & Industry ──────────────────────────────────────────
    ("AI startup", 2), ("AI funding", 2), ("AI investment", 2),
    ("AI venture", 2), ("AI lab", 2), ("AI research", 2),
    ("AI company", 2), ("AI corporation", 2),
    ("AI industry", 2), ("AI market", 2), ("AI sector", 2),
    ("AI revenue", 2), ("AI IPO", 2), ("AI valuation", 2),
    ("AI partnership", 2), ("AI collaboration", 2),
    ("AI acquisition", 2), ("AI merger", 2),
    ("AI job", 2), ("AI employment", 2), ("AI workforce", 2),
    ("AI job loss", 2), ("AI displacement", 2),
    ("AI productivity", 2), ("AI efficiency", 2),
    ("AI cost reduction", 2), ("AI automation", 2),
    ("AI digital transformation", 2), ("AI enterprise", 2),
    ("AI SaaS", 2), ("AI PaaS", 2), ("AI platform", 2),
    ("AI API", 2), ("AI model API", 2),
    ("AI subscription", 2), ("AI pricing", 2),
    ("AI chat", 2), ("AI conversation", 2),
    ("AI assistant", 2), ("AI personal assistant", 2),
    ("AI customer service", 2), ("AI support", 2),
    ("AI search", 2), ("AI search engine", 2),
    ("AI recommendation", 2), ("AI personalization", 2),
    ("AI analytics", 2), ("AI insights", 2),
]

CRIME_KEYWORDS = [
    ("кримінал", 3), ("злочин", 3), ("арешт", 3), ("затриман", 3),
    ("розслідуван", 3), ("слідств", 3), ("суд", 2), ("в'язниц", 3),
    ("в'язн", 2), ("крадіж", 3), ("грабіж", 3), ("вбивств", 3),
    ("замах", 2), ("корупц", 3), ("хабар", 3), ("мафія", 2),
    ("наркотик", 3), ("злочинн", 2), ("розшук", 2), ("підпал", 2),
    ("шпигун", 3), ("smuggling", 3), ("trafficking", 3), ("murder", 3),
    ("robbery", 3), ("theft", 3), ("burglary", 3), ("arson", 2),
    ("kidnapping", 3), ("gang", 2), ("cartel", 2), ("organized crime", 3),
    ("prison", 2), ("court", 1), ("trial", 1),
]

# Negative keywords — strong exclusions per category
WAR_NEGATIVE = [
    "тариф", "світло", "відключенн", "палив", "газ", "гривн",
    "інфляц", "ринк", "IPO", "spacex", "теніс", "овоч", "дитина",
    "сект", "гуру", "зірк", "нью-йорк", "модель", "прибулець",
    "здоров'я", "лікування", "дитин", "їжа", "рецепт", "вагітн",
    "порад", "як вибрати", "5 способів", "7 способів", "як привчити",
    "одяг", "спеку", "хот-дог", "пив", "історії",
]

GEOPOL_NEGATIVE = [
    "фронт", "атак", "оборон", "зСУ", "окуп", "ракета",
    "дрон", "танк", "артилер", "піхот", "ГУР",
    "тариф", "світло", "відключенн", "палив", "газ",
    "кримінал", "злочин", "арешт", "вбивств", "корупц",
    "сект", "гуру", "зірк", "нью-йорк", "модель",
]

ECONO_NEGATIVE = [
    "фронт", "атак", "оборон", "зсу", "окуп", "ракета",
    "ГУР", "дрон", "танк", "артилер", "піхот",
    "дитина", "овоч", "їжа", "рецепт", "лікування", "вагітн",
    "порад", "як вибрати", "5 способів", "7 способів", "як привчити",
    "кримінал", "злочин", "арешт", "вбивств", "корупц",
    "сект", "гуру", "зірк", "нью-йорк", "модель",
    "технолог", "IT", "AI", "штучний", "стартап", "цифра",
]

TECH_NEGATIVE = [
    "фронт", "атак", "оборон", "зСУ", "окуп", "ракета",
    "ГУР", "дрон", "танк", "артилер", "піхот",
    "тариф", "світло", "відключенн", "палив", "газ",
    "кримінал", "злочин", "арешт", "вбивств", "корупц",
    "сект", "гуру", "зірк", "нью-йорк", "модель",
    "здоров'я", "лікування", "дитин", "їжа", "рецепт",
    "одяг", "спеку", "хот-дог", "пив", "історії",
]

CRIME_NEGATIVE = [
    "фронт", "атак", "оборон", "зСУ", "окуп", "ракета",
    "дрон", "танк", "артилер", "піхот", "ГУР",
    "тариф", "світло", "відключенн", "палив", "газ",
    "сект", "гуру", "зірк", "нью-йорк", "модель",
    "здоров'я", "лікування", "дитин", "їжа", "рецепт",
    "одяг", "спеку", "хот-дог", "пив", "історії",
    "майна", "Vyriy", "індустр",
    "Громадське", "радіо долучає", "розслідуван", "Ініціатив",
]

LLM_NEGATIVE = [
    "фронт", "атак", "оборон", "зСУ", "окуп", "ракета",
    "ГУР", "дрон", "танк", "артилер", "піхот",
    "тариф", "світло", "відключенн", "палив", "газ",
    "кримінал", "злочин", "арешт", "вбивств", "корупц",
    "сект", "гуру", "зірк", "нью-йорк", "модель",
    "здоров'я", "лікування", "дитин", "їжа", "рецепт",
    "одяг", "спеку", "хот-дог", "пив", "історії",
    "прибуток", "збиток", "продаж", "акції", "бірж",
    "злитт", "поглинанн", "merger", "acquisition",
    "diCaprio", "Leonardo", "Leo",
    "Ryanair", "авіапаливо", "авіація", "рейс", "літак",
    "брати", "брат у ДБР",
]

NEGATIVE_MAP = {
    "war": WAR_NEGATIVE,
    "geopol": GEOPOL_NEGATIVE,
    "economy": ECONO_NEGATIVE,
    "tech": TECH_NEGATIVE,
    "crime": CRIME_NEGATIVE,
    "llm": LLM_NEGATIVE,
}

# ── RSS Feed sources ───────────────────────────────────────────────────────
FEEDS_LOCAL = [
    ("https://feeds.bbci.co.uk/ukrainian/rss.xml", "BBC"),
    ("https://hromadske.radio/feed/rss", "Громадське"),
    ("https://dou.ua/feed/", "DOU"),
    ("https://www.epravda.com.ua/rss/", "Економічна правда"),
    ("https://ain.ua/feed/", "AIN"),
]

FEEDS_INTERNATIONAL = [
    ("https://feeds.bbci.co.uk/news/rss.xml", "BBC World"),
]

from src.adapters.wiki import fetch_wiki_news, fetch_wiki_concepts, fetch_wiki_entities


def _clean_html(text):
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html_module.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def _parse_feed(url):
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "application/xml, text/xml, */*",
            },
            method="GET"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            root = ET.fromstring(resp.read())
            items = []
            feed_items = list(root.iter("item"))
            if not feed_items:
                feed_items = list(root.iter("entry"))
            for item in feed_items:
                title_elem = item.find("title")
                desc_elem = item.find("description") or item.find("summary") or item.find("{http://purl.org/rss/1.0/modules/content/}encoded")
                date_elem = item.find("pubDate") or item.find("published") or item.find("updated")
                title_text = title_elem.text.strip() if title_elem is not None and title_elem.text else ""
                desc_text = desc_elem.text.strip() if desc_elem is not None and desc_elem.text else ""
                desc_text = _clean_html(desc_text)
                if not desc_text:
                    desc_text = title_text
                if title_text:
                    title = title_text[:140]
                    description = desc_text[:500]
                    pub_dt = None
                    if date_elem is not None and date_elem.text:
                        raw = date_elem.text.strip()
                        for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%dT%H:%M:%S%z",
                                     "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d %H:%M:%S",
                                     "%a, %d %b %Y %H:%M:%S"):
                            try:
                                pub_dt = datetime.datetime.strptime(raw, fmt)
                                break
                            except ValueError:
                                pass
                    items.append((title, description, pub_dt))
                    if len(items) >= 12:
                        break
            return items
    except Exception as e:
        print(f"[WARN] Feed {url} failed: {e}", file=sys.stderr)
        return []


def _deduplicate_headlines(items, dedup_set):
    result = []
    for title, desc in items:
        title_lower = title.lower()
        is_dup = False
        for seen in dedup_set:
            seen_lower = seen.lower()
            title_words = set(title_lower.split())
            seen_words = set(seen_lower.split())
            if title_words and seen_words:
                intersection = len(title_words & seen_words)
                union = len(title_words | seen_words)
                jaccard = intersection / union
                is_substring = (title_lower in seen_lower) or (seen_lower in title_lower)
                shared_phrases = 0
                t_words_list = title_lower.split()
                s_words_list = seen_lower.split()
                for i in range(len(t_words_list) - 1):
                    phrase = ' '.join(t_words_list[i:i+2])
                    if phrase in seen_lower:
                        shared_phrases += 1
                if jaccard > 0.7 or is_substring or shared_phrases >= 2:
                    is_dup = True
                    break
        if not is_dup:
            result.append((title, desc))
            dedup_set.add(title)
    return result


def _score_item(keywords, title, desc):
    text = (title + " " + desc).lower()
    score = 0
    matched = 0
    for kw, weight in keywords:
        if kw.lower() in text:
            score += weight
            matched += 1
    return score, matched


def _assign_categories(all_items):
    categories = {
        "war": WAR_KEYWORDS,
        "geopol": GEOPOL_KEYWORDS,
        "economy": ECONO_KEYWORDS,
        "tech": TECH_KEYWORDS,
        "crime": CRIME_KEYWORDS,
        "llm": LLM_KEYWORDS,
    }
    scored_items = []
    for title, desc in all_items:
        scores = {}
        for cat_key, keywords in categories.items():
            score, matched = _score_item(keywords, title, desc)
            neg_keywords = NEGATIVE_MAP.get(cat_key, [])
            neg_penalty = 0
            for neg in neg_keywords:
                if neg.lower() in title.lower():
                    neg_penalty += 5
            scores[cat_key] = max(0, score - neg_penalty)
        best_cat = max(scores, key=scores.get)
        best_score = scores[best_cat]
        if best_score >= 3:
            scored_items.append({
                "title": title,
                "desc": desc,
                "category": best_cat,
                "score": best_score,
                "scores": scores,
            })
    result = {cat: [] for cat in categories}
    for item in scored_items:
        cat = item["category"]
        if len(result[cat]) < 3:
            result[cat].append(item)
    formatted = {}
    for cat_key, items in result.items():
        formatted[cat_key] = _format_items(items)
    return formatted


def _format_items(items):
    result = []
    for item in items:
        title = item["title"]
        desc = item["desc"]
        summary = _generate_summary(title, desc)
        if summary:
            result.append(f"🔹 {title} — 📝 {summary}")
        else:
            result.append(f"🔹 {title}")
    return result


def _generate_summary(title, desc):
    if not desc or desc == title:
        return None
    clean_desc = _clean_html(desc)
    if not clean_desc:
        return None
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', clean_desc) if len(s.strip()) > 15]
    if not sentences:
        return None
    title_words = set(w.lower() for w in title.lower().split())
    summary = None
    for sentence in sentences:
        sent_words = set(w.lower() for w in sentence.split()[:15])
        overlap = len(sent_words & title_words) / max(len(sent_words), 1)
        if overlap < 0.4:
            summary = sentence
            break
    if summary is None:
        summary = sentences[0]
    if len(summary) < 80 and len(sentences) > 1:
        idx = sentences.index(summary) if summary in sentences else 0
        for next_sent in sentences[idx+1:]:
            candidate = summary + ' ' + next_sent
            if len(candidate) <= 250:
                summary = candidate
            else:
                break
    if len(summary) > 250:
        cut_pos = summary.rfind(' ', 0, 250)
        if cut_pos > 50:
            summary = summary[:cut_pos] + '...'
        else:
            summary = summary[:247] + '...'
    summary = summary.replace('\n', ' ').replace('\r', ' ').strip()
    if summary and not summary[-1] in '.!?':
        summary += '.'
    return summary


def fetch_news() -> dict:
    result = {"war": [], "geopol": [], "economy": [], "tech": [], "crime": [], "llm": []}
    all_items = []
    seen_titles = set()
    tz_name = "Europe/Kiev"
    try:
        tz = ZoneInfo(tz_name)
    except Exception:
        tz = datetime.timezone(datetime.timedelta(hours=3))
    now_local = datetime.datetime.now(tz)
    prev_cutoff = (now_local - datetime.timedelta(days=1)).replace(hour=8, minute=0, second=0, microsecond=0)
    for feed_url, source_name in FEEDS_LOCAL + FEEDS_INTERNATIONAL:
        items = _parse_feed(feed_url)
        for rec in items:
            if len(rec) == 3:
                title, desc, pub_dt = rec
            else:
                title, desc = rec
                pub_dt = None
            if title in seen_titles:
                continue
            keep = True
            if isinstance(pub_dt, datetime.datetime):
                if pub_dt.tzinfo is None:
                    pub_dt = pub_dt.replace(tzinfo=tz)
                if pub_dt < prev_cutoff:
                    keep = False
            if keep:
                all_items.append((title, desc))
                seen_titles.add(title)
    wiki_news = fetch_wiki_news()
    wiki_concepts = fetch_wiki_concepts()
    wiki_entities = fetch_wiki_entities()
    for title, desc, pub_dt in wiki_news + wiki_concepts + wiki_entities:
        if title not in seen_titles:
            all_items.append((title, desc))
            seen_titles.add(title)
    dedup_set = set()
    deduped_items = _deduplicate_headlines(all_items, dedup_set)
    categorized = _assign_categories(deduped_items)
    for cat_key in ["war", "geopol", "economy", "tech", "crime", "llm"]:
        result[cat_key] = categorized.get(cat_key, [])
    used = set(
        item.replace("🔹 ", "").strip()
        for item in result.get("war", []) + result.get("geopol", []) +
        result.get("economy", []) + result.get("tech", []) + result.get("crime", []) + result.get("llm", [])
    )
    general = []
    for t, d in all_items:
        clean = t.replace("🔹 ", "").strip()
        if clean not in used:
            general.append(f"🔹 {clean}")
            used.add(clean)
    result["general"] = general[:3]
    return result


NEWS_SECTIONS_CONFIG = [
    ("war", "⚔️ ВІЙНА", 3),
    ("geopol", "🌍 ПОЛІТИКА", 3),
    ("economy", "💼 ЕКОНОМІКА", 3),
    ("tech", "💾 ТЕХНОЛОГІЇ", 3),
    ("crime", "🚔 КРИМІНАЛ", 3),
    ("llm", "🤖 LLM/AGENTS", 3),
    ("general", "📰 ЗАГАЛЬНІ НОВИНИ", 3),
]


def _format_news_item(text: str) -> str:
    text = text.strip()
    if not text.startswith("🔹"):
        return f"🔹 {text}"
    return text


def format_news_sections(news: dict) -> str:
    sections = ""
    for cat_key, header, limit in NEWS_SECTIONS_CONFIG:
        items = news.get(cat_key, [])
        if items:
            sections += f"{header}\n"
            for item in items[:limit]:
                sections += f"{_format_news_item(item)}\n"
            sections += "\n"
    if not sections:
        sections = "📰 Новин сьогодні немає. Працюємо спокійно."
    return sections
