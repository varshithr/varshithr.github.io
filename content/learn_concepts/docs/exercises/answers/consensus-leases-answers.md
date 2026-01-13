# Answer Key: Consensus & Leases

[Back to Exercises](../../02-distributed-systems/consensus-leases.md#exercises)

---

## Exercise 1: Choose Consensus

**Question**: When do you use consensus vs leases? What are the tradeoffs?

### Answer

**Use Consensus** when:
- Strong guarantees needed
- No single point of failure acceptable
- Can tolerate higher latency

**Use Leases** when:
- Coordination needed but consensus too expensive
- Time-based coordination sufficient
- Lower latency required

**Answer**: Use consensus for strong guarantees, leases for lighter-weight coordination.

---

## Exercise 2: Handle Leader Failure

**Question**: Your consensus system loses its leader. How does it recover?

### Answer

**Recovery Process**:
1. **Detect**: Detect leader failure (timeout)
2. **Elect**: Elect new leader (Raft/Paxos election)
3. **Resume**: Resume operations with new leader

**Answer**: Automatic leader election (Raft/Paxos), promote new leader, resume operations.

---

## Exercise 3: Design Leases

**Question**: Design a lease system for coordinating access to a shared resource.

### Answer

**Lease System**:
- **Lease server**: Manages leases
- **Lease duration**: Time-limited (e.g., 30 seconds)
- **Renewal**: Renew before expiry
- **Exclusivity**: Only one holder at a time

**Answer**: Lease server manages leases, time-limited exclusivity, renewable leases.

