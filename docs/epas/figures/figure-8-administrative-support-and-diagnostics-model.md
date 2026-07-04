# Figure 8 — Administrative Support and Diagnostics Model

**Canva design:** Pending — Canva generation failed through the connector during creation. The figure specification below is ready for Canva generation and should be updated with the final Canva design link once generated.

**Figure caption:**  
Figure 8 — Administrative support provides controlled configuration, diagnostics, recovery, exception review, and evidence lookup while preserving authorization, operational state, and audit traceability.

## Purpose

This figure describes how Toren EPAS administrative support provides configuration, diagnostics, service recovery, hardware verification, workflow setup, evidence lookup, and exception resolution without bypassing enterprise authority, operational state controls, or audit traceability.

The figure should show administrative support as a controlled edge capability rather than an unrestricted back door. Administrative actions are authorized, journaled, tied to administrator identity, and captured as audit evidence.

## Primary components

- Toren Edge Platform
- Administrative Console
- Authorized Administrator
- Enterprise Systems
- Configuration Management
- Kiosk / Site / Client Settings
- Workflow Configuration
- Locker Bank / Compartment Setup
- Controller Branch / Port Mapping
- Hardware Diagnostics
- Credential / Scan Device Diagnostics
- Transaction Recovery Console
- Exception Review
- Evidence Lookup
- Audit Evidence Capture
- Transaction Journal
- Local State Store
- Reconciliation Service
- Hardware Controllers
- Physical Compartments

## Flow intent

1. Authorized Administrator accesses the Administrative Console through a controlled administrative access path.
2. Administrative Console requires elevated authorization or permitted administrative role context before sensitive actions.
3. Configuration Management updates kiosk, site, client, workflow, locker bank, compartment, controller branch, and port mapping settings.
4. Hardware Diagnostics tests controller connectivity, branch status, port activation, door status, and compartment signals.
5. Credential / Scan Device Diagnostics verifies reader, scanner, and scan intake behavior.
6. Transaction Recovery Console reads Transaction Journal and Local State Store to identify incomplete, ACK pending, failed, or needs-reconciliation transactions.
7. Exception Review connects evidence, state, transaction history, administrator action, and reconciliation status.
8. Evidence Lookup reads audit evidence records and event history without altering the original evidence trail.
9. Reconciliation Service sends corrected, replayed, acknowledged, or exception-resolved updates back to Enterprise Systems.
10. All administrative actions are captured by Audit Evidence Capture and tied to administrator identity, action type, timestamp, and outcome.

## Visual structure

- Place **Administrative Console** prominently in the center inside a **Toren Edge Platform** boundary.
- Place **Authorized Administrator** on the left entering through a controlled access path.
- Place **Configuration Management**, **Workflow Configuration**, **Locker Bank / Compartment Setup**, and **Controller Branch / Port Mapping** in the upper portion of the diagram.
- Place **Hardware Diagnostics** and **Credential / Scan Device Diagnostics** to the right, connected to **Hardware Controllers** and **Physical Compartments**.
- Place **Transaction Recovery Console**, **Exception Review**, **Evidence Lookup**, **Transaction Journal**, **Local State Store**, and **Audit Evidence Capture** along the lower half.
- Place **Enterprise Systems** on the far right with reconciliation, administrative authority, and configuration governance paths.
- Show teal feedback paths for diagnostics, recovery, reconciliation, audit evidence, and operational state.
- Show amber only for elevated administrative permission or enterprise authority checks.

## Key callout

**Administrative tools support recovery and service without bypassing authorization, state, or evidence controls.**

## Color palette guidance

Use the same controlled technical-spec palette as Figures 1 through 7.

| Role | Suggested color direction | Purpose |
|---|---|---|
| Background | Warm off-white / very light gray | Calm document background |
| Main text | Dark charcoal | Primary readability |
| Component outlines | Soft slate / blue-gray | Structural definition |
| Normal arrows | Muted steel-blue | Standard configuration and diagnostic flow |
| Administrative authority accent | Muted amber | Elevated authorization / administrative permission |
| Diagnostics/state/recovery accent | Soft teal | Diagnostics feedback, recovery, reconciliation, evidence |

## Design notes

- Keep most components neutral: white fill, slate outline, charcoal text.
- Use amber only where administrator permission or enterprise authority is represented.
- Use teal for diagnostics feedback, recovery, reconciliation, evidence lookup, and operational state.
- Do not present administrative support as an override path around authorization or audit evidence.
- Show Transaction Journal, Local State Store, and Audit Evidence Capture as persistent controls that administrative workflows read from and write to.
- Avoid dark backgrounds, neon colors, gradients, cyber-style design, dramatic shadows, or excessive saturation.
- Preserve a readable technical architecture layout suitable for specification use.

## Canva generation prompt

Create a single-page professional architecture diagram titled **EPAS Figure 8 — Administrative Support and Diagnostics Model**. Use a light warm-gray background, charcoal text, slate outlines, muted steel-blue arrows, muted amber for admin authorization, and soft teal for diagnostics, recovery, reconciliation, state, and audit evidence. Center **Administrative Console** inside **Toren Edge Platform**. Surround it with Authorized Administrator, Configuration Management, Workflow Configuration, Locker / Compartment Setup, Controller Port Mapping, Hardware Diagnostics, Scan Device Diagnostics, Transaction Recovery, Exception Review, Evidence Lookup, Enterprise Systems, Hardware Controllers, Physical Compartments, Transaction Journal, Local State Store, and Audit Evidence Capture. Show administrative authorization into the console, configuration and diagnostics flowing outward, and state/evidence/recovery flowing back. Include the callout and caption listed above. Use a calm technical-spec style with no dark background, neon colors, gradients, cyber-style design, dramatic shadows, or saturated colors.
