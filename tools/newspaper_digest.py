#!/usr/bin/env python3
"""Newspaper Digest — щоденна електронна газета з новинами LLM-Wiki.

Парсить raw-файли за останні 24 години, витягує заголовки, завантажує повний текст,
генерає стислий переказ українською (макс 5 речень), формує компактний дайджест.

Використання:
    python3 tools/newspaper_digest.py [--dry-run]
    
Вивід:
    - stdout: готовий Markdown для Telegram
    - --dry-run: лише вивід без збереження
"""
import os
import re
import sys
import subprocess
import urllib.parse
import json
import math
from pathlib import Path
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field
from typing import Optional, List
from collections import Counter
import trafilatura

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw" / "articles"


# ---------------------------------------------------------------------------
# Категорії та іконки
# ---------------------------------------------------------------------------
CATEGORY_ICONS = {
    "🤖 AI / ML": "🧠",
    "💻 Programming": "⌨️",
    "🗄️ Databases": "🗃️",
    "🧮 Algorithms": "📐",
    "🛠️ IDE / Tools": "🔧",
    "📰 General": "📢",
    "🚀 GitHub Releases": "📦",
    "🤖 AI Agents": "🤖",
    "🚀 AI Startups": "🚀",
    "🤗 HuggingFace": "🤗",
    "🐙 GitHub Issues": "🐛",
    "📁 Local": "📂",
}

CATEGORY_MAP = {
    # AI / ML
    "Andrej Karpathy": "🤖 AI / ML",
    "Chip Huyen": "🤖 AI / ML",
    "Lilian Weng": "🤖 AI / ML",
    "Jay Alammar": "🤖 AI / ML",
    "Hacker News AI": "🤖 AI / ML",
    "ArXiv AI": "🤖 AI / ML",
    "Cloudflare Blog": "🤖 AI / ML",
    "OpenAI Blog": "🤖 AI / ML",
    "Google DeepMind": "🤖 AI / ML",
    "Distill AI": "🤖 AI / ML",
    "Papers With Code": "🤖 AI / ML",
    "Hugging Face Blog": "🤖 AI / ML",
    "The Gradient": "🤖 AI / ML",
    "r/MachineLearning": "🤖 AI / ML",
    "MarkTechPost": "🤖 AI / ML",
    "MIT Tech Review AI": "🤖 AI / ML",
    "The Verge AI": "🤖 AI / ML",
    "OpenAI News": "🤖 AI / ML",
    "Meta AI Blog": "🤖 AI / ML",
    "Hacker News": "🤖 AI / ML",
    "TechCrunch AI": "🤖 AI / ML",
    "VentureBeat AI": "🤖 AI / ML",
    # AI Startups
    "TechCrunch Startups": "🚀 AI Startups",
    "TechCrunch Venture": "🚀 AI Startups",
    # Programming Languages
    "Python Insider": "💻 Programming",
    "Planet Python": "💻 Programming",
    "TypeScript Blog": "💻 Programming",
    "Rust Blog": "💻 Programming",
    "Laravel News": "💻 Programming",
    # Databases
    "Oracle DBA Soyma": "🗄️ Databases",
    # Algorithms / CS
    "Google Research Blog": "🧮 Algorithms",
    "Algorithm Design": "🧮 Algorithms",
    "CS Theory": "🧮 Algorithms",
    "Algorithm Corner": "🧮 Algorithms",
    # IDE / Dev Tools
    "JetBrains Blog": "🛠️ IDE / Tools",
    "PyCharm Blog": "🛠️ IDE / Tools",
    "VS Code Blog": "🛠️ IDE / Tools",
    "IntelliJ Blog": "🛠️ IDE / Tools",
    # General Programming
    "GitHub Blog": "📰 General",
    "Microsoft Dev Blog": "📰 General",
    "Dev Community": "📰 General",
    "FreeCodeCamp Blog": "📰 General",
    "Netflix Tech Blog": "📰 General",
    "Hanselminutes": "📰 General",
    "Smashing Magazine": "📰 General",
}


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------
@dataclass
class Article:
    filename: str
    title: str
    summary: str  # стислий опис з frontmatter
    source: str
    category: str
    url: str
    ingested: str
    is_top: bool = False
    # поле для згенерованого переказу
    summary_uk: str = ""


