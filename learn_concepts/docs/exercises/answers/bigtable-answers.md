# Answer Key: Bigtable

[Back to Exercises](../../03-gcp-core-building-blocks/bigtable.md#exercises)

---

## Exercise 1: Design Keys

**Question**: Design row keys for a time-series application. How do you avoid hot spots?

### Answer

**Goal**: Design keys for even distribution and time-series queries.

### Key Design

**Good Design**: `{metric}:{hash}:{timestamp}`

**Example**:
```
cpu_usage:abc123:20240101100000
cpu_usage:def456:20240101100000
memory_usage:abc123:20240101100000
```

**Components**:
- **Prefix**: Metric name (logical grouping)
- **Hash**: Hash of device/entity ID (distribution)
- **Timestamp**: Time component (ordering)

**Benefits**:
- Even distribution (hash component)
- Supports time-range queries (timestamp component)
- Co-locates related data (prefix component)

**Answer**: Use `{metric}:{hash}:{timestamp}` format. Hash component ensures even distribution, timestamp enables time-range queries.

---

## Exercise 2: Handle Hot Spots

**Question**: Your table has hot spots. How do you fix them? What key changes do you make?

### Answer

**Hot spot causes**: Sequential keys, time-prefixed keys, small key space.

**Solutions**:

1. **Add Hash Component**: `{prefix}:{hash}:{suffix}`
2. **Reverse Timestamp**: Use reverse timestamp for recent data distribution
3. **Add Random Component**: Add random component to keys
4. **Redesign Keys**: Redesign key structure for better distribution

**Example**: Change from `{timestamp}:{device}` to `{device}:{hash}:{timestamp}`.

**Answer**: Add hash component to keys, reverse timestamp ordering, redesign key structure for even distribution.

---

## Exercise 3: Optimize Performance

**Question**: Your queries are slow. How do you optimize them? What column families do you use?

### Answer

**Optimization strategies**:

1. **Optimize Column Families**: Group related columns together
2. **Design Keys**: Design keys for even distribution
3. **Monitor Compaction**: Monitor and tune compaction
4. **Optimize Queries**: Reduce data scanned, use appropriate filters

**Example**: Use separate column families for frequently vs rarely accessed columns.

**Answer**: Optimize column families, design keys for distribution, monitor compaction, optimize query patterns.

