#!/usr/bin/env python3
"""Build a publication DOCX from the EPAS Markdown manuscript.

This script prepares a Pandoc-friendly working Markdown file, sizes final figure
references for Word output, verifies that all final PNG figures exist, and runs
Pandoc to produce a DOCX publication draft.

Source of truth remains:
    EdgePlatformArchitectureSpecification-v2.0-publication-draft.md

Output:
    build/EPAS-v2.0-publication-draft.docx
"""

from __future__ import annotations

from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path.cwd()
SOURCE_MD = ROOT / "EdgePlatformArchitectureSpecification-v2.0-publication-draft.md"
BUILD_DIR = ROOT / "build"
WORKING_MD = BUILD_DIR / "EPAS-v2.0-publication-draft.word.md"
OUTPUT_DOCX = BUILD_DIR / "EPAS-v2.0-publication-draft.docx"
FIGURE_DIR = ROOT / "figures" / "png"

EXPECTED_FIGURES = [
    "figure-01-edge-platform-context-model.png",
    "figure-02-platform-product-deployment-hierarchy.png",
    "figure-03-platform-technology-map.png",
    "figure-04-commissioning-flow.png",
    "figure-05-configurable-workflow-model.png",
    "figure-06-runtime-transaction-lifecycle.png",
    "figure-07-custody-state-model.png",
    "figure-08-transaction-journal-recovery-model.png",
    "figure-09-hardware-abstraction-layer.png",
    "figure-10-local-persistence-model.png",
    "figure-11-edge-to-backend-responsibility-split.png",
    "figure-12-cross-cutting-services-fabric.png",
    "figure-13-security-trust-boundary-model.png",
    "figure-14-administrative-operations-model.png",
    "figure-15-deployment-package-model.png",
    "figure-16-commercial-reuse-flywheel.png",
    "figure-17-platform-evolution-roadmap.png",
    "figure-18-ip-strategy-map.png",
    "figure-19-epas-strategic-summary.png",
]


def require_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(str(path))


def verify_inputs() -> None:
    require_file(SOURCE_MD)
    missing = [str(FIGURE_DIR / name) for name in EXPECTED_FIGURES if not (FIGURE_DIR / name).exists()]
    if missing:
        raise FileNotFoundError("Missing expected figure PNG files:\n" + "\n".join(missing))

    text = SOURCE_MD.read_text(encoding="utf-8")
    active_placeholders = [line for line in text.splitlines() if line.startswith("> **Diagram Placeholder:**")]
    if active_placeholders:
        raise RuntimeError(f"Active diagram placeholders remain: {len(active_placeholders)}")

    figure_refs = re.findall(r"figures/png/figure-\d{2}-[^)]+\.png", text)
    if len(set(figure_refs)) != 19:
        raise RuntimeError(f"Expected 19 unique figure references, found {len(set(figure_refs))}")


def prepare_markdown() -> None:
    BUILD_DIR.mkdir(exist_ok=True)
    text = SOURCE_MD.read_text(encoding="utf-8")

    # Pandoc/Word figure sizing. Use the full available text width for the 16:9 figures.
    text = re.sub(
        r"(!\[Figure \d+ — [^\]]+\]\(figures/png/figure-\d{2}-[^)]+\.png\))(?!\{)",
        r"\1{width=6.5in}",
        text,
    )

    # Start major parts and chapters on new pages in Word/PDF output.
    text = re.sub(r"\n# Part ", r"\n\\newpage\n\n# Part ", text)
    text = re.sub(r"\n# Chapter ", r"\n\\newpage\n\n# Chapter ", text)
    text = text.replace("\n## Appendix A", "\n\\newpage\n\n## Appendix A")

    WORKING_MD.write_text(text, encoding="utf-8", newline="\n")


def run_pandoc() -> None:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("Pandoc is not installed. Install it with: sudo apt-get update && sudo apt-get install -y pandoc")

    cmd = [
        pandoc,
        str(WORKING_MD),
        "--from", "markdown+raw_tex+link_attributes",
        "--to", "docx",
        "--toc",
        "--number-sections",
        "--resource-path", f"{ROOT}:{ROOT / 'figures' / 'png'}",
        "--metadata", "title=Edge Platform Architecture Specification (EPAS)",
        "--metadata", "subtitle=Version 2.0 Publication Draft",
        "--output", str(OUTPUT_DOCX),
    ]

    subprocess.run(cmd, check=True)


def main() -> int:
    verify_inputs()
    prepare_markdown()
    run_pandoc()
    print(f"Created {OUTPUT_DOCX}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
