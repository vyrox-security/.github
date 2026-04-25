# Vyrox Community Health

![Licence](https://img.shields.io/badge/licence-proprietary-lightgrey?style=flat-square)
![Build](https://img.shields.io/badge/build-passing-2ea44f?style=flat-square)
![Version](https://img.shields.io/badge/version-v0.1.0--alpha-005cc5?style=flat-square)
![Platform](https://img.shields.io/badge/platform-github-24292f?style=flat-square)
![Funny](https://img.shields.io/badge/incidents-preferably%20in%20daylight-6a737d?style=flat-square)

This repository holds the shared policy, templates, and workflow guardrails used across the public Vyrox repositories, so every bug report, pull request, and security disclosure lands in a format maintainers can actually act on. It exists separately because organisation-wide community health files should have one owner, one history, and one place to audit, especially when the broader product uses an open-core model where public trust is anchored in what security teams can inspect before they let code near production systems.

## Why This Exists

Most broken open-source governance is not malicious. It is just inconsistent. One repo has a sensible PR template, another has none, a third has security guidance that says to open an issue for vulnerabilities, and now everyone has a bad afternoon.

Vyrox spans Rust, Python, infrastructure glue, and docs. That means contribution paths are not identical, but baseline expectations should be. This repo makes sure reporting paths, ownership boundaries, and review standards are coherent, not copied and slightly mutated across six repositories.

This also keeps the social contract explicit. If a change touches a high-risk path such as HMAC verification or action execution controls, review requirements are stricter. That is not bureaucracy. That is what happens when your software can isolate production hosts.

## Architecture

```text
Contributor
	|
	v
Issue / PR template in this repo
	|
	v
Target repo workflow and CODEOWNERS
	|
	+--> Core review path
	|
	+--> Security disclosure path (SECURITY.md)
	|
	v
Merged change with auditable governance trail
```

## Quickstart

Prerequisites:

1. Git
2. Python 3.11+ (for tooling)
3. `yamllint`

1. Clone the repository.

```bash
# Clone the org-level community health repository
git clone https://github.com/vyrox-security/.github.git
cd .github
```

2. Install local validation tooling.

```bash
# Install YAML linter used for issue templates and workflows
python -m pip install --upgrade pip yamllint
```

3. Validate YAML files before opening a PR.

```bash
# Lint issue templates and workflow files
yamllint .github/ISSUE_TEMPLATE .github/workflows
```

4. Check Markdown rendering quickly.

```bash
# Optional: render check with markdownlint if you use it locally
echo "Run your markdown linter of choice here"
```

## Configuration

| Variable | Required | Default | Description |
| --- | --- | --- | --- |
| N/A | No | N/A | This repository has no runtime environment variables. |

## Contributing

Contributions are most useful when they improve reporting quality, tighten security response process documentation, or fix template defects that waste maintainer time. Good bug reports about template friction are welcome, because broken issue forms are a distributed denial-of-service against triage.

Do not propose weakening review gates for sensitive paths, normalising vague issue templates, or adding workflow shortcuts that trade security for convenience. If a change touches ownership boundaries or disclosure process language, expect slower and more careful review.

See CONTRIBUTING.md for full contribution process, style expectations, and merge criteria. This project is in alpha. We are accepting external feedback broadly and code contributions selectively, with security-first review on anything that can affect operational safety.

## Licence

This repository is distributed under Vyrox organisation terms for public community files. See LICENCE in the relevant target repository for component-specific licence terms.

Website: vyrox.dev (coming soon)