# MASI Research

**Open research into modular, specialized, interchangeable intelligence systems.**

MASI Research investigates whether a governed composition of genuinely specialized intelligence modules can equal or exceed substantially larger general-purpose models on complex decision tasks while improving inspectability, calibration, modularity, resource efficiency, and accountability to outcomes.

The project is not organized around a canonical model, provider, or implementation. Models are interchangeable participants. What matters is whether an implementation satisfies an explicit responsibility under measurable conditions.

## Core research thesis

> A dynamically composed ecology of specialized intelligence systems can outperform reliance on a single general-purpose model when the task benefits from distinct cognitive responsibilities, explicit disagreement, bounded authority, and learning from real-world outcomes.

## Construction doctrine

MASI's target is **specialization by construction, not specialization by subtraction**.

> **Begin with the smallest cognitive ambition the system actually requires. Engineer the representation, learning objective, state, feedback, uncertainty, and interfaces specifically for that bounded responsibility. Generality belongs to the governed composition, not to each component.**

A prompted or fine-tuned general-purpose model may be useful as a control, baseline, translator, tool, proposal generator, or transitional implementation. It is **not** presumed to be the target specialist architecture merely because it is convenient to build.

A purpose-built MASI specialist may be neural, probabilistic, Bayesian, causal, symbolic, deterministic, simulation-based, hybrid, or something else entirely. There is no requirement that it be an LLM.

The full non-negotiable engineering doctrine is in [`docs/CONSTRUCTION_DOCTRINE.md`](docs/CONSTRUCTION_DOCTRINE.md).

### General-purpose intelligence is retained, not rejected

MASI is not an anti-LLM architecture. A capable LLM can be treated as **general-purpose prior intelligence**: broad competence for language, translation, hypothesis generation, decomposition, synthesis, long-tail cases, and proposing what is plausible or worth investigating next.

Its output is not automatically truth, authority, forecast, diagnosis, or permission. Purpose-built specialists can confirm, correct, constrain, or disagree with it. Decision-native systems such as Jev are likewise useful components where their bounded interfaces fit; they remain interchangeable rather than canonical.

The working pattern is:

```text
human / messy world input
        ↓
general-purpose prior / translation / proposals
        ↓
purpose-built bounded specialists and decision instruments
        ↓
explicit disagreement, uncertainty, evidence, and outcome history
        ↓
governed result
```

This preserves the enormous practical value of LLMs without making the LLM the whole theory of cognition.

Existing AI systems are useful as:

- sources of primitives worth inheriting;
- implementations worth adapting where transparent and licensed;
- baselines / comparators;
- cautionary evidence about opacity, technical debt, training lineage, state failure, calibration, authority confusion, and other failure modes to engineer against.

The question is not simply "which current model should fill this role?" It is also "what does this system teach us about the bounded intelligence we should build from the responsibility outward?"

## Architectural commitments

- **No canonical model truth.** No module becomes authoritative merely because it occupies a named role.
- **Specialization by construction.** Purpose-built bounded intelligence is the target; narrowed general models are controls/transitional implementations unless evidence justifies promotion.
- **Minimum sufficient intelligence.** Add complexity only when a measured capability deficit requires it.
- **Generality belongs to composition.** Do not replicate broad general intelligence inside every specialist by default.
- **Generalists remain components.** LLMs and decision-native systems can provide breadth, translation, proposal generation, synthesis, or bounded judgments without becoming final epistemic or governance authority.
- **Interchangeability.** A responsibility may be implemented by a local model, frontier model, decision-native model, deterministic system, ensemble, simulator, causal model, bandit, or future method.
- **Typed semantic boundaries.** Semantically meaningful state crossing module boundaries should be named, typed, inspectable, testable, and where practical causally intervenable.
- **Governed composition.** The system controls which capabilities participate, how they interact, when disagreement is preserved, and when escalation is required.
- **Evidence over identity.** Module influence should be earned by measured performance, calibration, context, and outcomes rather than brand or model size.
- **Preserved disagreement.** Consensus is not automatically truth.
- **Outcome accountability.** Where possible, expected consequences should later be compared with observed consequences.
- **Human authority remains explicit.** MASI may structure, test, compare, and update intelligence; consequential human decisions should not be silently delegated by architecture.
- **Falsifiability.** A result that shows MASI adds no value, that a simpler system works better, or that a proposed module is unnecessary is a successful research result.

