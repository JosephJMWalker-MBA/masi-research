# Implementation Sprint 001 — From Research Foundation to Executable Evidence

**Status:** active planning / execution  
**Started:** 2026-09-17

## Objective

Use the remaining current-week high-capability agent allocation to move MASI from research scaffolding toward the **smallest executable system that can test interchangeability and learned specialization without prematurely building a general runtime**.

This sprint is not authorized to declare the MASI architecture validated. Its purpose is to create runnable seams, frozen evaluation contracts, and first evidence.

## Current operator workflow

The current working cadence is operational only; it is not part of the MASI architecture.

- **Primary implementation agent:** Astra on Ultra for the available weekly allocation.
- **Independent audit agent:** Claude at each approximately five-hour Astra boundary or major work-packet boundary.
- **Durable system of record:** this repository, its issues, branches, PRs, tests, experiment artifacts, and status records — not any model session.

The goal of switching agents is not stylistic diversity. It is to create an independent review boundary so one long-running implementation process does not silently redefine the research question, acceptance criteria, or evidence.

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
4. files changed;
5. tests executed and their exact results;
6. evidence artifacts produced;
7. known failures and unresolved questions;
8. claims the evidence does **not** support;
9. exact next action.

Claude's audit should independently check:

1. whether the implementation still answers the frozen question;
2. whether the diff adds unnecessary architecture;
3. whether baselines are fair and resource accounting is explicit;
4. whether test/data leakage or benchmark contamination is plausible;
5. whether model/provider licenses and publication terms are respected;
6. whether evidence and interpretation are separated;
7. whether failure/negative results have been preserved;
8. whether any implementation has accidentally become authoritative by convention;
9. whether the result should be accepted, repaired, narrowed, or treated as inconclusive.

An audit should not rewrite working code merely to impose a preferred style. It should identify research, correctness, reproducibility, governance, licensing, and scope defects first.

## Work packets

### WP0 — Freeze enough of Issues #1 and #2 to permit code

Before meaningful model integration:

- tighten the primary thesis and falsifiers;
- define the minimum common responsibility output envelope;
- define abstention / escalation / unsupported-assumption semantics;
- decide what belongs in `masi-bus` versus experiment-specific records;
- define a minimum Reality Audit record;
- document resource-accounting requirements.

**Exit condition:** a candidate adapter can be implemented without inventing its own incompatible semantics.

### WP1 — Build the smallest candidate-probe layer

Do **not** build a generic MASI server.

Create only enough implementation to:

- register a candidate implementation by stable identifier;
- record source/version/license metadata;
- invoke a local candidate through a thin adapter;
- normalize its bounded output into the experiment contract;
- preserve raw output separately from normalized interpretation;
- record latency/resource metadata where available;
- run fixed local fixtures reproducibly.

Start with one or two local candidates, not the entire registry.

Preferred first Precision probes:

- HHEM-2.1-Open;
- one NLI classifier.

Preferred first deterministic control:

- a trivial explicit rules/baseline adapter using the same envelope.

**Exit condition:** at least two interchangeable implementations can be invoked through the same bounded experiment interface without changing the calling experiment.

### WP2 — Prepare `MASI-E001`

Use Issue #3 as the authority for the experiment.

Required before training:

- freeze target observation dimensions;
- add independent-label review format;
- freeze split logic;
- freeze metrics;
- add negative/boundary controls;
- select a small trainable base model based on actual local hardware fit;
- implement untuned-local and larger-general baseline paths;
- preserve ADCP deterministic policy outside the learned observer.

**Exit condition:** training can begin without changing the test set or success criteria after results are visible.

### WP3 — First learned specialization

Train the smallest practical Empathy-semantic-observation specialist sufficient to test the E001 hypothesis.

Compare at minimum:

```text
B0 — trivial / deterministic baseline where meaningful
L1 — untuned local base model
S1 — same local base after specialization
F1 — larger general-purpose baseline
```

Do not claim MASI system-level superiority from this experiment. E001 tests whether learned specialization itself adds measurable value on one bounded responsibility.

### WP4 — Heterogeneous composition smoke test

Only after WP1 and E001 are sufficiently stable, construct a **minimal composed decision fixture** that can consume outputs from at least two different candidate responsibility implementations.

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

These may begin in parallel only if they do not block E001.

- **Foresight:** verify that a specialized quantitative forecaster (Chronos / TimesFM / equivalent) can be invoked as a bounded MASI candidate rather than asking a language model to imitate numerical forecasting.
- **Wisdom:** create a synthetic Reality Audit sequence and compare simple weighting, MABWiser, and/or Vowpal Wabbit before designing a learned language-model Wisdom implementation.

These are probes, not module finalization.

## Branch / review discipline

Prefer one branch or PR per bounded work packet or coherent experiment change. Avoid a single week-long branch containing unrelated architecture, data, training, and documentation changes.

Each PR should state:

```text
question
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
- the selected model does not fit available hardware;
- fixture labels are circular or contaminated;
- implementation requires a new abstraction not justified by the current question;
- a simpler existing component already answers the question;
- the evidence contradicts the intended MASI claim.

## End-of-week success

A successful week does **not** require a full MASI system.

A strong sprint outcome would be:

1. thesis/contracts are sufficiently frozen to support implementation;
2. a thin interchangeable candidate-probe layer exists;
3. at least two heterogeneous local implementations have run through it;
4. E001 is either ready for training or has produced its first controlled result;
5. Astra/Claude handoffs have left auditable state in GitHub;
6. the next experiment is obvious from evidence rather than enthusiasm.
