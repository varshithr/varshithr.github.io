# Answer Key: Cloud Storage

[Back to Exercises](../../03-gcp-core-building-blocks/cloud-storage.md#exercises)

---

## Exercise 1: Design Storage Strategy

**Question**: Design storage strategy for a media application. What storage classes? What lifecycle policies?

### Answer

**Goal**: Design cost-effective storage strategy for media files with different access patterns.

### Storage Strategy

**1. Frequently Accessed Media (Recent Uploads)**

**Storage Class**: **Standard Storage**

**Use case**: Recently uploaded media (last 30 days)

**Characteristics**:
- High availability (99.99%)
- Low latency (< 100ms)
- Frequently accessed

**Lifecycle**: No transition (stay in Standard)

**2. Occasionally Accessed Media (Older Content)**

**Storage Class**: **Nearline Storage**

**Use case**: Media older than 30 days, accessed monthly

**Characteristics**:
- Lower cost (~50% cheaper)
- Still low latency
- Accessed less frequently

**Lifecycle**: Transition from Standard after 30 days

**3. Rarely Accessed Media (Archive)**

**Storage Class**: **Coldline Storage**

**Use case**: Media older than 90 days, accessed quarterly

**Characteristics**:
- Lower cost (~70% cheaper)
- Still low latency
- Accessed rarely

**Lifecycle**: Transition from Nearline after 90 days

**4. Long-Term Archive**

**Storage Class**: **Archive Storage**

**Use case**: Media older than 365 days, accessed annually

**Characteristics**:
- Lowest cost (~80% cheaper)
- Higher latency (hours for retrieval)
- Accessed very rarely

**Lifecycle**: Transition from Coldline after 365 days

### Lifecycle Policy

```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
        "condition": {"age": 30}
      },
      {
        "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
        "condition": {"age": 90}
      },
      {
        "action": {"type": "SetStorageClass", "storageClass": "ARCHIVE"},
        "condition": {"age": 365}
      }
    ]
  }
}
```

### Cost Optimization

**Estimated Monthly Costs** (for 1TB storage):

- **Standard** (30 days): 100GB × $0.020 = $2.00
- **Nearline** (60 days): 200GB × $0.010 = $2.00
- **Coldline** (275 days): 500GB × $0.004 = $2.00
- **Archive** (365+ days): 200GB × $0.0012 = $0.24
- **Total**: ~$6.24/month (vs $20/month for all Standard)

**Savings**: ~70% cost reduction

### Answer

**Storage Classes**:
1. **Standard**: Recent media (0-30 days)
2. **Nearline**: Older media (30-90 days)
3. **Coldline**: Archive media (90-365 days)
4. **Archive**: Long-term archive (365+ days)

**Lifecycle Policy**:
- Transition to Nearline after 30 days
- Transition to Coldline after 90 days
- Transition to Archive after 365 days

**Key principles**:
- **Match access patterns**: Use storage classes matching access frequency
- **Automatic transitions**: Use lifecycle policies for automatic transitions
- **Cost optimization**: Significant cost savings with lifecycle management
- **Performance**: Maintain low latency for frequently accessed content

---

## Exercise 2: Handle Consistency

**Question**: Your application needs strong consistency for reads. How do you achieve this with Cloud Storage?

### Answer

**Goal**: Achieve strong consistency for Cloud Storage reads.

### Consistency Model

**Cloud Storage Consistency**:
- **Metadata**: Strongly consistent (immediately visible)
- **Object data**: Eventually consistent (may see stale data briefly)

### Solutions

**1. Use Metadata for Consistency**

**Strategy**: Use object metadata to ensure consistency

**Example**:
```python
# Write with metadata
object.metadata = {'version': 'v2', 'timestamp': '2024-01-01T10:00:00Z'}
object.upload_from_file(file)

# Read with metadata check
object.reload()
if object.metadata['version'] == 'v2':
    # Use this version
    data = object.download_as_bytes()
```

**How it works**:
- Metadata is strongly consistent
- Check metadata before reading
- Ensures reading latest version

**2. Use Object Versioning**

**Strategy**: Use object versioning for consistency

**Example**:
```python
# Enable versioning on bucket
bucket.versioning_enabled = True

# Read specific version
object = bucket.get_blob('file.txt', generation=1234567890)
data = object.download_as_bytes()
```

**How it works**:
- Versioning creates new version on each update
- Read specific version (strongly consistent)
- Track versions in application

**3. Use Generation Numbers**

**Strategy**: Use generation numbers for consistency

**Example**:
```python
# Write and get generation
object.upload_from_file(file)
generation = object.generation

# Read with generation check
object.reload()
if object.generation == generation:
    # This is the latest version
    data = object.download_as_bytes()
```

**How it works**:
- Generation number increments on each update
- Check generation before reading
- Ensures reading latest version

**4. Use Conditional Reads**

**Strategy**: Use conditional reads with generation

**Example**:
```python
# Read if generation matches
try:
    object = bucket.get_blob('file.txt', if_generation_match=generation)
    data = object.download_as_bytes()
except NotFound:
    # Generation mismatch, retry
    pass
```

**How it works**:
- Conditional read fails if generation doesn't match
- Retry if generation mismatch
- Ensures reading expected version

**5. Use Cache Control**

**Strategy**: Use cache control headers

**Example**:
```python
# Set cache control
object.cache_control = 'no-cache, no-store, must-revalidate'
object.upload_from_file(file)
```

**How it works**:
- Prevents caching at CDN/proxy
- Forces fresh reads
- Reduces stale data risk

### Best Practices

**1. Use Metadata for Version Tracking**:
- Store version in metadata
- Check metadata before reading
- Ensures consistency

**2. Use Object Versioning for Critical Data**:
- Enable versioning for important objects
- Read specific versions
- Track versions in application

**3. Implement Retry Logic**:
- Retry reads if generation mismatch
- Exponential backoff
- Handle eventual consistency

**4. Use Conditional Reads**:
- Use `if_generation_match` for conditional reads
- Fail fast if version mismatch
- Retry with updated generation

**5. Monitor Consistency**:
- Monitor read consistency
- Track generation mismatches
- Alert on consistency issues

### Answer

**Achieve Strong Consistency**:

1. **Use Object Versioning**:
   - Enable versioning on bucket
   - Read specific versions (strongly consistent)
   - Track versions in application

2. **Use Generation Numbers**:
   - Check generation before reading
   - Ensure reading latest version
   - Retry if generation mismatch

3. **Use Conditional Reads**:
   - Use `if_generation_match` for conditional reads
   - Fail fast if version mismatch
   - Retry with updated generation

4. **Use Metadata**:
   - Store version in metadata (strongly consistent)
   - Check metadata before reading
   - Ensures reading latest version

**Key principles**:
- **Versioning**: Use object versioning for critical data
- **Generation checks**: Check generation before reading
- **Conditional reads**: Use conditional reads for consistency
- **Retry logic**: Implement retry logic for eventual consistency
- **Monitor**: Monitor consistency and alert on issues

---

## Exercise 3: Optimize Costs

**Question**: Your storage costs are high. How do you optimize costs while maintaining performance?

### Answer

**Goal**: Reduce Cloud Storage costs while maintaining acceptable performance.

### Cost Optimization Strategies

**1. Use Lifecycle Management**

**Strategy**: Automatically transition objects to cheaper storage classes

**Example**:
```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
        "condition": {"age": 30}
      },
      {
        "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
        "condition": {"age": 90}
      }
    ]
  }
}
```

**Savings**: 50-80% cost reduction for older objects

**2. Optimize Storage Classes**

**Strategy**: Use appropriate storage classes for access patterns

**Analysis**:
- **Standard**: Frequently accessed (last 30 days)
- **Nearline**: Accessed monthly (30-90 days)
- **Coldline**: Accessed quarterly (90-365 days)
- **Archive**: Accessed annually (365+ days)

**Savings**: Match storage class to access pattern

**3. Compress Objects**

**Strategy**: Compress objects before upload

**Example**:
```python
import gzip

# Compress before upload
with gzip.open('file.txt.gz', 'wb') as f:
    f.write(data)

object.upload_from_filename('file.txt.gz')
```

**Savings**: 50-90% storage reduction (depending on content)

**4. Delete Unused Objects**

**Strategy**: Delete old or unused objects

**Example**:
```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "Delete"},
        "condition": {"age": 2555}  # 7 years
      }
    ]
  }
}
```

**Savings**: Eliminate storage costs for unused objects

**5. Optimize Object Size**

**Strategy**: Optimize object size for efficiency

**Best practices**:
- **Large objects**: Better for storage efficiency
- **Small objects**: More overhead, higher cost
- **Optimal size**: 1-10 MB per object

**Savings**: Reduce overhead costs

**6. Use Regional Storage**

**Strategy**: Use regional storage instead of multi-region

**Comparison**:
- **Multi-region**: Higher cost, higher availability
- **Regional**: Lower cost, regional availability

**Savings**: 20-30% cost reduction

**7. Monitor and Analyze**

**Strategy**: Monitor storage usage and costs

**Tools**:
- Cloud Storage usage reports
- Cost analysis tools
- Storage class breakdown

**Actions**:
- Identify high-cost buckets
- Analyze access patterns
- Optimize storage classes

### Cost Optimization Plan

**Phase 1: Immediate (No Code Changes)**

1. **Enable Lifecycle Management**:
   - Transition to Nearline after 30 days
   - Transition to Coldline after 90 days
   - Delete after 7 years

2. **Review Storage Classes**:
   - Identify objects in wrong storage class
   - Manually transition if needed

3. **Delete Unused Objects**:
   - Identify unused objects
   - Delete or archive

**Phase 2: Short-term (Code Changes)**

1. **Implement Compression**:
   - Compress objects before upload
   - Decompress on read

2. **Optimize Object Size**:
   - Combine small objects
   - Optimize upload patterns

3. **Use Regional Storage**:
   - Use regional storage where appropriate
   - Multi-region only for critical data

**Phase 3: Long-term (Architecture Changes)**

1. **Implement Tiering**:
   - Automatic tiering based on access patterns
   - Monitor and adjust

2. **Optimize Access Patterns**:
   - Cache frequently accessed objects
   - Reduce unnecessary reads

3. **Cost Monitoring**:
   - Set up cost alerts
   - Regular cost reviews

### Answer

**Optimize Costs**:

1. **Use Lifecycle Management**:
   - Automatically transition to cheaper storage classes
   - Delete old objects
   - 50-80% cost reduction

2. **Optimize Storage Classes**:
   - Match storage class to access pattern
   - Use Nearline/Coldline/Archive for older data
   - Significant cost savings

3. **Compress Objects**:
   - Compress before upload
   - 50-90% storage reduction

4. **Delete Unused Objects**:
   - Remove old or unused objects
   - Eliminate unnecessary storage costs

5. **Use Regional Storage**:
   - Use regional instead of multi-region where appropriate
   - 20-30% cost reduction

6. **Monitor and Analyze**:
   - Track storage usage and costs
   - Identify optimization opportunities

**Key principles**:
- **Lifecycle management**: Automatically transition objects
- **Right storage class**: Match storage class to access pattern
- **Compression**: Reduce storage size
- **Cleanup**: Delete unused objects
- **Monitor**: Track costs and optimize continuously

