# Edge Platform™ Architecture Specification (EPAS)

**Version 1.0 – Authoritative Working Draft**  
**Repository:** `Gablenook/EPAS`  
**Document:** `EdgePlatformArchitectureSpecification.md`

> EPAS defines the Edge Platform architecture: the durable engineering foundation for governed physical-edge systems such as SmartLocker, asset custody kiosks, field-deployed device exchange systems, and other transaction-controlled edge operations.

---

## Contents

- Executive Summary
- Part I — Platform Foundation
  - Chapter 1 — Platform Vision
  - Chapter 2 — Architectural Principles
  - Chapter 3 — Platform Technology Architecture
  - Chapter 4 — Commissioning Technology
  - Chapter 5 — Configurable Workflow Engine
  - Chapter 6 — Runtime Orchestration
- Part II — Operational Trust and Custody
  - Chapter 7 — Custody Governance
  - Chapter 8 — Transaction Integrity
  - Chapter 9 — Hardware Abstraction
  - Chapter 10 — Local Persistence
  - Chapter 11 — Backend Integration
- Part III — Platform Operations
  - Chapter 12 — Cross-Cutting Services
  - Chapter 13 — Security Architecture
  - Chapter 14 — Administrative Services
  - Chapter 15 — Deployment Architecture
  - Chapter 16 — Commercial Architecture
- Part IV — Strategic Direction
  - Chapter 17 — Future Platform Evolution
  - Chapter 18 — Intellectual Property Strategy
  - Chapter 19 — Conclusions and Strategic Vision
- Appendix A — Platform Technology Responsibility Matrix
- Appendix B — Core Architectural Principles
- Appendix C — Glossary

---

## Executive Summary

The Edge Platform is a software and systems architecture for controlling trusted physical transactions at the operational edge. It exists for environments where enterprise systems, local devices, human operators, physical compartments, credentials, scanners, relays, doors, sensors, and audit trails must work together as one governed system.

SmartLocker is the first product expression of the platform. EPAS is broader than SmartLocker. It captures the architectural foundation that allows one platform to support package pickup, asset checkout, device staging, custody transfer, equipment exchange, inventory-controlled access, and future edge workflows without rewriting the core system for each customer.

The platform is built around a simple but powerful division of responsibility:

- Enterprise systems define business authority.
- The edge platform executes physical operations.
- Local runtime services preserve continuity when connectivity is imperfect.
- Transaction journals protect operational truth.
- Configuration expresses deployment variation.
- Hardware adapters isolate device-specific behavior.
- Audit and reconciliation make every important action explainable.

The central claim of EPAS is that edge systems should not be treated as thin user interfaces attached to cloud software. Physical edge execution has its own responsibilities. Doors open locally. Credentials are scanned locally. Relays fire locally. Compartments become occupied or vacant locally. Operators need immediate feedback locally. When the network is slow, interrupted, or unavailable, the platform must still preserve an accurate account of what happened.

EPAS therefore describes a platform-first architecture rather than a single-purpose application. It establishes the rules, technologies, boundaries, and responsibilities needed to build repeatable edge products from a common foundation.

---

# Part I — Platform Foundation

# Chapter 1 — Platform Vision

## 1.1 Purpose

The Edge Platform exists to make physical edge operations trustworthy, repeatable, configurable, and commercially reusable. It is intended for systems where software is responsible for authorizing, controlling, recording, and reconciling physical actions.

Examples include:

- A worker checking out a serialized device.
- A technician staging equipment into a locker compartment.
- A customer retrieving a package.
- A government user accessing controlled equipment.
- A field employee returning a defective asset.
- A site administrator reconciling local physical state with enterprise records.

In each case, the system must answer four questions with confidence:

1. Who performed the action?
2. What object or asset was involved?
3. What physical compartment or device was used?
4. What evidence proves the transaction occurred?

## 1.2 Platform, Product, and Deployment

EPAS distinguishes between three levels of design:

