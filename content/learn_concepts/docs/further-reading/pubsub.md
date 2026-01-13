# Further Reading: Pub/Sub

[Back to Pub/Sub: Delivery Guarantees](../03-gcp-core-building-blocks/pubsub.md)

---

## Pub/Sub Documentation

**Official Documentation**: [Google Cloud Pub/Sub Documentation](https://cloud.google.com/pubsub/docs)

**Why it matters**: Comprehensive official documentation on Pub/Sub architecture, features, and best practices.

### Key Concepts

**Pub/Sub Architecture**:
- Topics and subscriptions
- Message delivery guarantees
- Ordering guarantees

**Reliability**:
- At-least-once delivery
- Dead letter queues
- Retry policies

**Relevance**: Provides the authoritative reference for Pub/Sub implementation details.

### Recommended Sections

- **Pub/Sub Overview**: Understanding Pub/Sub concepts
- **Delivery Guarantees**: At-least-once delivery
- **Ordering**: Ordering guarantees
- **Dead Letter Queues**: Handling failed messages
- **Performance**: Optimizing Pub/Sub performance

---

## Google Cloud Architecture Center

**Resource**: [Google Cloud Architecture Center](https://cloud.google.com/architecture)

**Why it matters**: Reference architectures and best practices for Pub/Sub deployments.

### Key Resources

**Messaging Patterns**:
- Event-driven architectures
- Microservices communication
- Data pipeline patterns

**Reliability Patterns**:
- Idempotency patterns
- Retry strategies
- Dead letter queue handling

**Relevance**: Provides real-world architecture examples and best practices.

---

## Additional Resources

### Books

**"Designing Data-Intensive Applications"** by Martin Kleppmann
- Chapter on messaging systems
- Delivery guarantees and ordering

**"Google Cloud Platform in Action"** by JJ Geewax
- Chapter on Pub/Sub
- Pub/Sub examples and best practices

**"Site Reliability Engineering"** (Google SRE Book)
- Chapter on messaging systems
- Real-world messaging challenges

### Online Resources

**Google Cloud Blog**: [Pub/Sub Articles](https://cloud.google.com/blog/products/data-analytics)
- Latest Pub/Sub features
- Best practices and case studies

**GCP Well-Architected Framework**: [Messaging](https://cloud.google.com/architecture/framework/messaging)
- Messaging best practices
- Design principles

---

## Key Takeaways

1. **At-least-once delivery**: Messages may be duplicated, handle idempotently
2. **Ordering is per-key**: Ordering only within same ordering key
3. **Dead letter queues**: Handle poison messages and failures
4. **Monitor backlog**: Track message backlog and processing rate
5. **Design for scale**: Pub/Sub scales to millions of messages per second

---

## Related Topics

- [Queues & Streams](../02-distributed-systems/queues-streams.md) - Messaging patterns
- [Idempotency & Retries](../02-distributed-systems/idempotency-retries.md) - Handling duplicates
- [Data Pipeline](../06-case-studies/data-pipeline.md) - Pub/Sub in data pipelines

