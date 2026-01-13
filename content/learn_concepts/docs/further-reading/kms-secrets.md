# Further Reading: KMS & Secrets

[Back to Cloud KMS & Secret Management](../03-gcp-core-building-blocks/kms-secrets.md)

---

## Cloud KMS Documentation

**Official Documentation**: [Google Cloud KMS Documentation](https://cloud.google.com/kms/docs)

**Why it matters**: Comprehensive official documentation on Cloud KMS architecture, features, and best practices.

### Key Concepts

**KMS Architecture**:
- Key hierarchy (key rings, keys, versions)
- Hardware Security Modules (HSM)
- Envelope encryption

**Key Management**:
- Key rotation
- Key versioning
- Key access control

**Relevance**: Provides the authoritative reference for Cloud KMS implementation details.

### Recommended Sections

- **KMS Overview**: Understanding KMS concepts
- **Key Management**: Creating and managing keys
- **Envelope Encryption**: Encrypting data with KMS
- **Key Rotation**: Rotating keys securely
- **Security**: Key security and access control

---

## Secret Manager Documentation

**Official Documentation**: [Google Cloud Secret Manager Documentation](https://cloud.google.com/secret-manager/docs)

**Why it matters**: Comprehensive official documentation on Secret Manager features and best practices.

### Key Concepts

**Secret Storage**:
- Secret versions
- Secret access control
- Secret rotation

**Security**:
- Encryption at rest
- Access control (IAM)
- Audit logging

**Relevance**: Provides the authoritative reference for Secret Manager implementation details.

### Recommended Sections

- **Secret Manager Overview**: Understanding Secret Manager concepts
- **Secret Management**: Creating and managing secrets
- **Access Control**: Controlling secret access
- **Secret Rotation**: Rotating secrets securely
- **Security**: Secret security best practices

---

## Google Cloud Architecture Center

**Resource**: [Google Cloud Architecture Center](https://cloud.google.com/architecture)

**Why it matters**: Reference architectures and best practices for KMS and Secret Manager deployments.

### Key Resources

**Security Patterns**:
- Encryption at rest
- Encryption in transit
- Key management patterns

**Compliance Patterns**:
- Regulatory compliance
- Audit and logging
- Key rotation strategies

**Relevance**: Provides real-world architecture examples and best practices.

---

## Additional Resources

### Papers

**"Envelope Encryption"** (Google Cloud Documentation)
- Envelope encryption patterns
- [Link](https://cloud.google.com/kms/docs/envelope-encryption)

### Books

**"Google Cloud Platform in Action"** by JJ Geewax
- Chapter on KMS and Secret Manager
- Security examples and best practices

**"Site Reliability Engineering"** (Google SRE Book)
- Chapter on security
- Real-world security challenges

### Online Resources

**Google Cloud Blog**: [Security Articles](https://cloud.google.com/blog/products/identity-security)
- Latest security features
- Best practices and case studies

**GCP Well-Architected Framework**: [Security](https://cloud.google.com/architecture/framework/security)
- Security best practices
- Design principles

---

## Key Takeaways

1. **Envelope encryption**: Encrypt data with DEK, protect DEK with KEK
2. **Key rotation**: Rotate keys regularly for security
3. **HSM protection**: Keys stored in HSM, never leave HSM
4. **Access control**: Use IAM to control key and secret access
5. **Audit everything**: Log all key and secret access

---

## Related Topics

- [IAM Evaluation](../03-gcp-core-building-blocks/iam-evaluation.md) - Access control
- [Multi-Region API](../06-case-studies/multi-region-api.md) - Security in multi-region deployments

