# Figure 6 — Hardware Control and Compartment Execution Model

**Canva design:** https://www.canva.com/d/038r6G3lLjwqtfq

**Figure caption:**  
Figure 6 — Authorized edge workflows are translated into controller commands, mapped to physical compartments, verified through observed hardware status, and persisted for audit, recovery, and diagnostics.

## Purpose

This figure describes how Toren EPAS converts an authorized workflow decision into safe local hardware execution and observed compartment state. It shows the path from workflow orchestration and compartment assignment through controller communication, branch and port mapping, physical compartment activation, observed hardware status, local persistence, audit evidence, recovery, and diagnostics.

## Primary components

- Toren Edge Platform
- Workflow Orchestration
- Compartment Assignment
- Hardware Control Adapter
- Controller Connection Manager
- Locker Controller / Relay Controller
- Controller Branch A
- Controller Branch B
- Controller Ports
- Physical Compartments
- Door Lock / Strike / Solenoid
- Door Contact / Sensor Status
- Compartment Occupancy / Package Presence
- Local State Store
- Transaction Journal
- Audit Evidence Capture
- Recovery / Retry Logic
- Administrative Diagnostics

## Flow intent

1. Workflow Orchestration receives an authorized action and passes execution intent to Compartment Assignment.
2. Compartment Assignment selects the target compartment and maps it to controller branch, controller port, and compartment identity.
3. Hardware Control Adapter sends a command through the Controller Connection Manager.
4. Controller Connection Manager communicates with the Locker Controller / Relay Controller.
5. Controller Branch A and Controller Branch B represent physical controller channels or locker banks.
6. Controller Ports map to Physical Compartments.
7. Door Lock / Strike / Solenoid is activated for the selected compartment.
8. Door Contact / Sensor Status and Compartment Occupancy / Package Presence return observed physical state.
9. Observed state updates the Local State Store and Transaction Journal.
10. Audit Evidence Capture records command, response, status observation, and completion evidence.
11. Recovery / Retry Logic handles command failure, disconnected controller, ambiguous door status, timeout, or incomplete closure.
12. Administrative Diagnostics supports controller tests, branch connection checks, port mapping verification, and service intervention.

## Execution model

The diagram should emphasize that EPAS hardware control is not simply command dispatch. Physical execution is treated as an observed and recoverable state transition. Controller commands, responses, door status, occupancy signals, and completion evidence are all persisted so that each hardware action can be audited, retried, reconciled, or reviewed.

## Key callout

**EPAS treats hardware execution as observed state, not just issued commands.**

## Color palette guidance

Use the same controlled technical-spec palette as Figures 1 through 5.

| Role | Suggested color direction | Purpose |
|---|---|---|
| Background | Warm off-white / very light gray | Calm document background |
| Main text | Dark charcoal | Primary readability |
| Component outlines | Soft slate / blue-gray | Structural definition |
| Normal arrows | Muted steel-blue | Standard command and process flow |
| Authorization / command permission accent | Muted amber | Authorized workflow decision / command permission |
| Feedback/state/recovery accent | Soft teal | Door status, sensor feedback, audit evidence, recovery |

## Design notes

- Keep most components neutral: white fill, slate outline, charcoal text.
- Use amber only for authorization or command-permission context.
- Use teal for observed hardware status, state feedback, audit evidence, and recovery paths.
- Show Toren Edge Platform / software services on the left.
- Show Controller Connection Manager and Locker Controller / Relay Controller in the middle.
- Show Branch A / Branch B, Controller Ports, and Physical Compartments on the right.
- Show Local State Store, Transaction Journal, and Audit Evidence Capture as a persistence and feedback foundation.
- Avoid dark backgrounds, neon colors, gradients, cyber-style design, dramatic shadows, or excessive saturation.
- Preserve a readable technical architecture layout suitable for specification use.
