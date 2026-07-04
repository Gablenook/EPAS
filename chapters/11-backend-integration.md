# Chapter 11 — Backend Integration

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Expanded chapter draft  
**Primary Figure:** Figure 11 — Edge-to-Backend Responsibility Split

---

## 11.1 Purpose

Backend Integration connects edge execution with enterprise authority. It defines how the Toren Edge Platform validates actors, credentials, assets, packages, work orders, permissions, reservations, acknowledgements, reconciliation events, configuration distribution, and audit ingestion with backend systems.

Backend Integration is the Platform Technology that makes enterprise authority explicit while preserving the edge platform’s responsibility for local physical execution truth.

## 11.2 Problem Addressed

Edge systems become fragile when backend calls rely on hidden assumptions. If kiosk identity, locker bank identity, workflow key, workflow action, actor identity, request ID, or correlation ID is missing, backend systems cannot reliably determine what physical event occurred or which edge node produced it.

Backend Integration addresses this by defining explicit contracts between enterprise authority and edge execution. It clarifies what the backend owns, what the edge owns, and what context must pass between them.

## Figure 11 — Edge-to-Backend Responsibility Split

> **Diagram Placeholder:** Create a two-column responsibility diagram. Left column: Enterprise Backend, including business rules, actor authority, asset master records, reservation authority, reporting, enterprise audit, configuration distribution, and long-term business records. Right column: Edge Platform, including credential capture, physical execution, compartment state, hardware commands, local transaction journal, local audit, ACK/retry, offline continuity, and reconciliation evidence. Add a center lane for API contracts: validate, authorize, ACK, reconcile, configuration sync, audit ingest, and health/status.

**Caption:** Figure 11 — Enterprise systems govern business authority; edge systems execute physical operations and preserve local truth until acknowledgement or reconciliation completes.

## 11.3 Primary Responsibilities

Backend Integration owns:

- API transport and endpoint configuration.
- Request/response DTO structure.
- Validation calls.
- Authorization calls.
- ACK calls.
- Reconciliation calls.
- Configuration sync where applicable.
- Backend error classification.
- Retry policy for backend communication.
- Interpretation of backend responses.
- Correlation between local transaction records and backend records.
- Observability of backend communication.

Backend Integration should make every enterprise-facing transaction explicit, traceable, and reviewable.

## 11.4 Backend Integration Responsibilities

Backend services typically provide:

- Actor validation.
- Credential validation.
- Asset, package, device, or work-order validation.
- Permission evaluation.
- Reservation creation or confirmation.
- Locker or compartment authorization.
- Transaction acknowledgement.
- Reconciliation processing.
- Configuration distribution.
- Audit ingestion.
- Reporting and enterprise record ownership.

The backend may own business authority, but it does not erase or replace the local edge record of physical execution.

## 11.5 Edge-to-Backend Contract

Every backend request should include enough identity and context for governance:

- Kiosk ID or edge-node ID.
- Locker bank or controlled-device group ID.
- Site or location ID.
- Client, tenant, customer, or licensee code.
- Workflow key.
- Workflow action.
- Workflow version where available.
- Actor ID or credential reference where applicable.
- Request ID.
- Transaction ID.
- Correlation ID.
- Timestamp.
- Relevant asset, package, device, work order, or reference values.
- Selected compartment or controlled-device identifier when applicable.
- Requested action and resulting action state when applicable.

The contract should be reviewed whenever workflow, custody, runtime, security, or ACK behavior changes.

## 11.6 Boundaries and Non-Responsibilities

Backend Integration owns enterprise communication, not local physical truth.

Boundary examples:

- Backend Integration may receive authorization; Runtime Orchestration coordinates the local transaction.
- Backend Integration may report backend acceptance; Transaction Integrity records whether ACK succeeded locally.
- Backend Integration may validate asset eligibility; Custody Governance determines local custody-state meaning.
- Backend Integration may distribute workflow configuration; Configurable Workflow Engine owns workflow interpretation.
- Backend Integration may accept audit evidence; Cross-Cutting Services and Transaction Integrity preserve local evidence.

Backend Integration should not erase local evidence when backend calls fail.

