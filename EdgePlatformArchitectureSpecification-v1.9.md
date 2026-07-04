# Edge Platform™ Architecture Specification (EPAS)

**Version 1.9 – Clean Control / Index Draft**  
**Repository:** `Gablenook/EPAS`  
**Document:** `EdgePlatformArchitectureSpecification-v1.9.md`  
**Status:** Clean control/index document for expanded chapter-file structure  
**Revision Date:** 2026-07-03

> EPAS defines the Toren Edge Platform architecture: the durable engineering foundation for governed physical-edge systems such as asset custody kiosks, field-deployed device exchange systems, package exchange systems, controlled-access equipment systems, and other transaction-controlled edge operations.

---

## Document Control

This file is the clean Version 1.9 control/index document for the Edge Platform Architecture Specification. It exists to stabilize the documentation structure after Chapters 7–19 and Appendices A–F were split into separate expanded source files.

The prior master file, `EdgePlatformArchitectureSpecification.md`, remains the Version 1.8 authoritative working draft containing the expanded manuscript through Chapter 6 and the earlier framework for the balance of the document. This v1.9 file should be used as the control structure for continuity review, later assembly, Canva alignment, publication planning, and final consolidation.

### Revision History

| Version | Date | Description |
| --- | --- | --- |
| 1.0 | 2026-07-02 | Master manuscript established as the authoritative EPAS architecture specification. |
| 1.1 | 2026-07-03 | Began structured manuscript edit: strengthened document governance, platform thesis, standard chapter pattern, responsibility boundaries, and implementation-alignment language. |
| 1.2 | 2026-07-03 | Aligned manuscript naming around Toren ownership, EPAS as the platform reference architecture, and generic licensed product/deployment language. |
| 1.3 | 2026-07-03 | Expanded Chapter 1 to define the platform vision, problem addressed, commercial hierarchy, operating domain, naming independence, and chapter boundary. |
| 1.4 | 2026-07-03 | Expanded Chapter 2 to define governing architectural principles, principle application rules, and platform-level decision tests. |
| 1.5 | 2026-07-03 | Expanded Chapter 3 to define the Platform Technology taxonomy, qualification criteria, collaboration model, ownership boundaries, and chapter-control role. |
| 1.6 | 2026-07-03 | Expanded Chapter 4 to define Commissioning Technology responsibilities, data ownership, operational model, failure modes, audit requirements, and platform significance. |
| 1.7 | 2026-07-03 | Expanded Chapter 5 to define Configurable Workflow Engine responsibilities, workflow schema, execution model, versioning, failure modes, audit requirements, and platform significance. |
| 1.8 | 2026-07-03 | Expanded Chapter 6 to define Runtime Orchestration responsibilities, transaction lifecycle, coordination model, failure modes, audit requirements, ACK/reconciliation path, and platform significance. |
| 1.9 | 2026-07-03 | Created clean control/index document: Chapters 1–6 remain governed by the v1.8 master baseline; Chapters 7–19 and Appendices A–F are referenced as expanded separate source files for continuity review and later consolidation. |

### Editing Rule

Do not expand large sections directly in this control/index file. Use the chapter and appendix source files listed below for continued editing. When the chapter files pass continuity review, assemble them into a future consolidated publication draft.

### Naming and Ownership Rule

Toren is the company, platform owner, and licensor. EPAS is the reference architecture for the Toren Edge Platform. Products, customer systems, licensee implementations, manufactured locker systems, and branded deployments may implement or express the platform, but they do not define the architecture. The master manuscript should avoid tying EPAS to any single product name, customer name, manufacturer, or licensee unless that reference is deliberately required for implementation evidence or commercial context.

---

## Purpose of This Control File

This v1.9 file establishes the clean working structure for the specification before final consolidation. It answers four documentation-control questions:

1. Which source contains the expanded Chapters 1–6 baseline?
2. Which files contain the expanded Chapters 7–19?
3. Which files contain the expanded Appendices A–F?
4. What sequence should be followed before producing the consolidated publication manuscript and Canva materials?

---

## Current Source Structure

### Baseline Master Through Chapter 6

| Scope | Source File | Status |
| --- | --- | --- |
| Document Control, Executive Summary, Figure Register, Chapters 1–6 | `EdgePlatformArchitectureSpecification.md` | Version 1.8 authoritative working draft; expanded through Chapter 6 |

### Expanded Chapter Files

