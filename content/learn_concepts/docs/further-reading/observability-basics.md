# Further Reading: Observability Basics

[Back to Observability Basics](../01-foundations/observability-basics.md)

---

## Observability Engineering

**Book**: [Observability Engineering](https://www.oreilly.com/library/view/observability-engineering/9781492076438/)

**Why it matters**: Comprehensive guide to observability, covering metrics, logs, and traces in depth.

### Key Concepts

**Three Pillars**:
- Metrics: What is happening
- Logs: What happened
- Traces: How it happened

**Observability vs Monitoring**:
- Monitoring: Pre-defined metrics (you know what to look for)
- Observability: Ability to ask new questions (you don't know what to look for)

**Relevance**: Provides the theoretical foundation and practical techniques for observability.

### Recommended Chapters

- **Chapter 1: Introduction**: What is observability
- **Chapter 2: Metrics**: Metrics best practices
- **Chapter 3: Logs**: Logging best practices
- **Chapter 4: Traces**: Distributed tracing

---

## Distributed Tracing

### OpenTelemetry

**Documentation**: [OpenTelemetry](https://opentelemetry.io/)

**Why it matters**: Industry standard for observability, including distributed tracing.

### Key Concepts

**Tracing**:
- Spans and traces
- Context propagation
- Sampling strategies

**Instrumentation**:
- Automatic instrumentation
- Manual instrumentation
- Best practices

**Relevance**: Provides the standard approach to distributed tracing.

---

## Prometheus Monitoring

**Documentation**: [Prometheus](https://prometheus.io/docs/)

**Why it matters**: Popular open-source monitoring system, widely used for metrics.

### Key Concepts

**Metrics**:
- Counters, gauges, histograms
- PromQL query language
- Alerting rules

**Best Practices**:
- Metric naming conventions
- Label cardinality
- Recording rules

**Relevance**: Provides practical guidance for metrics collection and querying.

---

## Structured Logging

### The Twelve-Factor App

**Article**: [The Twelve-Factor App: Logs](https://12factor.net/logs)

**Why it matters**: Best practices for logging in modern applications.

### Key Concepts

**Structured Logging**:
- Logs as event streams
- Structured format (JSON)
- Context and correlation

**Relevance**: Provides the philosophy and best practices for logging.

---

## Additional Resources

### Books

**"Observability Engineering"** by Charity Majors et al.
- Comprehensive observability guide
- Practical examples

**"Systems Performance"** by Brendan Gregg
- Performance analysis
- Tools and techniques

### Online Resources

**Google Cloud Operations Suite**: [Documentation](https://cloud.google.com/products/operations)
- GCP observability tools
- Best practices

**Datadog**: [Observability Guide](https://www.datadoghq.com/knowledge-center/observability/)
- Observability concepts
- Best practices

---

## Key Takeaways

1. **Three pillars**: Metrics, logs, and traces work together
2. **User-facing metrics**: Measure what users experience
3. **Structured logs**: JSON format with context
4. **Distributed tracing**: Understand request flow
5. **Observability contract**: Define what to measure

---

## Related Topics

- [SLIs/SLOs](../04-reliability-sre/sli-slo-error-budget.md) - What to measure for SLOs
- [Queueing Theory](../01-foundations/queueing-tail-latency.md) - Latency metrics
- [Capacity Math](../01-foundations/capacity-math.md) - Resource metrics

