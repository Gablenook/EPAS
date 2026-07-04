# Appendix D — Figure Production Notes

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Expanded appendix draft

---

## D.1 Purpose

The figures in EPAS are intentionally defined as numbered placeholders before final artwork is produced. This allows architecture, captions, cross-references, and publication structure to stabilize before time is spent on finished graphics.

The figure set should support three audiences:

- engineering teams that need responsibility clarity,
- commercial and executive audiences that need the platform argument,
- and legal/IP review that needs stable vocabulary and evidence mapping.

## D.2 Figure Development Sequence

Recommended figure production order:

1. **Figure 1 — Edge Platform Context Model** because it frames the entire EPAS argument.
2. **Figure 3 — Platform Technology Map** because it becomes the core architecture overview.
3. **Figure 6 — Runtime Transaction Lifecycle** because it explains how the platform operates.
4. **Figure 8 — Transaction Journal and Recovery Model** because it defends operational trust.
5. **Figure 11 — Edge-to-Backend Responsibility Split** because it clarifies authority and execution.
6. **Figure 16 — Commercial Reuse Flywheel** because it turns architecture into business value.
7. **Figure 19 — EPAS Strategic Summary** because it becomes the executive closing graphic.
8. **Figure 2 — Platform / Product / Deployment Hierarchy** because it supports naming, licensing, and commercial clarity.
9. **Figure 7 — Custody State Model** because it supports the operational trust story.
10. Remaining Platform Technology figures should follow after the core narrative is stable.

## D.3 Canva Deck Alignment

The first Canva executive deck should reuse a smaller subset of the figure register:

- Figure 1 as the opening context slide.
- Figure 2 as the platform/product/deployment explanation.
- Figure 3 as the architecture overview.
- Figure 6 as the runtime explanation.
- Figure 8 as the operational-trust proof point.
- Figure 11 as the backend/edge split.
- Figure 16 as the commercial argument.
- Figure 19 as the closing summary.

## D.4 Figure Style Guidance

Figures should be:

- clean enough for executive review,
- precise enough for engineering review,
- visually consistent across the deck and manuscript,
- traceable to figure numbers and captions,
- and free of product-specific naming unless deliberately required.

Recommended visual conventions:

- Use Toren / EPAS / Edge Platform terminology for platform-level diagrams.
- Use products, licensees, and deployments only as lower-level examples.
- Use consistent colors, iconography, and boundary boxes.
- Highlight responsibility boundaries rather than decorative detail.
- Avoid diagrams that imply the backend owns local physical truth.

## D.5 Publication Rule

Each finished figure should keep the figure number and caption from this manuscript unless the manuscript is deliberately renumbered. Canva graphics, Word/PDF editions, executive briefs, and presentation decks should use the same figure numbers wherever practical to preserve traceability.

## D.6 Figure Review Checklist

Before a figure is finalized, verify:

- It uses the correct figure number.
- It matches the manuscript caption.
- It uses Toren/EPAS naming correctly.
- It does not redefine a Platform Technology incorrectly.
- It shows responsibility boundaries clearly.
- It can be reused in a Canva deck or publication document.
- It does not expose confidential implementation detail unless intended for internal use.
