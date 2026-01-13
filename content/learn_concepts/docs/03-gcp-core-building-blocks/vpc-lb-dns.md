# VPC, Load Balancing & DNS

**One-line summary**: How requests flow through GCP networking: VPC routing, load balancer selection, and DNS resolution.

**Prerequisites**: Basic networking concepts (IP addresses, subnets, routing), [Foundations](../01-foundations/README.md).

---

## Mental Model

### Request Flow

```mermaid
flowchart LR
    Client[Client] --> DNS[DNS Resolution]
    DNS --> LB[Load Balancer]
    LB --> VPC[VPC Routing]
    VPC --> VM[VM/Instance]
    
    style DNS fill:#99ccff
    style LB fill:#ffcc99
    style VPC fill:#99ff99
```

**Key insight**: Every request goes through DNS → Load Balancer → VPC → Instance. Understanding each layer is critical for debugging and design.

### VPC Architecture

**VPC (Virtual Private Cloud)**: Logically isolated network in GCP.

**Components**:
- **Subnets**: IP address ranges within VPC
- **Routes**: How traffic is routed
- **Firewall rules**: What traffic is allowed
- **Peering**: Connecting VPCs

---

## Internals & Architecture

### VPC Deep Dive

#### Subnets

**Regional subnets**: Span all zones in a region.

**IP ranges**: CIDR blocks (e.g., 10.0.0.0/16).

**Private vs public**: 
- **Private**: No external IP, use NAT gateway
- **Public**: External IP, direct internet access

#### Routes

**Route table**: Determines where traffic goes.

**Default routes**:
- **Default internet gateway**: Routes to internet
- **Default VPC peering**: Routes to peered VPCs
- **Default subnet routes**: Routes within subnet

**Custom routes**: 
- **Static routes**: Manual routing rules
- **Dynamic routes**: BGP routes (for VPN/Interconnect)

#### Firewall Rules

**Firewall rules**: Control what traffic is allowed.

**Components**:
- **Direction**: Ingress (inbound) or egress (outbound)
- **Source/Destination**: IP ranges, tags, service accounts
- **Protocol/Port**: TCP, UDP, ICMP, specific ports
- **Action**: Allow or deny
- **Priority**: Lower number = higher priority

**Default rules**:
- **Default allow egress**: All outbound traffic allowed
- **Default deny ingress**: All inbound traffic denied (unless allowed)

#### VPC Peering

**VPC peering**: Connect VPCs for private communication.

**Types**:
- **Private peering**: Within same project
- **Cross-project peering**: Across projects
- **Cross-organization peering**: Across organizations

