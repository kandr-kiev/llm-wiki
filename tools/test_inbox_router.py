#!/usr/bin/env python3
"""Tests for inbox_router.py — маршрутизація файлів з /workspace/towiki/ → raw/."""
import os
import shutil
import tempfile
from pathlib import Path
from datetime import datetime, timezone

import pytest

# We need to patch INBOX_DIR before importing the module
import inbox_router

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------
@pytest.fixture
def inbox_tmp(tmp_path):
    """Create a temporary inbox directory."""
    inbox_dir = Path(tmp_path) / "towiki"
    inbox_dir.mkdir(parents=True)
    # Patch the module
    inbox_router.INBOX_DIR = inbox_dir
    inbox_router.RAW_DIR = Path(tmp_path) / "raw"
    inbox_router.PROCESSED_DB = Path(tmp_path) / ".processed" / "inbox_files.txt"
    return inbox_dir


@pytest.fixture
def raw_tmp(tmp_path):
    """Create raw directories."""
    for subdir in ["articles", "papers", "assets", "configs", "transcripts"]:
        (Path(tmp_path) / "raw" / subdir).mkdir(parents=True)
    return Path(tmp_path) / "raw"


@pytest.fixture
def sample_files(inbox_tmp):
    """Create sample files in inbox for testing."""
    files = {
        # Text files
        "article.md": "# Test Article\n\nThis is a test.\n",
        "notes.txt": "Some notes here.\n",
        "report.html": "<html><body><h1>Report</h1></body></html>\n",
        "readme.rst": "Test RST file.\n",
        # PDF files
        "paper.pdf": b"%PDF-1.4 fake pdf content",
        "arxiv-paper.pdf": b"%PDF-1.4 fake arxiv content",
        # Assets
        "image.png": b"\x89PNG fake png content",
        "logo.svg": b"<svg></svg>\n",
        "video.mp4": b"fake mp4 content",
        # Configs
        "config.json": '{"key": "value"}\n',
        "settings.yaml": "key: value\n",
        "data.csv": "a,b,c\n1,2,3\n",
        # Transcripts
        "recording.mp3": b"fake mp3 content",
        "interview.wav": b"fake wav content",
        # Subdirectory file
        "subdir/nested.md": "# Nested file\n",
        # Skip files
        ".DS_Store": b"macos junk",
    }
    for name, content in files.items():
        fpath = inbox_tmp / name
        fpath.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            fpath.write_bytes(content)
        else:
            fpath.write_text(content)
    return inbox_tmp


# ---------------------------------------------------------------------------
# Tests: _classify_file
# ---------------------------------------------------------------------------
class TestClassifyFile:
    def test_md_goes_to_articles(self):
        p = Path("test.md")
        assert inbox_router._classify_file(p) == "articles"

    def test_txt_goes_to_articles(self):
        p = Path("notes.txt")
        assert inbox_router._classify_file(p) == "articles"

    def test_rst_goes_to_articles(self):
        p = Path("readme.rst")
        assert inbox_router._classify_file(p) == "articles"

    def test_html_goes_to_articles(self):
        p = Path("page.html")
        assert inbox_router._classify_file(p) == "articles"

    def test_pdf_goes_to_papers(self):
        p = Path("paper.pdf")
        assert inbox_router._classify_file(p) == "papers"

    def test_png_goes_to_assets(self):
        p = Path("image.png")
        assert inbox_router._classify_file(p) == "assets"

    def test_svg_goes_to_assets(self):
        p = Path("logo.svg")
        assert inbox_router._classify_file(p) == "assets"

    def test_json_goes_to_configs(self):
        p = Path("config.json")
        assert inbox_router._classify_file(p) == "configs"

    def test_yaml_goes_to_configs(self):
        p = Path("settings.yaml")
        assert inbox_router._classify_file(p) == "configs"

    def test_csv_goes_to_configs(self):
        p = Path("data.csv")
        assert inbox_router._classify_file(p) == "configs"

    def test_mp3_goes_to_transcripts(self):
        p = Path("recording.mp3")
        assert inbox_router._classify_file(p) == "transcripts"

    def test_wav_goes_to_transcripts(self):
        p = Path("interview.wav")
        assert inbox_router._classify_file(p) == "transcripts"

    def test_m4a_goes_to_transcripts(self):
        p = Path("audio.m4a")
        assert inbox_router._classify_file(p) == "transcripts"

    def test_unknown_extension_returns_none(self):
        p = Path("file.xyz")
        assert inbox_router._classify_file(p) is None

    def test_gif_goes_to_assets(self):
        p = Path("animation.gif")
        assert inbox_router._classify_file(p) == "assets"

    def test_webp_goes_to_assets(self):
        p = Path("photo.webp")
        assert inbox_router._classify_file(p) == "assets"

    def test_toml_goes_to_configs(self):
        p = Path("pyproject.toml")
        assert inbox_router._classify_file(p) == "configs"

    def test_env_goes_to_configs(self):
        p = Path(".env")
        assert inbox_router._classify_file(p) == "configs"

    def test_xml_goes_to_configs(self):
        p = Path("data.xml")
        assert inbox_router._classify_file(p) == "configs"

    def test_mp4_goes_to_assets(self):
        p = Path("video.mp4")
        assert inbox_router._classify_file(p) == "assets"

    def test_jpg_goes_to_assets(self):
        p = Path("photo.jpg")
        assert inbox_router._classify_file(p) == "assets"

    def test_jpeg_goes_to_assets(self):
        p = Path("image.jpeg")
        assert inbox_router._classify_file(p) == "assets"

    def test_txt_uppercase_extension(self):
        p = Path("file.TXT")
        assert inbox_router._classify_file(p) == "articles"

    def test_md_lowercase_case(self):
        p = Path("file.MD")
        assert inbox_router._classify_file(p) == "articles"


