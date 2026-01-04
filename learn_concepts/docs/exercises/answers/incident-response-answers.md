# Answer Key: Incident Response & Postmortems

[Back to Exercises](../../04-reliability-sre/incident-response.md#exercises)

---

## Exercise 1: Design Incident Response

**Question**: Design an incident response process. What are the steps?

### Answer

**Incident Response Process**:
1. **Detect**: Detect incident (monitoring, alerts)
2. **Assess**: Assess severity and impact
3. **Mitigate**: Mitigate impact (rollback, scale, etc.)
4. **Resolve**: Fix root cause
5. **Postmortem**: Write postmortem, action items

**Answer**: Detect → Assess → Mitigate → Resolve → Postmortem.

---

## Exercise 2: Write Postmortem

**Question**: Write a postmortem for a hypothetical incident. What's included?

### Answer

**Postmortem Sections**:
1. **Timeline**: Incident timeline
2. **Impact**: Users affected, duration
3. **Root cause**: Root cause analysis
4. **Actions**: Action items to prevent recurrence
5. **Learnings**: Key learnings

**Answer**: Timeline, impact, root cause, action items, learnings.

---

## Exercise 3: Handle Incident

**Question**: Your service is down. How do you respond? What's the process?

### Answer

**Response Process**:
1. **Acknowledge**: Acknowledge incident (P0)
2. **Assess**: Check service health, identify issue
3. **Mitigate**: Rollback, scale, enable circuit breakers
4. **Resolve**: Fix root cause
5. **Postmortem**: Write postmortem

**Answer**: Acknowledge → Assess → Mitigate → Resolve → Postmortem.

