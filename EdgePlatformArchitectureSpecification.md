# Edge Platform™ Architecture Specification (EPAS)

**Version 1.2 – Authoritative Working Draft**  
**Repository:** `Gablenook/EPAS`  
**Document:** `EdgePlatformArchitectureSpecification.md`  
**Status:** Master manuscript / active architecture specification  
**Revision Date:** 2026-07-03

> EPAS defines the Toren Edge Platform architecture: the durable engineering foundation for governed physical-edge systems such as asset custody kiosks, field-deployed device exchange systems, package exchange systems, controlled-access equipment systems, and other transaction-controlled edge operations.

---

## Document Control

This document is the authoritative master manuscript for the Edge Platform Architecture Specification. It should be updated directly as the platform architecture matures. Separate slide decks, executive briefs, legal summaries, patent working notes, implementation tickets, customer proposals, and training materials may derive from this manuscript, but they should not replace it.

### Revision History

| Version | Date | Description |
| --- | --- | --- |
| 1.0 | 2026-07-02 | Master manuscript established as the authoritative EPAS architecture specification. |
| 1.1 | 2026-07-03 | Began structured manuscript edit: strengthened document governance, platform thesis, standard chapter pattern, responsibility boundaries, and implementation-alignment language. |
| 1.2 | 2026-07-03 | Aligned manuscript naming around Toren ownership, EPAS as the platform reference architecture, and generic licensed product/deployment language. |

### Editing Rule

When architectural language, figures, vocabulary, or technology boundaries change, update this master manuscript first. Downstream documents should be regenerated, revised, or cross-checked against this file.

### Naming and Ownership Rule

Toren is the company, platform owner, and licensor. EPAS is the reference architecture for the Toren Edge Platform. Products, customer systems, licensee implementations, manufactured locker systems, and branded deployments may implement or express the platform, but they do not define the architecture. The master manuscript should therefore avoid tying EPAS to any single product name, customer name, manufacturer, or licensee unless that reference is deliberately required for implementation evidence or commercial context.

---

## Contents

- Executive Summary
- List of Figures
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
- Appendix D — Figure Production Notes
- Appendix E — Chapter Specification Pattern
- Appendix F — Implementation Evidence Register

---

## Executive Summary

The Toren Edge Platform is a software and systems architecture for controlling trusted physical transactions at the operational edge. It exists for environments where enterprise systems, local devices, human operators, physical compartments, credentials, scanners, relays, doors, sensors, and audit trails must work together as one governed system.

EPAS captures the architectural foundation that allows one platform to support package pickup, asset checkout, device staging, custody transfer, equipment exchange, inventory-controlled access, and future edge workflows without rewriting the core system for each customer. The first commercial deployments may include locker-based custody, package exchange, device checkout, equipment staging, and other controlled-access applications, but those deployments are licensed or configured expressions of the Toren Edge Platform rather than the architectural boundary of EPAS.

The platform is built around a simple but powerful division of responsibility:

- Enterprise systems define business authority.
- The edge platform executes physical operations.
- Local runtime services preserve continuity when connectivity is imperfect.
- Transaction journals protect operational truth.
- Configuration expresses deployment variation.
- Hardware adapters isolate device-specific behavior.
- Audit and reconciliation make every important action explainable.

The central claim of EPAS is that edge systems should not be treated as thin user interfaces attached to cloud software. Physical edge execution has its own responsibilities. Doors open locally. Credentials are scanned locally. Relays fire locally. Compartments become occupied or vacant locally. Operators need immediate feedback locally. When the network is slow, interrupted, or unavailable, the platform must still preserve an accurate account of what happened.

EPAS therefore describes a platform-first architecture rather than a single-purpose application. It establishes the rules, technologies, boundaries, and responsibilities needed to build repeatable edge products from a common foundation. The visual structure of this argument is introduced in **Figure 1** and expanded through the remaining figures.

### Executive Thesis

The Toren Edge Platform creates commercial and technical leverage by converting one-off physical-edge applications into governed, configurable, recoverable, hardware-adaptable platform deployments. Its value is not merely that it opens a locker or validates an asset. Its value is that it defines a repeatable pattern for connecting business authority to local physical execution while preserving operational truth.

This thesis has four consequences:

1. **The platform must own edge execution.** Backend systems may authorize and record business state, but the local platform must own the truth of physical events it performs.
2. **The platform must be configurable before it is customized.** Customer-specific workflows should be expressed through workflow definitions, validation profiles, and policy configuration whenever practical.
3. **The platform must remain recoverable.** Every critical physical transaction must have a durable journal, terminal state, or reconciliation path.
4. **The platform must become commercially reusable.** Each deployment should improve the common platform rather than create another isolated custom solution.

---

## List of Figures