# ---------------------------------------------------------------------------
# Translation via Google Translate (deep-translator)
# ---------------------------------------------------------------------------
from deep_translator import GoogleTranslator

def translate_text(text: str, dest_lang: str = "uk") -> str:
    """Перекладає текст через Google Translate (en -> uk)."""
    if not text or len(text) < 3:
        return text
    
    try:
        translated = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        if translated and len(translated) > 5:
            return translated
    except Exception:
        pass
    
    return text


def clean_title_suffix(title: str) -> str:
    """Видаляє суфікс ' | SourceName' з заголовка."""
    if " | " in title:
        parts = title.rsplit(" | ", 1)
        source = parts[-1].strip()
        known_sources = [
            "TechCrunch", "MIT Technology Review", "The Verge", "JetBrains Blog",
            "The Gradient", "Hacker News", "MarkTechPost", "Laravel News",
            "Rust Blog", "Python Insider", "Microsoft Dev Blog",
            "DEV Community", "FreeCodeCamp", "GitHub Blog",
            "Smashing Magazine", "VentureBeat AI", "OpenAI News",
            "Google DeepMind", "Distill AI", "Papers With Code",
            "Hugging Face Blog", "r/MachineLearning", "Cloudflare Blog",
            "Andrej Karpathy", "Chip Huyen", "Lilian Weng", "Jay Alammar",
            "Hacker News AI", "OpenAI Blog", "Meta AI Blog",
            "The Verge AI", "TechCrunch AI", "MIT Tech Review AI",
        ]
        if source in known_sources:
            return parts[0].strip()
    return title


# ---------------------------------------------------------------------------
# Content extraction
# ---------------------------------------------------------------------------
def parse_frontmatter(content: str) -> dict:
    """Витягує frontmatter з raw-файлу."""
    fm = {}
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    fm[key.strip()] = val.strip()
    return fm


def extract_repo_name_from_url(url: str) -> str:
    """Витягує назву репо з URL GitHub releases."""
    if "/releases/tag/" in url:
        parts = url.split("/releases/tag/")[0].split("/")
        if len(parts) >= 2:
            return parts[-1]
    return ""


def extract_description_from_html(content: str) -> str:
    """Витягує опис з HTML (og:description або meta description)."""
    og_match = re.search(r'property="og:description"\s+content="(.*?)"', content)
    if og_match:
        desc = og_match.group(1).strip()
        if desc and len(desc) > 10:
            return desc
    
    meta_match = re.search(r'meta name="description"\s+content="(.*?)"', content)
    if meta_match:
        desc = meta_match.group(1).strip()
        if desc and len(desc) > 10:
            return desc
    
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
    if body_match:
        body = body_match.group(1)
        text = re.sub(r'<[^>]+>', ' ', body)
        text = re.sub(r'\s+', ' ', text).strip()
        if text and len(text) > 20:
            return text[:200] + "..." if len(text) > 200 else text
    
    return ""


def extract_title_from_content(content: str) -> str:
    """Витягує заголовок з HTML-контенту."""
    title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.DOTALL)
    if title_match:
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
        title = re.sub(r'\s+', ' ', title)
        if title and title not in ("Unknown", "Error fetching content"):
            return title
    
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if h1_match:
        title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        title = re.sub(r'\s+', ' ', title)
        if title and title not in ("Unknown", "Error fetching content"):
            return title
    
    url_match = re.search(r'source_url:\s*(\S+)', content)
    if url_match:
        url = url_match.group(1)
        if "/releases/tag/" in url:
            tag = url.split("/releases/tag/")[-1]
            repo = extract_repo_name_from_url(url)
            if repo:
                return f"{repo} {tag}"
            return f"Release {tag}"
        elif "/blog/" in url:
            parts = url.strip("/").split("/")
            return parts[-1].replace("-", " ").title() if parts else url
        elif "news.ycombinator.com" in url:
            return "Hacker News"
        elif "openai.com" in url:
            path = url.split("openai.com")[1].strip("/")
            if path:
                return path.replace("-", " ").title()
            return "OpenAI Blog"
        elif "google" in url:
            return "Google Blog"
    
    return "Unknown"


