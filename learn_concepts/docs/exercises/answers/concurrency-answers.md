# Answer Key: Concurrency Primitives

[Back to Exercises](../../05-llD-patterns/concurrency.md#exercises)

---

## Exercise 1: Design Concurrency

**Question**: Design concurrent access to shared resource. What primitives?

### Answer

**Concurrency Design**:
- **Mutex**: For exclusive access
- **Read-write lock**: For read-heavy workloads
- **Channels**: For communication between goroutines
- **Atomic operations**: For simple operations

**Answer**: Use mutex for exclusive access, read-write locks for reads, channels for communication.

---

## Exercise 2: Prevent Deadlock

**Question**: How do you prevent deadlocks in your system?

### Answer

**Deadlock Prevention**:
1. **Lock ordering**: Always acquire locks in same order
2. **Timeout**: Use timeout on locks
3. **Avoid circular dependencies**: Avoid circular lock dependencies
4. **Lock-free**: Use lock-free algorithms where possible

**Answer**: Consistent lock ordering, timeouts, avoid circular dependencies, use lock-free when possible.

---

## Exercise 3: Handle Race Condition

**Question**: Your system has a race condition. How do you fix it?

### Answer

**Fix Race Condition**:
1. **Identify**: Identify shared resource and race condition
2. **Add synchronization**: Add locks or atomic operations
3. **Test**: Test thoroughly for race conditions
4. **Verify**: Verify fix eliminates race condition

**Answer**: Identify race condition, add synchronization (locks/atomics), test thoroughly, verify fix.

