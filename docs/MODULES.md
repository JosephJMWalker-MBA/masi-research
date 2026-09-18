# Candidate MASI Responsibility Contracts

MASI responsibilities are **interfaces for competence**, not names for permanent models.

A responsibility may be implemented by a local model, frontier model, decision-native model, deterministic algorithm, simulator, ensemble, or hybrid system. Multiple implementations may coexist. None is authoritative by identity alone.

This document defines the current candidate responsibilities narrowly enough to evaluate them while leaving their implementations open.

## Shared contract principles

Any MASI-compatible implementation should make its output inspectable enough to support:

- provenance to the input evidence it used;
- uncertainty or confidence where meaningful;
- explicit unsupported assumptions;
- compatibility with disagreement and critique;
- resource accounting;
- replaceability by another implementation of the same responsibility;
- failure / abstention / escalation when the task exceeds its validated scope.

A module output is evidence for the system, not truth.

## Precision

### Intended responsibility

Evaluate bounded propositions, constraints, contradictions, classifications, and evidence relationships with strong calibration and willingness to abstain.

Candidate capabilities include:

- claim support / contradiction / insufficiency;
- constraint satisfaction;
- exact classification;
- consistency checking;
- extraction disambiguation;
- confidence-aware escalation;
- detection of unsupported inference;
- bounded numerical or logical checks.

### Non-goals

Precision should not become the default owner of moral judgment, long-horizon forecasting, stakeholder impact, or final authority merely because its outputs are structured.

### Candidate implementations

Examples may include:

- decision-native probabilistic models;
- small task-trained classifiers;
- constrained local language models;
- deterministic validators;
- verifier ensembles.

Jev may be studied as an external Precision-like comparator, but is not canonical MASI.

## Foresight

### Intended responsibility

Represent possible future states and conditional consequences across multiple horizons.

Candidate capabilities include:

- scenario branching;
- second-order effects;
- delayed consequences;
- dependency propagation;
- tail-risk identification;
- sensitivity to uncertain assumptions;
- explicit distinction between forecast and fact.

### Non-goals

Foresight should not silently convert plausible scenarios into predictions, nor should it determine stakeholder value or normative acceptability by itself.

### Candidate implementations

Examples may include:

- temporal models;
- simulation systems;
- planning models;
- causal / structural models;
- local language models adapted for scenario analysis;
- hybrid simulation + language systems.

## Empathy

### Intended responsibility

Represent human stakes and perspectives without confusing inferred human state with objective truth or clinical diagnosis.

Candidate capabilities include:

- stakeholder discovery;
- perspective representation;
- burden / benefit asymmetry;
- agency and consent effects;
- relational consequences;
- care-sensitive interpretation;
- missing-perspective detection;
- uncertainty about motives, emotions, and human state.

### Non-goals

Empathy is not agreement, sycophancy, sentiment matching, diagnosis, or moral authority.

An Empathy implementation should be able to preserve distinctions such as:

```text
stakeholder A may experience this as harmful
!=
stakeholder A's factual interpretation is established
```

### Candidate implementations

The Accumulated Distress Care Protocol (ADCP) provides one possible research substrate for a narrow Empathy-related capability: mapping conversational evidence into bounded observations while leaving downstream care policy deterministic. ADCP is not the Empathy module and need not become a MASI dependency.

Other implementations may focus on stakeholder impact, agency, relational dynamics, or different domains entirely.

## Wisdom

### Intended responsibility

Learn from outcomes over time which modules, evidence types, assumptions, reasoning patterns, or decision policies deserve influence in comparable contexts.

Candidate capabilities include:

- expected-vs-observed outcome comparison;
- calibration tracking;
- repeated-error detection;
- conditional credibility estimation;
- context-specific influence weighting;
- multi-horizon outcome accounting;
- preservation of unresolved alternatives;
- distinction between internal consensus and externally validated success.

### Non-goals

Wisdom is not a model prompted to sound philosophical or prudent. It should not collapse disagreement into a final answer merely because several modules agree.

### Candidate implementation form

A useful abstraction is:

```text
module × task family × evidence regime × horizon -> conditional influence
```

Influence updates should be distinguishable from retraining the underlying specialist. A system may first learn that one specialist deserves less weight in a context; later research may test whether that evidence should also contribute to deliberate specialist retraining.

## Composition is also tunable

MASI should support several independent forms of tuning:

### Composition tuning

Which responsibilities participate in this task?

### Implementation tuning

Which implementation fills or competes within a responsibility?

### Influence tuning

How much weight does each output receive in this context?

### Protocol tuning

Should modules work independently, sequentially, adversarially, recursively, or with human checkpoints?

These mechanisms should be evaluated rather than assumed.

## Revisability

Precision, Foresight, Empathy, and Wisdom originate in the MASI research lineage. They are not exempt from empirical revision.

Research may show that a responsibility should be:

- split;
- merged;
- renamed;
- implemented deterministically;
- represented by multiple competing modules;
- made task-specific;
- or removed entirely.

The architecture should follow evidence rather than preserve symmetry.

## Historical WP1 interface boundary

The [frozen `wp1-support-v1` contract at `81adfff`](https://github.com/JosephJMWalker-MBA/masi-research/blob/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/docs/WP0_WP1_CONTRACT.md) defines the historical probe's envelope, uncertainty, failure, MASI Bus boundary and documentation-only Reality Audit minimum. It remains a WP1-local interface, not the general Precision contract or a current thesis freeze. The [R1 class record](../experiments/wp1/IMPLEMENTATION_CLASSES.md) identifies an `INFRASTRUCTURE`/B0 floor and two externally adapted `CONTROL_B`-class specimens; no `MASI_TARGET` was observed. Caller-resident candidate-keyed normalization limits the observation to a closed set. Current [RESEARCH_THESIS.md](RESEARCH_THESIS.md) governs H2A/H2B and construction controls; code and frozen files remain unchanged.