| Figure | Title | Primary Location | Purpose |
| --- | --- | --- | --- |
| Figure 1 | Edge Platform Context Model | Executive Summary / Chapter 1 | Shows the relationship between enterprise authority, edge execution, operators, hardware, and audit evidence. |
| Figure 2 | Platform / Product / Deployment Hierarchy | Chapter 1 | Explains why EPAS governs the Toren Edge Platform while products and customer installations are licensed or configured expressions of the platform. |
| Figure 3 | Platform Technology Map | Chapter 3 | Organizes the major Platform Technologies and their boundaries. |
| Figure 4 | Commissioning Flow | Chapter 4 | Shows how a generic edge node becomes a site-specific operating system. |
| Figure 5 | Configurable Workflow Model | Chapter 5 | Shows how workflow configuration drives customer-specific behavior without code forks. |
| Figure 6 | Runtime Transaction Lifecycle | Chapter 6 | Shows a transaction from initiation through acknowledgement and reconciliation. |
| Figure 7 | Custody State Model | Chapter 7 | Shows movement among available, reserved, staged, occupied, checked out, returned, defective, and reconciliation states. |
| Figure 8 | Transaction Journal and Recovery Model | Chapter 8 | Shows how incomplete transactions are detected, recovered, acknowledged, or reconciled. |
| Figure 9 | Hardware Abstraction Layer | Chapter 9 | Shows platform logic separated from scanners, readers, relay controllers, sensors, and future hardware. |
| Figure 10 | Local Persistence Model | Chapter 10 | Shows configuration, locker status, journal, audit, diagnostics, and reconciliation queues. |
| Figure 11 | Edge-to-Backend Responsibility Split | Chapter 11 | Shows which responsibilities belong to the enterprise backend and which belong to edge execution. |
| Figure 12 | Cross-Cutting Services Fabric | Chapter 12 | Shows logging, tracing, health, diagnostics, retry policy, and correlation across the platform. |
| Figure 13 | Security Trust Boundary Model | Chapter 13 | Shows actor identity, kiosk identity, backend identity, administrative access, and protected local configuration. |
| Figure 14 | Administrative Operations Model | Chapter 14 | Shows governed support actions, diagnostics, recovery, and overrides. |
| Figure 15 | Deployment Package Model | Chapter 15 | Shows operating system, application runtime, hardware drivers, configuration, database, and support artifacts. |
| Figure 16 | Commercial Reuse Flywheel | Chapter 16 | Shows how platform-first engineering reduces deployment cost and compounds product value. |
| Figure 17 | Platform Evolution Roadmap | Chapter 17 | Shows future Platform Technologies and extension points. |
| Figure 18 | IP Strategy Map | Chapter 18 | Shows how vocabulary, architecture, implementation, and evidence support defensible intellectual property. |
| Figure 19 | EPAS Strategic Summary | Chapter 19 | Summarizes the full platform argument in one executive graphic. |

---

## Figure 1 — Edge Platform Context Model

> **Diagram Placeholder:** Create a context diagram with the Edge Platform at the center. Surrounding entities should include Enterprise Systems, Human Operators, Physical Compartments, Credential/Scan Devices, Hardware Controllers, Local Persistence, Audit Evidence, and Administrative Support. Use arrows to show enterprise authorization flowing toward the edge, physical execution occurring locally, and acknowledgement/reconciliation flowing back to enterprise systems.

**Caption:** Figure 1 — The Edge Platform coordinates enterprise authority, local physical execution, hardware control, operational state, and audit evidence.

---

# Part I — Platform Foundation

# Chapter 1 — Platform Vision

## 1.1 Purpose

The Toren Edge Platform exists to make physical operations trustworthy, repeatable, configurable, and commercially reusable. It is intended for systems where software is responsible for authorizing, controlling, recording, and reconciling physical actions. **Figure 1** shows the broad operating context in which EPAS applies.

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

## 1.2 Platform, Product, Licensee, and Deployment

EPAS distinguishes between four levels of design and commercialization:

- **Platform:** The durable Toren-owned architecture, runtime services, transaction model, workflow model, hardware abstraction, persistence model, security model, and integration patterns.
- **Product:** A packaged or branded expression of the platform.
- **Licensee:** A company or business entity authorized to implement, commercialize, manufacture, sell, operate, or distribute a product or deployment based on EPAS.
- **Deployment:** A configured instance of a product or licensed implementation for a customer, site, workflow, hardware set, and operating policy.

This distinction is fundamental. Product features should strengthen the platform whenever possible. Deployment-specific behavior should be expressed through configuration rather than source-code forks. Licensee or manufacturer-specific language should not be allowed to redefine the platform architecture. **Figure 2** should be used whenever EPAS is explained to a business, engineering, legal, investor, or partner audience because it prevents confusion between the platform, the product, the licensee, and any one customer installation.

