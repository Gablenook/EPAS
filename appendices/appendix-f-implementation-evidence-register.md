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
| Naming and ownership | Document control, naming rule, glossary, platform/product/deployment language | Supports Toren ownership and EPAS reference-architecture clarity. |
| Platform technology taxonomy | Responsibility matrix, chapter boundaries, Platform Technology definitions | Supports platform-first architecture and responsibility ownership. |
| Commissioning | Commissioning screens, kiosk identity records, locker bank identity, controller branch mapping, initial status records | Supports identity-bound edge-node setup and repeatable deployment readiness. |
| Workflow configuration | Workflow definition JSON, workflow keys, workflow actions, validation profiles, enabled workflow lists | Supports configuration-before-customization and workflow versioning. |
| Runtime orchestration | Transaction execution services, screen progression, validation/authorization sequence, assignment flow | Supports governed physical-edge execution. |
| Custody governance | Locker status records, asset status transitions, compartment state, defect handling, reservation records | Supports custody-state model and reconciliation. |
| Transaction integrity | Transaction journal table, transaction state enum, recovery service, ACK retry records | Supports local-first recovery and operational trust. |
| Hardware abstraction | Scanner service, reader adapter, locker controller service, controller branch mapping, hardware diagnostic logs | Supports hardware independence and adapter principle. |
| Local persistence | SQLite schema, configuration records, locker bank records, journal records, reconciliation queue | Supports durable local operational memory. |
| Backend integration | Validate, authorize, ACK, reconcile DTOs and service methods, request/correlation IDs | Supports explicit edge-to-backend contract. |
| Cross-cutting services | Structured logs, audit logs, error classification, health checks, support exports | Supports traceability and supportability. |
| Security architecture | Actor validation, role/permission records, kiosk identity, API credentials, protected configuration | Supports trust boundaries and permissioned physical action. |
| Administrative services | Admin diagnostics, locker status review, controller tests, recovery tools, reconciliation actions | Supports governed support and recovery. |
| Deployment architecture | Installer package, app settings, runtime dependencies, hardware drivers, support export, rollback notes | Supports repeatable deployment and supportability. |
| Commercial architecture | Reuse examples, deployment learning, product packaging, licensee assumptions, customer proposals | Supports commercial platform leverage. |
| Future evolution | Roadmap notes, prototypes, feature flags, support incident patterns, candidate Platform Technology notes | Supports deliberate platform evolution. |
| IP strategy | GitHub history, diagrams, glossary, implementation evidence, chapter revisions, legal-review notes | Supports defensible platform vocabulary and future IP work. |

## F.3 Evidence Quality Levels

Evidence can be classified by maturity:

- **Observed** — The behavior or artifact exists in a working implementation.
- **Documented** — The behavior or artifact is described in EPAS, tickets, code comments, or support notes.
- **Validated** — The behavior or artifact has been tested, reviewed, or demonstrated.
- **Deployed** — The behavior or artifact is present in a customer or field deployment.
- **Reusable** — The behavior or artifact is structured for platform reuse beyond one deployment.

## F.4 Evidence Capture Rule

When a chapter is expanded or a major implementation feature is completed, Appendix F should be updated with evidence references. Evidence should include file names, service names, DTOs, database tables, logs, configuration records, or deployment artifacts wherever practical.

## F.5 Evidence Review Checklist

For each evidence item, ask:

- Which Platform Technology does it support?
- Does it prove architecture or only implementation detail?
- Is it reusable across deployments?
- Does it support operational trust, custody, transaction integrity, or backend authority?
- Is it safe to share externally, or should it remain internal?
- Does it support commercial or IP positioning?

## F.6 Future Expansion

Future versions of this appendix should include direct references to repository paths, DTO names, service names, database tables, figure numbers, support logs, and customer deployment evidence.
