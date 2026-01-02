# Glossary

Definitions of terms used throughout this repository.

## A

**API Gateway**: A service that acts as a single entry point for API requests, handling routing, authentication, rate limiting, and other cross-cutting concerns.

**Availability**: The fraction of time a system is operational and able to serve requests. Usually expressed as a percentage (e.g., 99.9%).

## B

**Backpressure**: A mechanism where a system signals upstream components to slow down when it's overloaded, preventing cascading failures.

**Bigtable**: Google's distributed NoSQL database, designed for low-latency, high-throughput workloads. Used by many Google services internally.

**Blast Radius**: The scope of impact when a component fails. A small blast radius means failures are isolated.

## C

**Canary Deployment**: A deployment strategy where a new version is deployed to a small subset of instances first, monitored, and then gradually rolled out.

**CAP Theorem**: States that a distributed system can guarantee at most two of: Consistency, Availability, Partition tolerance.

**Circuit Breaker**: A pattern that prevents calls to a failing service, allowing it to recover and preventing cascading failures.

**Consensus**: Agreement among distributed nodes on a value or state. Algorithms like Raft and Paxos solve consensus.

**Consistency**: In distributed systems, refers to whether all nodes see the same data at the same time. Can be strong (linearizable) or weak (eventual).

## D

**Distributed System**: A system where components are located on different networked computers and coordinate to achieve a common goal.

**Durability**: The guarantee that once data is written, it will persist even if the system fails.

## E

**Error Budget**: The amount of unreliability a service can tolerate while still meeting its SLO. Calculated as 1 - SLO.

**Eventual Consistency**: A consistency model where, after updates stop, all nodes will eventually converge to the same state, but may temporarily have different values.

## F

**Failure Domain**: A set of components that fail together. Good design minimizes failure domains and limits blast radius.

## G

**GKE (Google Kubernetes Engine)**: Google's managed Kubernetes service, running on GCP.

## I

**IAM (Identity and Access Management)**: System for managing who can access what resources. In GCP, controls authentication and authorization.

**Idempotency**: Property where performing an operation multiple times has the same effect as performing it once. Critical for retries.

## L

**Latency**: Time taken for a request to complete. Usually measured as P50 (median), P95, P99 (percentiles).

**Lease**: A time-limited lock that grants exclusive access to a resource. Expires automatically, preventing deadlocks.

**Linearizability**: Strongest consistency model. All operations appear to occur atomically at some point in time.

**Load Shedding**: Dropping requests when a system is overloaded to prevent total failure. Better to serve some requests than none.

## M

**Mental Model**: A simplified representation of how a system works, used for reasoning about behavior and failures.

## O

**Observability**: The ability to understand a system's internal state from its external outputs (metrics, logs, traces).

**Overload**: When a system receives more load than it can handle, leading to degradation or failure.

## P

**Partition Tolerance**: The ability of a distributed system to continue operating despite network partitions (nodes can't communicate).

**Paxos**: A consensus algorithm for distributed systems. Complex but proven correct.

**Percentile (P50, P95, P99)**: A measure of latency distribution. P95 means 95% of requests complete in this time or less.

**PRR (Production Readiness Review)**: A review process to ensure a system is ready for production, covering reliability, security, operations.

**Pub/Sub**: Publish-subscribe messaging system. Publishers send messages to topics, subscribers receive messages from subscriptions.

## Q

**QPS (Queries Per Second)**: A measure of throughput, the number of requests a system handles per second.

**Queueing Theory**: Mathematical study of waiting lines. Explains tail latency and helps with capacity planning.

## R

**Raft**: A consensus algorithm simpler than Paxos, commonly used in distributed systems.

**Rate Limiting**: Controlling the rate of requests to prevent overload and ensure fair resource usage.

**Replication**: Storing copies of data on multiple nodes for availability and performance.

**Retry**: Attempting an operation again after it fails. Requires idempotency to be safe.

## S

**Sharding**: Partitioning data across multiple nodes. Each shard contains a subset of data.

**SLI (Service Level Indicator)**: A quantitative measure of service quality (e.g., latency, availability, error rate).

**SLO (Service Level Objective)**: A target value for an SLI (e.g., "P95 latency < 100ms", "availability > 99.9%").

**Spanner**: Google's globally distributed SQL database with strong consistency guarantees, using TrueTime for external consistency.

## T

**Tail Latency**: High percentiles of latency (P95, P99). Often much higher than median due to queueing and resource contention.

**Throughput**: The rate at which a system processes requests, usually measured in QPS or requests per second.

**TrueTime**: Google's clock synchronization service used by Spanner to provide external consistency guarantees.

## V

**VPC (Virtual Private Cloud)**: A logically isolated network in GCP where you can launch resources with private IP addresses.

## W

**Write-Ahead Log (WAL)**: A log where writes are recorded before being applied to the database, enabling durability and recovery.