## Figure 2 — Platform / Product / Deployment Hierarchy

> **Diagram Placeholder:** Create a hierarchy with Toren / EPAS / Edge Platform at the top. The middle tier should show product expressions such as asset custody kiosks, package exchange systems, device checkout systems, equipment staging systems, and future edge products. The commercial tier should show licensees, manufacturers, distributors, operators, or product companies that may commercialize platform-based products. The bottom tier should show customer deployments, sites, workflows, hardware configurations, and operating policies. Use downward arrows for architecture inheritance and upward arrows for deployment learning feeding the platform.

**Caption:** Figure 2 — EPAS governs the reusable Toren Edge Platform; products and licensees express the platform; deployments configure products for specific customers and sites.

## 1.3 Architectural Goal

The architectural goal is not merely to open lockers. The goal is to create a governed edge execution environment where physical action, business authorization, local state, backend state, and audit evidence remain aligned.

The platform must be:

- **Deterministic:** The same inputs should produce the same platform behavior.
- **Recoverable:** Interrupted transactions must be visible and reconcilable.
- **Configurable:** Different workflows must be supported without architectural rewrites.
- **Auditable:** Every important action must produce durable evidence.
- **Hardware-independent:** The platform must support different scanners, readers, controllers, and compartment technologies.
- **Commercially reusable:** Each customer deployment should improve the platform rather than create isolated custom code.

## 1.4 Product Naming and Brand Independence

EPAS intentionally separates platform language from product, customer, manufacturer, and licensee names. Toren is the platform owner and licensor. EPAS is the platform reference architecture. Products, licensees, manufacturers, customer-specific kiosks, and future branded systems may all express the platform, but they should not define the architecture.

A product name may carry market identity, but the platform vocabulary carries engineering, commercial, licensing, and intellectual-property continuity.

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

Business intent, runtime execution, custody, transaction integrity, hardware control, persistence, enterprise integration, and administration are intentionally separated into independent Platform Technologies. The separated technology boundaries are summarized visually in **Figure 3**.

This separation prevents the kiosk user interface from becoming the owner of business rules, hardware details, backend contracts, and transaction recovery. The UI presents and collects information. Platform services govern execution.

## 2.4 Principle 3 — Configuration Before Customization

Deployments should differ through configuration before source-code customization. Customer-specific behavior should be expressed through workflow definitions, validation profiles, hardware mappings, site settings, and policy configuration whenever practical. **Figure 5** illustrates this principle by separating workflow definition from runtime execution.

This principle makes the platform commercially scalable. It allows one product family to support Ryder-style asset workflows, Shaw-style equipment pickup, package workflows, staging workflows, and future custody use cases without fragmenting the codebase.

## 2.5 Principle 4 — Deterministic Execution

Identical operational inputs should produce identical architectural behavior. Deterministic execution simplifies diagnostics, testing, certification, recovery, support, and long-term maintenance.

Where external conditions vary, such as backend availability or hardware response timing, the platform must preserve deterministic local decisions and durable journal records. **Figure 8** shows how transaction journaling protects deterministic recovery.

## 2.6 Principle 5 — Operational Trust

The Edge Platform maintains trustworthy operational state even when enterprise connectivity is temporarily unavailable. Enterprise systems coordinate business operations; edge systems execute physical operations. The edge/backend responsibility split is shown in **Figure 11**.

A physical door opening is not theoretical. Once it occurs, the edge system must record it, even if the backend cannot be reached at that moment.

## 2.7 Principle 6 — Platform Before Product

Specific products, licensee systems, customer deployments, and manufactured implementations may express the Toren Edge Platform, but EPAS remains independent of any single product name, manufacturer, customer, or licensee. Engineering investment should strengthen the common platform before adding product-specific capability. This relationship is established in **Figure 2** and extended commercially in **Figure 16**.

Product-specific names, screens, labels, and workflows may vary. The platform responsibilities should remain stable.

## 2.8 Principle 7 — No Physical Action Without Transaction Context

Every governed physical action must be connected to an explicit transaction context before the action occurs. The platform should know the actor, workflow, requested action, target compartment, correlation identifiers, and expected acknowledgement path before a relay is commanded or a compartment is opened.

## 2.9 Principle 8 — Local Truth Must Be Durable

The edge node must preserve a durable account of physical actions because it is the system closest to the physical event. Backend records may later become authoritative for enterprise reporting, but they cannot replace the local record of what physically occurred.

## 2.10 Principle 9 — Backend Authority Must Be Explicit

Backend calls must carry explicit identity and context. Silent assumptions about kiosk identity, locker bank identity, workflow key, workflow action, actor identity, or request correlation create fragile systems.

## 2.11 Principle 10 — Administrative Actions Must Be Governed

