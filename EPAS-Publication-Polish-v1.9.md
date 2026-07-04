# EPAS Publication Polish — Version 1.9

**Repository:** `Gablenook/EPAS`  
**Polish Date:** 2026-07-03  
**Scope:** Chapters 7–19 and Appendices A–F  
**Status:** Publication-polish pass complete; ready for controlled consolidation.

---

## 1. Purpose

This report documents the focused publication-polish pass performed after the Version 1.9 continuity review. The objective was not to rewrite the specification, but to remove small publication-readiness issues before consolidating the specification into a full publication draft.

---

## 2. Requested Cleanup Tasks

The focused cleanup pass covered four tasks:

1. Update Appendix E Related Figures rule.
2. Add concrete evidence anchors to Appendix F.
3. Run terminology/capitalization polish across Chapters 7–19 and Appendices A–F.
4. Create this publication-polish report.

---

## 3. Changes Applied

### 3.1 Appendix E — Related Figures Rule

Updated `appendices/appendix-e-chapter-specification-pattern.md` so the chapter's primary figure header satisfies the Related Figures requirement unless the chapter references additional figures that need to be listed separately.

This avoids adding redundant `Related Figures` sections to every chapter while preserving the publication rule that every chapter must have a traceable figure reference.

### 3.2 Appendix F — Concrete Evidence Anchors

Expanded `appendices/appendix-f-implementation-evidence-register.md` with concrete evidence anchors, including:

- `KioskWorkflowConfiguration`
- `WorkflowDefinition`
- `DefaultWorkflowKey`
- `HomePickupWorkflowKey`
- `HomeDeliveryWorkflowKey`
- `EnabledWorkflows`
- `ScanValidationProfiles`
- `AssetValidateRequest`
- `LockerAuthorizeRequestDto`
- `LockerAckRequestDto`
- `LockerTransactionJournal`
- `LockerTransactionRecoveryService`
- `LockerActionService`
- `LockerControllerService`
- `BarcodeScanService`
- `FileAuditLogger`
- `Locker` table
- `LockerStatus` table
- Controller branch A/B mapping
- Admin locker status review
- Manual compartment/controller test
- ACK retry/reconciliation records

These anchors are still candidates until implementation repository paths and line references are verified, but they give the publication draft a much stronger evidence scaffold.

### 3.3 Appendix C — Glossary and Capitalization Terms

Updated `appendices/appendix-c-glossary.md` to add publication-polish glossary entries for:

- **API**
- **DTO**
- **ID**
- **IP**

The ID entry clarifies formal capitalization for Actor ID, Request ID, Transaction ID, Correlation ID, Kiosk ID, and Locker Bank ID. The IP entry clarifies uppercase IP for intellectual-property strategy, evidence, defensibility, or review.

---

## 4. Terminology and Capitalization Result

The source set now has explicit glossary support for the main capitalization-sensitive terms used throughout EPAS:

- ACK
- API
- DTO
- ID
- IP
- EPAS
- Platform Technology
- Runtime Orchestration
- Transaction Integrity
- Local Persistence
- Backend Integration
- Custody Governance
- Security Architecture
- Administrative Services
- Deployment Architecture
- Configurable Workflow Engine

The publication draft should preserve these exact forms unless a term appears in lowercase as ordinary descriptive prose rather than as a formal EPAS term.

---

## 5. Canva Impact

No Canva files were changed during this pass.

The Canva planning direction remains unchanged: use GitHub as the source of truth and align the executive architecture deck around Figures 1, 2, 3, 6, 8, 11, 16, and 19.

---

## 6. Remaining Pre-Consolidation Notes

The source files are ready for controlled consolidation. The consolidation process should still perform mechanical cleanup while assembling the publication draft:

1. Remove duplicate `Source`, `Status`, and `Primary Figure` header blocks from appended chapter and appendix files where appropriate.
2. Preserve figure numbers, figure titles, diagram placeholders, and captions.
3. Preserve chapter and appendix titles.
4. Preserve the v1.9 naming and ownership rule.
5. Preserve Appendix F as the evidence register, but label evidence anchors as candidate anchors until repository paths are verified.
6. Keep Canva references as downstream/publication planning material, not as source-of-truth material.

---

## 7. Recommended Next File

Create the consolidated publication draft as:

`EdgePlatformArchitectureSpecification-v2.0-publication-draft.md`

Recommended source order:

1. `EdgePlatformArchitectureSpecification.md` through the end of Chapter 6.
2. `chapters/07-custody-governance.md` through `chapters/19-conclusions-and-strategic-vision.md`.
3. `appendices/appendix-a-platform-technology-responsibility-matrix.md` through `appendices/appendix-f-implementation-evidence-register.md`.

---

## 8. Conclusion

Publication polish is complete for the current source set. The specification text, chapter structure, appendix support, glossary capitalization rules, figure-placeholder strategy, and implementation-evidence scaffold are ready for controlled consolidation into the Version 2.0 publication draft.
