#!/usr/bin/env python3
"""Source Monitor for LLM Wiki — об'єднаний монітор RSS + GitHub + Local.

Заміна трьох окремих моніторів одним скриптом:
  - RSS Feeds → raw/articles/
  - GitHub Releases → raw/articles/
  - Local Files → raw/articles/

Використовує canonical utils (build_frontmatter, compute_sha256, slugify).
Вивід: standard_report.py format_report_simple.
"""
import os
import sys
import feedparser
import requests
import subprocess
from pathlib import Path
from datetime import datetime, timezone

from utils import (
    compute_sha256,
    append_to_log,
    slugify,
    build_frontmatter,
    check_dir_exists,
    split_frontmatter,
    retry_for_status,
)
from standard_report import format_report_simple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw" / "articles"
LOG_FILE = ROOT / "log.md"

# ---------------------------------------------------------------------------
# RSS Feeds
# ---------------------------------------------------------------------------
RSS_DB = ROOT / ".processed" / "rss_urls.txt"
FEEDS = {
    # === AI / ML ===
    "Andrej Karpathy": "https://karpathy.bearblog.dev/feed/",
    "Chip Huyen": "https://huyenchip.com/feed",
    "Lilian Weng": "https://lilianweng.github.io/lil-log/feed.xml",
    "Jay Alammar": "https://jalammar.github.io/feed.xml",
    "Hacker News AI": "https://hnrss.org/frontpage?q=AI",
    "ArXiv AI": "https://export.arxiv.org/rss/cs.AI",
    "Cloudflare Blog": "https://blog.cloudflare.com/rss/",
    "OpenAI Blog": "https://openai.com/blog/rss.xml",
    "Google DeepMind": "https://blog.google/technology/ai/rss/",
    "Distill AI": "https://distill.pub/rss.xml",
    "Papers With Code": "https://paperswithcode.com/rss",
    "Hugging Face Blog": "https://huggingface.co/blog/feed.xml",
    "The Gradient": "https://thegradient.substack.com/feed",
    "r/MachineLearning": "https://old.reddit.com/r/MachineLearning/.rss",
    "MarkTechPost": "https://www.marktechpost.com/feed",
    "MIT Tech Review AI": "https://www.technologyreview.com/topic/artificial-intelligence/feed",
    "The Verge AI": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
    "OpenAI News": "https://openai.com/news/rss.xml",
    "Meta AI Blog": "https://ai.meta.com/blog/rss/",
    "Hacker News": "https://hnrss.org/frontpage",
    # === AI Startups ===
    "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
    "TechCrunch Startups": "https://techcrunch.com/category/startups/feed/",
    "TechCrunch Venture": "https://techcrunch.com/category/venture/feed/",
    "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
    # === Programming Languages ===
    "Python Insider": "https://blog.python.org/rss.xml",
    "Planet Python": "https://planet.python.org/rss20.xml",
    "TypeScript Blog": "https://devblogs.microsoft.com/typescript/feed/",
    "Rust Blog": "https://blog.rust-lang.org/feed.xml",
    "Laravel News": "https://laravel-news.com/feed",
    # === Databases ===
    "Oracle DBA Soyma": "https://dbasoumya.blogspot.com/feeds/posts/default?alt=rss",
    # === Algorithms / CS ===
    "Google Research Blog": "https://blog.research.google/atom.xml",
    "Algorithm Design": "https://www3.cs.stonybrook.edu/~skiena/",
    "CS Theory": "https://www.cs.cmu.edu/~odonnell/",
    "Algorithm Corner": "https://algorithmcorner.com/feed/",
    # === IDE / Dev Tools ===
    "JetBrains Blog": "https://blog.jetbrains.com/feed/",
    "PyCharm Blog": "https://blog.jetbrains.com/pycharm/feed/",
    "VS Code Blog": "https://code.visualstudio.com/feed.xml",
    "IntelliJ Blog": "https://blog.jetbrains.com/idea/feed/",
    # === General Programming ===
    "GitHub Blog": "https://github.blog/feed/",
    "Microsoft Dev Blog": "https://devblogs.microsoft.com/dotnet/feed/",
    "Dev Community": "https://dev.to/feed",
    "FreeCodeCamp Blog": "https://www.freecodecamp.org/news/rss/",
    "Netflix Tech Blog": "https://netflixtechblog.com/feed",
    "Hanselminutes": "https://www.hanselminutes.com/feed/hanselminutes.xml",
    "CSS Tricks": "https://css-tricks.com/feed/",
    "Smashing Magazine": "https://www.smashingmagazine.com/feed/",
}


