# Chapter 10 — Local Persistence

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Expanded chapter draft  
**Primary Figure:** Figure 10 — Local Persistence Model

---

## 10.1 Purpose

Local Persistence gives each edge node durable operational memory. It stores the configuration, identity, workflow cache, locker or compartment state, hardware mapping, transaction journal, audit references, diagnostics, and reconciliation records needed for the platform to operate safely at the physical edge.

Local Persistence is the Platform Technology that prevents edge execution from depending entirely on live backend availability or volatile application memory.

## 10.2 Problem Addressed

Physical edge operations happen locally. Doors open locally. Credentials are scanned locally. Relays fire locally. Operators walk away locally. If the only durable truth is remote, the platform may lose the ability to explain what happened when connectivity fails or the application restarts.

Local Persistence addresses this by storing the information needed to preserve local operational truth until backend acknowledgement, reconciliation, or administrative resolution can complete.

## Figure 10 — Local Persistence Model

> **Diagram Placeholder:** Create a data model diagram showing local stores for kiosk configuration, site identity, locker bank records, compartment records, locker status, workflow cache, hardware mapping, transaction journal, audit references, diagnostic logs, administrative settings, and reconciliation queue. Show links from commissioning, runtime orchestration, transaction integrity, custody governance, backend integration, administration, and hardware abstraction.

**Caption:** Figure 10 — Local Persistence gives the edge node durable operational memory for configuration, physical state, transaction recovery, audit, diagnostics, and reconciliation.

## 10.3 Primary Responsibilities

Local Persistence owns:

- Durable local storage mechanics.
- Local database initialization and migration support.
- Storage of commissioned identity and configuration.
- Locker bank and compartment records.
- Locker or compartment status records.
- Cached workflow configuration.
- Hardware mapping records.
- Transaction journal records.
- Reconciliation queue records.
- Administrative settings and support data.
- Diagnostic and audit references where stored locally.
- Data access patterns needed by local platform services.

Local Persistence should preserve platform state without becoming the owner of every state’s business meaning.

## 10.4 Local Data Categories

The local persistence model should include:

- Kiosk and site configuration.
- Customer, tenant, or licensee context.
- Locker bank and compartment records.
- Locker status records.
- Workflow configuration cache.
- Hardware mapping records.
- Transaction journal entries.
- Audit log index or references.
- Reconciliation queue.
- Administrative settings.
- Hardware health and diagnostic records.
- Version, migration, and schema readiness markers.

## 10.5 Boundaries and Non-Responsibilities

Local Persistence owns durable storage, not the meaning of every record.

Boundary examples:

- Custody Governance owns custody state meaning.
- Transaction Integrity owns journal state progression and recovery semantics.
- Configurable Workflow Engine owns workflow definition meaning.
- Commissioning owns initial identity binding.
- Hardware Abstraction owns device status interpretation.
- Backend Integration owns API contract state and remote acknowledgement meaning.
- Administrative Services owns governed correction workflows.

Local Persistence should not become a hidden business-rules engine simply because it stores important data.

## 10.6 Interfaces and Collaborators

Local Persistence collaborates with:

- **Commissioning Technology** to store identity, hardware topology, and initial state.
- **Configurable Workflow Engine** to cache and retrieve workflow definitions.
- **Runtime Orchestration** to read and update operational state.
- **Custody Governance** to persist custody and compartment status.
- **Transaction Integrity** to persist transaction journal state.
- **Backend Integration** to queue ACK and reconciliation records.
- **Hardware Abstraction** to store hardware mappings and diagnostic evidence.
- **Administrative Services** to inspect, correct, export, or reconcile local data.
- **Cross-Cutting Services** for diagnostics, logging, serialization, and error classification.
- **Security Architecture** for protected local configuration and access controls.

## 10.7 Data Ownership

Local Persistence owns storage mechanics for local records such as:

- Database files or local stores.
- Tables, collections, or serialized records.
- Schema version and migration status.
- Record creation and update operations.
- Local query access.
- Persistence error classification.
- Backup or support export behavior where applicable.

The platform technology that creates a record owns its meaning. Local Persistence owns the durable storage of that record.

## 10.8 Operational Model

A typical local persistence sequence includes:

1. Initialize or validate local database readiness.
2. Load commissioned identity and configuration.
3. Load workflow and hardware configuration.
4. Provide current compartment and custody state to runtime services.
5. Persist transaction journal milestones during execution.
6. Persist local state changes after physical action.
7. Queue ACK, retry, or reconciliation records when needed.
8. Support administrative review and export.
9. Preserve state across application restart and power loss.

Local Persistence should favor durability and explainability over convenience.

## 10.9 Failure Modes

Representative failure modes include:

- Local database unavailable.
- Schema migration fails.
- Record write fails after physical action.
- Record read returns stale or corrupt data.
- Workflow cache incompatible with runtime version.
- Hardware mapping missing or invalid.
- Transaction journal cannot be updated.
- Reconciliation queue cannot be written.
- Local storage full or inaccessible.
- Support export incomplete.
- Data conflict after backend synchronization.

Failures that occur after physical action should be treated as high-risk because they can weaken operational truth.

## 10.10 Configuration Model

Local persistence configuration may include:

- Database location.
- Schema version.
- Migration rules.
- Retention policy.
- Backup or export settings.
- Encryption or protection settings.
- Cache refresh settings.
- Retry and write-failure behavior.
- Diagnostic verbosity.

Configuration should be explicit and supportable in the field.

## 10.11 Security and Audit Considerations

Local data may contain identity, custody, transaction, and operational evidence. It must be protected from unauthorized access, tampering, and accidental loss.

Security and audit requirements include:

- Protected local configuration where sensitive values exist.
- Permissioned administrative access.
- Durable transaction and custody evidence.
- Audit trail for manual correction where applicable.
- Support export that avoids exposing secrets unnecessarily.
- Retention rules that preserve operational evidence long enough for reconciliation and support.

## 10.12 Persistence Principle

Local persistence should be treated as operational truth for physical edge events until reconciliation proves otherwise. Backend systems remain authoritative for enterprise business records, but the edge platform remains authoritative for what it physically executed. **Figure 10** and **Figure 11** should be interpreted together.

## 10.13 Commercial Significance

Local Persistence is commercially significant because it makes the platform reliable in real field conditions. Customers do not experience perfect networks, perfect operators, or perfect hardware. Durable local memory reduces support cost and increases confidence.

## 10.14 IP Significance

Local Persistence contributes to Toren's IP position by supporting a local-first operational truth model for governed physical-edge transactions, including transaction journaling, custody state, ACK/reconciliation queues, and administrative recovery evidence.

## 10.15 Related Implementation Evidence

Candidate evidence may include:

- SQLite schema.
- Locker and locker-status tables.
- Workflow cache tables or files.
- Transaction journal table.
- Reconciliation queue.
- Hardware mapping records.
- App settings records.
- Migration scripts.
- Support export files.
- Administrative review screens.

## 10.16 Boundary Rule

Local Persistence owns durable local storage mechanics and access to local platform records. It does not own the business, custody, workflow, hardware, security, or backend meaning of every stored value. Meaning is supplied by the Platform Technology that creates and consumes the record.