def extract_title_from_markdown(content: str) -> str:
    """Витягує заголовок з Markdown-файлу."""
    summary_match = re.search(r'summary:\s*(.+)', content)
    if summary_match:
        summary = summary_match.group(1).strip()
        if summary and summary != "Unknown":
            return summary[:120]
    
    url_match = re.search(r'source_url:\s*(\S+)', content)
    if url_match:
        url = url_match.group(1)
        if "/releases/tag/" in url:
            tag = url.split("/releases/tag/")[-1]
            repo = extract_repo_name_from_url(url)
            if repo:
                return f"{repo} {tag}"
            return f"Release {tag}"
        elif "openai.com" in url:
            path = url.split("openai.com")[1].strip("/")
            if path:
                return path.replace("-", " ").title()
        elif "/blog/" in url:
            parts = url.strip("/").split("/")
            return parts[-1].replace("-", " ").title() if parts else url
    
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h1_match:
        return h1_match.group(1).strip()[:100]
    
    return "Unknown"


# ---------------------------------------------------------------------------
# Article content fetching & summarization
# ---------------------------------------------------------------------------
def extract_text_from_html(html: str) -> str:
    """Витягує текст з HTML за допомогою trafilatura з fallback-стратегіями."""
    if not html or "<html" not in html.lower():
        return ""
    
    # Стратегія 1: trafilatura — тільки якщо повертає реальний текст
    try:
        text = trafilatura.extract(
            html,
            include_comments=False,
            include_tables=False,
            include_links=False,
            favor_precision=True,
        )
        if text and len(text) > 500:
            # Перевіряємо, чи це не просто frontmatter
            if "---" not in text or text.count("---") < 2:
                text = re.sub(r'[ \t]+', ' ', text)
                text = re.sub(r'\n{3,}', '\n\n', text)
                return text.strip()
    except Exception:
        pass
    
    # Стратегія 2: og:description (короткий опис)
    og_match = re.search(r'property="og:description"\s+content="(.*?)"', html)
    if og_match:
        desc = og_match.group(1).strip()
        if desc and len(desc) > 30:
            return desc
    
    # Стратегія 3: meta description
    meta_match = re.search(r'meta name="description"\s+content="(.*?)"', html)
    if meta_match:
        desc = meta_match.group(1).strip()
        if desc and len(desc) > 30:
            return desc
    
    # Стратегія 4: витягти <p> теги з body
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
    if body_match:
        body = body_match.group(1)
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', body, re.DOTALL)
        clean_ps = []
        for p in paragraphs:
            text_p = re.sub(r'<[^>]+>', '', p).strip()
            if len(text_p) > 30:
                clean_ps.append(text_p)
        if clean_ps:
            return " ".join(clean_ps[:10])
    
    # Стратегія 5: витягти <article>
    article_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    if article_match:
        text = re.sub(r'<[^>]+>', ' ', article_match.group(1))
        text = re.sub(r'\s+', ' ', text).strip()
        if len(text) > 50:
            return text
    
    return ""