def is_new_article(url: str) -> bool:
    if not RSS_DB.exists():
        return True
    with open(RSS_DB, 'r') as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]
    return url not in urls


def mark_article_read(url: str):
    with open(RSS_DB, 'a') as f:
        f.write(url + '\n')


def fetch_article_content(url: str) -> str:
    try:
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'LLM-Wiki-Source-Monitor/1.0'
        })
        response.raise_for_status()
        return response.text[:50000]
    except Exception as e:
        return f"Error fetching content: {e}"


def save_raw_article(title: str, url: str, content: str, source_blog: str) -> str:
    slug = slugify(title)
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    filename = f"{slug}-{date_str}.md"

    filepath = RAW_DIR / filename
    frontmatter = build_frontmatter(source_url=url, blog_source=source_blog)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)

    # Update SHA256
    file_content = filepath.read_text(encoding='utf-8')
    fm, body = split_frontmatter(file_content)
    if fm is not None:
        sha = compute_sha256(body)
        new_fm = fm.replace('sha256: PLACEHOLDER', f'sha256: {sha}')
        new_content = '---\n' + new_fm + '\n---\n' + body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return str(filepath.relative_to(ROOT))


# ---------------------------------------------------------------------------
# GitHub Releases
# ---------------------------------------------------------------------------
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')
GITHUB_DB = ROOT / ".processed" / "github_releases.txt"

# GitHub repos to monitor - AI/ML focused
# Single source of truth: github_repos.py
from github_repos import REPOS as GITHUB_REPOS


def _auth_headers():
    headers = {
        'User-Agent': 'LLM-Wiki-Source-Monitor/1.0',
        'Accept': 'application/vnd.github.v3+json',
    }
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'
    return headers


def is_new_release(repo: str, release_tag: str) -> bool:
    if not GITHUB_DB.exists():
        return True
    key = f"{repo}#{release_tag}"
    with open(GITHUB_DB, 'r') as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]
    return key not in urls


def mark_release_read(repo: str, release_tag: str):
    with open(GITHUB_DB, 'a') as f:
        f.write(f"{repo}#{release_tag}\n")


def fetch_release_content(repo: str, release_tag: str) -> str:
    try:
        url = f"https://api.github.com/repos/{repo}/releases/tags/{release_tag}"
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'LLM-Wiki-Source-Monitor/1.0',
            'Accept': 'application/vnd.github.v3+json'
        })
        response.raise_for_status()
        data = response.json()
        body = data.get('body', 'No body')
        return f"# Release {release_tag}\n\n{body}"
    except Exception as e:
        return f"Error fetching release: {e}"


def save_raw_release(repo: str, release_tag: str, content: str) -> str:
    slug = f"gh-{slugify(release_tag)}"
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    filename = f"{slug}-{date_str}.md"

    filepath = RAW_DIR / filename
    frontmatter = build_frontmatter(
        source_url=f"https://github.com/{repo}/releases/tag/{release_tag}",
        blog_source=f"github:{repo}"
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)

    # Update SHA256
    file_content = filepath.read_text(encoding='utf-8')
    fm, body = split_frontmatter(file_content)
    if fm is not None:
        sha = compute_sha256(body)
        new_fm = fm.replace('sha256: PLACEHOLDER', f'sha256: {sha}')
        new_content = '---\n' + new_fm + '\n---\n' + body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return str(filepath.relative_to(ROOT))


