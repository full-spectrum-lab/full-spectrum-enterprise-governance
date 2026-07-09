# Local Trial Case Pack

This guide defines the smallest public case pack an enterprise can use to try Full Spectrum governance locally.

It is designed for organizations that want to:

- test the method before large deployment;
- avoid external network dependency;
- keep ownership, data control, and execution authority inside the enterprise;
- evaluate whether Full Spectrum surfaces risks that ordinary QA or rule checks do not show clearly.

---

## 1. Purpose

The local trial case pack is not a production rollout kit.

It is a structured starter package for one enterprise team to answer:

> If we run a local governance engine on a small set of cases, do we see meaningful risk, responsibility, or boundary signals?

This means the first goal is not scale.  
The first goal is signal quality.

---

## 2. What the pack should contain

A minimal public local trial pack should contain four parts:

1. **input samples**
2. **inspection contract samples**
3. **review artifacts**
4. **business interpretation notes**

### 2.1 Input samples

Recommended first sample types:

- synthetic dialogue samples;
- desensitized historical dialogue samples;
- reconstructed conflict cases based on known business patterns.

Typical fields:

- conversation id;
- turn id and turn order;
- speaker role;
- user message;
- AI reply;
- business state snapshot;
- authority or permission context;
- scenario tags.

### 2.2 Inspection contract samples

The local trial pack should align with the FSHI inspection contract:

- request sample;
- response sample;
- RiskAlert sample;
- AuditTrace sample.

These artifacts help the enterprise understand what the engine consumes and what it emits without immediately touching production workflows.

### 2.3 Review artifacts

The pack should include review-facing outputs such as:

- a minimal markdown governance report;
- a human review form;
- a simple audit summary;
- a redaction guide.

### 2.4 Business interpretation notes

The pack should explain:

- why the case matters;
- what ordinary QA might miss;
- what specific boundary or responsibility issue is being tested;
- what a business reviewer is expected to decide after reading the output.

---

## 3. Recommended first scenario bundle

The first local trial pack should stay narrow.

Recommended bundle:

### Bundle A: customer-service over-commitment

Tests whether AI:

- promises something it cannot execute;
- uses soothing language that functions like a commitment;
- crosses the line between response convenience and authority.

### Bundle B: knowledge-source conflict

Tests whether AI:

- mixes platform rule, merchant rule, product rule, and order state incorrectly;
- cites the wrong authority source;
- produces an answer with missing responsibility ownership.

### Bundle C: human review trigger

Tests whether the governance flow:

- escalates at the right moment;
- pauses rather than over-automates;
- produces a concise trace that humans can actually use.

---

## 4. Recommended directory shape

One practical directory shape is:

```text
trial-pack/
  inputs/
    desensitized-dialogue-001.json
    desensitized-dialogue-002.json
  contracts/
    request.sample.json
    response.sample.json
    risk-alert.sample.json
    audit-trace.sample.json
  reports/
    minimal-report.example.md
    human-review-form.md
  notes/
    scenario-intent.md
    field-mapping-notes.md
    redaction-notes.md
```

This repository already contains pieces of that pack in:

- [`examples/fshi-api-contract/`](../examples/fshi-api-contract/)
- [`templates/`](../templates/)
- [`cases/`](../cases/)

---

## 5. How an enterprise should use the pack

### Step 1: start offline

Begin with offline batch review, not embedded production interception.

### Step 2: map only the minimum fields

Do not spend weeks modeling every business object first.

Map only:

- dialogue turns;
- role labels;
- core order or case state;
- authority boundary;
- commitment signal.

### Step 3: inspect for one type of failure

Choose one failure type first:

- over-commitment;
- boundary crossing;
- authority mismatch;
- multi-turn hidden escalation.

### Step 4: review with mixed roles

A useful first review group usually includes:

- one business owner;
- one QA or operations reviewer;
- one compliance or risk reviewer;
- one product or AI owner.

### Step 5: decide whether the signal is worth another round

Do not ask whether the pack “solves AI governance.”

Ask:

- did it reveal a real blind spot?
- was the result understandable?
- was the review burden reasonable?
- should we refine the field mapping and try a second cycle?

---

## 6. What the local trial pack does not assume

The local trial pack does not require:

- joining a Full Spectrum protocol network;
- external guardian review;
- public node certification;
- replacing customer-service systems;
- replacing the enterprise’s own execution authority.

This is a local-first trial path.

---

## 7. Relationship to the wider ecosystem

The local trial pack sits between repositories like this:

| Repository | Role in a first trial |
| --- | --- |
| `full-spectrum-engine` | runs the local governance logic |
| `full-spectrum-enterprise-governance` | provides case packs, templates, and enterprise interpretation |
| `full-spectrum-protocol` | defines schemas, RFCs, and contract semantics |
| `full-spectrum-commons` | provides ecosystem maps and public orientation |

---

## 8. Suggested public success criterion

The local trial pack is successful if an enterprise team can say:

> We did not need to replace our system, join a public network, or expose sensitive data, but we were still able to test a governance workflow and judge whether it adds value.

That is the point of the first pack.