def extractive_summarize(text: str, max_sentences: int = 5) -> str:
    """Extractive summarization: TF-IDF inspired sentence scoring.
    
    Вибирає найінформативніші речення на основі частоти слів.
    Гарантує максимум max_sentences речень.
    Агресивно фільтрує технічний контент (код, API, списки змін, інструкції).
    """
    if not text:
        return ""
    
    # Розбиваємо на речення
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 15]
    
    if not sentences:
        return ""
    
    if len(sentences) <= max_sentences:
        return "\n".join(sentences[:max_sentences])
    
    # Агресивно фільтруємо технічний контент
    filtered = []
    for sent in sentences:
        # Пропускаємо речення з кодом, API, списками змін
        if re.search(r'(use\s+|pub\s+|#[\w(]|impl\s+|fn\s+|struct\s+|let\s+)', sent):
            continue
        if re.search(r'(core::|std::|fn\s+\w+\s*\()', sent):
            continue
        # Пропускаємо речення з Rust/код патернами (assert!, panic!, debug_assert!, Debug)
        if re.search(r'(assert!\(|debug_assert!\(|panic!\(|\bDebug\b|matches!\()', sent, re.IGNORECASE):
            continue
        if re.search(r'(-\s+\w+\.|^\s*-\s+\w+)', sent):
            continue
        if re.search(r'(What\'s in|New Range|Associated iterators|Stabilized APIs)', sent):
            continue
        # Пропускаємо речення з командною строкою ($, rustup, php artisan, composer)
        if re.search(r'(\$\s+\w+|rustup\s+|php\s+artisan|composer\s+)', sent):
            continue
        # Пропускаємо речення з методом виклику (Http::, Route::)
        if re.search(r'(\w+::\w+\()', sent):
            continue
        # Пропускаємо речення з PHP/JS кодом ($request, );});, routes/)
        if re.search(r'(\$[a-zA-Z]|\);}|routes/|\.php)', sent):
            continue
        # Пропускаємо речення з Laravel/PHP атрибутами та технічними термінами
        if re.search(r'(LEGACY_BRIDGE|php_session|cookie сеансу|формат корисного|автентифікує|зашифрований формат|префікс сеансу|WithoutMiddleware|Middleware\]|Eloquent)', sent, re.IGNORECASE):
            continue
        # Пропускаємо речення з технічними деталями (CVE, ABI, IR, LLVM)
        if re.search(r'(CVE|libssh2|Cargo|LLVM|IR|rustup|compil|compil(?:er|ed|ation))', sent, re.IGNORECASE):
            continue
        # Пропускаємо речення з Rust-specific технічними деталями (mangle, ABI, crate, module path, generics)
        if re.search(r'(mangle|module path|defining crate|generics|Itanium ABI|nightly|stable Rust|release notes)', sent, re.IGNORECASE):
            continue
        # Пропускаємо речення з інструкціями установки
        if re.search(r'(install|setup|configure|download|get\s+started)', sent.lower()):
            # Але не пропускаємо, якщо це не чиста інструкція
            if re.search(r'(via|using|with|from|to)', sent.lower()):
                continue
        # Пропускаємо речення з URL/посиланнями
        if re.search(r'(https?://|www\.|github\.com/\w+/\w+)', sent):
            continue
        filtered.append(sent)
    
    if len(filtered) < len(sentences) * 0.35:
        # Якщо відфільтровано більше 65% — це технічна стаття, повертаємо порожнє
        return ""
    
    if not filtered:
        filtered = sentences  # fallback
    
    # Рахуємо частоту слів (без стоп-слів)
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
        'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'could', 'should', 'may', 'might', 'can', 'shall', 'it', 'its', 'this',
        'that', 'these', 'those', 'i', 'you', 'he', 'she', 'we', 'they', 'what',
        'which', 'who', 'whom', 'where', 'when', 'how', 'not', 'no', 'nor',
        'as', 'if', 'then', 'than', 'too', 'very', 'just', 'about', 'up',
    }
    
    word_freq = Counter()
    for sent in filtered:
        words = re.findall(r'[a-zA-Z]+', sent.lower())
        for w in words:
            if len(w) > 2 and w not in stop_words:
                word_freq[w] += 1
    
    if not word_freq:
        return "\n".join(filtered[:max_sentences])
    
    # Рахуємо score кожного речення
    sent_scores = []
    for i, sent in enumerate(filtered):
        words = re.findall(r'[a-zA-Z]+', sent.lower())
        score = sum(word_freq.get(w, 0) for w in words)
        # Бонус за позицію (перші речення важливіші)
        pos_bonus = 1.0 / (1 + i * 0.1)
        # Бонус за довжину (не занадто короткі)
        len_bonus = min(len(words) / 10.0, 1.5)
        sent_scores.append((score * pos_bonus * len_bonus, i, sent))
    
    # Сортуємо за score, беремо топ-N
    sent_scores.sort(reverse=True)
    top_indices = sorted([s[1] for s in sent_scores[:max_sentences]])
    
    result = "\n".join(filtered[i] for i in top_indices)
    # Гарантуємо максимум max_sentences речень
    final_sentences = [s.strip() for s in result.split('\n') if s.strip()]
    return "\n".join(final_sentences[:max_sentences])


