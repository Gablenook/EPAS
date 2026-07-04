# Appendix F — Implementation Evidence Register

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Expanded appendix draft

---

## F.1 Purpose

This appendix is a working register for connecting EPAS architecture to implementation evidence. It should be expanded as the codebase, logs, configuration files, deployment artifacts, diagrams, and customer implementation records mature.

The register helps convert architecture from description into defensible evidence. It supports engineering review, customer communication, support readiness, commercial reuse, and future IP strategy.

## F.2 Evidence Register

| Evidence Area | Candidate Implementation Evidence | EPAS Relevance |
| --- | --- | --- |
| Naming and ownership | Document control, naming rule, glossary, platform/product/deployment language, `EdgePlatformArchitectureSpecification-v1.9.md` | Supports Toren ownership and EPAS reference-architecture clarity. |
| Platform technology taxonomy | Responsibility matrix, chapter boundaries, Platform Technology definitions, `appendices/appendix-a-platform-technology-responsibility-matrix.md` | Supports platform-first architecture and responsibility ownership. |
| Commissioning | Commissioning screens, kiosk identity records, locker bank identity, controller branch mapping, initial status records, commissioning ID flow, controller port A/B setup | Supports identity-bound edge-node setup and repeatable deployment readiness. |
| Workflow configuration | Workflow definition JSON, workflow keys, workflow actions, validation profiles, enabled workflow lists, `KioskWorkflowConfiguration`, `WorkflowDefinition`, `DefaultWorkflowKey`, `EnabledWorkflows`, `ScanValidationProfiles` | Supports configuration-before-customization and workflow versioning. |
| Runtime orchestration | Transaction execution services, screen progression, validation/authorization sequence, assignment flow, runtime context carrying workflow key/action, compartment assignment service | Supports governed physical-edge execution. |
| Custody governance | Locker status records, asset status transitions, compartment state, defect handling, reservation records, `LockerStatus`, current asset/package references, defect option handling | Supports custody-state model and reconciliation. |
| Transaction integrity | Transaction journal table, transaction state enum, recovery service, ACK retry records, `LockerTransactionJournal`, `LockerTransactionRecoveryService`, ACK-pending/ACK-failed records | Supports local-first recovery and operational trust. |
| Hardware abstraction | Scanner service, reader adapter, locker controller service, controller branch mapping, hardware diagnostic logs, `BarcodeScanService`, credential reader adapters, `LockerControllerService`, controller branch A/B mapping | Supports hardware independence and adapter principle. |
| Local persistence | SQLite schema, configuration records, locker bank records, journal records, reconciliation queue, `Locker`, `LockerStatus`, local configuration tables, local database initialization | Supports durable local operational memory. |
| Backend integration | Validate, authorize, ACK, reconcile DTOs and service methods, request/correlation IDs, `AssetValidateRequest`, `LockerAuthorizeRequestDto`, `LockerAckRequestDto`, backend service calls | Supports explicit edge-to-backend contract. |
| Cross-cutting services | Structured logs, audit logs, error classification, health checks, support exports, `FileAuditLogger`, correlation ID traces, diagnostic exports | Supports traceability and supportability. |
| Security architecture | Actor validation, role/permission records, kiosk identity, API credentials, protected configuration, actor ID propagation, API authentication settings | Supports trust boundaries and permissioned physical action. |
| Administrative services | Admin diagnostics, locker status review, controller tests, recovery tools, reconciliation actions, admin incomplete transaction review, manual compartment test, out-of-service actions | Supports governed support and recovery. |
| Deployment architecture | Installer package, app settings, runtime dependencies, hardware drivers, support export, rollback notes, application runtime, driver/DLL dependencies, SQLite database location | Supports repeatable deployment and supportability. |
| Commercial architecture | Reuse examples, deployment learning, product packaging, licensee assumptions, customer proposals, executive briefing language, Canva deck alignment | Supports commercial platform leverage. |
| Future evolution | Roadmap notes, prototypes, feature flags, support incident patterns, candidate Platform Technology notes, remote commissioning concepts, advanced reconciliation concepts | Supports deliberate platform evolution. |
| IP strategy | GitHub history, diagrams, glossary, implementation evidence, chapter revisions, legal-review notes, `EPAS-Continuity-Review-v1.9.md`, figure placeholders, Canva artifacts | Supports defensible platform vocabulary and future IP work. |

