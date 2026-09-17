# MASI Research

**Open research into modular, specialized, interchangeable intelligence systems.**

MASI Research investigates whether a governed composition of genuinely specialized intelligence modules can equal or exceed substantially larger general-purpose models on complex decision tasks while improving inspectability, calibration, modularity, resource efficiency, and accountability to outcomes.

The project is not organized around a canonical model, provider, or implementation. Models are interchangeable participants. What matters is whether an implementation satisfies an explicit responsibility under measurable conditions.

## Core research thesis

> A dynamically composed ecology of specialized intelligence systems can outperform reliance on a single general-purpose model when the task benefits from distinct cognitive responsibilities, explicit disagreement, bounded authority, and learning from real-world outcomes.

In MASI, specialization should be encoded through training objectives, data, architecture, learned state, outcome feedback, deterministic machinery, or some combination of these. Different system prompts alone do not constitute the intended end state.

## Architectural commitments

- **No canonical model truth.** No module becomes authoritative merely because it occupies a named role.
- **Interchangeability.** A responsibility may be implemented by a local model, frontier model, decision-native model, deterministic system, ensemble, simulator, or future method.
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
        ↓ candidate implementations

masi-research
        ↓ experiments, comparison, falsification

reproducible evidence
```

Existing projects may provide bounded research substrates without becoming MASI dependencies. For example, the Accumulated Distress Care Protocol (ADCP) may supply part of an Empathy research track; a decision-native model such as Jev may be a useful Precision comparator; neither is canonical MASI.

## Current phase

**Phase 0 — research foundation and first falsifiable experiment.**

Near-term work is intentionally narrow:

1. freeze the research thesis and falsifiers;
2. define implementation-independent module contracts;
3. define fair baselines and evaluation rules;
4. design the first small learned-specialization experiment;
5. preserve enough provenance for independent reproduction.

The first proposed experiment is `MASI-E001`: test whether a small locally specialized semantic observer can outperform its untuned local baseline, and potentially a larger general-purpose model, on a bounded Empathy-related observation task derived from ADCP-style fixtures.

## How to contribute

This repository is public because the long-term goal is collaborative research, not a closed product roadmap.

Useful contributions include:

- reproductions;
- negative results;
- stronger baselines;
- benchmark critiques;
- prior-art findings;
- alternative module definitions;
- trained specialist implementations;
- calibration methods;
- datasets or synthetic fixtures with clear provenance;
- evidence that a module should be split, merged, replaced, or removed;
- evidence that the MASI thesis itself should be narrowed or rejected.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before proposing implementation work.

## Repository map

- [`STATUS.md`](STATUS.md) — current research state and next action
- [`AGENTS.md`](AGENTS.md) — operating rules for AI-assisted work
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and evidence standards
- [`docs/RESEARCH_THESIS.md`](docs/RESEARCH_THESIS.md) — hypotheses and falsification criteria
- [`docs/MODULES.md`](docs/MODULES.md) — candidate responsibility contracts
- [`docs/EVALUATION.md`](docs/EVALUATION.md) — baseline and comparison rules
- [`docs/PRIOR_ART.md`](docs/PRIOR_ART.md) — prior-art posture and research obligations
- [`experiments/README.md`](experiments/README.md) — experiment lifecycle and naming

## Research posture

MASI should not be protected from evidence.

The objective is not to prove that the historical architecture was right. The objective is to discover whether modular specialized intelligence provides measurable value, under what conditions, through what mechanisms, and at what cost.
