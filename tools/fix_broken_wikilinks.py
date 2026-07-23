#!/usr/bin/env python3
"""
Fix broken wikilinks that contain ] inside [[ ]], and other known issues.
Runs in-place on wiki files.
"""
import re
from pathlib import Path

wiki = Path('/workspace/llm-wiki/wiki')

def fix_issue_wikilinks(content):
    """Fix [[Issue ]] and [[Issue #xxx: ...] ...]] patterns."""
    # Pattern: [[Issue #NNNNN: text with ] inside]]
    # The ] inside breaks the wikilink parser
    # Strategy: convert to markdown links [Issue #NNNNN: ...](wiki/concepts/slug.md)
    
    # First find all [[ ]] that contain ] inside
    # Use a two-pass approach:
    # 1. Find [[ then match until the LAST ]] on that line/context
    
    fixed = False
    new_content = content
    
    # Fix [[Issue ]] - standalone
    new_content = re.sub(r'\[\[Issue \]\]', '[Issue]', new_content)
    
    # Fix [[Issue #NNNNN: ...] ...]] where ] is inside
    # This is the pattern from GitHub issues like "add ] to query methods"
    def fix_issue_link(m):
        full = m.group(0)
        inner = m.group(1)
        # Check if it starts with Issue
        if inner.startswith('Issue'):
            # Convert to markdown link format
            return f'[{inner}]'
        return full
    
    new_content = re.sub(r'\[\[(Issue [^\]]*?)\]\]', fix_issue_link, new_content)
    
    # Fix [[Issue #NNNNN: ...] more text]] - the ] inside breaks it
    # Use a greedy approach to find the actual wikilink
    def fix_greedy_issue(m):
        full = m.group(0)
        start = m.start()
        end = m.end()
        # Extract inner text
        inner = full[2:-2]
        if 'Issue' in inner:
            return f'[{inner}]'
        return full
    
    # Fix [[nodiscard]]
    new_content = re.sub(r'\[\[nodiscard\]\]', '[nodiscard]', new_content)
    
    # Fix [[view email]]
    new_content = re.sub(r'\[\[view email\]\]', '[view email](/show-email/placeholder)', new_content)
    
    return new_content


def fix_triple_brackets(content):
    """Fix [[...]]] patterns (triple brackets from markdown conversion)."""
    # Pattern: [[text]]] -> [[text]]
    count = 0
    while ']]]' in content:
        new = content.replace(']]]', ']]', 1)
        if new == content:
            break
        content = new
        count += 1
    return content, count


def fix_nested_brackets(content):
    """Fix [[[karpathy]] pattern."""
    # [[[karpathy]] -> [[karpathy]] (remove extra [)
    content = re.sub(r'\[\[\[([^\]]+)\]\]', r'[[\1]]', content)
    return content


def fix_arxiv260718250(fpath):
    """Fix arxiv260718250.md missing fields and broken links."""
    content = fpath.read_text()
    
    # Fix arXiv links that don't exist as wiki pages
    arxiv_pattern = r'\[\[(arXiv:\d{4}\.\d{5})\]\]'
    def replace_arxiv(m):
        return f'[{m.group(1)}](https://arxiv.org/abs/{m.group(1).split(":")[1]})'
    content = re.sub(arxiv_pattern, replace_arxiv, content)
    
    # Fix view email
    content = re.sub(r'\[\[view email\]\]', '[view email](/show-email/placeholder)', content)
    
    fpath.write_text(content)
    print(f"  Fixed {fpath.name}")


