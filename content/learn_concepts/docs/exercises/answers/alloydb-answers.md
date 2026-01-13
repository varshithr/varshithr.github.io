# Answer Key: AlloyDB

[Back to Exercises](../../03-gcp-core-building-blocks/alloydb.md#exercises)

---

## Exercise 1: Design Architecture

**Question**: Design an AlloyDB architecture for a high-traffic application. How many read replicas? What's the failover strategy?

### Answer

**Goal**: Design high-availability AlloyDB architecture.

### Architecture

**Primary Instance**: 
- Region: `us-central1`
- Machine Type: `db-standard-8` (8 vCPU, 30GB RAM)
- High Availability: Enabled

**Read Replicas**:
- **Replica 1**: `us-central1` (same zone as primary)
- **Replica 2**: `us-east1` (different region)
- **Replica 3**: `us-west1` (different region)

**Failover Strategy**:
- Automatic failover (< 60 seconds)
- Promote read replica to primary
- Update application connection strings

**Answer**: Use 3 read replicas (1 same region, 2 different regions), enable automatic failover, design for < 60 second RTO.

---

## Exercise 2: Handle Scaling

**Question**: Your application needs to scale reads. How do you scale with AlloyDB? What's the strategy?

### Answer

**Scaling strategies**:

1. **Add Read Replicas**: Add more read replicas for read scaling
2. **Connection Pooling**: Use connection pooling for efficient connections
3. **Read-Write Splitting**: Route reads to replicas, writes to primary
4. **Monitor Performance**: Monitor replica lag and performance

**Answer**: Add read replicas for horizontal read scaling, use connection pooling, implement read-write splitting.

---

## Exercise 3: Optimize Performance

**Question**: Your queries are slow. How do you optimize them? What AlloyDB features do you use?

### Answer

**Optimization strategies**:

1. **Use Columnar Cache**: Enable columnar cache for analytics
2. **Optimize Queries**: Use appropriate indexes and query patterns
3. **Connection Pooling**: Use connection pooling
4. **Monitor Performance**: Monitor query performance and optimize

**Answer**: Enable columnar cache, optimize queries with indexes, use connection pooling, monitor and optimize continuously.