def summarize_and_translate(html_content: str, fallback_title: str,
                            max_sentences: int = 5) -> str:
    """Витягує текст з HTML, генерує переказ, перекладає українською.
    
    Повертає стислий переказ максимум max_sentences речень українською.
    """
    if not html_content:
        return ""
    
    # Витягуємо текст з HTML
    text = extract_text_from_html(html_content)
    if not text or len(text) < 50:
        return ""
    
    # Extractive summarization
    summary_en = extractive_summarize(text, max_sentences)
    if not summary_en or len(summary_en) < 20:
        return ""
    
    # Переклад
    summary_uk = translate_text(summary_en)
    return summary_uk


# ---------------------------------------------------------------------------
# Categorization
# ---------------------------------------------------------------------------
def categorize_article(source: str, filename: str) -> str:
    """Визначає категорію статті за джерелом."""
    if source == "ArXiv AI":
        return None
    
    if source.startswith("github:"):
        parts = source.split(":")[1]
        repo = parts.split("/")[1].lower()
        if "hermes" in repo or "opencode" in repo or "cline" in repo or "kilo" in repo or "aider" in repo or "pi" in repo:
            return "🤖 AI Agents"
        elif "pytorch" in repo or "tensorflow" in repo or "transformers" in repo or "diffusers" in repo:
            return "🤖 AI / ML"
        elif "langchain" in repo or "autogen" in repo or "axolotl" in repo or "unsloth" in repo:
            return "🤖 AI / ML"
        elif "vllm" in repo or "ollama" in repo or "llamacpp" in repo or "ggml" in repo:
            return "🤖 AI / ML"
        elif "peft" in repo or "accelerate" in repo or "datasets" in repo or "optimum" in repo:
            return "🤖 AI / ML"
        elif "whisper" in repo or "sentence-transformers" in repo or "tokenizers" in repo:
            return "🤖 AI / ML"
        elif "trl" in repo or "text-generation-inference" in repo:
            return "🤖 AI / ML"
        elif "faiss" in repo or "llama-recipes" in repo:
            return "🤖 AI / ML"
        elif "mistralrs" in repo or "bitsandbytes" in repo:
            return "🤖 AI / ML"
        elif "gemma" in repo or "llama-models" in repo or "qwen36" in repo or "re2" in repo:
            return "🤖 AI / ML"
        elif "python" in repo:
            return "💻 Programming"
        elif "go" in repo:
            return "💻 Programming"
        elif "rust" in repo:
            return "💻 Programming"
        else:
            return "🚀 GitHub Releases"
    
    if source.startswith("huggingface:"):
        return "🤗 HuggingFace"
    
    if source.startswith("gh-"):
        return "🐙 GitHub Issues"
    
    for key, cat in CATEGORY_MAP.items():
        if key.lower() in source.lower():
            return cat
    
    if "gh-" in filename:
        return "🚀 GitHub Releases"
    if "hf-" in filename:
        return "🤗 HuggingFace"
    
    return "📰 General"