- **Platform:** The durable architecture, runtime services, transaction model, workflow model, hardware abstraction, persistence model, security model, and integration patterns.
- **Product:** A packaged expression of the platform, such as SmartLocker.
- **Deployment:** A configured instance of the product for a customer, site, workflow, hardware set, and operating policy.

This distinction is fundamental. Product features should strengthen the platform whenever possible. Deployment-specific behavior should be expressed through configuration rather than source-code forks.

## 1.3 Architectural Goal

The architectural goal is not merely to open lockers. The goal is to create a governed edge execution environment where physical action, business authorization, local state, backend state, and audit evidence remain aligned.

The platform must be:

- **Deterministic:** The same inputs should produce the same platform behavior.
- **Recoverable:** Interrupted transactions must be visible and reconcilable.
- **Configurable:** Different workflows must be supported without architectural rewrites.
- **Auditable:** Every important action must produce durable evidence.
- **Hardware-independent:** The platform must support different scanners, readers, controllers, and compartment technologies.
- **Commercially reusable:** Each customer deployment should improve the platform rather than create isolated custom code.

---

# Chapter 2 — Architectural Principles

## 2.1 Purpose

The Edge Platform is governed by a small set of architectural principles that remain constant regardless of programming language, operating system, deployment model, or hardware platform. These principles preserve architectural integrity as the platform evolves.

## 2.2 Principle 1 — Single Ownership

Every significant engineering responsibility has one architectural owner. Responsibility may be delegated for implementation, but ownership remains singular. This eliminates ambiguity, reduces duplication, and creates a clear place to improve each platform capability.

Examples:

- The workflow engine owns workflow step progression.
- The custody service owns custody-state rules.
- The hardware abstraction layer owns device interaction.
- The transaction journal owns durable transaction recovery.
- Backend integration services own enterprise communication.

## 2.3 Principle 2 — Separation of Responsibilities

Business intent, runtime execution, custody, transaction integrity, hardware control, persistence, enterprise integration, and administration are intentionally separated into independent Platform Technologies.

This separation prevents the kiosk user interface from becoming the owner of business rules, hardware details, backend contracts, and transaction recovery. The UI presents and collects information. Platform services govern execution.

## 2.4 Principle 3 — Configuration Before Customization

Deployments should differ through configuration before source-code customization. Customer-specific behavior should be expressed through workflow definitions, validation profiles, hardware mappings, site settings, and policy configuration whenever practical.

This principle makes the platform commercially scalable. It allows one product family to support Ryder-style asset workflows, Shaw-style equipment pickup, package workflows, staging workflows, and future custody use cases without fragmenting the codebase.

## 2.5 Principle 4 — Deterministic Execution

Identical operational inputs should produce identical architectural behavior. Deterministic execution simplifies diagnostics, testing, certification, recovery, support, and long-term maintenance.

Where external conditions vary, such as backend availability or hardware response timing, the platform must preserve deterministic local decisions and durable journal records.

## 2.6 Principle 5 — Operational Trust

The Edge Platform maintains trustworthy operational state even when enterprise connectivity is temporarily unavailable. Enterprise systems coordinate business operations; edge systems execute physical operations.

A physical door opening is not theoretical. Once it occurs, the edge system must record it, even if the backend cannot be reached at that moment.

## 2.7 Principle 6 — Platform Before Product

SmartLocker is an implementation of the Edge Platform. Engineering investment should strengthen the common platform before adding product-specific capability.

Product-specific names, screens, labels, and workflows may vary. The platform responsibilities should remain stable.

---

# Chapter 3 — Platform Technology Architecture

## 3.1 Overview

The platform is organized into Platform Technologies. A Platform Technology is a durable architectural responsibility with a clear owner, stable interfaces, and reusable value across deployments.

## 3.2 Core Platform Technologies

The first-generation Edge Platform includes the following technologies:

