#!/usr/bin/env python3
"""Inbox Router for LLM Wiki — маршрутизація файлів з /workspace/towiki/ → raw/.

Сканує /workspace/towiki/ рекурсивно, класифікує файли за розширенням,
переміщує у відповідну підпапку raw/, створює frontmatter для текстових файлів,
видаляє з inbox після обробки.

Usage:
    python3 inbox_router.py              # одноразовий запуск
    python3 inbox_router.py --daemon     # демо-режим (кожні N секунд)
    python3 inbox_router.py --dry-run    # показати що б було зроблено
    python3 inbox_router.py --once       # одноразовий запуск (якщо --daemon є основний)
"""
import os
import sys
import shutil
import re
from pathlib import Path
from datetime import datetime, timezone

# Canonical utils — single source of truth
sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import split_frontmatter, compute_sha256, slugify, build_frontmatter

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
INBOX_DIR = Path("/workspace/towiki")
RAW_DIR = Path("/workspace/llm-wiki/raw")
LOG_FILE = RAW_DIR.parent / "log.md"
PROCESSED_DB = RAW_DIR.parent / ".processed" / "inbox_files.txt"

# ---------------------------------------------------------------------------
# File type classification by extension
# ---------------------------------------------------------------------------
ARTICLE_EXTENSIONS = {'.md', '.txt', '.rst', '.html', '.htm', '.text'}
PAPER_EXTENSIONS = {'.pdf'}
ASSET_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', '.bmp',
                     '.mp4', '.webm', '.avi', '.mov', '.mkv', '.mp3', '.wav',
                     '.m4a', '.ogg', '.flac', '.aac', '.opus'}
CONFIG_EXTENSIONS = {'.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.xml',
                     '.csv', '.tsv', '.env', '.properties'}
TRANSCRIPT_EXTENSIONS = {'.mp3', '.wav', '.m4a', '.ogg', '.flac', '.aac', '.opus'}

# Skip patterns for inbox scanning
SKIP_PATTERNS = {
    '.DS_Store', 'Thumbs.db', '.gitkeep',
}

# ---------------------------------------------------------------------------
# Database (dedup)
# ---------------------------------------------------------------------------
def _is_processed(filepath: Path) -> bool:
    """Check if this file was already processed (by path+size+mtime)."""
    if not PROCESSED_DB.exists():
        return False
    key = f"{filepath}:{filepath.stat().st_mtime}"
    with open(PROCESSED_DB, 'r') as f:
        keys = [line.strip() for line in f.readlines() if line.strip()]
    return key in keys


def _mark_processed(filepath: Path):
    key = f"{filepath}:{filepath.stat().st_mtime}"
    with open(PROCESSED_DB, 'a') as f:
        f.write(key + '\n')


# ---------------------------------------------------------------------------
# Frontmatter generation
# ---------------------------------------------------------------------------
# Canonical functions imported from utils:
#   split_frontmatter, compute_sha256, slugify, build_frontmatter


def _classify_file(filepath: Path) -> str:
    """Classify file by extension. Returns target subdirectory name."""
    ext = filepath.suffix.lower()
    name = filepath.name.lower()

    # Special cases: dotfiles without extension
    if not ext and name in {'.env', '.gitignore', '.gitattributes', '.editorconfig',
                             '.dockerignore', '.prettierrc', '.eslintrc', '.babelrc',
                             '.npmrc', '.nvmrc', '.pylintrc', '.flake8', '.mypy.ini',
                             '.tool-configuration', '.env.example', '.env.template'}:
        return "configs"

    # Determine target based on extension
    if ext in ARTICLE_EXTENSIONS:
        return "articles"
    elif ext in PAPER_EXTENSIONS:
        # Distinguish papers from other PDFs by filename heuristics
        if any(kw in name for kw in ['paper', 'arxiv', 'preprint', 'research', 'thesis']):
            return "papers"
        # Default: papers (most PDFs in inbox are papers)
        return "papers"
    elif ext in ASSET_EXTENSIONS and ext not in TRANSCRIPT_EXTENSIONS:
        return "assets"
    elif ext in CONFIG_EXTENSIONS:
        return "configs"
    elif ext in TRANSCRIPT_EXTENSIONS:
        return "transcripts"
    else:
        # Unknown extension — default to articles if text-parseable, else skip
        return None


def _ensure_target_dir(subdir: str) -> Path:
    target = RAW_DIR / subdir
    target.mkdir(parents=True, exist_ok=True)
    return target


def _process_text_file(filepath: Path, target_dir: Path, subdir: str) -> dict:
    """Process a text file: add frontmatter, compute SHA256, save to target."""
    filepath = Path(filepath)
    content = filepath.read_text(encoding='utf-8', errors='replace')[:50000]

    # Determine blog_source from subdir
    blog_source_map = {
        "articles": f"inbox:local",
        "papers": f"inbox:local",
        "configs": f"inbox:local",
        "transcripts": f"inbox:local",
    }

    # Generate filename
    stem = filepath.stem
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    slug = slugify(stem)
    filename = f"inbox-{slug}-{date_str}.md"
    target_path = target_dir / filename

    # Build frontmatter
    frontmatter = build_frontmatter(
        source_url=f"file://{filepath}",
        blog_source=blog_source_map.get(subdir, "inbox:local"),
    )

    # Write with placeholder SHA
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)

    # Fix SHA256
    file_content = target_path.read_text(encoding='utf-8')
    fm, body = split_frontmatter(file_content)
    if fm is not None:
        sha = compute_sha256(body)
        new_fm = fm.replace('sha256: PLACEHOLDER', f'sha256: {sha}')
        new_content = '---\n' + new_fm + '\n---\n' + body
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return {
        "action": "text_file",
        "source": str(filepath),
        "target": target_path.name,
        "target_path": target_path,
        "sha256": sha,
    }


