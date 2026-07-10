#!/usr/bin/env python3
"""RSS Feed Monitor for LLM Wiki - Phase 1: Autonomous Source Collection"""
import feedparser
import requests
import hashlib
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw" / "articles"
LOG_FILE = ROOT / "log.md"
DB_FILE = ROOT / ".processed" / "rss_urls.txt"

# RSS Feeds to monitor - AI/LLM focused
FEEDS = {
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
}

def compute_sha256(content: str) -> str:
    """Compute SHA256 of content body."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def is_new_article(url: str) -> bool:
    """Check if article URL is not in database."""
    if not DB_FILE.exists():
        return True
    with open(DB_FILE, 'r') as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]
    return url not in urls

def mark_article_read(url: str):
    """Mark article as processed."""
    with open(DB_FILE, 'a') as f:
        f.write(url + '\n')

def save_raw_article(title: str, url: str, content: str, source_blog: str) -> str:
    """Save article as raw source file."""
    # Generate filename
    slug = title.lower().replace(' ', '-').replace('.', '').replace(',', '').replace(':', '').replace('—', '-')
    # Remove special characters
    slug = ''.join(c for c in slug if c.isalnum() or c in '-_')
    slug = slug[:100]  # Limit length
    
    filename = f"{slug}-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.md"
    filepath = RAW_DIR / filename
    
    # Create frontmatter
    frontmatter = f"""---
source_url: {url}
ingested: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
sha256: PLACEHOLDER
blog_source: {source_blog}
---
"""
    
    # Write file
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

def fetch_article_content(url: str) -> str:
    """Fetch article content from URL."""
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'LLM-Wiki-RSS-Monitor/1.0'})
        response.raise_for_status()
        return response.text[:50000]  # Limit content size
    except Exception as e:
        return f"Error fetching content: {e}"

def append_to_log(entry: str):
    """Append entry to log.md."""
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n## [{timestamp}] rss_monitor | {entry}\n")

def main():
    """Main RSS monitoring function."""
    print("🔄 LLM Wiki RSS Monitor - Starting...")
    print(f"📊 Monitoring {len(FEEDS)} feeds")
    print(f"📁 Raw directory: {RAW_DIR}")
    print(f"🗄️  Database: {DB_FILE}")
    print()
    
    new_articles = []
    total_scanned = 0
    
    # Ensure .processed directory exists
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    for blog_name, feed_url in FEEDS.items():
        print(f"📡 Scanning {blog_name}...")
        try:
            feed = feedparser.parse(feed_url)
            
            if feed.bozo:
                print(f"  ⚠️  Feed error: {feed.bozo_exception}")
                continue
            
            total_scanned += len(feed.entries)
            
            for entry in feed.entries[:10]:  # Check first 10 entries per feed
                url = entry.get('link', '')
                
                if not url or not is_new_article(url):
                    continue
                
                print(f"  📄 New: {entry.get('title', 'No title')}")
                
                # Fetch content
                content = fetch_article_content(url)
                
                # Save raw article
                filepath = save_raw_article(
                    title=entry.get('title', 'Untitled'),
                    url=url,
                    content=content,
                    source_blog=blog_name
                )
                
                new_articles.append(filepath)
                mark_article_read(url)
                
        except Exception as e:
            print(f"  ❌ Error scanning {blog_name}: {e}")
    
    # Status line
    if new_articles:
        print(f"Статус: [ACTIVE] — сканування {len(FEEDS)} feedів, знайдено {len(new_articles)} нових статей")
    else:
        print(f"Статус: [SILENT] — немає нових даних для інгесту")

    # Summary
    print()
    print(f"📊 Scan complete:")
    print(f"  📈 Total articles scanned: {total_scanned}")
    print(f"  🆕 New articles ingested: {len(new_articles)}")

    if new_articles:
        append_to_log(f"Scanned {total_scanned} articles, ingested {len(new_articles)} new sources: {', '.join(new_articles)}")
        print(f"  📝 Logged to {LOG_FILE}")
    else:
        append_to_log(f"Scanned {total_scanned} articles, no new sources found")
        print(f"  ✅ No new articles to ingest")
    
    return 0  # Always return 0 for cron — no new articles is not an error

if __name__ == '__main__':
    sys.exit(main())
