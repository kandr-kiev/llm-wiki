#!/usr/bin/env python3
"""Тестування Telegram MarkdownV2 escape для прихованих посилань."""

# Telegram MarkdownV2 requires escaping: _ * [ ] ( ) ~ ` > # + - = | { } . !
# For inline links [text](url), need to escape [, ], (, )

def escape_markdown_v2(text: str) -> str:
    """Escape special characters for Telegram MarkdownV2."""
    special_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for ch in special_chars:
        text = text.replace(ch, f'\\{ch}')
    return text

# Test: inline link with escaped characters
title = "Test Article Title"
url = "https://example.com/article"

# Method 1: Escape everything (including URL)
escaped_title = escape_markdown_v2(title)
escaped_url = escape_markdown_v2(url)
link_escaped = f"[{escaped_title}]({escaped_url})"
print(f"Method 1 (full escape): {link_escaped}")

# Method 2: Only escape [, ], (, ) for the link syntax
link_syntax = f"\\[{title}\\]\\({url}\\)"
print(f"Method 2 (syntax only): {link_syntax}")

# Method 3: Plain [text](url) - will Telegram render this?
print(f"Method 3 (plain): [{title}]({url})")

# Method 4: Just the URL (Telegram auto-renders as clickable)
print(f"Method 4 (plain URL): {url}")