# ---------------------------------------------------------------------------
# Tests: _build_frontmatter
# ---------------------------------------------------------------------------
class TestBuildFrontmatter:
    def test_contains_required_fields(self):
        fm = inbox_router._build_frontmatter(
            source_url="https://example.com",
            blog_source="inbox:local"
        )
        assert "source_url: https://example.com" in fm
        assert "blog_source: inbox:local" in fm
        assert "sha256: PLACEHOLDER" in fm
        assert "ingested:" in fm

    def test_ingested_date_format(self):
        fm = inbox_router._build_frontmatter(
            source_url="https://example.com",
            blog_source="inbox:local"
        )
        # ingested should be a valid date
        for line in fm.splitlines():
            if line.startswith("ingested:"):
                date_str = line.split(": ", 1)[1]
                datetime.strptime(date_str, '%Y-%m-%d')
                break

    def test_placeholder_sha(self):
        fm = inbox_router._build_frontmatter(
            source_url="https://example.com",
            blog_source="inbox:local"
        )
        assert "sha256: PLACEHOLDER" in fm


# ---------------------------------------------------------------------------
# Tests: _compute_sha256
# ---------------------------------------------------------------------------
class TestComputeSHA256:
    def test_deterministic(self):
        h1 = inbox_router._compute_sha256("hello")
        h2 = inbox_router._compute_sha256("hello")
        assert h1 == h2

    def test_different_content_different_hash(self):
        h1 = inbox_router._compute_sha256("hello")
        h2 = inbox_router._compute_sha256("world")
        assert h1 != h2

    def test_returns_64_char_hex(self):
        h = inbox_router._compute_sha256("test")
        assert len(h) == 64
        assert all(c in '0123456789abcdef' for c in h)


# ---------------------------------------------------------------------------
# Tests: _split_frontmatter
# ---------------------------------------------------------------------------
class TestSplitFrontmatter:
    def test_with_frontmatter(self):
        text = "---\nkey: value\n---\nbody content"
        fm, body = inbox_router._split_frontmatter(text)
        assert fm == "key: value"
        assert body == "body content"

    def test_without_frontmatter(self):
        text = "just some text"
        fm, body = inbox_router._split_frontmatter(text)
        assert fm is None
        assert body == text

    def test_empty_body(self):
        text = "---\nkey: value\n---\n"
        fm, body = inbox_router._split_frontmatter(text)
        assert fm == "key: value"
        assert body == ""


