#!/usr/bin/env python3
"""tag_sync.py — синхронізація APPROVED_TAGS між SCHEMA.md та tools/approved_tags.json.

SCHEMA.md (root) — єдине джерело істини для тегів.
tools/approved_tags.json — JSON-файл зApproved Tags (завантажується tools/utils.py).

Usage:
    python3 tools/tag_sync.py --check    # перевірка без змін
    python3 tools/tag_sync.py --apply    # merge: об'єднати всі теги, оновити обидва файли
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "SCHEMA.md"
TAGS_JSON_PATH = ROOT / "tools" / "approved_tags.json"

_SKIP_TAGS = {
    "type", "title", "description", "tags", "timestamp", "resource",
    "category", "confidence", "contested", "links", "sources", "status",
    "from taxonomy below", "Тег", "Tag",
    # OKF field values that get picked up by tag parser
    "_archive/", "comparison", "contested: true",
}


def extract_tags_from_schema(schema_path: Path) -> set:
    """Extract all tags from the Tag Taxonomy section of SCHEMA.md."""
    content = schema_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    taxonomy_lines = []
    in_taxonomy = False
    for line in lines:
        if line.startswith("## Tag Taxonomy"):
            in_taxonomy = True
            continue
        if in_taxonomy:
            if line.startswith("## "):
                break
            taxonomy_lines.append(line)

    taxonomy = "\n".join(taxonomy_lines)
    tags = set()
    # Match ALL backtick-quoted strings in table rows (including last column without trailing |)
    for m in re.finditer(r"\x60([^\x60]+)\x60", taxonomy):
        tag = m.group(1).strip()
        if tag not in _SKIP_TAGS and tag:
            tags.add(tag)
    return tags


def extract_tags_from_json(json_path: Path) -> set:
    """Extract APPROVED_TAGS from approved_tags.json."""
    if not json_path.exists():
        return set()
    return set(json.loads(json_path.read_text(encoding="utf-8")))


def write_tags_to_json(json_path: Path, tags: set) -> bool:
    """Write sorted tags list to approved_tags.json."""
    sorted_tags = sorted(tags)
    json_path.write_text(json.dumps(sorted_tags, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return True


def update_schema_tags(schema_path: Path, merged: set) -> bool:
    """Append missing tags to Extended Tags section in SCHEMA.md."""
    content = schema_path.read_text(encoding="utf-8")
    schema_tags = extract_tags_from_schema(schema_path)
    missing = sorted(merged - schema_tags)

    if not missing:
        return True

    # Find the Tag Taxonomy section
    taxonomy_match = re.search(
        r"(## Tag Taxonomy.*?)(### Page Thresholds)",
        content,
        re.DOTALL,
    )
    if not taxonomy_match:
        print("ERROR: Cannot find Tag Taxonomy section in SCHEMA.md")
        return False

    taxonomy_text = taxonomy_match.group(1)

    # Find the LAST data row (a line with | `...` | ... | pattern)
    all_rows = list(re.finditer(r"^\|.*\x60[^\x60]+\x60.*\|$", taxonomy_text, re.MULTILINE))
    if not all_rows:
        print("ERROR: No table data rows found in Tag Taxonomy section")
        print("DEBUG: First 200 chars of taxonomy:")
        print(repr(taxonomy_text[:200]))
        return False

    last_row = all_rows[-1]
    insert_pos = taxonomy_match.start(1) + last_row.end()

    # Build new table rows (4 per row)
    new_rows = []
    for i in range(0, len(missing), 4):
        row_tags = missing[i : i + 4]
        cells = " | ".join(f"`{t}`" for t in row_tags)
        while len(row_tags) < 4:
            cells += " | "
        new_rows.append(f"| {cells} |")

    new_section = "\n" + "\n".join(new_rows) + "\n"

    before = content[:insert_pos]
    after = content[insert_pos:]
    new_content = before + new_section + after

    schema_path.write_text(new_content, encoding="utf-8")
    print(f"Added {len(missing)} tags to SCHEMA.md Extended Tags section")
    return True


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("--check", "--apply"):
        print("Usage: python3 tools/tag_sync.py [--check|--apply]")
        sys.exit(1)

    apply = sys.argv[1] == "--apply"

    if not SCHEMA_PATH.exists():
        print(f"ERROR: {SCHEMA_PATH} not found (expected in root)")
        sys.exit(1)

    schema_tags = extract_tags_from_schema(SCHEMA_PATH)
    json_tags = extract_tags_from_json(TAGS_JSON_PATH)

    only_in_schema = schema_tags - json_tags
    only_in_json = json_tags - schema_tags
    common = schema_tags & json_tags

    print(f"SCHEMA.md tags: {len(schema_tags)}")
    print(f"approved_tags.json: {len(json_tags)}")
    print(f"Common: {len(common)}")

    if only_in_schema:
        print(f"\n⚠️  Tags in SCHEMA.md but NOT in approved_tags.json ({len(only_in_schema)}):")
        for tag in sorted(only_in_schema):
            print(f"   + {tag}")

    if only_in_json:
        print(f"\n⚠️  Tags in approved_tags.json but NOT in SCHEMA.md ({len(only_in_json)}):")
        for tag in sorted(only_in_json):
            print(f"   - {tag}")

    if not only_in_schema and not only_in_json:
        print("\n✅ APPROVED_TAGS fully synchronized with SCHEMA.md")
        return

    if apply:
        merged = schema_tags | json_tags

        if only_in_json:
            print(f"\n→ Adding {len(only_in_json)} tags to SCHEMA.md")
            if not update_schema_tags(SCHEMA_PATH, merged):
                print("❌ Failed to update SCHEMA.md")
                sys.exit(1)

        if only_in_schema:
            print(f"→ Adding {len(only_in_schema)} tags to approved_tags.json")

        if write_tags_to_json(TAGS_JSON_PATH, merged):
            print(f"\n✅ Updated approved_tags.json with {len(merged)} tags")
            print(f"✅ Updated SCHEMA.md with {len(only_in_json)} new tags")
        else:
            print("\n❌ Failed to update approved_tags.json")
            sys.exit(1)
    else:
        print(f"\nRun with --apply to synchronize both files.")
        sys.exit(1)


if __name__ == "__main__":
    main()
