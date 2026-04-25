![Ingest](https://img.shields.io/badge/stage-ingest-6a737d?style=flat-square)
![Triage](https://img.shields.io/badge/stage-triage-6a737d?style=flat-square)
![Approve](https://img.shields.io/badge/stage-approve-6a737d?style=flat-square)
![Execute](https://img.shields.io/badge/stage-execute-6a737d?style=flat-square)
![Alert Volume](https://img.shields.io/badge/alerts%2Fshift-300%2B-586069?style=flat-square)

Vyrox builds an autonomous AI SOC analyst that handles noisy alert queues before analysts lose another shift to false positives. The system ingests EDR alerts, applies deterministic heuristics first, escalates ambiguous cases to an LLM triage pass, routes high-risk decisions for human approval in Slack, and executes approved containment actions through a hardened Rust proxy.

The open-core model is deliberate. The code that directly touches EDR execution paths is public and MIT licensed so security teams can audit it under zero-trust assumptions. The private heuristics engine and internal orchestration layers remain proprietary because they encode the operating logic that differentiates signal from noise.

| Repository | What it is | Licence |
| --- | --- | --- |
| `vyrox-proxy` | Rust containment proxy with HMAC verification, rate limits, and audit logging | MIT |
| `vyrox-docs` | Architecture, API references, and security design documentation | Proprietary |
| `vyrox-simulator` | Alert simulation scripts for integration and demo flows | Proprietary |
| `vyrox-landing` | Public website and product narrative | Proprietary |

## The Design Philosophy

1. The proxy is public because trust starts where side effects start. If code can isolate a host, customers should be able to read it.
2. The heuristics are private because detection logic is the moat. Publishing every pattern makes adversary tuning easier.
3. SQLite is intentional for alpha because operational simplicity is a security property when teams are small and pager budgets are smaller.

## Contact

Website: vyrox.dev (coming soon)

Security vulnerabilities: sec.vyrox@proton.me

Everything else: open an issue in the relevant repository.
