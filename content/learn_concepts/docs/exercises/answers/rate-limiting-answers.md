# Answer Key: Rate Limiter Implementations

[Back to Exercises](../../05-llD-patterns/rate-limiting.md#exercises)

---

## Exercise 1: Implement Token Bucket

**Question**: Implement a token bucket rate limiter. What are the edge cases?

### Answer

**Goal**: Implement token bucket rate limiter with edge case handling

### Implementation

**Python Implementation**:

```python
import time
import threading

class TokenBucket:
    def __init__(self, capacity, rate):
        """
        capacity: Maximum tokens (burst size)
        rate: Tokens added per second (sustained rate)
        """
        self.capacity = capacity
        self.rate = rate
        self.tokens = capacity
        self.last_update = time.time()
        self.lock = threading.Lock()
    
    def allow_request(self, tokens_needed=1):
        """
        Check if request is allowed.
        Returns True if allowed, False otherwise.
        """
        with self.lock:
            # Add tokens based on time elapsed
            now = time.time()
            time_elapsed = now - self.last_update
            tokens_to_add = time_elapsed * self.rate
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_update = now
            
            # Check if enough tokens
            if self.tokens >= tokens_needed:
                self.tokens -= tokens_needed
                return True
            else:
                return False
```

### Edge Cases

**1. Concurrent Access**

**Issue**: Multiple threads accessing bucket simultaneously

**Solution**: Use locks (threading.Lock) to ensure thread safety

**2. Clock Skew**

**Issue**: System clock changes (NTP updates, time adjustments)

**Problem**: Time calculations become incorrect

**Solution**: 
- Use monotonic clock (`time.monotonic()`) instead of wall clock
- Or handle clock jumps gracefully

**3. First Request**

**Issue**: First request after initialization

**Solution**: Initialize `last_update` to current time, start with full tokens

**4. Long Idle Period**

**Issue**: No requests for long time, tokens accumulate

**Problem**: May allow burst larger than intended

**Solution**: Already handled (tokens capped at capacity)

**5. Very High Rate**

**Issue**: Rate higher than capacity

**Problem**: Tokens added faster than capacity

**Solution**: Already handled (tokens capped at capacity)

**6. Zero or Negative Values**

**Issue**: Invalid capacity or rate values

**Solution**: Validate inputs, raise errors for invalid values

**7. Precision Issues**

**Issue**: Floating point precision in time calculations

**Problem**: Small errors accumulate

**Solution**: Use high-precision time, or use integer-based calculations

### Improved Implementation

```python
import time
import threading

class TokenBucket:
    def __init__(self, capacity, rate):
        if capacity <= 0 or rate <= 0:
            raise ValueError("Capacity and rate must be positive")
        
        self.capacity = float(capacity)
        self.rate = float(rate)
        self.tokens = float(capacity)
        self.last_update = time.monotonic()  # Use monotonic clock
        self.lock = threading.Lock()
    
    def allow_request(self, tokens_needed=1):
        with self.lock:
            # Add tokens based on time elapsed
            now = time.monotonic()
            time_elapsed = now - self.last_update
            
            # Handle clock jumps (shouldn't happen with monotonic, but be safe)
            if time_elapsed < 0:
                time_elapsed = 0
            
            tokens_to_add = time_elapsed * self.rate
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_update = now
            
            # Check if enough tokens
            if self.tokens >= tokens_needed:
                self.tokens -= tokens_needed
                return True
            else:
                return False
    
    def get_tokens_available(self):
        """Get current number of tokens available"""
        with self.lock:
            now = time.monotonic()
            time_elapsed = now - self.last_update
            if time_elapsed < 0:
                time_elapsed = 0
            tokens_to_add = time_elapsed * self.rate
            current_tokens = min(self.capacity, self.tokens + tokens_to_add)
            return current_tokens
```

### Answer

**Token Bucket Implementation**:

**Key components**:
- Capacity (burst size)
- Rate (tokens per second)
- Tokens (current count)
- Last update time
- Lock (for thread safety)

**Edge cases**:
1. **Concurrent access**: Use locks for thread safety
2. **Clock skew**: Use monotonic clock
3. **First request**: Initialize last_update to current time
4. **Long idle**: Tokens capped at capacity
5. **High rate**: Tokens capped at capacity
6. **Invalid inputs**: Validate capacity and rate
7. **Precision**: Use float or high-precision calculations

**Key principles**:
- **Thread safety**: Use locks
- **Clock handling**: Use monotonic clock
- **Input validation**: Validate inputs
- **Precision**: Handle floating point precision

---

## Exercise 2: Compare Algorithms

**Question**: Compare token bucket vs sliding window log. When would you use each?

### Answer

**Goal**: Understand tradeoffs between token bucket and sliding window log

### Comparison

| Aspect | Token Bucket | Sliding Window Log |
|--------|--------------|-------------------|
| **Accuracy** | Medium (approximate) | High (precise) |
| **Memory** | O(1) | O(n) where n = requests in window |
| **CPU** | O(1) | O(n) to clean old entries |
| **Burst Handling** | Yes (allows bursts) | No (strict limit) |
| **Complexity** | Simple | More complex |
| **Distributed** | Easy (Redis counters) | Hard (need to sync logs) |

### When to Use Token Bucket

**Use token bucket when**:
- **Burst handling needed**: Need to allow bursts up to capacity
- **Memory constrained**: Limited memory available
- **High throughput**: Need to handle many requests
- **Simple implementation**: Want simple, efficient solution
- **Distributed**: Need distributed rate limiting

**Examples**:
- API rate limiting (allow bursts)
- Network traffic shaping
- Resource allocation

### When to Use Sliding Window Log

**Use sliding window log when**:
- **Accuracy critical**: Need precise limit enforcement
- **Memory available**: Have memory for request logs
- **Low throughput**: Fewer requests (memory manageable)
- **Strict limits**: Need strict limit (no bursts)
- **Single server**: Not distributed

**Examples**:
- Payment processing (strict limits)
- Critical operations (precise control)
- Low-volume APIs

### Hybrid Approach

**Best of both worlds**:
- Use token bucket for high-volume, burst-tolerant scenarios
- Use sliding window log for low-volume, accuracy-critical scenarios
- Or use sliding window counter (compromise)

### Answer

**Token Bucket**:
- **Use when**: Burst handling needed, memory constrained, high throughput, distributed
- **Pros**: Simple, efficient, allows bursts, low memory
- **Cons**: Less accurate, approximate

**Sliding Window Log**:
- **Use when**: Accuracy critical, memory available, low throughput, strict limits
- **Pros**: Precise, accurate limit enforcement
- **Cons**: High memory, high CPU, complex, hard to distribute

**Recommendation**:
- **Most cases**: Use token bucket (simpler, more efficient)
- **Critical cases**: Use sliding window log (more accurate)
- **Compromise**: Use sliding window counter (balance)

---

## Exercise 3: Distributed Rate Limiting

**Question**: Design a distributed rate limiter. How do you ensure consistency?

### Answer

**Goal**: Rate limiting across multiple servers with consistency

### Challenge

**Problem**: Multiple servers need to share rate limit state

**Requirements**:
- Consistent limits across servers
- Low latency
- High availability
- Accurate

### Solution Options

**1. Centralized Store (Redis)**

**Architecture**:
- All servers check Redis for rate limits
- Redis stores counters/tokens
- Atomic operations ensure consistency

**Implementation**:
```python
import redis

class DistributedTokenBucket:
    def __init__(self, redis_client, key_prefix, capacity, rate):
        self.redis = redis_client
        self.key_prefix = key_prefix
        self.capacity = capacity
        self.rate = rate
    
    def allow_request(self, client_id, tokens_needed=1):
        key = f"{self.key_prefix}:{client_id}"
        now = time.time()
        
        # Use Redis Lua script for atomicity
        lua_script = """
        local key = KEYS[1]
        local capacity = tonumber(ARGV[1])
        local rate = tonumber(ARGV[2])
        local tokens_needed = tonumber(ARGV[3])
        local now = tonumber(ARGV[4])
        
        local bucket = redis.call('HMGET', key, 'tokens', 'last_update')
        local tokens = tonumber(bucket[1]) or capacity
        local last_update = tonumber(bucket[2]) or now
        
        local time_elapsed = now - last_update
        local tokens_to_add = time_elapsed * rate
        tokens = math.min(capacity, tokens + tokens_to_add)
        
        if tokens >= tokens_needed then
            tokens = tokens - tokens_needed
            redis.call('HMSET', key, 'tokens', tokens, 'last_update', now)
            redis.call('EXPIRE', key, 3600)  -- TTL
            return 1
        else
            redis.call('HMSET', key, 'tokens', tokens, 'last_update', now)
            redis.call('EXPIRE', key, 3600)
            return 0
        end
        """
        
        result = self.redis.eval(lua_script, 1, key, 
                                 self.capacity, self.rate, 
                                 tokens_needed, now)
        return result == 1
```

**Pros**:
- Consistent (single source of truth)
- Accurate
- Atomic operations

**Cons**:
- Redis is single point of failure
- Network latency
- Redis capacity

**2. Distributed Counters**

**Architecture**:
- Each server maintains local counter
- Periodically sync counters
- Use consensus algorithm

**Implementation**:
- Use Raft or Paxos for consensus
- More complex, eventual consistency

**Pros**:
- No single point of failure
- Lower latency (local checks)

**Cons**:
- Less accurate (eventual consistency)
- More complex
- Higher overhead

**3. Client-Side Enforcement**

**Architecture**:
- Client enforces rate limit
- Server validates
- Use tokens or quotas

**Pros**:
- Reduces server load
- Lower latency

**Cons**:
- Not secure (client can bypass)
- Less accurate

### Recommended Solution

**Use Centralized Store (Redis) with**:
- **Redis Cluster**: For high availability
- **Lua scripts**: For atomicity
- **TTL**: For cleanup
- **Connection pooling**: For performance

### Consistency Guarantees

**Strong Consistency**:
- Use Redis with Lua scripts (atomic operations)
- Single Redis instance or Redis Cluster with strong consistency

**Eventual Consistency**:
- Use distributed counters
- Accept some inconsistency for better performance

### Answer

**Distributed Rate Limiter Design**:

**Architecture**: **Centralized Store (Redis)**

**Components**:
1. **Redis**: Stores rate limit state (counters/tokens)
2. **Lua scripts**: Atomic operations for consistency
3. **Key structure**: `rate_limit:{client_id}` or `rate_limit:{user_id}`
4. **TTL**: Expire keys after window (cleanup)

**Consistency**:
- **Atomic operations**: Lua scripts ensure atomicity
- **Single source of truth**: Redis is authoritative
- **Strong consistency**: All servers see same state

**High Availability**:
- **Redis Cluster**: Multiple Redis nodes
- **Failover**: Automatic failover
- **Replication**: Data replicated

**Performance**:
- **Connection pooling**: Reuse connections
- **Pipeline**: Batch operations
- **Local caching**: Cache recent decisions (with TTL)

**Tradeoffs**:
- **Consistency vs Performance**: Strong consistency has higher latency
- **Accuracy vs Complexity**: Centralized is simpler but has single point of failure

**Best practice**: Use Redis Cluster with Lua scripts for strong consistency and high availability.

