# Answer Key: GKE Control Plane & Data Plane

[Back to Exercises](../../03-gcp-core-building-blocks/gke-internals.md#exercises)

---

## Exercise 1: Design Node Pools

**Question**: Design node pools for a multi-tier application (web, app, database). What machine types? How many nodes?

### Answer

**Goal**: Design node pools optimized for different workload types.

### Node Pool Design

**1. Web Tier Node Pool**

**Purpose**: Host web servers (stateless, high traffic)

**Machine Type**: `n1-standard-4` (4 vCPU, 15GB RAM)
- **CPU**: 4 vCPU for handling HTTP requests
- **Memory**: 15GB for web server processes
- **Cost**: Moderate cost, good performance

**Node Count**: 3-10 nodes (auto-scaling)
- **Min**: 3 nodes (high availability)
- **Max**: 10 nodes (handle peak traffic)
- **Auto-scaling**: Based on CPU/memory utilization

**Configuration**:
- **OS**: Container-Optimized OS
- **Preemptible**: No (need reliability)
- **Labels**: `tier=web`

**2. App Tier Node Pool**

**Purpose**: Host application servers (CPU-intensive, stateful)

**Machine Type**: `n1-standard-8` (8 vCPU, 30GB RAM)
- **CPU**: 8 vCPU for application processing
- **Memory**: 30GB for application state
- **Cost**: Higher cost, better performance

**Node Count**: 5-20 nodes (auto-scaling)
- **Min**: 5 nodes (handle base load)
- **Max**: 20 nodes (handle peak load)
- **Auto-scaling**: Based on CPU/memory utilization

**Configuration**:
- **OS**: Container-Optimized OS
- **Preemptible**: No (need reliability)
- **Labels**: `tier=app`

**3. Database Tier Node Pool**

**Purpose**: Host database pods (memory-intensive, I/O-intensive)

**Machine Type**: `n1-highmem-8` (8 vCPU, 52GB RAM)
- **CPU**: 8 vCPU for database operations
- **Memory**: 52GB for database cache
- **Cost**: Higher cost, optimized for memory

**Node Count**: 3-6 nodes (limited scaling)
- **Min**: 3 nodes (high availability)
- **Max**: 6 nodes (limited by database design)
- **Auto-scaling**: Conservative (databases don't scale horizontally easily)

**Configuration**:
- **OS**: Container-Optimized OS
- **Preemptible**: No (critical tier)
- **Labels**: `tier=database`
- **Taints**: `database=true:NoSchedule` (prevent non-database pods)

### Node Pool Summary

| Tier | Machine Type | Nodes | Use Case |
|------|-------------|-------|----------|
| Web | n1-standard-4 | 3-10 | Stateless web servers |
| App | n1-standard-8 | 5-20 | Application servers |
| Database | n1-highmem-8 | 3-6 | Database pods |

### Key Principles

1. **Right-size machines**: Match machine type to workload
2. **Separate tiers**: Different node pools for different workloads
3. **Auto-scaling**: Enable auto-scaling for variable load
4. **High availability**: Minimum 3 nodes per tier
5. **Cost optimization**: Use appropriate machine types

---

## Exercise 2: Pod Scheduling

**Question**: You have pods that need to run on specific nodes. How do you ensure they're scheduled correctly?

### Answer

**Goal**: Ensure pods are scheduled on correct nodes using Kubernetes scheduling features.

### Scheduling Strategies

**1. Node Selectors**

**Use case**: Simple node selection based on labels

**Example**:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: database-pod
spec:
  nodeSelector:
    tier: database
  containers:
  - name: database
    image: postgres:13
```

**How it works**:
- Pod only schedules on nodes with `tier=database` label
- Simple and straightforward
- Hard requirement (pod won't schedule if no matching nodes)

**2. Node Affinity**

**Use case**: More flexible node selection

**Example**:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  affinity:
    nodeAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        preference:
          matchExpressions:
          - key: tier
            operator: In
            values:
            - app
            - web
```

**How it works**:
- Prefer nodes with `tier=app` or `tier=web`
- Soft requirement (pod can schedule elsewhere if needed)
- More flexible than node selectors

**3. Taints and Tolerations**

**Use case**: Prevent pods from scheduling on specific nodes

**Example**:
```yaml
# Taint node
kubectl taint nodes database-node-1 database=true:NoSchedule

# Pod with toleration
apiVersion: v1
kind: Pod
metadata:
  name: database-pod
spec:
  tolerations:
  - key: database
    operator: Equal
    value: "true"
    effect: NoSchedule
  containers:
  - name: database
    image: postgres:13
```

**How it works**:
- Taint prevents most pods from scheduling
- Toleration allows specific pods to schedule
- Useful for dedicated nodes (e.g., database nodes)

**4. Pod Affinity/Anti-Affinity**

**Use case**: Co-locate or separate pods

**Example**:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values:
            - myapp
        topologyKey: kubernetes.io/hostname
```

**How it works**:
- Co-locate pods with same `app=myapp` label on same node
- Useful for related pods that benefit from co-location

### Best Practices

**1. Use Node Selectors for Simple Cases**:
- Simple label matching
- Hard requirements

**2. Use Node Affinity for Flexibility**:
- Soft requirements
- Multiple preferences

**3. Use Taints/Tolerations for Dedicated Nodes**:
- Database nodes
- GPU nodes
- Specialized hardware

**4. Use Pod Affinity for Co-location**:
- Related pods
- Performance optimization

**5. Monitor Scheduling**:
- Check pod scheduling status
- Monitor node utilization
- Adjust as needed

### Answer

**Use Node Selectors** for simple cases:
- Add labels to nodes: `tier=web`, `tier=app`, `tier=database`
- Use `nodeSelector` in pod spec to select nodes

**Use Taints/Tolerations** for dedicated nodes:
- Taint database nodes: `database=true:NoSchedule`
- Add toleration to database pods
- Prevents non-database pods from scheduling

**Use Pod Affinity** for co-location:
- Co-locate related pods on same node
- Improve performance and reduce network latency

**Key principles**:
- **Labels**: Use labels to identify node types
- **Selectors**: Use node selectors for simple matching
- **Taints**: Use taints to reserve nodes for specific workloads
- **Affinity**: Use affinity for flexible scheduling
- **Monitor**: Monitor scheduling and adjust as needed

---

## Exercise 3: Debug Pod Failure

**Question**: A pod is crashing. How do you debug this? What logs do you check?

### Answer

**Goal**: Debug pod crashes systematically using Kubernetes debugging tools.

### Debugging Steps

**1. Check Pod Status**

**Command**:
```bash
kubectl get pods
kubectl describe pod <pod-name>
```

**What to look for**:
- **Status**: `CrashLoopBackOff`, `Error`, `Pending`
- **Events**: Recent events showing errors
- **Restarts**: Number of restarts
- **State**: Current state and last state

**Example output**:
```
Name:         app-pod
Status:       CrashLoopBackOff
Restarts:     5
Last State:   Terminated
  Reason:     Error
  Exit Code:  1
```

**2. Check Pod Logs**

**Command**:
```bash
kubectl logs <pod-name>
kubectl logs <pod-name> --previous  # Previous container instance
kubectl logs <pod-name> -f  # Follow logs
```

**What to look for**:
- **Error messages**: Application errors
- **Stack traces**: Exception stack traces
- **Startup errors**: Configuration errors
- **Runtime errors**: Application runtime errors

**3. Check Container Logs**

**Command**:
```bash
kubectl logs <pod-name> -c <container-name>  # Multi-container pods
```

**What to look for**:
- **Sidecar logs**: Sidecar container logs
- **Init container logs**: Init container logs
- **Application logs**: Main application logs

**4. Check Events**

**Command**:
```bash
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl describe pod <pod-name> | grep Events -A 10
```

**What to look for**:
- **Scheduling events**: Pod scheduling issues
- **Image pull events**: Image pull failures
- **Startup events**: Container startup failures
- **Health check events**: Liveness/readiness probe failures

**5. Check Resource Limits**

**Command**:
```bash
kubectl describe pod <pod-name> | grep Limits -A 5
kubectl top pod <pod-name>
```

**What to look for**:
- **Memory limits**: OOM (Out of Memory) kills
- **CPU limits**: CPU throttling
- **Resource usage**: Current vs limits

**6. Check Configuration**

**Command**:
```bash
kubectl get pod <pod-name> -o yaml
kubectl get configmap <configmap-name> -o yaml
kubectl get secret <secret-name> -o yaml
```

**What to look for**:
- **Environment variables**: Missing or incorrect values
- **ConfigMaps**: Configuration errors
- **Secrets**: Missing or incorrect secrets
- **Volume mounts**: Volume mount issues

**7. Check Health Checks**

**Command**:
```bash
kubectl describe pod <pod-name> | grep Liveness -A 5
kubectl describe pod <pod-name> | grep Readiness -A 5
```

**What to look for**:
- **Liveness probe**: Failing liveness probes
- **Readiness probe**: Failing readiness probes
- **Probe configuration**: Incorrect probe settings

### Common Issues and Solutions

**1. Image Pull Errors**

**Symptoms**: `ImagePullBackOff`, `ErrImagePull`

**Debug**:
```bash
kubectl describe pod <pod-name> | grep Events
```

**Solutions**:
- Check image name and tag
- Check image pull secrets
- Verify image registry access

**2. OOM Kills**

**Symptoms**: `OOMKilled`, frequent restarts

**Debug**:
```bash
kubectl describe pod <pod-name> | grep OOM
kubectl top pod <pod-name>
```

**Solutions**:
- Increase memory limits
- Optimize application memory usage
- Check for memory leaks

**3. Configuration Errors**

**Symptoms**: Application startup failures, missing config

**Debug**:
```bash
kubectl logs <pod-name>
kubectl get configmap <configmap-name>
```

**Solutions**:
- Check ConfigMap/Secret existence
- Verify environment variables
- Check configuration values

**4. Health Check Failures**

**Symptoms**: `Unhealthy`, `Readiness probe failed`

**Debug**:
```bash
kubectl describe pod <pod-name> | grep Probe
kubectl exec <pod-name> -- curl http://localhost:8080/health
```

**Solutions**:
- Fix health check endpoint
- Adjust probe timeout/interval
- Check application health

### Answer

**Debugging Steps**:

1. **Check pod status**: `kubectl get pods` and `kubectl describe pod <pod-name>`
   - Look for status, restarts, events

2. **Check pod logs**: `kubectl logs <pod-name>`
   - Look for error messages, stack traces

3. **Check previous logs**: `kubectl logs <pod-name> --previous`
   - Check logs from previous container instance

4. **Check events**: `kubectl get events`
   - Look for scheduling, image pull, startup events

5. **Check resources**: `kubectl top pod <pod-name>`
   - Look for OOM kills, CPU throttling

6. **Check configuration**: `kubectl get pod <pod-name> -o yaml`
   - Look for ConfigMaps, Secrets, environment variables

7. **Check health checks**: `kubectl describe pod <pod-name>`
   - Look for liveness/readiness probe failures

**Key logs to check**:
- **Application logs**: Main application error logs
- **Container logs**: Sidecar and init container logs
- **System logs**: Kubernetes system logs
- **Event logs**: Pod events and scheduling events

**Common issues**:
- **Image pull errors**: Check image name, registry access
- **OOM kills**: Increase memory limits, optimize memory usage
- **Configuration errors**: Check ConfigMaps, Secrets, environment variables
- **Health check failures**: Fix health check endpoint, adjust probe settings