Administrative actions are not exceptions to governance. Manual tests, overrides, recoveries, and out-of-service changes must be permissioned, logged, and explainable.

---

# Chapter 3 — Platform Technology Architecture

## 3.1 Overview

The platform is organized into Platform Technologies. A Platform Technology is a durable architectural responsibility with a clear owner, stable interfaces, and reusable value across deployments.

## Figure 3 — Platform Technology Map

> **Diagram Placeholder:** Create a layered architecture map. Suggested center layer: Runtime Orchestration. Surround it with Configurable Workflow Engine, Custody Governance, Transaction Integrity, Hardware Abstraction, Local Persistence, Backend Integration, Security Architecture, Administrative Services, Cross-Cutting Services, Commissioning Technology, Deployment Architecture, and Commercial Architecture. Use boundary boxes to make responsibility separation obvious.

**Caption:** Figure 3 — The Edge Platform is composed of reusable Platform Technologies with explicit ownership and boundaries.

## 3.2 Core Platform Technologies

The first-generation Edge Platform includes the following technologies:

1. **Commissioning Technology** — Initializes site, kiosk, controller, locker bank, hardware, and local database identity. See **Figure 4**.
2. **Configurable Workflow Engine** — Defines and executes customer workflows through configuration. See **Figure 5**.
3. **Runtime Orchestration** — Coordinates credential scan, reference scan, validation, authorization, compartment assignment, hardware action, state update, ACK, and recovery. See **Figure 6**.
4. **Custody Governance** — Governs asset, package, device, and compartment custody rules. See **Figure 7**.
5. **Transaction Integrity** — Journals every critical step and supports recovery after interruption. See **Figure 8**.
6. **Hardware Abstraction** — Isolates device-specific behavior behind stable platform interfaces. See **Figure 9**.
7. **Local Persistence** — Maintains local operational state, configuration, transaction records, and diagnostics. See **Figure 10**.
8. **Backend Integration** — Communicates with enterprise APIs for validation, authorization, acknowledgement, and reconciliation. See **Figure 11**.
9. **Cross-Cutting Services** — Provides logging, tracing, correlation IDs, error handling, telemetry, diagnostics, and service health. See **Figure 12**.
10. **Security Architecture** — Protects credentials, identities, device permissions, and operational boundaries. See **Figure 13**.
11. **Administrative Services** — Enables local support, diagnostics, override workflows, commissioning review, and reconciliation. See **Figure 14**.
12. **Deployment Architecture** — Defines how platform software is packaged, configured, installed, upgraded, and supported. See **Figure 15**.
13. **Commercial Architecture** — Converts engineering structure into repeatable deployment value, defensible platform language, and product-family leverage. See **Figure 16**.

## 3.3 Technology Boundaries

Each Platform Technology should expose interfaces that are stable enough for other services to depend on, but narrow enough to prevent responsibility leakage. For example, the workflow engine should not directly manipulate relay boards. The hardware layer should not decide whether an asset may be checked out. Backend integration should not own local door-state truth.

## 3.4 Standard Platform Technology Specification Pattern

Each Platform Technology chapter should eventually be expanded using the same specification pattern:

- Purpose.
- Problem addressed.
- Primary responsibilities.
- Boundaries and non-responsibilities.
- Interfaces and collaborators.
- Data ownership.
- Operational model.
- Failure modes.
- Configuration model.
- Security and audit considerations.
- Commercial significance.
- IP significance.
- Related implementation evidence.
- Related figures.

This pattern is also captured in **Appendix E** so the manuscript can be expanded consistently without becoming a loose collection of technical notes.

---

# Chapter 4 — Commissioning Technology

## 4.1 Purpose

Commissioning Technology converts generic platform software into a site-specific edge node. It establishes identity, hardware mapping, locker topology, controller ports, local database records, and initial operational state.

## Figure 4 — Commissioning Flow

> **Diagram Placeholder:** Create a left-to-right process flow: network readiness → customer/site selection → kiosk identity → locker bank identity → controller branch mapping → locker inventory generation → hardware validation → backend registration → initial status creation → commissioning audit record. Include a side lane for administrative review and correction.

**Caption:** Figure 4 — Commissioning binds a generic platform installation to a specific site, kiosk, locker bank, controller configuration, and operational state.

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

Commissioning is not a one-time setup screen. It is a platform capability that directly affects operational trust. The commissioning sequence in **Figure 4** should therefore be treated as a governed platform workflow rather than informal setup labor.

## 4.4 Boundary Rule

Commissioning owns identity binding and initial configuration. It does not own live custody decisions, transaction recovery, or workflow authorization. Once a deployment is commissioned, runtime services use the commissioned configuration but remain responsible for live transaction behavior.

---

# Chapter 5 — Configurable Workflow Engine

