#!/usr/bin/env python3
"""Newspaper Digest — щоденна електронна газета з новинами LLM-Wiki.

Парсить raw-файли за останні 24 години, витягує заголовки з frontmatter,
формує красивий Markdown-дайджест з іконками та категоріями.

Використання:
    python3 tools/newspaper_digest.py [--dry-run]
    
Вивід:
    - stdout: готовий Markdown для Telegram
    - --dry-run: лише вивід без збереження
"""
import os
import re
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field
from typing import Optional

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
    "🤗 HuggingFace": "🦗",
    "🐙 GitHub Issues": "🐛",
    "📁 Local": "📂",
}

# Категоризація за blog_source
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
    "CSS Tricks": "📰 General",
    "Smashing Magazine": "📰 General",
}


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------
@dataclass
class Article:
    filename: str
    title: str
    source: str  # blog_source або github:owner/repo
    category: str
    url: str
    ingested: str


# ---------------------------------------------------------------------------
# Parsing
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


def extract_title_from_content(content: str) -> str:
    """Витягує заголовок з HTML-контенту."""
    # Спроба з H1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if h1_match:
        title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        title = re.sub(r'\s+', ' ', title)
        if title and title != "Unknown":
            return title

    # Спроба з <title>
    title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.DOTALL)
    if title_match:
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
        title = re.sub(r'\s+', ' ', title)
        if title and title != "Unknown":
            return title

    # Fallback: з frontmatter URL (extract meaningful part)
    url_match = re.search(r'source_url:\s*(\S+)', content)
    if url_match:
        url = url_match.group(1)
        # Extract meaningful part from URL
        if "/releases/tag/" in url:
            tag = url.split("/releases/tag/")[-1]
            return f"Release {tag}"
        elif "/blog/" in url:
            parts = url.strip("/").split("/")
            return parts[-1].replace("-", " ").title() if parts else url
        elif "news.ycombinator.com" in url:
            return "Hacker News"
        elif "openai.com" in url:
            return "OpenAI Blog"
        elif "google" in url:
            return "Google Blog"

    return "Unknown"


def extract_title_from_markdown(content: str) -> str:
    """Витягує заголовок з Markdown-файлу."""
    # H1
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h1_match:
        return h1_match.group(1).strip()[:100]

    return "Unknown"


def categorize_article(source: str, filename: str) -> str:
    """Визначає категорію статті за джерелом."""
    # ArXiv — фільтруємо (дублікати, погані заголовки)
    if source == "ArXiv AI":
        return None  # Signal to skip this article

    # GitHub releases
    if source.startswith("github:"):
        parts = source.split(":")[1]  # owner/repo
        repo = parts.split("/")[1].lower()
        if "pytorch" in repo or "tensorflow" in repo or "transformers" in repo or "diffusers" in repo:
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

    # HuggingFace
    if source.startswith("huggingface:"):
        return "🤗 HuggingFace"

    # GitHub issues
    if source.startswith("gh-"):
        return "🐙 GitHub Issues"

    # RSS sources
    for key, cat in CATEGORY_MAP.items():
        if key.lower() in source.lower():
            return cat

    # Fallback за filename
    if "gh-" in filename:
        return "🚀 GitHub Releases"
    if "hf-" in filename:
        return "🤗 HuggingFace"

    return "📰 General"


# ---------------------------------------------------------------------------
# Digest builder
# ---------------------------------------------------------------------------
def build_digest(since: datetime) -> tuple:
    """Будує дайджест з raw-файлів за останні 24 години."""
    sections = {}
    total_articles = 0

    if not RAW_DIR.exists():
        return [], 0

    # Get all .md files
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
                    continue  # Older than 24h
            except ValueError:
                continue
        else:
            # Fallback: check file modification time
            try:
                mtime = datetime.fromtimestamp(filepath.stat().st_mtime, tz=timezone.utc)
                if mtime < since:
                    continue
            except Exception:
                continue

        # Extract title from content
        if "<!DOCTYPE" in content or "<html" in content:
            title = extract_title_from_content(content)
        else:
            title = extract_title_from_markdown(content)

        # Categorize
        category = categorize_article(source, filepath.name)
        if category is None:
            continue  # Skip filtered sources (ArXiv)

        article = Article(
            filename=filepath.name,
            title=title,
            source=source,
            category=category,
            url=url,
            ingested=ingested,
        )

        if category not in sections:
            sections[category] = []
        sections[category].append(article)
        total_articles += 1

    # Sort sections by count descending
    sorted_sections = sorted(
        sections.items(),
        key=lambda x: len(x[1]),
        reverse=True,
    )

    return sorted_sections, total_articles


