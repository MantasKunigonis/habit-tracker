# Security Policy

## Supported Versions
The 'main' branch is maintained by MantasKunigonis.

## Reporting Vulnerabilities
If you discover a security vulnerability, please use GitHub's private report feature to report it.

## Known Security Concerns
- Feature: user registration | Concern: weak passwords, email enumeration | Mitigation: enforce strong password policy, generic errors
- Feature: login/auth | Concern: brute force, session hijacking | Mitigation: rate limiting, secure cookies, token expiration
- Feature: habit creation/update | Concern: injection | Mitigation: input sanitization/validation
- Feature: API routes | Concern: unauthorized access | Mitigation: require authentication
