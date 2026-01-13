# Answer Key: PRR Checklist

[Back to Exercises](../../04-reliability-sre/prr-checklist.md#exercises)

---

## Exercise 1: Run a PRR

**Question**: Review a system design using this checklist. What issues do you find?

### Answer

**System**: API service with database, cache, and external API dependencies

### PRR Review Findings

**Critical Issues (Must Fix)**:

1. **No SLIs/SLOs Defined**
   - **Issue**: No service level indicators or objectives defined
   - **Impact**: Can't measure reliability, can't set error budgets
   - **Fix**: Define SLIs (availability, latency, error rate) and SLOs (targets)

2. **No Monitoring**
   - **Issue**: No metrics, logs, or traces configured
   - **Impact**: Can't detect problems, can't debug issues
   - **Fix**: Set up metrics (latency, throughput, errors), logs (structured), traces (critical paths)

3. **No On-Call**
   - **Issue**: No on-call rotation or procedures
   - **Impact**: Can't respond to incidents
   - **Fix**: Set up on-call rotation, define escalation paths, create runbooks

4. **No Rollback Plan**
   - **Issue**: No rollback procedure documented or tested
   - **Impact**: Can't recover from bad deployments
   - **Fix**: Document rollback procedure, test rollback, automate if possible

5. **No Security**
   - **Issue**: No authentication, authorization, or encryption
   - **Impact**: Vulnerable to attacks, data breaches
   - **Fix**: Add authentication (OAuth/JWT), authorization (IAM), encryption (TLS, at rest)

**Important Issues (Should Fix)**:

1. **Weak SLIs**
   - **Issue**: Using internal metrics (CPU, memory) instead of user-facing metrics
   - **Impact**: SLIs don't reflect user experience
   - **Fix**: Use user-facing metrics (availability, latency, error rate)

2. **Alert Fatigue**
   - **Issue**: Too many alerts, not actionable
   - **Impact**: Alerts ignored, real issues missed
   - **Fix**: Reduce alerts, make alerts actionable, set appropriate thresholds

3. **No Runbooks**
   - **Issue**: No runbooks for common operations or incidents
   - **Impact**: Don't know how to respond to issues
   - **Fix**: Create runbooks for common incidents, test runbooks

4. **No Load Testing**
   - **Issue**: System not load tested
   - **Impact**: Don't know capacity limits, may fail under load
   - **Fix**: Run load tests, test at 2× expected load, identify bottlenecks

5. **Weak Security**
   - **Issue**: Security gaps (no encryption, weak authentication)
   - **Impact**: Security vulnerabilities
   - **Fix**: Add encryption, strengthen authentication, add authorization

**Nice-to-Have (Consider)**:

1. **No Tracing**
   - **Issue**: No distributed tracing
   - **Impact**: Harder to debug performance issues
   - **Fix**: Add tracing for critical paths

2. **No Chaos Testing**
   - **Issue**: No chaos engineering
   - **Impact**: Don't know how system handles failures
   - **Fix**: Add chaos tests, test failure scenarios

3. **No Capacity Planning**
   - **Issue**: No capacity planning or forecasting
   - **Impact**: May run out of capacity unexpectedly
   - **Fix**: Plan capacity, forecast growth, monitor capacity

### Answer

**Critical Issues** (Must Fix):
1. No SLIs/SLOs defined
2. No monitoring configured
3. No on-call rotation
4. No rollback plan
5. No security (authentication, authorization, encryption)

**Important Issues** (Should Fix):
1. Weak SLIs (using internal metrics)
2. Alert fatigue (too many non-actionable alerts)
3. No runbooks
4. No load testing
5. Weak security

**Nice-to-Have** (Consider):
1. No tracing
2. No chaos testing
3. No capacity planning

**Top Priority**: Fix critical issues first (SLIs/SLOs, monitoring, on-call, rollback, security)

---

## Exercise 2: Fix PRR Issues

**Question**: A system fails PRR. What are the top 3 issues to fix?

### Answer

**System**: Failed PRR review

### Top 3 Issues to Fix

**1. Define SLIs and SLOs** (Highest Priority)

**Why**: Foundation for everything else
- Can't measure reliability without SLIs
- Can't set error budgets without SLOs
- Can't make data-driven decisions

**How**:
1. Define user-facing SLIs (availability, latency, error rate)
2. Set realistic SLOs based on baseline
3. Calculate error budgets
4. Set up monitoring to measure SLIs
5. Create SLO dashboard

**Timeline**: 1-2 weeks

**2. Set Up Monitoring** (High Priority)

**Why**: Can't detect or debug problems without monitoring
- Need metrics to measure SLIs
- Need logs to debug issues
- Need traces to identify bottlenecks

**How**:
1. Set up metrics (latency, throughput, errors, resources)
2. Configure structured logging
3. Set up distributed tracing (if applicable)
4. Create dashboards
5. Configure alerts

**Timeline**: 1-2 weeks

**3. Set Up On-Call and Runbooks** (High Priority)

**Why**: Can't respond to incidents without on-call
- Need on-call to respond to alerts
- Need runbooks to know how to respond
- Need escalation paths for critical issues

**How**:
1. Set up on-call rotation
2. Create runbooks for common incidents
3. Define escalation paths
4. Set up alerting (PagerDuty, etc.)
5. Train on-call engineers

**Timeline**: 1 week

### Why These Three?

**SLIs/SLOs**: Foundation - everything else depends on this
**Monitoring**: Detection - can't fix what you can't see
**On-Call**: Response - can't fix what you can't respond to

**Order**: Fix in this order (SLIs/SLOs → Monitoring → On-Call)

### Answer

**Top 3 Issues to Fix**:

1. **Define SLIs and SLOs** (Highest Priority)
   - Foundation for reliability
   - Define user-facing metrics and targets
   - Set up error budgets
   - Timeline: 1-2 weeks

2. **Set Up Monitoring** (High Priority)
   - Can't detect problems without monitoring
   - Set up metrics, logs, traces
   - Create dashboards and alerts
   - Timeline: 1-2 weeks

3. **Set Up On-Call and Runbooks** (High Priority)
   - Can't respond to incidents without on-call
   - Create runbooks for common incidents
   - Set up escalation paths
   - Timeline: 1 week

**Why these three**: SLIs/SLOs are foundation, monitoring enables detection, on-call enables response.

**Order**: Fix in this order for maximum impact.

---

## Exercise 3: Design for PRR

**Question**: Design a system that passes PRR. What do you include?

### Answer

**Goal**: Design system that passes PRR on first review

### PRR-Ready System Design

**1. SLIs, SLOs & Error Budgets**

**SLIs**:
- Availability: Fraction of successful requests
- Latency: P50, P95, P99 request latency
- Error rate: Fraction of 5xx errors

**SLOs**:
- Availability: 99.9%
- P95 Latency: < 100ms
- P99 Latency: < 200ms
- Error rate: < 0.1%

**Error Budgets**:
- Calculated from SLOs
- Policy defined (what happens at 50%, 25%, 0%)
- Tracked and monitored

**2. Observability**

**Metrics**:
- Latency: P50, P95, P99 tracked
- Throughput: QPS tracked
- Errors: Error rates and types tracked
- Resources: CPU, memory, disk, network tracked
- Business: User-facing metrics tracked

**Logs**:
- Structured JSON logs
- Request IDs for correlation
- Critical events logged
- Appropriate log levels

**Traces**:
- Critical paths traced
- 1% sampling (100% for errors)
- Spans for key operations

**Dashboards**:
- Service dashboard
- SLO dashboard
- Capacity dashboard
- Business dashboard

**Alerts**:
- Critical alerts (P0)
- Warning alerts (P1)
- Info alerts (P2)
- Actionable alerts with runbooks

**3. Incident Response**

**On-Call**:
- On-call rotation established
- Engineers trained
- Procedures documented
- Tools available
- Escalation paths clear

**Runbooks**:
- Common incidents documented
- Critical failures documented
- Recovery procedures included
- Rollback procedures included
- Tested and accessible

**Incident Management**:
- Process defined
- Communication channels established
- Postmortem process defined
- Tracking system used

**4. Capacity & Scaling**

**Capacity Planning**:
- Current capacity known
- Target capacity provisioned
- Growth forecast planned
- Scaling limits understood
- Capacity alerts configured

**Auto-Scaling**:
- Configured and tuned
- Scaling limits set
- Metrics appropriate
- Behavior tested

**Load Testing**:
- Tests run
- Handles expected load
- Handles 2× load
- Graceful degradation tested
- Bottlenecks identified

**5. Security**

**Authentication**:
- Required for all access
- Appropriate mechanism
- Tested
- Failures logged

**Authorization**:
- Checked for all operations
- Least privilege followed
- Documented
- Audited
- Failures logged

**Data Protection**:
- Encrypted at rest
- Encrypted in transit (TLS)
- Keys managed securely
- Data classified
- Retention policies defined

**6. Change Management**

**Deployment**:
- Process documented
- Automated
- Rollback tested
- Windows defined
- Approvals defined

**Feature Flags**:
- Used for risky changes
- Kill switches implemented
- Management documented
- Tested

**Testing**:
- Unit tests adequate
- Integration tests exist
- Load tests run regularly
- Chaos tests considered
- Smoke tests after deployment

### Complete PRR-Ready Checklist

**Must Have**:
- ✅ SLIs and SLOs defined
- ✅ Error budgets calculated
- ✅ Monitoring configured (metrics, logs, traces)
- ✅ Dashboards created
- ✅ Alerts configured
- ✅ On-call rotation established
- ✅ Runbooks created
- ✅ Rollback procedure tested
- ✅ Authentication and authorization
- ✅ Encryption (at rest and in transit)
- ✅ Load testing completed
- ✅ Capacity planning done

**Should Have**:
- ✅ Distributed tracing
- ✅ Chaos testing
- ✅ Feature flags
- ✅ Canary deployments
- ✅ Security monitoring

### Answer

**PRR-Ready System Includes**:

**1. SLIs/SLOs**:
- User-facing SLIs defined
- Realistic SLOs set
- Error budgets calculated and tracked

**2. Observability**:
- Metrics (latency, throughput, errors, resources)
- Structured logs with request IDs
- Distributed tracing
- Dashboards and alerts

**3. Incident Response**:
- On-call rotation
- Runbooks for common incidents
- Escalation paths
- Postmortem process

**4. Capacity**:
- Capacity planning
- Auto-scaling configured
- Load testing completed

**5. Security**:
- Authentication and authorization
- Encryption (at rest and in transit)
- Security monitoring

**6. Change Management**:
- Deployment automation
- Rollback procedure
- Feature flags
- Testing strategy

**Key principle**: **Production-ready from day one** - design with operations in mind.

