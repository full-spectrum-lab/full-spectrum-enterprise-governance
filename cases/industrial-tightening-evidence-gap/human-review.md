# Human Review — SYNTH-R04-001

> **SYNTHETIC · DESIGNED CASE · NOT PRODUCTION VALIDATED**

## Review question

Does the missing tightening result represent delayed data, adapter or identifier-mapping failure, source-system outage, or an actual absence of the required operation?

## Minimum checks

- verify the MES operation and timestamp;
- verify source-system health and the query window;
- verify work-item, station and tool identifier mappings;
- inspect the customer-controlled quality record;
- record which evidence was available and which remained missing;
- decide whether to acknowledge, investigate, resolve, close or reopen the observation.

## Prohibited automated actions

This case must not automatically:

- stop or start a production line;
- write MES/QMS status;
- release or reject quality status;
- send commands to a PLC, robot or tightening controller;
- declare the risk closed;
- upload complete production records outside the customer-controlled environment.

The final business and safety decision belongs to the authorized customer reviewer under the customer's own procedures.
