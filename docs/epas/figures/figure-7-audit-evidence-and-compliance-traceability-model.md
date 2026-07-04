# Figure 7 — Audit Evidence and Compliance Traceability Model

**Canva design:** https://www.canva.com/d/MD1xqMvLBQeZN0H

**Figure caption:**  
Figure 7 — EPAS captures audit evidence from identity, authorization, workflow context, hardware execution, observed state, acknowledgement, reconciliation, and exception review to preserve end-to-end traceability.

## Purpose

This figure describes how Toren EPAS captures audit evidence across the full edge transaction and connects that evidence to enterprise compliance, reconciliation, exception review, and operational traceability. It emphasizes that evidence is collected from the transaction itself rather than assembled after the fact.

## Primary components

- Toren Edge Platform
- Workflow Orchestration
- Enterprise Authorization Client
- Credential / Scan Intake
- Hardware Control Adapter
- Local State Store
- Transaction Journal
- Audit Evidence Capture
- Evidence Store
- Event Log / Audit Trail
- Acknowledgement Service
- Reconciliation Service
- Exception Review
- Administrative Console
- Enterprise Systems
- Audit / Compliance Consumers
- Operator Identity
- Asset / Package / Work Order Reference
- Compartment / Door / Sensor Status

## Evidence categories

- **Who:** operator identity, credential, role, authorization context
- **What:** asset, package, work order, device, action type
- **Where:** site, kiosk, locker bank, compartment
- **When:** request time, authorization time, command time, door/status time, ACK time
- **How:** workflow key, command result, controller response, recovery path
- **Outcome:** completed, ACK pending, reconciled, exception review

## Flow intent

1. Credential / Scan Intake and Workflow Orchestration provide identity, reference, workflow, and action context to Audit Evidence Capture.
2. Enterprise Authorization Client contributes authorization request, decision, policy, entitlement, and actor context.
3. Hardware Control Adapter contributes command, controller response, door status, sensor status, and physical execution evidence.
4. Local State Store and Transaction Journal provide state snapshots and transaction progression.
5. Audit Evidence Capture writes normalized evidence records to Evidence Store and Event Log / Audit Trail.
6. Acknowledgement Service sends completion evidence back to Enterprise Systems.
7. Reconciliation Service sends recovery and reconciliation evidence back to Enterprise Systems when ACK or connectivity is interrupted.
8. Audit / Compliance Consumers receive traceable evidence views or exports.
9. Administrative Console supports exception review, evidence lookup, diagnostics, and manual resolution.
10. Exception Review remains tied back to the original transaction journal, evidence records, and reconciliation state.

## Key callout

**Evidence is captured from authorization, execution, observed state, acknowledgement, and recovery — not added after the fact.**

## Color palette guidance

Use the same controlled technical-spec palette as Figures 1 through 6.

| Role | Suggested color direction | Purpose |
|---|---|---|
| Background | Warm off-white / very light gray | Calm document background |
| Main text | Dark charcoal | Primary readability |
| Component outlines | Soft slate / blue-gray | Structural definition |
| Normal arrows | Muted steel-blue | Standard context and process flow |
| Enterprise authority accent | Muted amber | Authorization / policy / decision context |
| Evidence/traceability accent | Soft teal | Audit evidence, ACK, reconciliation, exception review |

## Design notes

- Keep most components neutral: white fill, slate outline, charcoal text.
- Use teal for evidence movement, traceability, ACK, reconciliation, and exception review.
- Use amber only for enterprise authorization / policy decision context.
- Place Audit Evidence Capture prominently as the central evidence aggregator.
- Show persistence stores as a supporting foundation: Transaction Journal, Local State Store, Evidence Store, and Event Log / Audit Trail.
- Avoid dark backgrounds, neon colors, gradients, cyber-style design, dramatic shadows, or excessive saturation.
- Preserve a readable technical architecture layout suitable for specification use.
