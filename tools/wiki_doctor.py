#!/usr/bin/env python3
"""Wiki Doctor — діагностика та лікування LLM Wiki системи.

Дві функції:
  1. diagnose()     — виявлення проблем у всіх шарах системи
  2. diagnose_and_cure() — діагностика + автоматичне виправлення

Шари аналізу:
  - wiki_pages:    frontmatter, wikilinks, tags, index, size, confidence
  - raw_sources:   frontmatter, SHA256 integrity
  - index:         duplicates, stale links, metadata
  - infrastructure: APPROVED_TAGS sync, root files, _N duplicates, Astro truncation
  - integrator:    existence check
  - config:        SCHEMA.md tag taxonomy sync

Алгоритм лікування:
  - broken_wikilinks → замінити на існуючі slug-и або видалити
  - missing_fields → додати default frontmatter
  - sha256_drift → оновити хеш
  - missing_from_index → додати до index.md
  - root_files → перемістити у правильний підкаталог
  - _N_duplicates → видалити дублікати (base version існує)
  - approved_tags_drift → синхронізувати з SCHEMA.md
  - markdown_link_in_wikilink → конвертувати у стандартний markdown

Автор: Archivist | Версія: 1.0.0 | Дата: 2026-07-11
"""

import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Imports from utils (canonical functions)
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import (
    split_frontmatter,
    parse_simple_yaml,
    APPROVED_TAGS,
    compute_sha256,
    check_raw_integrity,
    fix_file_hash,
    append_to_log,
    slugify,
)
from standard_report import format_wiki_doctor_report

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
RAW_DIR = ROOT / "raw"
TOOLS_DIR = ROOT / "tools"
INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = ROOT / "log.md"
SCHEMA_FILE = ROOT / "SCHEMA.md"
RESERVED_NAMES = {"README.md"}

# Page type → subdirectory mapping
TYPE_DIR_MAP = {
    "concept": "concepts",
    "entity": "entities",
    "comparison": "comparisons",
    "playbook": "playbooks",
    "synthesis": "synthesis",
    "query": "queries",
    "reference": "references",
}

# Required frontmatter fields per OKF v0.1 + wiki convention
REQUIRED_FIELDS = {"type", "title", "description", "created", "updated", "tags", "sources", "confidence", "links"}

# ---------------------------------------------------------------------------
# Diagnostic Report Data Structure
# ---------------------------------------------------------------------------
class DoctorReport:
    """Structured diagnostic report with per-layer analysis."""

    def __init__(self):
        self.timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
        self.layers = {}  # layer_name → list of {severity, path, message, detail, auto_fixable}
        self.summary = {"total": 0, "ERROR": 0, "WARN": 0, "INFO": 0, "auto_fixable": 0}

    def add(self, layer, severity, path, message, detail=None, auto_fixable=False):
        entry = {
            "layer": layer,
            "severity": severity,
            "path": str(path),
            "message": message,
            "detail": detail,
            "auto_fixable": auto_fixable,
        }
        self.layers.setdefault(layer, []).append(entry)
        self.summary["total"] += 1
        self.summary[severity] = self.summary.get(severity, 0) + 1
        if auto_fixable:
            self.summary["auto_fixable"] += 1

    def get_all_issues(self):
        """Flatten all issues across layers."""
        issues = []
        for layer_issues in self.layers.values():
            issues.extend(layer_issues)
        return issues

    def severity_summary(self):
        return (
            f"**ERROR:** {self.summary['ERROR']} | "
            f"**WARN:** {self.summary['WARN']} | "
            f"**INFO:** {self.summary['INFO']} | "
            f"**Auto-fixable:** {self.summary['auto_fixable']}"
        )


# ---------------------------------------------------------------------------
# LAYER 1: Wiki Pages Diagnostics
# ---------------------------------------------------------------------------

