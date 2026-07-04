# Chapter 9 — Hardware Abstraction

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Chapter framework / pending expansion  
**Primary Figure:** Figure 9 — Hardware Abstraction Layer

---

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
