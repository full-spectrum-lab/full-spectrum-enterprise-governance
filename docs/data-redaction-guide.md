# Data Redaction Guide

Public examples in this repository should use synthetic or desensitized data.

## Remove or replace

- user names
- phone numbers
- addresses
- order numbers tied to real customers
- merchant identifiers when disclosure is not authorized
- internal ticket ids that can be traced back to private systems
- screenshots containing real account data

## Keep only what governance needs

Prefer preserving:

- turn order
- state changes
- authority conflicts
- evidence gaps
- promise wording
- escalation wording
- review trigger conditions

## Redaction rule

The purpose of a public case is not to expose private facts.

The purpose is to preserve governance structure:

```text
what happened
why it became risky
what should have been reviewed
how responsibility should be explained
```