def diagnose_wiki_pages(report):
    """Check all wiki pages: frontmatter, wikilinks, tags, index, size, confidence."""
    wiki_pages = [
        p for p in WIKI_DIR.rglob("*.md")
        if p.name not in RESERVED_NAMES and p.parent.name not in ("templates", "comparisons")
    ]
    slugs = {p.stem: p for p in wiki_pages}
    index_text = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""

    for page in wiki_pages:
        rel = page.relative_to(ROOT)
        text = page.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)

        # 1a. Missing frontmatter
        if fm is None:
            report.add("wiki_pages", "ERROR", rel, "missing or malformed frontmatter", auto_fixable=False)
            continue

        data = parse_simple_yaml(fm)

        # 1b. Missing required fields
        missing = sorted(REQUIRED_FIELDS - set(data))
        if missing:
            report.add("wiki_pages", "ERROR", rel, f"missing fields: {', '.join(missing)}", auto_fixable=True)

        # 1c. Unapproved tags
        for tag in data.get("tags", []):
            if tag not in APPROVED_TAGS:
                report.add("wiki_pages", "WARN", rel, f"unapproved tag: {tag}", auto_fixable=True)

        # 1d. Missing from index.md
        if str(rel) not in index_text and rel != Path("wiki/index.md"):
            report.add("wiki_pages", "ERROR", rel, "page missing from index.md", auto_fixable=True)

        # 1e. Page too large
        if len(text.splitlines()) > 200:
            report.add("wiki_pages", "WARN", rel, "page over 200 lines", auto_fixable=False)

        # 1f. Low confidence
        if str(data.get("confidence", "")).lower() == "low":
            report.add("wiki_pages", "INFO", rel, "low confidence page", auto_fixable=False)

        # 1g. Contested page
        if data.get("contested") is True:
            report.add("wiki_pages", "INFO", rel, "contested page", auto_fixable=False)

        # 1h. Broken wikilinks
        clean_body = re.sub(r'<astro-island\b.*', ' ', body, flags=re.DOTALL)
        clean_body = re.sub(r'<[^>]+>', ' ', clean_body)
        for link in re.findall(r"\[\[([^\]|#]+)", clean_body):
            if link not in slugs:
                report.add("wiki_pages", "ERROR", rel, f"broken wikilink: [[{link}]]", auto_fixable=True)

        # 1i. Source files missing
        sources = data.get("sources", [])
        if isinstance(sources, str):
            sources = [sources]
        for src in sources:
            src_path = ROOT / src
            if not src_path.is_file():
                report.add("wiki_pages", "ERROR", rel, f"source file missing: {src}", auto_fixable=True)

    return slugs


# ---------------------------------------------------------------------------
# LAYER 2: Raw Sources Diagnostics
# ---------------------------------------------------------------------------

def diagnose_raw_sources(report):
    """Check raw sources: frontmatter, SHA256 integrity."""
    for raw in RAW_DIR.rglob("*.md"):
        if raw.name == "README.md":
            continue
        rel = raw.relative_to(ROOT)
        text = raw.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)

        if fm is None:
            report.add("raw_sources", "ERROR", rel, "raw source missing frontmatter", auto_fixable=True)
            continue

        data = parse_simple_yaml(fm)
        expected = data.get("sha256")
        if expected is None:
            continue

        # strip leading newline that split_frontmatter includes
        body_hash = hashlib.sha256(body.lstrip("\n").encode("utf-8")).hexdigest()
        if expected != body_hash:
            report.add("raw_sources", "ERROR", rel, "sha256 drift", auto_fixable=True)


# ---------------------------------------------------------------------------
# LAYER 3: Index.md Diagnostics
# ---------------------------------------------------------------------------

def diagnose_index(report):
    """Check index.md: duplicates, stale links, metadata."""
    if not INDEX_FILE.exists():
        report.add("index", "ERROR", "wiki/index.md", "index.md missing", auto_fixable=False)
        return

    index_text = INDEX_FILE.read_text(encoding="utf-8")

    # 3a. Duplicate entries
    slug_counts = defaultdict(int)
    for match in re.finditer(r'\[\[([^\]]+)\]\]', index_text):
        slug = match.group(1)
        if '/' not in slug and not slug.endswith('.md'):
            slug_counts[slug] += 1
    for slug, count in slug_counts.items():
        if count > 1:
            report.add("index", "WARN", "wiki/index.md", f"duplicate entry: [[{slug}]] ({count}x)", auto_fixable=True)

    # 3b. Missing metadata
    if "Last updated:" not in index_text:
        report.add("index", "WARN", "wiki/index.md", "missing 'Last updated' metadata", auto_fixable=True)
    if "Total pages:" not in index_text:
        report.add("index", "WARN", "wiki/index.md", "missing 'Total pages' metadata", auto_fixable=True)

    # 3c. Stale links (pointing to deleted _N files or wrong paths)
    # Correct plural subdirectories
    correct_subdirs = {"concepts", "entities", "playbooks", "comparisons", "synthesis", "queries", "references"}
    for match in re.finditer(r'\[\[wiki/(\w+)/([^\]]+)\]\]', index_text):
        subdir = match.group(1)
        slug = match.group(2)
        if subdir not in correct_subdirs:
            report.add("index", "WARN", "wiki/index.md", f"stale path: wiki/{subdir}/ should be wiki/{slug} — unknown section", auto_fixable=True)


