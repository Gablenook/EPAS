# EPAS Figure Design Brief — Version 1.0

**Repository:** `Gablenook/EPAS`  
**Source Document:** `EdgePlatformArchitectureSpecification-v2.0-publication-draft.md`  
**Status:** Initial Canva production brief

---

## 1. Purpose

This brief defines the first professional figure set for EPAS. It converts the consolidated specification's figure placeholders into a Canva production plan.

The goal is to create a consistent figure system for:

1. the full EPAS technical specification,
2. an executive summary PDF,
3. the Canva executive architecture deck.

---

## 2. First Figure Set

Produce the first eight figures in this order:

1. Figure 1 — Edge Platform Context Model
2. Figure 3 — Platform Technology Map
3. Figure 6 — Runtime Transaction Lifecycle
4. Figure 8 — Transaction Journal and Recovery Model
5. Figure 11 — Edge-to-Backend Responsibility Split
6. Figure 16 — Commercial Reuse Flywheel
7. Figure 19 — EPAS Strategic Summary
8. Figure 2 — Platform / Product / Deployment Hierarchy

These eight figures carry the core EPAS story and should be completed before the remaining figure set.

---

## 3. Global Figure Style

All figures should use one visual system:

- clean technical style,
- consistent typography,
- consistent line weights,
- consistent box and arrow style,
- restrained color palette,
- clear responsibility boundaries,
- Toren / EPAS naming,
- no unnecessary product-specific naming.

Figures should be readable in both PDF page format and Canva slide format.

---

## 4. Figure 1 — Edge Platform Context Model

**Purpose:** Establish the overall EPAS operating context.

**Key message:** The Edge Platform coordinates enterprise authority, local execution, controlled equipment, local state, and audit evidence.

**Main visual approach:** Hub-and-spoke diagram with Toren Edge Platform in the center.

**Include:**

- Enterprise Systems
- Human Operators
- Credential / Scan Devices
- Hardware Controllers
- Physical Compartments
- Local Persistence
- Audit Evidence
- Administrative Support

**Export filename:** `figure-01-edge-platform-context-model.png`

---

## 5. Figure 2 — Platform / Product / Deployment Hierarchy

**Purpose:** Explain the difference between Toren, EPAS, the platform, products, licensees, and deployments.

**Key message:** EPAS governs the reusable platform; products and licensees express it; deployments configure it.

**Main visual approach:** Stacked hierarchy or pyramid.

**Include:**

- Toren / EPAS / Toren Edge Platform
- Product Expressions
- Licensees / Commercial Partners
- Customer Deployments
- Site, workflow, hardware, and policy configuration

**Export filename:** `figure-02-platform-product-deployment-hierarchy.png`

---

## 6. Figure 3 — Platform Technology Map

**Purpose:** Show the major EPAS Platform Technologies and their boundaries.

**Key message:** EPAS is a platform architecture made of durable, named technology responsibilities.

**Main visual approach:** Layered architecture map.

**Include:**

- Commissioning Technology
- Configurable Workflow Engine
- Runtime Orchestration
- Custody Governance
- Transaction Integrity
- Hardware Abstraction
- Local Persistence
- Backend Integration
- Cross-Cutting Services
- Security Architecture
- Administrative Services
- Deployment Architecture
- Commercial Architecture
- Future Platform Evolution
- Intellectual Property Strategy

**Export filename:** `figure-03-platform-technology-map.png`

---

## 7. Figure 6 — Runtime Transaction Lifecycle

**Purpose:** Show the governed transaction path from workflow selection through completion or reconciliation.

**Key message:** Runtime Orchestration turns configured workflow intent into recoverable edge execution.

**Main visual approach:** Swimlane or left-to-right lifecycle.

**Include:**

- Workflow selection
- Actor / credential / reference input
- Validation
- Authorization
- Custody rule evaluation
- Compartment or device selection
- Transaction journal update before equipment action
- Local state update
- ACK
- Failure / retry / reconciliation states

**Export filename:** `figure-06-runtime-transaction-lifecycle.png`

---

## 8. Figure 8 — Transaction Journal and Recovery Model

**Purpose:** Show how the transaction journal protects operational truth.

**Key message:** Interrupted or incomplete transactions are classified, retained, retried, recovered, or reconciled.

**Main visual approach:** State-machine or lifecycle diagram.

**Include:**

- Created
- Local action started
- Local state updated
- ACK pending
- ACK succeeded
- ACK failed
- Needs reconciliation
- Completed
- Failed
- Abandoned

**Export filename:** `figure-08-transaction-journal-recovery-model.png`

---

## 9. Figure 11 — Edge-to-Backend Responsibility Split

**Purpose:** Clarify backend responsibility versus Edge Platform responsibility.

**Key message:** Backend systems provide authority and records; the Edge Platform owns local execution, local truth, and recoverable evidence.

**Main visual approach:** Two-column responsibility split with an API contract layer between them.

**Include backend side:**

- Business authority
- Enterprise records
- Validation
- Authorization
- Reporting
- Reconciliation acceptance

**Include edge side:**

- Runtime execution
- Local input capture
- Equipment control
- Local state
- Transaction journal
- ACK generation
- Recovery support

**Export filename:** `figure-11-edge-to-backend-responsibility-split.png`

---

## 10. Figure 16 — Commercial Reuse Flywheel

**Purpose:** Explain the commercial value of platform-first engineering.

**Key message:** Each deployment should improve the reusable platform instead of creating isolated custom code.

**Main visual approach:** Circular flywheel.

**Include:**

- Common Platform Architecture
- Configurable Product Expression
- Faster Deployment
- Field Learning
- Platform Improvement
- Reusable Capabilities
- Lower Marginal Deployment Cost
- Stronger Product / Licensee Value

**Export filename:** `figure-16-commercial-reuse-flywheel.png`

---

## 11. Figure 19 — EPAS Strategic Summary

**Purpose:** Summarize the full EPAS argument in one executive figure.

**Key message:** EPAS defines a reusable architecture for configurable, recoverable, auditable, hardware-adaptable, commercially scalable edge transaction systems.

**Main visual approach:** Central EPAS block with six surrounding strategic blocks.

**Include:**

- Governed Edge Execution
- Configurable Workflow Variation
- Durable Transaction Integrity
- Hardware-Adaptable Local Control
- Backend Alignment and Reconciliation
- Commercial and Strategic Leverage

**Export filename:** `figure-19-epas-strategic-summary.png`

---

## 12. Canva Production Plan

Create or update a Canva design named:

`EPAS Specification Figures`

Recommended page structure:

- Page 1: Figure 1
- Page 2: Figure 2
- Page 3: Figure 3
- Page 4: Figure 6
- Page 5: Figure 8
- Page 6: Figure 11
- Page 7: Figure 16
- Page 8: Figure 19

---

## 13. Review Checklist

Before a figure is accepted, verify:

- correct figure number,
- correct title,
- caption alignment,
- Toren / EPAS naming,
- clear responsibility boundaries,
- readable at document and slide size,
- no unnecessary product-specific naming.

---

## 14. Next Step

Start Canva production with Figure 1 and Figure 3. Once those establish the visual style, complete the remaining six priority figures.
