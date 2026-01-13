# GCP Staff-Level System Design & SRE Deep Dive

> **Target audience**: Engineers aiming for staff/SRE-level depth in GCP, distributed systems, and production reliability.  
> **Goal**: Understand internals, failure modes, and tradeoffs at the depth expected of senior staff engineers and SREs at Google.

## Quick Start

1. **New to the repo?** Start here: [docs/INDEX.md](docs/INDEX.md)
2. **Want a guided path?** Follow the **Learning Path** section in the index.
3. **Looking for a specific topic?** Use the **Reference Map** section.
4. **Track your progress:** Check off items in [docs/PROGRESS.md](docs/PROGRESS.md)

## Structure

```
docs/
├── 00-meta/          # Templates, glossary, learning principles
├── 01-foundations/    # Quantitative reasoning, capacity math, mental models
├── 02-distributed-systems/  # Consensus, replication, ordering, overload
├── 03-gcp-core-building-blocks/  # VPC, GKE, IAM, Spanner, Bigtable, etc.
├── 04-reliability-sre/  # SLIs/SLOs, PRRs, postmortems, capacity planning
├── 05-llD-patterns/  # Idempotency, rate limiting, circuit breakers
└── 06-case-studies/  # End-to-end system designs with ops playbooks
```

## How to Use This Repo

### As a Curriculum
- Follow the phases in order (Phase 0 → Phase 4)
- Complete exercises and deep dives before moving on
- Use [docs/PROGRESS.md](docs/PROGRESS.md) to track milestones

### As a Reference
- Jump to specific topics via the Reference Map
- Use templates in `00-meta/` for your own deep dives
- Cross-reference related concepts using the links

### Depth Standards
Every deep dive includes:
- **Mental model**: How to think about the system
- **Internals**: Implementation details and architecture
- **Failure modes**: What breaks and why
- **Overload behavior**: Behavior at 10×, 100× load
- **Observability**: What to measure and where
- **Change safety**: Rollout strategies and reversibility
- **Security boundaries**: Identity, authorization, data protection
- **Tradeoffs**: What you gain/lose with each choice

## Contributing

When adding new content:
1. Use the templates in `docs/00-meta/`
2. Maintain staff-level depth (see guardrails in INDEX.md)
3. Cross-link related topics
4. Update INDEX.md and PROGRESS.md

## License

This is a personal learning repository. Use freely for your own education.