# ---------------------------------------------------------------------------
# LAYER 4: Infrastructure Diagnostics
# ---------------------------------------------------------------------------

def diagnose_infrastructure(report):
    """Check: APPROVED_TAGS sync, root files, _N duplicates, Astro truncation."""

    # 4a. Root-level wiki files (should be in subdirectories)
    for f in WIKI_DIR.glob("*.md"):
        if f.name in RESERVED_NAMES or f.name == "index.md" or f.name == "log.md":
            continue
        report.add("infrastructure", "WARN", f.relative_to(ROOT),
                   "wiki file in root directory (should be in subdirectory)", auto_fixable=True)

    # 4b. _N duplicate files
    for subdir in WIKI_DIR.iterdir():
        if not subdir.is_dir():
            continue
        files = list(subdir.glob("*.md"))
        base_names = defaultdict(list)
        for f in files:
            m = re.match(r'^(.+)_\d+$', f.stem)
            if m:
                base_names[m.group(1)].append(f)
        for base, variants in base_names.items():
            base_path = subdir / f"{base}.md"
            if base_path.exists():
                for v in variants:
                    report.add("infrastructure", "WARN", v.relative_to(ROOT),
                               f"duplicate of [[{base}]]", auto_fixable=True)
            else:
                # No base version — these ARE the content
                if len(variants) > 1:
                    for v in variants[1:]:
                        report.add("infrastructure", "WARN", v.relative_to(ROOT),
                                   f"fallback duplicate (no base version for '{base}')", auto_fixable=True)

    # 4c. APPROVED_TAGS drift vs SCHEMA.md
    schema_tags = extract_schema_tags()
    if schema_tags:
        missing_from_linter = schema_tags - APPROVED_TAGS
        extra_in_linter = APPROVED_TAGS - schema_tags
        if missing_from_linter:
            report.add("infrastructure", "WARN", "tools/approved_tags.json",
                       f"APPROVED_TAGS missing {len(missing_from_linter)} tags from SCHEMA.md", auto_fixable=True)
        if extra_in_linter and len(extra_in_linter) < 50:
            report.add("infrastructure", "WARN", "tools/approved_tags.json",
                       f"APPROVED_TAGS has {len(extra_in_linter)} tags not in SCHEMA.md", auto_fixable=False)

    # 4d. Truncated files (Astro JSON truncation)
    wiki_pages = list(WIKI_DIR.rglob("*.md"))
    for page in wiki_pages:
        if page.name in RESERVED_NAMES or page.parent.name in ("templates", "comparisons"):
            continue
        text = page.read_text(encoding="utf-8")
        if "<astro-island" in text:
            # Check if file ends abruptly after astro-island
            last_part = text[-500:]
            if not last_part.strip().endswith("---") and not last_part.strip().endswith("*Auto-generated*"):
                report.add("infrastructure", "WARN", page.relative_to(ROOT),
                           "possible truncated file (astro-island not closed)", auto_fixable=False)


# ---------------------------------------------------------------------------
# LAYER 5: Integrator Diagnostics
# ---------------------------------------------------------------------------

def diagnose_integrator(report):
    """Check if integrator.py exists and has critical bugs."""
    integrator = TOOLS_DIR / "integrator.py"
    if not integrator.exists():
        report.add("integrator", "WARN", "tools/integrator.py", "integrator.py missing", auto_fixable=False)
        return

    content = integrator.read_text(encoding="utf-8")

    # Check for known critical bugs
    if "for key, value in " in content and ".items()" not in content:
        report.add("integrator", "ERROR", "tools/integrator.py",
                   "dict iteration without .items() — will crash", auto_fixable=True)

    if "write_file" in content and re.search(r'r\\[\\s\\+\\]', content):
        report.add("integrator", "WARN", "tools/integrator.py",
                   "regex with backslashes — write_file may double-escape", auto_fixable=True)


# ---------------------------------------------------------------------------
# LAYER 6: Config / SCHEMA.md Diagnostics
# ---------------------------------------------------------------------------

