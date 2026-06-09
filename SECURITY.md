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

- The LLM model returning a low-quality verdict (this is a triage-quality matter, not a vulnerability)
- Notifier UI quality complaints
- Any scenario requiring physical server access

## Disclosure Policy

Vyrox follows coordinated disclosure. We will credit reporters in release notes unless anonymity is requested.

There are no bounty payouts during alpha.

## Known Limitations

- The LLM triage path runs under a configurable daily token budget; once it is exhausted, alerts fall back to a conservative deterministic verdict.
- The pilot single-writer datastore is not sized for sustained very-high alert volume per tenant; the platform moves to a horizontally scalable store before that becomes a constraint.

These are known system limits, not security vulnerabilities.