1. **Commissioning Technology** — Initializes site, kiosk, controller, locker bank, hardware, and local database identity.
2. **Configurable Workflow Engine** — Defines and executes customer workflows through configuration.
3. **Runtime Orchestration** — Coordinates credential scan, reference scan, validation, authorization, compartment assignment, hardware action, state update, ACK, and recovery.
4. **Custody Governance** — Governs asset, package, device, and compartment custody rules.
5. **Transaction Integrity** — Journals every critical step and supports recovery after interruption.
6. **Hardware Abstraction** — Isolates device-specific behavior behind stable platform interfaces.
7. **Local Persistence** — Maintains local operational state, configuration, transaction records, and diagnostics.
8. **Backend Integration** — Communicates with enterprise APIs for validation, authorization, acknowledgement, and reconciliation.
9. **Cross-Cutting Services** — Provides logging, tracing, correlation IDs, error handling, telemetry, diagnostics, and service health.
10. **Security Architecture** — Protects credentials, identities, device permissions, and operational boundaries.
11. **Administrative Services** — Enables local support, diagnostics, override workflows, commissioning review, and reconciliation.
12. **Deployment Architecture** — Defines how platform software is packaged, configured, installed, upgraded, and supported.

## 3.3 Technology Boundaries

Each Platform Technology should expose interfaces that are stable enough for other services to depend on, but narrow enough to prevent responsibility leakage. For example, the workflow engine should not directly manipulate relay boards. The hardware layer should not decide whether an asset may be checked out. Backend integration should not own local door-state truth.

---

# Chapter 4 — Commissioning Technology

## 4.1 Purpose

Commissioning Technology converts generic platform software into a site-specific edge node. It establishes identity, hardware mapping, locker topology, controller ports, local database records, and initial operational state.

## 4.2 Commissioning Responsibilities

Commissioning must capture or confirm:

- Customer identity.
- Site identity.
- Kiosk identity.
- Locker bank identity.
- Controller branch configuration.
- Locker numbers and physical positions.
- Locker sizes and zones.
- Scanner and credential-reader availability.
- Network configuration.
- Backend endpoint settings.
- Initial locker status.

## 4.3 Commissioning Outcomes

A properly commissioned edge node should be able to:

- Identify itself to backend services.
- Address every physical locker compartment correctly.
- Know which lockers are enabled, vacant, occupied, unavailable, or out of service.
- Validate local hardware communication.
- Produce a commissioning audit record.

Commissioning is not a one-time setup screen. It is a platform capability that directly affects operational trust.

---

# Chapter 5 — Configurable Workflow Engine

## 5.1 Purpose

The workflow engine allows customer-specific operational behavior to be expressed as configuration. It defines the screens, steps, references, validations, authorizations, and action semantics used by a deployment.

## 5.2 Workflow Model

A workflow definition should include:

- Workflow key.
- Display name.
- Workflow family or mode.
- Workflow action.
- Ordered steps.
- Reference labels.
- Validation profile.
- Size-selection policy.
- Home-screen label.
- Defect or exception options where applicable.

Example workflow families include:

- `package_workflow`
- `asset_workflow`
- `equipment_workflow`
- `inventory_workflow`

Example workflow actions include:

- `pickup`
- `stage`
- `checkout`
- `return`
- `exchange`
- `deposit`

## 5.3 Workflow Execution Principles

Workflow execution must be governed by platform services, not by ad hoc screen logic. The UI may display steps and collect input, but the runtime orchestration layer should decide what happens next.

Workflow configuration must be versioned, auditable, and testable. A deployment should be able to answer which workflow definition was active when a transaction occurred.

---

# Chapter 6 — Runtime Orchestration

## 6.1 Purpose

Runtime Orchestration coordinates the live execution of a workflow. It translates configuration and user input into a governed transaction.

## 6.2 Typical Runtime Sequence

A typical custody transaction includes:

1. Start transaction and assign correlation identifiers.
2. Capture credential or actor identity.
3. Capture reference input, asset tag, work order, package code, or device identifier.
4. Validate the reference against local and backend rules.
5. Request locker authorization if required.
6. Select or confirm a compartment.
7. Open the physical compartment.
8. Detect or confirm door action when hardware supports it.
9. Update local operational state.
10. Send acknowledgement to backend services.
11. Mark transaction complete or pending reconciliation.
12. Write audit and diagnostic records.

