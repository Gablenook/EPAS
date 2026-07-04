# Appendix F — Implementation Evidence Register

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Appendix framework / pending expansion

---

This appendix is a working register for connecting EPAS architecture to implementation evidence. It should be expanded as the codebase, logs, configuration files, and deployment artifacts mature.

| Evidence Area | Candidate Implementation Evidence | EPAS Relevance |
| --- | --- | --- |
| Workflow configuration | Workflow definition JSON, workflow keys, workflow actions, validation profiles | Supports configuration-before-customization and workflow versioning. |
| Runtime orchestration | Transaction execution services, screen progression, validation/authorization sequence | Supports governed physical-edge execution. |
| Transaction integrity | Transaction journal table, recovery service, ACK retry records | Supports local-first recovery and operational trust. |
| Custody governance | Locker status records, asset status transitions, defect handling | Supports custody-state model and reconciliation. |
| Backend integration | Validate, authorize, ACK, reconcile DTOs and service methods | Supports explicit edge-to-backend contract. |
| Hardware abstraction | Scanner service, reader adapter, locker controller service, controller branch mapping | Supports hardware independence and adapter principle. |
| Local persistence | SQLite schema, configuration records, locker bank records, journal records | Supports durable local operational memory. |
| Administrative services | Admin diagnostics, locker status review, controller tests, recovery tools | Supports governed support and recovery. |
| Deployment architecture | Installer package, app settings, runtime dependencies, hardware drivers, support export | Supports repeatable deployment and supportability. |
