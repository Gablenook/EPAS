# Chapter 8 — Transaction Integrity

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Expanded chapter draft  
**Primary Figure:** Figure 8 — Transaction Journal and Recovery Model

---

## 8.1 Purpose

Transaction Integrity protects the Toren Edge Platform from losing the truth of what happened during governed physical-edge operations. It provides the durable transaction journal, state progression, recovery model, ACK tracking, retry path, and reconciliation evidence needed when runtime execution is interrupted, partially completed, rejected, or ambiguous.

Transaction Integrity is the Platform Technology that turns physical-edge execution into recoverable operational truth.

## 8.2 Problem Addressed

Physical-edge transactions are not ordinary screen events. Once a compartment opens, a relay fires, a device is released, or an object is placed into custody, the platform must be able to explain what happened even if the application restarts, the network fails, the operator walks away, backend acknowledgement is rejected, or support must intervene later.

Without Transaction Integrity, the system may know that a workflow began but not whether the door opened, whether local state changed, whether ACK failed, or whether reconciliation is required. That creates operational risk and support ambiguity.

## Figure 8 — Transaction Journal and Recovery Model

> **Diagram Placeholder:** Create a journal-centered diagram. Inputs: workflow context, validation results, authorization results, compartment selection, hardware events, local state updates, backend calls, errors, retries, and administrative actions. Center: durable transaction journal with states Created, Validated, Authorized, CompartmentAssigned, DoorCommanded, DoorOpened, PhysicalActionConfirmed, LocalStateUpdated, AckPending, AckSucceeded, AckFailed, NeedsReconciliation, Completed, Failed, Abandoned. Outputs: startup recovery, ACK retry, administrative review, reconciliation request, support export, and audit evidence.

**Caption:** Figure 8 — Transaction Integrity preserves local transaction truth and provides recovery, retry, audit, and reconciliation paths when governed physical transactions are interrupted or incomplete.

## 8.3 Primary Responsibilities

Transaction Integrity owns:

- Durable transaction journal structure.
- Transaction state vocabulary.
- Transaction state progression rules.
- Required transaction identifiers and correlation fields.
- Recording of major runtime milestones.
- Recording of physical-action attempts and results.
- ACK state and retry status.
- Incomplete transaction detection.
- Startup recovery behavior.
- Reconciliation-required classification.
- Administrative review evidence.
- Error classification related to transaction progress.
- Preservation of original transaction evidence after failure.

Transaction Integrity does not make every runtime decision, but it preserves the evidence needed to understand and recover those decisions.

## 8.4 Transaction Journal

The platform should maintain a durable transaction journal for critical workflows. A journal entry should include:

- Request ID.
- Transaction ID.
- Command ID where applicable.
- Correlation ID.
- Workflow key.
- Workflow action.
- Workflow version or configuration reference where available.
- Actor ID or credential reference.
- Asset, package, device, work order, or reference value.
- Kiosk or edge-node ID.
- Locker bank or controlled-device group ID.
- Locker, compartment, or device identifier.
- Action type.
- Current transaction state.
- Previous transaction state where useful.
- Major timestamps.
- Validation and authorization outcomes.
- Hardware command result.
- Local state update result.
- ACK result.
- Retry count and retry status.
- Error code, error category, and diagnostic notes.
- Reconciliation status.

The transaction journal should survive application restarts and be inspectable by governed administrative tools.

## 8.5 Transaction States

Representative transaction states include:

- **Created** — Transaction context has been started.
- **Validated** — Required validation succeeded.
- **AuthorizationFailed** — Authorization was required and failed.
- **Authorized** — Required authorization succeeded.
- **CompartmentAssigned** — A compartment or controlled device was selected or reserved.
- **DoorCommanded** — Hardware action was attempted.
- **DoorOpened** — Door-open or command success evidence exists.
- **PhysicalActionConfirmed** — Physical completion was detected or confirmed where possible.
- **LocalStateUpdated** — Local operational state was updated.
- **AckPending** — Backend acknowledgement is required or queued.
- **AckSucceeded** — Backend acknowledgement succeeded.
- **AckFailed** — Backend acknowledgement failed after local action or state change.
- **RetryPending** — A retry path is available.
- **NeedsReconciliation** — Human, backend, or administrative reconciliation is required.
- **Completed** — The transaction reached a successful terminal state.
- **Failed** — The transaction failed before completion.
- **Abandoned** — The transaction was abandoned or timed out.

These states should align with Runtime Orchestration in Figure 6 and Custody Governance in Figure 7.

## 8.6 Interfaces and Collaborators

Transaction Integrity collaborates with:

