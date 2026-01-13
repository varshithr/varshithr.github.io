# Answer Key: Testing for Failure

[Back to Exercises](../../04-reliability-sre/testing-for-failure.md#exercises)

---

## Exercise 1: Design Failure Tests

**Question**: Design failure tests for a distributed system. What failures do you test?

### Answer

**Failure Tests**:
- **Network failures**: Latency, packet loss, partitions
- **Node failures**: Process kills, reboots, resource exhaustion
- **Service failures**: Service down, slow responses, errors
- **Database failures**: Connection failures, query failures

**Answer**: Test network, node, service, and database failures systematically.

---

## Exercise 2: Run Chaos Experiment

**Question**: Run a chaos engineering experiment. What's the process?

### Answer

**Chaos Process**:
1. **Hypothesis**: Form hypothesis about system behavior
2. **Experiment**: Run in staging first, then production
3. **Observe**: Monitor system behavior
4. **Learn**: Learn from results, improve system

**Answer**: Hypothesis → Experiment → Observe → Learn, start in staging.

---

## Exercise 3: Handle Test Failure

**Question**: Your failure test causes system failure. How do you respond?

### Answer

**Response**:
1. **Stop test**: Stop failure injection immediately
2. **Restore**: Restore system to normal state
3. **Investigate**: Investigate why system failed
4. **Fix**: Fix issues, improve resilience
5. **Retry**: Retry test after fixes

**Answer**: Stop test, restore system, investigate, fix issues, improve resilience, retry.

