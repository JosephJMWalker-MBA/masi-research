# Evaluation

MASI evaluation should distinguish architecture effects from model capability, extra inference budget, and favorable task design.

## Minimum comparison logic

Use the claim-linked mandatory contrasts in [RESEARCH_THESIS.md](RESEARCH_THESIS.md#required-controls). Later composed-system experiments include the applicable local conditions; H7 requires all four:

```text
F1  frontier monolith
L1  local monolith
L2  local ensemble / simple aggregation
M1  local MASI composition
```

These additional conditions are required when the corresponding mechanism is claimed:

```text
F2  frontier model under the same MASI protocol
M2  MASI with dynamic / learned routing
M3  MASI with outcome-grounded influence updates
```

Not every experiment needs every condition. A missing claim-critical control narrows or blocks that claim; it cannot be excused after seeing the result. Freeze one primary claim and decision rule, including margins, coverage, uncertainty and multiplicity handling, before final observation.

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

**WP0 minimum:** each future protocol must define the measurement method, units, scope, aggregation and applicable budget caps for the following observations. A run manifest may hold shared metadata; attempt records supply actual use. Record `not applicable`, `not measured` or `unavailable` with a reason instead of dropping a field or inventing zero. An estimate must be labeled with its method; a measured zero must name its scope.

| Observation | Required distinction |
| --- | --- |
| Component/source identity | Exact model/artifact, adapter, normalizer, evaluator and configuration revisions/hashes; parameter count where meaningful, precision/quantization, software environment and known/unknown provider version. |
| Calls and passes | Attempted/completed/failed invocations per component and deliberation/critique passes; definition of a call/forward, batching and samples per call. No equal-compute inference from equal call counts. |
| Input/output volume | Per-attempt native units (tokens with tokenizer revision, characters/bytes, samples, steps, etc.), totals and actual limits. Cross-tokenizer counts are descriptive, not equivalent compute. |
| Context and evidence | Allowed and actual context allocation per participant, immutable evidence references, repeated context, cache use, truncation/refusal and tool-result inclusion. Equal nominal windows do not mean equal information. |
| Wall time | End-to-end task elapsed time plus separately scoped load, preprocessing, invocation and postprocessing where measurable; timing method, cold/warm/cache state, network/queue inclusion, repetition and summary statistic. Summed call durations are not concurrent elapsed time. |
| Hardware | CPU/GPU/accelerator identity/count, total host/device capacity, execution device and thread limits. Provider-hidden hardware stays unknown. |
| Memory | Measurement method and interval; process high-water RSS, device peak allocation and host capacity kept distinct. Include load if measured that way; do not call host capacity an implementation requirement. |
| Storage | Model/artifact bytes and measured scope, including shared artifacts counted once and exclusions; separate evidence/cache storage when applicable. |
| External cost | Actual API charge or labeled estimate, currency, pricing date/source, discounts/cache/batch assumptions and included services. Zero external inference cost is not zero hardware, energy or total cost. |
| Retries and failures | All attempts, reasons, partial work, timeout/refusal and consumed resources before failure, linked to the original task. Retries cannot silently become independent successful trials. |
| Tool/retrieval use | Allowed and actual tool/retrieval calls, results/evidence supplied, external cost and latency; include router, translator, judge and escalation work rather than only specialist calls. |
| Concurrency | Planned and observed parallelism, batching, workers/threads, overlap and scheduling policy; declare unavailable observations. |

Freeze the experimental unit and denominator: all assigned cases and all attempts remain visible, with separate answered-only quality, coverage, abstention, error and escalation rates. For abstaining predictors, assess risk jointly with coverage; this avoids credit for answering only easy cases. The risk–coverage distinction is established in [Selective Classification](https://proceedings.neurips.cc/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html). Empty answered sets have undefined answered-only quality, not perfect accuracy.

Credible comparisons must declare what is held equal (evidence/tool access, inference allowance, hardware or monetary/latency budget) and what differs. Report actual consumption even under matched caps. Count development/training/selection effort separately from inference when construction cost or adaptation is compared. Do not collapse tokens, dollars, memory and time into a fabricated common compute unit. If hidden provider resources or incompatible timing boundaries prevent a matched comparison, report the observations descriptively and narrow the efficiency claim. Quality under a fixed cost/latency allowance and quality at unequal resource use are different claims.

Measurement boundaries draw on the [MLPerf inference rules at `d3eba2f`](https://github.com/mlcommons/inference_policies/blob/d3eba2f21026d868ad65cdcad2bb81e4a17ce3d3/inference_rules.adoc): describe the system under test, include preprocessing/postprocessing and state the workload/scenario. This is reuse of reporting discipline, not an MLPerf compliance or score claim. No benchmark harness is introduced.

## Error-correction accounting

For composed systems, preserve:

- errors introduced by each module;
- errors caught by another module;
- valid claims incorrectly rejected;
- disagreements that remain unresolved;
- disagreements resolved correctly;
- cases where composition makes the final result worse.

Cross-module correction is a candidate MASI mechanism and should be measured directly rather than inferred from final score alone.

## Causal modularity / specialist ablation

A named responsibility contract is not evidence that an implementation is genuinely modular. When MASI claims that a specialist has a bounded functional role, prefer a causal intervention test rather than inferring modularity from routing frequency, prompt labels, architecture diagrams, or final system accuracy.

The basic question is:

> **If specialist X is removed, neutralized, or replaced, does performance degrade primarily on X's declared responsibility rather than broadly across unrelated responsibilities?**

A claim-bearing modularity test should preregister:

- the specialist and exact declared responsibility being tested;
- one or more **on-target** task axes where that specialist should matter;
- credible **off-target** axes where it should not be necessary;
- the intervention: removal, bypass, neutral stub, frozen substitute, or another semantically justified ablation;
- a null/control intervention, such as a size/resource-matched random removal, irrelevant-module removal, or contract-preserving substitute where applicable;
- metrics and selectivity rule before seeing the intervention result;
- held-out or independently constructed evaluation material;
- uncertainty/statistical procedure where stochasticity matters;
- resource effects introduced by the ablation itself.

Useful evidence for bounded modularity has the qualitative form:

```text
large reproducible on-target degradation
+
materially smaller off-target degradation
+
stability across justified metrics / held-out material
+
no hidden change to evidence, routing, budget, or authority
```

Failure modes are scientifically useful:

- no meaningful degradation after removal → the specialist may be unnecessary, redundant, bypassed, or poorly tested;
- broad degradation across unrelated axes → the specialist may carry hidden general/shared state or the decomposition may be wrong;
- verdict flips across metric/corpus choices → the modularity claim is measurement-dependent and must be narrowed;
- another specialist silently absorbs the role → test composition/routing adaptation separately rather than calling the original component causally isolated;
- system failure caused only by interface breakage → repair the ablation design; do not misreport plumbing failure as cognitive modularity.

Where feasible, include a **positive control** whose selective role is already known or mechanically constructed so the evaluation can demonstrate that it is capable of detecting modularity when present.

This methodology is adapted from preregistered causal expert-ablation work on sparse MoE systems (Salomone, Gandhi & Asaria 2026, arXiv:2606.25092) but applies to MASI at the responsibility/component level. Their particular selectivity threshold is not imported as a universal MASI rule.

For H4 interchangeability, pair ablation with substitution: after showing that removing X selectively matters, replace X with a different implementation of the same frozen responsibility contract and test whether on-target capability returns without changing downstream consumer semantics.

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

## Independent reference checks — E1 decision

**Required in future contracts:** independently derived expected tables/checks for claim-critical deterministic semantics, including native-to-boundary mapping, abstention/escalation, scoring denominators and resource aggregation. A small hand-calculated table is sufficient; a second runtime is unnecessary. The reference must not import or call the production transformation it checks. Include applicable boundary, missing, invalid and non-finite cases; record derivation/reviewer provenance and freeze expected results before final observation. Standard hash algorithms need not be reimplemented.

Freeze and identify the runner, mapping, evaluator/reference check, protocol and evaluation assets for every reported run; changes create a new attributable version without overwriting earlier evidence. Shared helpers may still check integrity/drift, but cannot be the sole correctness check for their own semantics. For non-deterministic quality labels, use a frozen independently reviewed rubric and blinded assessment rather than pretending a deterministic table supplies ground truth.

WP1 remains accepted only as narrowed. E1 identifies shared runner/verifier helpers there; this decision applies to the next authorized contract and authorizes no WP1 code, evidence or evaluator repair.

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

Audit E1 is a **next-contract lesson only**: WP1's verifier shares normalization and hashing helpers with the runner, so it is an integrity/drift check rather than independent validation of those helpers. The WP0 decision above now requires an independent reference check for future claim-critical semantics. WP1 remains unchanged; neither R1–R7 nor this documentation packet authorizes an evaluator repair or new experiment.