## 5.1 Purpose

The workflow engine allows customer-specific operational behavior to be expressed as configuration. It defines the screens, steps, references, validations, authorizations, and action semantics used by a deployment.

## Figure 5 — Configurable Workflow Model

> **Diagram Placeholder:** Create a configuration-to-runtime diagram. Left side: workflow definition, validation profile, reference labels, action type, size policy, defect options, home button label. Center: workflow engine. Right side: runtime screens, validation calls, authorization request, locker assignment, physical action, and acknowledgement. Show that configuration changes behavior without source-code forks.

**Caption:** Figure 5 — Workflow configuration defines customer-specific behavior while runtime services preserve common platform execution rules.

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

Workflow execution must be governed by platform services, not by ad hoc screen logic. The UI may display steps and collect input, but the runtime orchestration layer should decide what happens next. **Figure 5** shows how the configured workflow remains separate from the common runtime engine.

Workflow configuration must be versioned, auditable, and testable. A deployment should be able to answer which workflow definition was active when a transaction occurred.

## 5.4 Boundary Rule

The workflow engine owns configured intent and step progression. It does not own hardware implementation, backend business authority, or custody-state truth. Those responsibilities belong to Hardware Abstraction, Backend Integration, and Custody Governance respectively.

---

# Chapter 6 — Runtime Orchestration

## 6.1 Purpose

Runtime Orchestration coordinates the live execution of a workflow. It translates configuration and user input into a governed transaction.

## Figure 6 — Runtime Transaction Lifecycle

> **Diagram Placeholder:** Create a numbered lifecycle diagram: start transaction → assign correlation IDs → capture actor/credential → capture reference/asset → validate → authorize → select compartment → command hardware → confirm physical action → update local state → send ACK → complete or reconcile. Include exception branches for validation failure, hardware failure, ACK failure, and recovery.

**Caption:** Figure 6 — Runtime Orchestration turns configured workflow intent into a governed physical transaction.

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

This sequence is represented in **Figure 6**. Its journaled counterpart is shown later in **Figure 8**.

## 6.3 Runtime Rule

No physical action should occur without a transaction context. No transaction context should disappear without a terminal state or recovery path.

## 6.4 Boundary Rule

Runtime Orchestration coordinates execution but should not absorb every implementation detail. It should call workflow, custody, hardware, persistence, backend, and audit services through explicit service boundaries. This protects the platform from becoming a single monolithic kiosk procedure.

---

# Part II — Operational Trust and Custody

# Chapter 7 — Custody Governance

## 7.1 Purpose

Custody Governance defines how the platform treats assets, packages, devices, compartments, actors, and actions as governed custody objects.

## Figure 7 — Custody State Model

> **Diagram Placeholder:** Create a state model with states including Available, Reserved, Staged, Occupied, Checked Out, Retrieved, Returned, Defective, Unknown, and Needs Reconciliation. Show valid transitions for staging, pickup, checkout, return, defect marking, timeout, and reconciliation. Highlight that compartment custody and asset custody may temporarily diverge until reconciled.

**Caption:** Figure 7 — Custody Governance defines valid custody states and transitions for assets, packages, devices, and compartments.

## 7.2 Custody Concepts

Custody is not merely inventory. Custody means the platform can explain who had authority over an object, where it was physically placed, when it moved, and what evidence supports that record. **Figure 7** gives this concept a reusable state vocabulary.

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

## 7.4 Boundary Rule

Custody Governance owns valid custody semantics and transition rules. It does not own relay commands, scanner input, UI rendering, or external API transport. It collaborates with those technologies to keep physical state, business authorization, and audit evidence aligned.

---

# Chapter 8 — Transaction Integrity

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

---

# Chapter 9 — Hardware Abstraction

## 9.1 Purpose

Hardware Abstraction isolates platform logic from specific physical devices. The platform should not embed scanner, reader, relay, or controller details inside workflow logic.

## Figure 9 — Hardware Abstraction Layer

> **Diagram Placeholder:** Create a layered diagram. Top: workflow and runtime services. Middle: hardware abstraction interfaces such as scanner adapter, credential reader adapter, locker controller adapter, door sensor adapter, camera adapter, printer adapter. Bottom: concrete devices and protocols. Show that platform services call stable interfaces while adapters own device-specific behavior.

**Caption:** Figure 9 — Hardware Abstraction allows the platform to support multiple physical devices without embedding device details in workflow logic.

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

The adapter owns device-specific details. Platform services own operational meaning. **Figure 9** should be used in engineering reviews to prevent hardware-specific code from leaking into workflow, custody, or backend-integration services.

## 9.4 Boundary Rule

Hardware Abstraction owns device communication and device health semantics. It does not decide whether a workflow is valid, whether an actor is authorized, or whether a custody transition is allowed.