# ---------------------------------------------------------------------------
# HuggingFace Hub Models
# ---------------------------------------------------------------------------
HF_DB = ROOT / ".processed" / "hf_models.txt"
HF_MODELS = [
    # === Chinese AI Labs — DeepSeek ===
    "deepseek-ai/DeepSeek-V4-Pro",    # V4 Pro — 1.6T MoE, 1M context
    "deepseek-ai/DeepSeek-V4-Flash",  # V4 Flash — cost-efficient
    "deepseek-ai/DeepSeek-V3.2",      # V3.2 — Thinking in Tool-Use
    "deepseek-ai/DeepSeek-R1",        # R1 — reasoning breakthrough
    # === Chinese AI Labs — Zhipu AI (Z.ai) ===
    "zai-org/GLM-5",      # GLM-5 — 744B MoE (40B active), MIT license
    "zai-org/GLM-5.1",    # GLM-5.1 — coding-focused variant
    "zai-org/GLM-5.2",    # GLM-5.2 — long-horizon, 1M context
    # === Chinese AI Labs — Moonshot AI (Kimi) ===
    "moonshotai/Kimi-K2.5",                     # K2.5 — multimodal agentic
    "moonshotai/Kimi-K2.6",                     # K2.6 — native multimodal coding
    "moonshotai/Kimi-K2.7-Code",                # K2.7-Code — coding-focused (GitHub Copilot)
    "moonshotai/Kimi-VL-A3B-Thinking-2506",     # VL A3B thinking model
    "moonshotai/Moonlight-16B-A3B-Instruct",    # Moonlight 16B MoE instruct
    "moonshotai/Moonlight-16B-A3B",             # Moonlight 16B MoE base
    # === Chinese AI Labs — Alibaba (Qwen) ===
    "Qwen/Qwen3.6-35B-A3B",         # Qwen3.6 MoE 35B/3B active — agentic coding
    "Qwen/Qwen3.6-27B",             # Qwen3.6 Dense 27B
    "Qwen/Qwen3.5-397B-A17B",       # Qwen3.5 massive MoE flagship
    "Qwen/Qwen3.5-122B-A10B",       # Qwen3.5 large MoE
]


def is_new_model_update(model_id: str, last_modified: str) -> bool:
    if not HF_DB.exists():
        return True
    key = f"{model_id}#{last_modified}"
    with open(HF_DB, 'r') as f:
        keys = [line.strip() for line in f.readlines() if line.strip()]
    return key not in keys


def mark_model_processed(model_id: str, last_modified: str):
    with open(HF_DB, 'a') as f:
        f.write(f"{model_id}#{last_modified}\n")


def fetch_model_info(model_id: str) -> dict | None:
    url = f"https://huggingface.co/api/models/{model_id}"
    try:
        r = requests.get(url, timeout=15, headers={
            'User-Agent': 'LLM-Wiki-Source-Monitor/1.0',
            'Accept': 'application/json',
        })
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None


def build_model_report(model_id: str, info: dict) -> str:
    lines = [f"# Model: {model_id}", ""]
    lines.append("## Overview")
    lines.append("")
    lines.append(f"- **Model ID**: `{model_id}`")
    lines.append(f"- **Last Modified**: {info.get('lastModified', 'N/A')}")
    lines.append(f"- **Pipeline Tag**: {info.get('pipeline_tag', 'N/A')}")
    lines.append(f"- **Private**: {info.get('private', False)}")
    lines.append(f"- **Downloads**: {info.get('downloads', 'N/A')}")
    lines.append(f"- **Likes**: {info.get('likes', 'N/A')}")
    tags = info.get('tags', [])
    if tags:
        lines.append(f"- **Tags**: {', '.join(tags)}")
    lines.append("")

    card_data = info.get('cardData', {})
    if card_data:
        lines.append("## Model Card Metadata")
        lines.append("")
        for key in ['base_model', 'config', 'dataset', 'datasets',
                     'license', 'language', 'model_name', 'model_creator',
                     'model_type', 'pipeline_tag', 'quantization_config',
                     'size_categories', 'tags', 'temperature', 'tokenizer_type']:
            if key in card_data:
                val = card_data[key]
                if isinstance(val, list):
                    lines.append(f"- **{key}**: {', '.join(str(v) for v in val)}")
                elif isinstance(val, dict):
                    lines.append(f"- **{key}**: `{val}`")
                else:
                    lines.append(f"- **{key}**: `{val}`")
        lines.append("")

    siblings = info.get('siblings', [])
    if siblings:
        lines.append("## Model Files")
        lines.append("")
        lines.append("| Filename | Size |")
        lines.append("|----------|------|")
        total_size = 0
        for s in siblings:
            filename = s.get('rfilename', '')
            size = s.get('size', 0)
            total_size += size
            size_mb = f"{size / (1024**2):.1f} MB" if size else "N/A"
            lines.append(f"| `{filename}` | {size_mb} |")
        total_gb = total_size / (1024**3)
        lines.append("")
        lines.append(f"**Total size**: ~{total_gb:.1f} GB")
        lines.append("")

    lines.append("## Links")
    lines.append("")
    lines.append(f"- [HuggingFace Hub](https://huggingface.co/{model_id})")
    lines.append(f"- [API](https://huggingface.co/api/models/{model_id})")
    lines.append("")

    lines.append("## Raw API Response")
    lines.append("")
    lines.append("```json")
    import json
    key_fields = {k: v for k, v in info.items()
                  if k in ('modelId', 'lastModified', 'pipeline_tag', 'tags',
                           'downloads', 'likes', 'private', 'cardData')}
    lines.append(json.dumps(key_fields, indent=2, ensure_ascii=False))
    lines.append("```")
    lines.append("")
    return '\n'.join(lines)


