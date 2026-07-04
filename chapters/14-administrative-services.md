# Chapter 14 — Administrative Services

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Chapter framework / pending expansion  
**Primary Figure:** Figure 14 — Administrative Operations Model

---

## 14.1 Purpose

Administrative Services allow trusted personnel to configure, diagnose, recover, and support the platform without bypassing governance.

## Figure 14 — Administrative Operations Model

> **Diagram Placeholder:** Create an administrative operations diagram with roles such as site administrator, support technician, field installer, and platform support. Show governed actions: locker status review, manual compartment test, controller test, workflow review, transaction journal inspection, recovery action, reconciliation action, log export, commissioning review, and out-of-service control. Show all actions flowing into audit logging.

**Caption:** Figure 14 — Administrative Services provide controlled support and recovery actions without bypassing platform governance.

## 14.2 Administrative Capabilities

Administrative services may include:

- Locker status review.
- Manual compartment test.
- Controller connection test.
- Workflow configuration review.
- Transaction journal inspection.
- Incomplete transaction recovery.
- Reconciliation tools.
- Hardware diagnostics.
- Local log export.
- Commissioning review.
- Out-of-service and return-to-service actions.

## 14.3 Administrative Principle

Administrative actions are still platform actions. They must be logged, permissioned, and explainable. **Figure 14** should explicitly show administrative actions flowing into audit evidence.
