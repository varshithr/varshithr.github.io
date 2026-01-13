# Reliability Engineering & SRE

Building and operating reliable systems at scale: SLIs/SLOs, incidents, capacity planning, and more.

## Overview

This chapter covers SRE practices for building reliable systems:
- **SLIs/SLOs**: Defining and measuring reliability
- **PRRs**: Production readiness reviews
- **Incidents**: Response and postmortems
- **Capacity**: Planning and forecasting
- **Load shedding**: Handling overload
- **Rollouts**: Safe deployments
- **Testing**: Testing for failure

## Topics

1. [SLIs, SLOs & Error Budgets](sli-slo-error-budget.md)
   - Defining meaningful SLIs
   - Setting appropriate SLOs
   - Using error budgets

2. [Production Readiness Reviews (PRR)](prr-checklist.md)
   - What staff engineers look for
   - PRR checklist and process
   - Common PRR failures

3. [Incident Response & Postmortems](incident-response.md)
   - Incident response process
   - Writing effective postmortems
   - Learning from incidents

4. [Capacity Planning & Forecasting](capacity-planning.md)
   - Calculating capacity needs
   - Forecasting growth
   - Scaling strategies

5. [Load Shedding & Circuit Breakers](load-shedding.md)
   - When and how to shed load
   - Circuit breaker patterns
   - Graceful degradation

6. [Canary Deployments & Rollouts](canary-rollouts.md)
   - Canary deployment strategies
   - Rollout automation
   - Rollback procedures

7. [Testing for Failure](testing-for-failure.md)
   - Chaos engineering
   - Failure injection
   - Load testing

## Learning Objectives

After completing this chapter, you should be able to:
- Define SLIs and set SLOs for systems
- Run production readiness reviews
- Respond to incidents effectively
- Plan capacity and forecast needs
- Design systems that degrade gracefully
- Deploy changes safely

## Prerequisites

- [Phase 0: Foundations](../01-foundations/README.md)
- [Phase 2: GCP Core Building Blocks](../03-gcp-core-building-blocks/README.md)

## Next Steps

- [Phase 4: Case Studies](../06-case-studies/README.md)
- [Back to Index](../INDEX.md)

