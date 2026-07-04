# Appendix C — Glossary

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Expanded appendix draft

---

## C.1 Purpose

This glossary defines the core vocabulary used across EPAS. These terms should be used consistently in the master manuscript, chapter files, diagrams, executive summaries, Canva materials, implementation tickets, and future legal or commercial summaries.

## C.2 Terms

**ACK** — Acknowledgement sent from the edge platform to backend services indicating the result of a governed transaction.

**Actor** — A person, service, or system identity performing an action.

**Administrative Services** — Platform Technology providing governed support, diagnostics, manual tests, recovery, reconciliation, and administrative review.

**Backend Integration** — Platform Technology responsible for API contracts, validation, authorization, ACK, reconciliation, configuration sync, and enterprise communication.

**Commissioning** — The process of assigning identity, configuration, hardware mapping, and initial state to an edge node.

**Configurable Workflow Engine** — Platform Technology that expresses deployment-specific behavior through workflow configuration rather than source-code customization.

**Correlation ID** — Identifier used to trace related activity across runtime, backend calls, logs, journal entries, and audit records.

**Cross-Cutting Services** — Shared platform services such as logging, diagnostics, correlation, health checks, time services, serialization support, and support export.

**Custody** — Governed responsibility for an asset, package, device, or compartment state.

**Custody Governance** — Platform Technology defining custody states, valid transitions, exception meaning, and relationship between custody objects and physical locations.

**Deployment** — A configured instance of a product or licensed implementation for a customer, site, workflow, hardware set, and operating policy.

**Deployment Architecture** — Platform Technology defining installation, packaging, configuration delivery, upgrade, rollback, dependency, and supportability structure.

**Diagram Placeholder** — A manuscript note defining the intent, content, and caption for a future professional figure.

**Edge Node** — A deployed kiosk, locker bank controller, or other field system executing physical operations.

**EPAS** — Edge Platform Architecture Specification; the reference architecture for the Toren Edge Platform.

**Figure Register** — The numbered list of figures used to coordinate manuscript text, diagram production, Canva design work, and final publication layout.

**Hardware Abstraction** — Platform layer that isolates device-specific communication from workflow and business logic.

**Licensee** — A company or business entity authorized to implement, commercialize, manufacture, sell, operate, or distribute a product or deployment based on EPAS.

**Local Persistence** — Platform Technology providing durable local operational memory for configuration, state, journal records, diagnostics, and reconciliation.

**Locker Bank** — A physical group of controlled compartments governed by the platform.

**Operational Trust** — The ability to explain and recover the truth of physical operations even when networks, devices, or workflows fail.

**Platform Technology** — A durable architectural responsibility within the Edge Platform.

**Product** — A packaged or branded expression of the Toren Edge Platform.

**Reconciliation** — The process of resolving differences between local physical-edge records and backend enterprise records.

**Runtime Orchestration** — Platform Technology coordinating configured workflow intent, validation, authorization, custody, hardware action, local state, ACK, and reconciliation.

**Security Architecture** — Platform Technology defining trust boundaries, identity, authority, permissions, protected configuration, and sensitive-data requirements.

**Toren** — The company, platform owner, and licensor associated with the Toren Edge Platform.

**Toren Edge Platform** — The platform governed by EPAS for configurable, recoverable, auditable, hardware-adaptable physical-edge transaction execution.

**Transaction Integrity** — Platform Technology providing durable journal state, recovery classification, ACK status, retry state, and reconciliation visibility.

**Transaction Journal** — Durable local record of transaction progress used for recovery, audit, and reconciliation.

**Workflow Action** — The operational intent of a workflow, such as pickup, stage, checkout, return, deposit, release, retrieve, exchange, or inspect.

**Workflow Key** — A stable configured identifier for a workflow definition.

## C.3 Naming Rule

Toren is the platform owner and licensor. EPAS is the reference architecture. Products, licensees, customer deployments, and manufactured systems may express the platform, but they should not redefine the platform vocabulary.
