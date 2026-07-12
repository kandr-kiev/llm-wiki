#!/usr/bin/env python3
"""Local File Monitor for LLM Wiki - Monitors local AI/ML repositories"""
import os
import sys
import hashlib
import subprocess
from pathlib import Path
from datetime import datetime, timezone

from utils import (
    compute_sha256,
    append_to_log,
    slugify,
    build_frontmatter,
    print_status,
    check_dir_exists,
    split_frontmatter,
)
from standard_report import format_report_simple

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw" / "articles"
LOG_FILE = ROOT / "log.md"
DB_FILE = ROOT / ".processed" / "local_files.txt"

# Local directories to monitor
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


def get_git_info(dirpath: Path) -> dict:
    """Get git info for a directory."""
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
            # Extract owner/repo from URL
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
    """Check if file is not in database."""
    if not DB_FILE.exists():
        return True
    with open(DB_FILE, 'r') as f:
        keys = [line.strip() for line in f.readlines() if line.strip()]
    return db_key not in keys


def mark_file_read(dirpath: Path, filepath: Path, db_key: str):
    """Mark file as processed."""
    with open(DB_FILE, 'a') as f:
        f.write(db_key + '\n')


def save_raw_file(dirpath: Path, filepath: Path) -> str:
    """Save local file as raw source using canonical utils."""
    # Get relative path from monitored directory
    rel_path = filepath.relative_to(dirpath)
    slug = slugify(str(rel_path))
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    filename = f"local-{slug}-{date_str}.md"
    
    filepath_out = RAW_DIR / filename
    
    # Read content
    content = filepath.read_text(encoding='utf-8', errors='replace')[:50000]
    
    # Get git info
    git_info = get_git_info(dirpath)
    
    # Build frontmatter
    frontmatter = build_frontmatter(
        source_url=f"file://{filepath}",
        blog_source=f"local:{git_info['remote']}"
    )
    
    # Write file
    with open(filepath_out, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)
    
    # Update SHA256 — canonical: no .strip()
    with open(filepath_out, 'r') as f:
        file_content = f.read()
    
    fm, body = split_frontmatter(file_content)
    if fm is not None:
        sha = compute_sha256(body)
        new_fm = fm.replace('sha256: PLACEHOLDER', f'sha256: {sha}')
        new_content = '---\n' + new_fm + '\n---\n' + body
        with open(filepath_out, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    return str(filepath_out.relative_to(ROOT))


def main():
    """Main local file monitoring function."""
    print("🔄 LLM Wiki Local File Monitor - Starting...")
    print(f"📁 Monitoring {len(LOCAL_DIRS)} directories")
    print(f"📁 Raw directory: {RAW_DIR}")
    print(f"🗄️  Database: {DB_FILE}")
    print()
    
    new_files = []
    total_scanned = 0
    
    # Ensure .processed directory exists
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    for dirpath in LOCAL_DIRS:
        dirpath = Path(dirpath)
        if not check_dir_exists(dirpath):
            print(f"⚠️  Directory not found: {dirpath}")
            continue
        
        print(f"📡 Scanning {dirpath}...")
        
        try:
            for root, dirs, files in os.walk(str(dirpath)):
                for filename in files[:50]:  # Limit files per directory
                    if not filename.endswith(('.py', '.md', '.txt', '.json', '.yaml', '.yml', '.rst', '.ipynb')):
                        continue
                    
                    filepath = Path(root) / filename
                    rel_path = filepath.relative_to(dirpath)
                    db_key = f"{dirpath}#{rel_path}"
                    
                    if not is_new_file(dirpath, filepath, db_key):
                        continue
                    
                    total_scanned += 1
                    print(f"  📄 New: {rel_path}")
                    
                    filepath_out = save_raw_file(dirpath, filepath)
                    new_files.append(filepath_out)
                    mark_file_read(dirpath, filepath, db_key)
                    
        except Exception as e:
            print(f"  ❌ Error scanning {dirpath}: {e}")
    
    # Generate standardized report
    report = format_report_simple(
        component="local_file_monitor",
        label="каталогів",
        count=len(new_files),
        source_count=len(LOCAL_DIRS),
        has_new=len(new_files) > 0,
        details=[f"  - {f}" for f in new_files] if new_files else None,
    )
    
    # Summary
    print()
    print(report)

    if new_files:
        append_to_log(LOG_FILE, "local_file_monitor", f"Scanned {total_scanned} files, ingested {len(new_files)} new sources: {', '.join(new_files)}")
        print(f"  📝 Logged to {LOG_FILE}")
    else:
        append_to_log(LOG_FILE, "local_file_monitor", f"Scanned {total_scanned} files, no new sources found")
        print(f"  ✅ No new files to ingest")
    
    return 0  # Always return 0 for cron


if __name__ == '__main__':
    sys.exit(main())