---

# Chapter 10 — Local Persistence

## 10.1 Purpose

Local Persistence provides the edge node with durable operational memory. This includes configuration, locker state, journal entries, audit events, hardware mappings, and diagnostic records.

## Figure 10 — Local Persistence Model

> **Diagram Placeholder:** Create a data model diagram showing local stores for kiosk configuration, site identity, locker bank records, locker status, workflow cache, hardware mapping, transaction journal, audit references, diagnostic logs, administrative settings, and reconciliation queue. Show links from runtime services, commissioning, administration, and backend integration.

**Caption:** Figure 10 — Local Persistence gives the edge node durable operational memory for configuration, physical state, transaction recovery, audit, and reconciliation.

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

Local persistence should be treated as operational truth for physical edge events until reconciliation proves otherwise. Backend systems remain authoritative for enterprise business records, but the edge platform remains authoritative for what it physically executed. **Figure 10** and **Figure 11** should be interpreted together.

## 10.4 Boundary Rule

Local Persistence owns durable storage of local platform state. It does not own the meaning of every stored state. Meaning is supplied by the Platform Technology that creates and consumes the record.

---

# Chapter 11 — Backend Integration

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

---

# Part III — Platform Operations

# Chapter 12 — Cross-Cutting Services

## 12.1 Purpose

Cross-Cutting Services support every Platform Technology. They provide the operational fabric needed for traceability, supportability, diagnostics, and reliability.

## Figure 12 — Cross-Cutting Services Fabric

> **Diagram Placeholder:** Create a horizontal fabric diagram beneath all Platform Technologies. Include structured logging, audit logging, correlation IDs, diagnostics, health checks, error classification, retry policy, configuration loading, serialization, telemetry, and support export. Show the fabric touching runtime orchestration, backend integration, local persistence, administration, and hardware abstraction.

**Caption:** Figure 12 — Cross-Cutting Services create the observability and reliability fabric that supports the full platform.

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

Every significant transaction should be traceable across UI activity, workflow execution, hardware command, local persistence, backend request, acknowledgement, and audit record. **Figure 12** should be used as the checklist for traceability coverage.

---

# Chapter 13 — Security Architecture

## 13.1 Purpose

Security Architecture protects identities, permissions, credentials, operational authority, and system integrity.

## Figure 13 — Security Trust Boundary Model

> **Diagram Placeholder:** Create a trust-boundary diagram. Include actor identity, credential readers, kiosk identity, local administrator, backend API, local database/configuration, hardware control, and audit records. Show trust boundaries around local device, backend services, administrative access, and physical hardware.

**Caption:** Figure 13 — Security Architecture protects the authority to perform physical actions and the evidence proving those actions occurred.

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

Physical action must require explicit authority. The platform should not treat possession of a scanned value as sufficient proof of permission unless the configured workflow deliberately allows it. The trust boundaries in **Figure 13** should be reviewed whenever a workflow shortcut is proposed.

---

# Chapter 14 — Administrative Services

## 14.1 Purpose

Administrative Services allow trusted personnel to configure, diagnose, recover, and support the platform without bypassing governance.

## Figure 14 — Administrative Operations Model

> **Diagram Placeholder:** Create an administrative operations diagram with roles such as site administrator, support technician, field installer, and platform support. Show governed actions: locker status review, manual compartment test, controller test, workflow review, transaction journal inspection, recovery action, reconciliation action, log export, commissioning review, and out-of-service control. Show all actions flowing into audit logging.

**Caption:** Figure 14 — Administrative Services provide controlled support and recovery actions without bypassing platform governance.

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

Administrative actions are still platform actions. They must be logged, permissioned, and explainable. **Figure 14** should explicitly show administrative actions flowing into audit evidence.

---

# Chapter 15 — Deployment Architecture

## 15.1 Purpose

Deployment Architecture defines how the platform is packaged, installed, configured, upgraded, monitored, and supported.

## Figure 15 — Deployment Package Model

> **Diagram Placeholder:** Create a package/deployment diagram. Include operating system image, application runtime, local database, hardware drivers/libraries, configuration files, certificates/secrets, workflow package, commissioning data, support tools, logging location, upgrade package, rollback package, and field diagnostic export.

**Caption:** Figure 15 — Deployment Architecture packages the platform into repeatable field installations with supportable upgrade and rollback paths.

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

Deployment should be repeatable. A field installation should not depend on undocumented tribal knowledge. The deployment package in **Figure 15** should become the baseline for installation checklists and support documentation.

---

# Chapter 16 — Commercial Architecture

## 16.1 Purpose

Commercial Architecture connects engineering structure to business value. EPAS is not only a technical document; it is a strategy for converting one-off engineering into reusable platform capability.

## Figure 16 — Commercial Reuse Flywheel

