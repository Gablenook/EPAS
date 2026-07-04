# Appendix B — Core Architectural Principles

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Expanded appendix draft

---

## B.1 Purpose

This appendix provides a compact reference for the core architectural principles governing EPAS and the Toren Edge Platform. Chapter 2 remains the authoritative expanded discussion. This appendix is intended as a quick checklist for design review, implementation review, support review, and future editing.

## B.2 Principle List

1. **Single Ownership** — Every significant engineering responsibility has one architectural owner.
2. **Separation of Responsibilities** — Major platform responsibilities remain separated so one layer does not absorb the whole system.
3. **Configuration Before Customization** — Deployment variation should be expressed through governed configuration before source-code customization.
4. **Deterministic Execution** — The same operational inputs should produce the same platform behavior unless a documented exception applies.
5. **Operational Trust** — The edge platform must preserve trustworthy local state when networks, devices, or workflows fail.
6. **Platform Before Product** — Products, licensees, and customer deployments express the platform; they do not define it.
7. **Transaction Context Before Governed Action** — Governed edge actions must be tied to explicit transaction context.
8. **Local Truth Must Be Durable** — The edge node must preserve durable evidence of local events.
9. **Backend Authority Must Be Explicit** — Backend calls must carry explicit identity, workflow, actor, request, and correlation context.
10. **Administrative Actions Must Be Governed** — Manual tests, overrides, recovery, reconciliation, and correction must be permissioned, logged, and explainable.

## B.3 Design Review Questions

Use these questions when reviewing changes:

- Which Platform Technology owns this responsibility?
- Is this behavior configured before it is customized?
- Does this change preserve transaction context?
- Does local truth remain durable after failure?
- Are backend assumptions explicit?
- Are administrative actions governed?
- Does the change strengthen the platform rather than create isolated product code?

## B.4 Editing Rule

When expanding any chapter, use these principles as the guardrails. Later chapters may apply the principles, but they should not redefine them.