# ---------------------------------------------------------------------------
# Tests: _slugify
# ---------------------------------------------------------------------------
class TestSlugify:
    def test_basic(self):
        assert inbox_router._slugify("Hello World") == "hello-world"

    def test_special_chars_removed(self):
        slug = inbox_router._slugify("Test: A/B, C.D")
        assert "/" not in slug
        assert "." not in slug
        assert "," not in slug
        assert ":" not in slug

    def test_uppercase_lowercased(self):
        assert inbox_router._slugify("UPPERCASE") == "uppercase"

    def test_long_slug_truncated(self):
        long_name = "A" * 200
        slug = inbox_router._slugify(long_name)
        assert len(slug) == 100


# ---------------------------------------------------------------------------
# Tests: scan_and_route — text files
# ---------------------------------------------------------------------------
class TestScanAndRouteText:
    def test_single_md_file(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "test.md").write_text("# Test\n\nContent.\n")
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 1
        assert actions[0]["action"] == "text_file"
        assert actions[0]["source"] == str(inbox_tmp / "test.md")
        # File should be removed from inbox
        assert not (inbox_tmp / "test.md").exists()
        # File should exist in raw/articles
        assert actions[0]["target_path"].exists()
        assert "articles" in str(actions[0]["target_path"])

    def test_single_txt_file(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "notes.txt").write_text("Some notes.\n")
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 1
        assert actions[0]["action"] == "text_file"
        assert not (inbox_tmp / "notes.txt").exists()
        assert actions[0]["target_path"].exists()

    def test_html_file(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "page.html").write_text("<html><body>Test</body></html>\n")
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 1
        assert actions[0]["action"] == "text_file"
        assert actions[0]["target_path"].exists()

    def test_frontmatter_has_sha(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "test.md").write_text("# Test\n\nContent.\n")
        inbox_router.scan_and_route(dry_run=False)
        # Find the output file
        out_dir = inbox_tmp / "raw" / "articles"
        out_files = list(out_dir.glob("inbox-test-*.md"))
        assert len(out_files) == 1
        content = out_files[0].read_text(encoding='utf-8')
        fm, body = inbox_router._split_frontmatter(content)
        assert fm is not None
        sha_match = __import__('re').search(r'sha256:\s*([a-f0-9]{64})', fm)
        assert sha_match is not None, "SHA256 should be computed, not placeholder"

    def test_dry_run_does_not_remove(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "test.md").write_text("# Test\n\nContent.\n")
        actions = inbox_router.scan_and_route(dry_run=True)
        assert len(actions) == 1
        # File should still be in inbox
        assert (inbox_tmp / "test.md").exists()


# ---------------------------------------------------------------------------
# Tests: scan_and_route — binary files
# ---------------------------------------------------------------------------
class TestScanAndRouteBinary:
    def test_pdf_to_papers(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "paper.pdf").write_bytes(b"%PDF-1.4")
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 1
        assert actions[0]["action"] == "binary_file"
        assert "papers" in str(actions[0]["target_path"])
        assert not (inbox_tmp / "paper.pdf").exists()

    def test_png_to_assets(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "image.png").write_bytes(b"\x89PNG")
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 1
        assert "assets" in str(actions[0]["target_path"])
        assert not (inbox_tmp / "image.png").exists()

    def test_json_to_configs(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "config.json").write_text('{"key": "value"}\n')
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 1
        assert "configs" in str(actions[0]["target_path"])
        assert not (inbox_tmp / "config.json").exists()

    def test_mp3_to_transcripts(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "audio.mp3").write_bytes(b"fake mp3")
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 1
        assert "transcripts" in str(actions[0]["target_path"])
        assert not (inbox_tmp / "audio.mp3").exists()

    def test_name_collision_handled(self, inbox_tmp, raw_tmp):
        """Two files with same name should not collide."""
        (inbox_tmp / "sub1" / "file.md").parent.mkdir(exist_ok=True)
        (inbox_tmp / "sub1" / "file.md").write_text("# File 1\n")
        (inbox_tmp / "sub2" / "file.md").parent.mkdir(exist_ok=True)
        (inbox_tmp / "sub2" / "file.md").write_text("# File 2\n")
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 2
        targets = [a["target"] for a in actions]
        assert len(set(targets)) == 2  # No duplicates