> **Diagram Placeholder:** Create a flywheel diagram: platform architecture → product capability → customer deployment → field learning → reusable platform improvement → faster future deployment → stronger commercial position. Include cost reduction, supportability, IP defensibility, and integration repeatability as side benefits.

**Caption:** Figure 16 — Platform-first engineering compounds commercial value by turning deployment learning into reusable capability.

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

The platform should make the second deployment easier than the first and the tenth deployment dramatically easier than the second. **Figure 16** is the visual expression of this principle.

---

# Part IV — Strategic Direction

# Chapter 17 — Future Platform Evolution

## 17.1 Purpose

The Edge Platform should evolve without losing its architectural center. Future capability should extend the platform model rather than bypass it.

## Figure 17 — Platform Evolution Roadmap

> **Diagram Placeholder:** Create a roadmap graphic with near-term, mid-term, and long-term evolution lanes. Include multi-bank orchestration, advanced reconciliation, remote commissioning, mobile administration, camera evidence, environmental monitoring, predictive maintenance, offline-first workflow packages, plugin adapters, expanded custody objects, cloud-managed workflow versioning, and AI-assisted diagnostics.

**Caption:** Figure 17 — Future evolution should extend the platform through reusable Platform Technologies and governed extension points.

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

New capabilities should become Platform Technologies when they represent reusable architectural responsibility rather than one-customer customization. Candidate Platform Technologies should be evaluated against the roadmap in **Figure 17**.

---

# Chapter 18 — Intellectual Property Strategy

## 18.1 Purpose

EPAS documents the architecture, vocabulary, boundaries, and operating principles that make the Edge Platform distinct. This supports engineering clarity, onboarding, customer communication, and intellectual property development.

## Figure 18 — IP Strategy Map

> **Diagram Placeholder:** Create a map connecting architectural vocabulary, Platform Technologies, implementation evidence, customer workflows, transaction records, diagrams, and commercial packaging. Show potential IP categories: patents, trade secrets, copyrighted documentation, design language, customer-specific configurations, and implementation know-how.

**Caption:** Figure 18 — EPAS supports intellectual property strategy by connecting architecture, vocabulary, implementation, evidence, and commercial expression.

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

The platform should be described consistently. Consistent vocabulary supports patents, trade secrets, customer proposals, training materials, and engineering execution. **Figure 18** should be used when converting EPAS into legal, commercial, or investor-facing materials.

---

# Chapter 19 — Conclusions and Strategic Vision

The Edge Platform is a governed execution architecture for physical operations at the edge. It treats locker control, asset custody, package movement, credential validation, workflow execution, transaction journaling, and backend reconciliation as parts of one coherent system.

## Figure 19 — EPAS Strategic Summary

> **Diagram Placeholder:** Create a one-page executive summary graphic. Center message: governed physical-edge execution. Surround it with platform-first architecture, configurable workflows, operational trust, transaction integrity, hardware abstraction, local persistence, backend integration, commercial reuse, and IP strategy. This should be suitable as the final slide of an executive deck.

**Caption:** Figure 19 — EPAS defines a reusable architecture for governed physical-edge execution, commercial platform reuse, and defensible technology development.

The strategic value of EPAS is that it turns a working implementation into a repeatable platform. It makes the architecture explainable to engineers, customers, partners, executives, and future investors. It also creates a foundation for product expansion beyond any single locker deployment.

The platform succeeds when field operations become boring in the best possible way: predictable, auditable, recoverable, supportable, and repeatable. This final strategic claim is summarized visually in **Figure 19**.

---

# Appendix A — Platform Technology Responsibility Matrix

| Platform Technology | Primary Responsibility | Must Not Own | Primary Figure |
| --- | --- | --- | --- |
| Commissioning Technology | Site, kiosk, bank, controller, and locker setup | Runtime custody decisions | Figure 4 |
| Configurable Workflow Engine | Workflow definition and step progression | Hardware device implementation | Figure 5 |
| Runtime Orchestration | Transaction execution coordination | Enterprise business record ownership | Figure 6 |
| Custody Governance | Custody state rules and movement semantics | Relay-board protocols | Figure 7 |
| Transaction Integrity | Journal, recovery, and transaction state | Customer-specific screen layout | Figure 8 |
| Hardware Abstraction | Device-specific communication | Business authorization | Figure 9 |
| Local Persistence | Local operational state | Cloud source-of-truth policy | Figure 10 |
| Backend Integration | API contracts and enterprise communication | UI rendering | Figure 11 |
| Cross-Cutting Services | Logging, tracing, diagnostics, health | Workflow-specific business meaning | Figure 12 |
| Security Architecture | Identity, authority, permissions, protection | Locker assignment algorithms | Figure 13 |
| Administrative Services | Support, diagnostics, controlled override | Unlogged operational bypass | Figure 14 |
| Deployment Architecture | Install, upgrade, configuration packaging | Product strategy | Figure 15 |
| Commercial Architecture | Platform reuse and business alignment | Low-level runtime implementation | Figure 16 |

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

