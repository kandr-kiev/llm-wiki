#!/usr/bin/env python3
"""Final sync: SCHEMA.md -> approved_tags.json (no OOM)."""
import re, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "SCHEMA.md"
TAGS_JSON = ROOT / "tools" / "approved_tags.json"

SKIP = {
    "type","title","description","tags","timestamp","resource",
    "category","confidence","contested","links","sources","status",
    "from taxonomy below","Тег","Tag",
    "_archive/","comparison","contested: true",
}

content = SCHEMA.read_text(encoding="utf-8")
lines = content.split("\n")
in_taxonomy = False
tags = set()

for line in lines:
    if line.startswith("## Tag Taxonomy"):
        in_taxonomy = True
        continue
    if in_taxonomy:
        if line.startswith("## "):
            break
        for m in re.finditer(r"\x60([^\x60]+)\x60", line):
            t = m.group(1).strip()
            if t not in SKIP and t:
                tags.add(t)

TAGS_JSON.write_text(json.dumps(sorted(tags), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"✅ Synced {len(tags)} tags from SCHEMA.md to approved_tags.json")
