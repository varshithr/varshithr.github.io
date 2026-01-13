# Answer Key: BigQuery

[Back to Exercises](../../03-gcp-core-building-blocks/bigquery.md#exercises)

---

## Exercise 1: Design Schema

**Question**: Design a BigQuery schema for a time-series analytics application. How do you partition? How do you cluster?

### Answer

**Goal**: Design efficient BigQuery schema for time-series analytics.

### Schema Design

```sql
CREATE TABLE events (
  event_id INT64 NOT NULL,
  user_id INT64 NOT NULL,
  event_time TIMESTAMP NOT NULL,
  event_type STRING NOT NULL,
  event_data JSON,
  created_at TIMESTAMP NOT NULL,
)
PARTITION BY DATE(event_time)
CLUSTER BY user_id, event_type;
```

**Partitioning**: By `event_time` (date)
- Reduces data scanned for time-range queries
- Automatic partition pruning

**Clustering**: By `user_id`, `event_type`
- Faster queries filtering by user or event type
- Better compression

**Answer**: Partition by date (event_time), cluster by user_id and event_type for common query patterns.

---

## Exercise 2: Optimize Queries

**Question**: Your queries are slow and expensive. How do you optimize them? What partitioning/clustering do you use?

### Answer

**Optimization strategies**:

1. **Add Partitioning**: Partition by date for time-range queries
2. **Add Clustering**: Cluster by frequently filtered columns
3. **Optimize Queries**: Reduce data scanned, use filters early
4. **Use Appropriate Functions**: Use efficient functions

**Example**: Partition by `event_date`, cluster by `user_id` and `event_type`.

**Answer**: Add partitioning for time-range queries, add clustering for common filters, optimize query patterns to reduce data scanned.

---

## Exercise 3: Handle Scaling

**Question**: Your application needs to handle 100× more queries. How do you scale BigQuery? What's the strategy?

### Answer

**Scaling strategies**:

1. **Reserve Slots**: Reserve slots for predictable workloads
2. **Optimize Queries**: Reduce query complexity and data scanned
3. **Use Caching**: Enable query result caching
4. **Distribute Load**: Distribute queries across time

**Answer**: Reserve slots for predictable load, optimize queries, enable caching, distribute query load across time.