**Deployment** — A configured instance of a product or licensed implementation for a customer, site, workflow, hardware set, and operating policy.

**Diagram Placeholder** — A manuscript note defining the intent, content, and caption for a future professional figure.

**Edge Node** — A deployed kiosk, locker bank controller, or other field system executing physical operations.

**EPAS** — Edge Platform Architecture Specification; the reference architecture for the Toren Edge Platform.

**Figure Register** — The numbered list of figures used to coordinate manuscript text, diagram production, Canva design work, and final publication layout.

**Hardware Abstraction** — Platform layer that isolates device-specific communication from workflow and business logic.

**Licensee** — A company or business entity authorized to implement, commercialize, manufacture, sell, operate, or distribute a product or deployment based on EPAS.

**Locker Bank** — A physical group of controlled compartments governed by the platform.

**Operational Trust** — The ability to explain and recover the truth of physical operations even when networks, devices, or workflows fail.

**Platform Technology** — A durable architectural responsibility within the Edge Platform.

**Product** — A packaged or branded expression of the Toren Edge Platform.

**Reconciliation** — The process of resolving differences between local physical-edge records and backend enterprise records.

**Toren** — The company, platform owner, and licensor associated with the Toren Edge Platform.

**Toren Edge Platform** — The platform governed by EPAS for configurable, recoverable, auditable, hardware-adaptable physical-edge transaction execution.

**Transaction Journal** — Durable local record of transaction progress used for recovery, audit, and reconciliation.

**Workflow Action** — The operational intent of a workflow, such as pickup, stage, checkout, return, deposit, or exchange.

**Workflow Key** — A stable configured identifier for a workflow definition.

---

# Appendix D — Figure Production Notes

The figures in this manuscript are intentionally defined as numbered placeholders before final artwork is produced. This allows the architecture, captions, cross-references, and publication structure to stabilize before time is spent on finished graphics.

## D.1 Figure Development Sequence

Recommended figure production order:

1. **Figure 1 — Edge Platform Context Model** because it frames the entire EPAS argument.
2. **Figure 3 — Platform Technology Map** because it becomes the core architecture overview.
3. **Figure 6 — Runtime Transaction Lifecycle** because it explains how the platform operates.
4. **Figure 8 — Transaction Journal and Recovery Model** because it defends operational trust.
5. **Figure 11 — Edge-to-Backend Responsibility Split** because it clarifies authority and execution.
6. **Figure 16 — Commercial Reuse Flywheel** because it turns architecture into business value.
7. **Figure 19 — EPAS Strategic Summary** because it becomes the executive closing graphic.

## D.2 Canva Deck Alignment

The first Canva executive deck should reuse a smaller subset of the figure register:

- Figure 1 as the opening context slide.
- Figure 2 as the platform/product/deployment explanation.
- Figure 3 as the architecture overview.
- Figure 6 as the runtime explanation.
- Figure 8 as the operational-trust proof point.
- Figure 11 as the backend/edge split.
- Figure 16 as the commercial argument.
- Figure 19 as the closing summary.

## D.3 Publication Rule

Each finished figure should keep the figure number and caption from this manuscript unless the manuscript is deliberately renumbered. Canva graphics, Word/PDF editions, executive briefs, and presentation decks should use the same figure numbers wherever practical to preserve traceability.

---

# Appendix E — Chapter Specification Pattern

Use this pattern when expanding any Platform Technology chapter:

1. **Purpose** — Why the technology exists.
2. **Problem Addressed** — What operational or commercial problem the technology solves.
3. **Primary Responsibilities** — What the technology owns.
4. **Boundaries and Non-Responsibilities** — What the technology must not own.
5. **Interfaces and Collaborators** — Which other technologies it depends on or serves.
6. **Data Ownership** — Which records, identifiers, states, or schemas it creates or governs.
7. **Operational Model** — How it behaves during normal execution.
8. **Failure Modes** — How it behaves when validation, hardware, storage, network, or operator behavior fails.
9. **Configuration Model** — Which behavior should be configurable.
10. **Security and Audit Considerations** — What must be protected, logged, or permissioned.
11. **Commercial Significance** — How it improves reuse, supportability, deployment speed, or customer value.
12. **IP Significance** — How it contributes to protectable vocabulary, architecture, method, or implementation evidence.
13. **Related Implementation Evidence** — Code, DTOs, logs, database tables, services, or workflows that prove the concept exists.
14. **Related Figures** — Figures that explain or summarize the technology.

---

# Appendix F — Implementation Evidence Register

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