# ---------------------------------------------------------------------------
# Tests: scan_and_route — skip & edge cases
# ---------------------------------------------------------------------------
class TestScanAndRouteEdgeCases:
    def test_empty_inbox(self, inbox_tmp, raw_tmp):
        actions = inbox_router.scan_and_route(dry_run=False)
        assert actions == []

    def test_skip_dotfiles(self, inbox_tmp, raw_tmp):
        (inbox_tmp / ".DS_Store").write_bytes(b"macos junk")
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 0
        assert (inbox_tmp / ".DS_Store").exists()

    def test_nested_subdirectory(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "a" / "b" / "c" / "file.md").parent.mkdir(parents=True)
        (inbox_tmp / "a" / "b" / "c" / "file.md").write_text("# Nested\n")
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 1
        assert actions[0]["action"] == "text_file"
        assert actions[0]["target_path"].exists()
        # Subdir should be cleaned up
        assert not (inbox_tmp / "a").exists()

    def test_unknown_extension_skipped(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "weird.xyz").write_text("unknown type\n")
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 0
        # File should remain in inbox
        assert (inbox_tmp / "weird.xyz").exists()

    def test_mixed_files(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "article.md").write_text("# Article\n")
        (inbox_tmp / "image.png").write_bytes(b"\x89PNG")
        (inbox_tmp / "config.json").write_text('{}\n')
        actions = inbox_router.scan_and_route(dry_run=False)
        assert len(actions) == 3
        targets = [str(a["target_path"]) for a in actions]
        assert any("articles" in t for t in targets)
        assert any("assets" in t for t in targets)
        assert any("configs" in t for t in targets)

    def test_nonexistent_inbox(self, tmp_path, raw_tmp):
        inbox_router.INBOX_DIR = tmp_path / "nonexistent"
        actions = inbox_router.scan_and_route(dry_run=False)
        assert actions == []


# ---------------------------------------------------------------------------
# Tests: dedup (processed DB)
# ---------------------------------------------------------------------------
class TestDedup:
    def test_processed_file_skipped(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "test.md").write_text("# Test\n")
        # First run
        actions1 = inbox_router.scan_and_route(dry_run=False)
        assert len(actions1) == 1
        # Second run — file already processed
        actions2 = inbox_router.scan_and_route(dry_run=False)
        assert len(actions2) == 0

    def test_dry_run_does_not_mark_processed(self, inbox_tmp, raw_tmp):
        (inbox_tmp / "test.md").write_text("# Test\n")
        inbox_router.scan_and_route(dry_run=True)
        # Should still be there
        assert (inbox_tmp / "test.md").exists()
        # Running again should still see it
        actions = inbox_router.scan_and_route(dry_run=True)
        assert len(actions) == 1


# ---------------------------------------------------------------------------
# Tests: _ensure_target_dir
# ---------------------------------------------------------------------------
class TestEnsureTargetDir:
    def test_creates_directory(self, tmp_path):
        inbox_router.RAW_DIR = tmp_path / "raw"
        result = inbox_router._ensure_target_dir("articles")
        assert result.exists()
        assert result.is_dir()

    def test_does_not_remove_existing(self, tmp_path):
        inbox_router.RAW_DIR = tmp_path / "raw"
        existing = tmp_path / "raw" / "articles"
        existing.mkdir(parents=True)
        (existing / "existing.md").write_text("existing")
        result = inbox_router._ensure_target_dir("articles")
        assert result.exists()
        assert (result / "existing.md").exists()


# ---------------------------------------------------------------------------
# Tests: _is_processed / _mark_processed
# ---------------------------------------------------------------------------
class TestProcessedDB:
    def test_new_file_not_processed(self, tmp_path):
        db = tmp_path / "inbox_files.txt"
        inbox_router.PROCESSED_DB = db
        p = tmp_path / "file.txt"
        p.write_text("test")
        assert inbox_router._is_processed(p) is False

    def test_marked_file_is_processed(self, tmp_path):
        db = tmp_path / "inbox_files.txt"
        inbox_router.PROCESSED_DB = db
        p = tmp_path / "file.txt"
        p.write_text("test")
        inbox_router._mark_processed(p)
        assert inbox_router._is_processed(p) is True


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    pytest.main([__file__, '-v'])
