# Further Reading: Rate Limiting

[Back to Rate Limiting](../05-llD-patterns/rate-limiting.md)

---

## Rate Limiting Algorithms

### Token Bucket Algorithm

**Paper**: [Token Bucket Algorithm](https://en.wikipedia.org/wiki/Token_bucket)

**Why it matters**: Classic algorithm for rate limiting, widely used in practice.

### Key Concepts

**Algorithm**:
- Tokens added at fixed rate
- Requests consume tokens
- Requests allowed if tokens available

**Properties**:
- Allows bursts up to capacity
- Simple to implement
- O(1) memory and time complexity

**Relevance**: Provides the mathematical foundation for token bucket implementation.

---

## Sliding Window Algorithms

### Fixed Window vs Sliding Window

**Article**: [Rate Limiting Algorithms](https://konghq.com/blog/how-to-design-a-scalable-rate-limiting-algorithm)

**Why it matters**: Comparison of different rate limiting algorithms and their tradeoffs.

### Key Concepts

**Fixed Window**:
- Simple implementation
- Allows bursts at window boundaries
- O(1) memory and time

**Sliding Window Log**:
- Precise limit enforcement
- No bursts
- O(n) memory and time

**Sliding Window Counter**:
- Compromise between fixed and log
- More accurate than fixed window
- O(k) memory and time (k = sub-windows)

**Relevance**: Explains when to use each algorithm and their tradeoffs.

---

## Distributed Rate Limiting

### Redis-Based Rate Limiting

**Article**: [Redis Rate Limiting](https://redis.io/docs/manual/patterns/rate-limiting/)

**Why it matters**: How to implement distributed rate limiting using Redis.

### Key Concepts

**Redis Lua Scripts**:
- Atomic operations
- Consistent across servers
- Single source of truth

**Implementation**:
- Store counters in Redis
- Use Lua scripts for atomicity
- Set TTL for cleanup

**Relevance**: Provides practical implementation for distributed rate limiting.

---

## Rate Limiting Best Practices

### Google Cloud Documentation

**Documentation**: [API Rate Limiting](https://cloud.google.com/endpoints/docs/openapi/rate-limiting)

**Why it matters**: GCP's approach to rate limiting in APIs.

### Key Practices

**1. Per-Client Limits**
- Different limits for different clients
- Protect against abuse
- Fair resource usage

**2. Global Limits**
- System-wide capacity limits
- Prevent overload
- Load shedding

**3. Monitoring**
- Track rate limit violations
- Monitor rate limit effectiveness
- Alert on abuse patterns

**Relevance**: Provides best practices for implementing rate limiting.

---

## Additional Resources

### Papers

**"Rate Limiting Algorithms"** (Various)
- Academic papers on rate limiting
- Algorithm analysis

### Books

**"Designing Data-Intensive Applications"** by Martin Kleppmann
- Chapter on rate limiting
- Distributed rate limiting

**"Building Microservices"** by Sam Newman
- Chapter on API design
- Rate limiting in microservices

### Online Resources

**Kong API Gateway**: [Rate Limiting](https://docs.konghq.com/hub/kong-inc/rate-limiting/)
- Rate limiting implementation
- Best practices

**AWS API Gateway**: [Rate Limiting](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
- AWS approach to rate limiting
- Implementation examples

---

## Key Takeaways

1. **Choose right algorithm**: Token bucket for bursts, sliding window for accuracy
2. **Distributed requires coordination**: Use Redis or similar for consistency
3. **Monitor violations**: Track rate limit effectiveness
4. **Tune limits**: Adjust based on actual usage
5. **Handle failures gracefully**: Fail open or closed based on requirements

---

## Related Topics

- [Overload & Backpressure](../02-distributed-systems/overload-backpressure.md) - How rate limiting prevents overload
- [Circuit Breakers](../05-llD-patterns/circuit-breakers.md) - Related pattern for failure handling
- [Load Shedding](../04-reliability-sre/load-shedding.md) - Related technique for overload