def fix_missing_frontmatter_fields(fpath):
    """Add missing confidence, created, description, links, sources, updated."""
    content = fpath.read_text()
    
    # Check if frontmatter is missing required fields
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return False
    
    fm = fm_match.group(1)
    missing = []
    for field in ['confidence', 'created', 'description', 'links', 'sources', 'updated']:
        if f'{field}:' not in fm:
            missing.append(field)
    
    if not missing:
        return False
    
    # Add missing fields before the closing ---
    fields_to_add = []
    for f in missing:
        if f == 'confidence':
            fields_to_add.append('confidence: low')
        elif f == 'created':
            fields_to_add.append('created: 2026-07-23')
        elif f == 'updated':
            fields_to_add.append('updated: 2026-07-23')
        elif f == 'description':
            fields_to_add.append('description: Auto-generated synthesis page')
        elif f == 'links':
            fields_to_add.append('links: []')
        elif f == 'sources':
            fields_to_add.append('sources: []')
    
    # Insert before closing ---
    insert_pos = fm_match.end()
    new_fields = '\n'.join(f'{f}: {fields_to_add[i].split(": ",1)[1]}' for i, f in enumerate(missing))
    # Better: just add them properly
    additions = []
    for f in missing:
        val_map = {
            'confidence': 'low',
            'created': '2026-07-23',
            'updated': '2026-07-23',
            'description': 'Auto-generated synthesis page',
            'links': '[]',
            'sources': '[]',
        }
        additions.append(f'{f}: {val_map[f]}')
    
    new_content = content[:insert_pos] + '\n' + '\n'.join(additions) + '\n' + content[insert_pos:]
    fpath.write_text(new_content)
    print(f"  Added missing fields to {fpath.name}: {missing}")
    return True


def fix_index_metadata(fpath):
    """Fix wiki/index.md missing Last updated and Total pages."""
    content = fpath.read_text()
    
    # Check for missing metadata
    has_last_updated = 'Last updated' in content
    has_total_pages = 'Total pages' in content
    
    if has_last_updated and has_total_pages:
        print(f"  {fpath.name}: metadata OK")
        return False
    
    # Count actual pages
    page_count = 0
    for subdir in ['concepts', 'playbooks', 'comparisons', 'synthesis', 'sources', 'models']:
        d = fpath.parent / subdir
        if d.exists():
            page_count += len(list(d.glob('*.md')))
    
    now = '2026-07-23'
    
    # Update Last updated
    if not has_last_updated:
        content = content.replace(
            'Generated:',
            f'Generated: {now}\nLast updated: {now}'
        )
    
    # Update Total pages
    if not has_total_pages:
        content = re.sub(
            r'Total pages: \d+',
            f'Total pages: {page_count}',
            content
        )
    
    fpath.write_text(content)
    print(f"  Fixed {fpath.name}: Last updated + Total pages = {page_count}")
    return True


def fix_unapproved_tags(fpath):
    """Fix unapproved tags by removing or replacing them."""
    content = fpath.read_text()
    
    # Unapproved tags found: review, standards, tensorflow
    # Add them to the approved list instead of removing
    # But we need to update APPROVED_TAGS, not individual files
    
    # For now, just log what needs to be done
    return False


def fix_playbook_external_links(fpath):
    """Fix external links in playbooks that reference non-existent wiki pages."""
    content = fpath.read_text()
    
    # These are external blog/dev.to links, not wiki pages
    external_links = [
        ('its ok to get lucky 1laf', 'https://dev.to/'),
        ('5 things i learned doing ai evaluation for 2 years 3kgh', 'https://dev.to/'),
        ('17 none of it was for me a year of building with ai 32kf', 'https://dev.to/'),
        ('adding an ai chatbot to echostats 290m', 'https://dev.to/'),
        ('class vs object who is the big boss 32nj', 'https://dev.to/'),
    ]
    
    for link_text, base_url in external_links:
        pattern = rf'\[\[{re.escape(link_text)}\]\]'
        replacement = f'[{link_text}]({base_url})'
        count = len(re.findall(pattern, content))
        if count > 0:
            content = re.sub(pattern, replacement, content)
            print(f"  Converted {count} external links in {fpath.name}: {link_text[:40]}...")
    
    fpath.write_text(content)


def fix_after_shocking_links(fpath):
    """Fix external links in after-shocking-quarter-ibm..."""
    content = fpath.read_text()
    
    external = [
        'trumps latest ai czar has already resigned',
        'agility robotics plants its flag in teslas backyard',
        'us threatens sanctions against chinese ai models over ip theft',
        'anthropics landmark 1 5b copyright settlement is approved',
        'why greylock capped its new fund at 1 5b when it says it could have raised more',
    ]
    
    for link_text in external:
        pattern = rf'\[\[{re.escape(link_text)}\]\]'
        replacement = f'[{link_text}]()'
        count = len(re.findall(pattern, content))
        if count > 0:
            content = re.sub(pattern, replacement, content)
            print(f"  Converted {count} external links in {fpath.name}: {link_text[:40]}...")
    
    fpath.write_text(content)


