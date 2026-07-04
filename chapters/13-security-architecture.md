# Chapter 13 — Security Architecture

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Chapter framework / pending expansion  
**Primary Figure:** Figure 13 — Security Trust Boundary Model

---

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
