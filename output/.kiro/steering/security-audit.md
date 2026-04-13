---
inclusion: auto
name: security-audit
description: Security review checklist for code changes. Use when reviewing PRs, handling user input, authentication, or working with sensitive data.
---

# Security Audit Standards

## OWASP Top 10 Checklist

### 1. Injection
- [ ] Parameterized queries for all SQL operations
- [ ] No string concatenation in queries or commands
- [ ] Input sanitization at all boundaries

### 2. Broken Authentication
- [ ] Secure password hashing (bcrypt, Argon2)
- [ ] Rate limiting on auth endpoints
- [ ] JWT with proper expiration and refresh tokens

### 3. Sensitive Data Exposure
- [ ] No secrets in source control
- [ ] HTTPS enforced
- [ ] PII encrypted at rest

### 4. XML External Entities (XXE)
- [ ] XML parsing with external entities disabled
- [ ] Use JSON instead of XML when possible

### 5. Broken Access Control
- [ ] Authorization checks on all endpoints
- [ ] RBAC or ABAC properly implemented
- [ ] No IDOR vulnerabilities

### 6. Security Misconfiguration
- [ ] Default credentials removed
- [ ] Error messages don't leak stack traces
- [ ] CORS properly configured

### 7. XSS
- [ ] Output encoding for all user-generated content
- [ ] CSP headers configured
- [ ] No `dangerouslySetInnerHTML` without sanitization

### 8. Insecure Deserialization
- [ ] No deserialization of untrusted data
- [ ] Use DTOs with explicit properties

### 9. Known Vulnerabilities
- [ ] Dependencies up to date
- [ ] `dotnet audit` / `npm audit` clean

### 10. Insufficient Logging
- [ ] Auth events logged
- [ ] No sensitive data in logs
- [ ] Structured logging (Serilog, Winston)