def save_raw_model(model_id: str, content: str) -> str:
    model_id_short = model_id.split('/')[-1]
    slug = f"hf-{slugify(model_id_short)}"
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    filename = f"{slug}-{date_str}.md"

    filepath = RAW_DIR / filename
    frontmatter = build_frontmatter(
        source_url=f"https://huggingface.co/{model_id}",
        blog_source=f"huggingface:{model_id}",
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)

    file_content = filepath.read_text(encoding='utf-8')
    fm, body = split_frontmatter(file_content)
    if fm is not None:
        sha = compute_sha256(body)
        new_fm = fm.replace('sha256: PLACEHOLDER', f'sha256: {sha}')
        new_content = '---\n' + new_fm + '\n---\n' + body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return str(filepath.relative_to(ROOT))


# ---------------------------------------------------------------------------
# Local Files
# ---------------------------------------------------------------------------
LOCAL_DB = ROOT / ".processed" / "local_files.txt"
LOCAL_DIRS = [
    "/workspace/Projects",
    "/workspace/ai",
    "/workspace/ml",
    "/workspace/research",
    "/workspace/llm",
    "/workspace/code",
    "/workspace/src",
    "/workspace/data",
]
SKIP_SUBDIRS = {
    "wiki", "raw", "tools", ".processed", "__pycache__", ".git",
    "node_modules", "venv", ".venv", "env", "dist", "build",
    "llm-wiki",
}
SUPPORTED_EXTENSIONS = ('.md', '.txt', '.json', '.yaml', '.yml', '.py', '.js', '.ts', '.rst', '.ipynb')


def get_git_info(dirpath: Path) -> dict:
    info = {"branch": "unknown", "commit": "unknown", "remote": "unknown"}
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=str(dirpath), capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            info["branch"] = result.stdout.strip()
    except Exception:
        pass

    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=str(dirpath), capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            info["commit"] = result.stdout.strip()[:8]
    except Exception:
        pass

    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=str(dirpath), capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            remote = result.stdout.strip()
            if "github.com" in remote:
                parts = remote.split("/")
                if len(parts) >= 2:
                    repo = parts[-1].replace(".git", "")
                    owner = parts[-2]
                    info["remote"] = f"{owner}/{repo}"
            else:
                info["remote"] = remote
    except Exception:
        pass

    return info


def is_new_file(dirpath: Path, filepath: Path, db_key: str) -> bool:
    if not LOCAL_DB.exists():
        return True
    with open(LOCAL_DB, 'r') as f:
        keys = [line.strip() for line in f.readlines() if line.strip()]
    return db_key not in keys


def mark_file_read(dirpath: Path, filepath: Path, db_key: str):
    with open(LOCAL_DB, 'a') as f:
        f.write(db_key + '\n')


