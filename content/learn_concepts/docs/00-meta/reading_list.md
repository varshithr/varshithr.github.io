# Reading List

Essential books, papers, and articles for staff-level understanding of distributed systems, GCP, and SRE.

## Books

### Distributed Systems
- **Designing Data-Intensive Applications** by Martin Kleppmann
  - Comprehensive guide to distributed systems, databases, and data processing
  - Covers consistency, replication, partitioning, transactions

- **Distributed Systems: Concepts and Design** by George Coulouris et al.
  - Academic textbook on distributed systems fundamentals
  - Covers time, ordering, consensus, fault tolerance

### Google SRE
- **Site Reliability Engineering** (SRE Book)
  - Google's SRE practices and principles
  - SLIs, SLOs, error budgets, incident response

- **The Site Reliability Workbook**
  - Practical SRE implementation guide
  - Case studies and real-world examples

### System Design
- **System Design Interview** by Alex Xu
  - Practical system design patterns
  - Good for interview prep and design thinking

- **Building Microservices** by Sam Newman
  - Microservices architecture patterns
  - Service boundaries, data management, deployment

### Performance & Capacity
- **Systems Performance** by Brendan Gregg
  - Deep dive into system performance analysis
  - Tools, methodologies, case studies

## Papers

### Consensus & Consistency
- **The Part-Time Parliament** (Lamport, 1998)
  - Original Paxos paper
  - Foundation of consensus algorithms

- **In Search of an Understandable Consensus Algorithm** (Ongaro & Ousterhout, 2014)
  - Raft consensus algorithm
  - More understandable than Paxos

- **Spanner: Google's Globally-Distributed Database** (Corbett et al., 2012)
  - How Spanner provides external consistency
  - TrueTime and distributed transactions

- **The Google File System** (Ghemawat et al., 2003)
  - Design of GFS
  - Foundation for distributed storage

### Distributed Systems
- **Time, Clocks, and the Ordering of Events in a Distributed System** (Lamport, 1978)
  - Logical clocks and causality
  - Fundamental paper on time in distributed systems

- **Dynamo: Amazon's Highly Available Key-value Store** (DeCandia et al., 2007)
  - Eventually consistent distributed storage
  - Tradeoffs in availability vs consistency

- **The Chubby Lock Service for Loosely-Coupled Distributed Systems** (Burrows, 2006)
  - Google's distributed lock service
  - Consensus and leases in practice

### Performance & Latency
- **The Tail at Scale** (Dean & Barroso, 2013)
  - Why tail latency matters
  - Techniques for reducing tail latency

- **The Datacenter as a Computer** (Barroso & Hölzle, 2018)
  - Datacenter design principles
  - Efficiency and performance at scale

### Reliability
- **Why Do Internet Services Fail, and What Can Be Done About It?** (Oppenheimer et al., 2003)
  - Analysis of internet service failures
  - Common failure modes and prevention

## Google-Specific

### GCP Documentation
- **GCP Architecture Center**
  - Best practices and reference architectures
  - Real-world case studies

- **GCP Well-Architected Framework**
  - Design principles for GCP
  - Security, reliability, performance, cost

### Google Research Papers
- **MapReduce: Simplified Data Processing on Large Clusters** (Dean & Ghemawat, 2004)
- **Bigtable: A Distributed Storage System for Structured Data** (Chang et al., 2006)
- **The Dataflow Model** (Akidau et al., 2015)
- **MillWheel: Fault-Tolerant Stream Processing at Internet Scale** (Akidau et al., 2013)

## Blogs & Articles

### Google Cloud Blog
- GCP product deep dives
- Architecture best practices
- Case studies

### High Scalability
- Real-world system architectures
- Lessons learned from scale

### AWS Architecture Blog
- System design patterns (applicable to GCP)
- Best practices

### Google SRE Blog
- SRE practices and principles
- Incident postmortems
- Reliability engineering

## Online Courses

### Distributed Systems
- **MIT 6.824: Distributed Systems**
  - Course materials available online
  - Labs implement Raft, MapReduce, etc.

### Cloud Architecture
- **GCP Professional Cloud Architect Certification**
  - Official GCP certification prep
  - Covers architecture best practices

## Conferences

### SREcon
- Site Reliability Engineering conference
- Talks on reliability, incidents, operations

### USENIX
- Systems and networking conferences
- Research papers and practical talks

### QCon
- Software architecture conference
- System design talks and case studies

## How to Use This List

1. **Start with fundamentals**: Read "Designing Data-Intensive Applications" and SRE Book
2. **Deep dive into topics**: Read papers on specific topics you're studying
3. **Apply to practice**: Use GCP documentation and case studies
4. **Stay current**: Follow blogs and conferences for latest practices

## Reading Order Recommendation

### Phase 0: Foundations
1. "Designing Data-Intensive Applications" (chapters 1-3)
2. SRE Book (chapters 1-5)

### Phase 1: Distributed Systems
1. "Time, Clocks, and the Ordering of Events"
2. "In Search of an Understandable Consensus Algorithm"
3. "Designing Data-Intensive Applications" (chapters 5-9)

### Phase 2: GCP Deep Dive
1. GCP Architecture Center
2. "Spanner: Google's Globally-Distributed Database"
3. "Bigtable: A Distributed Storage System"

### Phase 3: Reliability & SRE
1. SRE Book (chapters 6-10)
2. "The Tail at Scale"
3. "Why Do Internet Services Fail?"

### Phase 4: Case Studies
1. High Scalability blog posts
2. GCP case studies
3. Real-world postmortems

