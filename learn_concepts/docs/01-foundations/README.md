# Foundations

Quantitative reasoning, capacity math, and mental models for understanding systems at scale.

## Overview

Before diving into distributed systems and GCP, we need solid foundations in:
- **Queueing theory**: Why tail latency exists and how to reason about it
- **Capacity math**: How to calculate resource needs and plan for scale
- **Observability**: What to measure and why

## Topics

1. [Queueing Theory & Tail Latency](queueing-tail-latency.md)
   - Why P99 latency is much higher than P50
   - Queueing models and Little's Law
   - Techniques for reducing tail latency

2. [Capacity Math Cheat Sheet](capacity-math.md)
   - Calculating CPU, memory, disk, network needs
   - Scaling calculations
   - Capacity forecasting

3. [Observability Basics](observability-basics.md)
   - Metrics, logs, traces
   - What to measure and why
   - Building an observability contract

## Learning Objectives

After completing this chapter, you should be able to:
- Reason quantitatively about latency distributions
- Calculate capacity needs from requirements
- Define what metrics matter for a system
- Understand why tail latency matters

## Prerequisites

- Basic understanding of statistics (mean, median, percentiles)
- Familiarity with system resources (CPU, memory, disk, network)

## Next Steps

- [Phase 1: Distributed Systems](../02-distributed-systems/README.md)
- [Back to Index](../INDEX.md)