def extract_schema_tags():
    """Extract tags from SCHEMA.md tag taxonomy section ONLY.

    SCHEMA.md contains tags in Markdown tables within the '## Tag Taxonomy' section.
    This function isolates that section and parses table cells for backtick-enclosed tags.
    """
    if not SCHEMA_FILE.exists():
        return None
    text = SCHEMA_FILE.read_text(encoding="utf-8")
    tags = set()

    # Isolate the Tag Taxonomy section only
    taxonomy_start = text.find('## Tag Taxonomy')
    if taxonomy_start == -1:
        return None

    # Find the end: next major section after tags (e.g., '### Page Thresholds')
    taxonomy_end = text.find('### Page Thresholds', taxonomy_start)
    if taxonomy_end == -1:
        taxonomy_end = len(text)

    taxonomy_section = text[taxonomy_start:taxonomy_end]

    # Parse Markdown table rows for backtick-enclosed tags
    # Table rows look like: || `tag-name` | `tag2` | `tag3` | |
    for line in taxonomy_section.split('\n'):
        if not line.strip().startswith('|'):
            continue
        # Skip header separator rows (|---|---|)
        if re.match(r'^\|[\s\-:|]+\|', line) and not '`' in line:
            continue

        # Extract all backtick-enclosed values from this row
        for m in re.finditer(r'\`([^\`]+)\`', line):
            tag = m.group(1).strip()
            # Only accept valid tag format: lowercase alphanumeric + hyphens
            if tag and re.match(r'^[\w\-]+$', tag):
                tags.add(tag)

    return tags


def diagnose_config(report):
    """Check SCHEMA.md, config files."""
    if not SCHEMA_FILE.exists():
        report.add("config", "ERROR", "SCHEMA.md", "SCHEMA.md missing — wiki NOT OKF compliant", auto_fixable=False)
        return

    # Check tag taxonomy completeness
    schema_tags = extract_schema_tags()
    if schema_tags:
        # Check for tags used in wiki but not in SCHEMA.md
        used_tags = set()
        for page in (WIKI_DIR).rglob("*.md"):
            if page.name in RESERVED_NAMES or page.parent.name in ("templates", "comparisons"):
                continue
            text = page.read_text(encoding="utf-8")
            fm, _ = split_frontmatter(text)
            if fm:
                data = parse_simple_yaml(fm)
                for tag in data.get("tags", []):
                    used_tags.add(tag)
        unused_in_schema = used_tags - schema_tags
        if unused_in_schema:
            report.add("config", "WARN", "SCHEMA.md",
                       f"{len(unused_in_schema)} tags used in wiki not in SCHEMA.md taxonomy", auto_fixable=True)


# ---------------------------------------------------------------------------
# DIAGNOSIS ORCHESTRATOR
# ---------------------------------------------------------------------------

def diagnose():
    """Full system diagnosis — all layers. Returns DoctorReport."""
    report = DoctorReport()

    diagnose_wiki_pages(report)
    diagnose_raw_sources(report)
    diagnose_index(report)
    diagnose_infrastructure(report)
    diagnose_integrator(report)
    diagnose_config(report)

    return report


# ---------------------------------------------------------------------------
# CURE FUNCTIONS (auto-fix)
# ---------------------------------------------------------------------------

# Global flag for dry-run mode
_DRY_RUN = False


def _set_dry_run(flag: bool):
    """Set dry-run mode for all cure functions."""
    global _DRY_RUN
    _DRY_RUN = flag


def _write_if_not_dry(path: Path, content: str):
    """Write file only if not in dry-run mode."""
    if _DRY_RUN:
        return False
    path.write_text(content, encoding="utf-8")
    return True

