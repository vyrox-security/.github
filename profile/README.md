![Vyrox Security Banner](vyrox-security.png)

<p align="center">
  <img src="https://img.shields.io/badge/status-alpha-red?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/containment-human%20approved%20only-black?style=for-the-badge" alt="Containment policy">
  <img src="https://img.shields.io/badge/automation-judged%20by%20people%2C%20not%20mood-cyan?style=for-the-badge" alt="Automation policy">
  <img src="https://img.shields.io/badge/alerts-processed%20with%20extreme%20suspicion-orange?style=for-the-badge" alt="Alerts policy">
</p>

<p align="center">
</p>

## What It Does
Vyrox is the action layer that sits between your EDR and your team. It reads the alert queue, squints at it, acts on the real threats, and writes down exactly what it did so you can prove it later. It still asks a human before touching anything dangerous.

```
[EDR Alert] --> [Ingest] --> [Heuristics] --> [LLM triage] --> [Human Approval] --> [Action] --> [Audit]
```

1. **Ingest** - CrowdStrike, SentinelOne, Microsoft Defender, and a generic JSON adapter all arrive like they pay rent here.
2. **Triage** - Deterministic heuristics handle most of the obvious nonsense.
3. **Escalate** - Ambiguous cases get a second opinion from the LLM.
4. **Approve** - HIGH/CRITICAL alerts surface with enough context to make a sane decision.
5. **Execute** - Approved actions hit the hardened Rust proxy, because chaos deserves guardrails.
6. **Prove** - Every action lands in a SHA-256 hash-chained, tamper-evident audit log you own. The boring slide that wins the audit.

The important bit: **no autonomous containment** today. A human approves before anything gets isolated, killed, or dramatically overreacted to. Autonomy is opt-in and on the roadmap, never a default.

## Repositories

| Repo | Description | License | Stars |
|------|-------------|---------|-------|
| [vyrox-proxy](https://github.com/vyrox-security/vyrox-proxy) | Rust containment proxy for the important kind of panic | MIT | ![vyrox-proxy stars](https://img.shields.io/github/stars/vyrox-security/vyrox-proxy?style=flat-square) |
| [vyrox-docs](https://github.com/vyrox-security/vyrox-docs) | Architecture docs for the stuff everyone pretends not to read | Proprietary | ![vyrox-docs stars](https://img.shields.io/github/stars/vyrox-security/vyrox-docs?style=flat-square) |
| [vyrox-simulator](https://github.com/vyrox-security/vyrox-simulator) | Alert simulation, because production is a terrible place to improvise | Proprietary | ![vyrox-simulator stars](https://img.shields.io/github/stars/vyrox-security/vyrox-simulator?style=flat-square) |
| [vyrox-landing](https://github.com/vyrox-security/vyrox-landing) | Public marketing site with just enough polish to be dangerous | Proprietary | ![vyrox-landing stars](https://img.shields.io/github/stars/vyrox-security/vyrox-landing?style=flat-square) |

## Why Open Core

The proxy is MIT because if software can isolate a production host, the public should at least be able to audit the melodrama.

The heuristics stay proprietary because that is the actual product, and shipping detection logic publicly would be a very generous gift to the other team.

## Quick Links

- Website: [vyrox.dev](https://vyrox.dev)
- Security issues: security@vyrox.dev
- PGP key: [vyrox.dev/.well-known/pgp-key.txt](https://vyrox.dev/.well-known/pgp-key.txt)
- Report vulnerabilities: [SECURITY.md](https://github.com/vyrox-security/.github/blob/main/SECURITY.md)

## Status

Alpha. Breaking things. Moving fast. Wearing a hard hat.

Recently shipped: multi-EDR ingestion (CrowdStrike, SentinelOne, Microsoft Defender, generic JSON), a SHA-256 hash-chained tamper-evident audit log, and an MIT-licensed Rust containment proxy you can read in an afternoon.


<!-- contributors start -->
## Contributors
<!-- auto-generated; do not edit -->
<table><tr>
  <td align="center"><a href="https://github.com/keirsalterego"><img src="https://avatars.githubusercontent.com/u/121482214?v=4&s=80" width="80px;" alt="keirsalterego"/><br /><sub><b>keirsalterego</b></sub></a></td>
</tr></table>

<sub>Total unique contributors: 1</sub>

<!-- contributors end -->

---

Built for analysts who deserve real signal, not 300 false positives per shift.
