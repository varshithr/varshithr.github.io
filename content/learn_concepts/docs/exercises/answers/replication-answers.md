# Answer Key: Replication Strategies

[Back to Exercises](../../02-distributed-systems/replication.md#exercises)

---

## Exercise 1: Choose Replication

**Question**: When do you use master-slave vs multi-master? What are the tradeoffs?

### Answer

**Master-Slave**:
- Strong consistency required
- Read scaling needed
- Can tolerate master failure downtime

**Multi-Master**:
- High availability required
- Write scaling needed
- Can tolerate eventual consistency

**Answer**: Master-slave for consistency, multi-master for availability and write scaling.

---

## Exercise 2: Handle Master Failure

**Question**: Your master-slave system loses its master. How does it recover?

### Answer

**Recovery Process**:
1. **Detect**: Detect master failure
2. **Promote**: Promote slave to master
3. **Update**: Update routing to new master
4. **Resume**: Resume operations

**Answer**: Automatic failover, promote slave to master, update routing, resume operations.

---

## Exercise 3: Design Quorum

**Question**: Design a quorum replication system. How many replicas? What's the quorum?

### Answer

**Quorum Design**:
- **Replicas**: 3 replicas (minimum for quorum)
- **Write quorum**: 2 replicas (majority)
- **Read quorum**: 2 replicas (majority)
- **Availability**: Available if 2+ replicas available

**Answer**: 3 replicas, quorum of 2 (majority), available if majority available.

