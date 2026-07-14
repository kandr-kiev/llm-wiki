#!/usr/bin/env python3
"""
conftest.py — pytest fixtures для Wiki Doctor тестів.

Створює тимчасову імітацію файлової системи LLM Wiki:
  tmpdir/
    SCHEMA.md
    wiki/
      index.md
      concepts/
      entities/
      playbooks/
    raw/
      articles/
    tools/
      wiki_doctor.py (замінює оригінал)
      utils.py (замінює оригінал)
      standard_report.py (замінює оригінал)

Всі тестування ізолювані — жодна зміна не потрапить у реальний wiki.
"""

import hashlib
import importlib.util
import shutil
import sys
from pathlib import Path

import pytest


def slugify(text):
    """Convert text to URL-friendly slug."""
    import re
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def _split_frontmatter(text):
    """Split markdown into frontmatter and body."""
    if not text.startswith('---'):
        return None, text
    parts = text.split('---', 2)
    if len(parts) < 3:
        return None, text
    fm = parts[1].strip()
    body = parts[2].lstrip('\n')
    return fm, body


def parse_simple_yaml(fm):
    """Parse simple YAML frontmatter into dict."""
    data = {}
    current_key = None
    current_list = None
    for line in fm.split('\n'):
        line = line.rstrip()
        if not line or line.strip().startswith('#'):
            continue
        if line.startswith('  - ') or line.startswith('- '):
            if current_key and current_list is not None:
                val = line.lstrip('- ').strip()
                current_list.append(val)
            continue
        if ':' in line:
            if current_key and current_list is not None:
                data[current_key] = current_list
            key = line.split(':')[0].strip()
            val = ':'.join(line.split(':')[1:]).strip()
            current_key = key
            if val == '':
                current_list = []
                data[key] = []
            elif val.startswith('[') and val.endswith(']'):
                items = val[1:-1].split(',')
                data[key] = [i.strip().strip('"').strip("'") for i in items if i.strip()]
                current_list = None
            elif val.startswith('['):
                items = val[1:].strip().split(',')
                data[key] = [i.strip().strip('"').strip("'") for i in items if i.strip()]
                current_list = data[key]
            else:
                current_list = None
                data[key] = val
    if current_key and current_list is not None:
        data[current_key] = current_list
    return data


def _create_minimal_utils(wiki_root):
    """Create a minimal utils.py for tests."""
    import shutil
    src = Path("/workspace/llm-wiki/tools/utils.py")
    dst = wiki_root / "tools" / "utils.py"
    shutil.copy2(src, dst)
    return dst


def _create_minimal_standard_report(wiki_root):
    """Create a minimal standard_report.py for tests."""
    content = '''#!/usr/bin/env python3
"""Minimal standard_report for tests."""


def format_wiki_doctor_report(component, before_errors, before_warns, before_info,
                               before_auto_fixable, after_errors, after_warns,
                               after_info, after_auto_fixable, fixes_applied,
                               error_details=None, warn_details=None):
    lines = [
        f"## Wiki Doctor Report",
        f"",
        f"| Metric | Before | After |",
        f"|--------|--------|-------|",
        f"| ERROR | {before_errors} | {after_errors} |",
        f"| WARN | {before_warns} | {after_warns} |",
        f"| INFO | {before_info} | {after_info} |",
        f"| Auto-fixable | {before_auto_fixable} | {after_auto_fixable} |",
        f"| Fixes applied | — | {fixes_applied} |",
    ]
    if error_details:
        lines.append("")
        lines.append("### Errors")
        for e in error_details:
            lines.append(f"- {e}")
    if warn_details:
        lines.append("")
        lines.append("### Warnings")
        for w in warn_details:
            lines.append(f"- {w}")
    return "\\n".join(lines)
'''
    dst = wiki_root / "tools" / "standard_report.py"
    dst.write_text(content, encoding='utf-8')
    return dst


@pytest.fixture
def wiki_root(tmp_path):
    """Create a temporary LLM Wiki structure."""
    root = tmp_path

    # SCHEMA.md
    schema = root / "SCHEMA.md"
    schema.write_text("""---
type: reference
title: Wiki Schema
---
# Wiki Schema

## Tag Taxonomy

- ai — artificial intelligence
- machine-learning — ML
- deep-learning — DL
- nlp — natural language processing
- transformers — transformer models
- rag — retrieval augmented generation
- llm — large language models
- architecture — system architecture
- evaluation — model evaluation
- benchmark — benchmarks
- training — model training
- inference — model inference
- quantization — model quantization
- fine-tuning — fine-tuning
- security — security
- ethics — AI ethics
- research — research papers
- tutorial — tutorials
- guide — guides
- comparison — comparisons
- playbook — playbooks
- synthesis — synthesis
- tool — tools
- framework — frameworks
- library — libraries
- api — APIs
- deployment — deployment
- optimization — optimization
- data — data
- dataset — datasets
- prompt-engineering — prompt engineering
- agent — AI agents
- memory — memory systems
- retrieval — retrieval
- embedding — embeddings
- vector-database — vector databases
- gpt — GPT models
- llama — LLaMA models
- claude — Claude models
- open-source — open source
- closed-source — closed source
- commercial — commercial
- academic — academic
- pytorch — PyTorch
- tensorflow — TensorFlow
- cuda — CUDA
- gpu — GPU
- cloud — cloud
- devops — DevOps
- mlops — MLOps
""", encoding='utf-8')

    # wiki/
    wiki_dir = root / "wiki"
    wiki_dir.mkdir()

    # wiki/index.md
    index = wiki_dir / "index.md"
    index.write_text("""---
type: reference
title: Wiki Index
---
# Wiki Index

Last updated: 2026-07-13

Total pages: 0

### Concepts

### Entities

### Playbooks

### Comparisons

### Synthesis

### Queries

### References

*Auto-generated*
""", encoding='utf-8')

    # wiki subdirectories
    for subdir in ["concepts", "entities", "playbooks", "comparisons", "templates"]:
        (wiki_dir / subdir).mkdir()

    # raw/articles/
    (root / "raw" / "articles").mkdir(parents=True)

    # tools/
    tools_dir = root / "tools"
    tools_dir.mkdir()
    _create_minimal_utils(root)
    _create_minimal_standard_report(root)

    # Copy wiki_doctor.py
    src_doctor = Path("/workspace/llm-wiki/tools/wiki_doctor.py")
    if src_doctor.exists():
        shutil.copy2(src_doctor, tools_dir / "wiki_doctor.py")

    return root


