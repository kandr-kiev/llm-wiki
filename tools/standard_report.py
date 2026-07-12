#!/usr/bin/env python3
"""
Standardized report format for all LLM Wiki monitors.

All monitors (RSS, GitHub Release, Local File, Wiki Doctor) must use
this module to generate structured, machine-readable reports.

Report format:
  ## [YYYY-MM-DD HH:MM UTC] COMPONENT | action summary

  **Status**: [ACTIVE] | [SILENT] | [ERROR]
  **Sources scanned**: N
  **New items**: N
  **Errors**: N (list if > 0)
  **Details**:
  - item1
  - item2
  - ...

  ---
  Scan time: Xs | Items/s: Y
"""

import time
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Optional


def format_report(
    component: str,
    status: str,
    sources_scanned: int,
    new_items: int,
    errors: Optional[List[str]] = None,
    details: Optional[List[str]] = None,
    scan_time: float = 0.0,
) -> str:
    """Generate a standardized report string.
    
    Args:
        component: Monitor name (e.g., 'rss_monitor', 'github_release_monitor')
        status: [ACTIVE] | [SILENT] | [ERROR]
        sources_scanned: Total sources checked
        new_items: New items ingested
        errors: List of error messages (if any)
        details: List of detail lines (e.g., file paths)
        scan_time: Duration in seconds
    
    Returns:
        Formatted report string (markdown)
    """
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    
    lines = []
    lines.append(f"## [{timestamp}] {component} | {status}")
    lines.append("")
    lines.append(f"**Status**: {status}")
    lines.append(f"**Sources scanned**: {sources_scanned}")
    lines.append(f"**New items**: {new_items}")
    
    if errors:
        lines.append(f"**Errors**: {len(errors)}")
        for err in errors:
            lines.append(f"  - {err}")
    
    if details:
        lines.append("**Details**:")
        for detail in details:
            lines.append(f"  - {detail}")
    
    if scan_time > 0:
        items_per_sec = new_items / scan_time if scan_time > 0 else 0
        lines.append("")
        lines.append(f"---")
        lines.append(f"Scan time: {scan_time:.1f}s | Items/s: {items_per_sec:.1f}")
    
    return "\n".join(lines)


def format_report_simple(
    component: str,
    label: str,
    count: int,
    source_count: int,
    has_new: bool,
    errors: Optional[List[str]] = None,
    details: Optional[List[str]] = None,
    scan_time: float = 0.0,
) -> str:
    """Generate a compact report for simple scan operations.
    
    Args:
        component: Monitor name
        label: Plural label for sources (e.g., 'feedів', 'репозиторіїв')
        count: New items found
        source_count: Total sources checked
        has_new: Whether new items were found
        errors: List of error messages
        details: List of detail lines
        scan_time: Duration in seconds
    
    Returns:
        Formatted report string
    """
    status = "[ACTIVE]" if has_new else "[SILENT]"
    summary = f"Сканування {source_count} {label}, знайдено {count} нових" if has_new else "Немає нових даних для сканування"
    
    return format_report(
        component=component,
        status=status,
        sources_scanned=source_count,
        new_items=count,
        errors=errors,
        details=details,
        scan_time=scan_time,
    )


def format_wiki_doctor_report(
    component: str,
    before_errors: int,
    before_warns: int,
    before_info: int,
    before_auto_fixable: int,
    after_errors: int,
    after_warns: int,
    after_info: int,
    after_auto_fixable: int,
    fixes_applied: int,
    error_details: Optional[List[str]] = None,
    warn_details: Optional[List[str]] = None,
    scan_time: float = 0.0,
) -> str:
    """Generate a standardized Wiki Doctor report.
    
    Args:
        component: 'wiki_doctor'
        before_*: Counts before fix
        after_*: Counts after fix
        fixes_applied: Number of auto-fixes applied
        error_details: List of error descriptions
        warn_details: List of warning descriptions
        scan_time: Duration in seconds
    
    Returns:
        Formatted report string
    """
    lines = []
    lines.append(f"## [{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}] {component} | Wiki Doctor — до: **ERROR:** {before_errors} | **WARN:** {before_warns} | **INFO:** {before_info} | **Auto-fixable:** {before_auto_fixable}, після: **ERROR:** {after_errors} | **WARN:** {after_warns} | **INFO:** {after_info} | **Auto-fixable:** {after_auto_fixable}, виправлень: {fixes_applied}")
    
    if error_details:
        lines.append("")
        lines.append("**Помилки**:")
        for err in error_details:
            lines.append(f"  - {err}")
    
    if warn_details:
        lines.append("")
        lines.append("**Застереження**:")
        for warn in warn_details:
            lines.append(f"  - {warn}")
    
    if scan_time > 0:
        lines.append("")
        lines.append(f"---")
        lines.append(f"Scan time: {scan_time:.1f}s")
    
    return "\n".join(lines)


def format_comparison_report(
    component: str,
    total_compared: int,
    new_compared: int,
    unchanged: int,
    errors: Optional[List[str]] = None,
    details: Optional[List[str]] = None,
    scan_time: float = 0.0,
) -> str:
    """Generate a standardized comparison report.
    
    Args:
        component: 'comparison' or 'wiki_doctor'
        total_compared: Total pairs compared
        new_compared: New comparisons generated
        unchanged: Unchanged pairs
        errors: List of error messages
        details: List of detail lines
        scan_time: Duration in seconds
    
    Returns:
        Formatted report string
    """
    status = "[ACTIVE]" if new_compared > 0 else "[SILENT]"
    
    lines = []
    lines.append(f"## [{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}] {component} | {status}")
    lines.append("")
    lines.append(f"**Status**: {status}")
    lines.append(f"**Total pairs compared**: {total_compared}")
    lines.append(f"**New comparisons**: {new_compared}")
    lines.append(f"**Unchanged**: {unchanged}")
    
    if errors:
        lines.append(f"**Errors**: {len(errors)}")
        for err in errors:
            lines.append(f"  - {err}")
    
    if details:
        lines.append("**Details**:")
        for detail in details:
            lines.append(f"  - {detail}")
    
    if scan_time > 0:
        lines.append("")
        lines.append(f"---")
        lines.append(f"Scan time: {scan_time:.1f}s | Pairs/s: {total_compared/scan_time:.1f}")
    
    return "\n".join(lines)
