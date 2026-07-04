# EPAS Publication Style Guide

**Repository:** `Gablenook/EPAS`  
**Source Document:** `EdgePlatformArchitectureSpecification-v2.0-publication-draft.md`  
**Status:** Initial publication and Canva style guide  
**Purpose:** Define the visual, formatting, and production standards for the EPAS technical specification, figures, PDF, executive summary, and Canva deck.

---

## 1. Publication Goal

EPAS should look like a professional technical architecture specification: clean, precise, stable, and executive-readable. The design should support engineering confidence, customer clarity, commercial credibility, and future review without feeling like a dark software-marketing presentation.

The visual goal is:

> Professional engineering whitepaper with restrained executive polish.

---

## 2. Source-of-Truth Rule

The Markdown specification remains the source of truth.

Primary source:

`EdgePlatformArchitectureSpecification-v2.0-publication-draft.md`

Downstream outputs:

- technical PDF,
- executive summary PDF,
- Canva figure set,
- Canva executive deck,
- customer-facing excerpts,
- legal or commercial summaries.

Downstream materials should derive from the Markdown source, not replace it.

---

## 3. Visual Tone

Use a light, clean, technical style.

Preferred feel:

- whitepaper,
- architecture document,
- professional engineering presentation,
- calm executive briefing,
- precise system documentation.

Avoid:

- dark dashboard styling,
- neon technology colors,
- heavy gradients,
- dramatic shadows,
- cyber/security visual language,
- overly decorative icons,
- marketing clutter.

---

## 4. Color Direction

Use a restrained light palette.

Recommended palette direction:

| Role | Suggested Color Direction | Use |
| --- | --- | --- |
| Background | White or very light warm gray | Page and figure background |
| Primary text | Dark charcoal | Body text and labels |
| Secondary text | Medium gray | Notes, captions, secondary labels |
| Boundary lines | Soft blue-gray | Boxes and diagram boundaries |
| Primary accent | Muted steel blue | Main arrows and selected highlights |
| Secondary accent | Muted copper or muted slate | Limited emphasis only |
| Success/complete | Muted green | Optional status indication |
| Warning/review | Muted amber | Optional exception indication |

Color should clarify meaning. It should not be used merely for decoration.

---

## 5. Typography

Use common professional fonts that render well in PDF, Word, GitHub, and Canva.

Recommended font direction:

| Element | Font Direction |
| --- | --- |
| Document title | Aptos Display, Arial, or Inter |
| Chapter headings | Aptos Display, Arial, or Inter |
| Body text | Aptos, Calibri, Arial, or Source Sans |
| Captions | Same body font, smaller size |
| Code, DTOs, file names | Consolas, Courier New, or equivalent monospace |

Do not use decorative fonts. Prioritize readability and consistency.

---

## 6. Document Formatting

Recommended formal document format:

- Page size: Letter.
- Margins: 0.75 inch to 1.0 inch.
- Body text: 10.5 to 11 point.
- Line spacing: comfortable single or 1.08 to 1.15.
- Chapter titles: large, clear, and separated from body text.
- Section headings: numbered and consistent.
- Captions: smaller than body text and directly below figures.
- Tables: clean grid, light lines, bold header row.
- Page footer: document name, version, page number.

---

## 7. Heading Structure

Use the consolidated Markdown heading structure as the document hierarchy.

Recommended mapping:

| Markdown | Publication Role |
| --- | --- |
| `#` | Document title, part title, chapter title, appendix title |
| `##` | Major section |
| `###` | Subsection |
| `####` | Minor subsection or callout heading |

Avoid creating deep heading levels unless truly needed.

---

## 8. Figure Style

Figures should be consistent across the technical PDF and Canva deck.

Every figure should include:

- figure number,
- figure title,
- clear diagram content,
- manuscript-aligned caption,
- consistent visual style,
- readable labels,
- clear responsibility boundaries.

Figure design rules:

- Use light backgrounds.
- Use restrained colors.
- Use consistent arrows and connector lines.
- Use consistent box shapes and spacing.
- Use color to show responsibility or flow.
- Avoid visual effects that distract from the architecture.
- Avoid product-specific branding unless intentionally required.

---

## 9. Figure File Standards

Finished figure exports should be stored as separate assets.

Recommended paths:

```text
figures/png/
figures/pdf/
figures/svg/
```

Recommended filename format:

```text
figure-##_short-descriptive-title.png
```

Examples:

```text
figure-01-edge-platform-context-model.png
figure-03-platform-technology-map.png
figure-06-runtime-transaction-lifecycle.png
figure-08-transaction-journal-recovery-model.png
figure-11-edge-to-backend-responsibility-split.png
figure-16-commercial-reuse-flywheel.png
figure-19-epas-strategic-summary.png
```

The Markdown should reference exported figure files. Canva remains the editable design environment.

---

## 10. Canva Standards

Canva should be used for:

- final figure artwork,
- executive architecture deck,
- visual summaries,
- cover or title graphics if needed.

Canva should not become the source of truth for specification text.

Recommended Canva design files:

- `EPAS Specification Figures`
- `EPAS Executive Architecture Deck`

The first figure pass should use a light technical-document style. The previous dark direction should not be used as the governing style.

---

## 11. Tables and Registers

Tables should be readable, compact, and restrained.

Use:

- bold header row,
- light grid lines,
- consistent column names,
- no unnecessary background color,
- enough spacing for readability.

Important table-heavy areas:

- List of Figures,
- Appendix A — Platform Technology Responsibility Matrix,
- Appendix F — Implementation Evidence Register.

---

## 12. Callout Style

Use callouts sparingly and consistently.

Recommended callout types:

- Principle,
- Boundary Rule,
- Implementation Evidence,
- Publication Note,
- Review Note.

Callouts should clarify the architecture. They should not interrupt the main reading flow.

---

## 13. Naming and Terminology

Use the formal EPAS terms consistently:

- Toren,
- EPAS,
- Toren Edge Platform,
- Edge Platform,
- Platform Technology,
- Product,
- Licensee,
- Deployment,
- Runtime Orchestration,
- Transaction Integrity,
- Custody Governance,
- Backend Integration,
- Local Persistence,
- Hardware Abstraction,
- Configurable Workflow Engine.

Use uppercase forms for:

- ACK,
- API,
- DTO,
- ID,
- IP,
- EPAS.

---

## 14. Publication Package

The professional publication package should eventually include:

- consolidated Markdown source,
- publication style guide,
- exported figure assets,
- technical specification PDF,
- executive summary PDF,
- Canva executive deck,
- optional DOCX review copy.

---

## 15. Immediate Design Decision

The approved direction for the next Figure 1 pass is:

- light background,
- dark charcoal text,
- soft blue-gray outlines,
- muted steel-blue arrows,
- restrained accent color,
- clean architecture-document feel.

This style should be validated on Figure 1 and Figure 3 before producing the remaining priority figures.