def cure_broken_wikilinks(report):
    """Fix broken wikilinks: replace with existing slugs or remove."""
    wiki_pages = [
        p for p in WIKI_DIR.rglob("*.md")
        if p.name not in RESERVED_NAMES and p.parent.name not in ("templates", "comparisons")
    ]
    slugs = {p.stem: p for p in wiki_pages}
    fixes = 0
    dry_changes = 0

    for page in wiki_pages:
        text = page.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is None:
            continue

        # Fix broken wikilinks in body
        clean_body = re.sub(r'<astro-island\b.*', ' ', body, flags=re.DOTALL)
        clean_body = re.sub(r'<[^>]+>', ' ', clean_body)

        def replace_wikilink(m):
            nonlocal fixes, dry_changes
            link = m.group(1)
            if link in slugs:
                return m.group(0)  # already valid
            # Check if it's a markdown link [[name](url)] — convert to standard markdown
            full_match = m.group(0)
            if "](" in full_match:
                fixes += 1
                if _DRY_RUN:
                    dry_changes += 1
                    return m.group(0).replace("[[", "[").rstrip("]")
                return m.group(0).replace("[[", "[").rstrip("]")
            # Try to find similar existing slug
            best = _find_best_slug_match(link, slugs)
            if best:
                fixes += 1
                if _DRY_RUN:
                    dry_changes += 1
                    return f"[[{best}]]"
                return f"[[{best}]]"
            # Remove orphaned wikilink
            fixes += 1
            if _DRY_RUN:
                dry_changes += 1
            return ""

        # Use clean_body (Astro tags stripped) — matches diagnose_wiki_pages input
        # This ensures diagnose and cure operate on the same input surface
        # NOTE: pattern allows # (for [[page#anchor]] and [[Issue #123: title]]).
        # Non-greedy + ] exclusion handles all wikilink variants.
        new_body = re.sub(r"\[\[([^\]]+?)\]\]", replace_wikilink, clean_body)
        if new_body != clean_body:
            new_text = fm + "\n" + new_body
            _write_if_not_dry(page, new_text)

    # P1a: Fix triple/nested brackets — [[[[karpathy]] -> [[karpathy]]
    for page in wiki_pages:
        text = page.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is None:
            continue
        clean_body = re.sub(r'<astro-island\b.*', ' ', body, flags=re.DOTALL)
        clean_body = re.sub(r'<[^>]+>', ' ', clean_body)

        # Fix [[[text]] -> [[text]] (remove extra leading [)
        new_body = re.sub(r'\[\[\[([^\]]+)\]\]', r'[[\1]]', clean_body)

        # Fix ]]] -> ]] (triple closing)
        while ']]]' in new_body:
            new_body = new_body.replace(']]]', ']]', 1)

        if new_body != clean_body:
            new_text = fm + "\n" + new_body
            _write_if_not_dry(page, new_text)
            fixes += 1

    # P1b: Fix [[Issue #NNNNN: text with ] inside]] — regex [^\]|#]+ fails on ]
    # Strategy: find [[ then match until the LAST ]] on a reasonable boundary
    for page in wiki_pages:
        text = page.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is None:
            continue
        clean_body = re.sub(r'<astro-island\b.*', ' ', body, flags=re.DOTALL)
        clean_body = re.sub(r'<[^>]+>', ' ', clean_body)
        original = clean_body

        # Pattern: [[Issue #DIGIT: ...]] where ... may contain ]
        # Use greedy match to LAST ]] on the line
        def fix_issue_greedy(m):
            nonlocal fixes
            full = m.group(0)
            inner = m.group(1)
            # Convert to markdown link format
            fixes += 1
            return f'[{inner}]'

        # Match [[ then everything until the last ]] in context
        # This handles [[Issue #123: text with ] inside]]
        new_body = re.sub(r'\[\[(Issue #[\d]+: [^\]]+?)\]\]', fix_issue_greedy, clean_body)
        # Also handle cases with ] inside: [[Issue #123: text] more]]
        new_body = re.sub(r'\[\[(Issue #[\d]+:[^\]]*(?:\][^\]]+?)?)\]\]', fix_issue_greedy, new_body)

        if new_body != original:
            new_text = fm + "\n" + new_body
            _write_if_not_dry(page, new_text)

    return fixes


def cure_missing_frontmatter(report):
    """Add default frontmatter to pages missing it."""
    wiki_pages = [
        p for p in WIKI_DIR.rglob("*.md")
        if p.name not in RESERVED_NAMES and p.parent.name not in ("templates", "comparisons")
    ]
    fixes = 0
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d')

    for page in wiki_pages:
        text = page.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is not None:
            continue

        # Extract title from H1
        h1_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
        title = h1_match.group(1).strip() if h1_match else page.stem.replace('-', ' ').title()

        default_fm = (
            f"---\n"
            f"type: concept\n"
            f"title: {title}\n"
            f"description: Auto-generated by Wiki Doctor\n"
            f"tags: [llm-wiki, concept]\n"
            f"sources: []\n"
            f"confidence: medium\n"
            f"links: []\n"
            f"created: {now}\n"
            f"updated: {now}\n"
            f"---\n"
        )
        _write_if_not_dry(page, default_fm + body)
        if not _DRY_RUN:
            fixes += 1

    return fixes


