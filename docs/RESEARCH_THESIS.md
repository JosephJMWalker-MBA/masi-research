# MASI Research Thesis

## Primary question

Can a governed composition of specialized, interchangeable intelligence systems equal or exceed substantially larger general-purpose models on complex decision tasks while preserving inspectability, calibration, modularity, and accountability to outcomes?

## Core hypothesis

MASI proposes that system-level intelligence can emerge from the governed composition of different learned or computational competencies rather than requiring one model to be uniformly strong at every cognitive responsibility.

The stronger construction hypothesis is that a useful specialist need not begin as a reduced or adapted general-purpose model at all:

> **Begin with the smallest cognitive ambition the system actually requires. Engineer the representation, learning objective, state, feedback, uncertainty, and interfaces specifically for that bounded responsibility. Generality belongs to the governed composition, not to each component.**

This is the default MASI construction doctrine, not a side experiment. See [`CONSTRUCTION_DOCTRINE.md`](CONSTRUCTION_DOCTRINE.md).

A useful MASI result should therefore demonstrate more than "multiple calls beat one call." It should identify which architectural property produced the gain and whether the specialization came from a purpose-built bounded intelligence, a general-model adaptation, simple decomposition, or another mechanism.

Candidate mechanisms include:

- purpose-built bounded intelligence;
- learned specialization;
- heterogeneous model families and non-model computational systems;
- explicit decomposition of responsibilities;
- preserved disagreement;
- cross-module error correction;
- dynamic composition;
- confidence-aware escalation;
- conditional influence weighting;
- outcome-grounded updating over time.

## Construction classes

MASI experiments should distinguish implementation class where relevant:

```text
CONTROL_A      general-purpose model + role prompt
CONTROL_B      general/pretrained base + role-specific adaptation or fine-tuning
MASI_TARGET    purpose-built bounded intelligence designed from the responsibility outward
INFRASTRUCTURE routing, logging, evaluation, governance, transport, or other supporting machinery
```

`CONTROL_A` and `CONTROL_B` are valuable scientific controls and may be useful transitional implementations. They do not become the target architecture by convenience or inertia.

A `MASI_TARGET` may be neural, probabilistic, Bayesian, causal, symbolic, deterministic, simulation-based, hybrid, or another architecture entirely. There is no requirement that it be an LLM.

## What would count as evidence for MASI?

Evidence may support progressively stronger claims.

### H1 — Decomposition value

A role-decomposed system outperforms a comparable monolithic baseline under clearly stated resource conditions.

This is useful but does not yet establish learned specialization or purpose-built specialized intelligence.

### H2A — Adapted specialization value

A locally trained or adapted specialist outperforms the same underlying local base model on its bounded responsibility, including held-out and adversarial cases.

This establishes value from role-specific adaptation but does **not** by itself validate the stronger specialization-by-construction thesis.

### H2B — Purpose-built specialization value

A bounded intelligence designed from the responsibility outward performs competitively with or better than general-model controls on its responsibility while providing materially better inspectability, state discipline, calibration, efficiency, or failure localization.

The purpose-built system should begin with the minimum sufficient representational and computational scope and add complexity only in response to measured capability deficits.

### H3 — Composition value

A composition of specialist implementations outperforms the constituent specialists operating independently or a simple aggregation baseline.

### H4 — Interchangeability value

Different implementations can satisfy the same responsibility contract and be substituted without rewriting the overall system architecture or leaking implementation-specific hidden representations across boundaries.

### H5 — Dynamic composition value

A governed router can reduce unnecessary specialist invocation, improve escalation, or preserve performance under lower resource use compared with always-on composition.

### H6 — Reality-grounded adaptation value

Outcome records from prior decisions improve later weighting, routing, calibration, or module selection on materially comparable tasks without hiding repeated error behind general capability.

### H7 — Local-system competitiveness

A composed local MASI system equals or exceeds a substantially larger frontier-model baseline on a preregistered task family under transparent resource and pass-count accounting.

This is the strongest near-term system-level hypothesis and should not be claimed from a narrow or favorable fixture set.

## Required controls

Where relevant, experiments should distinguish at least:

```text
F1  frontier monolith
L1  local monolith
L2  local ensemble / simple aggregation
M1  local MASI composition
```

For specialist-construction experiments, also distinguish where practical:

```text
C_A  prompted general-model control
C_B  adapted / fine-tuned general-model control
T    purpose-built MASI target
```

Later experiments may add:

```text
F2  frontier model under the same MASI protocol
M2  MASI with learned/dynamic routing
M3  MASI with outcome-grounded influence adaptation
```

These controls separate model capability from architecture, extra inference passes, routing, adaptation, and purpose-built specialization.

## Strong falsifiers

MASI should be narrowed or rejected if repeated well-controlled experiments show one or more of the following:

1. **Prompt decomposition explains the gains.** Learned or purpose-built specialization adds no measurable value beyond role prompting.
2. **General-model adaptation explains the gains.** Purpose-built bounded intelligence provides no measurable advantage in capability, inspectability, calibration, efficiency, failure localization, or governance over simpler adapted general models.
3. **More tokens explain the gains.** A frontier model given equivalent inference budget matches or exceeds MASI.
4. **Simple ensembles explain the gains.** Voting, averaging, or best-of-N reproduces the effect without MASI governance.
5. **Specialists do not generalize.** Improvements disappear outside training-like cases or under mild distribution shift.
6. **Interchangeability fails.** Supposed responsibility contracts are actually tied to one specific model, tokenizer, representation, provider, or implementation.
7. **Governance overhead dominates.** Coordination costs exceed quality, reliability, or efficiency gains on the intended task class.
8. **Reality feedback adds no value.** Outcome-based influence updates do not improve later decisions beyond ordinary calibration or established simpler methods.
9. **Canonical responsibility boundaries are artificial.** Precision, Foresight, Empathy, Wisdom, or any other decomposition fails to produce separable measurable competencies.
10. **Existing systems solve the problem more simply.** Established routing, mixture-of-experts, ensemble, bandit, verifier, or multi-agent methods reproduce the desired properties without MASI-specific machinery.

A falsifier is not a project failure. It tells the research program what to stop building.

## Measurement principles

- freeze the benchmark before evaluating the final systems;
- include negative and boundary controls;
- separate capability quality from cost and latency;
- report pass count and model-call count;
- preserve disagreements and failed runs;
- measure calibration only where a calibrated probability claim is actually made;
- distinguish outcome quality from stylistic preference;
- distinguish observed improvement from causal explanation;
- record implementation class (`CONTROL_A`, `CONTROL_B`, `MASI_TARGET`, `INFRASTRUCTURE`) for experimental components;
- for purpose-built targets, record ontology/state, allowed inputs, outputs, feedback signal, transparent baseline, and the capability deficit justifying each major complexity increase;
- do not publish provider-restricted benchmark results.

## Research posture

The historical MASI disclosures establish a conceptual lineage, not a requirement that future experiments reproduce every earlier mechanism.

The architecture should become smaller, stranger, more heterogeneous, or substantially different if evidence requires it.

A frontier or general-purpose model may help build MASI, but it must not silently become MASI's theory of cognition.
