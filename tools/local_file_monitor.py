#!/usr/bin/env python3
"""Local File Monitor for LLM Wiki - Monitors local directories for new articles."""
import hashlib
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw" / "articles"
LOG_FILE = ROOT / "log.md"
DB_FILE = ROOT / ".processed" / "local_files.txt"

# Directories to monitor
WATCH_DIRS = {
    "Projects": Path("/workspace/Projects"),
}

def compute_sha256(content: str) -> str:
    """Compute SHA256 of content body."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def is_new_file(filepath: Path) -> bool:
    """Check if file is not in database."""
    if not DB_FILE.exists():
        return True
    with open(DB_FILE, 'r') as f:
        files = [line.strip() for line in f.readlines() if line.strip()]
    return str(filepath.absolute()) not in files

def mark_file_processed(filepath: Path):
    """Mark file as processed."""
    with open(DB_FILE, 'a') as f:
        f.write(str(filepath.absolute()) + '\n')

def save_raw_article(title: str, url: str, content: str, source_file: str) -> str:
    """Save article as raw source file."""
    slug = title.lower().replace(' ', '-').replace('.', '').replace(',', '').replace(':', '').replace('—', '-')
    slug = ''.join(c for c in slug if c.isalnum() or c in '-_')
    slug = slug[:100]
    
    filename = f"{slug}-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.md"
    filepath = RAW_DIR / filename
    
    frontmatter = f"""---
source_url: {url}
ingested: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
sha256: PLACEHOLDER
blog_source: local
---
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)
    
    # Update SHA256 — use split_frontmatter logic (same as wiki_lint.py)
    with open(filepath, 'r') as f:
        file_content = f.read()
    
    # Find frontmatter boundaries: starts with '---\n', ends with '\n---\n'
    start = file_content.index('---\n') + 4
    end = file_content.index('\n---\n', start)
    body = file_content[end+5:]
    sha = compute_sha256(body)
    file_content = file_content[:end] + '\n' + body.replace('PLACEHOLDER', sha) + '\n'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_content)
    
    return str(filepath.relative_to(ROOT))

def read_text_file(filepath: Path) -> str:
    """Read text content from file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def append_to_log(entry: str):
    """Append entry to log.md."""
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n## [{timestamp}] local_file_monitor | {entry}\n")

def main():
    """Main local file monitoring function."""
    print("🔄 LLM Wiki Local File Monitor - Starting...")
    print(f"📁 Raw directory: {RAW_DIR}")
    print(f"🗄️  Database: {DB_FILE}")
    print()
    
    new_articles = []
    total_scanned = 0
    
    # Ensure .processed directory exists
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    for dir_name, dir_path in WATCH_DIRS.items():
        if not dir_path.exists():
            print(f"⚠️  {dir_name} directory not found: {dir_path}")
            continue
        
        print(f"📂 Scanning {dir_name}...")
        for md_file in dir_path.rglob('*.md'):
            total_scanned += 1
            
            if not is_new_file(md_file):
                continue
            
            print(f"  📄 New: {md_file.name}")
            
            content = read_text_file(md_file)
            if len(content) < 100:
                print(f"    ⚠️  Skipping: too short ({len(content)} chars)")
                continue
            
            filepath = save_raw_article(
                title=md_file.stem,
                url=f"local://{md_file.absolute()}",
                content=content,
                source_file=str(md_file.relative_to(Path.home()))
            )
            
            new_articles.append(filepath)
            mark_file_processed(md_file)
    
    # Status line
    if new_articles:
        print(f"Статус: [ACTIVE] — сканування {len(WATCH_DIRS)} каталогів, знайдено {len(new_articles)} нових файлів")
    else:
        print(f"Статус: [SILENT] — немає нових даних для інгесту")

    # Summary
    print()
    print(f"📊 Scan complete:")
    print(f"  📈 Total files scanned: {total_scanned}")
    print(f"  🆕 New files ingested: {len(new_articles)}")

    if new_articles:
        append_to_log(f"Scanned {total_scanned} files, ingested {len(new_articles)} new sources: {', '.join(new_articles)}")
        print(f"  📝 Logged to {LOG_FILE}")
    else:
        append_to_log(f"Scanned {total_scanned} files, no new sources found")
        print(f"  ✅ No new files to ingest")
    
    return 0 if new_articles else 1

if __name__ == '__main__':
    sys.exit(main())
