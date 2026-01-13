# Answer Key: Time, Ordering, and Causality

[Back to Exercises](../../02-distributed-systems/time-ordering-causality.md#exercises)

---

## Exercise 1: Design Ordering

**Question**: Design an event ordering system for a distributed application. What clocks do you use?

### Answer

**Use Vector Clocks** for precise causality tracking:
- Each process maintains vector of counters
- Captures causality precisely
- Can detect concurrent events

**Alternative**: Use Lamport clocks if precision not needed (simpler, less storage).

**Answer**: Use vector clocks for precise causality, or Lamport clocks for simpler ordering.

---

## Exercise 2: Handle Clock Skew

**Question**: Your system has clock skew. How do you handle it? What's the strategy?

### Answer

**Strategies**:
1. **Use logical clocks**: Don't rely on physical clocks
2. **Synchronize clocks**: Regular clock synchronization (NTP)
3. **Bounded uncertainty**: Use TrueTime-like approach with bounded uncertainty

**Answer**: Use logical clocks (vector clocks), synchronize physical clocks regularly, or use bounded clock uncertainty.

---

## Exercise 3: Establish Causality

**Question**: How do you establish causality between events in a distributed system?

### Answer

**Use Vector Clocks**:
- Each event gets vector clock timestamp
- Compare vector clocks to establish causality
- If V(A) < V(B), then A → B

**Answer**: Use vector clocks to establish causality by comparing timestamps.

