# Distributed Systems

The building blocks that make distributed systems work: consensus, replication, ordering, and handling overload.

## Overview

Distributed systems are the foundation of modern cloud infrastructure. This chapter covers:
- **Time and ordering**: How to reason about events in distributed systems
- **Consensus**: How nodes agree on values
- **Replication**: Keeping data consistent across nodes
- **Sharding**: Partitioning data for scale
- **Overload**: Handling more load than capacity
- **Idempotency**: Making retries safe
- **Queues and streams**: Asynchronous processing

## Topics

1. [Time, Ordering, and Causality](time-ordering-causality.md)
   - Logical clocks vs physical clocks
   - Causality and happens-before relationships
   - Vector clocks

2. [Consensus & Leases](consensus-leases.md)
   - Paxos and Raft algorithms
   - Leases for distributed locking
   - When to use consensus vs leases

3. [Replication Strategies](replication.md)
   - Synchronous vs asynchronous replication
   - Leader-follower and multi-leader patterns
   - Consistency models

4. [Sharding & Partitioning](sharding-partitioning.md)
   - Horizontal vs vertical partitioning
   - Sharding strategies and tradeoffs
   - Rebalancing and hot spots

5. [Overload & Backpressure](overload-backpressure.md)
   - What happens when load exceeds capacity
   - Backpressure mechanisms
   - Load shedding strategies

6. [Idempotency & Retry Semantics](idempotency-retries.md)
   - Making operations idempotent
   - Retry strategies and exponential backoff
   - Idempotency keys and deduplication

7. [Queues & Streams](queues-streams.md)
   - Message queues vs streams
   - Delivery guarantees (at-least-once, at-most-once, exactly-once)
   - Ordering and partitioning

## Learning Objectives

After completing this chapter, you should be able to:
- Choose between consensus and leases for coordination
- Design replication strategies with appropriate consistency
- Handle overload gracefully with backpressure
- Make systems safe for retries with idempotency
- Choose between queues and streams

## Prerequisites

- [Phase 0: Foundations](../01-foundations/README.md)
- Understanding of basic networking and system design

## Next Steps

- [Phase 2: GCP Core Building Blocks](../03-gcp-core-building-blocks/README.md)
- [Phase 3: LLD Patterns](../05-llD-patterns/README.md)
- [Back to Index](../INDEX.md)

