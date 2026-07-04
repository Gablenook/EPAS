# Development / Collaboration Statement of Work v0.1

**Status:** Business/legal discussion draft; not legal advice; intended for attorney review.  
**Purpose:** Define how Kevin / Toren and Fernando / SmartLockerAP / SmartLocker, LLC will collaborate operationally while preserving separate IP ownership.  
**Related documents:**

- `legal/Toren-Fernando-IP-Collaboration-Term-Sheet-v0.1.md`
- `legal/Toren-Background-IP-Schedule-v0.1.md`
- `legal/Fernando-SmartLockerAP-Background-IP-Schedule-v0.1.md`
- `legal/Mutual-Confidentiality-and-Non-Use-Agreement-v0.1.md`
- `legal/IP-Ownership-and-Contribution-Agreement-v0.1.md`

---

## 1. Purpose

This Statement of Work defines the practical collaboration process for developing, integrating, testing, deploying, supporting, and improving a combined solution using Toren / EPAS edge platform assets and SmartLockerAP backend platform assets.

This SOW is not intended to transfer ownership. It operates under the IP Ownership and Contribution Agreement and the Mutual Confidentiality and Non-Use Agreement.

---

## 2. Collaboration Model

The parties are separately owned platform contributors.

- Kevin / Toren is responsible for Toren / EPAS edge-side architecture, local execution, workflow model, local transaction handling, kiosk-side behavior, edge documentation, and Toren-controlled implementation artifacts.
- Fernando / SmartLockerAP is responsible for SmartLockerAP backend services, hosted APIs, backend authorization, backend validation, backend data model, backend administration, service hosting, and SmartLockerAP-controlled implementation artifacts.
- SmartLocker, LLC may sell locker hardware and may participate in customer delivery, licensing, and commercial packaging as separately agreed.
- Penco Products or other hardware suppliers may provide locker products as separately agreed.

---

## 3. Scope of Collaboration

The collaboration may include:

- integrating Toren / EPAS edge systems with SmartLockerAP backend services;
- defining API contracts and payloads;
- defining workflow mappings between edge actions and backend records;
- supporting locker authorization, asset validation, acknowledgement, and reconciliation;
- preparing customer demonstrations;
- supporting customer deployments;
- resolving defects across edge and backend boundaries;
- documenting deployment patterns;
- preparing future licensing and commercial packaging models.

The collaboration does not include transfer of either party's platform ownership unless separately agreed in writing.

---

## 4. Out of Scope Unless Separately Agreed

The following are out of scope unless expressly approved in writing:

- transfer of Toren Background IP;
- transfer of Fernando / SmartLockerAP Background IP;
- broad sublicensing of either platform;
- expanded access to production systems beyond approved collaboration roles;
- source repository access beyond agreed repositories and branches;
- direct modification of the other party's controlled platform without review;
- customer-facing license commitments on behalf of the other party;
- use of the other party's confidential information in unapproved external systems;
- expansion into unrelated products, customers, or markets beyond the agreed collaboration.

---

## 5. Workstreams

### 5.1 Toren / EPAS Edge Workstream

Toren-side work may include:

- EPAS specification updates;
- edge architecture documentation;
- kiosk workflow implementation;
- local locker control behavior;
- transaction journaling;
- local acknowledgement handling;
- recovery and reconciliation support;
- local audit logging;
- commissioning process;
- customer-specific workflow configuration;
- Toren-side integration client logic;
- deployment documentation.

### 5.2 SmartLockerAP Backend Workstream

SmartLockerAP-side work may include:

- backend API implementation;
- actor / role / permission handling;
- asset validation;
- locker authorization;
- acknowledgement endpoint handling;
- reconciliation endpoint handling;
- backend event history;
- customer / site / kiosk / locker-bank administration;
- backend database management;
- hosted service deployment;
- backend logging, monitoring, and support.

### 5.3 Integration Workstream

Integration work may include:

- API request / response contracts;
- payload examples;
- field mappings;
- status codes and error models;
- workflow key and action mapping;
- test scripts and test data;
- integration diagrams;
- customer deployment runbooks;
- issue triage process;
- version compatibility matrix.

---

## 6. Repository and File Access

Repository and file access should be limited by role and need.

Recommended rules:

- Toren-controlled repositories remain controlled by Kevin / Toren.
- SmartLockerAP-controlled repositories remain controlled by Fernando / SmartLockerAP.
- Cross-access should be limited to the minimum needed for integration.
- Branch protections, pull requests, and review gates should be used where practical.
- Direct commits to the other party's controlled repositories should be avoided unless expressly approved.
- Access should be removed when no longer needed.
- Repository access does not create ownership or license rights beyond the written agreement.

---

## 7. Change Control

Recommended process:

1. Identify whether a change is Toren-side, SmartLockerAP-side, or integration-layer.
2. Create an issue or work item describing the change.
3. Identify affected repositories, branches, APIs, configuration, and customer deployments.
4. Make changes in a branch or controlled environment.
5. Review changes with the responsible platform owner.
6. Test locally or in a shared test environment.
7. Document version numbers, commit hashes, configuration changes, and deployment notes.
8. Deploy only after the responsible platform owner approves.

---

## 8. API Contract Management

API contracts should be documented and versioned.

Each API contract should identify:

