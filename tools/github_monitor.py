#!/usr/bin/env python3
"""GitHub Repository Monitor for LLM Wiki - Phase 1"""
import requests
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw" / "articles"
LOG_FILE = ROOT / "log.md"
DB_FILE = ROOT / ".processed" / "github_tags.txt"

# Repositories to monitor - AI/LLM focused
REPOS = {
    "Hugging Face Transformers": "https://api.github.com/repos/huggingface/transformers",
    "PyTorch": "https://api.github.com/repos/pytorch/pytorch",
    "LangChain": "https://api.github.com/repos/langchain-ai/langchain",
    "vLLM": "https://api.github.com/repos/vllm-project/vllm",
    "Ollama": "https://api.github.com/repos/ollama/ollama",
    "Llama.cpp": "https://api.github.com/repos/ggerganov/llama.cpp",
    "Cloudflare Workers AI": "https://api.github.com/repos/cloudflare/workers-ai",
    "OpenAI Python": "https://api.github.com/repos/openai/openai-python",
    "Anthropic SDK": "https://api.github.com/repos/anthropics/anthropic-sdk-python",
}

def compute_sha256(content: str) -> str:
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def is_new_release(tag: str) -> bool:
    if not DB_FILE.exists():
        return True
    with open(DB_FILE, 'r') as f:
        tags = [line.strip() for line in f.readlines() if line.strip()]
    return tag not in tags

def mark_release(tag: str):
    with open(DB_FILE, 'a') as f:
        f.write(tag + '\n')

def save_release_info(repo_name: str, tag: str, url: str, body: str) -> str:
    slug = repo_name.lower().replace(' ', '-').replace('.', '').replace('/', '-')
    slug = ''.join(c for c in slug if c.isalnum() or c in '-_')
    
    filename = f"gh-{slug}-release-{tag}-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.md"
    filepath = RAW_DIR / filename
    
    content = f"""# Release Notes: {repo_name} v{tag}

**Source:** {url}
**Published:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}
**Type:** Release notes / changelog

---

## What's New

{body}

---

*Auto-collected by LLM Wiki GitHub Monitor*
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return str(filepath.relative_to(ROOT))

def append_to_log(entry: str):
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n## [{timestamp}] github_monitor | {entry}\n")

def main():
    print("🔄 LLM Wiki GitHub Monitor - Starting...")
    print(f"📊 Monitoring {len(REPOS)} repositories")
    print()
    
    new_releases = []
    
    for repo_name, api_url in REPOS.items():
        print(f"📦 Checking {repo_name}...")
        try:
            response = requests.get(api_url, timeout=10, headers={
                'Accept': 'application/vnd.github.v3+json',
                'User-Agent': 'LLM-Wiki-GitHub-Monitor/1.0'
            })
            response.raise_for_status()
            data = response.json()
            
            # Get latest release
            releases_url = data.get('releases_url', '').replace('{/tag_name}', '')
            releases_response = requests.get(releases_url, timeout=10, headers={
                'Accept': 'application/vnd.github.v3+json',
                'User-Agent': 'LLM-Wiki-GitHub-Monitor/1.0'
            })
            releases_response.raise_for_status()
            releases = releases_response.json()
            
            if not releases:
                print(f"  ⚠️  No releases found")
                continue
            
            latest = releases[0]
            tag = latest.get('tag_name', '')
            url = latest.get('html_url', '')
            body = latest.get('body', 'No release notes')
            
            print(f"  🆕 Latest: {tag}")
            
            if is_new_release(tag):
                print(f"  ✅ New release!")
                filepath = save_release_info(repo_name, tag, url, body)
                new_releases.append(filepath)
                mark_release(tag)
            else:
                print(f"  ⏭️  Already processed")
                
        except Exception as e:
            print(f"  ❌ Error: {e}")
    
    print()
    print(f"📊 Monitor complete:")
    print(f"  🆕 New releases: {len(new_releases)}")
    
    if new_releases:
        append_to_log(f"Found {len(new_releases)} new releases: {', '.join(new_releases)}")
        print(f"  📝 Logged")
    else:
        append_to_log("Checked all repos, no new releases")
        print(f"  ✅ No new releases")
    
    return 0 if new_releases else 1

if __name__ == '__main__':
    sys.exit(main())
