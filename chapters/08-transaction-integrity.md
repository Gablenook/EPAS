# Chapter 8 — Transaction Integrity

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Chapter framework / pending expansion  
**Primary Figure:** Figure 8 — Transaction Journal and Recovery Model

---

## 8.1 Purpose

Transaction Integrity protects the platform from losing the truth of what happened during physical operations. It is the operational mechanism that makes the runtime lifecycle in **Figure 6** recoverable.

## Figure 8 — Transaction Journal and Recovery Model

> **Diagram Placeholder:** Create a journal-centered diagram. Inputs: runtime transaction steps, hardware events, backend calls, local state updates. Center: durable transaction journal with states Created, Authorized, DoorOpened, LocalStateUpdated, AckPending, AckSucceeded, AckFailed, NeedsReconciliation, Completed, Abandoned. Outputs: startup recovery, retry ACK, administrative review, reconciliation request, audit evidence.

**Caption:** Figure 8 — Transaction Integrity preserves local truth and provides a recovery path when transactions are interrupted or acknowledgements fail.

## 8.2 Transaction Journal

The platform should maintain a durable transaction journal for critical workflows. A journal entry should include:

- Request ID.
- Transaction ID.
- Command ID.
- Correlation ID.
- Workflow key.
- Workflow action.
- Actor ID or credential reference.
- Asset, package, or device reference.
- Locker ID or locker number.
- Action type.
- Current transaction state.
- Timestamps for major transitions.
- Error and retry information.

## 8.3 Transaction States

Representative transaction states include:

- Created.
- Authorized.
- DoorOpened.
- LocalStateUpdated.
- AckPending.
- AckSucceeded.
- AckFailed.
- NeedsReconciliation.
- Completed.
- Abandoned.

These states should align with **Figure 8** and with the custody-state model shown in **Figure 7**.

## 8.4 Recovery Principle

Startup recovery must inspect incomplete transactions and move them toward a safe state. The platform should never rely on operator memory to reconstruct whether a door opened or an asset was staged.

## 8.5 Boundary Rule

Transaction Integrity owns durable transaction progress and recovery state. It does not decide business eligibility, does not select user-interface copy, and does not directly command hardware. It preserves the evidence needed to determine what happened and what must happen next.
