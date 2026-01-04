# Answer Key: Data Pipeline

[Back to Exercises](../../06-case-studies/data-pipeline.md#exercises)

---

## Exercise 1: Design Improvements

**Question**: How would you improve this design? What tradeoffs?

### Answer

**Potential improvements**:

1. **Add Data Validation Layer**: Separate validation from transformation
2. **Implement Schema Registry**: Centralized schema management
3. **Add Monitoring**: Enhanced monitoring and alerting
4. **Optimize Costs**: Right-size Dataflow workers, optimize BigQuery

**Tradeoffs**:
- More complexity vs better reliability
- Higher cost vs better performance
- More components vs simpler architecture

**Answer**: Add validation layer, implement schema registry, enhance monitoring, optimize costs. Balance complexity vs reliability.

---

## Exercise 2: Handle Schema Evolution

**Question**: How do you handle schema changes without breaking the pipeline?

### Answer

**Schema evolution strategies**:

1. **Schema Registry**: Use schema registry for versioning
2. **Backward Compatibility**: Maintain backward compatibility
3. **Gradual Migration**: Migrate schemas gradually
4. **Version Handling**: Handle multiple schema versions in pipeline

**Answer**: Use schema registry, maintain backward compatibility, migrate gradually, handle multiple versions.

---

## Exercise 3: Optimize Costs

**Question**: How would you reduce costs by 30%? What tradeoffs?

### Answer

**Cost optimization strategies**:

1. **Right-size Workers**: Optimize Dataflow worker count
2. **Optimize BigQuery**: Use partitioning/clustering, reduce data scanned
3. **Use Preemptible Workers**: Use preemptible workers for non-critical workloads
4. **Optimize Pub/Sub**: Reduce message retention, optimize subscriptions

**Tradeoffs**:
- Lower cost vs higher latency
- Less redundancy vs cost savings
- More optimization effort vs cost reduction

**Answer**: Right-size workers, optimize BigQuery, use preemptible workers, optimize Pub/Sub. Balance cost vs performance.

