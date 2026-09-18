# Status

**Current phase:** WP1 **accepted only as narrowed** after Audit Addendum B. WP0 research gates for Issues #1/#2 are **accepted by Audit Addendum C for the bounded purpose of enabling design of the next experiment**. No experiment protocol or implementation is yet authorized.

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

## WP1 acceptance checkpoint

The first Astra block began before the doctrine was explicit enough. Claude's [independent audit](docs/AUDIT_WP0_WP1_2026-09-17.md) found that the later freeze and runs still used the older branch governance. Implementation and evidence survived audit; the required corrections were documentation-only R1–R7.

Astra recorded the [R1–R7 reconciliation](docs/RECONCILIATION_WP1_R1_R7.md), including implementation classes, superseded thesis/E001 framing, the absence of a demonstrated capability deficit, closed-set invocation limits, and the historical validation erratum.

Claude's scoped re-check, preserved as **Audit Addendum B**, returned `ACCEPT`.

> **WP1 is accepted only as narrowed.**

The construction-doctrine reconciliation hold is therefore cleared. This does **not** merge the frozen builder packet or authorize WP2, E001, training, new candidates, or runtime expansion. The next work packet is separately bounded below.

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

WP1 is complete **as narrowed**. The frozen builder artifact remains `codex/wp0-wp1-candidate-probe @ 81adfff`; its code and evidence are still not merged into `main`.

## Observed WP1 scope

Three pre-registered implementations — `exact-match-v1` (`INFRASTRUCTURE`/B0 floor), `hhem-2.1` and `nli-deberta-small` (externally adapted `CONTROL_B`-class specimens) — used uniform invocation by changing the candidate identifier and reproduced bit-identically on one host. The probe and adapters are `INFRASTRUCTURE`; no `CONTROL_A` or `MASI_TARGET` was tested. See [implementation classes](experiments/wp1/IMPLEMENTATION_CLASSES.md).

Substitution is demonstrated only for that closed set: normalization is caller-resident and candidate-keyed, and both learned candidates share one classifier stack and adapter class. The protocol's inference-branching condition was not triggered; the contract's broader caller-branch condition holds only for invocation, not normalization. Open-set or cross-paradigm interchangeability is unestablished. WP1 identified no capability deficit in transparent Precision approaches and does not justify learned complexity.

The historical WP1-local thesis matrix is superseded for thesis purposes by current H2A/H2B, `C_A/C_B/T` controls and falsifiers 1–10 in [RESEARCH_THESIS.md](docs/RESEARCH_THESIS.md). The accepted [WP0 research gates](docs/WP0_RESEARCH_GATES.md) satisfy Issues #1/#2 at gate level without selecting a benchmark, task-specific protocol, transport, or implementation. Issue #4 remains broader than WP1.

## Immediate sequence

1. Treat WP1 as accepted **only as narrowed**; preserve the builder packet at `81adfff` as immutable historical evidence.
2. Treat the [WP0 research-gates packet](docs/WP0_RESEARCH_GATES.md) as independently accepted **only for bounded experiment design** under Audit Addendum C.
3. Make one operator choice before further research execution: select whether to authorize a protocol-binding packet for exactly one named experiment. That protocol packet must be audited before implementation; acceptance of WP0 alone does not authorize WP2/E001, K001 execution, training, new candidates or runtime expansion.

The accepted packet retains H2A/H2B and falsifiers 1–10, requires claim-linked comparisons and future independent reference checks (E1), and documents the current Bus v1.0 confidence/cost/native-output gaps without changing Bus. Task-specific metrics/margins, inputs, family profile, outcome horizon/rule and resource caps remain unselected by design. The next protocol must also (a) operationally define a competent control, (b) declare an energy-measurement method if energy is claimed or mark energy unmeasured, and (c) state whether adversarial epistemic-integrity cases are included. WP1's historical records and all frozen/code/evidence artifacts remain untouched.

## First specialization experiment

**MASI-E001 — Empathy semantic-observation specialist**

Revised research pressure:

> Can a purpose-built bounded intelligence infer an evidence-grounded human-impact / care observation state competitively with general-model controls while providing stronger inspectability, state discipline, uncertainty handling, efficiency, or failure localization?

ADCP remains useful because it separates human-authored observations from deterministic downstream policy. E001 targets the observation layer only; it must not train a model to imitate ADCP's policy thresholds.

A pretrained base selection or fine-tuning path is an **optional `CONTROL_B` arm**. The target remains purpose-built bounded Empathy-observation intelligence designed from the responsibility outward. No E001 preparation, base selection, labeling, split freezing, implementation or training is authorized by R1–R7.

## Not yet authorized

- beginning WP2/E001, K001 execution, or new specialist implementation before a separately authorized and audited protocol-binding packet exists;
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

**Operator decision only:** choose whether to authorize exactly one bounded protocol-binding packet for a single named experiment. The packet must bind the experiment-specific task, competent controls, metrics/margins, data/splits where applicable, resource budgets, outcome rules and required integrity checks, then stop for independent audit before implementation. Do not infer WP2/E001/K001 or runtime authority from WP0 acceptance.
