# Design Review Template

Use this template when reviewing system designs at staff level.

## Design Overview

**System Name**: [Name]

**Purpose**: [What problem does this solve?]

**Designer**: [Who designed this?]

**Reviewer**: [Who is reviewing?]

**Date**: [Date]

---

## Requirements & Constraints

### Functional Requirements
- [Requirement 1]
- [Requirement 2]

### Non-Functional Requirements
- **Latency**: [Target latency, e.g., P95 < 100ms]
- **Throughput**: [Target QPS]
- **Availability**: [Target uptime, e.g., 99.9%]
- **Consistency**: [Consistency model]
- **Durability**: [Data durability requirements]

### Constraints
- **Budget**: [Cost constraints]
- **Timeline**: [Deadlines]
- **Dependencies**: [External dependencies]
- **Compliance**: [Regulatory requirements]

---

## Architecture Review

### High-Level Design
- [ ] Architecture diagram is clear and accurate
- [ ] Components and responsibilities are well-defined
- [ ] Data flow is documented
- [ ] Critical paths are identified

### Component Design
- [ ] Each component has a clear purpose
- [ ] Component boundaries are well-defined
- [ ] Interfaces are documented
- [ ] Dependencies are explicit

### Data Model
- [ ] Data model is appropriate for use case
- [ ] Schema is documented
- [ ] Data lifecycle is considered
- [ ] Data retention policies are defined

---

## Failure Modes & Reliability

### Failure Domains
- [ ] Failure domains are identified
- [ ] Blast radius is limited
- [ ] Failures are isolated
- [ ] Single points of failure are eliminated

### Failure Scenarios
- [ ] Common failure scenarios are documented
- [ ] Failure detection is planned
- [ ] Recovery procedures are defined
- [ ] Cascading failures are prevented

### Overload Behavior
- [ ] Behavior at 10× load is understood
- [ ] Behavior at 100× load is considered
- [ ] Load shedding is implemented
- [ ] Graceful degradation is planned

### SLIs, SLOs & Error Budgets
- [ ] SLIs are defined and measurable
- [ ] SLOs are set appropriately
- [ ] Error budgets are calculated
- [ ] Alerting thresholds are set

---

## Observability

### Metrics
- [ ] Key metrics are identified
- [ ] Latency metrics (P50/P95/P99) are tracked
- [ ] Throughput metrics are tracked
- [ ] Error rates are tracked
- [ ] Resource usage is monitored

### Logging
- [ ] Critical events are logged
- [ ] Log levels are appropriate
- [ ] Logs are structured
- [ ] Log retention is defined

### Tracing
- [ ] Critical paths are traced
- [ ] Spans are well-defined
- [ ] Trace sampling strategy is defined
- [ ] Cross-service correlation works

### Alerting
- [ ] Alerts are actionable
- [ ] Alert fatigue is avoided
- [ ] On-call procedures are defined
- [ ] Escalation paths are clear

---

## Change Safety

### Deployment Strategy
- [ ] Rollout strategy is defined
- [ ] Canary deployment is planned
- [ ] Rollback procedure is documented
- [ ] Feature flags are used appropriately

### Testing
- [ ] Unit tests are planned
- [ ] Integration tests are planned
- [ ] Load tests are planned
- [ ] Chaos tests are considered

### Feature Flags
- [ ] Feature flags are used for risky changes
- [ ] Kill switches are implemented
- [ ] Flag management is documented

---

## Security

### Identity & Authentication
- [ ] Authentication is required
- [ ] Authentication mechanism is appropriate
- [ ] Identity is verified correctly

### Authorization
- [ ] Authorization is checked
- [ ] Principle of least privilege is followed
- [ ] Permissions are well-defined
- [ ] Access is audited

### Data Protection
- [ ] Data is encrypted at rest
- [ ] Data is encrypted in transit
- [ ] Key management is secure
- [ ] Data exfiltration is prevented

### Attack Surfaces
- [ ] Attack vectors are identified
- [ ] Mitigations are in place
- [ ] Security monitoring is planned

---

## Capacity & Performance

### Capacity Planning
- [ ] Capacity requirements are calculated
- [ ] Scaling strategy is defined
- [ ] Scaling limits are understood
- [ ] Capacity forecasting is planned

### Performance
- [ ] Performance targets are met
- [ ] Bottlenecks are identified
- [ ] Optimization opportunities are considered
- [ ] Tail latency is addressed

### Cost
- [ ] Cost model is understood
- [ ] Cost optimization is considered
- [ ] Cost monitoring is planned

---

## Operational Readiness

### Documentation
- [ ] Architecture is documented
- [ ] Runbooks are written
- [ ] Onboarding docs exist
- [ ] Troubleshooting guides exist

### On-Call
- [ ] On-call rotation is defined
- [ ] Escalation paths are clear
- [ ] Incident response is planned
- [ ] Postmortem process is defined

### Monitoring
- [ ] Dashboards are created
- [ ] Alerts are configured
- [ ] Monitoring is tested
- [ ] Debugging tools are available

---

## Staff-Level Questions

### Design Questions
- [ ] What's the failure domain?
- [ ] How do we detect failures?
- [ ] What's the blast radius?
- [ ] How do we roll back?
- [ ] What's the observability contract?

### Scale Questions
- [ ] What happens at 10× load?
- [ ] What are the bottlenecks?
- [ ] How does it degrade?

### Security Questions
- [ ] Who can access this?
- [ ] How is data protected?
- [ ] What's the attack surface?

### Operational Questions
- [ ] How do we monitor this?
- [ ] What's the runbook?
- [ ] How do we debug issues?

---

## Review Feedback

### Critical Issues (Must Fix)
1. [Issue 1]
2. [Issue 2]

### Important Issues (Should Fix)
1. [Issue 1]
2. [Issue 2]

### Nice-to-Have (Consider)
1. [Issue 1]
2. [Issue 2]

### Questions
1. [Question 1]
2. [Question 2]

---

## Approval

- [ ] **Approved** - Design is ready for implementation
- [ ] **Approved with Changes** - Design is approved pending fixes
- [ ] **Needs Revision** - Design needs significant changes
- [ ] **Rejected** - Design is not viable

**Reviewer Signature**: [Name]

**Date**: [Date]

**Next Steps**: [What happens next?]

