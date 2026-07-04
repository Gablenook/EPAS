# Chapter 9 — Hardware Abstraction

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Expanded chapter draft  
**Primary Figure:** Figure 9 — Hardware Abstraction Layer

---

## 9.1 Purpose

Hardware Abstraction isolates platform logic from specific physical devices. The Toren Edge Platform should not embed scanner, reader, relay-controller, sensor, camera, printer, display, or future device details inside workflow, custody, backend, or UI logic.

Hardware Abstraction is the Platform Technology that lets the platform control physical devices while keeping operational meaning above the device layer.

## 9.2 Problem Addressed

Physical-edge systems frequently become hard to maintain when device details leak into business logic. A workflow screen may know relay numbers. A backend call may assume a controller branch. A custody rule may depend on a sensor protocol. A support tool may test a door by duplicating production hardware code. Each leak makes future hardware substitutions more expensive.

Hardware Abstraction addresses this by placing all device-specific communication behind stable platform interfaces. Platform services ask for operations such as scan received, credential read, open compartment, read door state, test controller, or report device health. Adapters handle the details of the actual hardware.

## Figure 9 — Hardware Abstraction Layer

> **Diagram Placeholder:** Create a layered diagram. Top: workflow, runtime, custody, administration, and backend-integration services. Middle: hardware abstraction interfaces such as scanner adapter, credential reader adapter, locker controller adapter, door sensor adapter, presence sensor adapter, camera adapter, printer adapter, and environmental sensor adapter. Bottom: concrete devices, protocols, drivers, DLLs, serial ports, USB HID devices, network devices, and future physical-control technologies. Show that platform services call stable interfaces while adapters own device-specific behavior.

**Caption:** Figure 9 — Hardware Abstraction allows the platform to support multiple physical devices without embedding device details in workflow, custody, or business logic.

## 9.3 Primary Responsibilities

Hardware Abstraction owns:

- Device discovery where applicable.
- Device connection and disconnection behavior.
- Device-specific protocol handling.
- Controller addressing and command translation.
- Scanner, reader, relay, sensor, camera, printer, and peripheral adapters.
- Hardware health reporting.
- Hardware test operations.
- Device error classification.
- Device timing and command-result interpretation.
- Safe exposure of physical capabilities to Runtime Orchestration and Administrative Services.

The hardware layer should expose platform-level operations, not raw device details, except where diagnostics deliberately require low-level information.

## 9.4 Hardware Categories

The platform may interact with:

- Barcode scanners.
- RFID or credential readers.
- Relay controllers.
- Locker or compartment controllers.
- Door sensors.
- Presence sensors.
- Touch displays.
- Cameras.
- Printers.
- Environmental sensors.
- Network-connected controllers.
- USB HID peripherals.
- Serial devices.
- Future compartment-control technologies.

## 9.5 Adapter Principle

Each hardware family should be represented through an adapter that exposes stable platform operations such as:

- `StartScan`
- `StopScan`
- `CredentialRead`
- `OpenCompartment`
- `ReadDoorState`
- `ReadPresenceState`
- `TestController`
- `GetHealth`
- `ResetDevice`
- `ExportDiagnostics`

The adapter owns device-specific details. Platform services own operational meaning.

## 9.6 Boundaries and Non-Responsibilities

Hardware Abstraction owns device communication and device health semantics. It does not decide whether:

- a workflow is valid,
- an actor is authorized,
- a custody transition is allowed,
- a backend request should be accepted,
- a transaction should be reconciled,
- a product should enable a workflow,
- or an administrator should be allowed to override state.

Hardware Abstraction may report that a door opened, but Custody Governance determines what that means. It may report that a relay command succeeded, but Transaction Integrity preserves the transaction evidence.

## 9.7 Interfaces and Collaborators

Hardware Abstraction collaborates with:

