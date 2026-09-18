# Evaluation

MASI evaluation should distinguish architecture effects from model capability, extra inference budget, and favorable task design.

## Minimum comparison logic

Where the experiment permits, compare:

```text
F1  frontier monolith
L1  local monolith
L2  local ensemble / simple aggregation
M1  local MASI composition
```

Later work may add:

```text
F2  frontier model under the same MASI protocol
M2  MASI with dynamic / learned routing
M3  MASI with outcome-grounded influence updates
```

Not every experiment needs every condition, but omitted controls must be explained.

## Primary dimensions

Experiments should define task-specific scoring before final evaluation. Useful dimensions may include:

- correctness / task success;
- hard-constraint satisfaction;
- evidence fidelity;
- unsupported-assumption rate;
- calibration / abstention quality;
- contradiction detection;
- second-order consequence recognition;
- stakeholder-impact coverage;
- appropriate escalation;
- cross-module error correction;
- robustness under perturbation or distribution shift;
- reproducibility.

Avoid vague aggregate labels such as "wisdom" or "alignment" unless they are operationalized for the experiment.

## Resource accounting

Record enough information to distinguish better architecture from simply spending more inference.

Where practical report:

- model identities and sizes;
- quantization;
- number of model calls;
- input/output tokens;
- context supplied to each call;
- wall-clock latency;
- peak memory where locally measurable;
- hardware;
- API cost where allowed;
- number of deliberation / critique passes;
- tool and retrieval access.

A MASI result may still be valuable when it spends more compute, but the tradeoff must be explicit.

## Error-correction accounting

For composed systems, preserve:

- errors introduced by each module;
- errors caught by another module;
- valid claims incorrectly rejected;
- disagreements that remain unresolved;
- disagreements resolved correctly;
- cases where composition makes the final result worse.

Cross-module correction is a candidate MASI mechanism and should be measured directly rather than inferred from final score alone.

## Calibration

Do not label a numeric confidence value as calibrated merely because it falls between 0 and 1.

Calibration claims require an appropriate held-out distribution and a declared metric such as Brier score, log loss, expected calibration error, reliability curves, or another justified method.

Calibration should be interpreted within the task/domain actually measured.

## Data split discipline

For learned-specialization experiments:

1. define train / validation / test logic before final training;
2. prevent near-duplicate leakage across splits;
3. preserve difficult negative controls;
4. include boundary cases where possible;
5. freeze the held-out test set before inspecting final model behavior;
6. keep any later error-analysis set distinct from the original test claim.

## Judge independence

Where scoring cannot be fully deterministic, prefer one or more of:

- blinded human review;
- multiple independent reviewers;
- a frozen rubric;
- a separate model judge that does not know the system identity;
- adjudication of disagreements after independent scoring.

A frontier model should not be treated as ground truth merely because it is stronger than the tested models.

## Publication boundaries

Some external providers restrict publication of benchmark or performance information. Respect those terms.

A restricted external system may still be used privately as a research comparator, but public artifacts should omit prohibited performance data unless written permission or applicable terms clearly allow publication.

## Interpretation

A score difference alone does not establish why MASI worked.

Interpretation should distinguish:

```text
observed performance difference
!=
mechanism established
```

Mechanism claims require additional controls or ablations.

## Historical WP1 evaluation boundary

The [frozen WP1 contract at `81adfff`](https://github.com/JosephJMWalker-MBA/masi-research/blob/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/docs/WP0_WP1_CONTRACT.md) records local support/abstention semantics, raw-output separation and descriptive resource accounting. Its scope is the audited closed candidate set; it is not a thesis freeze or general capability evaluation. The [reconciled results](../experiments/wp1/RESULTS.md) state the current limits. Current [RESEARCH_THESIS.md](RESEARCH_THESIS.md), including H2A/H2B, `C_A/C_B/T` and falsifiers 1–10, governs thesis interpretation. No code or evidence is imported by this crosslink.

Audit E1 is a **next-contract lesson only**: WP1's verifier shares normalization and hashing helpers with the runner, so it is an integrity/drift check rather than independent validation of those helpers. A separately authorized future contract may add an independent reference check. R1–R7 authorize no evaluator repair or new experiment.
