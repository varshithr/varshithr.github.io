# Further Reading: SLIs, SLOs & Error Budgets

[Back to SLIs/SLOs](../04-reliability-sre/sli-slo-error-budget.md)

---

## Site Reliability Engineering (Google SRE Book)

**Book**: [Site Reliability Engineering: How Google Runs Production Systems](https://sre.google/books/)

**Why it matters**: The definitive guide to SRE practices, including the original explanation of SLIs, SLOs, and error budgets.

### Key Concepts

**SLIs (Service Level Indicators)**:
- What to measure
- How to measure it
- User-facing vs internal metrics

**SLOs (Service Level Objectives)**:
- How to set targets
- What targets are realistic
- How to communicate SLOs

**Error Budgets**:
- How to calculate error budgets
- How to use error budgets
- Error budget policies

**Relevance**: Provides the foundational concepts and real-world examples from Google.

### Recommended Chapters

- **Chapter 4: Service Level Objectives**: Comprehensive SLO guide
- **Chapter 5: Eliminating Toil**: Using error budgets to reduce toil
- **Chapter 6: Monitoring Distributed Systems**: How to measure SLIs

### Key Excerpts

**On SLIs**:

> "SLIs should measure what users care about, not what's easy to measure. Internal metrics like CPU utilization don't reflect user experience."

**Key insight**: SLIs must be user-facing. Internal metrics don't tell you if users are happy.

**On SLOs**:

> "SLOs should be achievable but not too easy. They should reflect user needs and business requirements, not just current performance."

**Relevance**: Explains how to set appropriate SLOs that balance user needs with feasibility.

**On Error Budgets**:

> "Error budgets balance reliability and velocity. When error budget is exhausted, stop feature work and focus on reliability."

**Key insight**: Error budgets provide a data-driven way to balance feature development and reliability work.

---

## The Site Reliability Workbook

**Book**: [The Site Reliability Workbook: Practical Ways to Implement SRE](https://sre.google/workbook/)

**Why it matters**: Practical guide to implementing SRE practices, including detailed SLI/SLO examples.

### Key Concepts

**Implementing SLIs**:
- Step-by-step process
- Common pitfalls
- Real-world examples

**Setting SLOs**:
- How to choose targets
- How to validate targets
- How to adjust SLOs

**Using Error Budgets**:
- Error budget policies
- How to track error budgets
- How to respond to budget exhaustion

**Relevance**: Provides practical, actionable guidance for implementing SLIs/SLOs.

### Recommended Chapters

- **Chapter 2: Implementing SLOs**: Practical implementation guide
- **Chapter 3: SLO Engineering Case Studies**: Real-world examples
- **Chapter 4: Error Budgets**: Error budget policies and practices

---

## SLI/SLO Best Practices

### Google Cloud Documentation

**Documentation**: [SLI/SLO Best Practices](https://cloud.google.com/architecture/framework/reliability/service-level-objectives)

**Why it matters**: GCP's recommended practices for defining and using SLIs/SLOs.

### Key Practices

**1. Start Simple**
- Begin with availability and latency
- Add more SLIs as needed
- Don't over-engineer initially

**2. Measure What Matters**
- User-facing metrics
- Business-critical operations
- Not internal implementation details

**3. Set Realistic Targets**
- Based on baseline performance
- Account for improvement over time
- Balance user needs and feasibility

**4. Use Error Budgets**
- Calculate error budgets from SLOs
- Define error budget policies
- Track and monitor error budgets

**Relevance**: Provides concrete best practices for implementing SLIs/SLOs.

---

## Error Budget Policies

### Example Policies

**Google's Approach**:
- **> 50% remaining**: Normal operations
- **25-50% remaining**: Reduce risky changes
- **< 25% remaining**: Stop feature work
- **0% remaining**: Emergency reliability only

**Why it works**:
- Gradual escalation
- Clear thresholds
- Data-driven decisions

**Relevance**: Provides a concrete example of error budget policy implementation.

---

## Additional Resources

### Papers

**"Site Reliability Engineering"** (Google SRE Book)
- Original SLO concepts
- [Link](https://sre.google/books/)

**"The Site Reliability Workbook"** (Google SRE Workbook)
- Practical implementation guide
- [Link](https://sre.google/workbook/)

### Books

**"Implementing Service Level Objectives"** by Alex Hidalgo
- Comprehensive SLO guide
- Practical examples

### Online Resources

**Google Cloud Documentation**: [SLO Documentation](https://cloud.google.com/monitoring/api/v3/slo)
- GCP SLO implementation
- API and tools

**SRE Book**: [sre.google](https://sre.google/)
- Free online version
- All chapters available

---

## Key Takeaways

1. **SLIs measure user experience**: User-facing metrics, not internal metrics
2. **SLOs balance needs and feasibility**: Realistic but not too easy
3. **Error budgets enable velocity**: Data-driven balance between features and reliability
4. **Start simple**: Begin with availability and latency, expand as needed
5. **Monitor and adjust**: SLOs should evolve with system and user needs

---

## Related Topics

- [PRR Checklist](../04-reliability-sre/prr-checklist.md) - Using SLOs in production readiness
- [Observability Basics](../01-foundations/observability-basics.md) - How to measure SLIs
- [Capacity Planning](../04-reliability-sre/capacity-planning.md) - Capacity and SLOs

