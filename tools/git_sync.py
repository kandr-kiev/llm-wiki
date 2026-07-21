#!/usr/bin/env python3
"""
Git Sync — Автоматичне додавання/видалення файлів у git для LLM Wiki.

Додає файли з правильних каталогів, ігнорує кеш та тимчасові файли.
Призначений для виклику з git alias: `git add-wiki`

Usage:
    python3 tools/git_sync.py          # Додати нові файли
    python3 tools/git_sync.py --clean  # Видалити tracked файли з .gitignore категорій
    python3 tools/git_sync.py --status # Показати статус
"""

import fnmatch
import os
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent

# ✅ Каталоги та файли, які ТРЕБА трекати
TRACK_PATTERNS = [
    # Raw sources (immutable)
    "raw/**/*.md",
    # Wiki synthesized pages (mutable)
    "wiki/concepts/**/*.md",
    "wiki/entities/**/*.md",
    "wiki/comparisons/**/*.md",
    "wiki/playbooks/**/*.md",
    "wiki/synthesis/**/*.md",
    "wiki/queries/**/*.md",
    "wiki/references/**/*.md",
    "wiki/templates/**/*.md",
    # Wiki index/log
    "wiki/index.md",
    "wiki/log.md",
    # Tools
    "tools/**/*.py",
    # Root docs
    "README.md",
    "SCHEMA.md",
    "AGENTS.md",
    "ARCHITECTURE.md",
    "log.md",
]

# ❌ Каталоги та файли, які ТРЕБА ігнорувати (не додавати)
IGNORE_PATTERNS = [
    ".processed/**/*",
    "outputs/**/*",
    "__pycache__/**/*",
    ".obsidian/workspace*.json",
    "wiki-secret.txt",
    "*.bak",
    "*.pyc",
    "*.pyo",
    ".DS_Store",
    "Thumbs.db",
]

# 📁 Каталог, який завжди ігноруємо повністю
IGNORE_DIRS = {
    ".processed",
    "outputs",
    "__pycache__",
    ".obsidian",
}


def should_ignore(filepath_str: str) -> bool:
    """Перевіряє, чи файл треба ігнорувати."""
    # Перевіряємо ignore directories
    parts = filepath_str.replace("\\", "/").split("/")
    for part in parts:
        if part in IGNORE_DIRS:
            return True

    # Перевіряємо ignore patterns
    for pattern in IGNORE_PATTERNS:
        if _match_pattern(filepath_str, pattern):
            return True

    return False


def should_track(filepath_str: str) -> bool:
    """Перевіряє, чи файл треба трекати."""
    if should_ignore(filepath_str):
        return False

    # Перевіряємо track patterns
    for pattern in TRACK_PATTERNS:
        if _match_pattern(filepath_str, pattern):
            return True

    return False


def _match_pattern(path: str, pattern: str) -> bool:
    """Проста перевірка pattern з * та **."""
    import fnmatch

    # Розбиваємо pattern на сегменти по '/'
    # ** = будь-які сегменти шляху
    # * = будь-які символи в межах одного сегмента
    path_parts = path.replace("\\", "/").split("/")
    pattern_parts = pattern.split("/")

    return _match_parts(path_parts, pattern_parts)


def _match_parts(path_parts: list, pattern_parts: list) -> bool:
    """Рекурсивний match сегментів шляху."""
    # Якщо pattern закінчився — перевіряємо чи path також
    if not pattern_parts:
        return not path_parts

    first_pat = pattern_parts[0]

    # ** — match 0+ сегментів
    if first_pat == "**":
        # ** може match 0, 1, або більше сегментів
        for i in range(len(path_parts) + 1):
            if _match_parts(path_parts[i:], pattern_parts[1:]):
                return True
        return False

    # Якщо path закінчився, а pattern ще є — не match
    if not path_parts:
        return False

    # Перевіряємо перший сегмент
    if fnmatch.fnmatch(path_parts[0], first_pat):
        return _match_parts(path_parts[1:], pattern_parts[1:])

    return False


def get_git_status() -> dict:
    """Отримує git status у форматі, зручному для парсингу."""
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=WIKI_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"❌ git status error: {result.stderr}")
        return {"modified": [], "untracked": [], "deleted": []}

    modified = []
    untracked = []
    deleted = []

    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        status = line[:2]
        raw_filepath = line[3:].strip()

        # Git quote filenames з кирилицею/спеціальними символами
        # Формат: "wiki/comparisons/3-\320\277..."
        # Розкутуємо: прибираємо лапки та розкодовуємо octal-escaped UTF-8 байти
        filepath = raw_filepath
        if filepath.startswith('"') and filepath.endswith('"'):
            filepath = filepath[1:-1]
            # Git escape: \NNN — octal байт UTF-8
            # Збираємо всі байти, потім декодуємо як UTF-8
            import re
            raw_bytes = bytearray()
            last_end = 0
            for m in re.finditer(r'\\([0-7]{3})', filepath):
                raw_bytes.extend(filepath[last_end:m.start()].encode('latin-1'))
                raw_bytes.append(int(m.group(1), 8))
                last_end = m.end()
            raw_bytes.extend(filepath[last_end:].encode('latin-1'))
            filepath = raw_bytes.decode('utf-8')

        if status == " M" or status == "M ":
            modified.append(filepath)
        elif status == "??":
            untracked.append(filepath)
        elif status == " D" or status == "D ":
            deleted.append(filepath)

    return {"modified": modified, "untracked": untracked, "deleted": deleted}


