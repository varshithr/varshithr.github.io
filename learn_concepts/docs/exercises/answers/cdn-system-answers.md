# Answer Key: CDN System

[Back to Exercises](../../06-case-studies/cdn-system.md#exercises)

---

## Exercise 1: Design Improvements

**Question**: How would you improve this design? What tradeoffs?

### Answer

**Potential improvements**:

1. **Add More Edge Locations**: Increase edge coverage
2. **Implement Cache Warming**: Pre-warm cache for popular content
3. **Add Analytics**: Enhanced analytics and monitoring
4. **Optimize Compression**: Better compression algorithms

**Tradeoffs**:
- Higher cost vs better performance
- More complexity vs simpler architecture
- More maintenance vs better features

**Answer**: Add more edge locations, implement cache warming, enhance analytics, optimize compression. Balance cost vs performance.

---

## Exercise 2: Handle Cache Invalidation

**Question**: How do you handle cache invalidation for frequently updated content?

### Answer

**Cache invalidation strategies**:

1. **Versioned URLs**: Use versioned URLs (e.g., `/v1/image.jpg`)
2. **Selective Invalidation**: Invalidate only changed content
3. **TTL Optimization**: Use appropriate TTL for content type
4. **Cache Tags**: Use cache tags for grouped invalidation

**Answer**: Use versioned URLs, invalidate selectively, optimize TTL, use cache tags for grouped invalidation.

---

## Exercise 3: Optimize Costs

**Question**: How would you reduce costs by 30%? What tradeoffs?

### Answer

**Cost optimization strategies**:

1. **Optimize Cache Hit Rate**: Increase cache hit rate to reduce origin load
2. **Use Regional Storage**: Use regional instead of multi-region storage
3. **Optimize Compression**: Better compression to reduce bandwidth
4. **Reduce Origin Load**: Cache more content, reduce origin requests

**Tradeoffs**:
- Lower cache hit rate vs cost savings
- Less redundancy vs cost reduction
- More optimization effort vs cost savings

**Answer**: Optimize cache hit rate, use regional storage, optimize compression, reduce origin load. Balance cost vs performance.