def is_low_quality_title(title: str) -> bool:
    """Фільтрує низькоякісні заголовки."""
    if not title or title == "Unknown":
        return True
    if title in ("MachineLearning", "Medium", "Hacker News", 
                 "Computer Science > Machine Learning", 
                 "Computer Science > Computation and Language"):
        return True
    if len(title) < 15:
        return True
    low_quality_phrases = ["pointer-events", "translate()", "translateX()", "translateY()", "translateZ()"]
    for phrase in low_quality_phrases:
        if phrase in title:
            return True
    bad_hn = ["Dan Kendalls", "Unicode text processing"]
    for bad in bad_hn:
        if bad in title:
            return True
    return False


def deduplicate_titles(articles: list) -> list:
    """Видаляє дублікати заголовків у межах категорії."""
    seen = set()
    unique = []
    for art in articles:
        normalized = art.title.lower().strip()
        if normalized not in seen:
            seen.add(normalized)
            unique.append(art)
    return unique


def filter_release_duplicates(articles: list) -> list:
    """Для TypeScript/Release — залишає лише Final, не Beta/RC."""
    filtered = []
    version_map = {}
    for art in articles:
        title_lower = art.title.lower()
        if "announcing typescript" in title_lower:
            if "beta" in title_lower or "rc" in title_lower or "progress" in title_lower:
                continue
            m = re.search(r'typescript (\d+\.\d+(?:\.\d+)?)', title_lower)
            if m:
                ver = m.group(1)
                key = f"ts-{ver}"
                if key not in version_map:
                    version_map[key] = art
                continue
        if "python" in title_lower and ("beta" in title_lower or "release candidate" in title_lower or "rc" in title_lower):
            continue
        filtered.append(art)
    filtered.extend(version_map.values())
    return filtered


# ---------------------------------------------------------------------------
# Digest builder
# ---------------------------------------------------------------------------
def build_digest(since: datetime) -> tuple:
    """Будує дайджест з raw-файлів за останні 24 години."""
    sections = {}
    total_articles = 0
    
    if not RAW_DIR.exists():
        return [], 0
    
    files = list(RAW_DIR.glob("*.md"))
    
    for filepath in files:
        try:
            content = filepath.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        
        fm = parse_frontmatter(content)
        source = fm.get("blog_source", "unknown")
        url = fm.get("source_url", "")
        ingested = fm.get("ingested", "")
        
        # Parse ingested date
        if ingested:
            try:
                ingested_dt = datetime.strptime(ingested, "%Y-%m-%d").replace(tzinfo=timezone.utc)
                if ingested_dt < since.replace(hour=0, minute=0, second=0):
                    continue
            except ValueError:
                continue
        else:
            try:
                mtime = datetime.fromtimestamp(filepath.stat().st_mtime, tz=timezone.utc)
                if mtime < since:
                    continue
            except Exception:
                continue
        
        # Extract title and description
        if "<!DOCTYPE" in content or "<html" in content:
            title = extract_title_from_content(content)
            description = extract_description_from_html(content)
        else:
            title = extract_title_from_markdown(content)
            summary_match = re.search(r'summary:\s*(.+)', content)
            description = summary_match.group(1).strip() if summary_match else ""
        
        # Categorize
        category = categorize_article(source, filepath.name)
        if category is None:
            continue
        
        # Filter low-quality
        if is_low_quality_title(title):
            continue
        
        # === FILTER: stale Google Research Blog (2024 articles) ===
        if "google research blog" in source.lower():
            if "2024/" in url:
                continue
            if ingested:
                try:
                    ingested_dt = datetime.strptime(ingested, "%Y-%m-%d").replace(tzinfo=timezone.utc)
                    if ingested_dt.year < 2025:
                        continue
                except ValueError:
                    pass
            else:
                if "2024" in filepath.name:
                    continue
        
        # === FILTER: Oracle DBA Soyma — не LLM-контент ===
        if source == "Oracle DBA Soyma":
            continue
        
        # === FILTER: JetBrains — лише релізи IDE (без описів) ===
        if source == "JetBrains Blog":
            if not description and "2026" in title:
                continue
        
        # === FILTER: Rust release announcements — технічні, без змістовного переказу ===
        if source == "Rust Blog":
            if re.search(r'Announcing Rust \d+\.\d+', title, re.IGNORECASE):
                continue
        
        # === FILTER: Laravel News — технічний контент, без загального переказу ===
        if source == "Laravel News":
            continue
        
        # Clean title suffixes
        title = clean_title_suffix(title)
        
        article = Article(
            filename=filepath.name,
            title=title,
            summary=description,
            source=source,
            category=category,
            url=url,
            ingested=ingested,
        )
        
        if category not in sections:
            sections[category] = []
        sections[category].append(article)
        total_articles += 1
    
    # Deduplicate
    for cat in sections:
        sections[cat] = deduplicate_titles(sections[cat])
    
    # Filter release duplicates
    for cat in sections:
        sections[cat] = filter_release_duplicates(sections[cat])
    
    # Limit per category to 12 (before summarization)
    MAX_PER_CATEGORY = 12
    for cat in sections:
        if len(sections[cat]) > MAX_PER_CATEGORY:
            sections[cat] = sections[cat][:MAX_PER_CATEGORY]
    
    # Sort by count descending
    sorted_sections = sorted(sections.items(), key=lambda x: len(x[1]), reverse=True)
    
    return sorted_sections, total_articles


