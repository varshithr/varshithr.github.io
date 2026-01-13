# Answer Key: KMS & Secrets

[Back to Exercises](../../03-gcp-core-building-blocks/kms-secrets.md#exercises)

---

## Exercise 1: Design Key Management

**Question**: Design a key management strategy for a multi-tenant application. What keys? How is rotation handled?

### Answer

**Goal**: Design secure key management for multi-tenant application.

### Key Management Strategy

**Key Hierarchy**:
- **Key Ring**: `multi-tenant-app` (regional)
- **Keys**: 
  - `tenant-data-key`: Encrypt tenant data
  - `api-key`: Encrypt API keys
  - `secrets-key`: Encrypt secrets

**Rotation**:
- Automatic rotation every 90 days
- Support multiple key versions during rotation
- Re-encrypt data with new key versions

**Answer**: Use separate keys per use case, enable automatic rotation, support multiple versions during rotation.

---

## Exercise 2: Handle Key Compromise

**Question**: A key is compromised. How do you respond? What's the recovery strategy?

### Answer

**Recovery steps**:

1. **Rotate Immediately**: Create new key version, promote to primary
2. **Re-encrypt Data**: Re-encrypt all data encrypted with compromised key
3. **Revoke Access**: Revoke IAM access to compromised key
4. **Investigate**: Investigate how key was compromised
5. **Audit**: Review all key usage logs

**Answer**: Rotate key immediately, re-encrypt data, revoke access, investigate compromise, audit key usage.

---

## Exercise 3: Optimize Performance

**Question**: Your application has high KMS latency. How do you optimize it? What's the strategy?

### Answer

**Optimization strategies**:

1. **Use Envelope Encryption**: Encrypt data with DEK, protect DEK with KMS
2. **Cache Keys**: Cache decrypted DEKs (securely)
3. **Batch Operations**: Batch KMS operations where possible
4. **Regional Keys**: Use regional keys for lower latency

**Answer**: Use envelope encryption, cache keys securely, batch operations, use regional keys for lower latency.

