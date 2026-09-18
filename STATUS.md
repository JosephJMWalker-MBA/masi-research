# Status

**Current phase:** WP1 observed; independent audit: `CLAIM_NARROWING_REQUIRED`, pending acceptance of documentation narrowing; **paused for construction-doctrine reconciliation**.

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

The first Astra block began before the doctrine was explicit enough. Claude's [independent audit](docs/AUDIT_WP0_WP1_2026-09-17.md) found that the later freeze and runs still used the older branch governance. Implementation and evidence survived audit; the required corrections are documentation-only R1–R7.

**Do not begin the next Astra implementation block until WP-1 in `docs/IMPLEMENTATION_SPRINT_001.md` is complete.**

The [R1–R7 reconciliation](docs/RECONCILIATION_WP1_R1_R7.md) records classes, superseded thesis/E001 framing, the absence of a demonstrated capability deficit, closed-set invocation limits and the historical validation erratum. It is submitted for a **scoped Claude re-check**, not accepted merely by publication. No implementation or evidence repair is authorized.

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

The current packet is **WP-1 documentation reconciliation only**. The frozen builder artifact remains `codex/wp0-wp1-candidate-probe @ 81adfff`; its code and evidence are not merged into this branch.

## Observed WP1 scope

Three pre-registered implementations — `exact-match-v1` (`INFRASTRUCTURE`/B0 floor), `hhem-2.1` and `nli-deberta-small` (externally adapted `CONTROL_B`-class specimens) — used uniform invocation by changing the candidate identifier and reproduced bit-identically on one host. The probe and adapters are `INFRASTRUCTURE`; no `CONTROL_A` or `MASI_TARGET` was tested. See [implementation classes](experiments/wp1/IMPLEMENTATION_CLASSES.md).

Substitution is demonstrated only for that closed set: normalization is caller-resident and candidate-keyed, and both learned candidates share one classifier stack and adapter class. The protocol's inference-branching condition was not triggered; the contract's broader caller-branch condition holds only for invocation, not normalization. Open-set or cross-paradigm interchangeability is unestablished. WP1 identified no capability deficit in transparent Precision approaches and does not justify learned complexity.

The historical WP1-local thesis matrix is superseded for thesis purposes by current H2A/H2B, `C_A/C_B/T` controls and falsifiers 1–10 in [RESEARCH_THESIS.md](docs/RESEARCH_THESIS.md). Issue #1's WP0 thesis-freeze deliverable remains open. Issue #2 remains broader than this local interface, and Issue #4 remains broader than WP1.

## Immediate sequence

1. Complete the scoped Claude re-check of R1–R7 against governing `main` at `a0ac9fe9cd400a6c03d6543d5b79f651bf89a3a5` and the unchanged builder artifact at `81adfff`.
2. Record the auditor's disposition. `CLAIM_NARROWING_REQUIRED` and the implementation hold remain until that check accepts the narrowing.
3. Stop. WP2/E001 preparation, training, new candidates, runtime changes and merging any branch require separate operator authorization.

## First specialization experiment

**MASI-E001 — Empathy semantic-observation specialist**

Revised research pressure:

> Can a purpose-built bounded intelligence infer an evidence-grounded human-impact / care observation state competitively with general-model controls while providing stronger inspectability, state discipline, uncertainty handling, efficiency, or failure localization?

ADCP remains useful because it separates human-authored observations from deterministic downstream policy. E001 targets the observation layer only; it must not train a model to imitate ADCP's policy thresholds.

A pretrained base selection or fine-tuning path is an **optional `CONTROL_B` arm**. The target remains purpose-built bounded Empathy-observation intelligence designed from the responsibility outward. No E001 preparation, base selection, labeling, split freezing, implementation or training is authorized by R1–R7.

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

**WP-1 only:** scoped Claude re-check of the [R1–R7 documentation reconciliation](docs/RECONCILIATION_WP1_R1_R7.md). Verify the documentation-only diff, historical annotations, unchanged frozen/code/evidence files and both existing evidence-verifier results. E1 remains a next-contract lesson, not a WP1 repair. Do not proceed to WP2.