def select_top_stories(sections: list) -> list:
    """Виділяє Top Stories з AI/ML категорії."""
    top_stories = []
    for category, articles in sections:
        if "AI / ML" in category:
            for art in articles[:5]:
                art.is_top = True
                top_stories.append(art)
            break
    return top_stories


# ---------------------------------------------------------------------------
# Compact formatter (Telegram-friendly)
# ---------------------------------------------------------------------------
def format_compact(sections: list, total: int, date_str: str) -> str:
    """Форматує дайджест у новому стилі (Telegram-friendly).
    
    Структура на категорію:
    ### 🤖 AI / ML
    🧠 **Заголовок новини**
    Стислий переказ українською (макс 5 речень).
    📎 [Джерело](url)
    
    ---
    """
    lines = []
    
    # === HEADER ===
    lines.append(f"📰 *{date_str}*")
    lines.append("")
    
    # === SECTIONS BY CATEGORY (5 top per category) ===
    for category, articles in sections:
        lines.append(f"### {category}")
        lines.append("")
        
        for art in articles[:5]:
            # Тематична іконка
            icon_map = {
                "🤖 AI / ML": "🧠",
                "💻 Programming": "⌨️",
                "🗄️ Databases": "🗃️",
                "🧮 Algorithms": "📐",
                "🛠️ IDE / Tools": "🔧",
                "📰 General": "📢",
                "🚀 GitHub Releases": "📦",
                "🤖 AI Agents": "🤖",
                "🚀 AI Startups": "🚀",
                "🤗 HuggingFace": "🤗",
                "🐙 GitHub Issues": "🐛",
                "📁 Local": "📂",
            }
            icon = icon_map.get(category, "📌")
            
            # Заголовок
            lines.append(f"{icon} **{art.title}**")
            
            # Переказ (якщо є)
            if art.summary_uk:
                lines.append(art.summary_uk)
            
            # Посилання на джерело
            if art.url:
                lines.append(f"📎 {art.url}")
            
            lines.append("")
    
    # === FOOTER ===
    lines.append("---")
    now = datetime.now(timezone.utc)
    lines.append(f"*Згенеровано:* {now.strftime('%H:%M UTC')}")
    lines.append(f"*Джерела:* RSS + GitHub + HuggingFace")
    lines.append("*LLM-Wiki Daily Gazette*")
    
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Stats helpers
# ---------------------------------------------------------------------------
def read_feeds_count() -> int:
    """Reads FEEDS count from source_monitor.py."""
    try:
        sm_path = ROOT / "tools" / "source_monitor.py"
        content = sm_path.read_text()
        m = re.search(r'FEEDS = \{(.*?)\}', content, re.DOTALL)
        if m:
            feeds_section = m.group(1)
            names = re.findall(r'^\s+"([^"]+)"\s*:', feeds_section, re.MULTILINE)
            return len(names)
    except Exception:
        pass
    return 39