- **Runtime Orchestration** to receive transaction milestones and state changes.
- **Configurable Workflow Engine** to preserve workflow key, action, and version context.
- **Custody Governance** to preserve custody transition evidence and reconciliation status.
- **Hardware Abstraction** to record command attempts, command results, and hardware event evidence.
- **Local Persistence** to store durable journal records.
- **Backend Integration** to record ACK, retry, and reconciliation status.
- **Administrative Services** to review, retry, resolve, or reconcile incomplete transactions.
- **Cross-Cutting Services** to supply timestamps, correlation IDs, logs, diagnostics, and error classification.
- **Security Architecture** to preserve actor identity and permission context where applicable.

## 8.7 Operational Model

A typical transaction integrity sequence includes:

1. Create a journal entry when governed runtime execution begins.
2. Record workflow context, actor context, identifiers, and requested action.
3. Update journal state after validation and authorization milestones.
4. Record compartment or controlled-device assignment before physical action.
5. Record hardware command attempt before or at the time of command.
6. Record hardware result or ambiguity.
7. Record local state update result.
8. Mark ACK pending before backend acknowledgement is attempted when local action has occurred.
9. Mark ACK succeeded, ACK failed, retry pending, or needs reconciliation.
10. Mark terminal completed, failed, abandoned, or reconciled state.
11. Preserve enough evidence for startup recovery and administrative review.

The journal should never skip over a physical action without durable evidence that the action was attempted, completed, failed, or ambiguous.

## 8.8 Startup Recovery

Startup recovery must inspect incomplete transactions and move them toward a safe state. The platform should never rely on operator memory to reconstruct whether a door opened or an asset was staged.

Recovery behavior should classify incomplete transactions into categories such as:

- Safe to abandon because no physical action occurred.
- Safe to retry validation or authorization.
- Physical action may have occurred; administrative review required.
- Local state changed but ACK failed; retry ACK.
- Local/backend state conflict; reconciliation required.
- Hardware state unknown; support review required.

Startup recovery should preserve the original transaction record and append recovery actions rather than rewriting history.

## 8.9 Failure Modes

Representative failure modes include:

- Journal entry cannot be created.
- Transaction state cannot be updated.
- Application crashes after authorization but before door command.
- Door command occurs but result is not recorded.
- Door opens but local state update fails.
- Local state updates but ACK fails.
- ACK succeeds but local terminal state is not recorded.
- Transaction ID or correlation ID is missing.
- Duplicate transaction or duplicate ACK occurs.
- Retry count exceeds allowed limit.
- Startup recovery cannot determine physical status.
- Administrative user resolves transaction without preserving evidence.

Failure handling should favor visibility over false completion.

## 8.10 Configuration Model

Transaction Integrity may consume configuration such as:

- Journal retention policy.
- Retry limits and retry intervals.
- ACK retry policy.
- Reconciliation thresholds.
- Timeout rules.
- Terminal-state rules.
- Recovery classification rules.
- Administrative review permissions.
- Diagnostic export settings.

Configuration should not weaken the requirement that critical physical transactions have durable evidence.

## 8.11 Security and Audit Considerations

Transaction journal records can contain sensitive operational evidence. They must be protected against unauthorized editing, deletion, or silent overwrite.

Security and audit requirements include:

- Journal changes should be append-friendly or otherwise auditable.
- Administrative recovery should record actor, timestamp, reason, and action.
- Failed ACK and reconciliation states should remain visible.
- Sensitive credential values should be protected or referenced appropriately.
- Transaction records should support support review without exposing unnecessary secrets.
- Original failure evidence should not be erased by correction actions.

## 8.12 Commercial Significance

Transaction Integrity is commercially significant because it reduces support ambiguity and builds customer trust. Customers care not only that the platform works when everything succeeds, but that it can explain what happened when something fails.

A strong transaction integrity model makes the platform more deployable, supportable, auditable, and certifiable across products and licensee implementations.

## 8.13 IP Significance

Transaction Integrity contributes to Toren's intellectual-property position by defining a durable recovery model for governed physical-edge transactions. The value is the method of preserving transaction truth across workflow, identity, hardware action, local state, backend ACK, retry, recovery, and reconciliation.

## 8.14 Related Implementation Evidence

Candidate implementation evidence may include:

- Transaction journal table schema.
- Transaction state enum.
- Recovery service logic.
- ACK retry records.
- Reconciliation queue.
- Runtime transaction context objects.
- Audit logs tied to transaction IDs.
- Error classification records.
- Startup recovery traces.
- Administrative recovery screens.

## 8.15 Boundary Rule

Transaction Integrity owns durable transaction progress, evidence, recovery classification, ACK status, retry state, and reconciliation visibility. It does not decide business eligibility, custody semantics, UI copy, hardware protocols, backend business authority, or administrative permission policy. It preserves the evidence needed to determine what happened and what must happen next.
