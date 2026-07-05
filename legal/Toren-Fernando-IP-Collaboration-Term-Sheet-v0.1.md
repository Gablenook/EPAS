# Toren / Fernando IP and Collaboration Term Sheet v0.1

**Status:** Business discussion draft; not legal advice; intended for attorney review.  
**Purpose:** Establish a plain-English foundation for a later agreement packet protecting Toren / Kevin IP and Fernando / SmartLockerAP IP while enabling active technical collaboration.  
**Parties contemplated:** Kevin Booth / Toren and Fernando / SmartLocker, LLC / SmartLockerAP, LLC, with final legal party names to be confirmed by counsel.  
**Primary technical exhibit:** Exhibit A — Edge Platform Architecture Specification (EPAS), Version 2.0 Publication Draft, Repository: `Gablenook/EPAS`.

---

## 1. Business Context

Kevin / Toren and Fernando / SmartLockerAP are not entering a contractor, employee, co-founder, advisor, or vendor relationship.

The intended relationship is a collaboration between separately owned but interoperating platforms:

- **Toren / Kevin** owns and controls EPAS, the Toren Edge Platform, platform architecture, edge execution model, specifications, documentation, workflows, commercial packaging, and related intellectual property.
- **Fernando / SmartLockerAP** owns and controls the SmartLockerAP backend platform and related backend software, methods, services, infrastructure, and intellectual property.
- **SmartLocker, LLC** may sell locker products manufactured by Penco Products or others and may request licenses from Toren / Kevin and Fernando / SmartLockerAP for the software needed to deliver a complete customer solution.
- **Penco Products or other channel partners** may sell locker products that require the combined software solution and may request licenses from one or both platform owners.
- For customer simplicity, licensing may later be structured through SmartLockerAP, SmartLocker, LLC, a joint commercial vehicle, or another licensing administrator. That commercial structure should not change underlying IP ownership unless separately agreed in writing.

The core business goal is to let the platforms work hand in hand while preventing informal collaboration from diluting either party's IP ownership.

---

## 2. Proposed Agreement Packet

The final agreement packet should likely include four documents:

1. **Mutual Confidentiality and Non-Use Agreement**
2. **IP Ownership and Contribution Agreement**
3. **Development / Collaboration Statement of Work**
4. **Toren IP Schedule and Background Technology Register**

The most important document is the **IP Ownership and Contribution Agreement**. It should clearly separate background IP, new work product, platform-specific inventions, reusable tools, confidential information, reverse engineering restrictions, and future license rights.

---

## 3. Definitions to Use in the Agreement Packet

### 3.1 Toren / Kevin Background IP

Toren / Kevin Background IP means all IP, know-how, specifications, architecture, source code, documentation, figures, workflows, naming, strategy, product hierarchy, implementation direction, and commercial packaging created, conceived, reduced to practice, authored, or controlled by Kevin / Toren before Fernando's contribution or outside Fernando / SmartLockerAP work.

This includes, at minimum:

- EPAS — Edge Platform Architecture Specification
- Toren Edge Platform architecture
- Edge execution model
- Edge / cloud interaction model from the Toren side
- Kiosk, edge, workflow, transaction, audit, commissioning, and deployment models developed by Kevin / Toren
- Toren platform documentation, diagrams, figures, examples, product naming, and commercial packaging
- Toren workflows, business process models, and customer deployment patterns
- Toren software, source code, libraries, DLLs, executable components, configuration models, and technical specifications
- Any patent disclosures, invention notes, diagrams, claims concepts, or technical descriptions derived from Kevin / Toren work

### 3.2 Fernando / SmartLockerAP Background IP

Fernando / SmartLockerAP Background IP means all IP, know-how, source code, tools, templates, methods, libraries, services, APIs, backend architecture, infrastructure, data models, deployment practices, and reusable development methods created, conceived, reduced to practice, authored, or controlled by Fernando / SmartLockerAP before Toren collaboration or outside Toren-specific work.

This includes, at minimum:

- SmartLockerAP backend platform
- Backend API services and platform components developed by Fernando / SmartLockerAP
- Pre-existing SmartLockerAP libraries, tools, templates, infrastructure scripts, AI-assisted development practices, DevOps practices, and reusable methods
- SmartLockerAP customer, hosting, data, cloud, and service delivery architecture to the extent independently developed by Fernando / SmartLockerAP

### 3.3 Jointly Discussed Ideas

Jointly discussed ideas means concepts discussed during collaboration that are not yet embodied in a specific work product, source code contribution, written specification, patent disclosure, diagram, design, or implementation.

The agreement should say that informal discussion alone does not create joint ownership. Ownership should depend on:

