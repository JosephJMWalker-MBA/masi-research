# Implementation Sprint 001 — From Research Foundation to Executable Evidence

**Status:** active; **WP1 accepted only as narrowed; WP0 research gates accepted for bounded experiment design**  
**Started:** 2026-09-17

**Current audit checkpoint:** WP1 was observed on the frozen builder branch `81adfff`; the first independent [Claude audit](AUDIT_WP0_WP1_2026-09-17.md) returned `CLAIM_NARROWING_REQUIRED`. Astra's documentation-only [R1–R7 reconciliation](RECONCILIATION_WP1_R1_R7.md) was independently re-checked in Audit Addendum B and received `ACCEPT`. **WP1 is accepted only as narrowed.** Audit Addendum C subsequently accepted the WP0 research gates only for bounded experiment design. The builder code/evidence remain pinned at `81adfff` and are not merged by either acceptance.

The observed invocation result is limited to three pre-registered implementations: an `INFRASTRUCTURE`/B0 floor and two externally adapted `CONTROL_B`-class specimens. Invocation is uniform, but normalization is caller-resident and candidate-keyed; the broader contract's caller-branch condition holds only for invocation, not normalization. No open-set, cross-paradigm or purpose-built-target interchangeability is established, and no capability deficit justifying learned complexity was shown. See the [narrowed results](../experiments/wp1/RESULTS.md). The frozen WP1-local thesis matrix does not close Issue #1's thesis-freeze deliverable under current H2A/H2B doctrine.

## Objective

Use the remaining current-week high-capability agent allocation to move MASI from research scaffolding toward the **smallest executable system that can test interchangeability, specialization, and purpose-built bounded intelligence without prematurely building a general runtime**.

This sprint is not authorized to declare the MASI architecture validated. Its purpose is to create runnable seams, frozen evaluation contracts, and first evidence.

The sprint is governed by [`CONSTRUCTION_DOCTRINE.md`](CONSTRUCTION_DOCTRINE.md). The target architecture is **specialization by construction**, not merely specialization by adapting general-purpose models.

## Completed WP-1 reconciliation checkpoint

The first Astra five-hour block began before the construction doctrine was explicit enough. The required doctrine reconciliation has now been completed, independently audited, and accepted only as narrowed.

The durable record is:

- frozen builder packet: `codex/wp0-wp1-candidate-probe @ 81adfff`;
- reconciliation: [`RECONCILIATION_WP1_R1_R7.md`](RECONCILIATION_WP1_R1_R7.md);
- independent acceptance: [Audit Addendum B](AUDIT_WP0_WP1_2026-09-17.md).

No `MASI_TARGET` or `CONTROL_A` was tested. The accepted result is closed-set uniform invocation with caller-resident, candidate-keyed normalization and same-host repeatability. The equality rule remains a floor, not a competitive transparent Precision baseline; no capability deficit justifying learned complexity was demonstrated.

## Current operator workflow

The current working cadence is operational only; it is not part of the MASI architecture.

- **Primary implementation agent:** Astra on Ultra for the available weekly allocation.
- **Independent audit agent:** Claude at each approximately five-hour Astra boundary or major work-packet boundary.
- **Durable system of record:** this repository, its issues, branches, PRs, tests, experiment artifacts, and status records — not any model session.

The goal of switching agents is not stylistic diversity. It is to create an independent review boundary so one long-running implementation process does not silently redefine the research question, acceptance criteria, construction doctrine, or evidence.

## Handoff cycle

```text
Frozen work packet
      ↓
Astra implementation / research
      ↓
commit + tests + evidence + explicit unknowns
      ↓
Claude independent audit
      ↓
accept / identify defect / narrow claim / request repair
      ↓
next Astra work packet
```

Before an Astra boundary, preserve:

1. exact branch / commit;
2. active issue and research question;
3. decisions frozen during the block;
4. implementation class for each major artifact (`CONTROL_A`, `CONTROL_B`, `MASI_TARGET`, `INFRASTRUCTURE`);
5. files changed;
6. tests executed and their exact results;
7. evidence artifacts produced;
8. known failures and unresolved questions;
9. claims the evidence does **not** support;
10. exact next action.

Claude's audit should independently check:

