# Figure 5 — Operational State and Recovery Model

**Canva design:** https://www.canva.com/d/h_MrKJW5ID2n4Vv

**Figure caption:**  
Figure 5 — Local journaling, state storage, evidence capture, recovery services, and reconciliation ensure that interrupted edge transactions remain visible, recoverable, and auditable.

## Purpose

This figure describes how Toren EPAS preserves operational state locally, detects incomplete or interrupted transactions, and recovers or reconciles them with enterprise systems. It expands the transaction lifecycle from Figure 3 by showing the persistence and recovery mechanisms that keep physical execution auditable even when acknowledgement, connectivity, or downstream enterprise updates are interrupted.

## Primary states

- Transaction Created
- Authorization Context Captured
- Compartment Assigned
- Hardware Command Issued
- Door / Sensor Status Observed
- Local State Updated
- Evidence Captured
- ACK Pending
- ACK Succeeded
- Transaction Complete
- ACK Failed
- Needs Reconciliation
- Exception Review
- Recovered / Replayed / Corrected

## Core components

- Transaction Journal
- Local State Store
- Audit Evidence Store
- Recovery Service
- Reconciliation Service
- Administrative Console
- Enterprise Systems
- Hardware Controllers
- Physical Compartments

## Flow intent

1. A Transaction Journal entry is created early, before hardware execution.
2. Local State Store records compartment status, occupancy, workflow state, and recovery metadata.
3. Hardware execution updates local state through observed door and sensor status.
4. Audit Evidence Store receives event and evidence records.
5. ACK Pending represents the handoff from local execution back to Enterprise Systems.
6. ACK Succeeded leads to Transaction Complete.
7. ACK Failed leads to Recovery Service and Reconciliation Service.
8. Needs Reconciliation and Exception Review are controlled unresolved states, not lost failures.
9. Administrative Console supports manual review, correction, replay, and service intervention.
10. Recovered / Replayed / Corrected flows back toward ACK Pending or Transaction Complete.

## Local persistence foundation

The diagram should emphasize a local persistence foundation containing:

- **Transaction Journal** for durable transaction progression and recovery context.
- **Local State Store** for compartment status, occupancy, workflow state, and operational metadata.
- **Audit Evidence Store** for event history and evidence records.

## Key callout

**Incomplete transactions are recoverable because state is written before and after physical execution.**

## Color palette guidance

Use the same controlled technical-spec palette as Figures 1 through 4.

| Role | Suggested color direction | Purpose |
|---|---|---|
| Background | Warm off-white / very light gray | Calm document background |
| Main text | Dark charcoal | Primary readability |
| State and component outlines | Soft slate / blue-gray | Structural definition |
| Normal arrows | Muted steel-blue | Standard transaction and state flow |
| Enterprise authority accent | Muted amber | Authorization / authority / decision points |
| Evidence/state/recovery accent | Soft teal | ACK / reconciliation / evidence / recovery |

## Design notes

- Keep most states and components neutral: white fill, slate outline, charcoal text.
- Use teal sparingly for ACK, recovery, reconciliation, evidence, and state feedback.
- Use amber only where enterprise authorization or decision authority is represented.
- Show Needs Reconciliation and Exception Review as managed states rather than terminal failures.
- Avoid dark backgrounds, neon colors, gradients, cyber-style design, dramatic shadows, or excessive saturation.
- Preserve a readable state-machine or lifecycle-loop structure suitable for a technical specification.
