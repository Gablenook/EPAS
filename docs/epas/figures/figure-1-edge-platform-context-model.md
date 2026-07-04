# Figure 1 — Edge Platform Context Model

**Canva design:** https://www.canva.com/d/Gu3g4La3e8rx7P9

**Figure caption:**  
Figure 1 — The Edge Platform coordinates enterprise authority, local physical execution, hardware control, operational state, and audit evidence.

## Purpose

This figure is the context model for the Toren Edge Platform within EPAS. It shows Toren Edge Platform as the local edge coordinator between enterprise authority, human interaction, credential/scan devices, hardware controllers, physical compartments, local persistence, administrative support, and audit evidence.

## Diagram structure

- **Center:** Toren Edge Platform
- **Surrounding context nodes:**
  - Enterprise Systems
  - Human Operators
  - Credential / Scan Devices
  - Hardware Controllers
  - Physical Compartments
  - Local Persistence
  - Audit Evidence
  - Administrative Support

## Flow intent

- **Enterprise authorization / policy / entitlement** flows from Enterprise Systems toward Toren Edge Platform.
- **Local physical execution** flows from Toren Edge Platform through Hardware Controllers to Physical Compartments.
- **Acknowledgement / reconciliation / audit evidence** flows back toward Enterprise Systems and Audit Evidence.
- **Operational state** is maintained through Local Persistence.
- **Administrative Support** provides configuration, diagnostics, recovery, and service workflows.

## Color palette guidance

Use the palette as a controlled technical-spec palette, not as unrelated decoration.

| Role | Suggested color direction | Purpose |
|---|---|---|
| Background | Warm off-white / very light gray | Calm document background |
| Main text | Dark charcoal | Primary readability |
| Node outlines | Soft slate / blue-gray | Structural definition |
| Normal arrows | Muted steel-blue | Standard platform/process flow |
| Enterprise authority accent | Muted amber | Authorization / policy / entitlement flowing in |
| Evidence/state accent | Soft teal | ACK / reconciliation / evidence / operational state flowing back |

## Design notes

- Keep most nodes neutral: white fill, slate outline, charcoal text.
- Use amber sparingly for enterprise authority only.
- Use teal sparingly for audit, evidence, reconciliation, and operational state feedback.
- Avoid dark backgrounds, neon colors, gradients, cyber-style design, dramatic shadows, or excessive saturation.
- Preserve generous whitespace and a clean hub-and-spoke layout.