def format_digest(sections: list, total: int, date_str: str) -> str:
    """Форматує дайджест як електронну газету."""
    lines = []

    # === HEADER ===
    lines.append("📰 **LLM-WIKI DAILY GAZETTE**")
    lines.append(f"🗓️ {date_str}")
    lines.append("")
    lines.append("─" * 40)
    lines.append("")

    # === STATS SUMMARY ===
    lines.append("📊 **ЗАГАЛЬНА СТАТИСТИКА**")
    lines.append("")
    lines.append(f"📈 **Новин за 24г:** {total}")
    lines.append(f"📡 **RSS-джерел моніторингу:** {read_feeds_count()}")
    lines.append(f"📚 **Wiki-сторінок:** {count_wiki_pages()}")
    lines.append(f"📄 **Raw-статей:** {count_raw_articles()}")
    lines.append("")

    # === SECTION BY CATEGORY ===
    for category, articles in sections:
        icon = CATEGORY_ICONS.get(category, "📌")

        lines.append(f"{'─' * 40}")
        lines.append(f"{icon} **{category}** ({len(articles)})")
        lines.append(f"{'─' * 40}")
        lines.append("")

        for i, art in enumerate(articles, 1):
            # Short title or truncate
            display_title = art.title
            if len(display_title) > 100:
                display_title = display_title[:97] + "..."

            # Source label
            source_label = art.source
            if source_label.startswith("github:"):
                source_label = "🐙 " + source_label.split(":")[1]
            elif source_label.startswith("huggingface:"):
                source_label = "🤗 " + source_label.split(":")[1]
            elif source_label.startswith("gh-"):
                source_label = "🐛 " + source_label.split("-")[2]
            else:
                source_label = f"📡 {source_label}"

            lines.append(f"  {i}. **{display_title}**")
            lines.append(f"     {source_label}")
            if art.url:
                lines.append(f"     🔗 {art.url}")
            lines.append("")

    # === FOOTER ===
    lines.append("─" * 40)
    lines.append("")
    lines.append("📌 **Джерела:** RSS (39) + GitHub Releases + HuggingFace + Local")
    lines.append("🔄 **Наступний дайджест:** завтра о 09:00 UTC")
    lines.append("🔗 **Wiki:** https://github.com/kandr-kiev/llm-wiki")
    lines.append("")
    lines.append("*LLM-Wiki Daily Gazette • Powered by Source Monitor*")

    return "\n".join(lines)


def read_feeds_count() -> int:
    """Reads FEEDS count from source_monitor.py."""
    try:
        sm_path = ROOT / "tools" / "source_monitor.py"
        content = sm_path.read_text()
        m = re.search(r'FEEDS = \{(.*?)\}', content, re.DOTALL)
        if m:
            feeds_section = m.group(1)
            # Count only keys (lines starting with quote, not URLs)
            # Pattern: "Name": "url" — count the first quoted string per line
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
# Main
# ---------------------------------------------------------------------------
def main():
    # Calculate 24h ago
    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=24)
    date_str = now.strftime("%B %d, %Y")  # e.g. "July 16, 2026"

    # Build digest
    sections, total = build_digest(since)

    if not sections:
        print("📭 Ніяких новин за останні 24 години.")
        return

    # Format
    digest = format_digest(sections, total, date_str)

    print(digest)


if __name__ == "__main__":
    main()