## Candidate cognitive responsibilities

The historical MASI lineage includes four recurring responsibilities:

- **Precision** — calibrated bounded judgment, constraint satisfaction, contradiction detection, evidence consistency, classification, abstention, and escalation.
- **Foresight** — conditional future-state modeling, scenario branching, delayed consequences, second-order effects, and tail risks.
- **Empathy** — stakeholder representation, burden, agency, relational consequences, care-sensitive interpretation, and uncertainty about inferred human states.
- **Wisdom** — outcome-grounded meta-learning: comparing predictions with consequences and updating the conditional influence of models, evidence, assumptions, and reasoning patterns over time.

These are architectural abstractions, not canonical model identities. Their boundaries, multiplicity, implementations, and necessity remain experimentally revisable.

## Relationship to existing work

This repository is the experimental research layer. It does not replace the existing MASI disclosures or the `masi-bus` protocol artifact.

```text
published MASI disclosures
        ↓ conceptual lineage

masi-bus
        ↓ communication reference

specialist research / external systems
        ↓ candidate implementations, baselines, primitives, cautions

masi-research
        ↓ experiments, comparison, falsification

reproducible evidence
```

Existing projects may provide bounded research substrates without becoming MASI dependencies. For example, the Accumulated Distress Care Protocol (ADCP) may supply part of an Empathy research track; a decision-native model such as Jev may be a useful Precision comparator or bounded decision component; neither is canonical MASI.

The focused prior-art record in [`docs/PRIOR_ART.md`](docs/PRIOR_ART.md) now treats blackboard systems/Hearsay-II, Brooks' subsumption architecture, Global Workspace/IDA/LIDA, Neural Module Networks, modular deep learning, MRKL, FlexOlmo, Concept Bottleneck Models, and contemporary modular-composition work as important neighboring lineages.

## Candidate implementations

MASI is expected to be heterogeneous. A useful implementation may be a language model, classifier, forecaster, reward model, contextual bandit, simulator, deterministic policy, causal model, symbolic component, or external decision-native service.

The working candidate registry is maintained in [`docs/CANDIDATE_IMPLEMENTATIONS.md`](docs/CANDIDATE_IMPLEMENTATIONS.md). It currently includes Telos as a candidate governance/control-plane substrate, routing baselines such as vLLM Semantic Router and RouteLLM, bounded Precision verifiers, specialist forecasting systems, ADCP-derived Empathy work, and contextual-bandit approaches to early Wisdom experiments.

The registry is a search surface, not a canonical fleet. Candidates must earn inclusion in experiments through fit, licensing, reproducibility, hardware practicality, and evidence.

## Current phase

**WP1 accepted only as narrowed; WP0 research gates independently accepted for bounded experiment design.**

The first Astra implementation block began before the specialization-by-construction doctrine was explicit enough in the repository. Its classification and reconciliation against [`docs/CONSTRUCTION_DOCTRINE.md`](docs/CONSTRUCTION_DOCTRINE.md) are complete; the remaining gates concern future work.

**WP1 audit checkpoint:** Claude's [independent audit](docs/AUDIT_WP0_WP1_2026-09-17.md) of the frozen builder packet `81adfff` initially returned `CLAIM_NARROWING_REQUIRED`. Astra's documentation-only [R1–R7 reconciliation](docs/RECONCILIATION_WP1_R1_R7.md) was then independently re-checked in Audit Addendum B and received `ACCEPT`. **WP1 is accepted only as narrowed.** The reconciliation does not merge the builder's code, frozen files, or evidence; the immutable builder packet remains pinned at `81adfff`.

The observed result is uniform invocation of a **closed, pre-registered set**: an `INFRASTRUCTURE`/B0 equality floor and two externally adapted pretrained transformer classifiers (`CONTROL_B`-class specimens), repeated bit-identically on one host. Normalization remains caller-resident and candidate-keyed. The protocol's inference-branching condition was not triggered; the broader contract's caller-branch condition holds only for invocation, not normalization. Neither arbitrary new implementations, purpose-built targets nor cross-paradigm interchangeability were demonstrated. [Results](experiments/wp1/RESULTS.md) record no capability deficit justifying learned complexity. Issue #1's gate-level thesis/falsification criteria are now satisfied by the accepted WP0 packet; task-specific bindings remain provisional.

