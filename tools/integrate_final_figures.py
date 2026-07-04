#!/usr/bin/env python3
"""Integrate final EPAS figure PNG references into the v2.0 publication draft.

This script replaces each Diagram Placeholder block under an EPAS figure heading
with a Markdown image reference to the accepted final PNG in figures/png/.

It preserves the existing captions in the manuscript.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

DRAFT_PATH = Path("EdgePlatformArchitectureSpecification-v2.0-publication-draft.md")
FIGURE_DIR = Path("figures/png")

FIGURES = {
    1: ("Edge Platform Context Model", "figure-01-edge-platform-context-model.png"),
    2: ("Platform / Product / Deployment Hierarchy", "figure-02-platform-product-deployment-hierarchy.png"),
    3: ("Platform Technology Map", "figure-03-platform-technology-map.png"),
    4: ("Commissioning Flow", "figure-04-commissioning-flow.png"),
    5: ("Configurable Workflow Model", "figure-05-configurable-workflow-model.png"),
    6: ("Runtime Transaction Lifecycle", "figure-06-runtime-transaction-lifecycle.png"),
    7: ("Custody State Model", "figure-07-custody-state-model.png"),
    8: ("Transaction Journal and Recovery Model", "figure-08-transaction-journal-recovery-model.png"),
    9: ("Hardware Abstraction Layer", "figure-09-hardware-abstraction-layer.png"),
    10: ("Local Persistence Model", "figure-10-local-persistence-model.png"),
    11: ("Edge-to-Backend Responsibility Split", "figure-11-edge-to-backend-responsibility-split.png"),
    12: ("Cross-Cutting Services Fabric", "figure-12-cross-cutting-services-fabric.png"),
    13: ("Security Trust Boundary Model", "figure-13-security-trust-boundary-model.png"),
    14: ("Administrative Operations Model", "figure-14-administrative-operations-model.png"),
    15: ("Deployment Package Model", "figure-15-deployment-package-model.png"),
    16: ("Commercial Reuse Flywheel", "figure-16-commercial-reuse-flywheel.png"),
    17: ("Platform Evolution Roadmap", "figure-17-platform-evolution-roadmap.png"),
    18: ("IP Strategy Map", "figure-18-ip-strategy-map.png"),
    19: ("EPAS Strategic Summary", "figure-19-epas-strategic-summary.png"),
}


def require_files() -> None:
    if not DRAFT_PATH.exists():
        raise FileNotFoundError(f"Missing manuscript: {DRAFT_PATH}")

    missing = [str(FIGURE_DIR / filename) for _, filename in FIGURES.values() if not (FIGURE_DIR / filename).exists()]
    if missing:
        raise FileNotFoundError("Missing final figure PNG files:\n" + "\n".join(missing))


def integrate(text: str) -> tuple[str, list[int]]:
    integrated: list[int] = []

    for number, (title, filename) in FIGURES.items():
        heading = rf"## Figure {number} — {re.escape(title)}"
        image = f"![Figure {number} — {title}]({FIGURE_DIR.as_posix()}/{filename})"

        # Replace one or more consecutive blockquote placeholder lines following the figure heading.
        pattern = re.compile(
            rf"({heading}\n\n)(?:> \*\*Diagram Placeholder:\*\*.*\n)+",
            flags=re.MULTILINE,
        )

        text, count = pattern.subn(rf"\1{image}\n", text, count=1)
        if count == 1:
            integrated.append(number)
            continue

        # Idempotent success: image already present under the heading.
        already_pattern = re.compile(
            rf"{heading}\n\n!\[Figure {number} — {re.escape(title)}\]\({re.escape(FIGURE_DIR.as_posix() + '/' + filename)}\)",
            flags=re.MULTILINE,
        )
        if already_pattern.search(text):
            integrated.append(number)
            continue

        raise ValueError(f"Could not find placeholder block for Figure {number} — {title}")

    return text, integrated


def main() -> int:
    require_files()
    original = DRAFT_PATH.read_text(encoding="utf-8")
    updated, integrated = integrate(original)

    if updated == original:
        print("No manuscript changes needed; figure references already appear integrated.")
    else:
        DRAFT_PATH.write_text(updated, encoding="utf-8", newline="\n")
        print(f"Updated {DRAFT_PATH} with {len(integrated)} figure references.")

    for number in integrated:
        title, filename = FIGURES[number]
        print(f"Figure {number}: {filename} — {title}")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