- who brought the idea into the discussion;
- whether the idea derives from a party's background IP;
- whether the idea is implemented specifically in Toren / EPAS work, SmartLockerAP backend work, or both;
- whether the idea becomes a patentable invention; and
- whether the parties later document ownership or license rights in writing.

### 3.4 Toren Work Product

Toren Work Product means work created specifically for Toren, EPAS, the Toren Edge Platform, Toren-controlled edge products, Toren documentation, Toren source code, Toren figures, Toren workflows, Toren architecture, Toren specifications, Toren customer deployments, or Toren commercial packaging.

Unless expressly excluded in a signed written schedule, Toren Work Product should be owned by Toren / Kevin or assigned to Toren / Kevin.

### 3.5 SmartLockerAP Work Product

SmartLockerAP Work Product means work created specifically for SmartLockerAP backend platform, backend services, cloud platform, backend APIs, SmartLockerAP-managed infrastructure, or Fernando / SmartLockerAP-controlled commercial packaging.

Unless expressly excluded in a signed written schedule, SmartLockerAP Work Product should be owned by Fernando / SmartLockerAP.

### 3.6 Integration Work Product

Integration Work Product means interface definitions, payload structures, API contracts, deployment mappings, integration documents, test plans, and operational coordination artifacts created to allow Toren / EPAS and SmartLockerAP to interoperate.

Integration Work Product should not automatically make either party the owner of the other party's platform. A later agreement should decide whether Integration Work Product is:

- owned by the party that authored it;
- jointly owned only for the specific integration layer;
- cross-licensed for the joint solution; or
- assigned to one party with a defined license to the other.

The recommended starting position is reciprocal use rights for the defined integration, with no transfer of either party's platform ownership.

---

## 4. Starting Ownership Position

### 4.1 Toren / Kevin Owns

Toren / Kevin owns or controls:

- EPAS and all versions of the Edge Platform Architecture Specification
- Toren Edge Platform architecture
- Toren platform source code and executable components
- Toren documentation, diagrams, figures, workflows, examples, and specifications
- Toren naming, product hierarchy, deployment model, workflow model, transaction architecture, and commercial packaging
- Toren business strategy, licensing model, commissioning model, and productization direction
- Toren-created patent disclosures, invention notes, and patentable subject matter derived from Toren / Kevin work

### 4.2 Fernando / SmartLockerAP Owns

Fernando / SmartLockerAP owns or controls:

- SmartLockerAP backend platform
- SmartLockerAP backend source code, services, APIs, infrastructure, deployment model, and data model
- Fernando's pre-existing tools, methods, libraries, templates, reusable development practices, know-how, and AI-assisted development workflows
- SmartLockerAP-created patent disclosures, invention notes, and patentable subject matter derived from Fernando / SmartLockerAP work

### 4.3 No Implied Joint Ownership

Collaboration, technical discussion, troubleshooting, access to repositories, review of code, participation in meetings, or contribution to customer delivery should not create implied joint ownership.

Joint ownership should exist only if the parties expressly agree in a signed writing or if legally required for a specific patentable invention based on actual inventorship, with commercial ownership and license rights then handled under the agreement.

---

## 5. Work Product Rules

### 5.1 Work Specifically for Toren

Work performed specifically for Toren, EPAS, Toren Edge Platform products, Toren software, Toren documentation, Toren figures, Toren workflows, Toren architecture, or Toren customer deployments should be owned by Toren / Kevin unless expressly excluded in writing.

This should include:

- source code changes to Toren-controlled repositories;
- changes to Toren DLLs, edge services, kiosk software, transaction services, workflow definitions, commissioning tools, and local control services;
- Toren specification changes;
- Toren diagrams and figures;
- Toren deployment documents;
- Toren product descriptions and commercial packaging; and
- customer-specific Toren implementation artifacts.

### 5.2 Work Specifically for SmartLockerAP

Work performed specifically for SmartLockerAP backend platform, backend APIs, backend services, cloud services, SmartLockerAP infrastructure, or SmartLockerAP commercial packaging should be owned by Fernando / SmartLockerAP unless expressly excluded in writing.

### 5.3 Integration Work

Integration work should be carefully documented. The agreement should avoid language such as “we both own the solution” unless that is truly intended.

A better approach is:

- Toren owns Toren-side implementation.
- SmartLockerAP owns SmartLockerAP-side implementation.
- Each party receives a limited, perpetual, non-exclusive license to use integration specifications and interface definitions as needed to operate, support, license, and maintain the joint solution.
- Neither party receives ownership of the other party's source code, platform architecture, or background IP merely because the systems interoperate.

---

## 6. Background Technology and Reusable Tools

Fernando may retain his pre-existing tools, methods, libraries, templates, AI prompts, code-generation practices, DevOps methods, and reusable development practices, provided they are listed or described in a background technology schedule.