The [WP0 research-gates packet](docs/WP0_RESEARCH_GATES.md) records claim-linked controls, the minimum semantic responsibility boundary, Reality Audit record, current MASI Bus ownership/gaps, resource observations and the future independent-reference-check requirement. H2A/H2B and existing falsifiers are retained. Audit Addendum C independently accepted these gates **only for the bounded purpose of enabling design of the next experiment**; this is not demonstrated implementation conformance or permission to start an experiment.

The next operator decision is whether to authorize exactly one protocol-binding packet for a single named experiment. That packet must bind the task, metrics/margins, competent controls, family-specific semantics, budgets and applicable integrity checks, then stop for independent audit before implementation. WP2/E001, K001 execution, training, new candidates and runtime expansion remain unauthorized until such an explicit decision.

The first specialization experiment remains `MASI-E001`, but a fine-tuned local language model is now explicitly a control condition rather than the presumed target. The target is the smallest credible Empathy-observation intelligence designed from the responsibility outward.

The active implementation plan is [`docs/IMPLEMENTATION_SPRINT_001.md`](docs/IMPLEMENTATION_SPRINT_001.md).

## How to contribute

This repository is public because the long-term goal is collaborative research, not a closed product roadmap.

Useful contributions include:

- reproductions;
- negative results;
- stronger baselines;
- benchmark critiques;
- prior-art findings;
- alternative module definitions;
- purpose-built specialist architectures;
- trained/adapted model controls;
- calibration methods;
- datasets or synthetic fixtures with clear provenance;
- evidence that a module should be split, merged, replaced, or removed;
- evidence that the MASI thesis itself should be narrowed or rejected.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before proposing implementation work.

## Repository map

- [`STATUS.md`](STATUS.md) — current research state and next action
- [`AGENTS.md`](AGENTS.md) — operating and audit rules for AI-assisted work
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and evidence standards
- [`docs/CONSTRUCTION_DOCTRINE.md`](docs/CONSTRUCTION_DOCTRINE.md) — non-negotiable specialization-by-construction doctrine
- [`docs/RESEARCH_THESIS.md`](docs/RESEARCH_THESIS.md) — hypotheses and falsification criteria
- [`docs/MODULES.md`](docs/MODULES.md) — candidate responsibility contracts
- [`docs/EVALUATION.md`](docs/EVALUATION.md) — baseline and comparison rules
- [`docs/WP0_RESEARCH_GATES.md`](docs/WP0_RESEARCH_GATES.md) — bounded WP0 decisions, Bus ownership, provisional choices and audit handoff
- [`docs/PRIOR_ART.md`](docs/PRIOR_ART.md) — focused prior-art lineage and research obligations
- [`docs/CANDIDATE_IMPLEMENTATIONS.md`](docs/CANDIDATE_IMPLEMENTATIONS.md) — candidate models, systems, substrates, and baselines
- [`docs/IMPLEMENTATION_SPRINT_001.md`](docs/IMPLEMENTATION_SPRINT_001.md) — current bounded implementation plan and builder/auditor cadence
- [`experiments/README.md`](experiments/README.md) — experiment lifecycle and naming

## Licensing and reuse

MASI is published to be tested, implemented, challenged, extended, and reused. The purpose of this repository is to make the architecture operational and empirically accountable, not to restrict independent implementations.

Unless otherwise noted, original code, schemas, experiment harnesses, documentation source, and other repository content are licensed under the [Apache License 2.0](LICENSE).

This repository does not relicense external material:

- previously published MASI defensive disclosures retain the terms attached to those publications;
- third-party models, datasets, libraries, artifacts, and services retain their own licenses and terms;
- contributed material must be compatible with this repository's licensing and contribution requirements.

## Research posture

MASI should not be protected from evidence.

The objective is not to prove that the historical architecture was right. The objective is to discover whether modular specialized intelligence provides measurable value, under what conditions, through what mechanisms, and at what cost.

A frontier or general-purpose model may help us build and operate MASI. It must not silently become MASI's entire theory of cognition, and it should not be removed when its breadth genuinely solves a problem the specialists should not be forced to inherit.