def count_wiki_pages() -> int:
    """Counts wiki pages."""
    wiki_dir = ROOT / "wiki"
    if wiki_dir.exists():
        return len([f for f in wiki_dir.rglob("*.md") if f.is_file()])
    return 0


def count_raw_articles() -> int:
    """Counts raw articles."""
    if RAW_DIR.exists():
        return len([f for f in RAW_DIR.rglob("*.md") if f.is_file()])
    return 0


# ---------------------------------------------------------------------------
# Debug
# ---------------------------------------------------------------------------
DEBUG = False

def debug(*args, **kwargs):
    if DEBUG:
        print("[DEBUG]", *args, **kwargs)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    import argparse
    parser = argparse.ArgumentParser(description="Newspaper Digest — daily wiki newsletter")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    parser.add_argument("--hours", type=int, default=24, help="Lookback hours (default: 24)")
    parser.add_argument("--dry-run", action="store_true", help="Only print without saving")
    args = parser.parse_args()
    global DEBUG
    DEBUG = args.debug
    
    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=args.hours)
    date_str = now.strftime("%B %d, %Y")
    
    debug(f"⏰ Current UTC: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    debug(f"📅 Lookback: {args.hours}h → since={since.strftime('%Y-%m-%d %H:%M:%S')}")
    debug(f"📁 RAW_DIR: {RAW_DIR}")
    debug(f"📁 RAW_DIR exists: {RAW_DIR.exists()}")
    
    if RAW_DIR.exists():
        all_files = list(RAW_DIR.glob("*.md"))
        debug(f"📄 Total .md files in RAW_DIR: {len(all_files)}")
        for f in sorted(all_files)[-5:]:
            stat = f.stat()
            mtime = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
            debug(f"   {f.name} | mtime={mtime.strftime('%Y-%m-%d %H:%M')} | size={stat.st_size}")
    
    # Build digest
    debug("🔨 Building digest...")
    sections, total = build_digest(since)
    
    debug(f"📊 Total articles: {total}")
    debug(f"📂 Categories found: {len(sections)}")
    for cat, arts in sections:
        debug(f"   {cat}: {len(arts)} articles")
        for a in arts[:3]:
            debug(f"      - {a.title[:60]} | source={a.source[:40]} | cat={a.category}")
    
    if not sections:
        print("📭 Ніяких новин за останні 24 години.")
        return
    
    # === SUMMARIZE & TRANSLATE top 5 per category ===
    MAX_SUMMARY = 5
    articles_to_summarize = []
    
    # Top stories from AI/ML
    top_stories = select_top_stories(sections)
    articles_to_summarize.extend(top_stories)
    
    # Top 5 from each other category
    for category, articles in sections:
        if top_stories and "AI / ML" in category:
            continue  # already covered
        for art in articles[:MAX_SUMMARY]:
            articles_to_summarize.append(art)
    
    debug(f"📝 Articles to summarize: {len(articles_to_summarize)}")
    
    # Batch fetch & summarize from raw file content
    # Build a map of filename -> full content
    raw_content_map = {}
    for filepath in RAW_DIR.glob("*.md"):
        try:
            raw_content_map[filepath.name] = filepath.read_text(encoding="utf-8", errors="replace")
        except Exception:
            pass
    
    for i, art in enumerate(articles_to_summarize):
        debug(f"  [{i+1}/{len(articles_to_summarize)}] {art.title[:60]}...")
        try:
            html_content = raw_content_map.get(art.filename, "")
            art.summary_uk = summarize_and_translate(
                html_content, art.title, max_sentences=5
            )
        except Exception as e:
            debug(f"    ERROR: {e}")
            art.summary_uk = ""
    
    # Format as compact digest
    debug("🎨 Formatting compact digest...")
    digest = format_compact(sections, total, date_str)
    
    print(digest)
    
    debug("✅ Digest generation complete.")


if __name__ == "__main__":
    main()