def add_files(filepaths: list[str]) -> int:
    """Додає файли до git. Повертає кількість доданих."""
    if not filepaths:
        return 0

    # Для файлів з кирилицею/спеціальними символами використовуємо
    # git add --pathspec-from-file з --pathspec-file-nul (null-terminated)
    # Цей підхід працює навіть на старих версіях git
    import tempfile
    import os

    # Розбиваємо на чанки по 50 файлів (обмеження довжини командного рядка)
    chunk_size = 50
    total_added = 0

    for i in range(0, len(filepaths), chunk_size):
        chunk = filepaths[i:i + chunk_size]

        # Створюємо тимчасовий файл зі шляхами (null-terminated)
        chunk_bytes = b''.join(fp.encode('utf-8') + b'\0' for fp in chunk)

        with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.paths') as tmp:
            tmp.write(chunk_bytes)
            tmp_path = tmp.name

        try:
            result = subprocess.run(
                ["git", "add", "--pathspec-from-file=" + tmp_path, "--pathspec-file-nul"],
                cwd=WIKI_ROOT,
                capture_output=True,
            )
            if result.returncode != 0:
                print(f"❌ git add error (chunk {i//chunk_size}): {result.stderr.decode()}")
            else:
                total_added += len(chunk)
        finally:
            os.unlink(tmp_path)

    return total_added


def remove_files(filepaths: list[str]) -> int:
    """Видаляє файли з git tracking (не з диска)."""
    if not filepaths:
        return 0

    result = subprocess.run(
        ["git", "rm", "--cached"] + filepaths,
        cwd=WIKI_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"❌ git rm error: {result.stderr}")
        return 0

    return len(filepaths)


def cmd_add() -> int:
    """Додає всі правильні файли."""
    status = get_git_status()

    # Фільтруємо untracked файли
    to_add = [f for f in status["untracked"] if should_track(f)]

    # Фільтруємо modified файли (вони вже tracked, але на випадок conflicts)
    # Modified файли вже в git, тому їх не треба додавати

    count = add_files(to_add)

    print(f"\n{'='*60}")
    print(f"📋 Git Sync Report")
    print(f"{'='*60}")
    print(f"  Модифіковані (tracked):  {len(status['modified'])}")
    print(f"  Невідомі (untracked):   {len(status['untracked'])}")
    print(f"  Видалені:               {len(status['deleted'])}")
    print(f"  Додано до git:          {count}")

    # Показуємо, що було проігноровано
    ignored = [f for f in status["untracked"] if not should_track(f)]
    if ignored:
        print(f"\n  ⏭ Пропущено (ігнор):   {len(ignored)}")
        # Показуємо перші 10
        for f in ignored[:10]:
            print(f"    - {f}")
        if len(ignored) > 10:
            print(f"    ... ще {len(ignored) - 10}")

    print(f"{'='*60}\n")

    return count


def cmd_clean() -> int:
    """Видаляє з git tracking файли, які потрапили туди помилково."""
    status = get_git_status()

    # Знаходимо tracked файли, які мають бути ігноровані
    # Для цього перевіряємо modified файли
    to_remove = [f for f in status["modified"] if should_ignore(f)]

    if not to_remove:
        print("✅ Немає файлів для видалення з tracking.")
        return 0

    count = remove_files(to_remove)

    print(f"\n{'='*60}")
    print(f"🧹 Git Clean Report")
    print(f"{'='*60}")
    print(f"  Видалено з tracking:    {count}")
    print(f"{'='*60}\n")

    return count


def cmd_status():
    """Показує детальний статус."""
    status = get_git_status()

    # Аналізуємо untracked файли за каталогами
    tracked_new = []
    ignored_new = []

    for f in status["untracked"]:
        if should_track(f):
            tracked_new.append(f)
        else:
            ignored_new.append(f)

    # Аналізуємо modified за каталогами
    mod_by_dir = {}
    for f in status["modified"]:
        parts = f.split("/", 1)
        if len(parts) > 1:
            top_dir = parts[0]
        else:
            top_dir = "(root)"
        mod_by_dir[top_dir] = mod_by_dir.get(top_dir, 0) + 1

    print(f"\n{'='*60}")
    print(f"📊 Git Status Detail")
    print(f"{'='*60}")

    print(f"\n📝 Модифіковані (tracked): {len(status['modified'])}")
    for d, c in sorted(mod_by_dir.items(), key=lambda x: -x[1]):
        print(f"  {d}/: {c}")

    print(f"\n🆕 Невідомі (untracked): {len(status['untracked'])}")
    print(f"  ✅ Треба додати: {len(tracked_new)}")
    print(f"  ⏭ Ігнорувати:    {len(ignored_new)}")

    if tracked_new:
        dir_counts = {}
        for f in tracked_new:
            parts = f.split("/", 1)
            top_dir = parts[0] if len(parts) > 1 else "(root)"
            dir_counts[top_dir] = dir_counts.get(top_dir, 0) + 1
        print(f"  За каталогами:")
        for d, c in sorted(dir_counts.items(), key=lambda x: -x[1]):
            print(f"    {d}/: {c}")

    if ignored_new:
        dir_counts = {}
        for f in ignored_new:
            parts = f.split("/", 1)
            top_dir = parts[0] if len(parts) > 1 else "(root)"
            dir_counts[top_dir] = dir_counts.get(top_dir, 0) + 1
        print(f"  За каталогами:")
        for d, c in sorted(dir_counts.items(), key=lambda x: -x[1]):
            print(f"    {d}/: {c}")

    print(f"{'='*60}\n")


def main():
    if len(sys.argv) < 2:
        cmd_add()
        return

    command = sys.argv[1]

    if command == "--add" or command == "add":
        cmd_add()
    elif command == "--clean" or command == "clean":
        cmd_clean()
    elif command == "--status" or command == "status":
        cmd_status()
    else:
        print(f"❌ Невідома команда: {command}")
        print(f"   Використання: git_sync.py [--add|--clean|--status]")
        sys.exit(1)


if __name__ == "__main__":
    main()