@pytest.fixture
def wiki_structure(wiki_root):
    """Set up wiki_doctor globals to point to tmp_path, and import wiki_doctor."""
    import importlib.util
    import sys

    doctor_path = wiki_root / "tools" / "wiki_doctor.py"
    spec = importlib.util.spec_from_file_location("wiki_doctor", doctor_path)
    module = importlib.util.module_from_spec(spec)

    sys.path.insert(0, str(wiki_root / "tools"))

    spec.loader.exec_module(module)

    # Patch ROOT and all paths
    module.ROOT = wiki_root
    module.WIKI_DIR = wiki_root / "wiki"
    module.RAW_DIR = wiki_root / "raw"
    module.TOOLS_DIR = wiki_root / "tools"
    module.INDEX_FILE = wiki_root / "wiki" / "index.md"
    module.LOG_FILE = wiki_root / "log.md"
    module.SCHEMA_FILE = wiki_root / "SCHEMA.md"

    return module


@pytest.fixture
def sample_concept_page(wiki_root):
    """Create a sample concept page."""
    page = wiki_root / "wiki" / "concepts" / "transformer-architecture.md"
    page.write_text("""---
type: concept
title: Transformer Architecture
description: Attention-based neural network architecture
tags: [transformers, architecture, deep-learning]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Transformer Architecture

The transformer is a neural network architecture based on self-attention.
""", encoding='utf-8')
    return page


@pytest.fixture
def sample_entity_page(wiki_root):
    """Create a sample entity page."""
    page = wiki_root / "wiki" / "entities" / "openai.md"
    page.write_text("""---
type: entity
title: OpenAI
description: AI research company
tags: [ai, open-source, commercial]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# OpenAI

OpenAI is an AI research and deployment company.
""", encoding='utf-8')
    return page


@pytest.fixture
def sample_raw_source(wiki_root):
    """Create a sample raw source file with SHA256."""
    raw = wiki_root / "raw" / "articles" / "test-article.md"
    raw.write_text("""---
type: raw
title: Test Article
sha256: placeholder
---
# Test Article

This is a test article for wiki doctor testing.
""", encoding='utf-8')
    # Fix the sha256 to match
    actual = hashlib.sha256("# Test Article\n\nThis is a test article for wiki doctor testing.\n".encode('utf-8')).hexdigest()
    text = raw.read_text(encoding='utf-8')
    text = text.replace('sha256: placeholder', f'sha256: {actual}')
    raw.write_text(text, encoding='utf-8')
    return raw


@pytest.fixture
def broken_wiki_pages(wiki_root):
    """Create pages with known problems for testing."""
    # Page with broken wikilink
    page1 = wiki_root / "wiki" / "concepts" / "test-page-with-broken-link.md"
    page1.write_text("""---
type: concept
title: Test Page
description: Has broken wikilink
tags: [test]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Test Page

See [[comparisons/nonexistent]] for details.
""", encoding='utf-8')

    # Page missing frontmatter
    page2 = wiki_root / "wiki" / "concepts" / "no-frontmatter.md"
    page2.write_text("""# No Frontmatter

This page has no frontmatter at all.
""", encoding='utf-8')

    # Page missing fields
    page3 = wiki_root / "wiki" / "concepts" / "missing-fields.md"
    page3.write_text("""---
type: concept
title: Missing Fields
---
# Missing Fields

This page is missing description, tags, sources, etc.
""", encoding='utf-8')

    # Page with missing source file
    page4 = wiki_root / "wiki" / "concepts" / "missing-source.md"
    page4.write_text("""---
type: concept
title: Missing Source
description: Has missing source
tags: [test]
sources: [raw/articles/nonexistent.md]
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Missing Source

This page references a non-existent source.
""", encoding='utf-8')

    # Page not in index
    page5 = wiki_root / "wiki" / "concepts" / "not-in-index.md"
    page5.write_text("""---
type: concept
title: Not In Index
description: Missing from index.md
tags: [test]
sources: []
confidence: high
links: []
created: 2026-07-13
updated: 2026-07-13
---
# Not In Index

This page is not referenced in wiki/index.md.
""", encoding='utf-8')

    return [page1, page2, page3, page4, page5]


@pytest.fixture
def drift_raw_source(wiki_root):
    """Create a raw source with SHA256 drift (content changed, hash not updated)."""
    raw = wiki_root / "raw" / "articles" / "drifted-article.md"
    content = """---
type: raw
title: Drifted Article
sha256: deadbeef1234567890abcdef12345678deadbeef1234567890abcdef12345678
---
# Drifted Article

This content was modified but the SHA256 was not updated.
"""
    raw.write_text(content, encoding='utf-8')
    return raw