## 6.3 Runtime Rule

No physical action should occur without a transaction context. No transaction context should disappear without a terminal state or recovery path.

---

# Part II — Operational Trust and Custody

# Chapter 7 — Custody Governance

## 7.1 Purpose

Custody Governance defines how the platform treats assets, packages, devices, compartments, actors, and actions as governed custody objects.

## 7.2 Custody Concepts

Custody is not merely inventory. Custody means the platform can explain who had authority over an object, where it was physically placed, when it moved, and what evidence supports that record.

Custody state may include:

- Available.
- Reserved.
- Staged.
- Occupied.
- Checked out.
- Retrieved.
- Returned.
- Defective.
- Unknown.
- Needs reconciliation.

## 7.3 Compartment Custody

A locker compartment is an operational custody location. Its state must be governed independently of the backend asset record because the physical compartment can change state even when backend communication fails.

Compartment state should include:

- Enabled or disabled.
- Vacant, occupied, reserved, unavailable, or out of service.
- Current asset or package reference when applicable.
- Door state if available.
- Reservation expiration if applicable.
- Last transaction reference.

---

# Chapter 8 — Transaction Integrity

## 8.1 Purpose

Transaction Integrity protects the platform from losing the truth of what happened during physical operations.

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

## 8.4 Recovery Principle

Startup recovery must inspect incomplete transactions and move them toward a safe state. The platform should never rely on operator memory to reconstruct whether a door opened or an asset was staged.

---

# Chapter 9 — Hardware Abstraction

## 9.1 Purpose

Hardware Abstraction isolates platform logic from specific physical devices. The platform should not embed scanner, reader, relay, or controller details inside workflow logic.

## 9.2 Hardware Categories

The platform may interact with:

- Barcode scanners.
- RFID or credential readers.
- Locker relay controllers.
- Door sensors.
- Presence sensors.
- Touch displays.
- Cameras.
- Printers.
- Environmental sensors.
- Future compartment-control technologies.

## 9.3 Adapter Principle

Each hardware family should be represented through an adapter that exposes stable platform operations such as scan received, credential read, open compartment, read door state, test controller, or report health.

The adapter owns device-specific details. Platform services own operational meaning.

---

# Chapter 10 — Local Persistence

## 10.1 Purpose

Local Persistence provides the edge node with durable operational memory. This includes configuration, locker state, journal entries, audit events, hardware mappings, and diagnostic records.

## 10.2 Local Data Categories

The local persistence model should include:

- Kiosk and site configuration.
- Locker bank and compartment records.
- Locker status records.
- Workflow configuration cache.
- Transaction journal.
- Audit log index or references.
- Hardware configuration.
- Reconciliation queue.
- Administrative settings.

## 10.3 Persistence Principle

Local persistence should be treated as operational truth for physical edge events until reconciliation proves otherwise. Backend systems remain authoritative for enterprise business records, but the edge platform remains authoritative for what it physically executed.

---

# Chapter 11 — Backend Integration

## 11.1 Purpose

Backend Integration connects edge execution with enterprise authority. It validates credentials, assets, packages, work orders, permissions, reservations, acknowledgements, and reconciliation events.

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

Backend integration should be explicit and observable. Silent assumptions about identity, workflow, actor, or action type create fragile systems.

---

# Part III — Platform Operations

# Chapter 12 — Cross-Cutting Services

## 12.1 Purpose

Cross-Cutting Services support every Platform Technology. They provide the operational fabric needed for traceability, supportability, diagnostics, and reliability.

## 12.2 Core Services

Cross-cutting services include:

- Structured logging.
- File audit logging.
- Trace correlation.
- Error classification.
- Retry policy.
- Health checks.
- Configuration loading.
- Feature flags.
- Time services.
- Serialization and schema validation.
- Diagnostic export.

