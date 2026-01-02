# Learning Principles

## How to Use This Repository

### Depth Over Breadth
- **Staff-level depth** means understanding internals, failure modes, and tradeoffs
- Don't skip sections—each builds on previous concepts
- When you encounter a term you don't know, check the [glossary](glossary.md)

### Active Learning
- **Don't just read**—implement concepts, draw diagrams, explain to others
- Use the templates to create your own deep dives
- Challenge assumptions: "What if this fails?" "What happens at 10× load?"

### Quantitative Reasoning
- Always think in numbers: latency (P50/P95/P99), throughput (QPS), capacity (CPU/memory/IOPS)
- Understand the math behind queueing, capacity planning, and SLOs
- Use back-of-envelope calculations to validate designs

### Failure-First Thinking
- **Every system fails**—understand how and why
- Design for graceful degradation, not perfection
- Know your failure domains and blast radius

### Production Mindset
- Systems are built to be operated, not just deployed
- Consider observability, rollouts, and incident response from day one
- Security and reliability are not afterthoughts

## Study Techniques

### 1. Mental Models First
Before diving into implementation details, build a mental model:
- How does data flow?
- What are the critical paths?
- Where are the bottlenecks?

### 2. Failure Modes Analysis
For every system, ask:
- What breaks first under load?
- What happens if component X fails?
- How do we detect and recover?

### 3. Tradeoff Analysis
Every design choice has tradeoffs:
- What do we gain?
- What do we lose?
- What are the operational implications?

### 4. Cross-Reference
- Link related concepts
- Build a web of understanding
- Revisit topics as you learn more

## Staff-Level Expectations

### What Staff Engineers Know
- **Internals**: How systems actually work under the hood
- **Failure modes**: What breaks and why
- **Scale**: Behavior at 10×, 100×, 1000× normal load
- **Tradeoffs**: When to use what and why
- **Operations**: How to run systems reliably

### What Staff Engineers Ask
- "What's the failure domain?"
- "How do we detect this?"
- "What's the blast radius?"
- "How do we roll back?"
- "What's the observability contract?"

### What Staff Engineers Care About
- **Reliability**: SLOs, error budgets, incident response
- **Security**: Identity, authorization, data protection
- **Performance**: Latency, throughput, tail latency
- **Operability**: Rollouts, monitoring, debugging
- **Cost**: Capacity planning, efficiency

## Progression Path

1. **Understand the concept** (what is it?)
2. **Understand the internals** (how does it work?)
3. **Understand failure modes** (what breaks?)
4. **Understand tradeoffs** (when to use it?)
5. **Understand operations** (how to run it?)
6. **Apply to real systems** (case studies)

## Common Pitfalls

### ❌ Surface-Level Understanding
- "I know what Spanner is" → but can't explain consistency model
- "I understand SLOs" → but can't define SLIs for a real system

### ✅ Deep Understanding
- Can explain Spanner's TrueTime and how it enables external consistency
- Can define SLIs, set SLOs, and use error budgets in practice

### ❌ Ignoring Operations
- Focus only on design, ignore rollouts and incidents
- Don't think about observability until production

### ✅ Production-First Thinking
- Design with rollouts and rollbacks in mind
- Define observability contract before implementation

### ❌ Avoiding Math
- Skip capacity calculations
- Don't understand queueing theory

### ✅ Quantitative Reasoning
- Calculate capacity needs from requirements
- Understand tail latency and its causes

## Resources

- [Reading List](reading_list.md) - Books and papers for deeper study
- [Glossary](glossary.md) - Definitions of terms
- [Deep Dive Template](deep_dive_template.md) - Structure for your own deep dives
- [Design Review Template](design_review_template.md) - How to review designs
- [PRR Template](prr_template.md) - Production readiness checklist
- [Postmortem Template](postmortem_template.md) - Incident analysis structure

