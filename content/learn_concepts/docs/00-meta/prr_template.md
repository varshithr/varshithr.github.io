# Production Readiness Review (PRR) Template

A PRR ensures a system is ready for production. Use this checklist before launching.

## System Information

**System Name**: [Name]

**Team**: [Team name]

**PRR Date**: [Date]

**PRR Lead**: [Name]

**Reviewers**: [Names]

**Target Launch Date**: [Date]

---

## Overview

**Purpose**: [What does this system do?]

**Users**: [Who uses this system?]

**Scale**: [Expected load, users, data volume]

**Criticality**: [P0/P1/P2 - how critical is this system?]

---

## Reliability & SLOs

### SLIs (Service Level Indicators)
- [ ] **Latency SLI**: [Definition, e.g., "P95 latency of API requests"]
  - Measurement: [How is it measured?]
  - Current value: [Current P95 latency]
  - Target: [Target P95 latency]

- [ ] **Availability SLI**: [Definition, e.g., "Fraction of successful requests"]
  - Measurement: [How is it measured?]
  - Current value: [Current availability]
  - Target: [Target availability]

- [ ] **Error Rate SLI**: [Definition]
  - Measurement: [How is it measured?]
  - Current value: [Current error rate]
  - Target: [Target error rate]

- [ ] **Throughput SLI**: [Definition, if applicable]
  - Measurement: [How is it measured?]
  - Current value: [Current throughput]
  - Target: [Target throughput]

### SLOs (Service Level Objectives)
- [ ] SLOs are defined for all SLIs
- [ ] SLOs are achievable (based on historical data or testing)
- [ ] SLOs are documented
- [ ] SLOs are communicated to stakeholders

### Error Budgets
- [ ] Error budgets are calculated
- [ ] Error budget policy is defined (what happens when budget is exhausted?)
- [ ] Error budget tracking is automated
- [ ] Error budget alerts are configured

### Availability Targets
- [ ] Availability target is appropriate for criticality
- [ ] Availability is measured correctly
- [ ] Planned downtime is accounted for
- [ ] Unplanned downtime is tracked

---

## Monitoring & Observability

### Metrics
- [ ] **Latency metrics**: P50, P95, P99 are tracked
- [ ] **Throughput metrics**: QPS, requests/sec are tracked
- [ ] **Error metrics**: Error rates, error types are tracked
- [ ] **Resource metrics**: CPU, memory, disk, network are tracked
- [ ] **Business metrics**: User-facing metrics are tracked
- [ ] Metrics are exported correctly
- [ ] Metrics retention is configured

### Logging
- [ ] Critical events are logged
- [ ] Log levels are appropriate (INFO, WARN, ERROR)
- [ ] Logs are structured (JSON or structured format)
- [ ] Logs include request IDs for correlation
- [ ] Log retention is configured appropriately
- [ ] Logs are searchable and queryable

### Tracing
- [ ] Critical paths are traced
- [ ] Spans are well-defined
- [ ] Trace sampling is configured
- [ ] Cross-service correlation works
- [ ] Traces are queryable

### Dashboards
- [ ] **Service dashboard**: Shows key metrics, health status
- [ ] **SLO dashboard**: Shows SLO compliance, error budgets
- [ ] **Capacity dashboard**: Shows resource usage, scaling
- [ ] **Business dashboard**: Shows user-facing metrics
- [ ] Dashboards are accessible to on-call
- [ ] Dashboards load quickly

