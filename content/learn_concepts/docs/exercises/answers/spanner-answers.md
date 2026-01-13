# Answer Key: Spanner

[Back to Exercises](../../03-gcp-core-building-blocks/spanner.md#exercises)

---

## Exercise 1: Design Schema

**Question**: Design a schema for an e-commerce application. What tables? What indexes? How do you handle interleaving?

### Answer

**Goal**: Design efficient Spanner schema for e-commerce application.

### Schema Design

**1. Users Table**

```sql
CREATE TABLE Users (
  UserId INT64 NOT NULL,
  Email STRING(MAX) NOT NULL,
  Name STRING(MAX),
  CreatedAt TIMESTAMP NOT NULL,
) PRIMARY KEY (UserId);

CREATE INDEX UsersByEmail ON Users(Email);
```

**2. Products Table**

```sql
CREATE TABLE Products (
  ProductId INT64 NOT NULL,
  Name STRING(MAX) NOT NULL,
  Price FLOAT64 NOT NULL,
  CategoryId INT64 NOT NULL,
  CreatedAt TIMESTAMP NOT NULL,
) PRIMARY KEY (ProductId);

CREATE INDEX ProductsByCategory ON Products(CategoryId);
```

**3. Orders Table (Interleaved)**

```sql
CREATE TABLE Orders (
  UserId INT64 NOT NULL,
  OrderId INT64 NOT NULL,
  Total FLOAT64 NOT NULL,
  Status STRING(MAX) NOT NULL,
  CreatedAt TIMESTAMP NOT NULL,
) PRIMARY KEY (UserId, OrderId),
  INTERLEAVE IN PARENT Users ON DELETE CASCADE;

CREATE INDEX OrdersByStatus ON Orders(Status);
```

**4. OrderItems Table (Interleaved)**

```sql
CREATE TABLE OrderItems (
  UserId INT64 NOT NULL,
  OrderId INT64 NOT NULL,
  ItemId INT64 NOT NULL,
  ProductId INT64 NOT NULL,
  Quantity INT64 NOT NULL,
  Price FLOAT64 NOT NULL,
) PRIMARY KEY (UserId, OrderId, ItemId),
  INTERLEAVE IN PARENT Orders ON DELETE CASCADE;
```

### Key Design Decisions

**Interleaving**:
- Orders interleaved in Users (co-locate user orders)
- OrderItems interleaved in Orders (co-locate order items)
- Benefits: Faster joins, better locality, atomic transactions

**Indexes**:
- UsersByEmail: Fast user lookup by email
- ProductsByCategory: Fast product filtering by category
- OrdersByStatus: Fast order filtering by status

**Answer**: Use interleaving for related data (Orders in Users, OrderItems in Orders), create indexes for common queries, design keys for even distribution.

---

## Exercise 2: Handle Consistency

**Question**: Your application needs external consistency. How do you ensure this with Spanner?

### Answer

**Spanner provides external consistency by default** using TrueTime and Paxos.

**Key points**:
- All read-write transactions are externally consistent
- TrueTime ensures global ordering
- No additional configuration needed

**Best practices**:
- Use read-write transactions for writes
- Use read-only transactions for reads (better performance)
- Understand TrueTime uncertainty (< 7ms)

**Answer**: Spanner provides external consistency automatically. Use read-write transactions for writes, read-only transactions for reads.

---

## Exercise 3: Optimize Performance

**Question**: Your queries are slow. How do you optimize them? What indexes do you add?

### Answer

**Optimization strategies**:

1. **Add Secondary Indexes**: Create indexes on frequently queried columns
2. **Use Interleaving**: Co-locate related data for faster joins
3. **Optimize Queries**: Reduce data scanned, use appropriate indexes
4. **Partition Data**: Use appropriate key design for distribution

**Example**: Add index on `Orders(Status)` for status filtering, use interleaving for Orders/OrderItems joins.

**Answer**: Add indexes for common queries, use interleaving for related data, optimize query patterns, design keys for even distribution.

