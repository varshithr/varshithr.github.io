# Answer Key: Pub/Sub

[Back to Exercises](../../03-gcp-core-building-blocks/pubsub.md#exercises)

---

## Exercise 1: Design Messaging

**Question**: Design a Pub/Sub architecture for an event-driven application. What topics? What subscriptions? How is ordering handled?

### Answer

**Goal**: Design Pub/Sub architecture for event-driven application.

### Architecture

**Topics**:
- `user-events`: User actions (login, logout, profile updates)
- `order-events`: Order events (created, updated, cancelled)
- `payment-events`: Payment events (processed, failed)

**Subscriptions**:
- `user-events-analytics`: Analytics processing
- `order-events-notifications`: Notification service
- `payment-events-audit`: Audit logging

**Ordering**: Use ordering keys (e.g., `user_id`, `order_id`) for per-entity ordering.

**Answer**: Separate topics by event type, create subscriptions per consumer, use ordering keys for per-entity ordering.

---

## Exercise 2: Handle Duplicates

**Question**: Your application receives duplicate messages. How do you handle them? What's the idempotency strategy?

### Answer

**Idempotency strategies**:

1. **Idempotency Keys**: Use message ID or custom idempotency key
2. **Deduplication**: Track processed message IDs (e.g., in database)
3. **Idempotent Operations**: Make operations idempotent (e.g., upsert)

**Example**: Track processed message IDs in database, check before processing.

**Answer**: Use idempotency keys, track processed message IDs, make operations idempotent.

---

## Exercise 3: Handle Failures

**Question**: Messages are failing to process. How do you handle failures? What's the dead letter queue strategy?

### Answer

**Failure handling**:

1. **Dead Letter Queue**: Configure DLQ for failed messages
2. **Retry Logic**: Implement exponential backoff retry
3. **Error Handling**: Handle different error types appropriately
4. **Monitoring**: Monitor DLQ and failed messages

**Answer**: Configure DLQ, implement retry logic, handle errors appropriately, monitor DLQ for issues.

