# Chapter 10 — Local Persistence

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Chapter framework / pending expansion  
**Primary Figure:** Figure 10 — Local Persistence Model

---

## 10.1 Purpose

Local Persistence provides the edge node with durable operational memory. This includes configuration, locker state, journal entries, audit events, hardware mappings, and diagnostic records.

## Figure 10 — Local Persistence Model

> **Diagram Placeholder:** Create a data model diagram showing local stores for kiosk configuration, site identity, locker bank records, locker status, workflow cache, hardware mapping, transaction journal, audit references, diagnostic logs, administrative settings, and reconciliation queue. Show links from runtime services, commissioning, administration, and backend integration.

**Caption:** Figure 10 — Local Persistence gives the edge node durable operational memory for configuration, physical state, transaction recovery, audit, and reconciliation.

## 10.2 Local Data Categories

The local persistence model should include:

- Kiosk and site configuration.
- Locker bank and compartment records.
- Locker status records.
- Workflow configuration cache.
- Transaction journal.
- Audit log index or references.
- Hardware configuration.
- Reconciliation queue.
- Administrative settings.

## 10.3 Persistence Principle

Local persistence should be treated as operational truth for physical edge events until reconciliation proves otherwise. Backend systems remain authoritative for enterprise business records, but the edge platform remains authoritative for what it physically executed. **Figure 10** and **Figure 11** should be interpreted together.

## 10.4 Boundary Rule

Local Persistence owns durable storage of local platform state. It does not own the meaning of every stored state. Meaning is supplied by the Platform Technology that creates and consumes the record.