Kevin / Toren may retain Toren pre-existing tools, methods, libraries, templates, specifications, code, documentation, and platform architecture, provided they are listed or described in a Toren background technology schedule.

If either party uses background technology in delivered work, the other party should receive only the license needed to use, maintain, deploy, support, and commercialize the delivered work as intended. That license should not become a general ownership transfer.

---

## 7. Patentable Inventions

Patentable inventions should be handled separately from copyright ownership.

The agreement should say:

- Actual inventorship will be determined under applicable patent law based on who made inventive contributions to the claimed invention.
- The parties will document invention disclosures promptly.
- The parties will not assume that collaboration, coding, testing, or implementation support alone makes someone an inventor.
- Commercial ownership, assignment obligations, and license rights will follow the agreement, subject to legally correct inventorship.
- Each party will cooperate in signing patent assignments, declarations, powers of attorney, and related documents needed to protect the agreed ownership and licensing structure.
- Patent prosecution strategy, filing costs, maintenance costs, abandonment decisions, and enforcement decisions must be addressed in the final agreement.

Recommended starting point:

- Toren / Kevin owns patentable inventions derived primarily from Toren / EPAS / Toren Edge Platform architecture or Toren implementation.
- Fernando / SmartLockerAP owns patentable inventions derived primarily from SmartLockerAP backend platform architecture or backend implementation.
- Inventions that genuinely require inventive contribution from both parties should be documented separately and may be jointly owned or assigned/licensed according to a specific written invention schedule.

---

## 8. Confidentiality and Non-Use

Each party should treat the other party's confidential information as confidential and may use it only for the defined collaboration.

Confidential information should include:

- source code;
- DLLs, binaries, services, build outputs, and executable components;
- specifications and unpublished technical documents;
- architecture diagrams;
- patent disclosures and invention notes;
- customer information and deployment details;
- pricing, licensing, commissioning fees, and commercial strategy;
- AI prompts, generated work, and troubleshooting outputs containing confidential information;
- security information, credentials, keys, certificates, tokens, and deployment secrets;
- non-public repository content;
- product roadmaps and business plans.

The agreement should prohibit using confidential information to build, train, generate, reverse engineer, reproduce, or commercialize a competing or derivative product outside the agreed collaboration.

---

## 9. Reverse Engineering / Decompilation / AI-Assisted Analysis

Because there has already been an instance where a Toren DLL was reverse-engineered during troubleshooting, the final agreement should address this directly and practically.

Recommended position:

- No party may reverse engineer, decompile, disassemble, inspect, reconstruct, scrape, train on, or derive source code, architecture, algorithms, data structures, or proprietary methods from the other party's binaries, DLLs, services, repositories, hosted systems, APIs, or documentation except with prior written permission for a specific purpose.
- Emergency troubleshooting does not create ownership or license rights.
- If reverse engineering or AI-assisted analysis occurs accidentally or without proper authorization, the receiving party must promptly disclose it, stop the activity, preserve evidence, segregate any resulting materials, delete or return unauthorized outputs if requested, and not use those outputs for any purpose except resolving the incident.
- AI tools must not be given the other party's confidential source code, binaries, specifications, credentials, or customer data unless the parties have approved the tool, data handling terms, and permitted scope in writing.
- The agreement should distinguish between good-faith troubleshooting and unauthorized derivative use, but it should still protect the underlying IP.

---

## 10. Licenses Needed for Commercial Operation

The agreement packet should separate IP ownership from future commercial licensing.

Potential licensing model:

- SmartLocker, LLC sells locker products made by Penco Products or others.
- SmartLocker, LLC requests or receives licenses from Toren / Kevin and Fernando / SmartLockerAP for the software components needed for the complete solution.
- Penco Products or another channel partner may license needed software directly from Toren / Kevin, Fernando / SmartLockerAP, SmartLockerAP, SmartLocker, LLC, or another agreed licensing administrator.
- Customer-facing licensing may be simplified into one product offering, but that should not blur underlying ownership.

Example commercial terms to evaluate later:

- recurring software license fee, such as a per-opening per-month fee;
- Toren commissioning fee, such as a per-opening installation / commissioning fee;
- backend service fee;
- support / maintenance fee;
- revenue share between platform owners;
- minimum monthly fee;
- customer-specific customization fee;
- license administrator fee if one entity collects and distributes payments.

These terms should be handled in a later licensing agreement, not buried inside the IP ownership agreement.

---

## 11. What Fernando Can Reuse Elsewhere

Fernando should be free to reuse his general skills, experience, pre-existing tools, reusable development methods, backend practices, templates, and know-how, provided he does not use or disclose Toren confidential information or Toren-specific work product.

Fernando should not reuse elsewhere:

