# Figure 4 — Authorization and Trust Boundary Model

**Canva design:** https://www.canva.com/d/TYo37LsAKXNaL_T

**Figure caption:**  
Figure 4 — Enterprise systems remain the source of authority while the Edge Platform enforces authorized local execution, records state and evidence, and reconciles interrupted or completed transactions.

## Purpose

This figure describes how Toren EPAS separates enterprise authority from local edge execution while preserving a clear platform boundary. Enterprise systems remain the source of identity, policy, entitlement, and authorization decisions. The Toren Edge Platform performs controlled local execution, state recording, evidence capture, acknowledgement, and reconciliation.

## Architecture zones

### Enterprise Authority Zone

- Enterprise Identity Systems
- Policy / Entitlement Engine
- Asset / Package / Work Order Systems
- Audit / Compliance Consumers

### Toren Edge Platform Boundary

- Enterprise Authorization Client
- Workflow Orchestration
- Local Policy Cache / Authorization Context
- Transaction Journal
- Local State Store
- Audit Evidence Capture
- Reconciliation & Recovery

### Physical Execution Zone

- Credential / Scan Devices
- Hardware Controllers
- Physical Compartments
- Door / Sensor Status

## Flow intent

1. Operator and scan inputs enter the Toren Edge Platform boundary through Credential / Scan Devices.
2. Toren Edge Platform requests authorization from the Enterprise Authority Zone.
3. Enterprise systems return authorization decisions, policy, and entitlement context.
4. Toren Edge Platform performs local physical execution only after authorization context is established.
5. Hardware commands flow from the edge platform to Hardware Controllers and Physical Compartments.
6. Door and sensor status returns from the Physical Execution Zone to the edge platform.
7. Transaction Journal and Local State Store preserve operational state and recovery context.
8. Audit Evidence Capture and Reconciliation & Recovery send acknowledgement, evidence, and reconciliation back to the Enterprise Authority Zone.
9. The edge platform may continue controlled recovery and reconciliation when enterprise connectivity is interrupted.

## Key callouts

- **Enterprise decides; edge executes and records.**
- **Interrupted transactions remain journaled until acknowledged or reconciled.**

## Color palette guidance

Use the same controlled technical-spec palette as Figures 1 through 3.

| Role | Suggested color direction | Purpose |
|---|---|---|
| Background | Warm off-white / very light gray | Calm document background |
| Main text | Dark charcoal | Primary readability |
| Zone and module outlines | Soft slate / blue-gray | Structural definition |
| Normal arrows | Muted steel-blue | Standard platform/process flow |
| Enterprise authority accent | Muted amber | Authorization / policy / entitlement decisions |
| Evidence/state accent | Soft teal | ACK / reconciliation / evidence / recovery |

## Design notes

- Use three lightly outlined zones: Enterprise Authority Zone, Toren Edge Platform Boundary, and Physical Execution Zone.
- Keep the Toren Edge Platform boundary central and prominent.
- Use amber only for enterprise authorization and decision context.
- Use teal only for acknowledgement, audit evidence, reconciliation, recovery, and operational state feedback.
- Avoid dark backgrounds, neon colors, gradients, cyber-style design, dramatic shadows, or excessive saturation.
- Preserve a clean boundary-based architecture layout suitable for a technical specification.