def cure_raw_sources_frontmatter(report):
    """Add default frontmatter to raw source files missing it."""
    fixes = 0
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d')

    for raw in RAW_DIR.rglob("*.md"):
        if raw.name == "README.md":
            continue
        text = raw.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is not None:
            continue

        default_fm = (
            f"---\n"
            f"source_url: unknown\n"
            f"ingested: {now}\n"
            f"sha256: PLACEHOLDER\n"
            f"blog_source: inbox:local\n"
            f"---\n"
        )
        _write_if_not_dry(raw, default_fm + body)
        if not _DRY_RUN:
            fixes += 1

    return fixes


def cure_sha256_drift(report):
    """Fix SHA256 drift in raw sources."""
    fixes = 0
    for raw in RAW_DIR.rglob("*.md"):
        if raw.name == "README.md":
            continue
        if _DRY_RUN:
            # Dry-run: check if hash would change without writing
            # MUST use body.lstrip("\n") to match diagnose_raw_sources and fix_file_hash
            text = raw.read_text(encoding='utf-8')
            fm, body = split_frontmatter(text)
            if fm:
                data = parse_simple_yaml(fm)
                expected = data.get("sha256")
                if expected:
                    actual = hashlib.sha256(body.lstrip("\n").encode("utf-8")).hexdigest()
                    if expected != actual:
                        fixes += 1
        else:
            if fix_file_hash(raw):
                fixes += 1
    return fixes


