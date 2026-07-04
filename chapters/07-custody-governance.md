# Chapter 7 — Custody Governance

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Expanded chapter draft  
**Primary Figure:** Figure 7 — Custody State Model

---

## 7.1 Purpose

Custody Governance defines how the Toren Edge Platform treats assets, packages, devices, compartments, actors, and actions as governed custody objects. It establishes the state vocabulary, transition rules, compartment semantics, exception handling, and reconciliation expectations needed to explain who had authority over an object, where that object was physically located, and what evidence supports the custody record.

Custody Governance is the Platform Technology that prevents physical-edge execution from becoming a loose collection of scans, door opens, and database updates. It gives those events operational meaning.

## 7.2 Problem Addressed

Physical-edge systems often confuse inventory, compartment state, and custody. Inventory may say an object exists. A compartment record may say a door or bin is occupied. A backend asset record may say an item is available, assigned, or checked out. None of those facts alone proves custody.

Custody requires a governed explanation of authority, location, action, timing, and evidence. Without Custody Governance, the platform can open a compartment and update a database but still fail to answer whether an object was staged, retrieved, returned, defective, reserved, abandoned, or in need of reconciliation.

Custody Governance addresses this by defining valid states and transitions across assets, packages, devices, compartments, actors, and workflow actions. It ensures that physical state and business state may diverge temporarily during real-world failure, but that the divergence is visible, journaled, and reconcilable.

## Figure 7 — Custody State Model

> **Diagram Placeholder:** Create a state model with states including Available, Reserved, Staged, Occupied, Checked Out, Retrieved, Returned, Defective, Unknown, and Needs Reconciliation. Show valid transitions for staging, pickup, checkout, return, defect marking, timeout, abandonment, administrative correction, and reconciliation. Include separate but linked lanes for custody object state and compartment state. Highlight that compartment custody and asset/package/device custody may temporarily diverge until reconciled.

**Caption:** Figure 7 — Custody Governance defines valid custody states and transitions for assets, packages, devices, compartments, actors, and physical-edge actions.

## 7.3 Primary Responsibilities

Custody Governance owns:

- Custody-state vocabulary.
- Valid custody transitions.
- Relationship between workflow actions and custody outcomes.
- Relationship between custody objects and physical compartments.
- Compartment occupancy semantics.
- Reservation semantics and expiration behavior.
- Defect, exception, and condition semantics.
- Rules for staging, pickup, checkout, return, retrieval, deposit, exchange, release, and reconciliation.
- Rules for when local physical state may differ from backend business state.
- Requirements for evidence needed to support a custody transition.
- Conditions that require administrative review or reconciliation.

Custody Governance must make custody meaning explicit enough that Runtime Orchestration, Transaction Integrity, Local Persistence, Backend Integration, and Administrative Services can preserve and explain the state of a physical-edge transaction.

## 7.4 Custody Concepts

Custody is not merely inventory. Custody means the platform can explain:

- which object was involved,
- who or what had authority over it,
- where it was physically located,
- what workflow action changed its state,
- when the action occurred,
- what evidence supports the transition,
- and what system or administrator must resolve any ambiguity.

Custody objects may include:

- Serialized assets.
- Packages.
- Devices.
- Equipment.
- Inventory items.
- Work-order controlled objects.
- Returned or defective objects.
- Future controlled physical objects governed by the platform.

Custody locations may include lockers, compartments, cabinets, controlled bins, device bays, storage locations, or other locally controlled physical endpoints.

## 7.5 Custody State Vocabulary

Representative custody states include:

- **Available** — The object is available for assignment, staging, checkout, pickup, or release.
- **Reserved** — The object or compartment has been allocated for a pending transaction but the physical action has not fully completed.
- **Staged** — The object has been placed into a controlled location for later retrieval, pickup, checkout, or processing.
- **Occupied** — A compartment or controlled location is known or believed to contain an object.
- **Checked Out** — The object has been released to an actor, user, service, or downstream process.
- **Retrieved** — The object has been removed from a controlled location as part of an authorized retrieval or pickup action.
- **Returned** — The object has been placed back into platform custody after use or release.
- **Defective** — The object has been marked with a condition or disposition requiring special handling.
- **Unavailable** — The object or compartment is not eligible for normal workflow use.
- **Out of Service** — The compartment, device, or location has been administratively removed from service.
- **Unknown** — The platform cannot confidently determine the current physical or custody state.
- **Needs Reconciliation** — Local and backend state, physical evidence, or transaction records require review and resolution.

The exact vocabulary may be extended by product or deployment, but the platform should preserve stable canonical meanings for governed custody transitions.

## 7.6 Compartment Custody

A compartment is an operational custody location. Its state must be governed independently of the backend object record because physical compartments can change state even when backend communication fails.

Compartment state should include:

- Enabled or disabled.
- Vacant, occupied, reserved, unavailable, unknown, or out of service.
- Current asset, package, device, or reference value where applicable.
- Door state where hardware supports detection.
- Presence state where hardware supports detection.
- Reservation expiration where applicable.
- Last transaction reference.
- Last known actor or workflow context where appropriate.
- Reconciliation status where physical and system state may differ.

A compartment state change should be tied to transaction context whenever it results from a governed runtime action.

## 7.7 Relationship to Workflow Actions

Workflow actions give custody transitions their intent. The same physical action may have different custody meaning depending on the workflow.

Examples:

