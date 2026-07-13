#!/usr/bin/env python3
"""GitHub Release Monitor for LLM Wiki - Monitors releases from AI/ML repositories"""
import requests
import os
import sys
from pathlib import Path
from datetime import datetime, timezone

import os

from utils import (
    compute_sha256,
    append_to_log,
    slugify,
    build_frontmatter,
    print_status,
    check_dir_exists,
    split_frontmatter,
    retry_for_status,
)
from standard_report import format_report_simple

# GitHub token for authenticated API access
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')

def _auth_headers():
    """Return headers with optional auth token."""
    headers = {
        'User-Agent': 'LLM-Wiki-GitHub-Monitor/1.0',
        'Accept': 'application/vnd.github.v3+json',
    }
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'
    return headers

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw" / "articles"
LOG_FILE = ROOT / "log.md"
DB_FILE = ROOT / ".processed" / "github_releases.txt"

# GitHub repos to monitor - AI/ML focused
REPOS = [
    "openai/whisper",
    "google-deepmind/gemma",
    "google-deepmind/alphafold",
    "meta-llama/llama3",
    "meta-llama/llama-models",
    "mistralai/mistral-src",
    "mistralai/mistral.rs",
    "microsoft/DeepSpeed",
    "microsoft/DeepSpeedExamples",
    "huggingface/transformers",
    "huggingface/diffusers",
    "huggingface/text-generation-inference",
    "huggingface/optimum",
    "huggingface/accelerate",
    "huggingface/peft",
    "huggingface/bitsandbytes",
    "huggingface/trl",
    "huggingface/alignment-handbook",
    "huggingface/axolotl",
    "facebookresearch/llama-recipes",
    "facebookresearch/parlai",
    "facebookresearch/faiss",
    "facebookresearch/detectron2",
    "google-research/google-research",
    "unslothai/unsloth",
    "google-research/re2",
]


def is_new_release(repo: str, release_tag: str) -> bool:
    """Check if release is not in database."""
    if not DB_FILE.exists():
        return True
    key = f"{repo}#{release_tag}"
    with open(DB_FILE, 'r') as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]
    return key not in urls


def mark_release_read(repo: str, release_tag: str):
    """Mark release as processed."""
    with open(DB_FILE, 'a') as f:
        f.write(f"{repo}#{release_tag}\n")


def fetch_release_content(repo: str, release_tag: str) -> str:
    """Fetch release content from GitHub API."""
    try:
        url = f"https://api.github.com/repos/{repo}/releases/tags/{release_tag}"
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'LLM-Wiki-GitHub-Monitor/1.0',
            'Accept': 'application/vnd.github.v3+json'
        })
        response.raise_for_status()
        data = response.json()
        body = data.get('body', 'No body')
        return f"# Release {release_tag}\n\n{body}"
    except Exception as e:
        return f"Error fetching release: {e}"


def save_raw_release(repo: str, release_tag: str, content: str) -> str:
    """Save release as raw source file using canonical utils."""
    slug = f"gh-{slugify(release_tag)}"
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    filename = f"{slug}-{date_str}.md"
    
    filepath = RAW_DIR / filename
    
    # Build frontmatter
    frontmatter = build_frontmatter(
        source_url=f"https://github.com/{repo}/releases/tag/{release_tag}",
        blog_source=f"github:{repo}"
    )
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)
    
    # Update SHA256 — canonical: no .strip()
    with open(filepath, 'r') as f:
        file_content = f.read()
    
    fm, body = split_frontmatter(file_content)
    if fm is not None:
        sha = compute_sha256(body)
        fm = fm.replace('sha256: PLACEHOLDER', f'sha256: {sha}')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('---\n' + fm + '\n---\n' + body)
    
    return str(filepath.relative_to(ROOT))


def main():
    """Main GitHub release monitoring function."""
    print("🔄 LLM Wiki GitHub Release Monitor - Starting...")
    print(f"📊 Monitoring {len(REPOS)} repositories")
    print(f"📁 Raw directory: {RAW_DIR}")
    print(f"🗄️  Database: {DB_FILE}")
    print()
    
    new_releases = []
    total_scanned = 0
    
    # Ensure .processed directory exists
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    for repo in REPOS:
        print(f"📡 Checking {repo}...")
        try:
            # Get latest release
            url = f"https://api.github.com/repos/{repo}/releases/latest"
            response = retry_for_status(url, _auth_headers(), status=200)
            
            if response.status_code != 200:
                print(f"  ⚠️  No access or not found")
                continue
            
            total_scanned += 1
            data = response.json()
            tag = data.get('tag_name', '')
            title = data.get('name', tag)
            
            if not tag or not is_new_release(repo, tag):
                print(f"  ✅ Already processed: {tag}")
                continue
            
            print(f"  📄 New release: {title} ({tag})")
            
            # Fetch content
            content = fetch_release_content(repo, tag)
            
            # Save raw release
            filepath = save_raw_release(repo, tag, content)
            
            new_releases.append(filepath)
            mark_release_read(repo, tag)
            
        except Exception as e:
            print(f"  ❌ Error checking {repo}: {e}")
    
    # Generate standardized report
    report = format_report_simple(
        component="github_release_monitor",
        label="репозиторіїв",
        count=len(new_releases),
        source_count=len(REPOS),
        has_new=len(new_releases) > 0,
        details=[f"  - {r}" for r in new_releases] if new_releases else None,
    )
    
    # Summary
    print()
    print(report)

    if new_releases:
        append_to_log(LOG_FILE, "github_release_monitor", f"Scanned {total_scanned} repos, ingested {len(new_releases)} new releases: {', '.join(new_releases)}")
        print(f"  📝 Logged to {LOG_FILE}")
    else:
        append_to_log(LOG_FILE, "github_release_monitor", f"Scanned {total_scanned} repos, no new releases found")
        print(f"  ✅ No new releases to ingest")
    
    return 0  # Always return 0 for cron


if __name__ == '__main__':
    sys.exit(main())
