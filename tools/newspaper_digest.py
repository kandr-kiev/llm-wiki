#!/usr/bin/env python3
"""Newspaper Digest — щоденна електронна газета з новинами LLM-Wiki.

Парсить raw-файли за останні 24 години, витягує заголовки з frontmatter,
формує красивий Markdown-дайджест з іконками, бейджями та Top Stories.

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
    "🚀 AI Startups": "🚀",
    "🤗 HuggingFace": "🤗",
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
    is_top: bool = False  # чи є Top Story


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


def extract_repo_name_from_url(url: str) -> str:
    """Витягує назву репо з URL GitHub releases."""
    if "/releases/tag/" in url:
        parts = url.split("/releases/tag/")[0].split("/")
        if len(parts) >= 2:
            return parts[-1]  # owner/repo -> repo name (last segment)
    return ""


def extract_title_from_content(content: str) -> str:
    """Витягує заголовок з HTML-контенту."""
    # Спроба з H1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if h1_match:
        title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        title = re.sub(r'\s+', ' ', title)
        if title and title not in ("Unknown", "Error fetching content"):
            return title

    # Спроба з <title>
    title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.DOTALL)
    if title_match:
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
        title = re.sub(r'\s+', ' ', title)
        if title and title not in ("Unknown", "Error fetching content"):
            return title

    # Fallback: з frontmatter URL (extract meaningful part)
    url_match = re.search(r'source_url:\s*(\S+)', content)
    if url_match:
        url = url_match.group(1)
        # Extract meaningful part from URL
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
            # Extract from openai.com URL path
            path = url.split("openai.com")[1].strip("/")
            if path:
                return path.replace("-", " ").title()
            return "OpenAI Blog"
        elif "google" in url:
            return "Google Blog"

    return "Unknown"


def extract_title_from_markdown(content: str) -> str:
    """Витягує заголовок з Markdown-файлу."""
    # Спочатку перевіряємо URL для кращих заголовків
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

    # H1 — fallback
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


def select_top_stories(sections: list) -> list:
    """Виділяє Top Stories з AI/ML категорії (якщо є)."""
    top_stories = []
    
    # Шукаємо AI/ML категорію
    for category, articles in sections:
        if "AI / ML" in category:
            # Беремо перші 3 (або менше)
            for art in articles[:3]:
                art.is_top = True
                top_stories.append(art)
            break
    
    return top_stories


def format_digest(sections: list, total: int, date_str: str) -> str:
    """Форматує дайджест як електронну газету."""
    lines = []

    # === HEADER ===
    lines.append("📰✨ **LLM-WIKI DAILY GAZETTE** ✨📰")
    lines.append(f"🗓️ *{date_str}*")
    lines.append("")
    lines.append("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    lines.append("")

    # === TOP STORIES ===
    top_stories = select_top_stories(sections)
    if top_stories:
        lines.append("⭐ **TOP STORIES**")
        lines.append("🏆 Найважливіші новини дня")
        lines.append("")
        lines.append("─── ⭐ ───")
        lines.append("")
        
        for i, art in enumerate(top_stories, 1):
            display_title = art.title
            if len(display_title) > 80:
                display_title = display_title[:77] + "..."
            
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
            
            # Category badge
            cat_emoji = art.category.split()[0] if art.category else "📌"
            
            lines.append(f"  {i}. **{display_title}**")
            lines.append(f"     {source_label} • {cat_emoji}")
            if art.url:
                lines.append(f"     🔗 {art.url}")
            lines.append("")

    # === STATS SUMMARY ===
    lines.append("─── 📊 ───")
    lines.append("")
    lines.append("📈 **Новин за 24г:** " + str(total))
    lines.append("📡 **RSS-джерел моніторингу:** " + str(read_feeds_count()))
    lines.append("📚 **Wiki-сторінок:** " + str(count_wiki_pages()))
    lines.append("📄 **Raw-статей:** " + str(count_raw_articles()))
    lines.append("")

    # === SECTION BY CATEGORY ===
    for category, articles in sections:
        icon = CATEGORY_ICONS.get(category, "📌")

        lines.append("─── " + icon + " ───")
        lines.append(f"**{category}** ({len(articles)})")
        lines.append("")

        for i, art in enumerate(articles, 1):
            # Skip if already in Top Stories
            if art.is_top:
                continue
                
            display_title = art.title
            if len(display_title) > 80:
                display_title = display_title[:77] + "..."

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

            # Category badge
            cat_emoji = art.category.split()[0] if art.category else "📌"

            lines.append(f"  {i}. **{display_title}**")
            lines.append(f"     {source_label} • {cat_emoji}")
            if art.url:
                lines.append(f"     🔗 {art.url}")
            lines.append("")

    # === FOOTER ===
    lines.append("─── 📌 ───")
    lines.append("")
    now = datetime.now(timezone.utc)
    lines.append(f"⏰ **Згенеровано:** {now.strftime('%H:%M UTC')}")
    lines.append(f"🔄 **Наступний дайджест:** завтра о 09:00 UTC")
    lines.append(f"📡 **Джерела:** RSS ({read_feeds_count()}) + GitHub Releases + HuggingFace")
    lines.append(f"🔗 **Wiki:** https://github.com/kandr-kiev/llm-wiki")
    lines.append("")
    lines.append("*📰 LLM-Wiki Daily Gazette • Powered by Source Monitor 🤖*")

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
# Debug helpers
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

    # Calculate lookback
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
        for f in sorted(all_files)[-5:]:  # last 5 files
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

    # Format
    debug("🎨 Formatting digest...")
    digest = format_digest(sections, total, date_str)

    print(digest)

    debug("✅ Digest generation complete.")


if __name__ == "__main__":
    main()
