# Chapter 11 — Backend Integration

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Chapter framework / pending expansion  
**Primary Figure:** Figure 11 — Edge-to-Backend Responsibility Split

---

## 11.1 Purpose

Backend Integration connects edge execution with enterprise authority. It validates credentials, assets, packages, work orders, permissions, reservations, acknowledgements, and reconciliation events.

## Figure 11 — Edge-to-Backend Responsibility Split

> **Diagram Placeholder:** Create a two-column responsibility diagram. Left column: Enterprise Backend, including business rules, actor authority, asset master records, reservation authority, reporting, enterprise audit, configuration distribution. Right column: Edge Platform, including credential capture, physical execution, locker state, hardware commands, local transaction journal, local audit, ACK/retry, offline continuity. Add a center lane for API contracts: validate, authorize, ACK, reconcile, configuration sync.

**Caption:** Figure 11 — Enterprise systems govern business authority; edge systems execute and preserve the truth of local physical operations.

## 11.2 Integration Responsibilities

Backend services typically provide:

- Actor validation.
- Credential validation.
- Asset or package validation.
- Locker authorization.
- Reservation creation or confirmation.
- Transaction acknowledgement.
- Reconciliation processing.
- Configuration distribution.
- Audit ingestion.

## 11.3 Edge-to-Backend Contract

Every backend request should include enough identity and context for governance:

- Kiosk ID.
- Locker bank ID.
- Site or location ID.
- Client or tenant code.
- Workflow key.
- Workflow action.
- Actor ID where applicable.
- Request ID.
- Timestamp.
- Correlation ID.
- Relevant asset, package, device, or reference values.

## 11.4 Integration Principle

Backend integration should be explicit and observable. Silent assumptions about identity, workflow, actor, or action type create fragile systems. The explicit contract lane in **Figure 11** should become the reference point for API review.

## 11.5 Implementation Alignment Note

Current locker-based implementation evidence demonstrates why this contract matters. Stage, checkout, and ACK flows must propagate the active workflow key, workflow action, kiosk identity, locker bank identity, and actor identity through validation, authorization, local state update, acknowledgement, and recovery. Any missing identity field weakens governance because the backend cannot reliably distinguish which edge node, locker bank, actor, workflow, or action produced the physical event.

## 11.6 Boundary Rule

Backend Integration owns API transport, contracts, request/response interpretation, retry behavior, and backend communication observability. It does not own physical execution truth and should not erase local transaction evidence when a backend call fails.
