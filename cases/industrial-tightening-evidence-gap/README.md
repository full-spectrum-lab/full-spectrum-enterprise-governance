# Industrial Tightening Evidence Gap

> **SYNTHETIC · DESIGNED CASE · NOT PRODUCTION VALIDATED · NO NAMED CUSTOMER**

This public case demonstrates one narrow industrial-governance claim:

> MES reports a station operation as complete, while the authorized read-only tightening feed contains no matching critical tightening result. The Observer should surface an evidence gap for human review; it must not stop the line, change MES, release quality status or write to a PLC.

The scenario is distilled from a project design baseline and uses invented identifiers and timestamps. It is evidence of a reviewable case design, not evidence of deployment at a real factory.

## Why this case is public

The case makes the relationship between the three core components concrete:

| Component | Role in this case |
| --- | --- |
| Protocol | Defines subjects, context, evidence references, output and audit boundaries. |
| Engine | Evaluates normalized facts and emits a deterministic risk interpretation. |
| Observer | Collects authorized read-only facts, preserves evidence, shows uncertainty and routes human review. |

## Files

- [`synthetic-input.json`](./synthetic-input.json): invented MES and tightening facts.
- [`subject-manifest.json`](./subject-manifest.json): bounded identities and capabilities.
- [`profile.json`](./profile.json): designed evaluation rule and decision boundary.
- [`expected-observation.json`](./expected-observation.json): expected normalized observation, not a captured production output.
- [`evidence-manifest.json`](./evidence-manifest.json): evidence and replay expectations.
- [`human-review.md`](./human-review.md): the human decision point and prohibited actions.

## Designed flow

```text
authorized read-only MES fact ─┐
                               ├─ normalize ─ evaluate ─ Observation + Evidence
authorized tightening fact ────┘                         └─ human review
```

The expected state is `ACTION_PROPOSED`, not `RESOLVED` or `CLOSED`. A human reviewer must verify the source systems and decide whether and how to act.

## Acceptance criteria for a future executable version

1. A fixed input produces a canonically equivalent observation and stable reason code.
2. Missing, stale and contradictory source states remain distinguishable from a confirmed defect.
3. Every conclusion links to source facts, adapter/schema/profile/engine versions and a replay capability level.
4. The default integration is read-only and has no production-control credential.
5. Observer failure does not affect MES, QMS, the tightening controller or the production line.
6. Only the customer-controlled review workflow may close the risk.

## Current evidence level

`DESIGNED` only. These JSON files are internally consistent public fixtures, but this package is not yet wired to a released industrial adapter or claimed as a passing Engine/Observer golden case.
