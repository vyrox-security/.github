# Contributing to Vyrox Repositories

## Before You Open a PR

Vyrox is in alpha and pre-revenue. We are building for correctness before convenience, and we review accordingly. Bug reports and issue writeups are welcome from anyone.

Code contributions to the Rust proxy are welcome, but they require security review before merge. Changes to security-critical paths are intentionally slower to merge than docs or tests.

If you want the easiest path to contribute useful code, start with the simulator repository. New attack simulation scripts and fixture quality improvements provide immediate value without touching live action execution paths.

## Development Setup

Clone the target repository:

```bash
# Clone the repository you want to contribute to
git clone https://github.com/vyrox-security/<repo>.git
cd <repo>
```

Set up environment variables from the example file:

```bash
# Copy environment template for local development
cp .env.example .env
```

Python repositories:

```bash
# Install Python dependencies including development tooling
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"

# Run lint and type checks
ruff check .
mypy . --strict

# Run tests
pytest -v --tb=short
```

Rust repositories:

```bash
# Install and lock dependencies
cargo build --locked

# Run tests, lint, formatting, and security audit
cargo test -- --test-threads=1
cargo clippy -- -D warnings
cargo fmt -- --check
cargo audit
```

## Opening an Issue

Use the issue templates in `.github/ISSUE_TEMPLATE/` and choose either Bug Report or Feature Request based on what you are reporting. Fill in commands, versions, and logs so maintainers can reproduce the problem.

Do not open security vulnerabilities as GitHub issues. Report them through SECURITY.md.

## Opening a Pull Request

Use `.github/PULL_REQUEST_TEMPLATE.md` and complete every relevant checkbox. Every pull request must include a test that covers the changed code path.

For `vyrox-proxy`, any pull request touching HMAC verification, rate limiting, or action dispatching must be reviewed by a Vyrox core maintainer before merge. There are no exceptions.

## Code Style

Rust:

- Use `rustfmt` and pass `cargo fmt -- --check`
- Pass `cargo clippy -- -D warnings`
- Do not add `unsafe` blocks without documented security justification
- Do not use `unwrap()` in production paths

Python:

- Use `ruff` for linting
- Pass `mypy . --strict`
- Do not use bare `except` clauses

All repositories:

- Use Conventional Commits: `feat`, `fix`, `docs`, `test`, `chore`
- Do not use vague commit messages such as `stuff`, `misc`, or `updates`

## Adding a New Action Type

This section applies to `vyrox-proxy` contributions.

Any new action type requires:

1. A short security review document describing abuse paths and mitigations.
2. A test proving the audit log entry is written before any EDR API call.
3. Approval from two `@vyrox-security/proxy-maintainers` reviewers.

If one of those is missing, the PR is not mergeable.

## What We Will Not Merge

- `unsafe` Rust blocks without a security justification document.
- Changes that disable or weaken HMAC verification.
- New EDR action types without audit-log coverage.
- Documentation-only pull requests that do not correct a documented inaccuracy.