def _process_binary_file(filepath: Path, target_dir: Path, subdir: str) -> dict:
    """Process a binary file: copy to target, no frontmatter needed."""
    filename = filepath.name
    target_path = target_dir / filename

    # Handle name collisions
    if target_path.exists():
        stem = filepath.stem
        ext = filepath.suffix
        date_str = datetime.now(timezone.utc).strftime('%Y%m%d')
        filename = f"{stem}-{date_str}{ext}"
        target_path = target_dir / filename

    shutil.copy2(str(filepath), str(target_path))

    return {
        "action": "binary_file",
        "source": str(filepath),
        "target": target_path.name,
        "target_path": target_path,
    }


# ---------------------------------------------------------------------------
# Main router
# ---------------------------------------------------------------------------
def scan_and_route(dry_run: bool = False) -> list[dict]:
    """Scan inbox directory and route all files to appropriate raw/ subdirectories.

    Returns list of actions performed.
    """
    inbox_str = str(INBOX_DIR)
    if not os.path.isdir(inbox_str):
        print(f"📭 Inbox не знайдено: {INBOX_DIR}")
        return []

    actions = []
    errors = []
    processed_count = 0

    # Collect all files using os.walk (avoids py.path.local / pathlib.Path incompatibility)
    file_list = []
    for dirpath, dirnames, filenames in os.walk(inbox_str):
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            if os.path.isfile(fpath):
                file_list.append(fpath)

    file_count = len(file_list)
    print(f"📂 Сканування inbox: {INBOX_DIR}")
    print(f"🔍 Знайдено файлів: {file_count}")
    print()

    for fpath_str in sorted(file_list):
        fname = os.path.basename(fpath_str)

        # Skip dotfiles and patterns
        if fname.startswith('.') or fname in SKIP_PATTERNS:
            continue

        # Convert to pathlib.Path for downstream functions
        filepath = Path(fpath_str)

        # Skip already processed
        if _is_processed(filepath):
            print(f"  ⏭️  Пропущено (оброблено): {filepath.relative_to(INBOX_DIR)}")
            continue

        subdir = _classify_file(filepath)
        if subdir is None:
            errors.append({
                "action": "skipped_unknown",
                "source": os.path.relpath(fpath_str, inbox_str),
                "reason": f"невідоме розширення {filepath.suffix}",
            })
            print(f"  ⚠️  Пропущено (невідоме розширення): {os.path.relpath(fpath_str, inbox_str)}")
            continue

        try:
            target_dir = _ensure_target_dir(subdir)

            if filepath.suffix.lower() in ARTICLE_EXTENSIONS:
                action = _process_text_file(filepath, target_dir, subdir)
            else:
                action = _process_binary_file(filepath, target_dir, subdir)

            target_path = action["target_path"]

            if not dry_run:
                os.unlink(fpath_str)
                _mark_processed(filepath)

            actions.append(action)
            processed_count += 1

            status_icon = "📝" if action["action"] == "text_file" else "📎"
            print(f"  {status_icon} {action['action']}: {os.path.relpath(fpath_str, inbox_str)} → {target_path.name}")

        except Exception as e:
            errors.append({
                "action": "error",
                "source": os.path.relpath(fpath_str, inbox_str),
                "error": str(e),
            })
            print(f"  ❌ Помилка: {os.path.relpath(fpath_str, inbox_str)} — {e}")

    # Clean up empty subdirectories in inbox
    for dirpath, dirnames, filenames in os.walk(inbox_str, topdown=False):
        if dirpath != inbox_str and not any(os.listdir(dirpath)):
            try:
                os.rmdir(dirpath)
            except OSError:
                pass

    if dry_run:
        print(f"\n🔒 DRY RUN — файлів оброблено: {processed_count} (не переміщено)")
    else:
        print(f"\n✅ Оброблено: {processed_count} файлів")

    if errors:
        print(f"\n⚠️  Помилки: {len(errors)}")
        for err in errors:
            print(f"  - {err['source']}: {err.get('reason', err.get('error', 'unknown'))}")

    return actions


def main():
    dry_run = '--dry-run' in sys.argv
    daemon = '--daemon' in sys.argv
    once = '--once' in sys.argv

    if daemon:
        # Remove --daemon from args so scan_and_route doesn't see it
        import time
        interval = 60
        if '--interval' in sys.argv:
            idx = sys.argv.index('--interval')
            if idx + 1 < len(sys.argv):
                try:
                    interval = int(sys.argv[idx + 1])
                except ValueError:
                    pass

        print(f"🔄 Inbox Router — daemon mode (interval: {interval}s)")
        print(f"📂 Inbox: {INBOX_DIR}")
        print(f"📁 Raw: {RAW_DIR}")
        print()

        PROCESSED_DB.parent.mkdir(parents=True, exist_ok=True)

        while True:
            scan_and_route(dry_run=dry_run)
            print(f"\n💤 Чекаю {interval} секунд...")
            time.sleep(interval)
    else:
        # Single run
        PROCESSED_DB.parent.mkdir(parents=True, exist_ok=True)
        actions = scan_and_route(dry_run=dry_run)
        print(f"\n📊 Підсумок: {len(actions)} дій, {len([a for a in actions if a['action'] == 'error'])} помилок")


if __name__ == '__main__':
    main()