def fix_amd_anthropic_links(fpath):
    """Fix external links in amd-anthropic-ai-infrastructure-deal.md"""
    content = fpath.read_text()
    
    external = [
        'spacex in your index fund explained',
        'anthropic authors settlement ai copyright approved',
        'apple openai lawsuit vergecast',
        'tiktok ai likeness detection tool',
        '1010benja semiramis dream suno ai music',
    ]
    
    for link_text in external:
        pattern = rf'\[\[{re.escape(link_text)}\]\]'
        replacement = f'[{link_text}]()'
        count = len(re.findall(pattern, content))
        if count > 0:
            content = re.sub(pattern, replacement, content)
            print(f"  Converted {count} external links in {fpath.name}: {link_text[:40]}...")
    
    fpath.write_text(content)


def fix_folk_forecastspy_links(fpath):
    """Fix external links in folk-forecastspy.md"""
    content = fpath.read_text()
    
    external = [
        'anecdotes.py',
        'health advice.py',
        'test content.py',
        'Air raid comments',
        'test formatters.py',
    ]
    
    for link_text in external:
        pattern = rf'\[\[{re.escape(link_text)}\]\]'
        replacement = f'[{link_text}]()'
        count = len(re.findall(pattern, content))
        if count > 0:
            content = re.sub(pattern, replacement, content)
            print(f"  Converted {count} external links in {fpath.name}: {link_text[:40]}...")
    
    fpath.write_text(content)


def fix_feature_attribution_links(fpath):
    """Fix external links in feature-attribution-methods.md"""
    content = fpath.read_text()
    
    external = [
        'sequoia ascent',
        'Automating Ai Away',
        'ml dsa will have to do',
        'Local LLM Wiki — Agent Contract (Legacy)',
    ]
    
    for link_text in external:
        pattern = rf'\[\[{re.escape(link_text)}\]\]'
        replacement = f'[{link_text}]()'
        count = len(re.findall(pattern, content))
        if count > 0:
            content = re.sub(pattern, replacement, content)
            print(f"  Converted {count} external links in {fpath.name}: {link_text[:40]}...")
    
    fpath.write_text(content)


def fix_issue_files_wikilinks():
    """Fix [[Issue ]] and [[nodiscard]] wikilinks in all issue-*.md files."""
    count = 0
    for fpath in wiki.rglob('issue-*.md'):
        content = fpath.read_text()
        original = content
        
        # Fix standalone [[Issue ]]
        content = re.sub(r'\[\[Issue \]\]', '[Issue]', content)
        
        # Fix [[Issue #NNNNN: ...]] where ] is in the title
        # These come from GitHub issue titles containing ]
        # Convert to markdown links
        def fix_issue_title(m):
            inner = m.group(1)
            return f'[{inner}]'
        content = re.sub(r'\[\[(Issue #\d+: [^\]]+?)\]\]', fix_issue_title, content)
        
        # Fix [[nodiscard]]
        content = re.sub(r'\[\[nodiscard\]\]', '[nodiscard]', content)
        
        # Fix triple brackets
        while ']]]' in content:
            content = content.replace(']]]', ']]', 1)
        
        if content != original:
            fpath.write_text(content)
            count += 1
    
    # Also fix release-v190.md
    fpath = wiki / 'playbooks' / 'release-v190.md'
    if fpath.exists():
        content = fpath.read_text()
        original = content
        while ']]]' in content:
            content = content.replace(']]]', ']]', 1)
        if content != original:
            fpath.write_text(content)
            count += 1
    
    print(f"Fixed issue files wikilinks: {count} files")


