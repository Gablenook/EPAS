# EPAS Consolidation Runbook — Version 2.0

**Repository:** `Gablenook/EPAS`  
**Date:** 2026-07-03  
**Status:** Consolidation process defined for generating the publication draft.

---

## Purpose

This runbook defines how to consolidate the EPAS Markdown source files into a single source-of-truth publication draft.

The target output is:

`EdgePlatformArchitectureSpecification-v2.0-publication-draft.md`

---

## Source Files

The consolidation process assembles the final document from:

1. `EdgePlatformArchitectureSpecification.md` through the end of Chapter 6.
2. Expanded chapter files from `chapters/07-custody-governance.md` through `chapters/19-conclusions-and-strategic-vision.md`.
3. Expanded appendix files from `appendices/appendix-a-platform-technology-responsibility-matrix.md` through `appendices/appendix-f-implementation-evidence-register.md`.

---

## Consolidation Script

The consolidation script is:

`tools/consolidate_epas.py`

Use it from the repository root to generate:

`EdgePlatformArchitectureSpecification-v2.0-publication-draft.md`

---

## What the Script Does

The script:

1. Reads the current master manuscript.
2. Updates front-matter metadata to Version 2.0 publication-draft language.
3. Keeps the master text through the end of Chapter 6.
4. Removes the old framework text beginning at `# Part II — Operational Trust and Custody`.
5. Appends expanded Chapters 7–19 from the chapter files.
6. Appends Appendices A–F from the appendix files.
7. Removes duplicate `Source`, `Status`, and `Primary Figure` headers from split files.
8. Preserves chapter titles, appendix titles, figure placeholders, and captions.
9. Writes the consolidated v2.0 publication draft file.

---

## Post-Generation Verification

After generation, verify the output file includes:

- Version 2.0 publication-draft metadata.
- Document control and revision history.
- Executive Summary.
- Figure Register.
- Chapters 1–19.
- Appendices A–F.
- Figure placeholders and captions.
- Appendix C glossary with API, DTO, ID, and IP entries.
- Appendix F concrete evidence anchors.

Also verify the output file does not include duplicate split-file metadata blocks such as `Source`, `Status`, or `Primary Figure` at the beginning of appended chapter or appendix sections.

---

## Source-of-Truth Rule After Consolidation

After the generated file is reviewed and committed, it becomes the source-of-truth candidate for the Specification.

Recommended rule:

- Small edits should be made directly in the consolidated file.
- Large future edits may be drafted in temporary working files, then merged back into the consolidated source.
- Canva documents, PDFs, executive summaries, legal/IP summaries, and customer-facing collateral should derive from the consolidated Markdown file.

---

## Connector Note

The repository connector view truncates very large file fetches. The consolidation was therefore defined as a deterministic repository-side script rather than by manually reconstructing large Markdown content through the connector view. This avoids accidental text loss or duplicate obsolete chapter content during consolidation.