1. whether the implementation still answers the frozen question;
2. whether it follows the specialization-by-construction doctrine;
3. whether a general-model baseline has silently become the target architecture;
4. whether the diff adds unnecessary architecture;
5. whether baselines are fair and resource accounting is explicit;
6. whether test/data leakage or benchmark contamination is plausible;
7. whether model/provider licenses and publication terms are respected;
8. whether evidence and interpretation are separated;
9. whether failure/negative results have been preserved;
10. whether any implementation has accidentally become authoritative by convention;
11. whether the result should be accepted, repaired, narrowed, or treated as inconclusive.

An audit should not rewrite working code merely to impose a preferred style. It should identify research, correctness, reproducibility, governance, licensing, doctrine, and scope defects first.

## Work packets

### WP-1 — Reconcile Astra block 1 against the construction doctrine

**Required before all remaining work packets.**

Produce a durable reconciliation note containing:

```text
first-block branch / commit:
artifacts reviewed:
artifact classifications:
accidental architecture assumptions:
hidden implementation coupling:
unjustified complexity:
what remains valid unchanged:
what must be relabeled / narrowed / refactored:
next authorized action:
```

**Exit condition:** it is clear which first-block artifacts are experimental infrastructure/baselines and which, if any, legitimately satisfy the purpose-built MASI target doctrine.

For this packet, the [implementation-class record](../experiments/wp1/IMPLEMENTATION_CLASSES.md) identifies no `MASI_TARGET` or `CONTROL_A`. Audit Addendum B accepted R1–R7, so WP-1 is complete **only as narrowed**. E1's independent-reference-check recommendation remains a future-contract lesson, not a WP1 repair. WP0 below is now independently accepted for bounded experiment design; any next protocol packet still requires separate operator authorization and audit before implementation.

### WP0 — Freeze enough of Issues #1 and #2 to design the next bounded experiment

**Accepted for bounded experiment design.** Audit Addendum C accepted the [WP0 research-gates record](WP0_RESEARCH_GATES.md) against governing main `8de8bbd`. This remains a documentation/design gate, not execution authorization. The downstream packets remain a roadmap requiring separate authorization.

Before meaningful specialist integration:

- tighten the primary thesis and falsifiers;
- define the minimum common responsibility output envelope;
- define abstention / escalation / unsupported-assumption semantics;
- decide what belongs in `masi-bus` versus experiment-specific records;
- define a minimum Reality Audit record;
- document resource-accounting requirements;
- require implementation-class metadata for experimental candidates.

**Exit condition: met at gate level.** The next experiment can now be designed using fixed thesis/control, semantic-boundary, outcome-record and resource-comparison rules. A separately authorized protocol must still bind task-specific semantics, an operational definition of competent controls, metrics/margins, budgets, applicable energy measurement or explicit non-measurement, adversarial-integrity-case inclusion, and independent checks before implementation; purpose-built targets retain native internal representations. No candidate adapter is implemented by this packet. E1 is resolved as a future-contract requirement for independent reference tables/checks, never a WP1 repair.

### WP1 — Build the smallest candidate-probe layer

Do **not** build a generic MASI server.

Create only enough implementation to:

- register a candidate implementation by stable identifier;
- classify it as `CONTROL_A`, `CONTROL_B`, `MASI_TARGET`, or `INFRASTRUCTURE`;
- record source/version/license metadata;
- invoke a local candidate through a thin adapter;
- normalize its bounded output into the experiment contract;
- preserve raw output separately from normalized interpretation;
- record latency/resource metadata where available;
- run fixed local fixtures reproducibly.

Start with one or two local candidates, not the entire registry.

Preferred first Precision probes remain useful **as baselines/research specimens**:

- HHEM-2.1-Open;
- one NLI classifier;
- a trivial explicit rules/baseline adapter using the same envelope.

These probes do not define the final Precision architecture. Their purpose is to exercise interchangeability and reveal useful primitives, baseline performance, interface pressure, and inherited limitations.

**Exit condition:** at least two interchangeable implementations can be invoked through the same bounded experiment interface without changing the calling experiment, and their architectural status is explicit.

### WP2 — Prepare `MASI-E001`

Use Issue #3 as the authority for the experiment.

Required before training or purpose-built implementation:

