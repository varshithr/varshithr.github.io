# Further Reading: Time, Ordering, and Causality

[Back to Time, Ordering, and Causality](../02-distributed-systems/time-ordering-causality.md)

---

## Research Papers

**"Time, Clocks, and the Ordering of Events in a Distributed System"** (Lamport, 1978)
- Original Lamport clocks paper
- [Link](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)

**"Virtual Time and Global States of Distributed Systems"** (Mattern, 1989)
- Vector clocks paper
- [Link](https://www.vs.inf.ethz.ch/pubs/papers/Mattern89.pdf)

---

## Additional Resources

### Books

**"Distributed Systems: Concepts and Design"** by George Coulouris
- Chapter on time and ordering
- Logical clocks and causality

**"Designing Data-Intensive Applications"** by Martin Kleppmann
- Chapter on ordering and causality
- Practical examples

---

## Key Takeaways

1. **Logical clocks**: Use logical clocks for causality without global clocks
2. **Vector clocks**: Vector clocks capture causality precisely
3. **TrueTime**: Bounded clock uncertainty enables external consistency
4. **Ordering**: Different ordering guarantees for different use cases

---

## Related Topics

- [Consensus & Leases](../02-distributed-systems/consensus-leases.md) - Consensus algorithms
- [Spanner: Consistency & Performance](../03-gcp-core-building-blocks/spanner.md) - TrueTime in Spanner
- [Back to Distributed Systems](../02-distributed-systems/README.md)

