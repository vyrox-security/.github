## What this does

Describe what changed and why in one to three sentences.

## Type of change

- [ ] Bug fix
- [ ] New feature
- [ ] Refactor
- [ ] Documentation only
- [ ] Test coverage
- [ ] Dependency update
- [ ] Security fix

## How to test

1. Describe setup and test data.
2. Run the relevant test suite with exact commands.
3. Confirm expected behavior and include output summary.

Example commands:

```bash
# Rust repos
cargo test -- --test-threads=1

# Python repos
pytest tests/ -v --tb=short
```

## Security checklist

Required for PRs touching ingestion, worker, proxy, or code that calls EDR APIs.

- [ ] HMAC verification is not weakened by this change
- [ ] Every new action type has a corresponding audit log entry
- [ ] No secrets are hardcoded or logged
- [ ] Rate limiter is not bypassed by this change
- [ ] If this adds a new dependency: I have run cargo audit / pip-audit and there are no known vulnerabilities

## Breaking changes

State explicitly whether this changes the webhook contract, Discord action payload format, or proxy API.

## Linked issues

Closes #

## Notes for reviewers

Add context that is not obvious from the diff.
