# Ecommerce Knowledge-Source Adapter Spec v0.1

This document defines a first public draft for the knowledge inputs commonly needed when inspecting ecommerce AI customer-service dialogues.

It is not a complete production contract. It is an engineering anchor for case design, field mapping, and adapter development.

## 1. Why this adapter exists

Ecommerce customer-service risk is usually not caused by dialogue text alone.

The same sentence can be safe or risky depending on:

- platform rules;
- merchant policy;
- product policy;
- order status;
- coupon or promotion state;
- available authority;
- previous turns in the conversation.

This adapter spec helps structure those knowledge sources.

## 2. Recommended source groups

### A. Platform rule source

Typical fields:

- `platform_name`
- `refund_rule_version`
- `after_sales_rule_version`
- `sla_rule_version`
- `prohibited_commitment_rules`
- `platform_dispute_escalation_rule`

### B. Merchant rule source

Typical fields:

- `merchant_id`
- `merchant_refund_policy`
- `merchant_compensation_policy`
- `merchant_exception_policy`
- `merchant_manual_review_required_rules`
- `merchant_supported_actions`

### C. Product knowledge source

Typical fields:

- `product_id`
- `category`
- `returnable`
- `warranty_scope`
- `delivery_promise`
- `special_restrictions`
- `inventory_relevant_notes`

### D. Order state source

Typical fields:

- `order_id`
- `payment_status`
- `shipment_status`
- `delivery_status`
- `sign_status`
- `after_sales_status`
- `refund_request_status`
- `dispute_status`

### E. Promotion / coupon source

Typical fields:

- `coupon_id`
- `coupon_type`
- `coupon_validity`
- `coupon_recoverable`
- `promotion_binding_constraints`
- `compensation_overlap_rules`

### F. Customer-service dialogue source

Typical fields:

- `dialogue_id`
- `turn_id`
- `speaker_role`
- `speaker_id`
- `message_text`
- `timestamp`
- `channel`
- `detected_commitment`
- `detected_emotion_state`

### G. Authority / action source

Typical fields:

- `agent_role`
- `declared_capabilities`
- `max_refund_scope`
- `can_issue_coupon`
- `can_trigger_escalation`
- `requires_human_review`

## 3. Minimal public mapping requirement

For a first public or internal trial, the minimum useful set is:

- dialogue content;
- order state;
- merchant rule;
- authority declaration;
- detected commitment or promise.

Everything else can be layered in later.

## 4. Common conflict types

This adapter is meant to support at least the following conflict classes:

- semantic conflict
- authority conflict
- rule conflict
- state conflict
- responsibility gap
- trust degradation
- human-review trigger conflict

## 5. Public boundary

This spec does not require:

- real production customer data;
- direct platform integration;
- full replacement of QA systems;
- a global Full Spectrum network connection.

It can be used locally for:

- synthetic case construction;
- desensitized batch inspection;
- adapter prototyping;
- field-contract discussion between business and engineering teams.

## 6. Suggested next engineering artifacts

This v0.1 spec can later expand into:

- JSON request contract;
- adapter field-mapping template;
- validation sample set;
- case-specific scenario packs;
- benchmark datasets for multi-turn ecommerce inspection.
