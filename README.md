# Full Spectrum Enterprise Governance

[![Public case boundary](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/actions/workflows/public-case-check.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/actions/workflows/public-case-check.yml)

Enterprise-facing governance packages, inspection cases, deployment patterns, and human-review workflows for AI customer-service and industrial observation scenarios.

This repository is the business application layer of the Full Spectrum Lab ecosystem.

It focuses on a practical question:

> Once an enterprise AI system is running, who audits the AI, how are risks surfaced, and how does human review re-enter the loop?

## Role in the ecosystem

| Repository | Role |
|---|---|
| `full-spectrum-protocol` | defines schemas, RFCs, boundaries, and governance semantics |
| `full-spectrum-engine` | runs the local-first governance runtime |
| `full-spectrum-enterprise-governance` | translates protocol + runtime into enterprise-facing cases, reports, adapters, and deployment guidance |
| `full-spectrum-commons` | provides shared maps, diagrams, indexes, and public orientation |

## Current focus

The first public scenario cluster is:

- AI customer-service over-commitment
- ecommerce knowledge-source conflict
- non-invasive dialogue inspection
- human review trigger and audit reporting
- a synthetic industrial tightening-evidence gap

## What this repository includes

- business-facing governance cases
- desensitized example inputs
- report templates
- enterprise FAQ and deployment notes
- adapters and field-mapping guidance
- human-review workflow framing

## What this repository does not claim

This repository does not claim:

- production validation for any named company
- legal or regulatory authority
- that all cases are based on real customer data
- that the examples here replace enterprise business systems

Unless explicitly stated otherwise, public case materials are synthetic or desensitized reconstructions for governance design and review.

## Industrial public entry

The first industrial case is intentionally small: [MES reports a critical tightening operation complete while the authorized tightening feed contains no matching result](./cases/industrial-tightening-evidence-gap/README.md).

It is labeled **SYNTHETIC · DESIGNED CASE · NOT PRODUCTION VALIDATED · NO NAMED CUSTOMER**. The package demonstrates the intended evidence and human-review boundary; it is not yet an executable industrial adapter or a claim of factory deployment.

The [public-case boundary gate](./tools/validate_public_cases.py) verifies fixture structure and the read-only/no-writeback safety claims. Passing this gate means `DESIGNED / FIXTURE-VALIDATED`; it does **not** mean the Adapter, Engine path, Observer path or production pilot has been implemented.

## Try the first case

**AI customer-service refund over-commitment**

```text
Input:
AI says: “A full refund can be issued.”

Governance result:
commitment_authorized = false
human_review_required = true
recommended_response = “Current evidence is insufficient. Verify refund authority before making a commitment.”
```

Start from [cases/refund-overcommitment](./cases/refund-overcommitment/README.md), then use [Try It Locally](./docs/try-it-locally.md).

The observer produces warnings, recommendations, reports, and audit references. Any actual order, refund, account, knowledge-base, or production-system update remains an enterprise integration decision and responsibility.

## Evidence boundary

- [Evidence and Project Status](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/evidence-and-status.md)
- [WP-001: Governance Semantics and a Local-First Observer Engine](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/research/working-papers/wp-001-governance-semantics-and-local-observer-engine.md) — working paper, not peer reviewed
- Public cases are not presented as validation for a named enterprise unless an explicit evidence record says otherwise.

## Start here

- [docs/ai-customer-service-governance.md](./docs/ai-customer-service-governance.md)
- [docs/deployment-patterns.md](./docs/deployment-patterns.md)
- [docs/try-it-locally.md](./docs/try-it-locally.md)
- [docs/local-trial-case-pack.md](./docs/local-trial-case-pack.md)
- [docs/ecommerce-knowledge-source-adapter-spec-v0.1.md](./docs/ecommerce-knowledge-source-adapter-spec-v0.1.md)
- [docs/enterprise-faq.md](./docs/enterprise-faq.md)
- [cases/refund-overcommitment/README.md](./cases/refund-overcommitment/README.md)
- [cases/ecommerce-knowledge-conflict/README.md](./cases/ecommerce-knowledge-conflict/README.md)
- [cases/industrial-tightening-evidence-gap/README.md](./cases/industrial-tightening-evidence-gap/README.md)

## Related repositories

- [full-spectrum-protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol)
- [full-spectrum-engine](https://github.com/full-spectrum-lab/full-spectrum-engine)
- [full-spectrum-commons](https://github.com/full-spectrum-lab/full-spectrum-commons)

## License

See [LICENSE](./LICENSE).