- **Runtime Orchestration** for live physical actions.
- **Commissioning Technology** for controller mapping and hardware validation.
- **Administrative Services** for manual tests and diagnostics.
- **Transaction Integrity** for command evidence and hardware-result recording.
- **Custody Governance** for interpreting physical state changes.
- **Local Persistence** for hardware mapping and configuration records.
- **Cross-Cutting Services** for logs, health, diagnostics, timeouts, and error classification.
- **Security Architecture** for protecting hardware-control authority.
- **Deployment Architecture** for drivers, DLLs, OS dependencies, and device installation requirements.

## 9.8 Data Ownership

Hardware Abstraction governs the meaning of hardware-facing data, including:

- Device identifiers.
- Controller branch, port, channel, address, or relay mapping.
- Device type and adapter type.
- Connection status.
- Command status.
- Door state.
- Presence state.
- Device health.
- Hardware error codes.
- Diagnostic details.

Local Persistence may store the records, but Hardware Abstraction owns the interpretation of device-specific results.

## 9.9 Operational Model

A typical hardware operation includes:

1. Runtime or administrative service requests a platform-level hardware action.
2. Hardware Abstraction resolves the configured adapter and mapped device.
3. Adapter translates the request into device-specific protocol or driver calls.
4. Adapter reports command attempt, result, error, or ambiguity.
5. Cross-Cutting Services record diagnostics.
6. Transaction Integrity records command evidence when part of a governed transaction.
7. Runtime Orchestration or Administrative Services decide what happens next.

Hardware Abstraction should not silently convert device failures into business decisions.

## 9.10 Failure Modes

Representative failure modes include:

- Device unavailable.
- Device driver missing.
- Serial port unavailable.
- USB HID reader not detected.
- Controller branch mapping wrong.
- Relay command succeeds on wrong output.
- Door sensor unavailable or stuck.
- Presence sensor ambiguous.
- Scanner sends malformed input.
- Reader returns duplicate credential events.
- Command times out.
- Device health unknown.
- Adapter throws unclassified error.

Failures should be classified, logged, and surfaced to the caller without hiding uncertainty.

## 9.11 Configuration Model

Hardware configuration should include:

- Device type.
- Adapter type.
- Controller branch or connection path.
- Port, channel, address, relay, or compartment mapping.
- Timeout settings.
- Retry settings.
- Test mode settings.
- Hardware enabled/disabled state.
- Diagnostic verbosity.
- Driver or dependency requirements where relevant.

Configuration should be explicit and inspectable during commissioning and support.

## 9.12 Security and Audit Considerations

Hardware actions can cause physical consequences, so hardware control must be protected.

Security and audit requirements include:

- Governed hardware actions should require transaction context or administrative authority.
- Manual tests should be permissioned and logged.
- Hardware mapping changes should be audited.
- Device errors should preserve diagnostic context.
- Sensitive hardware configuration should be protected where applicable.
- Physical commands should be traceable to workflow or administrative action.

## 9.13 Commercial Significance

Hardware Abstraction is commercially significant because it allows Toren-based products to support different controllers, readers, scanners, sensors, and future devices without rewriting the platform. It reduces vendor lock-in and increases deployment flexibility.

## 9.14 IP Significance

Hardware Abstraction contributes to Toren's IP position by defining a repeatable method for separating physical device control from workflow, custody, transaction, and backend meaning while preserving governed execution and evidence.

## 9.15 Related Implementation Evidence

Candidate evidence may include:

- Scanner services.
- Credential reader adapters.
- Locker controller services.
- Controller branch mapping tables.
- Hardware diagnostic logs.
- Manual test screens.
- Door or presence sensor adapters.
- Device health reports.
- Driver/DLL integration notes.

## 9.16 Boundary Rule

Hardware Abstraction owns device communication, physical command translation, hardware result interpretation, and device health semantics. It does not own workflow validity, actor authority, custody meaning, backend business authority, transaction recovery, or administrative permission policy.
