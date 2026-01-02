# GCP Core Building Blocks

Deep understanding of GCP primitives: how they work, how they fail, and when to use them.

## Overview

This chapter covers GCP's core services at staff-level depth:
- **Networking**: VPC, load balancing, DNS
- **Compute**: GKE internals, container orchestration
- **Identity**: IAM evaluation model, service accounts
- **Storage**: Cloud Storage, Spanner, Bigtable, BigQuery
- **Messaging**: Pub/Sub delivery guarantees
- **Security**: KMS, secret management

## Topics

1. [VPC, Load Balancing & DNS](vpc-lb-dns.md)
   - VPC architecture and routing
   - Load balancer types and use cases
   - DNS resolution and caching

2. [GKE Control Plane & Data Plane](gke-internals.md)
   - Kubernetes control plane components
   - GKE-managed control plane
   - Pod networking and service mesh

3. [IAM Evaluation Model](iam-evaluation.md)
   - How IAM policies are evaluated
   - Service accounts and workload identity
   - Common IAM footguns

4. [Cloud Storage Deep Dive](cloud-storage.md)
   - Storage classes and lifecycle policies
   - Consistency model
   - Performance characteristics

5. [Spanner: Consistency & Performance](spanner.md)
   - TrueTime and external consistency
   - Distributed transactions
   - Performance characteristics and tradeoffs

6. [Bigtable: Design & Tradeoffs](bigtable.md)
   - Wide-column store design
   - Performance characteristics
   - When to use vs Spanner

7. [BigQuery Architecture](bigquery.md)
   - Columnar storage and Dremel
   - Query execution
   - Performance optimization

8. [Pub/Sub: Delivery Guarantees](pubsub.md)
   - At-least-once delivery
   - Ordering guarantees
   - Dead letter queues

9. [Cloud KMS & Secret Management](kms-secrets.md)
   - Key management and rotation
   - Secret Manager
   - Encryption at rest and in transit

## Learning Objectives

After completing this chapter, you should be able to:
- Design networks and load balancing strategies
- Understand GKE internals and troubleshoot issues
- Design IAM policies correctly
- Choose the right storage solution for use cases
- Understand Pub/Sub delivery guarantees
- Implement secure key and secret management

## Prerequisites

- [Phase 1: Distributed Systems](../02-distributed-systems/README.md)
- Basic familiarity with GCP services

## Next Steps

- [Phase 3: Reliability & SRE](../04-reliability-sre/README.md)
- [Phase 4: Case Studies](../06-case-studies/README.md)
- [Back to Index](../INDEX.md)