## F.3 Concrete Evidence Anchors

The following implementation anchors should be used when assembling legal-review notes, engineering proof summaries, customer technical appendices, or future publication evidence tables. Names may be refined as the implementation repository is reviewed in detail.

| Anchor | Evidence Type | Relevant EPAS Area |
| --- | --- | --- |
| `KioskWorkflowConfiguration` | Workflow configuration object | Configurable Workflow Engine |
| `WorkflowDefinition` | Workflow definition object | Configurable Workflow Engine |
| `DefaultWorkflowKey` / `HomePickupWorkflowKey` / `HomeDeliveryWorkflowKey` | Workflow selection settings | Configurable Workflow Engine |
| `EnabledWorkflows` | Workflow enablement list | Configurable Workflow Engine / Administration |
| `ScanValidationProfiles` | Validation profile configuration | Workflow / Backend Integration |
| `AssetValidateRequest` | Backend validation DTO | Backend Integration |
| `LockerAuthorizeRequestDto` | Backend authorization DTO | Backend Integration |
| `LockerAckRequestDto` | Backend acknowledgement DTO | Backend Integration / Transaction Integrity |
| `LockerTransactionJournal` | Durable transaction journal table | Transaction Integrity / Local Persistence |
| `LockerTransactionRecoveryService` | Startup/incomplete transaction recovery service | Transaction Integrity / Administrative Services |
| `LockerActionService` | Runtime action coordination service | Runtime Orchestration |
| `LockerControllerService` | Hardware control service | Hardware Abstraction |
| `BarcodeScanService` | Scanner input service | Hardware Abstraction / Workflow |
| `FileAuditLogger` | File-based audit evidence | Cross-Cutting Services / Audit |
| `Locker` table | Local compartment or locker identity records | Local Persistence / Commissioning |
| `LockerStatus` table | Local compartment or locker state records | Local Persistence / Custody Governance |
| Controller branch A/B mapping | Hardware topology configuration | Commissioning / Hardware Abstraction |
| Admin locker status review | Administrative diagnostic view | Administrative Services |
| Manual compartment/controller test | Administrative hardware diagnostic action | Administrative Services / Hardware Abstraction |
| ACK retry/reconciliation records | Recovery and backend alignment evidence | Transaction Integrity / Backend Integration |

## F.4 Evidence Quality Levels

Evidence can be classified by maturity:

- **Observed** — The behavior or artifact exists in a working implementation.
- **Documented** — The behavior or artifact is described in EPAS, tickets, code comments, or support notes.
- **Validated** — The behavior or artifact has been tested, reviewed, or demonstrated.
- **Deployed** — The behavior or artifact is present in a customer or field deployment.
- **Reusable** — The behavior or artifact is structured for platform reuse beyond one deployment.

## F.5 Evidence Capture Rule

When a chapter is expanded or a major implementation feature is completed, Appendix F should be updated with evidence references. Evidence should include file names, service names, DTOs, database tables, logs, configuration records, or deployment artifacts wherever practical.

## F.6 Evidence Review Checklist

For each evidence item, ask:

- Which Platform Technology does it support?
- Does it prove architecture or only implementation detail?
- Is it reusable across deployments?
- Does it support operational trust, custody, transaction integrity, or backend authority?
- Is it safe to share externally, or should it remain internal?
- Does it support commercial or IP positioning?

## F.7 Future Expansion

Future versions of this appendix should include direct references to repository paths, DTO names, service names, database tables, figure numbers, support logs, and customer deployment evidence. The next evidence pass should inspect the implementation repository and replace candidate anchor names with verified file paths and line references where practical.
