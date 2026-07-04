# Appendix A — Platform Technology Responsibility Matrix

**Source:** Edge Platform Architecture Specification (EPAS)  
**Status:** Appendix framework / pending expansion

---

| Platform Technology | Primary Responsibility | Must Not Own | Primary Figure |
| --- | --- | --- | --- |
| Commissioning Technology | Site, kiosk, bank, controller, and locker setup | Runtime custody decisions | Figure 4 |
| Configurable Workflow Engine | Workflow definition and step progression | Hardware device implementation | Figure 5 |
| Runtime Orchestration | Transaction execution coordination | Enterprise business record ownership | Figure 6 |
| Custody Governance | Custody state rules and movement semantics | Relay-board protocols | Figure 7 |
| Transaction Integrity | Journal, recovery, and transaction state | Customer-specific screen layout | Figure 8 |
| Hardware Abstraction | Device-specific communication | Business authorization | Figure 9 |
| Local Persistence | Local operational state | Cloud source-of-truth policy | Figure 10 |
| Backend Integration | API contracts and enterprise communication | UI rendering | Figure 11 |
| Cross-Cutting Services | Logging, tracing, diagnostics, health | Workflow-specific business meaning | Figure 12 |
| Security Architecture | Identity, authority, permissions, protection | Locker assignment algorithms | Figure 13 |
| Administrative Services | Support, diagnostics, controlled override | Unlogged operational bypass | Figure 14 |
| Deployment Architecture | Install, upgrade, configuration packaging | Product strategy | Figure 15 |
| Commercial Architecture | Platform reuse and business alignment | Low-level runtime implementation | Figure 16 |
