# Figure 3 — Edge Transaction Lifecycle Model

**Canva design:** https://www.canva.com/d/B_a_7obY_3nx7JC

**Figure caption:**  
Figure 3 — Each edge transaction is journaled before execution, coordinated through authorization and hardware control, completed with local state and audit evidence, and recovered through acknowledgement and reconciliation when interrupted.

## Purpose

This figure describes the lifecycle of a single Toren EPAS edge transaction. It shows how operator input, scan intake, workflow context, enterprise authorization, local compartment assignment, hardware control, state persistence, audit evidence, acknowledgement, and recovery are coordinated as a complete edge transaction.

## Main transaction flow

1. Operator / Device Input
2. Credential, Asset, Package, or Reference Scan
3. Workflow Context Established
4. Enterprise Authorization Request
5. Authorization Decision
6. Compartment Assignment
7. Hardware Command Issued
8. Door / Compartment Status Observed
9. Local State Updated
10. Audit Evidence Captured
11. Acknowledgement Sent
12. Transaction Completed

## Supporting persistence and recovery lane

- Transaction Journal Entry Created
- State Snapshot Stored
- ACK Pending
- Recovery / Reconciliation if interrupted
- Needs Reconciliation / Exception Review if unresolved

## External actors and systems

- **Human Operator** initiates the transaction.
- **Credential / Scan Device** supplies credential, asset, package, or reference input.
- **Enterprise Systems** provide authorization decisions and receive acknowledgements / reconciliation.
- **Hardware Controller** executes physical compartment commands.
- **Physical Compartment** provides door and compartment status.
- **Audit Evidence Store** receives transaction evidence.
- **Administrative Support** handles recovery, diagnostics, exception review, and service intervention.

## Flow intent

- Normal transaction flow uses muted steel-blue.
- Enterprise authorization request and decision use muted amber accents.
- Acknowledgement, audit evidence, reconciliation, and recovery paths use soft teal accents.
- The transaction journal begins early, before physical execution, so incomplete transactions can be recovered.
- Acknowledgement is sent after local state and audit evidence are captured.
- Interrupted or unresolved transactions move through recovery, reconciliation, and exception review.

## Color palette guidance

Use the same controlled technical-spec palette as Figures 1 and 2.

| Role | Suggested color direction | Purpose |
|---|---|---|
| Background | Warm off-white / very light gray | Calm document background |
| Main text | Dark charcoal | Primary readability |
| Step outlines | Soft slate / blue-gray | Structural definition |
| Normal arrows | Muted steel-blue | Standard transaction flow |
| Enterprise authority accent | Muted amber | Authorization request / decision |
| Evidence/state accent | Soft teal | ACK / reconciliation / evidence / recovery |

## Design notes

- Keep most transaction steps neutral: white fill, slate outline, charcoal text.
- Use amber only for enterprise authorization / authority decision points.
- Use teal only for ACK, audit evidence, reconciliation, recovery, and operational state feedback.
- Show the transaction journal and recovery lane as supporting infrastructure, not as decoration.
- Avoid dark backgrounds, neon colors, gradients, cyber-style design, dramatic shadows, or excessive saturation.
- Preserve a clear left-to-right lifecycle flow with a secondary persistence/recovery lane.