| Chapter | Title | Source File | Status |
| --- | --- | --- | --- |
| 7 | Custody Governance | `chapters/07-custody-governance.md` | Expanded chapter draft |
| 8 | Transaction Integrity | `chapters/08-transaction-integrity.md` | Expanded chapter draft |
| 9 | Hardware Abstraction | `chapters/09-hardware-abstraction.md` | Expanded chapter draft |
| 10 | Local Persistence | `chapters/10-local-persistence.md` | Expanded chapter draft |
| 11 | Backend Integration | `chapters/11-backend-integration.md` | Expanded chapter draft |
| 12 | Cross-Cutting Services | `chapters/12-cross-cutting-services.md` | Expanded chapter draft |
| 13 | Security Architecture | `chapters/13-security-architecture.md` | Expanded chapter draft |
| 14 | Administrative Services | `chapters/14-administrative-services.md` | Expanded chapter draft |
| 15 | Deployment Architecture | `chapters/15-deployment-architecture.md` | Expanded chapter draft |
| 16 | Commercial Architecture | `chapters/16-commercial-architecture.md` | Expanded chapter draft |
| 17 | Future Platform Evolution | `chapters/17-future-platform-evolution.md` | Expanded chapter draft |
| 18 | Intellectual Property Strategy | `chapters/18-intellectual-property-strategy.md` | Expanded chapter draft |
| 19 | Conclusions and Strategic Vision | `chapters/19-conclusions-and-strategic-vision.md` | Expanded chapter draft |

### Expanded Appendix Files

| Appendix | Title | Source File | Status |
| --- | --- | --- | --- |
| A | Platform Technology Responsibility Matrix | `appendices/appendix-a-platform-technology-responsibility-matrix.md` | Expanded appendix draft |
| B | Core Architectural Principles | `appendices/appendix-b-core-architectural-principles.md` | Expanded appendix draft |
| C | Glossary | `appendices/appendix-c-glossary.md` | Expanded appendix draft |
| D | Figure Production Notes | `appendices/appendix-d-figure-production-notes.md` | Expanded appendix draft |
| E | Chapter Specification Pattern | `appendices/appendix-e-chapter-specification-pattern.md` | Expanded appendix draft |
| F | Implementation Evidence Register | `appendices/appendix-f-implementation-evidence-register.md` | Expanded appendix draft |

---

## Publication Contents

The final consolidated publication manuscript should assemble the specification in this order:

1. Document Control
2. Executive Summary
3. List of Figures
4. Figure 1 — Edge Platform Context Model
5. Part I — Platform Foundation
   - Chapter 1 — Platform Vision
   - Chapter 2 — Architectural Principles
   - Chapter 3 — Platform Technology Architecture
   - Chapter 4 — Commissioning Technology
   - Chapter 5 — Configurable Workflow Engine
   - Chapter 6 — Runtime Orchestration
6. Part II — Operational Trust and Custody
   - Chapter 7 — Custody Governance
   - Chapter 8 — Transaction Integrity
   - Chapter 9 — Hardware Abstraction
   - Chapter 10 — Local Persistence
   - Chapter 11 — Backend Integration
7. Part III — Platform Operations
   - Chapter 12 — Cross-Cutting Services
   - Chapter 13 — Security Architecture
   - Chapter 14 — Administrative Services
   - Chapter 15 — Deployment Architecture
   - Chapter 16 — Commercial Architecture
8. Part IV — Strategic Direction
   - Chapter 17 — Future Platform Evolution
   - Chapter 18 — Intellectual Property Strategy
   - Chapter 19 — Conclusions and Strategic Vision
9. Appendix A — Platform Technology Responsibility Matrix
10. Appendix B — Core Architectural Principles
11. Appendix C — Glossary
12. Appendix D — Figure Production Notes
13. Appendix E — Chapter Specification Pattern
14. Appendix F — Implementation Evidence Register

---

## Continuity Review Checklist

Before consolidation, review all source files for:

- Toren / EPAS / Toren Edge Platform naming consistency.
- Platform/product/licensee/deployment distinction.
- Chapter ownership and boundary rules.
- Figure numbering and caption consistency.
- Cross-references among Chapters 1–19.
- Glossary consistency with chapter terminology.
- Appendix A responsibility matrix alignment.
- Appendix F evidence alignment.
- Commercial and IP language consistency.
- Removal or containment of product-specific naming unless intentionally used as implementation evidence.

---

## Consolidation Plan

After continuity review, create a consolidated publication draft using this source order:

1. Start from the Version 1.8 master baseline through Chapter 6.
2. Remove the old framework text for Chapters 7–19 and Appendices A–F from the baseline.
3. Append the expanded chapter files from `chapters/07...` through `chapters/19...`.
4. Append the expanded appendix files from `appendices/appendix-a...` through `appendices/appendix-f...`.
5. Create a new consolidated manuscript file, recommended name:
   - `EdgePlatformArchitectureSpecification-v2.0-publication-draft.md`

---

## Canva Alignment Plan

Canva materials should be updated after the continuity pass and before final publication layout. The first Canva alignment set should focus on the executive architecture story using these figures:

- Figure 1 — Edge Platform Context Model
- Figure 2 — Platform / Product / Deployment Hierarchy
- Figure 3 — Platform Technology Map
- Figure 6 — Runtime Transaction Lifecycle
- Figure 8 — Transaction Journal and Recovery Model
- Figure 11 — Edge-to-Backend Responsibility Split
- Figure 16 — Commercial Reuse Flywheel
- Figure 19 — EPAS Strategic Summary

The Canva executive deck should derive from EPAS but should not replace the GitHub source files.

---

## Current Control Status

This v1.9 control/index file is the coordination point for the next phase. It is not the final publication manuscript. The next recommended step is a continuity pass across the expanded chapter and appendix files, followed by creation of a consolidated publication draft.
