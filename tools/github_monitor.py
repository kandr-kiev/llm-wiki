#!/usr/bin/env python3
"""GitHub Repository Monitor for LLM Wiki - Monitors issues, PRs, and changes"""
import requests
import os
import sys
from pathlib import Path
from datetime import datetime, timezone

import os

from tools.utils import (
    compute_sha256,
    append_to_log,
    slugify,
    build_frontmatter,
    print_status,
    check_dir_exists,
    retry_for_status,
)

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
DB_FILE = ROOT / ".processed" / "github_issues.txt"

# GitHub repos to monitor for issues/PRs
REPOS = [
    "openai/whisper",
    "openai/gpt-2",
    "openai/openai-cookbook",
    "huggingface/transformers",
    "huggingface/diffusers",
    "huggingface/peft",
    "huggingface/trl",
    "meta-llama/llama",
    "mistralai/mistral-src",
    "google-deepmind/gemma",
    "facebookresearch/llama-recipes",
    "microsoft/DeepSpeed",
    "pytorch/pytorch",
    "tensorflow/tensorflow",
    "langchain-ai/langchain",
    "microsoft/autogen",
    "google-research/google-research",
]


def is_new_issue(repo: str, issue_number: str) -> bool:
    """Check if issue/PR is not in database."""
    if not DB_FILE.exists():
        return True
    key = f"{repo}#{issue_number}"
    with open(DB_FILE, 'r') as f:
        keys = [line.strip() for line in f.readlines() if line.strip()]
    return key not in keys


def mark_issue_read(repo: str, issue_number: str):
    """Mark issue/PR as processed."""
    with open(DB_FILE, 'a') as f:
        f.write(f"{repo}#{issue_number}\n")


def fetch_issue_content(repo: str, issue_number: str, issue_type: str = "issue") -> str:
    """Fetch issue/PR content from GitHub API."""
    try:
        url = f"https://api.github.com/repos/{repo}/{issue_type}s/{issue_number}"
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'LLM-Wiki-GitHub-Monitor/1.0',
            'Accept': 'application/vnd.github.v3+json'
        })
        response.raise_for_status()
        data = response.json()
        
        title = data.get('title', 'No title')
        body = data.get('body', 'No body')
        state = data.get('state', 'unknown')
        author = data.get('user', {}).get('login', 'unknown')
        created = data.get('created_at', 'unknown')
        
        return f"# {issue_type.title()} #{issue_number}: {title}\n\n" \
               f"**State:** {state} | **Author:** {author} | **Created:** {created}\n\n" \
               f"{body}"
    except Exception as e:
        return f"Error fetching {issue_type}: {e}"


def save_raw_issue(repo: str, issue_number: str, content: str, issue_type: str = "issue") -> str:
    """Save issue/PR as raw source file using canonical utils."""
    slug = f"gh-{slugify(repo)}-{issue_type}-{issue_number}"
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    filename = f"{slug}-{date_str}.md"
    
    filepath = RAW_DIR / filename
    
    # Build frontmatter
    frontmatter = build_frontmatter(
        source_url=f"https://github.com/{repo}/{issue_type}s/{issue_number}",
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
        new_fm = fm.replace('sha256: PLACEHOLDER', f'sha256: {sha}')
        new_content = '---\n' + new_fm + '\n---\n' + body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    return str(filepath.relative_to(ROOT))


def main():
    """Main GitHub issue/PR monitoring function."""
    print("🔄 LLM Wiki GitHub Monitor - Starting...")
    print(f"📊 Monitoring {len(REPOS)} repositories")
    print(f"📁 Raw directory: {RAW_DIR}")
    print(f"🗄️  Database: {DB_FILE}")
    print()
    
    new_items = []
    total_scanned = 0
    
    # Ensure .processed directory exists
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    for repo in REPOS:
        print(f"📡 Checking {repo}...")
        try:
            # Check issues
            issues_url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=5"
            issues_response = retry_for_status(issues_url, _auth_headers(), status=200)
            
            if issues_response.status_code != 200:
                print(f"  ⚠️  No access")
                continue
            
            total_scanned += 1
            issues = issues_response.json()
            
            for issue in issues:
                issue_number = str(issue.get('number', ''))
                title = issue.get('title', 'No title')
                
                if not issue_number or not is_new_issue(repo, issue_number):
                    continue
                
                print(f"  📄 New issue: {title} (#{issue_number})")
                
                content = fetch_issue_content(repo, issue_number, "issue")
                filepath = save_raw_issue(repo, issue_number, content, "issue")
                
                new_items.append(filepath)
                mark_issue_read(repo, issue_number)
            
        except Exception as e:
            print(f"  ❌ Error checking {repo}: {e}")
    
    # Status line — canonical format
    print_status(has_new=len(new_items) > 0, label="репозиторіїв", count=len(new_items), source_count=len(REPOS))

    # Summary
    print()
    print(f"📊 Scan complete:")
    print(f"  📈 Total repositories scanned: {total_scanned}")
    print(f"  🆕 New issues/PRs ingested: {len(new_items)}")

    if new_items:
        append_to_log(LOG_FILE, "github_monitor", f"Scanned {total_scanned} repos, ingested {len(new_items)} new issues: {', '.join(new_items)}")
        print(f"  📝 Logged to {LOG_FILE}")
    else:
        append_to_log(LOG_FILE, "github_monitor", f"Scanned {total_scanned} repos, no new issues found")
        print(f"  ✅ No new issues to ingest")
    
    return 0  # Always return 0 for cron


if __name__ == '__main__':
    sys.exit(main())
