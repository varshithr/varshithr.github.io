# Answer Key: Load Shedding & Circuit Breakers

[Back to Exercises](../../04-reliability-sre/load-shedding.md#exercises)

---

## Exercise 1: Design Load Shedding

**Question**: Design a load shedding strategy. What requests do you shed?

### Answer

**Load Shedding Strategy**:
- **Priority-based**: Shed low-priority requests first
- **Rate-based**: Limit request rate, drop excess
- **Queue-based**: Drop when queue full
- **Protect critical**: Always process high-priority requests

**Answer**: Priority-based shedding, protect critical requests, drop low-priority when overloaded.

---

## Exercise 2: Configure Circuit Breaker

**Question**: Configure a circuit breaker. What are the thresholds?

### Answer

**Circuit Breaker Configuration**:
- **Error threshold**: 50% errors
- **Latency threshold**: P95 > 1 second
- **Timeout**: 30 seconds
- **Recovery**: 5 successes to close

**Answer**: 50% error threshold, P95 latency threshold, 30s timeout, 5 successes to recover.

---

## Exercise 3: Handle Overload

**Question**: Your system is overloaded. How do you handle it?

### Answer

**Overload Response**:
1. **Shed load**: Enable load shedding
2. **Circuit breakers**: Open circuit breakers to failing services
3. **Scale**: Scale up resources
4. **Monitor**: Monitor and adjust

**Answer**: Enable load shedding, open circuit breakers, scale resources, monitor closely.

