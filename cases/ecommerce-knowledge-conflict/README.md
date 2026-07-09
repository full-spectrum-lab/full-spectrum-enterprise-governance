# Case: Ecommerce Knowledge-Source Conflict

## Summary

An ecommerce AI customer-service system responds in a scenario where multiple knowledge sources are relevant at the same time:

- platform rules
- merchant rules
- product knowledge
- order state
- user escalation state
- customer-service wording

These sources do not fully agree, and the AI output crosses from explanation into commitment.

## Governance question

How should the enterprise detect and surface conflicts between knowledge sources before they collapse into a user-facing trust problem?

## Why this case matters

Single-turn quality checks usually miss:

- state conflict across turns
- semantic conflict across rule sources
- hidden authority mismatch
- responsibility gaps between platform, merchant, and operations teams

## Desired governance result

The case should help the enterprise answer:

- what conflicted
- who was affected
- which authority boundary was crossed
- whether human review should have been triggered
- what should later be corrected in prompts, rules, or knowledge-source mapping
