# Further Reading: IAM Evaluation Model

[Back to IAM Evaluation](../03-gcp-core-building-blocks/iam-evaluation.md)

---

## GCP IAM Documentation

**Official Documentation**: [Google Cloud IAM Documentation](https://cloud.google.com/iam/docs)

**Why it matters**: Comprehensive official documentation on GCP IAM architecture, policies, and best practices.

### Key Concepts

**IAM Fundamentals**:
- How IAM works in GCP
- Policy evaluation process
- Resource hierarchy

**Best Practices**:
- Principle of least privilege
- Service accounts
- Workload Identity

**Relevance**: Provides the authoritative reference for GCP IAM implementation.

### Recommended Sections

- **IAM Overview**: Understanding IAM concepts
- **Service Accounts**: Using service accounts
- **Workload Identity**: GKE workload identity
- **IAM Best Practices**: Security best practices
- **Troubleshooting**: Debugging IAM issues

---

## BeyondCorp: A New Approach to Enterprise Security

**Paper**: [BeyondCorp: A New Approach to Enterprise Security](https://research.google/pubs/pub43231/)

**Why it matters**: Google's approach to zero-trust security, which heavily relies on IAM principles.

### Key Concepts

**Zero-Trust Model**:
- No implicit trust based on network location
- Every access request is verified
- Access based on identity and context

**IAM Role**:
- Central to zero-trust architecture
- Identity verification for all access
- Context-aware authorization

**Relevance**: Explains the philosophy behind Google's IAM approach and why it matters.

### Key Excerpts

**On zero-trust**:

> "BeyondCorp moves access controls from the network perimeter to individual devices and users. Access is granted based on what we know about the user and their device, not their network location."

**Key insight**: IAM is central to zero-trust security. Every access decision is based on identity and context, not network location.

---

## GCP IAM Best Practices

**Documentation**: [IAM Best Practices](https://cloud.google.com/iam/docs/using-iam-securely)

**Why it matters**: Google's recommended practices for using IAM securely.

### Key Practices

**1. Principle of Least Privilege**
- Grant minimum necessary permissions
- Regular access reviews
- Remove unused permissions

**2. Use Service Accounts**
- Use service accounts for applications
- Don't use user accounts for services
- Rotate service account keys

**3. Workload Identity**
- Use Workload Identity for GKE
- Don't store service account keys in pods
- Better security and auditability

**4. Regular Audits**
- Review IAM policies regularly
- Monitor access patterns
- Alert on policy changes

**Relevance**: Provides concrete best practices for implementing IAM securely.

---

## Workload Identity

**Documentation**: [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)

**Why it matters**: Modern approach to service account authentication in GKE, replacing service account keys.

### Key Concepts

**How It Works**:
1. Kubernetes service account (KSA) mapped to GCP service account (GSA)
2. Pod uses KSA
3. GKE authenticates pod as GSA
4. Pod accesses GCP resources as GSA

**Benefits**:
- No service account keys to manage
- Better security (keys can't be leaked)
- Better auditability
- Automatic key rotation

**Relevance**: Explains the modern, secure way to authenticate GKE workloads.

---

## Additional Resources

### Papers

**"BeyondCorp"** (Google Research)
- Zero-trust security model
- [Link](https://research.google/pubs/pub43231/)

### Books

**"Google Cloud Platform in Action"** by JJ Geewax
- Chapter on IAM
- Service accounts and workload identity

**"Site Reliability Engineering"** (Google SRE Book)
- Chapter on security
- IAM in production systems

### Online Resources

**Google Cloud Blog**: [Security Articles](https://cloud.google.com/blog/products/identity-security)
- Latest security features
- Best practices

**GCP Well-Architected Framework**: [Security](https://cloud.google.com/architecture/framework/security)
- Security best practices
- IAM design principles

---

## Key Takeaways

1. **IAM is fundamental**: Central to security in GCP
2. **Least privilege**: Grant minimum necessary permissions
3. **Service accounts**: Use for applications, not user accounts
4. **Workload Identity**: Modern, secure approach for GKE
5. **Regular audits**: Review and monitor IAM policies

---

## Related Topics

- [VPC, LB & DNS](../03-gcp-core-building-blocks/vpc-lb-dns.md) - Network security
- [KMS & Secrets](../03-gcp-core-building-blocks/kms-secrets.md) - Secret management
- [Multi-Region API](../06-case-studies/multi-region-api.md) - IAM in practice

