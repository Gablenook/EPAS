# Chapter 7 — Custody Governance

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Chapter framework / pending expansion  
**Primary Figure:** Figure 7 — Custody State Model

---

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
