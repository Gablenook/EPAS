# Appendix A — Platform Technology Responsibility Matrix

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Expanded appendix draft

---

## A.1 Purpose

This appendix provides a consolidated responsibility matrix for the Toren Edge Platform. It is intended to help engineers, support personnel, commercial stakeholders, licensees, and documentation reviewers understand which Platform Technology owns each major responsibility and which responsibilities must remain outside that technology.

The matrix should be used during design review, implementation review, chapter editing, support analysis, and future platform planning.

## A.2 Core Responsibility Matrix

| Platform Technology | Primary Responsibility | Must Not Own | Primary Figure |
| --- | --- | --- | --- |
| Commissioning Technology | Site, kiosk, locker bank, controller, hardware topology, initial identity, and initial local state | Runtime custody decisions or live transaction recovery | Figure 4 |
| Configurable Workflow Engine | Workflow definition, workflow identity, workflow action, configuration-driven step progression | Hardware device implementation or backend business authority | Figure 5 |
| Runtime Orchestration | Coordinated execution of governed transactions | Enterprise business record ownership or low-level hardware protocols | Figure 6 |
| Custody Governance | Custody state vocabulary, valid transitions, compartment/object custody meaning | Relay-board protocols or API transport | Figure 7 |
| Transaction Integrity | Durable journal, transaction states, ACK status, recovery and reconciliation evidence | Customer-specific screen layout or business eligibility | Figure 8 |
| Hardware Abstraction | Device communication, command translation, hardware health, and physical event reporting | Business authorization or custody semantics | Figure 9 |
| Local Persistence | Durable local storage and local operational memory | Business meaning of every stored value or cloud source-of-truth policy | Figure 10 |
| Backend Integration | API contracts, enterprise communication, validation, authorization, ACK, reconciliation transport | UI rendering or local physical truth | Figure 11 |
| Cross-Cutting Services | Logging, tracing, diagnostics, correlation, time, serialization, health, support export | Workflow-specific business meaning or custody semantics | Figure 12 |
| Security Architecture | Identity, authority, permissions, secrets, trust boundaries, protected configuration | Locker assignment algorithms or workflow step progression | Figure 13 |
| Administrative Services | Governed support, diagnostics, manual tests, recovery, reconciliation, controlled override | Unlogged operational bypass or ownership of underlying state meaning | Figure 14 |
| Deployment Architecture | Installation, packaging, dependencies, upgrade, rollback, configuration delivery | Product strategy or live runtime behavior | Figure 15 |
| Commercial Architecture | Platform reuse, product/licensee/deployment value, commercial leverage | Low-level runtime implementation or legal filing decisions | Figure 16 |

## A.3 Review Rule

When a proposed feature, bug fix, customer request, or implementation change touches more than one Platform Technology, the design should identify:

1. Primary owner.
2. Supporting collaborators.
3. Data owner.
4. Failure owner.
5. Audit/evidence owner.
6. Commercial or IP relevance.

No implementation should quietly move responsibility into a screen, DTO, database table, or adapter simply because that is where the immediate code change is easiest.

## A.4 Responsibility Leakage Signals

Common signs of responsibility leakage include:

- UI code deciding custody state.
- Hardware adapters deciding business eligibility.
- Backend DTOs defining local physical truth.
- Database tables becoming the only description of platform meaning.
- Administrative tools changing state without audit evidence.
- Workflow configuration bypassing security requirements.
- Runtime orchestration absorbing all platform responsibilities.
- Product-specific naming redefining platform architecture.

## A.5 Use in Future Editing

Each chapter expansion should be checked against this matrix. If a later chapter introduces a new responsibility that does not fit the matrix, either the chapter should be corrected or the Platform Technology taxonomy in Chapter 3 should be deliberately revised.
