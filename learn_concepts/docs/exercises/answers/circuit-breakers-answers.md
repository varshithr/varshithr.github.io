# Answer Key: Circuit Breaker Pattern

[Back to Exercises](../../05-llD-patterns/circuit-breakers.md#exercises)

---

## Exercise 1: Implement Circuit Breaker

**Question**: Implement a circuit breaker. What are the states?

### Answer

**Circuit Breaker States**:
- **Closed**: Normal operation, calls pass through
- **Open**: Service failing, calls rejected
- **Half-open**: Testing if service recovered

**State transitions**: Closed → Open (on failure), Open → Half-open (on timeout), Half-open → Closed (on success).

**Answer**: Three states (closed/open/half-open), transitions based on failure/success.

---

## Exercise 2: Configure Thresholds

**Question**: Configure circuit breaker thresholds. What values?

### Answer

**Thresholds**:
- **Error rate**: 50% errors
- **Latency**: P95 > 1 second
- **Timeout**: 30 seconds open state
- **Success threshold**: 5 successes to close

**Answer**: 50% error threshold, P95 latency, 30s timeout, 5 successes to recover.

---

## Exercise 3: Handle Recovery

**Question**: Your circuit breaker opens. How does it recover?

### Answer

**Recovery Process**:
1. **Wait**: Wait for timeout (30 seconds)
2. **Test**: Transition to half-open, allow test requests
3. **Evaluate**: Evaluate test results
4. **Close**: Close if successful, reopen if failed

**Answer**: Wait timeout → half-open → test → evaluate → close on success, reopen on failure.

