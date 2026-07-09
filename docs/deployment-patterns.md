# Deployment Patterns

This repository assumes a non-invasive deployment posture by default.

## Pattern A: Offline batch inspection

The enterprise exports desensitized dialogues or case records on a schedule.

The governance runtime inspects them offline and outputs:

- RiskAlert
- AuditTrace
- report
- optimization suggestions

Use when:

- the enterprise is early in AI adoption
- security review is strict
- runtime integration is not yet approved

## Pattern B: Online side-path inspection

The governance runtime receives a side-path copy of conversation or event streams without directly controlling business execution.

Use when:

- the enterprise wants faster visibility
- business systems should remain unchanged
- human review needs to be triggered in near real time

## Pattern C: Authorized embedded governance checkpoint

The enterprise deliberately places governance checks into its internal AI workflow.

In this pattern, the engine may output:

- review recommended
- do not auto-commit
- boundary conflict detected

But final business action still remains enterprise-owned unless explicitly integrated otherwise.

## Recommended order

For most first-time adopters:

1. start with offline batch inspection
2. validate field mapping and report usefulness
3. move to side-path inspection
4. only then consider embedded checkpoints