- Toren source code;
- Toren DLL internals or reconstructed logic;
- EPAS protected expression, figures, specification text, or proprietary diagrams;
- Toren-specific workflow models, transaction architecture, or edge platform architecture except as licensed;
- Toren customer-specific deployment details;
- Toren patent disclosures, claims concepts, or invention notes;
- Toren commercial strategy, pricing, or packaging except as authorized.

---

## 12. What Toren Can Use Forever

Toren should receive a perpetual right to use, maintain, modify, deploy, support, commercialize, and license Toren Work Product and Toren-side integration work.

If Fernando contributes background technology that is necessary for Toren to use delivered Toren Work Product, Toren should receive a perpetual, irrevocable, worldwide, royalty-free or commercially defined license to that background technology only to the extent embedded in or necessary to use the delivered work as intended.

The final agreement should define whether this license is:

- non-exclusive or exclusive;
- sublicensable to customers, installers, manufacturers, and channel partners;
- transferable with Toren assets or a Toren acquisition;
- limited to the locker / edge platform field; and
- subject to payment or revenue-share terms.

---

## 13. What SmartLockerAP Can Use Forever

Fernando / SmartLockerAP should receive a perpetual right to use, maintain, modify, deploy, support, commercialize, and license SmartLockerAP Work Product and SmartLockerAP-side integration work.

If Toren contributes background technology necessary for SmartLockerAP to operate the agreed integration, SmartLockerAP should receive only the license needed to operate, support, and commercialize the joint customer solution, not a general right to clone, replace, or independently commercialize the Toren Edge Platform.

---

## 14. End of Relationship

If the relationship ends:

- each party keeps its own background IP;
- each party keeps work product assigned to it under the agreement;
- licenses already granted for deployed customers should continue as defined in the licensing agreement;
- neither party may use the other party's confidential information to build a competing substitute;
- repositories, credentials, binaries, confidential documents, and customer data must be returned, deleted, or access-restricted as appropriate;
- pending patent disclosures and joint invention issues must be resolved in writing;
- customer support obligations must be handled in a transition plan;
- neither party should interfere with existing customer operations or installed systems.

---

## 15. Open Business Questions

The final agreement packet should answer these before lawyer drafting:

1. What are the exact legal names of all parties?
2. Will Toren be a separate legal entity now, or will Kevin initially hold IP personally and assign/license it to Toren later?
3. Will Fernando sign personally, through SmartLockerAP, through SmartLocker, LLC, or through both entities?
4. What IP is already owned by SmartLocker, LLC versus SmartLockerAP, LLC?
5. Who will own customer-specific customizations?
6. Who will own integration-layer API specifications?
7. Will SmartLockerAP be allowed to act as the licensing administrator for the combined software product?
8. If one entity collects customer license fees, what audit, reporting, payment, and termination rights apply?
9. Will Toren receive a direct license to SmartLockerAP APIs needed for installed systems?
10. Will SmartLockerAP receive a direct license to Toren edge components needed for installed systems?
11. Are licenses sublicensable to Penco Products, SmartLocker, LLC, dealers, installers, customers, and support providers?
12. Who pays patent filing, prosecution, maintenance, and enforcement costs?
13. What happens if one party decides not to pursue a patent?
14. What happens if one party is acquired or shuts down?
15. What reverse-engineering incident response process should be used?
16. What AI tools are approved, and what data may be provided to them?
17. What repository access rules, code review rules, and binary access rules apply?
18. What customer deployments are already covered by the collaboration?
19. What fee structure is intended: per opening per month, commissioning fee, support fee, or another model?
20. What happens to deployed customers if the parties disagree later?

---

## 16. Recommended Immediate Next Steps

1. Create a Toren Background IP Schedule using EPAS as Exhibit A.
2. Create a Fernando / SmartLockerAP Background IP Schedule.
3. Identify any existing repositories, DLLs, binaries, API services, documents, diagrams, and specifications each party has already shared.
4. Document the prior DLL reverse-engineering incident as a collaboration-control issue, not as an accusation, and use it to justify a clear reverse-engineering / AI-assisted analysis clause.
5. Decide whether Kevin personally owns the Toren IP initially or whether Toren is already the intended owner.
6. Decide whether SmartLockerAP will be only the backend platform owner or also the licensing administrator.
7. Have counsel convert this term sheet into the four-document agreement packet.

---

## 17. Plain-English Principle

The agreement should protect both sides without pretending the collaboration is something it is not.

Toren / Kevin and Fernando / SmartLockerAP are separate platform owners building interoperating components of a final customer solution. Collaboration should create compatibility, not accidental co-ownership. Each party should be able to innovate, license, and protect its own platform while granting the limited rights needed for the combined solution to work for customers.