## 11.7 Interfaces and Collaborators

Backend Integration collaborates with:

- **Runtime Orchestration** for validation, authorization, ACK, and reconciliation calls.
- **Configurable Workflow Engine** for workflow context and validation profile selection.
- **Custody Governance** for custody transition meaning and reconciliation content.
- **Transaction Integrity** for ACK status, retry state, and transaction correlation.
- **Local Persistence** for queued requests, cached config, and retry records.
- **Security Architecture** for API authentication, service identity, certificates, and tokens.
- **Administrative Services** for manual retry, reconciliation review, and diagnostics.
- **Cross-Cutting Services** for logging, correlation, diagnostics, serialization, and error classification.

## 11.8 Operational Model

A typical backend integration sequence includes:

1. Runtime Orchestration creates transaction context.
2. Backend Integration prepares a request with explicit identity and workflow context.
3. Security Architecture supplies API authority or service identity.
4. Backend validates or authorizes the requested action.
5. Runtime Orchestration proceeds or fails based on response.
6. Local physical execution occurs through governed platform services.
7. Backend Integration sends ACK after local state and transaction evidence are available.
8. ACK succeeds, fails, retries, or moves to reconciliation.
9. Administrative Services may review unresolved backend communication failures.

## 11.9 Failure Modes

Representative failure modes include:

- Backend unavailable.
- Timeout.
- Authentication failure.
- Authorization rejection.
- Validation rejection.
- Missing identity field.
- Workflow key/action mismatch.
- Backend rejects ACK.
- Duplicate ACK.
- Local transaction exists but backend record missing.
- Backend record exists but local transaction incomplete.
- Configuration sync stale or incompatible.
- Reconciliation request rejected.

Backend failures after local physical action must preserve local evidence and move toward retry or reconciliation.

## 11.10 Configuration Model

Backend configuration may include:

- Endpoint URLs.
- Environment name.
- Tenant/customer/licensee context.
- API credentials or certificates.
- Timeout settings.
- Retry policy.
- Validation profile mapping.
- ACK endpoint mapping.
- Reconciliation endpoint mapping.
- Configuration sync policy.
- Diagnostic verbosity.

Configuration should be explicit, protected, and inspectable by authorized support personnel.

## 11.11 Security and Audit Considerations

Backend Integration is a security boundary between local physical execution and enterprise authority.

Security and audit requirements include:

- API authentication should be explicit.
- Kiosk and locker bank identity should be protected from spoofing.
- Sensitive tokens, secrets, and certificates should be protected.
- Backend requests should carry correlation identifiers.
- Failed requests should be logged without exposing secrets.
- ACK and reconciliation records should preserve original transaction evidence.
- Administrative retry should be permissioned and audited.

## 11.12 Implementation Alignment Note

Current locker-based implementation evidence demonstrates why this contract matters. Stage, checkout, and ACK flows must propagate the active workflow key, workflow action, kiosk identity, locker bank identity, and actor identity through validation, authorization, local state update, acknowledgement, and recovery. Any missing identity field weakens governance because the backend cannot reliably distinguish which edge node, locker bank, actor, workflow, or action produced the physical event.

## 11.13 Commercial Significance

Backend Integration is commercially significant because repeatable integration patterns reduce deployment cost and make new enterprise environments easier to support. The clearer the contract, the easier it is to license, implement, test, and defend the platform across customers and products.

## 11.14 IP Significance

Backend Integration contributes to Toren's IP position by defining the explicit split between enterprise authority and edge execution, along with the contract model that preserves workflow, identity, custody, transaction, ACK, and reconciliation context.

## 11.15 Related Implementation Evidence

Candidate evidence may include:

- Validate DTOs.
- Authorize DTOs.
- ACK DTOs.
- Reconcile DTOs.
- API service methods.
- Request ID and correlation ID propagation.
- Backend error logs.
- Retry queues.
- Configuration sync records.
- Authentication configuration.

## 11.16 Boundary Rule

Backend Integration owns API transport, contracts, request/response interpretation, retry behavior, backend communication observability, and enterprise communication context. It does not own physical execution truth and should not erase local transaction evidence when backend calls fail.