def cure_approved_tags_drift(report):
    """Sync APPROVED_TAGS in approved_tags.json with SCHEMA.md + actual wiki usage."""
    approved_path = TOOLS_DIR / "approved_tags.json"
    schema_tags = extract_schema_tags()
    if not schema_tags:
        return 0

    # Load current approved tags from JSON
    if approved_path.exists():
        current_tags = set(json.loads(approved_path.read_text(encoding="utf-8")))
    else:
        current_tags = set()

    # Collect all tags actually used in wiki pages
    used_tags = set()
    for page in WIKI_DIR.rglob("*.md"):
        if page.name in RESERVED_NAMES or page.parent.name in ("templates", "comparisons"):
            continue
        text = page.read_text(encoding="utf-8")
        fm, _ = split_frontmatter(text)
        if fm:
            data = parse_simple_yaml(fm)
            for tag in data.get("tags", []):
                used_tags.add(tag)

    # Merge: schema + actual usage + current approved
    all_tags = schema_tags | used_tags | current_tags

    # Sort alphabetically and write to JSON
    sorted_tags = sorted(all_tags)
    approved_path.write_text(json.dumps(sorted_tags, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return len(all_tags) - len(current_tags) if current_tags else len(all_tags)


def cure_missing_index_entries(report):
    """Add pages missing from index.md."""
    if not INDEX_FILE.exists():
        return 0

    wiki_pages = [
        p for p in WIKI_DIR.rglob("*.md")
        if p.name not in RESERVED_NAMES and p.parent.name not in ("templates", "comparisons")
    ]
    fixes = 0

    # Read index ONCE, then collect ALL entries to add before writing
    # Bug fix: previously read index_text once but wrote N times, each overwriting previous
    index_text = INDEX_FILE.read_text(encoding="utf-8")
    entries_to_add = []

    for page in wiki_pages:
        rel = page.relative_to(ROOT)
        if page.name == "index.md":
            continue
        if str(rel) in index_text:
            continue

        # Extract title
        text = page.read_text(encoding="utf-8")
        fm, _ = split_frontmatter(text)
        if fm:
            data = parse_simple_yaml(fm)
            title = data.get("title", page.stem.replace('-', ' ').title())
        else:
            title = page.stem.replace('-', ' ').title()

        # Find insertion point (correct section)
        page_type = (data.get("type", "concept") if fm else "concept")
        subdir = TYPE_DIR_MAP.get(page_type, "concepts")
        section_marker = f"### {subdir.capitalize()}"

        lines = index_text.split('\n')
        insert_idx = len(lines)
        for i, line in enumerate(lines):
            if section_marker in line:
                # Find end of this section (next ### header)
                for j in range(i + 1, len(lines)):
                    if lines[j].startswith('### '):
                        insert_idx = j
                        break
                else:
                    insert_idx = len(lines)
                break

        entries_to_add.append((insert_idx, title, rel))

    # Now apply all entries in reverse order so indices stay valid
    if entries_to_add:
        fixes = len(entries_to_add)
        lines = index_text.split('\n')
        for insert_idx, title, rel in reversed(entries_to_add):
            entry = f"| {title} | `{rel}` |\n"
            lines.insert(insert_idx, entry)

        new_index = '\n'.join(lines)

        # Update total count: add all fixes at once
        total_match = re.search(r'Total pages:\s*(\d+)', new_index)
        if total_match:
            new_total = int(total_match.group(1)) + fixes
            new_index = re.sub(r'(Total pages:\s*)\d+', rf'\g<1>{new_total}', new_index)

        _write_if_not_dry(INDEX_FILE, new_index)

    return fixes


def cure_missing_sources(report):
    """Remove or fix source files that don't exist."""
    wiki_pages = [
        p for p in WIKI_DIR.rglob("*.md")
        if p.name not in RESERVED_NAMES and p.parent.name not in ("templates", "comparisons")
    ]
    fixes = 0

    for page in wiki_pages:
        text = page.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is None:
            continue

        data = parse_simple_yaml(fm)
        sources = data.get("sources", [])
        if isinstance(sources, str):
            sources = [sources]

        valid_sources = []
        changed = False
        for src in sources:
            src_path = ROOT / src
            if src_path.is_file():
                valid_sources.append(src)
            else:
                changed = True

        if changed:
            # Rebuild frontmatter — use valid_sources (not original sources)
            lines = fm.split('\n')
            new_lines = []
            i = 0
            while i < len(lines):
                line = lines[i]
                if line.strip().startswith("sources:"):
                    if isinstance(valid_sources, list) and len(valid_sources) == 1:
                        new_lines.append(f"sources: [{valid_sources[0]}]")
                    elif isinstance(valid_sources, list) and len(valid_sources) > 1:
                        new_lines.append(f"sources: [{', '.join(valid_sources)}]")
                    else:
                        new_lines.append("sources: []")
                else:
                    new_lines.append(line)
                i += 1

            new_fm = '\n'.join(new_lines)
            new_text = f"---\n{new_fm}\n---\n{body}"
            _write_if_not_dry(page, new_text)
            fixes += 1

    return fixes


def cure_missing_fields(report):
    """Add missing required fields to frontmatter."""
    wiki_pages = [
        p for p in WIKI_DIR.rglob("*.md")
        if p.name not in RESERVED_NAMES and p.parent.name not in ("templates", "comparisons")
        and p.name != "index.md"
    ]
    fixes = 0
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    for page in wiki_pages:
        text = page.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is None:
            continue

        data = parse_simple_yaml(fm)
        missing = sorted(REQUIRED_FIELDS - set(data))
        if not missing:
            continue

        # Build new frontmatter lines
        lines = fm.split('\n')
        existing_keys = set()
        new_lines = []
        for line in lines:
            if ':' in line and not line.strip().startswith('#'):
                key = line.split(':')[0].strip()
                existing_keys.add(key)
            new_lines.append(line)

        # Add missing fields
        defaults = {
            "description": "Auto-filled by Wiki Doctor",
            "tags": "[llm-wiki]",
            "sources": "[]",
            "confidence": "medium",
            "links": "[]",
            "created": now,
            "updated": now,
        }
        for key in missing:
            if key == "type":
                continue  # Don't auto-assign type
            val = defaults.get(key, "")
            new_lines.append(f"{key}: {val}")

        new_fm = '\n'.join(new_lines)
        new_text = f"---\n{new_fm}\n---\n{body}"
        _write_if_not_dry(page, new_text)
        if not _DRY_RUN:
            fixes += 1

    return fixes


# ---------------------------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------------------------

def _find_best_slug_match(link, slugs):
    """Find best matching slug for a broken wikilink."""
    if link in slugs:
        return link

    # Simple word overlap
    link_words = set(re.split(r'[-\s]+', link.lower()))
    best_score = 0
    best_slug = None

    for slug in slugs:
        slug_words = set(re.split(r'[-\s]+', slug.lower()))
        overlap = len(link_words & slug_words)
        if overlap > best_score:
            best_score = overlap
            best_slug = slug

    # Require at least 2 shared words
    if best_score >= 2:
        return best_slug
    return None


# ---------------------------------------------------------------------------
# CURE ORCHESTRATOR
# ---------------------------------------------------------------------------

def diagnose_and_cure(dry_run=False):
    """Full diagnosis + auto-cure cycle. Returns DoctorReport + cure stats."""
    global _DRY_RUN
    _DRY_RUN = dry_run

    mode_label = "DRY-RUN" if dry_run else "LIVE"
    print("=" * 60)
    print(f"  WIKI DOCTOR — Повна діагностика та лікування [{mode_label}]")
    print(f"  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 60)

    # Phase 1: Diagnose
    print(f"\n🔍 Фаза 1: Діагностика всіх шарів...")
    report = diagnose()
    print(f"\n📊 Результати діагностики:")
    print(f"   {report.severity_summary()}")

    # Phase 2: Cure
    print(f"\n💊 Фаза 2: Лікування...")
    cure_stats = {}

    if report.summary["ERROR"] > 0:
        # Priority 1: Fix broken wikilinks
        n = cure_broken_wikilinks(report)
        cure_stats["broken_wikilinks"] = n

        # Priority 2: Fix missing frontmatter
        n = cure_missing_frontmatter(report)
        cure_stats["missing_frontmatter"] = n

        # Priority 2.5: Fix raw sources missing frontmatter
        n = cure_raw_sources_frontmatter(report)
        cure_stats["raw_sources_frontmatter"] = n

        # Priority 3: Fix SHA256 drift
        n = cure_sha256_drift(report)
        cure_stats["sha256_drift"] = n

        # Priority 4: Fix missing fields
        n = cure_missing_fields(report)
        cure_stats["missing_fields"] = n

        # Priority 5: Fix missing sources
        n = cure_missing_sources(report)
        cure_stats["missing_sources"] = n

        # Priority 6: Fix missing index entries
        n = cure_missing_index_entries(report)
        cure_stats["missing_index_entries"] = n

        # Priority 7: Sync APPROVED_TAGS
        n = cure_approved_tags_drift(report)
        cure_stats["approved_tags_sync"] = n

    # Phase 3: Re-diagnose
    print(f"\n🔍 Фаза 3: Повторна діагностика (після лікування)...")
    report2 = diagnose()
    print(f"\n📊 Результати після лікування:")
    print(f"   {report2.severity_summary()}")

    # Phase 4: Final status report
    # Collect remaining error/warn details
    error_details = [f"[{i['layer']}] {i['path']}: {i['message']}" for i in report2.get_all_issues() if i["severity"] == "ERROR"]
    warn_details = [f"[{i['layer']}] {i['path']}: {i['message']}" for i in report2.get_all_issues() if i["severity"] == "WARN"]

    # Generate standardized report
    report_str = format_wiki_doctor_report(
        component="wiki_doctor",
        before_errors=report.summary["ERROR"],
        before_warns=report.summary["WARN"],
        before_info=report.summary["INFO"],
        before_auto_fixable=report.summary["auto_fixable"],
        after_errors=report2.summary["ERROR"],
        after_warns=report2.summary["WARN"],
        after_info=report2.summary["INFO"],
        after_auto_fixable=report2.summary["auto_fixable"],
        fixes_applied=sum(cure_stats.values()),
        error_details=error_details if error_details else None,
        warn_details=warn_details if warn_details else None,
    )

    print()
    print(report_str)

    # Save report (JSON always saved, even in dry-run)
    report_path = ROOT / "outputs" / "doctor-report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_data = {
        "timestamp": report2.timestamp,
        "mode": "dry-run" if dry_run else "live",
        "before": report.summary,
        "after": report2.summary,
        "cure_stats": cure_stats,
        "remaining_issues": [
            {"layer": i["layer"], "severity": i["severity"], "path": i["path"], "message": i["message"]}
            for i in report2.get_all_issues()
        ],
    }
    report_path.write_text(json.dumps(report_data, indent=2, ensure_ascii=False), encoding="utf-8")

    # Log
    log_entry = (
        f"Wiki Doctor ({mode_label}) — до: {report.severity_summary()}, після: {report2.severity_summary()}, "
        f"виправлень: {sum(cure_stats.values())}"
    )
    append_to_log(LOG_FILE, "wiki_doctor", log_entry)

    return report2


# ---------------------------------------------------------------------------
# CLI ENTRY POINT
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Wiki Doctor — діагностика та лікування LLM Wiki")
    parser.add_argument(
        "mode",
        nargs="?",
        choices=["diagnose", "cure"],
        default="cure",
        help="diagnose = тільки діагностика; cure = діагностика + лікування (за замовчуванням)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Показати що буде виправлено без зміни файлів",
    )
    args = parser.parse_args()

    if args.mode == "diagnose":
        report = diagnose()
        print(f"\n📊 Результати: {report.severity_summary()}")
        for issue in report.get_all_issues():
            print(f"  [{issue['severity']}] {issue['path']}: {issue['message']}")
    else:
        diagnose_and_cure(dry_run=args.dry_run)
