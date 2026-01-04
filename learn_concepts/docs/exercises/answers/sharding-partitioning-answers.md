# Answer Key: Sharding & Partitioning

[Back to Exercises](../../02-distributed-systems/sharding-partitioning.md#exercises)

---

## Exercise 1: Design Partitioning

**Question**: Design a partitioning strategy for a user database. What partition key? What strategy?

### Answer

**Partitioning Strategy**:
- **Partition key**: `user_id`
- **Strategy**: Hash partitioning (even distribution)
- **Shards**: Distribute across shards by hash

**Alternative**: Range partitioning if range queries needed.

**Answer**: Hash partitioning on user_id for even distribution, or range partitioning for range queries.

---

## Exercise 2: Handle Hot Spots

**Question**: Your partitioned system has hot spots. How do you fix them?

### Answer

**Solutions**:
1. **Redesign keys**: Add hash component to keys
2. **Split shards**: Split hot shards
3. **Rebalance**: Rebalance data across shards

**Answer**: Redesign keys with hash component, split hot shards, rebalance data.

---

## Exercise 3: Rebalance Data

**Question**: How do you rebalance data when adding new shards?

### Answer

**Rebalancing Process**:
1. **Add shards**: Add new shards
2. **Migrate data**: Migrate data to new shards
3. **Update routing**: Update routing to new shards
4. **Verify**: Verify data distribution

**Answer**: Add shards, migrate data using consistent hashing, update routing, verify distribution.

