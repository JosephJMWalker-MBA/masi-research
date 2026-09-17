# Experiments

MASI experiments should be small, precommitted, reproducible, and capable of producing negative results.

## Naming

Use:

```text
MASI-E###
```

Examples:

- `MASI-E001` — first learned-specialization experiment
- `MASI-E002` — next independently scoped experiment

Do not encode success claims into experiment names.

## Required protocol fields

Each experiment should define before final evaluation:

1. **Research question**
2. **Hypothesis**
3. **Why this matters to MASI**
4. **Systems / conditions compared**
5. **Dataset / fixture identity**
6. **Train / validation / test split logic**, if applicable
7. **Metrics**
8. **Resource accounting**
9. **Success conditions**
10. **Falsifiers / failure conditions**
11. **Known confounds**
12. **Publication / licensing constraints**
13. **Reproduction procedure**

## Experiment lifecycle

```text
question
  ↓
prior-art check
  ↓
protocol freeze
  ↓
implementation
  ↓
preflight
  ↓
execution
  ↓
evidence preservation
  ↓
interpretation
  ↓
replication / challenge
  ↓
revision or next experiment
```

## Result classes

Use explicit result language:

- `supported`
- `not_supported`
- `inconclusive`
- `halted`
- `invalidated`

Do not rename a failed result as a successful "exploration" after the fact.

## MASI-E001 candidate

**Working title:** Empathy semantic-observation specialist

**Question:** Can a small locally specialized model infer a bounded evidence-grounded observation vector more reliably than the same untuned local base model, and how does it compare with a larger general-purpose baseline?

The first candidate substrate is ADCP-style conversational observation because the downstream policy can remain deterministic while the learned model is evaluated only on semantic observation.

Before implementation, E001 still requires:

- a frozen target observation schema;
- an independent labeling procedure that avoids simply encoding known thresholds;
- dataset provenance and privacy rules;
- negative and boundary cases;
- model-family selection;
- resource limits suitable for local execution;
- a scoring plan that distinguishes exact observation recovery from downstream stage agreement;
- a decision on whether any external comparator's performance may legally be published.

No training should begin until those decisions are durable.
