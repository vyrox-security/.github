# Security Policy

## Supported Versions

| Version | Supported |
| --- | --- |
| v0.1.0 | Yes |
| < v0.1.0 | No |

Versions prior to `v0.1.0` are not supported and should not be deployed.

## Reporting a Vulnerability

Do not open a public GitHub issue for security reports.

Email: `security@vyrox.dev`

Subject line format:

```text
SECURITY: <brief description>
```

Response SLA:

- Acknowledgement within 48 hours
- Initial triage within 7 days
- Patch timeline communicated within 14 days

PGP key available at https://vyrox.dev/.well-known/pgp-key.txt.

## Scope

In scope:

- HMAC bypass
- Rate limiter bypass
- Audit log tampering
- Action execution without approval
- Authentication weaknesses in the proxy
- SQL injection in the worker

Out of scope:

- OpenRouter free-tier model hallucinating a verdict
- Discord bot UI quality complaints
- Any scenario requiring physical server access

## Disclosure Policy

Vyrox follows coordinated disclosure. We will credit reporters in release notes unless anonymity is requested.

There are no bounty payouts during alpha.

## Known Limitations

- OpenRouter free tier has a 20k token/day cap. This is an operational constraint.
- SQLite single-writer behavior is not suitable above roughly 50k alerts/day per tenant.

These are known system limits, not security vulnerabilities.
