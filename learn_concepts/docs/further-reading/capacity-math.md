# Further Reading: Capacity Math

[Back to Capacity Math](../01-foundations/capacity-math.md)

---

## Systems Performance (Brendan Gregg)

**Book**: [Systems Performance: Enterprise and the Cloud](https://www.brendangregg.com/sysperfbook.html)

**Why it matters**: Comprehensive guide to capacity planning and performance analysis, with practical formulas and methodologies.

### Key Concepts

**Capacity Planning**:
- How to measure current capacity
- How to forecast future needs
- How to identify bottlenecks

**Resource Analysis**:
- CPU capacity calculations
- Memory capacity calculations
- Disk I/O capacity calculations
- Network capacity calculations

**Relevance**: Provides the mathematical foundation and practical tools for capacity planning.

### Recommended Chapters

- **Chapter 2: Methodologies**: Capacity planning methodologies
- **Chapter 6: CPUs**: CPU capacity and utilization
- **Chapter 7: Memory**: Memory capacity planning
- **Chapter 8: File Systems**: Disk I/O capacity

---

## The Datacenter as a Computer (Barroso & Hölzle, 2018)

**Book**: [The Datacenter as a Computer: Designing Warehouse-Scale Machines](https://research.google/pubs/pub35290/)

**Why it matters**: Explains capacity planning at Google scale, including how to think about resource utilization and efficiency.

### Key Excerpts

**On capacity planning**:

> "Capacity planning requires understanding both current utilization and future growth. We need to plan for peak loads, not just average loads, and account for growth over time."

**Key insight**: Capacity planning must account for:
1. Current peak load (not average)
2. Growth projections
3. Safety margins
4. Failure scenarios (fewer resources available)

**On resource efficiency**:

> "Efficiency comes from right-sizing resources, not over-provisioning. We need to understand actual usage patterns, not theoretical maximums."

**Relevance**: Emphasizes the importance of measuring actual usage and right-sizing, rather than over-provisioning.

---

## Capacity Planning Best Practices

### 1. Measure Baseline

**Critical step**: Before planning capacity, measure current usage.

**What to measure**:
- **Peak usage**: Maximum resource usage, not average
- **Usage patterns**: How usage varies over time (daily, weekly, seasonal)
- **Growth trends**: How usage is changing over time

**Tools**:
- Monitoring systems (Prometheus, Cloud Monitoring)
- Resource utilization dashboards
- Historical data analysis

### 2. Forecast Growth

**Methods**:
- **Linear growth**: Simple percentage increase
- **Exponential growth**: Compound growth (more realistic)
- **Seasonal patterns**: Account for seasonal variations
- **Event-driven**: Account for known events (product launches, marketing campaigns)

**Example**:
- Current: 1,000 QPS
- Growth: 15% per month
- 12 months: 1,000 × (1.15)^12 = 5,350 QPS

### 3. Add Safety Margins

**Why**: 
- Traffic spikes
- Growth uncertainty
- Failure scenarios
- Maintenance windows

**Typical margins**:
- **CPU**: 20-30% headroom (70-80% utilization)
- **Memory**: 20% headroom
- **Disk**: 20-30% headroom
- **Network**: 30-50% headroom (for bursts)

### 4. Plan for Failures

**Failure scenarios**:
- Single instance failure: Need redundancy
- Region failure: Need multi-region capacity
- Database failure: Need read replicas

**Capacity during failures**:
- Plan for N-1 capacity (one instance down)
- Or N-2 capacity (two instances down)
- Depends on availability requirements

---

## Resource-Specific Capacity Planning

### CPU Capacity

**Key formula**: `CPU Cores = (QPS × CPU Time Per Request) / Target Utilization`

**Considerations**:
- **Single-threaded vs multi-threaded**: Multi-threaded can use more cores
- **CPU-bound vs I/O-bound**: I/O-bound may need more cores for concurrency
- **Context switching**: Too many threads can hurt performance
- **NUMA**: Non-uniform memory access affects performance

**Best practices**:
- Measure actual CPU time per request
- Account for context switching overhead
- Use appropriate target utilization (70-80%)

### Memory Capacity

**Key formula**: `Memory = (Concurrent Requests × Memory Per Request) + Base Memory + Cache`

**Considerations**:
- **Peak vs average**: Use peak memory, not average
- **Garbage collection**: GC overhead in managed languages
- **Memory leaks**: Monitor for gradual memory growth
- **Swap**: Avoid swap for performance-critical systems

**Best practices**:
- Measure peak memory per request
- Account for GC overhead
- Monitor for memory leaks
- Size cache appropriately

### Disk Capacity

**Key formulas**:
- **Storage**: `Disk = Data Volume + Logs + Temporary Files + Safety Margin`
- **I/O**: `IOPS Needed = QPS × I/O Operations Per Request`

**Considerations**:
- **SSD vs HDD**: SSD has much higher IOPS
- **Random vs sequential**: Random I/O is slower
- **Read vs write**: Writes are often slower

**Best practices**:
- Use SSD for performance-critical workloads
- Optimize for sequential I/O when possible
- Separate read and write workloads

### Network Capacity

**Key formula**: `Bandwidth = QPS × (Request Size + Response Size)`

**Considerations**:
- **Bidirectional**: Both ingress and egress matter
- **Peak vs average**: Plan for peak traffic
- **Compression**: Can reduce bandwidth needs
- **CDN**: Reduces egress bandwidth

**Best practices**:
- Plan for peak traffic, not average
- Use compression when possible
- Use CDN for static content
- Monitor both ingress and egress

---

## Additional Resources

### Papers

**"The Tail at Scale"** (Dean & Barroso, 2013)
- How tail latency affects capacity planning
- [Link](https://research.google/pubs/pub40801/)

**"The Datacenter as a Computer"** (Barroso & Hölzle, 2018)
- Capacity planning at scale
- [Link](https://research.google/pubs/pub35290/)

### Books

**"Systems Performance"** by Brendan Gregg
- Comprehensive capacity planning guide
- Practical formulas and tools

**"Designing Data-Intensive Applications"** by Martin Kleppmann
- Chapter on scalability
- Capacity planning for distributed systems

### Online Resources

**Google SRE Book**: [Site Reliability Engineering](https://sre.google/books/)
- Chapter on capacity planning
- Real-world examples

**AWS Well-Architected Framework**: [Capacity Planning](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/capacity-planning.html)
- Capacity planning best practices
- Applicable to GCP as well

---

## Key Takeaways

1. **Measure baseline**: Understand current usage before planning
2. **Forecast growth**: Account for future growth (exponential, not linear)
3. **Add margins**: Safety margins for spikes and failures
4. **Plan for failures**: Capacity during failure scenarios
5. **Right-size**: Don't over-provision, but don't under-provision either

---

## Related Topics

- [Queueing Theory & Tail Latency](../01-foundations/queueing-tail-latency.md) - How queueing affects capacity
- [Observability Basics](../01-foundations/observability-basics.md) - How to measure capacity
- [Capacity Planning](../04-reliability-sre/capacity-planning.md) - SRE perspective on capacity

