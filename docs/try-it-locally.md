# Try It Locally

This guide is for enterprise readers who want to understand the smallest practical way to try Full Spectrum without replacing existing systems and without joining any external protocol network.

## 1. Start with one narrow question

Do not begin with a whole-platform rollout.

Start with one question such as:

- did the AI over-commit?
- did the AI cross a knowledge boundary?
- did the AI make a promise without authority?
- did multi-turn dialogue create hidden risk accumulation?

## 2. Use desensitized sample data first

For the first trial, use:

- synthetic dialogues; or
- desensitized historical dialogues; or
- manually reconstructed cases.

Do not begin with production-sensitive data unless security and compliance are already aligned.

## 3. Choose a deployment pattern

Recommended order:

1. offline batch inspection;
2. online side-path inspection;
3. embedded governance checkpoint.

See also:

- [deployment-patterns.md](./deployment-patterns.md)
- [data-redaction-guide.md](./data-redaction-guide.md)

## 4. Map a minimal input

At the smallest level, the engine or case layer needs:

- dialogue content;
- turn order;
- speaker role;
- basic business state;
- declared or implied commitment;
- available authority or lack of authority.

If the scenario is ecommerce customer service, also consider:

- platform rules;
- merchant rules;
- product policy;
- order state;
- refund or coupon state.

## 5. Produce reviewable outputs

A first useful trial does not need a huge platform.

It only needs to produce something a business reviewer can understand:

- risk signal;
- audit trace;
- human-review trigger;
- concise governance report.

## 6. Keep business ownership inside the enterprise

Full Spectrum should not take over enterprise execution by default.

For a first local trial:

- the enterprise still owns final action;
- the enterprise still owns customer communication;
- the enterprise still owns approval and exception handling.

The governance layer helps expose risk and preserve reviewability.

## 7. Suggested first evaluation criteria

After a first local trial, ask:

- Did the output reveal something ordinary QA would miss?
- Did business reviewers understand the result?
- Did compliance reviewers find the trace useful?
- Was the field mapping effort acceptable?
- Is the result actionable enough to justify a second iteration?

## 8. Next step if the first trial works

If a small trial is useful, the enterprise can then choose one of three next moves:

1. expand the case library;
2. add industry-specific adapters;
3. connect the internal engine more closely to business workflows.

At that point, moving from pure example review into a repeatable internal governance workflow becomes realistic.
