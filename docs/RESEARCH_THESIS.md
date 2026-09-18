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

## WP0 claim and decision gate

This documentation packet tests no performance hypothesis. **H7 is the strongest system-level claim under investigation and remains untested.** H2A/H2B and falsifiers 1–10 are sufficient; their names and scope are retained. They distinguish adaptation from construction, while H1/H3/H5/H6 distinguish decomposition, composition, routing and feedback. These mechanisms can interact, so support for one does not establish the others.

For a later authorized specialist experiment, **H2B is the primary construction claim**: the purpose-built system must both meet a preregistered quality requirement relative to competent controls and materially improve a declared primary property. Freeze the comparison arm, quality metric and non-inferiority/superiority margin, property metric and minimum improvement, coverage requirement, uncertainty method and multiplicity policy before final observation. Do not select whichever property happens to improve after seeing results. Inspectability requires an operational test, such as correct semantic intervention or failure localization, not merely more fields or a longer rationale.

H2A separately requires the exact unadapted-base comparison. An interface-only experiment may instead target a bounded H4 claim. This gate does not choose the next experiment, start E001/K001, or require a learned target: a competent transparent system satisfying the responsibility is a valid result, and supplies no reason to add complexity.

Before implementation, the next authorized protocol must bind its primary claim, task family, allowed evidence, controls, metrics/margins, resource allowances, evaluation/sample plan, uncertainty and stop rules to these gates. Before final observation it must freeze the actual evaluation assets, system revisions and independent checks. Open experiment-specific values are listed in [WP0_RESEARCH_GATES.md](WP0_RESEARCH_GATES.md); a missing claim-critical control blocks that claim.

## Required controls

Later composed-system experiments must include the applicable local conditions below. **H7 requires all four**, including a publishable or otherwise lawfully reportable `F1` comparison; absent that comparison, narrow to a local claim.

```text
F1  frontier monolith
L1  local monolith
L2  local ensemble / simple aggregation
M1  local MASI composition
```

For specialist-construction experiments, distinguish:

```text
C_A  prompted general-model control
C_B  adapted / fine-tuned general-model control
T    purpose-built MASI target
```

Additional conditions become mandatory when their mechanism is claimed:

```text
F2  frontier model under the same MASI protocol
M2  MASI with learned/dynamic routing
M3  MASI with outcome-grounded influence adaptation
```

The following contrasts are mandatory for the corresponding attribution. One arm may satisfy multiple control roles if declared in advance; a speculative full factorial is not required.

| Claimed mechanism | Minimum contrast and conditions | Limit if missing |
| --- | --- | --- |
| H1 decomposition | Same base and evidence: role decomposition versus monolith, including an equivalent extra-pass monolith under the declared resource allowance. | Roles versus one call cannot isolate decomposition. |
| H2A adaptation | Adapted implementation versus its exact unadapted base; disclose prompts, development data/effort and inference resources. | Unrelated pretrained specimens establish no adaptation effect. |
| H2B construction | Competent transparent `B0`, prompted `C_A`, purpose-built `T`; include `C_B` when adaptation is a live alternative. Apply the conjunctive decision rule above. | Omitted `C_B` forbids a superiority-to-adaptation claim. A deliberately weak floor cannot establish a capability deficit. |
| H3 composition | Strongest applicable standalone constituent, simple aggregation `L2`, and governed composition `M1`, using the same constituents and information; hold constituent outputs fixed for the policy contrast. | Final accuracy alone does not distinguish composition policy from stronger components or extra calls. |
| H4 interchangeability | Fixed semantic contract and consumers; preregistered substitutions with independently checked semantic conformance. | State the tested set, computational families and allowed adapter changes. Uniform invocation alone is insufficient. |
| H5 routing | Same candidate set/information: always-on composition, simple fixed routing, proposed dynamic routing `M2`. | Count routing/escalation overhead; an oracle route is only a diagnostic ceiling. |
| H6 outcome feedback | Same chronological history: no update, established simple update/calibration, proposed update `M3`. | No later evidence may enter earlier decisions; action selection and missing outcomes limit attribution. |
| H7 competitiveness | `F1/L1/L2/M1`, equal evidence/tool access, extra-pass controls and the resource rules in [EVALUATION.md](EVALUATION.md). | Unknown frontier size forbids a demonstrated “substantially larger” claim; incomparable resources forbid an efficiency attribution. |