def save_raw_file(dirpath: Path, filepath: Path) -> str:
    rel_path = filepath.relative_to(dirpath)
    slug = slugify(str(rel_path))
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    filename = f"local-{slug}-{date_str}.md"

    filepath_out = RAW_DIR / filename
    content = filepath.read_text(encoding='utf-8', errors='replace')[:50000]

    git_info = get_git_info(dirpath)
    frontmatter = build_frontmatter(
        source_url=f"file://{filepath}",
        blog_source=f"local:{git_info['remote']}"
    )

    with open(filepath_out, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)

    # Update SHA256
    file_content = filepath_out.read_text(encoding='utf-8')
    fm, body = split_frontmatter(file_content)
    if fm is not None:
        sha = compute_sha256(body)
        new_fm = fm.replace('sha256: PLACEHOLDER', f'sha256: {sha}')
        new_content = '---\n' + new_fm + '\n---\n' + body
        with open(filepath_out, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return str(filepath_out.relative_to(ROOT))


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------
def main():
    """Combined source monitor: RSS + GitHub + Local."""
    print("🔄 LLM Wiki Source Monitor — RSS + GitHub + Local")
    print(f"📊 RSS feeds: {len(FEEDS)} | GitHub repos: {len(GITHUB_REPOS)} | Local dirs: {len(LOCAL_DIRS)}")
    print(f"📁 Raw directory: {RAW_DIR}")
    print(f"🗄️  Databases: {RSS_DB}, {GITHUB_DB}, {LOCAL_DB}")
    print()

    new_articles = []
    new_releases = []
    new_hf_models = []
    new_local_files = []
    total_rss_scanned = 0
    total_github_scanned = 0
    total_hf_scanned = 0
    total_local_scanned = 0

    # Ensure .processed directory exists
    RSS_DB.parent.mkdir(parents=True, exist_ok=True)
    GITHUB_DB.parent.mkdir(parents=True, exist_ok=True)
    HF_DB.parent.mkdir(parents=True, exist_ok=True)
    LOCAL_DB.parent.mkdir(parents=True, exist_ok=True)

    # =========================================
    # 1. RSS Feeds
    # =========================================
    print("📡 RSS Feeds:")
    for blog_name, feed_url in FEEDS.items():
        print(f"  📡 Scanning {blog_name}...")
        try:
            feed = feedparser.parse(feed_url)

            if feed.bozo:
                print(f"    ⚠️  Feed error: {feed.bozo_exception}")
                continue

            total_rss_scanned += len(feed.entries)

            for entry in feed.entries[:10]:
                url = entry.get('link', '')
                if not url or not is_new_article(url):
                    continue

                print(f"    📄 New: {entry.get('title', 'No title')}")
                content = fetch_article_content(url)
                filepath = save_raw_article(
                    title=entry.get('title', 'Untitled'),
                    url=url,
                    content=content,
                    source_blog=blog_name
                )
                new_articles.append(filepath)
                mark_article_read(url)

        except Exception as e:
            print(f"    ❌ Error scanning {blog_name}: {e}")

    # =========================================
    # 2. GitHub Releases
    # =========================================
    print("\n📡 GitHub Releases:")
    for repo in GITHUB_REPOS:
        print(f"  📡 Checking {repo}...")
        try:
            url = f"https://api.github.com/repos/{repo}/releases/latest"
            response = retry_for_status(url, _auth_headers(), status=200)

            if response.status_code != 200:
                print(f"    ⚠️  No access or not found")
                continue

            total_github_scanned += 1
            data = response.json()
            tag = data.get('tag_name', '')
            title = data.get('name', tag)

            if not tag or not is_new_release(repo, tag):
                print(f"    ✅ Already processed: {tag}")
                continue

            print(f"    📄 New release: {title} ({tag})")
            content = fetch_release_content(repo, tag)
            filepath = save_raw_release(repo, tag, content)
            new_releases.append(filepath)
            mark_release_read(repo, tag)

        except Exception as e:
            print(f"    ❌ Error checking {repo}: {e}")

    # =========================================
    # 3. HuggingFace Hub Models
    # =========================================
    print("\n🤗 HuggingFace Hub Models:")
    for model_id in HF_MODELS:
        print(f"  📡 Checking {model_id}...")
        try:
            info = fetch_model_info(model_id)
            if info is None:
                print(f"    ⚠️  Model not found or API error")
                continue

            total_hf_scanned += 1
            last_modified = info.get('lastModified', '')
            model_name = info.get('modelId', model_id)

            if not last_modified or not is_new_model_update(model_id, last_modified):
                print(f"    ✅ Up to date: {last_modified}")
                # Always include HF models in report (even if up to date)
                new_hf_models.append(f"{model_id} (up to date)")
                continue

            print(f"    📄 New update: {last_modified}")

            content = build_model_report(model_id, info)
            filepath = save_raw_model(model_id, content)
            new_hf_models.append(filepath)
            mark_model_processed(model_id, last_modified)

        except Exception as e:
            print(f"    ❌ Error checking {model_id}: {e}")

    # =========================================
    # 4. Local Files
    # =========================================
    print("\n📡 Local Files:")
    for dirpath_str in LOCAL_DIRS:
        dirpath = Path(dirpath_str)
        if not check_dir_exists(dirpath):
            print(f"  ⚠️  Directory not found: {dirpath}")
            continue

        print(f"  📡 Scanning {dirpath}...")

        try:
            for root, dirs, files in os.walk(str(dirpath)):
                # Prune unwanted directories
                dirs[:] = [d for d in dirs if d not in SKIP_SUBDIRS]

                for filename in sorted(files):
                    if not filename.endswith(SUPPORTED_EXTENSIONS):
                        continue

                    filepath = Path(root) / filename
                    rel_path = filepath.relative_to(dirpath)
                    db_key = f"{dirpath}#{rel_path}"

                    if not is_new_file(dirpath, filepath, db_key):
                        continue

                    total_local_scanned += 1
                    print(f"    📄 New: {rel_path}")

                    filepath_out = save_raw_file(dirpath, filepath)
                    new_local_files.append(filepath_out)
                    mark_file_read(dirpath, filepath, db_key)

        except Exception as e:
            print(f"    ❌ Error scanning {dirpath}: {e}")

    # =========================================
    # Summary report
    # =========================================
    total_new = len(new_articles) + len(new_releases) + len(new_hf_models) + len(new_local_files)

    report = format_report_simple(
        component="source_monitor",
        label="джерел",
        count=total_new,
        source_count=len(FEEDS) + len(GITHUB_REPOS) + len(HF_MODELS) + len(LOCAL_DIRS),
        has_new=total_new > 0,
        details=None,
    )

    # Add per-source breakdown
    breakdown_lines = []
    if new_articles:
        breakdown_lines.append(f"  📰 RSS: {len(new_articles)}")
        breakdown_lines.extend([f"    - {a}" for a in new_articles])
    if new_releases:
        breakdown_lines.append(f"  🐙 GitHub: {len(new_releases)}")
        breakdown_lines.extend([f"    - {r}" for r in new_releases])
    if new_hf_models:
        breakdown_lines.append(f"  🤗 HF Hub: {len(new_hf_models)}")
        breakdown_lines.extend([f"    - {m}" for m in new_hf_models])
    if new_local_files:
        breakdown_lines.append(f"  📁 Local: {len(new_local_files)}")
        breakdown_lines.extend([f"    - {f}" for f in new_local_files])

    if breakdown_lines:
        report += "\n\nДеталі:\n" + "\n".join(breakdown_lines)

    print()
    print(report)

    # Log
    if total_new > 0:
        all_new = new_articles + new_releases + new_hf_models + new_local_files
        append_to_log(LOG_FILE, "source_monitor",
                      f"RSS: {total_rss_scanned}, GH: {total_github_scanned}, HF: {total_hf_scanned}, Local: {total_local_scanned} | "
                      f"new: {total_new} ({len(new_articles)} articles, {len(new_releases)} releases, {len(new_hf_models)} HF, {len(new_local_files)} local)")
        print(f"  📝 Logged to {LOG_FILE}")
    else:
        append_to_log(LOG_FILE, "source_monitor",
                      f"RSS: {total_rss_scanned}, GH: {total_github_scanned}, HF: {total_hf_scanned}, Local: {total_local_scanned} | no new sources")
        print(f"  ✅ No new sources to ingest")

    return 0  # Always return 0 for cron


if __name__ == '__main__':
    sys.exit(main())