- `stage` may move an object from available or expected state into staged/occupied platform custody.
- `pickup` may move an object from staged or occupied state to retrieved or checked-out state.
- `checkout` may move a device from available or staged state to checked-out state.
- `return` may move an object from checked-out state to returned, staged, or occupied state.
- `exchange` may combine retrieval of one object with return or staging of another.
- `deposit` may place an object into platform custody without implying immediate availability.
- `defect` or a defect option may change object condition without completing normal custody release.

Custody Governance should define which transitions are valid for each workflow action and which transitions require backend authority, local evidence, administrative review, or reconciliation.

## 7.8 Interfaces and Collaborators

Custody Governance collaborates with:

- **Configurable Workflow Engine** to interpret workflow action and configured intent.
- **Runtime Orchestration** to evaluate whether a custody transition may occur during live execution.
- **Transaction Integrity** to preserve custody-related transaction progress and recovery states.
- **Local Persistence** to store local compartment and custody state.
- **Backend Integration** to exchange validation, authorization, ACK, and reconciliation context.
- **Hardware Abstraction** to receive door, presence, or compartment evidence where available.
- **Administrative Services** to review, correct, reconcile, or mark custody exceptions.
- **Security Architecture** to ensure custody-changing actions require proper authority.
- **Cross-Cutting Services** to log, trace, and classify custody-related events.

Custody Governance should not be buried in UI code, backend DTO assumptions, or locker table values alone.

## 7.9 Data Ownership

Custody Governance governs the meaning of custody-related data, including:

- Custody object identifiers.
- Custody object type.
- Current custody state.
- Current condition or disposition.
- Current compartment or controlled-location reference.
- Actor, workflow, and action associated with the last transition.
- Reservation ownership and expiration.
- Defect or exception status.
- Reconciliation status.
- Last transaction reference.
- Evidence required to support a transition.

Local Persistence may store the data, and Backend Integration may transmit related records, but Custody Governance owns the meaning of custody states and transitions.

## 7.10 Operational Model

A typical custody-governed transaction includes:

1. Receive workflow action and transaction context from Runtime Orchestration.
2. Identify the custody object and current known state.
3. Identify the compartment or physical custody location where applicable.
4. Evaluate whether the requested transition is allowed.
5. Confirm required backend authority if the transition requires enterprise approval.
6. Reserve, stage, occupy, release, return, mark defective, or reconcile according to state rules.
7. Record local custody and compartment state.
8. Preserve transition evidence in the transaction journal and audit trail.
9. Send custody outcome through ACK or reconciliation path.
10. Mark exceptions as failed, unknown, or needs-reconciliation rather than hiding ambiguity.

Custody transitions should be deterministic for the same workflow action, actor context, object state, compartment state, backend result, and physical evidence.

## 7.11 Failure Modes

Representative custody failure modes include:

- Object state is unknown or missing.
- Object is not eligible for requested action.
- Compartment is occupied when expected vacant.
- Compartment is vacant when expected occupied.
- Reservation expires before physical action completes.
- Door opens but object presence cannot be confirmed.
- Backend says object is available but local compartment state says occupied.
- Local state says staged but backend does not acknowledge the stage.
- Object is returned as defective without proper disposition context.
- Actor retrieves from the wrong compartment.
- Hardware evidence conflicts with database state.
- Administrative correction changes state without adequate evidence.
- Custody transition completes locally but ACK fails.

Failures should produce visible custody status, durable transaction evidence, and a reconciliation path.

## 7.12 Security and Audit Considerations

Custody-changing actions must be governed because they affect responsibility for physical objects.

Security and audit requirements include:

- Actor identity or credential context should be tied to custody transitions where applicable.
- Workflow key and workflow action should be recorded with custody changes.
- Backend authorization should be recorded when required.
- Physical location and compartment identity should be recorded.
- Defect, exception, and administrative correction actions should be audited.
- Custody state changes should preserve previous state, new state, timestamp, actor, and transaction reference where practical.
- Reconciliation should not erase original evidence.

The platform must be able to explain why an object changed state and what evidence supports that change.

## 7.13 Commercial Significance

Custody Governance is commercially significant because it allows multiple products and deployments to share a common concept of controlled physical responsibility. A customer may describe the workflow as pickup, checkout, staging, return, exchange, or equipment issue, but the platform can reuse the same custody model underneath.

This improves supportability, strengthens audit confidence, and makes new custody-based products easier to configure and license.

## 7.14 IP Significance

Custody Governance contributes to Toren's intellectual-property position by defining a repeatable method for connecting workflow intent, actor authority, physical location, local state, backend state, transaction evidence, and reconciliation into a governed custody model.

The protectable value is not merely tracking an item. The value is the custody governance method that preserves operational truth across physical actions, backend authority, local persistence, and failure recovery.

## 7.15 Related Implementation Evidence

Candidate implementation evidence may include:

- Locker status tables.
- Asset status records.
- Reservation records.
- Current asset or package references on compartment records.
- Workflow action fields.
- Defect option handling.
- Transaction journal custody states.
- ACK payloads containing custody outcome.
- Reconciliation DTOs.
- Administrative correction logs.
- Door or presence sensor logs.

This evidence should be expanded in Appendix F as the implementation matures.

## 7.16 Boundary Rule

Custody Governance owns custody semantics, valid transitions, exception meaning, and the relationship between physical custody locations and custody objects. It does not own relay commands, scanner input, UI rendering, API transport, storage mechanics, or administrative authority. It collaborates with those technologies to keep physical state, business authorization, transaction evidence, and custody meaning aligned.