A composed-system claim also needs a monolithic `L1` control, even if a constituent is strongest. Include prompted-role composition when attributing gains to specialist identity; use `F2` when attributing a frontier comparison to that identity rather than the MASI protocol. If a necessary arm is infeasible or restricted, narrow the claim before execution rather than treating its omission as a favorable result. Same-model sampling/aggregation is an established simpler explanation; see [Self-Consistency](https://arxiv.org/abs/2203.11171v4).

Governance benefit requires authority/conflict/failure-preservation cases and a policy contrast over the same component outputs. Any relaxed-policy control belongs in a bounded offline evaluation, never an unauthorized real action. General task accuracy does not establish governance benefit.

## Confounds that the protocol must control or retain as limits

- Training lineage, contamination, visible author-created fixtures, weak baselines and unequal development effort.
- Different evidence, context, retrieval/tools, passes, retries, translation or normalization that supplies hidden candidate advantages.
- Shared runner/evaluator logic, judge identity bias, circular labels and evaluator defects.
- Selective abstention, excluded failures, best-seed selection, post hoc endpoints and correlated repeats counted as independent cases.
- Outcome delay, censoring, action selection, unobserved counterfactuals and post-decision evidence leakage.
- Different hardware, cache state, numerical precision, concurrency or unknown provider resources.

Keep unsuccessful runs, unresolved disagreements and missing observations visible. A control that cannot remove a confound must narrow the resulting claim.

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

For each experiment, preregister which falsifier its contrasts can address. Falsifiers 1–4 and 10 select simpler explanations; 5 limits generalization; 6 limits substitution; 7 can defeat operational usefulness despite a score gain; 8 removes a feedback-value claim; 9 permits revising or removing responsibilities. An adequately measured simpler-system win narrows or rejects the tested mechanism within that domain. Repeated controlled failures across preregistered task families narrow the broader MASI claim; a single narrow failure does not reject every possible composition.

A null result leaves a claim unsupported; it establishes equivalence only if the design and uncertainty bounds support that conclusion. Missing critical controls, insufficient precision or integrity defects yield an inconclusive or defective evaluation. Do not rescue a failed primary claim by switching mechanisms or secondary endpoints after observation.

## Current nonclaims

Neither WP0 documentation nor accepted-as-narrowed WP1 establishes MASI efficacy, purpose-built specialization, open-set/cross-paradigm interchangeability, calibration, generalization, composition or governance benefit, or a capability deficit justifying learned complexity. A common contract is a design constraint, not evidence that any implementation satisfies it. H1–H7 remain empirical questions.

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

## WP1-local matrix supersession — R2

The historical [WP0/WP1 interface contract at `81adfff`](https://github.com/JosephJMWalker-MBA/masi-research/blob/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/docs/WP0_WP1_CONTRACT.md) remains frozen. Its H1–H7 matrix is WP1-local and **superseded for thesis purposes** by this governing document's H2A/H2B distinction, `C_A/C_B/T` controls and falsifiers 1–10. The old builder crosslink's claim that the matrix fixed the minimum thesis/control distinctions does not hold under current doctrine. Issue #1's WP0 thesis-freeze deliverable remains open.

The [reconciled WP1 result](../experiments/wp1/RESULTS.md) demonstrates only uniform invocation within a closed pre-registered set, with caller-resident candidate-keyed normalization and same-host repeatability. It establishes no H1–H7 effect, including H2A or H2B. Externally adapted `CONTROL_B` specimens without a same-base comparison are not adaptation-value evidence; no `MASI_TARGET` was tested. The equality floor is not a competitive transparent Precision baseline, so WP1 establishes no capability deficit justifying learned complexity. Audit Addendum B in [the independent audit record](AUDIT_WP0_WP1_2026-09-17.md) accepted the R1–R7 narrowing; **WP1 is accepted only as narrowed**.
