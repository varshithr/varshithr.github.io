# Postmortem Template

Use this template for writing postmortems after incidents. Focus on learning, not blame.

## Incident Summary

**Incident Title**: [Brief description]

**Date**: [Date and time]

**Duration**: [How long did it last?]

**Severity**: [P0/P1/P2]

**Impact**: [What was affected? How many users?]

**Status**: [Resolved/Mitigated/Ongoing]

---

## Timeline

### Discovery
- **Time**: [Timestamp]
- **Event**: [How was the incident discovered?]
- **Who**: [Who discovered it?]

### Response
- **Time**: [Timestamp]
- **Event**: [What happened next?]
- **Who**: [Who responded?]

### Resolution
- **Time**: [Timestamp]
- **Event**: [How was it resolved?]
- **Who**: [Who resolved it?]

### Recovery
- **Time**: [Timestamp]
- **Event**: [When was full recovery?]
- **Who**: [Who verified recovery?]

---

## Impact Assessment

### User Impact
- **Users Affected**: [Number or percentage]
- **Geographic Impact**: [Which regions?]
- **Feature Impact**: [Which features?]
- **Data Impact**: [Any data loss?]

### Business Impact
- **Revenue Impact**: [If applicable]
- **SLO Impact**: [Error budget consumed?]
- **Reputation Impact**: [Any public impact?]

### Technical Impact
- **Services Affected**: [Which services?]
- **Infrastructure Impact**: [What broke?]
- **Data Impact**: [Any data corruption?]

---

## Root Cause Analysis

### What Happened?
[Detailed description of what actually happened]

### Why Did It Happen?
[Root cause analysis - dig deep, ask "why" 5 times]

### Contributing Factors
- [Factor 1]
- [Factor 2]
- [Factor 3]

### Why Wasn't It Detected Earlier?
- [Detection gap 1]
- [Detection gap 2]

### Why Wasn't It Prevented?
- [Prevention gap 1]
- [Prevention gap 2]

---

## Detection & Response

### How Was It Detected?
- [Detection method 1]
- [Detection method 2]

### Detection Gaps
- [What should have detected it but didn't?]
- [What alerts should have fired?]
- [What monitoring was missing?]

### Response Effectiveness
- **Time to Detection**: [How long to detect?]
- **Time to Response**: [How long to respond?]
- **Time to Resolution**: [How long to resolve?]
- **What Went Well**: [What worked well?]
- **What Went Poorly**: [What didn't work well?]

### Communication
- **Internal Communication**: [How was the team notified?]
- **External Communication**: [How were users notified?]
- **Communication Gaps**: [What communication was missing?]

---

## Recovery

### Recovery Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Recovery Time
- **Time to Mitigation**: [How long to mitigate?]
- **Time to Resolution**: [How long to fully resolve?]
- **Time to Recovery**: [How long to full recovery?]

### Recovery Effectiveness
- **What Worked**: [What recovery steps worked?]
- **What Didn't Work**: [What recovery steps failed?]
- **What Slowed Recovery**: [What made recovery slower?]

---

## Action Items

### Immediate Actions (Fix Now)
- [ ] **Action**: [What to do]
  - **Owner**: [Who owns this?]
  - **Due Date**: [When?]
  - **Priority**: [P0/P1/P2]

- [ ] **Action**: [What to do]
  - **Owner**: [Who owns this?]
  - **Due Date**: [When?]
  - **Priority**: [P0/P1/P2]

### Short-Term Actions (Fix Soon)
- [ ] **Action**: [What to do]
  - **Owner**: [Who owns this?]
  - **Due Date**: [When?]
  - **Priority**: [P0/P1/P2]

- [ ] **Action**: [What to do]
  - **Owner**: [Who owns this?]
  - **Due Date**: [When?]
  - **Priority**: [P0/P1/P2]

### Long-Term Actions (Fix Eventually)
- [ ] **Action**: [What to do]
  - **Owner**: [Who owns this?]
  - **Due Date**: [When?]
  - **Priority**: [P0/P1/P2]

- [ ] **Action**: [What to do]
  - **Owner**: [Who owns this?]
  - **Due Date**: [When?]
  - **Priority**: [P0/P1/P2]

---

## Lessons Learned

### What We Learned
- [Lesson 1]
- [Lesson 2]
- [Lesson 3]

### What We'll Do Differently
- [Change 1]
- [Change 2]
- [Change 3]

### What We'll Keep Doing
- [Good practice 1]
- [Good practice 2]
- [Good practice 3]

---

## Prevention

### How Do We Prevent This?
- [Prevention measure 1]
- [Prevention measure 2]
- [Prevention measure 3]

### How Do We Detect This Earlier?
- [Detection improvement 1]
- [Detection improvement 2]
- [Detection improvement 3]

### How Do We Respond Better?
- [Response improvement 1]
- [Response improvement 2]
- [Response improvement 3]

---

## Follow-Up

### Review Date
- **Postmortem Review**: [When will we review action items?]
- **Follow-Up Review**: [When will we check progress?]

### Tracking
- [ ] Action items are tracked in issue tracker
- [ ] Action items have owners and due dates
- [ ] Progress is reviewed regularly

---

## Appendix

### Logs & Metrics
- [Links to relevant logs]
- [Links to relevant metrics]
- [Screenshots of dashboards]

### Related Incidents
- [Link to similar incidents]
- [Link to related postmortems]

### References
- [Links to documentation]
- [Links to runbooks]
- [Links to design docs]

---

## Sign-Off

**Postmortem Author**: [Name]

**Date**: [Date]

**Reviewed By**: [Names]

**Approved By**: [Name]

---

## Notes

[Additional notes or context]

