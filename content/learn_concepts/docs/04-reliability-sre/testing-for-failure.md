# Testing for Failure

**One-line summary**: How to test systems for failure scenarios, chaos engineering, and failure injection.

**Prerequisites**: [Foundations](../01-foundations/README.md), understanding of testing and reliability.

---

## Mental Model

### Failure Testing

**Failure testing**: Intentionally inject failures to test system resilience.

**Goals**:
- **Find weaknesses**: Discover failure modes before production
- **Validate resilience**: Verify system handles failures correctly
- **Build confidence**: Build confidence in system reliability

```mermaid
graph LR
    System[System] --> Inject[Inject Failure]
    Inject --> Observe[Observe Behavior]
    Observe --> Learn[Learn & Improve]
    
    style Inject fill:#ff9999
    style Observe fill:#99ccff
```

**Key insight**: Testing for failure helps build resilient systems by discovering weaknesses early.

---

## Internals & Architecture

### Failure Injection Types

#### Network Failures

**Types**:
- **Latency**: Add network latency
- **Packet loss**: Drop packets
- **Partition**: Network partition
- **Timeout**: Connection timeouts

**Use case**: Test network resilience.

#### Node Failures

**Types**:
- **Kill process**: Kill application process
- **Reboot node**: Reboot server
- **Resource exhaustion**: Exhaust CPU/memory
- **Disk failure**: Simulate disk failure

**Use case**: Test node failure handling.

#### Service Failures

**Types**:
- **Service down**: Take service offline
- **Slow responses**: Slow down service responses
- **Error injection**: Inject errors
- **Timeout**: Service timeouts

**Use case**: Test service failure handling.

### Chaos Engineering

**Chaos engineering**: Systematic experimentation on distributed systems.

**Process**:
1. **Hypothesis**: Form hypothesis about system behavior
2. **Experiment**: Run experiment in production-like environment
3. **Observe**: Observe system behavior
4. **Learn**: Learn from results, improve system

**Principles**:
- **Start small**: Start with small experiments
- **Gradual**: Gradually increase scope
- **Automated**: Automate experiments
- **Safe**: Ensure experiments are safe

---

## Failure Modes & Blast Radius

### Testing Failures

#### Scenario 1: Test Too Aggressive
- **Impact**: System fails, production impact
- **Blast radius**: Entire system
- **Detection**: System failures during testing
- **Recovery**: Stop testing, restore system
- **Mitigation**: Start small, test in staging first

#### Scenario 2: Missing Failure Scenarios
- **Impact**: Undiscovered failure modes, production incidents
- **Blast radius**: Production incidents
- **Detection**: Production failures
- **Recovery**: Fix issues, add tests
- **Mitigation**: Comprehensive test coverage

---

## Observability Contract

### Metrics

- **Test coverage**: Failure scenarios tested
- **Test success rate**: Percentage of tests passing
- **Failure detection**: Failures discovered
- **Recovery time**: Time to recover from test failures

### Alerts

- Test failures
- System failures during testing
- Missing test coverage

---

## Change Safety

### Testing Process

- **Process**: Run tests in staging, then production
- **Risk**: Low (controlled testing)
- **Rollback**: Stop tests if issues

---

## Tradeoffs

### Staging vs Production Testing

**Staging testing**:
- **Pros**: Safer, no production impact
- **Cons**: May not catch production-specific issues

**Production testing**:
- **Pros**: Real environment, catch real issues
- **Cons**: Production impact risk

---

## Operational Considerations

### Best Practices

1. **Start small**: Begin with small, safe tests
2. **Automate**: Automate failure injection
3. **Monitor**: Monitor system during tests
4. **Learn**: Learn from test results, improve

---

## What Staff Engineers Ask in Reviews

- "What failure scenarios are tested?"
- "How is chaos engineering used?"
- "What's the testing process?"
- "How are test results used?"

---

## Further Reading

**Comprehensive Guide**: [Further Reading: Testing for Failure](../further-reading/testing-for-failure.md)

**Quick Links**:
- "Chaos Engineering" (Netflix)
- [Canary Deployments & Rollouts](canary-rollouts.md)
- [Incident Response & Postmortems](incident-response.md)
- [Back to Reliability & SRE](README.md)

---

## Exercises

1. **Design failure tests**: Design failure tests for a distributed system. What failures do you test?

2. **Run chaos experiment**: Run a chaos engineering experiment. What's the process?

3. **Handle test failure**: Your failure test causes system failure. How do you respond?

**Answer Key**: [View Answers](../exercises/answers/testing-for-failure-answers.md)

