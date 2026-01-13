# Answer Key: Queues & Streams

[Back to Exercises](../../02-distributed-systems/queues-streams.md#exercises)

---

## Exercise 1: Choose Messaging

**Question**: When do you use queues vs streams? What are the tradeoffs?

### Answer

**Queues**:
- Task distribution
- Single consumer per message
- Job processing

**Streams**:
- Event distribution
- Multiple consumers
- Event-driven architectures

**Answer**: Queues for tasks, streams for events.

---

## Exercise 2: Handle Backlog

**Question**: Your queue has a large backlog. How do you handle it?

### Answer

**Solutions**:
1. **Scale consumers**: Add more consumers
2. **Optimize processing**: Optimize message processing
3. **Increase capacity**: Increase queue capacity
4. **Prioritize**: Process high-priority messages first

**Answer**: Scale consumers, optimize processing, increase capacity, prioritize messages.

---

## Exercise 3: Design Stream

**Question**: Design a stream processing system for real-time events.

### Answer

**Stream System**:
- **Topics**: Separate topics per event type
- **Subscriptions**: Subscriptions per consumer group
- **Ordering**: Ordering keys for per-key ordering
- **Processing**: Real-time processing with backpressure handling

**Answer**: Topics for events, subscriptions for consumers, ordering keys, backpressure handling.

