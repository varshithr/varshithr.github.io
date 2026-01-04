# Further Reading: Spanner

[Back to Spanner: Consistency & Performance](../03-gcp-core-building-blocks/spanner.md)

---

## Spanner Documentation

**Official Documentation**: [Google Cloud Spanner Documentation](https://cloud.google.com/spanner/docs)

**Why it matters**: Comprehensive official documentation on Spanner architecture, features, and best practices.

### Key Concepts

**Spanner Architecture**:
- TrueTime and external consistency
- Distributed transactions
- Multi-region replication

**Schema Design**:
- Tables and indexes
- Interleaving
- Secondary indexes

**Relevance**: Provides the authoritative reference for Spanner implementation details.

### Recommended Sections

- **Spanner Overview**: Understanding Spanner concepts
- **TrueTime**: How TrueTime enables external consistency
- **Schema Design**: Best practices for schema design
- **Performance**: Optimizing query performance
- **Multi-Region**: Multi-region deployment patterns

---

## Spanner Research Papers

**"Spanner: Google's Globally-Distributed Database"** (Corbett et al., 2012)
- Original Spanner paper
- [Link](https://research.google/pubs/pub39966/)

**Why it matters**: Deep dive into Spanner's architecture and design principles.

### Key Topics

**TrueTime**:
- Distributed clock synchronization
- External consistency guarantees
- Performance implications

**Distributed Transactions**:
- Two-phase commit
- Paxos consensus
- Transaction performance

**Relevance**: Understanding the research behind Spanner's design.

---

## Google Cloud Architecture Center

**Resource**: [Google Cloud Architecture Center](https://cloud.google.com/architecture)

**Why it matters**: Reference architectures and best practices for Spanner deployments.

### Key Resources

**Database Patterns**:
- Multi-region database deployments
- Schema design patterns
- Performance optimization

**Consistency Patterns**:
- External consistency use cases
- Transaction design patterns
- Replication strategies

**Relevance**: Provides real-world architecture examples and best practices.

---

## Additional Resources

### Papers

**"Spanner, TrueTime and The CAP Theorem"** (Google Research)
- CAP theorem analysis
- [Link](https://research.google/pubs/pub45855/)

**"The Datacenter as a Computer"** (Barroso & Hölzle, 2018)
- Chapter on distributed databases
- [Link](https://research.google/pubs/pub35290/)

### Books

**"Designing Data-Intensive Applications"** by Martin Kleppmann
- Chapter on distributed transactions
- Consistency models and tradeoffs

**"Google Cloud Platform in Action"** by JJ Geewax
- Chapter on Spanner
- Spanner examples and best practices

### Online Resources

**Google Cloud Blog**: [Spanner Articles](https://cloud.google.com/blog/products/databases)
- Latest Spanner features
- Best practices and case studies

**GCP Well-Architected Framework**: [Databases](https://cloud.google.com/architecture/framework/databases)
- Database best practices
- Design principles

---

## Key Takeaways

1. **TrueTime enables external consistency**: Stronger than serializability
2. **Multi-region by default**: Global distribution with strong consistency
3. **Schema design matters**: Interleaving and indexes affect performance
4. **Transactions are expensive**: Design to minimize transaction conflicts
5. **Plan for scale**: Spanner scales to petabytes and millions of QPS

---

## Related Topics

- [Consensus & Leases](../02-distributed-systems/consensus-leases.md) - Consensus algorithms
- [Replication Strategies](../02-distributed-systems/replication.md) - Replication patterns
- [Multi-Region API](../06-case-studies/multi-region-api.md) - Spanner in multi-region architecture

