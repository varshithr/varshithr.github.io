# Answer Key: Canary Deployments & Rollouts

[Back to Exercises](../../04-reliability-sre/canary-rollouts.md#exercises)

---

## Exercise 1: Design Canary

**Question**: Design a canary deployment process. What percentage? How long?

### Answer

**Canary Design**:
- **Percentage**: 5% traffic
- **Duration**: 30 minutes monitoring
- **Metrics**: Error rate, latency, SLOs
- **Decision**: Proceed if metrics OK, rollback if issues

**Answer**: 5% traffic, 30 minutes monitoring, check error rate/latency/SLOs, proceed or rollback.

---

## Exercise 2: Handle Canary Failure

**Question**: Your canary shows issues. How do you respond?

### Answer

**Response**:
1. **Detect**: Detect issues in canary metrics
2. **Rollback**: Rollback canary immediately
3. **Investigate**: Investigate root cause
4. **Fix**: Fix issues before retry

**Answer**: Detect issues, rollback immediately, investigate root cause, fix before retry.

---

## Exercise 3: Plan Rollout

**Question**: Plan a gradual rollout. What are the phases?

### Answer

**Rollout Phases**:
1. **Canary**: 5% traffic, 30 minutes
2. **Phase 1**: 25% traffic, 15 minutes
3. **Phase 2**: 50% traffic, 15 minutes
4. **Phase 3**: 100% traffic, 1 hour

**Answer**: Canary (5%) → 25% → 50% → 100%, monitor at each phase.

