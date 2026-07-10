#!/usr/bin/env python3
"""GitHub Release Monitor for LLM Wiki - Monitors GitHub releases for new AI/LLM tools."""
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw" / "articles"
LOG_FILE = ROOT / "log.md"
DB_FILE = ROOT / ".processed" / "github_releases.txt"

# GitHub repositories to monitor
REPOS = {
    "OpenAI": "openai/openai-cookbook",
    "Anthropic": "anthropics/anthropic-cookbook",
    "LangChain": "langchain-ai/langchain",
    "LlamaIndex": "run-llama/llama_index",
    "Hugging Face": "huggingface/transformers",
    "PyTorch": "pytorch/pytorch",
    "TensorFlow": "tensorflow/tensorflow",
    "MLflow": "mlflow/mlflow",
    "Weights & Biases": "wandb/wandb",
    "vLLM": "vllm-project/vllm",
}

def compute_sha256(content: str) -> str:
    """Compute SHA256 of content body."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def is_new_release(repo: str, tag: str) -> bool:
    """Check if release is not in database."""
    if not DB_FILE.exists():
        return True
    with open(DB_FILE, 'r') as f:
        releases = [line.strip() for line in f.readlines() if line.strip()]
    return f"{repo}:{tag}" not in releases

def mark_release_processed(repo: str, tag: str):
    """Mark release as processed."""
    with open(DB_FILE, 'a') as f:
        f.write(f"{repo}:{tag}\n")

def save_raw_release(title: str, url: str, content: str, source_repo: str) -> str:
    """Save release as raw source file."""
    slug = title.lower().replace(' ', '-').replace('.', '').replace(',', '').replace(':', '').replace('—', '-')
    slug = ''.join(c for c in slug if c.isalnum() or c in '-_')
    slug = slug[:100]
    
    filename = f"{slug}-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.md"
    filepath = RAW_DIR / filename
    
    frontmatter = f"""---
source_url: {url}
ingested: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
sha256: PLACEHOLDER
blog_source: github
---
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)
    
    # Update SHA256
    with open(filepath, 'r') as f:
        file_content = f.read()
    
    parts = file_content.split('---', 2)
    if len(parts) >= 3:
        body = parts[2]
        sha = compute_sha256(body)
        file_content = parts[0] + '---\n' + parts[1] + '---\n' + parts[2].replace('PLACEHOLDER', sha)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(file_content)
    
    return str(filepath.relative_to(ROOT))

def fetch_release_info(repo: str) -> list:
    """Fetch releases from GitHub API."""
    import requests
    url = f"https://api.github.com/repos/{repo}/releases"
    try:
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'LLM-Wiki-GitHub-Monitor/1.0',
            'Accept': 'application/vnd.github.v3+json'
        })
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return []

def append_to_log(entry: str):
    """Append entry to log.md."""
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n## [{timestamp}] github_release_monitor | {entry}\n")

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
    
    for repo_name, repo_path in REPOS.items():
        print(f"📡 Scanning {repo_name} ({repo_path})...")
        releases = fetch_release_info(repo_path)
        
        if not releases:
            print(f"  ⚠️  No releases found or API error")
            continue
        
        for release in releases[:5]:  # Check last 5 releases
            tag = release.get('tag_name', '')
            title = release.get('name', release.get('tag_name', 'Untitled'))
            url = release.get('html_url', '')
            body = release.get('body', '')
            
            total_scanned += 1
            
            if not is_new_release(repo_name, tag):
                continue
            
            print(f"  🆕 New: {title} ({tag})")
            
            content = f"# {title}\n\n## Release Notes\n\n{body}\n\n## Download\n\n{url}"
            
            filepath = save_raw_release(
                title=title,
                url=url,
                content=content,
                source_repo=repo_path
            )
            
            new_releases.append(filepath)
            mark_release_processed(repo_name, tag)
    
    # Status line
    if new_releases:
        print(f"Статус: [ACTIVE] — моніторинг {len(REPOS)} репозиторіїв, знайдено {len(new_releases)} нових релізів")
    else:
        print(f"Статус: [SILENT] — немає нових даних для інгесту")

    # Summary
    print()
    print(f"📊 Scan complete:")
    print(f"  📈 Total releases scanned: {total_scanned}")
    print(f"  🆕 New releases ingested: {len(new_releases)}")

    if new_releases:
        append_to_log(f"Scanned {total_scanned} releases, ingested {len(new_releases)} new sources: {', '.join(new_releases)}")
        print(f"  📝 Logged to {LOG_FILE}")
    else:
        append_to_log(f"Scanned {total_scanned} releases, no new releases found")
        print(f"  ✅ No new releases to ingest")
    
    return 0 if new_releases else 1

if __name__ == '__main__':
    sys.exit(main())
