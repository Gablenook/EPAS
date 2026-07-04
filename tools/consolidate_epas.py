#!/usr/bin/env python3
"""
Consolidate EPAS Markdown source files into one publication-draft source-of-truth file.

This script intentionally assembles the specification from repository files instead of
manually copying text through an editor. It avoids transcription errors and preserves
repeatability for future publication builds.

Output:
    EdgePlatformArchitectureSpecification-v2.0-publication-draft.md

Usage from repository root:
    python tools/consolidate_epas.py
"""

from __future__ import annotations

from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT = REPO_ROOT / "EdgePlatformArchitectureSpecification-v2.0-publication-draft.md"
MASTER = REPO_ROOT / "EdgePlatformArchitectureSpecification.md"

CHAPTER_FILES = [
    REPO_ROOT / "chapters/07-custody-governance.md",
    REPO_ROOT / "chapters/08-transaction-integrity.md",
    REPO_ROOT / "chapters/09-hardware-abstraction.md",
    REPO_ROOT / "chapters/10-local-persistence.md",
    REPO_ROOT / "chapters/11-backend-integration.md",
    REPO_ROOT / "chapters/12-cross-cutting-services.md",
    REPO_ROOT / "chapters/13-security-architecture.md",
    REPO_ROOT / "chapters/14-administrative-services.md",
    REPO_ROOT / "chapters/15-deployment-architecture.md",
    REPO_ROOT / "chapters/16-commercial-architecture.md",
    REPO_ROOT / "chapters/17-future-platform-evolution.md",
    REPO_ROOT / "chapters/18-intellectual-property-strategy.md",
    REPO_ROOT / "chapters/19-conclusions-and-strategic-vision.md",
]

APPENDIX_FILES = [
    REPO_ROOT / "appendices/appendix-a-platform-technology-responsibility-matrix.md",
    REPO_ROOT / "appendices/appendix-b-core-architectural-principles.md",
    REPO_ROOT / "appendices/appendix-c-glossary.md",
    REPO_ROOT / "appendices/appendix-d-figure-production-notes.md",
    REPO_ROOT / "appendices/appendix-e-chapter-specification-pattern.md",
    REPO_ROOT / "appendices/appendix-f-implementation-evidence-register.md",
]


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Missing source file: {path}")
    return path.read_text(encoding="utf-8")


def update_master_front_matter(text: str) -> str:
    """Update v1.8 master front matter to v2.0 publication draft metadata."""
    text = text.replace(
        "**Version 1.8 – Authoritative Working Draft**  ",
        "**Version 2.0 – Publication Draft / Source of Truth**  ",
        1,
    )
    text = text.replace(
        "**Document:** `EdgePlatformArchitectureSpecification.md`  ",
        "**Document:** `EdgePlatformArchitectureSpecification-v2.0-publication-draft.md`  ",
        1,
    )
    text = text.replace(
        "**Status:** Master manuscript / active architecture specification  ",
        "**Status:** Consolidated publication draft / authoritative source-of-truth candidate  ",
        1,
    )

    revision_row = (
        "| 2.0 | 2026-07-03 | Consolidated Version 1.8 master baseline through Chapter 6 "
        "with expanded Chapters 7–19 and Appendices A–F into one publication-draft source file. |"
    )
    marker = (
        "| 1.8 | 2026-07-03 | Expanded Chapter 6 to define Runtime Orchestration responsibilities, "
        "transaction lifecycle, coordination model, failure modes, audit requirements, ACK/reconciliation path, "
        "and platform significance. |"
    )
    if revision_row not in text and marker in text:
        text = text.replace(marker, marker + "\n" + revision_row, 1)

    text = text.replace(
        "When architectural language, figures, vocabulary, or technology boundaries change, update this master manuscript first. Downstream documents should be regenerated, revised, or cross-checked against this file.",
        "After Version 2.0 consolidation, this publication draft is the source-of-truth candidate for the Specification. Downstream documents, PDFs, Canva designs, executive briefs, legal summaries, implementation tickets, customer proposals, and training materials should be regenerated, revised, or cross-checked against this file.",
        1,
    )
    return text


def master_through_chapter_6(master_text: str) -> str:
    """Keep master content through Chapter 6 and remove old framework for Chapter 7 onward."""
    boundary = "\n# Part II — Operational Trust and Custody\n"
    if boundary not in master_text:
        raise ValueError("Could not locate Part II boundary in master manuscript.")
    return master_text.split(boundary, 1)[0].rstrip()


def strip_source_header(text: str) -> str:
    """Remove per-file source/status metadata blocks from split chapter/appendix files."""
    lines = text.splitlines()
    if not lines:
        return ""

    output: list[str] = []
    i = 0

    # Always keep first heading.
    output.append(lines[0].rstrip())
    i = 1

    # Drop initial blank lines and metadata lines until first horizontal rule.
    while i < len(lines):
        line = lines[i]
        if line.strip() == "---":
            i += 1
            break
        if line.startswith("**Source:**") or line.startswith("**Status:**") or line.startswith("**Primary Figure:**") or not line.strip():
            i += 1
            continue
        # Unexpected content before horizontal rule; keep it.
        output.append(line.rstrip())
        i += 1

    # Avoid extra blank immediately after title.
    body = "\n".join(lines[i:]).strip()
    if body:
        output.append("")
        output.append(body)

    return "\n".join(output).rstrip()


def normalize_spacing(parts: list[str]) -> str:
    joined = "\n\n---\n\n".join(part.strip() for part in parts if part.strip())
    # Collapse excessive blank lines but keep Markdown readability.
    joined = re.sub(r"\n{4,}", "\n\n\n", joined)
    return joined.rstrip() + "\n"


def main() -> None:
    master_text = update_master_front_matter(read_text(MASTER))
    parts = [master_through_chapter_6(master_text)]

    parts.append("# Part II — Operational Trust and Custody")
    for path in CHAPTER_FILES[:5]:
        parts.append(strip_source_header(read_text(path)))

    parts.append("# Part III — Platform Operations")
    for path in CHAPTER_FILES[5:10]:
        parts.append(strip_source_header(read_text(path)))

    parts.append("# Part IV — Strategic Direction")
    for path in CHAPTER_FILES[10:]:
        parts.append(strip_source_header(read_text(path)))

    parts.append("# Appendices")
    for path in APPENDIX_FILES:
        parts.append(strip_source_header(read_text(path)))

    OUTPUT.write_text(normalize_spacing(parts), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