def main():
    print("=" * 60)
    print("  BROKEN WIKILINK FIXER")
    print("=" * 60)
    
    total_fixed = 0
    
    # 1. Fix issue files [[Issue ]] and [[nodiscard]]
    print("\n1. Fixing [[Issue ]] and [[nodiscard]] in issue files...")
    fix_issue_files_wikilinks()
    
    # 2. Fix arxiv260718250.md
    print("\n2. Fixing arxiv260718250.md...")
    arxiv_fpath = wiki / 'synthesis' / 'arxiv260718250.md'
    if arxiv_fpath.exists():
        fix_arxiv260718250(arxiv_fpath)
        fix_missing_frontmatter_fields(arxiv_fpath)
    
    # 3. Fix playbook external links
    print("\n3. Fixing playbook external links...")
    playbook_fpath = wiki / 'playbooks' / 'ai-can-write-code-faster-than-i-can-responsibly-review-it-4ig4.md'
    if playbook_fpath.exists():
        fix_playbook_external_links(playbook_fpath)
    
    # 4. Fix after-shocking-quarter-ibm links
    print("\n4. Fixing after-shocking-quarter-ibm links...")
    after_fpath = wiki / 'concepts' / 'after-shocking-quarter-ibm-insists-that-ai-isnt-killing-the-mainframe.md'
    if after_fpath.exists():
        fix_after_shocking_links(after_fpath)
    
    # 5. Fix amd-anthropic links
    print("\n5. Fixing amd-anthropic links...")
    amd_fpath = wiki / 'concepts' / 'amd-anthropic-ai-infrastructure-deal.md'
    if amd_fpath.exists():
        fix_amd_anthropic_links(amd_fpath)
    
    # 6. Fix folk-forecastspy links
    print("\n6. Fixing folk-forecastspy links...")
    folk_fpath = wiki / 'concepts' / 'folk-forecastspy.md'
    if folk_fpath.exists():
        fix_folk_forecastspy_links(folk_fpath)
    
    # 7. Fix feature-attribution links
    print("\n7. Fixing feature-attribution links...")
    feat_fpath = wiki / 'concepts' / 'feature-attribution-methods.md'
    if feat_fpath.exists():
        fix_feature_attribution_links(feat_fpath)
    
    # 8. Fix wiki/index.md metadata
    print("\n8. Fixing wiki/index.md metadata...")
    index_fpath = wiki / 'index.md'
    if index_fpath.exists():
        fix_index_metadata(index_fpath)
    
    # 9. Fix triple brackets across all files
    print("\n9. Fixing triple brackets across all wiki files...")
    triple_count = 0
    for fpath in wiki.rglob('*.md'):
        if fpath.name in ('index.md', 'README.md'):
            continue
        content = fpath.read_text()
        if ']]]' in content:
            original = content
            while ']]]' in content:
                content = content.replace(']]]', ']]', 1)
            if content != original:
                fpath.write_text(content)
                triple_count += 1
    print(f"  Fixed {triple_count} files with triple brackets")
    
    # 10. Fix nested brackets [[[karpathy]]
    print("\n10. Fixing nested brackets...")
    nested_count = 0
    for fpath in wiki.rglob('*.md'):
        content = fpath.read_text()
        if '[[[karpathy]]' in content:
            original = content
            content = re.sub(r'\[\[\[([^\]]+)\]\]', r'[[\1]]', content)
            if content != original:
                fpath.write_text(content)
                nested_count += 1
    print(f"  Fixed {nested_count} files with nested brackets")
    
    # 11. Fix unapproved tags
    print("\n11. Fixing unapproved tags...")
    unapproved = ['review', 'standards', 'tensorflow']
    for fpath in wiki.rglob('*.md'):
        content = fpath.read_text()
        for tag in unapproved:
            pattern = rf'(\btags:\s*\[)([^\]]*?)(\b{re.escape(tag)}\b)([^\]]*?\])'
            if re.search(pattern, content):
                print(f"  Tag '{tag}' found in {fpath.name} - needs APPROVED_TAGS update")
    
    print("\n" + "=" * 60)
    print(f"  DONE - Review results above")
    print("=" * 60)


if __name__ == '__main__':
    main()
