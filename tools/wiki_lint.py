#!/usr/bin/env python3
"""Structural lint for Local LLM Wiki."""
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"type", "title", "description", "created", "updated", "tags", "sources", "confidence", "links"}
RESERVED_NAMES = {"README.md"}

from utils import split_frontmatter, parse_simple_yaml, APPROVED_TAGS


def slug_for(path):
    return path.stem


def main():
    issues = []
    wiki_pages = [p for p in (ROOT / "wiki").rglob("*.md") if p.name not in RESERVED_NAMES and p.parent.name not in ("templates", "comparisons")]
    slugs = {slug_for(p): p for p in wiki_pages}
    # Add comparison slugs for wikilink validation (comparisons excluded from wiki_pages lint but valid link targets)
    comparison_slugs = {p.stem for p in (ROOT / "wiki" / "comparisons").rglob("*.md")}
    index_text = (ROOT / "wiki" / "index.md").read_text(encoding="utf-8") if (ROOT / "wiki" / "index.md").exists() else ""

    for page in wiki_pages:
        text = page.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        rel = page.relative_to(ROOT)
        if fm is None:
            issues.append(("ERROR", str(rel), "missing or malformed frontmatter"))
            continue
        data = parse_simple_yaml(fm)
        missing = sorted(REQUIRED - set(data))
        if missing:
            issues.append(("ERROR", str(rel), "missing fields: " + ", ".join(missing)))
        for tag in data.get("tags", []):
            if tag not in APPROVED_TAGS:
                issues.append(("WARN", str(rel), f"unapproved tag: {tag}"))
        if str(rel) not in index_text and rel != Path("wiki/index.md"):
            issues.append(("ERROR", str(rel), "page missing from index.md"))
        if len(text.splitlines()) > 200:
            issues.append(("WARN", str(rel), "page over 200 lines"))
        if str(data.get("confidence", "")).lower() == "low":
            issues.append(("INFO", str(rel), "low confidence page"))
        if data.get("contested") is True:
            issues.append(("INFO", str(rel), "contested page"))
        # Strip HTML before checking wikilinks (prevents false positives from Astro JSON props)
        # NOTE: integrator may produce truncated files where astro-island tags are never closed.
        # Handle both complete tags (astro-island ... />) and truncated tags (astro-island ... EOF).
        # Strategy: remove everything from <astro-island to end of body, since it's never valid markdown.
        clean_body = re.sub(r'<astro-island\b.*', ' ', body, flags=re.DOTALL)
        # Then strip remaining HTML tags
        clean_body = re.sub(r'<[^>]+>', ' ', clean_body)
        for link in re.findall(r"\[\[([^\]|#]+)", clean_body):
            # Extract stem from link (handles both "slug" and "dir/slug" formats)
            link_stem = link.split('/')[-1]
            if link_stem not in slugs and link_stem not in comparison_slugs:
                issues.append(("ERROR", str(rel), f"broken wikilink: [[{link}]]"))
        # Check that source files actually exist
        sources = data.get("sources", [])
        if isinstance(sources, str):
            sources = [sources]
        for src in sources:
            src_path = ROOT / src
            if not src_path.is_file():
                issues.append(("ERROR", str(rel), f"source file missing: {src}"))

    for raw in (ROOT / "raw").rglob("*.md"):
        if raw.name == "README.md":
            continue
        text = raw.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        rel = raw.relative_to(ROOT)
        if fm is None:
            issues.append(("ERROR", str(rel), "raw source missing frontmatter"))
            continue
        data = parse_simple_yaml(fm)
        expected = data.get("sha256")
        if expected is None:
            continue  # no sha256 field — not a drift, just unindexed
        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if expected != actual:
            issues.append(("ERROR", str(rel), "sha256 drift"))

    out = ROOT / "outputs" / "lint-report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Local LLM Wiki Lint Report", "", f"Pages checked: {len(wiki_pages)}", f"Issues: {len(issues)}", ""]
    if issues:
        for severity, path, msg in issues:
            lines.append(f"- **{severity}** `{path}` — {msg}")
    else:
        lines.append("No structural issues found.")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    if any(sev == "ERROR" for sev, _, _ in issues):
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