## 12.3 Correlation Principle

Every significant transaction should be traceable across UI activity, workflow execution, hardware command, local persistence, backend request, acknowledgement, and audit record.

---

# Chapter 13 — Security Architecture

## 13.1 Purpose

Security Architecture protects identities, permissions, credentials, operational authority, and system integrity.

## 13.2 Security Domains

Security must address:

- Actor authentication.
- Role and permission authorization.
- Kiosk identity.
- Backend service identity.
- Local administrative access.
- Credential-reader trust.
- API authentication.
- Audit integrity.
- Protection of sensitive local configuration.

## 13.3 Security Principle

Physical action must require explicit authority. The platform should not treat possession of a scanned value as sufficient proof of permission unless the configured workflow deliberately allows it.

---

# Chapter 14 — Administrative Services

## 14.1 Purpose

Administrative Services allow trusted personnel to configure, diagnose, recover, and support the platform without bypassing governance.

## 14.2 Administrative Capabilities

Administrative services may include:

- Locker status review.
- Manual compartment test.
- Controller connection test.
- Workflow configuration review.
- Transaction journal inspection.
- Incomplete transaction recovery.
- Reconciliation tools.
- Hardware diagnostics.
- Local log export.
- Commissioning review.
- Out-of-service and return-to-service actions.

## 14.3 Administrative Principle

Administrative actions are still platform actions. They must be logged, permissioned, and explainable.

---

# Chapter 15 — Deployment Architecture

## 15.1 Purpose

Deployment Architecture defines how the platform is packaged, installed, configured, upgraded, monitored, and supported.

## 15.2 Deployment Concerns

A deployment must account for:

- Operating system image.
- Runtime dependencies.
- Local database initialization.
- Hardware drivers and libraries.
- Controller addressing.
- Configuration files.
- Backend endpoint settings.
- Certificate and secret handling.
- Upgrade procedure.
- Rollback strategy.
- Offline support.
- Field diagnostics.

## 15.3 Deployment Principle

Deployment should be repeatable. A field installation should not depend on undocumented tribal knowledge.

---

# Chapter 16 — Commercial Architecture

## 16.1 Purpose

Commercial Architecture connects engineering structure to business value. EPAS is not only a technical document; it is a strategy for converting one-off engineering into reusable platform capability.

## 16.2 Commercial Value

The platform creates value by:

- Reducing custom-code cost per deployment.
- Shortening implementation cycles.
- Improving supportability.
- Allowing customer workflows to be configured.
- Creating defensible intellectual property.
- Supporting multiple product lines from a shared architecture.
- Making integrations more repeatable.
- Increasing confidence in field operations.

## 16.3 Commercial Principle

The platform should make the second deployment easier than the first and the tenth deployment dramatically easier than the second.

---

# Part IV — Strategic Direction

# Chapter 17 — Future Platform Evolution

## 17.1 Purpose

The Edge Platform should evolve without losing its architectural center. Future capability should extend the platform model rather than bypass it.

## 17.2 Candidate Evolution Areas

Future evolution may include:

- Multi-bank orchestration.
- Advanced reconciliation dashboards.
- Remote commissioning support.
- Mobile administrative tools.
- Camera-based evidence capture.
- Environmental monitoring.
- Predictive hardware maintenance.
- Offline-first workflow packages.
- Plugin hardware adapters.
- Expanded custody object types.
- Cloud-managed workflow versioning.
- AI-assisted diagnostics and support.

## 17.3 Evolution Principle

New capabilities should become Platform Technologies when they represent reusable architectural responsibility rather than one-customer customization.

---

# Chapter 18 — Intellectual Property Strategy

## 18.1 Purpose

EPAS documents the architecture, vocabulary, boundaries, and operating principles that make the Edge Platform distinct. This supports engineering clarity, onboarding, customer communication, and intellectual property development.

## 18.2 Protectable Concepts

Potentially protectable or commercially defensible concepts include:

