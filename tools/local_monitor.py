#!/usr/bin/env python3
"""Local File Monitor for LLM Wiki - Phase 1"""
import hashlib
import sys
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw" / "articles"
LOG_FILE = ROOT / "log.md"
DB_FILE = ROOT / ".processed" / "local_hashes.txt"

# Directories to monitor
MONITORED_DIRS = [
    ROOT / "workspace",  # User's workspace
    Path("/workspace/projects"),  # Projects directory
]

def compute_sha256(path: Path) -> str:
    """Compute SHA256 of file content."""
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def is_new_file(filepath: Path) -> bool:
    """Check if file is not in database."""
    if not DB_FILE.exists():
        return True
    with open(DB_FILE, 'r') as f:
        hashes = [line.strip() for line in f.readlines() if line.strip()]
    try:
        file_hash = compute_sha256(filepath)
        return file_hash not in hashes
    except Exception:
        return False

def mark_file_processed(filepath: Path):
    """Mark file as processed."""
    with open(DB_FILE, 'a') as f:
        file_hash = compute_sha256(filepath)
        f.write(file_hash + '\n')

def save_local_file(filepath: Path) -> str:
    """Save local file as raw source."""
    filename = filepath.name
    # Avoid duplicates
    if (RAW_DIR / filename).exists():
        return None
    
    # Copy to raw directory
    dest = RAW_DIR / filename
    dest.write_bytes(filepath.read_bytes())
    
    # Add frontmatter if markdown
    if filename.endswith('.md'):
        with open(dest, 'r') as f:
            content = f.read()
        
        if not content.startswith('---'):
            frontmatter = f"""---
source_type: local_file
local_path: {filepath}
ingested: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
sha256: PLACEHOLDER
---
"""
            with open(dest, 'w') as f:
                f.write(frontmatter + content)
            
            # Update SHA256
            parts = content.split('---', 2)
            if len(parts) >= 3:
                body = parts[2]
                sha = hashlib.sha256(body.encode('utf-8')).hexdigest()
                file_content = parts[0] + '---\n' + parts[1] + '---\n' + parts[2].replace('PLACEHOLDER', sha)
                with open(dest, 'w') as f:
                    f.write(file_content)
    
    return str(dest.relative_to(ROOT))

def append_to_log(entry: str):
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n## [{timestamp}] local_monitor | {entry}\n")

def main():
    print("🔄 LLM Wiki Local File Monitor - Starting...")
    print(f"📁 Raw directory: {RAW_DIR}")
    print(f"🗄️  Database: {DB_FILE}")
    print()
    
    new_files = []
    
    for dirpath in MONITORED_DIRS:
        if not dirpath.exists():
            print(f"⏭️  Directory not found: {dirpath}")
            continue
        
        print(f"📂 Scanning {dirpath}...")
        
        for root, dirs, files in os.walk(dirpath):
            for filename in files:
                if not filename.endswith(('.md', '.txt', '.json', '.yaml', '.yml', '.py', '.js', '.ts')):
                    continue
                
                filepath = Path(root) / filename
                
                if is_new_file(filepath):
                    print(f"  📄 New: {filepath}")
                    result = save_local_file(filepath)
                    if result:
                        new_files.append(result)
                        mark_file_processed(filepath)
                    else:
                        mark_file_processed(filepath)  # Skip duplicates
    
    print()
    print(f"📊 Monitor complete:")
    print(f"  🆕 New files ingested: {len(new_files)}")
    
    if new_files:
        append_to_log(f"Found {len(new_files)} new local files: {', '.join(new_files)}")
        print(f"  📝 Logged")
    else:
        append_to_log("Checked local directories, no new files")
        print(f"  ✅ No new files")
    
    return 0 if new_files else 1

if __name__ == '__main__':
    sys.exit(main())
