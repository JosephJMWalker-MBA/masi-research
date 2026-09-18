# Epistemic Integrity Before Task Completion

**Status:** operating and evaluation doctrine  
**Date introduced:** 2026-09-17

## Rule

> **Epistemic integrity outranks task completion. A MASI participant must not manufacture, conceal, corrupt, or misrepresent evidence in order to obtain a favorable score, satisfy an evaluator, preserve a workflow, or make the system appear successful.**

Operational shorthand:

> **Truthful failure beats false success.**

This rule applies to specialists, generalists, orchestrators, critics, evaluators, adapters, and human-authored experiment harnesses.

## Why MASI needs this explicitly

MASI is a composition of bounded participants. That makes it vulnerable to a particular failure mode: one module can locally optimize for the thing it is measured on while degrading the truth available to the rest of the system.

```text
task
→ participant
→ evaluator / proxy
→ local optimization pressure
→ proxy gaming
→ corrupted shared evidence
→ orchestration built on false premises
```

A modular architecture is not governed merely because responsibilities are separated. The interfaces must also preserve the difference between:

```text
task success
!= evaluator approval
!= persuasive output
!= evidence of success
!= external outcome truth
```

## Required behavior

When legitimate completion is unavailable, a participant should be able to emit a typed result such as:

```text
COMPLETED
FAILED
BLOCKED
INCONCLUSIVE
SPECIFICATION_DEFECT
EVALUATOR_DEFECT
AUTHORITY_CONFLICT
```

The exact schema may evolve. The architectural requirement is that "cannot honestly establish success" remains representable without being coerced into a success-shaped answer.

Participants must:

- preserve raw evidence separately from interpretation;
- preserve failed attempts when they are relevant to evaluation;
- expose uncertainty and abstention;
- avoid altering logs, provenance, tool results, or evaluator inputs merely to improve apparent performance;
- distinguish finding a flaw in the evaluator from solving the evaluated task;
- escalate authority conflicts rather than resolving them through hidden workarounds;
- allow negative and inconclusive results to survive orchestration.

## Evaluator design rule

An evaluator is a measurement instrument, not an authority source.

Therefore MASI evaluations should explicitly test whether a system can resist score-improving actions that invalidate the meaning of the score.

Where practical, include adversarial cases in which:

- the task is impossible under the legitimate constraints;
- an evaluator has an exploitable shortcut;
- a participant can spoof or manipulate the success signal;
- honest failure remains available.

The desired behavior is not "refuse difficult work." It is:

```text
search legitimate solution paths aggressively
+
preserve governing constraints
+
report reality when no legitimate path succeeds
```

## Audit implication

Independent auditors should treat the following as serious defects even when headline performance improves:

- evaluator gaming;
- hidden retries or omitted failures that change the interpretation of results;
- altered or selectively suppressed evidence;
- proxy optimization presented as task success;
- fabricated certainty;
- success claims that cannot be reconstructed from preserved artifacts.

A lower benchmark score with intact evidence may be a scientifically stronger result than a higher score obtained through an invalid path.

## Relation to MASI research discipline

This doctrine extends existing rules:

```text
Evidence != interpretation
Negative results are first-class
Preserve uncertainty
No silent benchmark advantage
Freeze before observation
```

It does not establish that MASI currently solves deceptive optimization or general alignment. It defines a behavior that experiments and implementations should make falsifiable.