- Governed physical-edge transaction orchestration.
- Configurable custody workflows.
- Local-first transaction journaling for physical action recovery.
- Separation of enterprise authority and edge execution.
- Hardware-abstracted compartment control.
- Reconciliation between local physical truth and enterprise records.
- Commissioning models for identity-bound edge nodes.
- Platform Technology responsibility taxonomy.

## 18.3 IP Principle

The platform should be described consistently. Consistent vocabulary supports patents, trade secrets, customer proposals, training materials, and engineering execution.

---

# Chapter 19 — Conclusions and Strategic Vision

The Edge Platform is a governed execution architecture for physical operations at the edge. It treats locker control, asset custody, package movement, credential validation, workflow execution, transaction journaling, and backend reconciliation as parts of one coherent system.

The strategic value of EPAS is that it turns a working product into a repeatable platform. It makes the architecture explainable to engineers, customers, partners, executives, and future investors. It also creates a foundation for product expansion beyond any single locker deployment.

The platform succeeds when field operations become boring in the best possible way: predictable, auditable, recoverable, supportable, and repeatable.

---

# Appendix A — Platform Technology Responsibility Matrix

| Platform Technology | Primary Responsibility | Must Not Own |
| --- | --- | --- |
| Commissioning Technology | Site, kiosk, bank, controller, and locker setup | Runtime custody decisions |
| Configurable Workflow Engine | Workflow definition and step progression | Hardware device implementation |
| Runtime Orchestration | Transaction execution coordination | Enterprise business record ownership |
| Custody Governance | Custody state rules and movement semantics | Relay-board protocols |
| Transaction Integrity | Journal, recovery, and transaction state | Customer-specific screen layout |
| Hardware Abstraction | Device-specific communication | Business authorization |
| Local Persistence | Local operational state | Cloud source-of-truth policy |
| Backend Integration | API contracts and enterprise communication | UI rendering |
| Cross-Cutting Services | Logging, tracing, diagnostics, health | Workflow-specific business meaning |
| Security Architecture | Identity, authority, permissions, protection | Locker assignment algorithms |
| Administrative Services | Support, diagnostics, controlled override | Unlogged operational bypass |
| Deployment Architecture | Install, upgrade, configuration packaging | Product strategy |
| Commercial Architecture | Platform reuse and business alignment | Low-level runtime implementation |

---

# Appendix B — Core Architectural Principles

1. Single Ownership.
2. Separation of Responsibilities.
3. Configuration Before Customization.
4. Deterministic Execution.
5. Operational Trust.
6. Platform Before Product.
7. No Physical Action Without Transaction Context.
8. Local Truth Must Be Durable.
9. Backend Authority Must Be Explicit.
10. Administrative Actions Must Be Governed.

---

# Appendix C — Glossary

**ACK** — Acknowledgement sent from the edge platform to backend services indicating the result of a governed transaction.

**Actor** — A person, service, or system identity performing an action.

**Commissioning** — The process of assigning identity, configuration, hardware mapping, and initial state to an edge node.

**Custody** — Governed responsibility for an asset, package, device, or compartment state.

**Edge Node** — A deployed kiosk, locker bank controller, or other field system executing physical operations.

**EPAS** — Edge Platform Architecture Specification.

**Hardware Abstraction** — Platform layer that isolates device-specific communication from workflow and business logic.

**Locker Bank** — A physical group of controlled compartments governed by the platform.

**Operational Trust** — The ability to explain and recover the truth of physical operations even when networks, devices, or workflows fail.

**Platform Technology** — A durable architectural responsibility within the Edge Platform.

**Reconciliation** — The process of resolving differences between local physical-edge records and backend enterprise records.

**SmartLocker** — A product expression of the Edge Platform.

**Transaction Journal** — Durable local record of transaction progress used for recovery, audit, and reconciliation.

**Workflow Action** — The operational intent of a workflow, such as pickup, stage, checkout, return, deposit, or exchange.

**Workflow Key** — A stable configured identifier for a workflow definition.