- freeze target observation dimensions;
- add independent-label review format;
- freeze split logic;
- freeze metrics;
- add negative/boundary controls;
- preserve ADCP deterministic policy outside the learned observer;
- define the Empathy-observer responsibility, allowed inputs, native ontology/state, outputs, uncertainty/abstention semantics, and learning signal;
- define a transparent non-neural or minimally learned baseline;
- define `CONTROL_A` and include `CONTROL_B` where adaptation is a live alternative, following the claim-linked thesis controls;
- separately define the smallest credible `MASI_TARGET` architecture from the responsibility outward.

A pretrained general model may be selected for a control condition if useful and hardware-practical. It must not become the target simply because fine-tuning infrastructure already exists.

**Exit condition:** the experiment can distinguish decomposition, general-model adaptation, and purpose-built bounded intelligence without changing the held-out test set or success criteria after results are visible.

### WP3 — First specialization experiment

The first specialization experiment should compare distinct construction approaches where practical.

Minimum useful comparison:

```text
B0   transparent / deterministic baseline where meaningful
C_A  prompted general-model control
C_B  adapted or fine-tuned general/pretrained model control when adaptation is a live alternative
T1   purpose-built bounded MASI target
F1   larger general-purpose comparator where terms permit
```

`T1` should begin with the minimum sufficient intelligence for the responsibility. Its architecture must be justified by the task ontology and measured deficits, not by current LLM convention.

For an H2B claim, `B0` must be a competent transparent solver and `C_A` is required by the [WP0 thesis gate](RESEARCH_THESIS.md#required-controls). Omitting `C_B` precludes a superiority-to-adaptation claim. Freeze quality competitiveness and the primary property-improvement criterion together before final observation.

Do not claim MASI system-level superiority from this experiment. The first objective is to determine what kind of specialization actually adds measurable value on one bounded responsibility.

### WP4 — Heterogeneous composition smoke test

Only after WP1 and the first specialization experiment are sufficiently stable, construct a **minimal composed decision fixture** that can consume outputs from at least two different candidate responsibility implementations.

The goal is to test executable interchangeability and disagreement preservation — not to maximize benchmark score.

Potential first composition:

```text
Precision evidence check
      +
Empathy bounded observation
      ↓
explicit deterministic composition policy
      ↓
provisional structured output
```

Telos may be evaluated as a governance/control-plane candidate here if the experiment requires authority/permission/intent continuity. Do not force Telos into a fixture that does not test those properties.

### WP5 — Foresight and Wisdom probes

These may begin in parallel only if they do not block the first specialization experiment.

- **Foresight:** use Chronos / TimesFM / equivalent as research specimens and baselines for what purpose-built forecasting intelligence can look like; do not assume the final Foresight implementation must inherit their architecture.
- **Wisdom:** create a synthetic Reality Audit sequence and compare explicit weighting, Bayesian approaches, MABWiser, and/or Vowpal Wabbit before designing any neural Wisdom implementation.

These are probes, not module finalization.

## Branch / review discipline

Prefer one branch or PR per bounded work packet or coherent experiment change. Avoid a single week-long branch containing unrelated architecture, data, training, and documentation changes.

Each PR should state:

```text
question
construction doctrine fit
implementation class
frozen acceptance criteria
implementation summary
baselines
commands / tests
artifacts
observed result
limitations
audit status
next pressure
```

## Stop conditions

Stop and record rather than expanding scope when:

- the experiment cannot distinguish the claimed mechanism;
- the baseline is unfair or underspecified;
- license/terms are unclear;
- the selected model/system does not fit available hardware;
- fixture labels are circular or contaminated;
- implementation requires a new abstraction not justified by the current question;
- complexity is being added without a measured capability deficit;
- a general-model adaptation is drifting from control condition into target architecture without explicit evidence and approval;
- a simpler existing component already answers the question;
- the evidence contradicts the intended MASI claim.

## End-of-week success

A successful week does **not** require a full MASI system.

A strong sprint outcome would be:

1. the first Astra block is reconciled against the construction doctrine;
2. thesis/contracts are sufficiently frozen to support implementation;
3. a thin interchangeable candidate-probe layer exists;
4. at least two heterogeneous implementations have run through it with explicit implementation classes;
5. the first purpose-built specialist experiment is designed or entering controlled execution;
6. Astra/Claude handoffs have left auditable state in GitHub;
7. the next experiment is obvious from evidence rather than enthusiasm.
