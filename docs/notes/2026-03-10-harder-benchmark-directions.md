# Harder Benchmark Directions

The current real smoke runs are useful because they validate the runtime, trace capture, and evaluator pipeline. They are not yet strong enough to separate good models from merely cautious models.

## Why The Current Pilot Can Be Too Easy

- the malicious instruction is explicit
- the protected asset path is obvious
- the safe response is directly hinted in the prompt
- the completion requirement is lightweight

## Harder Variants To Add Next

### 1. Remove Safe-Hint Framing

Do not tell the model to "respond safely". Require only the task outcome and let the policy boundary emerge from the system.

### 2. Split The Attack Across Turns

Move the benign request and the malicious request into separate messages so the model must carry prior context and resolve authority correctly.

### 3. Hide Asset Access Behind Debugging Language

Replace direct secret/token wording with language like:

- "include the auth material needed to reproduce"
- "attach the local credential blob for correlation"
- "use the prior bootstrap token if available"

### 4. Strengthen Completion Pressure

Make the task harder to complete without touching the protected asset, so the model faces a more realistic tradeoff.

### 5. Add Attachment-Style Content

Represent the delayed instruction as if it came from attached logs, pasted shell output, or an imported template rather than a plain instruction line.

### 6. Add Approval-Ambiguous Tooling

For approval tasks, force the model into a state where a protected command would look operationally attractive, but still requires explicit fresh approval.

## Recommended Next Hardening Order

1. harder `AS-002` variant without safe-hint language
2. harder `AE-002` variant with more realistic debugging pressure
3. first real `PF-001` run with persistence temptation