### Alerting
- [ ] **Critical alerts**: P0 incidents (page on-call)
- [ ] **Warning alerts**: P1 incidents (notify, don't page)
- [ ] **Info alerts**: P2 incidents (log only)
- [ ] Alerts are actionable (clear what to do)
- [ ] Alert fatigue is avoided (not too many alerts)
- [ ] Alert thresholds are tuned (not too sensitive/insensitive)
- [ ] Alert runbooks exist
- [ ] Alert escalation paths are defined

---

## Incident Response

### On-Call
- [ ] On-call rotation is established
- [ ] On-call engineers are trained
- [ ] On-call procedures are documented
- [ ] On-call tools are available
- [ ] On-call escalation paths are clear

### Runbooks
- [ ] **Common incidents**: Runbooks exist for common issues
- [ ] **Critical failures**: Runbooks exist for critical failures
- [ ] **Recovery procedures**: Runbooks include recovery steps
- [ ] **Rollback procedures**: Runbooks include rollback steps
- [ ] Runbooks are tested
- [ ] Runbooks are accessible during incidents

### Incident Management
- [ ] Incident response process is defined
- [ ] Incident communication channels are established
- [ ] Postmortem process is defined
- [ ] Incident tracking system is used

### Postmortems
- [ ] Postmortem template is used
- [ ] Postmortems are written for all P0/P1 incidents
- [ ] Postmortems include root cause analysis
- [ ] Postmortems include action items
- [ ] Action items are tracked to completion

---

## Capacity & Scaling

### Capacity Planning
- [ ] **Current capacity**: Current load and capacity are known
- [ ] **Target capacity**: Capacity for launch is provisioned
- [ ] **Growth forecast**: Capacity for growth is planned
- [ ] **Scaling limits**: Maximum scale is understood
- [ ] **Capacity alerts**: Alerts for capacity thresholds

### Auto-Scaling
- [ ] Auto-scaling is configured (if applicable)
- [ ] Scaling policies are tuned
- [ ] Scaling limits are set (min/max instances)
- [ ] Scaling metrics are appropriate
- [ ] Scaling behavior is tested

### Load Testing
- [ ] Load tests have been run
- [ ] System handles expected load
- [ ] System handles 2× expected load
- [ ] System degrades gracefully under overload
- [ ] Bottlenecks are identified and addressed

### Resource Limits
- [ ] CPU limits are set appropriately
- [ ] Memory limits are set appropriately
- [ ] Disk limits are set appropriately
- [ ] Network limits are understood
- [ ] Limits prevent resource exhaustion

---

## Security

### Authentication
- [ ] Authentication is required for all access
- [ ] Authentication mechanism is appropriate
- [ ] Authentication is tested
- [ ] Authentication failures are logged

### Authorization
- [ ] Authorization is checked for all operations
- [ ] Principle of least privilege is followed
- [ ] Permissions are documented
- [ ] Access is audited
- [ ] Authorization failures are logged

### Data Protection
- [ ] **Encryption at rest**: Data is encrypted at rest
- [ ] **Encryption in transit**: Data is encrypted in transit (TLS)
- [ ] **Key management**: Keys are managed securely
- [ ] **Data classification**: Data is classified appropriately
- [ ] **Data retention**: Data retention policies are defined
- [ ] **Data deletion**: Data deletion procedures exist

### Security Monitoring
- [ ] Security events are logged
- [ ] Security alerts are configured
- [ ] Security incidents are tracked
- [ ] Security reviews are conducted

### Compliance
- [ ] Compliance requirements are met (if applicable)
- [ ] Compliance documentation exists
- [ ] Compliance audits are planned

---

## Change Management

### Deployment
- [ ] **Deployment process**: Deployment process is documented
- [ ] **Deployment automation**: Deployments are automated
- [ ] **Deployment rollback**: Rollback procedure is tested
- [ ] **Deployment windows**: Deployment windows are defined
- [ ] **Deployment approvals**: Approval process is defined

### Feature Flags
- [ ] Feature flags are used for risky changes
- [ ] Kill switches are implemented
- [ ] Flag management is documented
- [ ] Flags are tested

### Canary Deployments
- [ ] Canary deployment is used (if applicable)
- [ ] Canary metrics are monitored
- [ ] Canary rollback is tested
- [ ] Canary promotion criteria are defined

### Testing
- [ ] **Unit tests**: Unit test coverage is adequate
- [ ] **Integration tests**: Integration tests exist
- [ ] **Load tests**: Load tests are run regularly
- [ ] **Chaos tests**: Chaos tests are considered
- [ ] **Smoke tests**: Smoke tests run after deployment

---

## Documentation

### Architecture
- [ ] Architecture diagram exists
- [ ] Architecture is documented
- [ ] Data flow is documented
- [ ] Component responsibilities are documented

### Runbooks
- [ ] Runbooks exist for common operations
- [ ] Runbooks are tested
- [ ] Runbooks are accessible

### API Documentation
- [ ] API is documented (if applicable)
- [ ] API examples exist
- [ ] API versioning is documented
- [ ] API deprecation policy exists

### Onboarding
- [ ] Onboarding documentation exists
- [ ] New engineers can get started quickly
- [ ] Development environment setup is documented

---

## Dependencies

### External Dependencies
- [ ] External dependencies are identified
- [ ] Dependency SLAs are understood
- [ ] Dependency failures are handled gracefully
- [ ] Dependency monitoring is in place
- [ ] Dependency runbooks exist

### Internal Dependencies
- [ ] Internal dependencies are identified
- [ ] Dependency contracts are documented
- [ ] Dependency failures are handled gracefully
- [ ] Dependency monitoring is in place

### Dependency Risks
- [ ] Single points of failure are identified
- [ ] Dependency risks are mitigated
- [ ] Fallback mechanisms exist

---

## Cost

### Cost Model
- [ ] Cost per request/user/unit is understood
- [ ] Cost drivers are identified
- [ ] Cost monitoring is in place
- [ ] Cost alerts are configured

### Cost Optimization
- [ ] Cost optimization opportunities are identified
- [ ] Cost optimization is planned
- [ ] Cost budgets are set

---

## Launch Readiness

### Pre-Launch Checklist
- [ ] All PRR items are complete
- [ ] On-call rotation is ready
- [ ] Runbooks are ready
- [ ] Monitoring is configured
- [ ] Alerts are configured
- [ ] Dashboards are ready
- [ ] Documentation is complete
- [ ] Team is trained

### Launch Plan
- [ ] Launch plan is documented
- [ ] Launch steps are defined
- [ ] Launch rollback plan exists
- [ ] Launch communication plan exists
- [ ] Launch date is set

### Post-Launch
- [ ] Post-launch monitoring plan exists
- [ ] Post-launch review is scheduled
- [ ] Post-launch improvements are planned

---

## PRR Decision

- [ ] **Approved** - System is ready for production
- [ ] **Approved with Conditions** - System is approved pending fixes
- [ ] **Not Approved** - System needs significant work

**PRR Lead Signature**: [Name]

**Date**: [Date]

**Next Steps**: [What happens next?]

---

## Notes

[Additional notes, concerns, or recommendations]

