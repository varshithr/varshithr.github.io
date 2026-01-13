# Further Reading: Sharding & Partitioning

[Back to Sharding & Partitioning](../02-distributed-systems/sharding-partitioning.md)

---

## Research Papers

**"Scalable Web Architecture and Distributed Systems"** (Barroso & Hölzle)
- Sharding and partitioning patterns

---

## Additional Resources

### Books

**"Designing Data-Intensive Applications"** by Martin Kleppmann
- Chapter on partitioning
- Sharding strategies

---

## Key Takeaways

1. **Range partitioning**: Supports range queries, may have hot spots
2. **Hash partitioning**: Even distribution, no range queries
3. **Consistent hashing**: Minimal rebalancing
4. **Hot spots**: Design keys to avoid hot spots

---

## Related Topics

- [Bigtable: Design & Tradeoffs](../03-gcp-core-building-blocks/bigtable.md) - Key design in Bigtable
- [BigQuery Architecture](../03-gcp-core-building-blocks/bigquery.md) - Partitioning in BigQuery
- [Back to Distributed Systems](../02-distributed-systems/README.md)

