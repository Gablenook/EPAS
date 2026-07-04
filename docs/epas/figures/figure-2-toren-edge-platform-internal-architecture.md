# Figure 2 — Toren Edge Platform Internal Architecture

**Canva design:** https://www.canva.com/d/yO2Zc_bmuDI3o7L

**Figure caption:**  
Figure 2 — The Edge Platform separates operator interaction, workflow orchestration, enterprise authorization, hardware execution, local state, recovery, and audit evidence into coordinated edge services.

## Purpose

This figure describes the internal functional architecture of the Toren Edge Platform within EPAS. It expands the central edge platform shown in Figure 1 into coordinated edge services responsible for operator interaction, credential and scan intake, workflow control, enterprise authorization, local physical execution, operational state, recovery, diagnostics, and audit evidence.

## Platform boundary

The diagram should show a large outer boundary labeled **Toren Edge Platform**. Internal modules are organized as coordinated services inside that boundary.

## Internal modules

- Operator Experience Layer
- Credential & Scan Intake
- Workflow Orchestration
- Enterprise Authorization Client
- Locker / Compartment Assignment
- Hardware Control Adapter
- Local State Store
- Transaction Journal
- Audit Evidence Capture
- Reconciliation & Recovery
- Administrative Console
- Configuration & Diagnostics

## External connections

- **Enterprise Systems** connect to Enterprise Authorization Client and Reconciliation & Recovery.
- **Human Operators** interact through the Operator Experience Layer.
- **Credential / Scan Devices** feed scan and credential data into Credential & Scan Intake.
- **Hardware Controllers** connect through the Hardware Control Adapter.
- **Physical Compartments** are controlled downstream from Hardware Controllers.
- **Audit / Compliance Consumers** consume evidence produced by Audit Evidence Capture.

## Flow intent

1. Human Operators and Credential / Scan Devices provide identity, asset, package, or reference inputs.
2. Workflow Orchestration coordinates validation, authorization, assignment, hardware execution, journaling, and evidence capture.
3. Enterprise Authorization Client sends authorization requests to Enterprise Systems and receives authorization decisions.
4. Locker / Compartment Assignment determines the target compartment.
5. Hardware Control Adapter sends commands to Hardware Controllers and receives door/status responses.
6. Local State Store and Transaction Journal preserve operational state and incomplete transaction recovery.
7. Audit Evidence Capture records events and evidence.
8. Reconciliation & Recovery sends acknowledgement, reconciliation, and exception recovery information back to Enterprise Systems.
9. Administrative Console connects to Configuration & Diagnostics for setup, service, recovery, and troubleshooting.

## Color palette guidance

Use the same controlled technical-spec palette as Figure 1.

| Role | Suggested color direction | Purpose |
|---|---|---|
| Background | Warm off-white / very light gray | Calm document background |
| Main text | Dark charcoal | Primary readability |
| Module outlines | Soft slate / blue-gray | Structural definition |
| Normal arrows | Muted steel-blue | Standard platform/process flow |
| Enterprise authority accent | Muted amber | Authorization / policy / entitlement |
| Evidence/state accent | Soft teal | ACK / reconciliation / evidence / operational state feedback |

## Design notes

- Keep most modules neutral: white fill, slate outline, charcoal text.
- Use amber only for enterprise authorization / authority.
- Use teal only for audit evidence, reconciliation, recovery, and operational state feedback.
- Keep Workflow Orchestration prominent but restrained.
- Avoid dark backgrounds, neon colors, gradients, cyber-style design, dramatic shadows, or excessive saturation.
- Preserve generous whitespace and a clean modular layout.
