# Answer Key: Capacity Math Cheat Sheet

[Back to Exercises](../../01-foundations/capacity-math.md#exercises)

---

## Exercise 1: Calculate Capacity

**Question**: API with 5,000 QPS, 20ms CPU time per request, 5MB memory per request. How many 8-core, 32GB instances do you need?

### Answer

**Given**:
- QPS = 5,000 requests/second
- CPU time per request = 20ms = 0.02 seconds
- Memory per request = 5MB (peak)
- Instance specs: 8 cores, 32GB RAM

### CPU Calculation

**CPU cores needed**:
- CPU cores = (QPS × CPU time per request) / Target utilization
- CPU cores = (5,000 × 0.02) / 0.7 = 100 / 0.7 = **142.9 cores**

**Instances needed for CPU**:
- Instances = 142.9 / 8 = **17.9 → 18 instances**

### Memory Calculation

**Concurrent requests**:
- Need to estimate concurrent requests
- Concurrent requests ≈ QPS × average latency
- Assuming average latency = 50ms (processing + queueing)
- Concurrent requests = 5,000 × 0.05 = **250 concurrent requests**

**Memory needed**:
- Memory = (Concurrent requests × Memory per request) + Base memory + Cache
- Memory = (250 × 5MB) + 2GB base + 10GB cache
- Memory = 1.25GB + 2GB + 10GB = **13.25GB**

**Instances needed for memory**:
- Instances = 13.25GB / 32GB = **0.41 → 1 instance** (but need redundancy)

**However**: Memory per request is peak, not average. Need to account for:
- Peak concurrent requests may be higher
- Memory overhead per request
- Safety margin

**Revised memory calculation**:
- Peak concurrent requests = 5,000 × 0.1 = 500 (assuming 100ms peak latency)
- Memory = (500 × 5MB) + 2GB + 10GB = 2.5GB + 2GB + 10GB = **14.5GB**
- With 20% safety margin: 14.5GB × 1.2 = **17.4GB**
- Instances = 17.4GB / 32GB = **0.54 → 1 instance** (but need redundancy)

### Final Answer

**CPU is the bottleneck**: Need **18 instances** for CPU capacity

**With redundancy**: Need **20 instances** (18 for capacity + 2 for redundancy)

**Per instance**:
- CPU utilization: (5,000 × 0.02) / (20 × 8) = 100 / 160 = **62.5%** (good headroom)
- Memory utilization: 14.5GB / 32GB = **45%** (good headroom)

**Answer**: **20 instances** (18 for capacity, 2 for redundancy)

**Key insights**:
- CPU is the bottleneck in this case
- Memory is not the constraint
- Need redundancy for high availability
- Good headroom for spikes

---

## Exercise 2: Forecast Growth

**Question**: Current capacity handles 1,000 QPS. Traffic grows 15% per month. What capacity do you need in 12 months?

### Answer

**Given**:
- Current capacity = 1,000 QPS
- Growth rate = 15% per month
- Time = 12 months

### Calculation

**Exponential growth formula**:
- Future capacity = Current capacity × (1 + growth_rate)^time
- Future capacity = 1,000 × (1.15)^12

**Step-by-step**:
- Month 1: 1,000 × 1.15 = 1,150 QPS
- Month 2: 1,150 × 1.15 = 1,322.5 QPS
- Month 3: 1,322.5 × 1.15 = 1,520.9 QPS
- ...
- Month 12: 1,000 × (1.15)^12 = **5,350 QPS**

**Using calculator**:
- (1.15)^12 = 5.35
- Future capacity = 1,000 × 5.35 = **5,350 QPS**

### Capacity Planning

**Current capacity**: 1,000 QPS
**Future capacity**: 5,350 QPS
**Growth factor**: 5.35× (435% increase)

**Capacity needed**: **5,350 QPS** (or plan for 6,000 QPS with headroom)

**Scaling strategy**:
- **Immediate**: Current capacity sufficient
- **6 months**: Need ~2,300 QPS (2.3× current)
- **12 months**: Need ~5,350 QPS (5.35× current)

**Recommendations**:
- Plan for **5× capacity** in 12 months
- Scale gradually (monthly or quarterly)
- Monitor growth rate (may change)
- Add capacity before needed (don't wait until month 12)

**Answer**: **5,350 QPS** in 12 months (5.35× current capacity)

**Key insights**:
- Exponential growth compounds quickly
- 15% monthly = ~435% annual growth
- Need to plan capacity well in advance
- Monitor actual growth vs forecast

---

## Exercise 3: Identify Bottleneck

**Question**: System with 1,000 QPS, CPU at 50%, memory at 90%, disk I/O at 80%. What's the bottleneck?

### Answer

**Given**:
- QPS = 1,000 requests/second
- CPU utilization = 50%
- Memory utilization = 90%
- Disk I/O utilization = 80%

### Analysis

**Bottleneck identification**:
- **CPU**: 50% utilization (not bottleneck, has headroom)
- **Memory**: 90% utilization (**bottleneck**, very high)
- **Disk I/O**: 80% utilization (high, but not critical yet)

### Memory is the Bottleneck

**Why memory is the bottleneck**:
1. **Highest utilization**: 90% is highest among all resources
2. **Close to limit**: Only 10% headroom remaining
3. **Risk of OOM**: High risk of out-of-memory errors
4. **Performance impact**: High memory usage can cause:
   - Garbage collection pauses (in managed languages)
   - Swap usage (if enabled, very slow)
   - OOM kills (process killed by OS)

**Why not CPU**:
- CPU at 50% has plenty of headroom
- Can handle 2× load before saturation
- Not the limiting factor

**Why not disk I/O**:
- Disk I/O at 80% is high but not critical
- Still has 20% headroom
- May become bottleneck if memory issue is fixed

### Recommendations

**Immediate actions**:
1. **Scale up memory**: Add more memory to instances
2. **Scale out**: Add more instances to distribute memory load
3. **Reduce memory usage**: Optimize memory usage per request
4. **Enable swap**: Temporary measure (not recommended for production)

**Long-term actions**:
1. **Memory optimization**: Profile and optimize memory usage
2. **Cache optimization**: Reduce cache size if possible
3. **Memory monitoring**: Set up alerts for memory usage
4. **Capacity planning**: Plan for memory growth

**Answer**: **Memory is the bottleneck** at 90% utilization

**Reasoning**:
- Highest utilization (90% vs 50% CPU, 80% disk I/O)
- Only 10% headroom remaining
- High risk of OOM errors
- Will limit system capacity before other resources

**Actions**:
- Scale up memory or scale out instances
- Optimize memory usage
- Monitor memory closely

