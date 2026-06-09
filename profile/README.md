![Vyrox Security Banner](vyrox-security.png)

<p align="center">
  <img src="https://img.shields.io/badge/status-alpha-red?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/action%20layer-for%20security%20ops-black?style=for-the-badge" alt="Action layer">
  <img src="https://img.shields.io/badge/containment-human%20approved%20by%20default-blue?style=for-the-badge" alt="Containment policy">
  <img src="https://img.shields.io/badge/every%20action-audited%20%26%20provable-2ea44f?style=for-the-badge" alt="Audit policy">
</p>

# Vyrox

**The autonomous, auditable action layer for security operations.**

Detection is solved. Response is not. An alert fires, lands in a queue, and at 2am
nobody is home. When someone does act, no one can reconstruct afterward what was
done or why. Teams bought detection and were left alone with the hard part.

Vyrox acts on the alert and proves it. We triage every EDR alert, take action on the
ones that are real, and write every action to a tamper-evident log the customer owns.

## How it works

```
[EDR alert] -> [Ingest] -> [Heuristics] -> [LLM triage] -> [Decide] -> [Act] -> [Audit]
```

1. **Ingest** - CrowdStrike, SentinelOne, Defender, and a field-mapped generic adapter post alerts to a per-tenant webhook, authenticated with HMAC-SHA256.
2. **Triage** - A deterministic heuristics engine clears the obvious noise in milliseconds. Only the genuinely ambiguous alerts reach an LLM, which writes verdict fields and never executes anything.
3. **Decide** - Human approval by default. Autonomous only where the customer has turned it on and the action is reversible.
4. **Act** - Approved containment runs through a small, hardened Rust proxy: signed, rate-limited, and built to fail closed.
5. **Prove** - Every action lands in a SHA-256 hash-chained audit log the customer owns, ready for an auditor or an insurer.

## Who it is for

Sold MSSP-first: one analyst runs many client tenants from a single console and can
prove every action to each client's auditor. Lean in-house teams that own security but
have no 24/7 SOC come in through the inbound door.

## Open core

The execution proxy is MIT licensed. If a piece of software can isolate a production
host, the people running it should be able to read exactly what it does before they
trust it. The heuristics corpus and the orchestration core stay private: that is the
product, and handing detection logic to attackers helps no one.

## Repositories

| Repo | What it is | License |
|------|-----------|---------|
| [vyrox-proxy](https://github.com/vyrox-security/vyrox-proxy) | Rust containment proxy, the audited execution boundary | MIT |
| [vyrox-docs](https://github.com/vyrox-security/vyrox-docs) | Public architecture, API contracts, threat model, audit-chain spec | Proprietary |
| [vyrox-simulator](https://github.com/vyrox-security/vyrox-simulator) | Deterministic alert simulation for exercising the pipeline | MIT |
| [vyrox-www](https://github.com/vyrox-security/vyrox-www) | Public product site | Proprietary |

## Contact

- Website: [vyrox.dev](https://vyrox.dev)
- General: hello@vyrox.dev
- Security: security@vyrox.dev (see [SECURITY.md](https://github.com/vyrox-security/.github/blob/main/SECURITY.md) and the [PGP key](https://vyrox.dev/.well-known/pgp-key.txt))

## Status

Alpha. Shipping today: the Rust proxy, ingestion, two-stage triage, human-approved
containment, and the SHA-256 audit chain. In active build: the operational console,
graduated autonomy, and the evidence engine.


<!-- contributors start -->
## Contributors
<!-- auto-generated; do not edit -->
<table><tr>
  <td align="center"><a href="https://github.com/keirsalterego"><img src="https://avatars.githubusercontent.com/u/121482214?v=4&s=80" width="80px;" alt="keirsalterego"/><br /><sub><b>keirsalterego</b></sub></a></td>
  <td align="center"><a href="https://github.com/starkalterego"><img src="https://avatars.githubusercontent.com/u/178389306?v=4&s=80" width="80px;" alt="starkalterego"/><br /><sub><b>starkalterego</b></sub></a></td>
</tr></table>

<sub>Total unique contributors: 2</sub>

<!-- contributors end -->

---

Built for analysts who deserve real signal, not 300 false positives a shift.
