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

## Minimum semantic boundary — WP0 gate

**Role contract != model identity. Common boundary != common internal representation.** These are semantic obligations for the next authorized contract, not a new wire schema or runtime. The [WP0 ownership record](WP0_RESEARCH_GATES.md#masi-bus-ownership-and-gaps) maps them to current MASI Bus and identifies gaps. A small experiment manifest plus linked input/output records may satisfy them; every item need not be repeated in every response.

| Information available at the boundary | Minimum obligation |
| --- | --- |
| Responsibility and contract identity | Named bounded responsibility, contract/profile version, allowed inputs and units/capacity limits. Multiple implementations may satisfy the same profile. Family/tokenizer limits remain implementation-specific; no universal token bound. |
| Implementation and source identity | Stable implementation identity and exact revision/source, separately identifying model, adapter and mapping; construction class from [RESEARCH_THESIS.md](RESEARCH_THESIS.md). Reference the existing candidate manifest for license/lineage status rather than duplicating it. |
| Input/evidence references | Exact input snapshot or durable content reference with version/hash where possible, evidence actually supplied and transformations applied. Distinguish supplied evidence from wider available evidence; unknown use is not proof of use. |
| Native output | Retain the actual native value/artifact or retrievable reference, type/format and units. A proof, constraint state, distribution, simulation or observation need not become prose. Retain partial output on failure where available. |
| Bounded judgment/state | Only when required by the consuming responsibility: a named typed value and its meaning, linked to the native output and frozen mapping. Disclose lost distinctions. No universal support score, probability or hidden embedding shared by all families. |
| Uncertainty | State its kind, referent, domain and method: e.g. uncalibrated score, predictive interval, epistemic unknown or deterministic result. Supply a value only when meaningful, with units and calibration evidence/status. `not applicable`, `not measured` and `unavailable` with reasons are distinct. |
| Execution and judgment disposition | Distinguish completed computation from an answered judgment, abstention, execution failure or blockage. Preserve specification/evaluator/authority defects as such; none becomes an ordinary negative verdict or success. |
| Abstention and escalation | Abstention withholds the specified judgment and names the reason/scope. Escalation requests a stated review/capability because a bound was exceeded; record recipient/authority if defined, or unresolved destination. It grants no permission and may accompany abstention or a provisional answer. |
| Assumptions and disagreement | Explicit unsupported/conditional assumptions, their affected outputs and evidence links or stated lack of support. “None declared” is not proof of absence. Keep each participant's output, conflicts and unresolved alternatives; no forced consensus or averaging of incomparable scores. |
| Provenance and resources | Link input → native output → normalized interpretation to participant, source/mapping revisions and invocation/attempt; link resource observations under [EVALUATION.md](EVALUATION.md#resource-accounting). Record absent values with reasons, including failed attempts. |

Reason codes, structured witnesses or evidence references are sufficient where the profile permits them; a specialist need not fabricate a rationale. If required semantics cannot be represented or supplied, record a contract gap or failed conformance, not a plausible-looking substitute. Consumers interpret declared semantic fields without inferring hidden internals or changing their meaning by implementation identity. Identity alone grants no authority; declared provenance and measured performance history may inform selection/influence under a separately frozen policy. Normalization belongs behind the implementation's declared boundary, with an auditable mapping; it may not introduce new evidence or authority. A future H4 test must freeze permitted adapter/registration changes while keeping the contract and consumer semantics fixed, and test actual semantic preservation, not merely identical method signatures.

Class describes construction, not experimental role or authority. `B0` is a comparison role, not a fifth class: a transparent solver can be a `MASI_TARGET` only if it satisfies the doctrine's responsibility-first gate; an evaluation floor remains `INFRASTRUCTURE`. No new candidate is classified or selected here.

### Responsibility-specific semantics remain distinct

The common obligations above coexist with these family distinctions. A later profile must choose bounded sub-responsibilities and exact types; these examples are not mandatory model outputs.

| Family | Semantics its profile must preserve when applicable |
| --- | --- |
| Precision | Proposition/constraint and evidence identity; support, contradiction and insufficient evidence are distinct when the task needs them; a proof/check result is not a calibrated probability. |
| Foresight | Conditional scenario versus probabilistic forecast; target quantity/state, units, conditioning/action assumptions, horizon and uncertainty meaning. A scenario list supplies no implied likelihood. |
| Empathy | Stakeholder and evidence links; reported human state versus inferred observation, missing perspectives and uncertainty. Inference supplies neither diagnosis nor normative/action authority. |
| Wisdom | Comparable context, prior prediction/action/outcome links and eligibility of later evidence; any proposed influence update distinct from approved/applied change. No learner or update rule is implemented or selected here. |

## Minimum Reality Audit record

The record is a durable relation between existing artifacts, not another message envelope. It reuses input/output and provenance records above. A future outcome-bearing experiment must bind the following information before execution, then append observations and assessments without rewriting decision-time state.

| Record portion | Required information where applicable |
| --- | --- |
| Identity and lineage | Experiment/record and task references; responsible human/component, implementation class and exact source/version; links to participating outputs and assessment author/version. Distinguish record revisions from new attempts. |
| Decision-time snapshot | Prediction/proposal reference and native meaning, relevant assumptions, uncertainty semantics/calibration status, evidence available at decision time, subset supplied to each participant, availability/cutoff time and provenance. |
| Expected consequences | Predicted target(s), quantity/state and units, conditions/action assumed, expected consequence(s), uncertainty and horizon/window for each; freeze the correspondence rule and due time before observing outcomes. Non-predictive proposals explicitly say so. |
| Decision and authority | Chosen action/decision reference or explicit no-action/not-yet-decided state, decision-maker and time, rejected alternatives where recorded, permission/authority source and allowed boundary. Record actual execution separately from selection, including deviation or non-execution. |
| Later observations | Actual consequences, event time/window and evidence availability/collection time, provenance/method/observer, relevant changed conditions and action-execution reference. Retain pending, censored, missing, disputed and not-applicable outcomes with reasons; absence is not zero error. |
| Correspondence/error assessment | Link each expected consequence to observed evidence or an explicit unassessable state; apply the frozen matching/error rule with assessor/version and assessment time. Preserve per-horizon results, failed predictions and unresolved alternatives before aggregation. |

```text
prediction != action
action != outcome
later outcome != evidence available earlier
successful outcome != retroactive proof that earlier reasoning was sound
```

Use stable references and versioned snapshots so the decision can be reconstructed without later knowledge. Append corrections with their own time/provenance; retain the earlier record. Shared task identity does not prove causation. Outcomes following a selected action do not reveal unchosen counterfactuals; a later H6 protocol must address selection and missingness before learning or causal claims. A prediction never acted upon may still be scored where its frozen target permits it. For a probe with no real action/outcome, explicitly mark those portions not applicable instead of manufacturing a Reality Audit success.

This reuses the entity/activity/agent and usage/derivation distinctions in [W3C PROV-DM (2013 Recommendation)](https://www.w3.org/TR/2013/REC-prov-dm-20130430/). It does not require RDF, a provenance service, a universal utility score, or an outcome learner.

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