- endpoint name and purpose;
- owning platform;
- request payload;
- response payload;
- required fields;
- optional fields;
- authentication and authorization requirements;
- error responses;
- retry behavior;
- idempotency expectations;
- logging expectations;
- version compatibility;
- deprecation rules.

Changes that affect the other platform should not be made without notice and testing.

---

## 9. Testing and Validation

Testing should include:

- unit tests where practical;
- API contract tests;
- edge / backend integration tests;
- workflow tests;
- offline / degraded connectivity tests where relevant;
- acknowledgement and reconciliation tests;
- customer deployment acceptance tests;
- rollback tests where practical.

Test results should be documented with dates, versions, commit hashes, environment names, and known limitations.

---

## 10. Customer Deployment Process

For each customer deployment, the parties should document:

- customer name;
- site and location identifiers;
- locker hardware supplier;
- locker-bank identifiers;
- kiosk identifiers;
- backend tenant or customer configuration;
- workflow configuration;
- API environment;
- software versions;
- responsible support contacts;
- commissioning date;
- acceptance criteria;
- recurring license assumptions;
- commissioning fee assumptions;
- customer-specific customizations and ownership classification.

---

## 11. Support and Incident Handling

Support issues should be classified as:

- Toren-side issue;
- SmartLockerAP-side issue;
- integration issue;
- hardware issue;
- customer configuration issue;
- network / environment issue;
- unknown / triage required.

Incident records should capture:

- date and time;
- customer / site;
- affected device or service;
- observed behavior;
- logs and diagnostics;
- responsible owner;
- corrective action;
- whether protected materials were involved;
- whether the issue created new work product or invention material.

---

## 12. Protected Material Handling

Protected materials include source code, compiled components, hosted service internals, database schemas, confidential specifications, customer data, access credentials, patent notes, invention disclosures, and non-public commercial terms.

Rules:

- share only what is needed;
- avoid unnecessary local copies;
- do not share access credentials through unsecured channels;
- do not provide protected materials to unapproved external systems;
- mark sensitive documents where practical;
- log significant disclosures;
- remove access when no longer needed.

---

## 13. AI-Assisted Development Rules

AI tools may be useful, but they must be controlled.

Before using AI tools with collaboration materials, the parties should define:

- approved tools;
- allowed data categories;
- prohibited data categories;
- redaction rules;
- whether code may be submitted;
- whether customer data may be submitted;
- whether patent notes may be submitted;
- retention restrictions;
- output review process.

Default position: no protected materials from the other party should be provided to AI tools without written approval.

---

## 14. Technical Incident Process

If a party discovers that protected technical material was accessed, analyzed, copied, uploaded, or used outside the approved process, the party should:

1. stop the activity;
2. notify the other party;
3. document what occurred;
4. preserve relevant evidence;
5. isolate generated or copied materials;
6. avoid further use until resolved;
7. agree on remediation steps;
8. update process controls to prevent recurrence.

This is intended to support trust and practical troubleshooting, not to turn every mistake into a dispute.

---

## 15. Deliverables

Potential deliverables may include:

- API contract documents;
- integration test plans;
- deployment runbooks;
- workflow configuration files;
- edge-side software releases;
- backend service releases;
- customer deployment records;
- commissioning records;
- support and incident logs;
- patent disclosure notes;
- license model notes;
- background IP schedule updates.

Each deliverable should be classified as Toren Work Product, SmartLockerAP Work Product, Integration Work Product, customer-owned work, or third-party work.

---

## 16. Acceptance Criteria

Acceptance criteria should be defined per deliverable.

For a customer deployment, acceptance may include:

- user authentication works;
- asset or package validation works;
- locker authorization works;
- physical locker action works;
- acknowledgement succeeds;
- backend records update correctly;
- reconciliation works for incomplete transactions;
- audit records are created;
- customer workflow behaves as configured;
- support documentation is complete enough for operation.

---

## 17. Commercial Terms Reserved

This SOW does not finalize pricing, recurring license fees, commissioning fees, revenue share, license administration, support fees, hardware sales margins, or customer-facing contract terms.

Those terms should be handled in a later commercial license agreement.

Known concepts to preserve for later discussion:

- recurring fee per opening per month;
- Toren commissioning fee per opening per installation;
- SmartLockerAP backend service fee;
- possible single customer-facing license administrator;
- possible direct licenses to SmartLocker, LLC, Penco Products, customers, dealers, or installers.

---

## 18. Termination or Pause of Collaboration

If collaboration is paused or terminated:

- each party should retain its Background IP;
- access should be reviewed and reduced or removed;
- confidential information should be returned, deleted, or access-restricted;
- open customer support obligations should be documented;
- deployed customers should be transitioned according to applicable license agreements;
- pending work product and inventions should be classified;
- unresolved integration issues should be documented.

---

## 19. Open Items for Counsel and Business Review

Before this SOW is signed, the parties should confirm:

- exact party names;
- legal owner of Toren IP;
- legal owner of SmartLockerAP backend IP;
- whether SmartLocker, LLC signs;
- repository access process;
- approved AI tool policy;
- security obligations;
- customer data obligations;
- support response obligations;
- ownership of customer-specific customizations;
- license administration model;
- customer transition obligations;
- dispute escalation process.

---

## 20. Plain-English Summary

This SOW is the working rulebook. Toren controls the edge platform. SmartLockerAP controls the backend platform. The parties can collaborate, integrate, test, deploy, and support customers, but each item of work should be classified so collaboration does not create accidental ownership confusion.
