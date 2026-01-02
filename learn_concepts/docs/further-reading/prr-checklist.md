# Further Reading: PRR Checklist

[Back to PRR Checklist](../04-reliability-sre/prr-checklist.md)

---

## Site Reliability Engineering (Google SRE Book)

**Book**: [Site Reliability Engineering: How Google Runs Production Systems](https://sre.google/books/)

**Why it matters**: Google's approach to production readiness, including what makes systems production-ready.

### Key Concepts

**Production Readiness**:
- What makes a system production-ready
- How to evaluate production readiness
- Common production readiness failures

**Checklists**:
- What to check before production
- How to verify readiness
- When to approve for production

**Relevance**: Provides the foundation for PRR practices and what Google considers production-ready.

### Recommended Chapters

- **Chapter 4: Service Level Objectives**: SLOs and production readiness
- **Chapter 6: Monitoring Distributed Systems**: Observability requirements
- **Chapter 10: Practical Alerting**: Alerting best practices
- **Chapter 11: On-Call**: On-call requirements

---

## The Site Reliability Workbook

**Book**: [The Site Reliability Workbook: Practical Ways to Implement SRE](https://sre.google/workbook/)

**Why it matters**: Practical guide to implementing PRR practices with detailed checklists and examples.

### Key Concepts

**PRR Process**:
- How to run a PRR
- What to check
- How to document findings

**Common Issues**:
- What typically fails PRR
- How to fix common issues
- How to prevent issues

**Relevance**: Provides practical, actionable guidance for running PRRs.

### Recommended Chapters

- **Chapter 2: Implementing SLOs**: SLO requirements for PRR
- **Chapter 4: Error Budgets**: Error budget requirements
- **Chapter 5: Alerting on SLOs**: Alerting requirements
- **Chapter 6: On-Call**: On-call requirements

---

## Google Cloud Production Readiness

**Documentation**: [Production Readiness Review](https://cloud.google.com/architecture/framework/reliability/production-readiness)

**Why it matters**: GCP's recommended practices for production readiness reviews.

### Key Areas

**1. Reliability**
- SLIs and SLOs defined
- Error budgets calculated
- Monitoring configured

**2. Observability**
- Metrics, logs, traces
- Dashboards created
- Alerts configured

**3. Security**
- Authentication and authorization
- Encryption configured
- Security monitoring

**4. Operations**
- On-call rotation
- Runbooks created
- Incident response process

**Relevance**: Provides GCP-specific guidance for production readiness.

---

## PRR Best Practices

### What Staff Engineers Look For

**Critical (Must Fix)**:
1. No SLIs/SLOs defined
2. No monitoring configured
3. No on-call rotation
4. No rollback plan
5. No security (auth, encryption)

**Important (Should Fix)**:
1. Weak SLIs (internal metrics)
2. Alert fatigue
3. No runbooks
4. No load testing
5. Weak security

**Nice-to-Have**:
1. Distributed tracing
2. Chaos testing
3. Capacity planning

**Relevance**: Provides a prioritized checklist of what matters most.

---

## Additional Resources

### Books

**"The Site Reliability Workbook"** (Google SRE Workbook)
- Practical PRR implementation
- Real-world examples

**"Release It!"** by Michael Nygard
- Production readiness patterns
- Common production failures

### Online Resources

**Google Cloud Documentation**: [Production Readiness](https://cloud.google.com/architecture/framework/reliability/production-readiness)
- GCP production readiness guide
- Checklists and best practices

**SRE Book**: [sre.google](https://sre.google/)
- Free online version
- PRR concepts and practices

---

## Key Takeaways

1. **PRR ensures readiness**: Don't skip production readiness reviews
2. **Focus on critical issues**: SLIs/SLOs, monitoring, on-call, rollback, security
3. **Use checklists**: Systematic approach to PRR
4. **Document findings**: Clear feedback and action items
5. **Iterate**: PRR is not one-time, systems evolve

---

## Related Topics

- [SLIs/SLOs](../04-reliability-sre/sli-slo-error-budget.md) - Foundation for PRR
- [Observability Basics](../01-foundations/observability-basics.md) - Monitoring requirements
- [Incident Response](../04-reliability-sre/incident-response.md) - On-call and runbooks

