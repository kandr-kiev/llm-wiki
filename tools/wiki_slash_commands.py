#!/usr/bin/env python3
"""
Wiki Slash Commands - Telegram /wm, /wi, /wd handlers.
Executes wiki tools directly without cron scheduler.
"""

import sys
import os
import subprocess
from pathlib import Path

# Add tools dir to path
TOOLS_DIR = Path(__file__).parent
sys.path.insert(0, str(TOOLS_DIR))


def run_source_monitor():
    """Run Source Monitor - scans raw/ for new content."""
    print("=" * 60)
    print("📡 SOURCE MONITOR")
    print("=" * 60)
    result = subprocess.run(
        [sys.executable, str(TOOLS_DIR / "source_monitor.py")],
        capture_output=True,
        text=True,
        cwd=str(TOOLS_DIR.parent)
    )
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    return result.returncode


def run_integrator():
    """Run Wiki Integrator - processes new raw articles."""
    print("=" * 60)
    print("🔗 WIKI INTEGRATOR")
    print("=" * 60)
    result = subprocess.run(
        [sys.executable, str(TOOLS_DIR / "integrator.py")],
        capture_output=True,
        text=True,
        cwd=str(TOOLS_DIR.parent)
    )
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    return result.returncode


def run_wiki_doctor():
    """Run Wiki Doctor - diagnoses and cures wiki issues."""
    print("=" * 60)
    print("🩺 WIKI DOCTOR")
    print("=" * 60)
    result = subprocess.run(
        [sys.executable, str(TOOLS_DIR / "wiki_doctor.py"), "cure"],
        capture_output=True,
        text=True,
        cwd=str(TOOLS_DIR.parent)
    )
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    return result.returncode


def main():
    if len(sys.argv) < 2:
        print("Usage: wiki_slash_commands.py <wm|wi|wd>")
        print("  wm  - Source Monitor (scan raw/ for new content)")
        print("  wi  - Wiki Integrator (process new raw articles)")
        print("  wd  - Wiki Doctor (diagnose and cure wiki issues)")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "wm":
        exit_code = run_source_monitor()
    elif command == "wi":
        exit_code = run_integrator()
    elif command == "wd":
        exit_code = run_wiki_doctor()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