**Limitations**:
- No transitive peering (A→B→C doesn't work)
- IP ranges must not overlap

### Load Balancing

#### Load Balancer Types

**1. Global Load Balancer (HTTP(S))**
- **Use case**: HTTP/HTTPS traffic
- **Features**: SSL termination, content-based routing, CDN integration
- **Scope**: Global (anywhere → any region)

**2. Global Load Balancer (TCP/SSL)**
- **Use case**: TCP/SSL traffic
- **Features**: SSL passthrough, TCP proxy
- **Scope**: Global

**3. Regional Load Balancer (Internal)**
- **Use case**: Internal traffic within region
- **Features**: Private IP only, lower latency
- **Scope**: Regional

**4. Network Load Balancer**
- **Use case**: Non-HTTP traffic, high performance
- **Features**: Pass-through, preserves client IP
- **Scope**: Regional

#### Load Balancing Algorithms

**HTTP(S) Load Balancer**:
- **Least connections**: Route to backend with fewest connections
- **Round robin**: Distribute evenly
- **Geographic**: Route based on client location

**Network Load Balancer**:
- **5-tuple hash**: Hash on (src IP, src port, dst IP, dst port, protocol)
- **Consistent**: Same client → same backend (session affinity)

#### Health Checks

**Health checks**: Determine if backends are healthy.

**Types**:
- **HTTP**: Check HTTP endpoint (e.g., /health)
- **HTTPS**: Check HTTPS endpoint
- **TCP**: Check TCP port
- **SSL**: Check SSL handshake

**Configuration**:
- **Interval**: How often to check (e.g., 10s)
- **Timeout**: How long to wait (e.g., 5s)
- **Healthy threshold**: Consecutive successes needed (e.g., 2)
- **Unhealthy threshold**: Consecutive failures needed (e.g., 3)

### DNS Resolution

#### DNS Architecture

**Cloud DNS**: GCP's DNS service.

**Components**:
- **Zones**: DNS namespaces (e.g., example.com)
- **Records**: DNS records (A, AAAA, CNAME, etc.)
- **Policies**: Routing policies (geolocation, weighted, etc.)

#### DNS Resolution Flow

1. **Client queries DNS**: Resolves domain name to IP
2. **DNS resolver**: Checks cache, queries authoritative DNS
3. **Authoritative DNS**: Returns IP address
4. **Client connects**: Uses IP to connect to load balancer

#### DNS Caching

**TTL (Time To Live)**: How long DNS records are cached.

**Tradeoffs**:
- **Short TTL**: Faster updates, more DNS queries
- **Long TTL**: Fewer queries, slower updates

**Recommendation**: Use short TTL (60s) for production, longer for static resources.

---

## Failure Modes & Blast Radius

### VPC Failures

#### Scenario 1: Misconfigured Firewall Rules
- **Impact**: Traffic blocked, services unreachable
- **Blast radius**: Entire VPC or specific services
- **Detection**: Monitoring, health checks fail
- **Recovery**: Fix firewall rules, verify connectivity

#### Scenario 2: Subnet Exhaustion
- **Impact**: Can't create new instances
- **Blast radius**: New deployments fail
- **Detection**: Instance creation failures
- **Recovery**: Expand subnet CIDR or create new subnet

#### Scenario 3: Route Misconfiguration
- **Impact**: Traffic routed incorrectly, services unreachable
- **Blast radius**: Affected routes
- **Detection**: Traffic not reaching destinations
- **Recovery**: Fix routes, verify routing table

### Load Balancer Failures

#### Scenario 1: All Backends Unhealthy
- **Impact**: No traffic served, service down
- **Blast radius**: Entire service
- **Detection**: Health check failures, error rate spikes
- **Recovery**: Fix backends, verify health checks

#### Scenario 2: Load Balancer Overload
- **Impact**: Increased latency, timeouts
- **Blast radius**: All traffic through load balancer
- **Detection**: Latency metrics, error rate
- **Recovery**: Scale load balancer, add backends

#### Scenario 3: SSL Certificate Expiry
- **Impact**: HTTPS connections fail
- **Blast radius**: All HTTPS traffic
- **Detection**: SSL errors, certificate expiry alerts
- **Recovery**: Renew certificate, update load balancer

### DNS Failures

#### Scenario 1: DNS Resolution Failure
- **Impact**: Can't resolve domain names, services unreachable
- **Blast radius**: All clients using DNS
- **Detection**: DNS query failures, connection failures
- **Recovery**: Check DNS configuration, verify records

#### Scenario 2: DNS Cache Poisoning
- **Impact**: Clients connect to wrong IPs
- **Blast radius**: Affected clients
- **Detection**: Unusual traffic patterns, errors
- **Recovery**: Clear DNS cache, verify DNS records

#### Scenario 3: DNS Propagation Delay
- **Impact**: Some clients see old IPs, some see new
- **Blast radius**: Clients during DNS updates
- **Detection**: Inconsistent connectivity
- **Recovery**: Wait for propagation, use short TTL

### Overload Scenarios

#### 10× Normal Load
- **VPC**: Routes handle load, but may see increased latency
- **Load Balancer**: May need to scale, backends may be overloaded
- **DNS**: DNS queries increase, but usually handles load

#### 100× Normal Load
- **VPC**: Routes may be overwhelmed, packet loss possible
- **Load Balancer**: Likely overloaded, needs scaling
- **DNS**: May need to scale DNS servers

---

## Observability Contract

### Metrics to Track

#### VPC Metrics
- **Packet loss**: Packets dropped
- **Latency**: Network latency between zones
- **Bandwidth**: Network throughput

#### Load Balancer Metrics
- **Request rate**: Requests per second
- **Latency**: P50/P95/P99 latency
- **Error rate**: 4xx/5xx errors
- **Backend health**: Healthy vs unhealthy backends
- **Connection count**: Active connections

#### DNS Metrics
- **Query rate**: DNS queries per second
- **Response time**: DNS resolution latency
- **Error rate**: Failed DNS queries
- **Cache hit rate**: DNS cache effectiveness

### Logs

Log events:
- Firewall rule matches (allow/deny)
- Load balancer access logs
- DNS query logs
- Route changes

### Traces

Trace:
- End-to-end request latency
- DNS resolution time
- Load balancer processing time
- VPC routing time

### Alerts

**Critical alerts**:
- All backends unhealthy
- Load balancer error rate > threshold
- DNS resolution failures
- Firewall blocking legitimate traffic

**Warning alerts**:
- Backend health degrading
- Load balancer latency increasing
- DNS query rate spiking

---

## Change Safety

### VPC Changes

#### Adding Subnets
- **Process**: Create subnet, configure routes
- **Risk**: Low (additive change)
- **Rollback**: Delete subnet

#### Changing Firewall Rules
- **Process**: Update rule, verify connectivity
- **Risk**: Medium (may block traffic)
- **Rollback**: Revert firewall rule

#### VPC Peering
- **Process**: Create peering, configure routes
- **Risk**: Medium (may affect routing)
- **Rollback**: Delete peering

### Load Balancer Changes

#### Adding Backends
- **Process**: Add backend, verify health checks
- **Risk**: Low (additive change)
- **Rollback**: Remove backend

#### Changing Health Checks
- **Process**: Update health check config, monitor
- **Risk**: Medium (may mark healthy backends as unhealthy)
- **Rollback**: Revert health check config

#### SSL Certificate Updates
- **Process**: Upload new certificate, update load balancer
- **Risk**: High (may break HTTPS)
- **Rollback**: Revert certificate

### DNS Changes

#### Updating Records
- **Process**: Update DNS record, wait for propagation
- **Risk**: Medium (may break connectivity)
- **Rollback**: Revert DNS record

#### Changing TTL
- **Process**: Update TTL, wait for cache expiry
- **Risk**: Low (affects caching only)
- **Rollback**: Revert TTL

---

## Security Boundaries

### VPC Security

- **Firewall rules**: Control what traffic is allowed
- **Private IPs**: Use private IPs for internal traffic
- **Service accounts**: Use service accounts for authentication
- **VPC peering**: Limit peering to trusted VPCs

### Load Balancer Security

- **SSL/TLS**: Encrypt traffic in transit
- **WAF**: Use Web Application Firewall for HTTP(S) load balancers
- **DDoS protection**: Built-in DDoS protection
- **Backend security**: Secure backends independently

### DNS Security

- **DNSSEC**: Sign DNS records for authenticity
- **Private zones**: Use private DNS zones for internal services
- **Access control**: Limit who can modify DNS records

---

## Tradeoffs

### VPC Tradeoffs

**Regional vs Zonal**:
- **Regional**: Span multiple zones, more resilient
- **Zonal**: Lower latency, simpler

**Public vs Private**:
- **Public**: Direct internet access, simpler
- **Private**: More secure, requires NAT gateway

### Load Balancer Tradeoffs

**Global vs Regional**:
- **Global**: Lower latency (closer to users), more complex
- **Regional**: Simpler, higher latency for distant users

**HTTP(S) vs Network**:
- **HTTP(S)**: More features (SSL termination, routing), higher latency
- **Network**: Lower latency, fewer features

### DNS Tradeoffs

**Short vs Long TTL**:
- **Short TTL**: Faster updates, more queries
- **Long TTL**: Fewer queries, slower updates

---

## Operational Considerations

### Capacity Planning

**VPC**:
- Plan subnet sizes (don't run out of IPs)
- Plan for VPC peering (IP ranges must not overlap)

**Load Balancer**:
- Plan backend capacity
- Plan for health check overhead

**DNS**:
- Plan for DNS query rate
- Plan for DNS record storage

### Monitoring & Debugging

**VPC**:
- Monitor firewall rule matches
- Monitor route changes
- Monitor network latency

**Load Balancer**:
- Monitor backend health
- Monitor request rate and latency
- Monitor error rate

**DNS**:
- Monitor DNS query rate
- Monitor DNS resolution time
- Monitor DNS errors

### Incident Response

**Common incidents**:
- Services unreachable (firewall, routing)
- Load balancer failures
- DNS resolution failures

**Response**:
1. Check firewall rules
2. Check routes
3. Check load balancer health
4. Check DNS records
5. Verify connectivity

---

## What Staff Engineers Ask in Reviews

### Design Questions
- "What's the VPC architecture?"
- "How is traffic routed?"
- "What's the load balancing strategy?"
- "How is DNS configured?"

### Scale Questions
- "What happens at 10× load?"
- "How does the load balancer scale?"
- "What's the DNS query capacity?"

### Security Questions
- "What firewall rules are in place?"
- "How is traffic encrypted?"
- "Who can modify DNS records?"

### Operational Questions
- "How do we monitor networking?"
- "What alerts do we have?"
- "How do we debug connectivity issues?"

---

## Further Reading

**Comprehensive Guide**: [Further Reading: VPC, Load Balancing & DNS](../further-reading/vpc-lb-dns.md)

**Quick Links**:
- [GCP VPC Documentation](https://cloud.google.com/vpc/docs)
- [GCP Load Balancing Documentation](https://cloud.google.com/load-balancing/docs)
- [GCP Cloud DNS Documentation](https://cloud.google.com/dns/docs)
- [Google Cloud Architecture Center](https://cloud.google.com/architecture)
- [Back to GCP Core Building Blocks](README.md)

---

## Exercises

1. **Design VPC**: Design a VPC for a multi-tier application (web, app, database). What subnets do you need? What firewall rules?

2. **Load balancer selection**: You have an API that needs low latency and high throughput. Do you use HTTP(S) or Network Load Balancer? Why?

3. **DNS strategy**: You're deploying a new service. What DNS TTL do you use? How do you handle DNS updates during deployments?

**Answer Key**: [View Answers](../exercises/answers/vpc-lb-dns-answers.md)

