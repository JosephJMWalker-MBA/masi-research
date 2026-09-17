# Status

**Current phase:** Phase 0 -> Phase 1 transition — bounded implementation, **paused for construction-doctrine reconciliation**

**Primary objective:** turn MASI from a conceptual/disclosure lineage into falsifiable executable research while preserving model interchangeability, explicit governance, fair baselines, claim discipline, and the project's original specialization-by-construction thesis.

## Construction doctrine — now explicit and mandatory

[`docs/CONSTRUCTION_DOCTRINE.md`](docs/CONSTRUCTION_DOCTRINE.md) is a governing research document.

MASI does **not** presume that specialized intelligence should be created by taking a general-purpose model and narrowing, prompting, pruning, or fine-tuning it into a role.

The default target is:

> **Start with the smallest cognitive ambition actually required. Engineer the representation, learning objective, state, feedback, uncertainty, and interfaces specifically for that bounded responsibility. Generality belongs to the governed composition, not to each component.**

Prompted and fine-tuned general models remain useful controls, baselines, tools, translators, and transitional implementations. They are not presumed end-state MASI specialists.

Every substantive implementation should be classified as:

```text
CONTROL_A      general-purpose model + role prompt
CONTROL_B      general/pretrained base + role-specific adaptation / fine-tuning
MASI_TARGET    purpose-built bounded intelligence designed from the responsibility outward
INFRASTRUCTURE supporting routing, logging, evaluation, governance, transport, etc.
```

## Immediate hold

The first Astra five-hour block completed before the construction doctrine was explicit enough in the repository instructions.

**Do not begin the next Astra implementation block until WP-1 in `docs/IMPLEMENTATION_SPRINT_001.md` is complete.**

The next session must first reconcile the existing first-block work against the doctrine, classify artifacts, identify accidental coupling/architecture assumptions, and record what remains valid versus what must be narrowed, relabeled, or refactored.

This is a correction of architectural interpretation, not a presumption that the first block should be discarded.

## Current decisions

- `masi-research` is the public experimental home for ongoing MASI work.
- `masi-bus` remains the communication/reference artifact; it is not replaced by this repository.
- No model is canonical merely because it implements a named MASI responsibility.
- Precision, Foresight, Empathy, and Wisdom are current architectural responsibility abstractions whose boundaries remain revisable.
- **Specialization by construction, not subtraction, is the default target.**
- Prompt-only role decomposition is an experimental baseline, not the intended definition of specialization.
- Fine-tuning/adapting a pretrained general model is also a useful control/transitional path, not the presumed end state.
- Generality belongs at the governed system level; it should not be replicated inside every specialist by default.
- Telos is a leading **candidate** for governance/control-plane orchestration, especially intent/authority/permission continuity; it is not thereby a mandatory dependency or the learned task router.
- The candidate fleet should be heterogeneous: language models, classifiers, forecasters, reward models, bandits, deterministic systems, causal systems, simulators, and hybrids may all compete for bounded responsibilities.
- New complexity must be justified by a measured capability deficit or a frozen experiment/interface need.
- Existing AI systems are research specimens: sources of useful primitives, adaptable implementations, baselines, and cautionary evidence.

## Candidate landscape

The working registry is maintained in [`docs/CANDIDATE_IMPLEMENTATIONS.md`](docs/CANDIDATE_IMPLEMENTATIONS.md).

Initial high-priority probes include:

- **Routing:** vLLM Semantic Router / RouteLLM plus a deterministic routing baseline;
- **Precision:** HHEM-2.1-Open, NLI classifiers, Jev as an external comparator where terms permit;
- **Foresight:** Chronos / TimesFM-class numerical forecasters plus explicit causal/simulation alternatives;
- **Empathy:** an ADCP-derived semantic observer plus bounded auxiliary sensors and explicit ontology/state modeling;
- **Wisdom:** simple explicit weighting, Bayesian approaches, MABWiser / Vowpal Wabbit contextual-bandit baselines before assuming Wisdom should be a neural language model;
- **Governance/control:** Telos plus a simpler deterministic governance baseline.

These systems do not define the final module architectures. They are candidates, comparators, components, or cautionary evidence.

## Active implementation sprint

[`docs/IMPLEMENTATION_SPRINT_001.md`](docs/IMPLEMENTATION_SPRINT_001.md) defines the current execution plan.

Current operator cadence:

```text
Astra on Ultra — primary implementation/research block
        ↓
commit + tests + evidence + unknowns
        ↓
Claude — independent audit at ~5-hour / work-packet boundary
        ↓
accept / repair / narrow / mark inconclusive
        ↓
next Astra block
```

GitHub is the durable state boundary. No model session is the system of record.

The next Astra block begins with **WP-1 doctrine reconciliation**, not new implementation.

## Immediate sequence

1. Complete WP-1: reconcile Astra block 1 against `CONSTRUCTION_DOCTRINE.md`.
2. Close enough of Issues #1 and #2 to freeze the thesis, common responsibility envelope, and Reality Audit minimum.
3. Preserve/build only the smallest candidate-probe layer needed to invoke interchangeable local implementations through one bounded experiment interface.
4. Run heterogeneous research specimens/baselines through that interface while keeping their architectural class explicit.
5. Redesign/freeze `MASI-E001` so it can distinguish general-model controls from a purpose-built bounded Empathy target.
6. Attempt a minimal heterogeneous composition smoke test only after individual candidate behavior is observable.

## First specialization experiment

**MASI-E001 — Empathy semantic-observation specialist**

Revised research pressure:

> Can a purpose-built bounded intelligence infer an evidence-grounded human-impact / care observation state competitively with general-model controls while providing stronger inspectability, state discipline, uncertainty handling, efficiency, or failure localization?

ADCP remains useful because it separates human-authored observations from deterministic downstream policy. E001 targets the observation layer only; it must not train a model to imitate ADCP's policy thresholds.

A fine-tuned local language model may remain a `CONTROL_B` condition. It should not be assumed to be the final Empathy architecture.

## Not yet authorized

- beginning a second Astra implementation block before WP-1 doctrine reconciliation is recorded;
- building a general-purpose MASI platform before bounded experiments require it;
- creating separate repositories for individual MASI modules;
- treating Telos, Jev, ADCP, any router, or any local model as canonical MASI;
- treating a pretrained/fine-tuned general model as the target specialist without explicit evidence and architectural justification;
- allowing routing convenience to become governance authority;
- training a Wisdom language model before an auditable outcome record and simpler baselines exist;
- publishing third-party performance benchmarks where provider terms prohibit publication;
- prohibited reverse engineering, distillation, imitation training, source extraction, or other use inconsistent with provider/model terms;
- installing the entire candidate registry at once;
- changing held-out evaluation criteria after observing results.

## Next durable action

**WP-1 only:** Astra should pull the latest repository state, read `docs/CONSTRUCTION_DOCTRINE.md` and `AGENTS.md`, inspect its first five-hour block, classify the artifacts, record the reconciliation, and stop there for audit if the architectural impact is material.
