# MASI Research Thesis

## Primary question

Can a governed composition of specialized, interchangeable intelligence systems equal or exceed substantially larger general-purpose models on complex decision tasks while preserving inspectability, calibration, modularity, and accountability to outcomes?

## Core hypothesis

MASI proposes that system-level intelligence can emerge from the governed composition of different learned or computational competencies rather than requiring one model to be uniformly strong at every cognitive responsibility.

A useful MASI result should therefore demonstrate more than "multiple calls beat one call." It should identify which architectural property produced the gain.

Candidate mechanisms include:

- learned specialization;
- heterogeneous model families;
- explicit decomposition of responsibilities;
- preserved disagreement;
- cross-module error correction;
- dynamic composition;
- confidence-aware escalation;
- conditional influence weighting;
- outcome-grounded updating over time.

## What would count as evidence for MASI?

Evidence may support progressively stronger claims.

### H1 — Decomposition value

A role-decomposed system outperforms a comparable monolithic baseline under clearly stated resource conditions.

This is useful but does not yet establish learned specialization.

### H2 — Learned specialization value

A locally trained or adapted specialist outperforms the same underlying local base model on its bounded responsibility, including held-out and adversarial cases.

### H3 — Composition value

A composition of specialist implementations outperforms the constituent specialists operating independently or a simple aggregation baseline.

### H4 — Interchangeability value

Different implementations can satisfy the same responsibility contract and be substituted without rewriting the overall system architecture.

### H5 — Dynamic composition value

A governed router can reduce unnecessary specialist invocation, improve escalation, or preserve performance under lower resource use compared with always-on composition.

### H6 — Reality-grounded adaptation value

Outcome records from prior decisions improve later weighting, routing, calibration, or module selection on materially comparable tasks without hiding repeated error behind general capability.

### H7 — Local-system competitiveness

A composed local MASI system equals or exceeds a substantially larger frontier-model baseline on a preregistered task family under transparent resource and pass-count accounting.

This is the strongest near-term hypothesis and should not be claimed from a narrow or favorable fixture set.

## Required controls

Where relevant, experiments should distinguish at least:

```text
F1  frontier monolith
L1  local monolith
L2  local ensemble / simple aggregation
M1  local MASI composition
```

Later experiments may add:

```text
F2  frontier model under the same MASI protocol
M2  MASI with learned/dynamic routing
M3  MASI with outcome-grounded influence adaptation
```

These controls separate model capability from architecture, extra inference passes, routing, and specialization.

## Strong falsifiers

MASI should be narrowed or rejected if repeated well-controlled experiments show one or more of the following:

1. **Prompt decomposition explains the gains.** Learned specialization adds no measurable value beyond role prompting.
2. **More tokens explain the gains.** A frontier model given equivalent inference budget matches or exceeds MASI.
3. **Simple ensembles explain the gains.** Voting, averaging, or best-of-N reproduces the effect without MASI governance.
4. **Specialists do not generalize.** Improvements disappear outside training-like cases or under mild distribution shift.
5. **Interchangeability fails.** Supposed responsibility contracts are actually tied to one specific model or implementation.
6. **Governance overhead dominates.** Coordination costs exceed quality, reliability, or efficiency gains on the intended task class.
7. **Reality feedback adds no value.** Outcome-based influence updates do not improve later decisions beyond ordinary calibration or established simpler methods.
8. **Canonical responsibility boundaries are artificial.** Precision, Foresight, Empathy, Wisdom, or any other decomposition fails to produce separable measurable competencies.
9. **Existing systems solve the problem more simply.** Established routing, mixture-of-experts, ensemble, bandit, verifier, or multi-agent methods reproduce the desired properties without MASI-specific machinery.

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
- do not publish provider-restricted benchmark results.

## Research posture

The historical MASI disclosures establish a conceptual lineage, not a requirement that future experiments reproduce every earlier mechanism.

The architecture should become smaller, stranger, or substantially different if evidence requires it.
