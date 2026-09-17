# MASI Construction Doctrine

## Non-negotiable design invariant

MASI does **not** assume that specialized intelligence should be produced by starting with a general-purpose model and narrowing, prompting, pruning, or fine-tuning it into a role.

The stronger construction thesis is:

> **Begin with the smallest cognitive ambition that the system actually requires. Engineer the representation, learning objective, state, feedback, uncertainty, and interfaces specifically for that bounded responsibility. Generality belongs to the governed composition, not to each component.**

This is not an optional research branch. It is the default construction doctrine for the project.

A general-purpose model that is prompted or fine-tuned into a role may still be useful as a baseline, transitional implementation, tool, translator, proposal generator, or experimental control. It is **not** presumed to be the target specialist architecture merely because current tooling makes it convenient.

## Specialization by construction, not subtraction

MASI distinguishes three implementation classes:

```text
CONTROL A
General-purpose model + role prompt

CONTROL B
General-purpose/pretrained base + role-specific adaptation or fine-tuning

MASI TARGET
Purpose-built bounded intelligence whose architecture is designed from the responsibility outward
```

Controls A and B are scientifically useful. They can show whether decomposition or adaptation explains a result. They must not silently redefine the MASI target.

A purpose-built specialist may be:

- a small neural model;
- a classifier;
- a probabilistic graphical model;
- a Bayesian learner;
- a causal model;
- a time-series forecaster;
- a contextual bandit;
- a constraint solver;
- a state machine;
- a simulator;
- a symbolic or neuro-symbolic system;
- a hybrid of several of these;
- or a future method that better satisfies the responsibility contract.

There is no requirement that a MASI specialist be a language model.

## Minimum sufficient intelligence

For each responsibility, begin by asking:

> **What is the smallest representational and computational system capable of performing this responsibility well enough to participate in MASI?**

Then expand only when measured failure demonstrates a missing capability.

The default sequence is:

1. define the bounded responsibility;
2. define what information the intelligence may perceive;
3. define its native ontology / state representation;
4. define its permitted outputs;
5. define uncertainty, abstention, and escalation;
6. define the feedback signal by which it can improve;
7. implement the simplest transparent system that can perform the job;
8. measure it against frozen baselines;
9. identify a demonstrated capability deficit;
10. add only the complexity required to address that deficit.

**No complexity without an identified capability deficit that justifies it.**

Small means conceptual scope, not merely parameter count. A small opaque model with unknown training lineage and an entangled objective may carry more architectural debt than a larger but tightly controlled specialist.

## Transparency target

MASI does not require the impossible claim that every multiplication inside every learned system is human-interpretable.

It does require a much stronger system-level condition than a monolithic black box normally provides:

> **Every semantically meaningful state that crosses an architectural boundary must be named, typed, inspectable, testable, and, where practical, causally intervenable.**

Desired specialist properties include:

```text
bounded responsibility
+ bounded information domain
+ known training lineage
+ explicit ontology
+ observable state transitions
+ measurable objective
+ calibrated uncertainty where claimed
+ reproducible behavior
+ interchangeable interface
```

Latent computation may exist inside a bounded component, but hidden state must not silently become authority for the system at large.

## Generality belongs to composition

Do not replicate general intelligence inside every MASI component.

A specialist should not be expected to know everything that another specialist or the control plane can supply. The system should achieve breadth by composing distinct competencies under explicit governance.

Examples:

- Precision may combine bounded evidence verification, constraint satisfaction, contradiction detection, and calibrated abstention without needing broad social or literary competence.
- Foresight may use causal models, simulation, quantitative forecasting, and uncertainty estimation rather than a language model merely prompted to "think ahead."
- Empathy may operate over explicit stakeholder, burden, agency, relational, and care-sensitive concepts rather than relying on generative tone or agreeableness.
- Wisdom may begin as an explicit outcome/credibility learner over prediction -> consequence records rather than as a "wise" language-model persona.
- Telos or another governance substrate may preserve intent, authority, permission, and legitimate change without acquiring epistemic truth merely because it coordinates execution.

These examples are illustrative, not canonical implementations.

## General-purpose models are components, not discarded competitors

The construction doctrine is **not anti-LLM** and does not require removing general-purpose models from MASI.

A useful operational framing is to treat a capable general-purpose language model as **general-purpose prior intelligence**: a broad learned instrument for answering what is plausible, commonly supported, linguistically coherent, worth proposing, or worth investigating next given its training distribution and current context.

"Average intelligence" may be a useful intuition, but it should not be interpreted as a literal statistical claim that an LLM computes the average human answer. The architectural point is that its output is a broad prior or proposal, **not automatically truth, authority, forecast, diagnosis, or permission**.

A general-purpose model may therefore be especially valuable for:

- translating messy human language into typed problem representations;
- translating structured specialist outputs back into human language;
- generating candidate hypotheses, decompositions, counterexamples, and questions;
- handling long-tail cases that fall between narrow specialists;
- discovering potentially relevant specialists, tools, or missing information;
- synthesizing specialist outputs while preserving provenance and disagreement;
- providing `CONTROL_A` and `CONTROL_B` baselines;
- helping research, code, test, and audit the MASI system itself.

The LLM should usually lose authority as the problem becomes more bounded and a purpose-built instrument becomes available.

A useful epistemic pattern is:

```text
messy request
    ↓
general-purpose prior / candidate generation
    ↓
purpose-built evidence, prediction, human-impact, or decision instruments
    ↓
explicit disagreement / correction / uncertainty
    ↓
governed result
```

This means an LLM can be indispensable glue without being the architecture's final epistemic authority.

The same principle applies to decision-native systems such as Jev. Jev should not be discarded merely because MASI targets purpose-built specialists. Where its public/contracted interface matches a bounded responsibility, it may be a useful component, comparator, sensor, or decision instrument. It remains interchangeable and subject to provider terms; it does not become canonical by convenience.

## How existing AI should be used

Existing models and systems are research specimens and engineering resources, not the default theory of cognition for MASI.

Classify discovered systems into one or more of the following:

### 1. Primitive worth inheriting

A useful mechanism or objective can be understood and reimplemented or incorporated cleanly, such as calibrated bounded judgment, concept bottlenecks, causal forecasting, contextual-bandit updating, structured abstention, or evidence-grounded classification.

### 2. Implementation worth adapting

An implementation is sufficiently transparent, licensed, bounded, and architecturally aligned that it can legitimately participate as a MASI candidate.

### 3. Benchmark / comparator only

A capable system is useful for establishing what the purpose-built specialist must equal, exceed, complement, or differ from, but its architecture should not be inherited by default.

### 4. Cautionary evidence

A system exposes technical debt, failure modes, opacity, training-lineage risks, source/authority confusion, state accumulation defects, hidden coupling, reward pathologies, calibration failures, or other properties MASI should explicitly engineer against.

The question is not "Which current model should become MASI?"

The question is:

> **What does this system teach us about the bounded intelligence we need to engineer, the baseline we must beat, the useful general capability we should retain, or the failure mode we must avoid?**

## Clean-room and legal discipline

The word "reverse engineer" in research discussion must not be treated as permission to violate licenses, provider terms, or law.

- Open-source/open-weight systems may be inspected, modified, and adapted only within their applicable licenses and terms.
- Published papers, documentation, benchmarks, and disclosed architectural ideas may be studied as prior art.
- Proprietary services may be used only as permitted by their agreements and public documentation.
- Do not perform prohibited reverse engineering, distillation, imitation training, source extraction, or publication of restricted benchmarks.
- A proprietary model can still teach MASI through public ideas, documented behavior, permitted experiments, and independently developed alternatives.

## Interface doctrine

Interchangeability is not satisfied merely because two models expose the same API endpoint.

A responsibility contract should expose semantic state that is independent of a specific implementation. The rest of MASI must not silently adapt to hidden representations or quirks of one candidate.

A specialist that cannot be replaced without rewriting the surrounding architecture has failed the interchangeability objective, regardless of its benchmark score.

## Agent instruction

Astra, Claude, GPT, or any other agent assisting this repository may use general-purpose models to research, code, critique, translate, generate fixtures, establish baselines, generate proposals, or bridge human language and typed system state.

They must **not** silently turn the current general-purpose model ecosystem into MASI's architecture, but they also must **not** remove useful LLM/Jev/generalist components merely to make the system appear more purpose-built.

Before implementing a specialist, the agent must state:

```text
responsibility:
allowed inputs:
native state / ontology:
outputs:
uncertainty / abstention semantics:
learning or update signal:
transparent baseline:
why additional complexity is necessary:
implementation class: CONTROL_A | CONTROL_B | MASI_TARGET | INFRASTRUCTURE
```

If these cannot yet be stated, implementation should stop at research/prototyping rather than hardening an accidental architecture.

For any general-purpose or external decision component retained in the architecture, also state:

```text
component role:
why breadth/generalization is useful here:
what authority it does NOT have:
what bounded specialist may override/correct it:
what provenance is preserved:
```

## Doctrine reconciliation checkpoint — required before further Sprint 001 implementation

The first Astra block began before this doctrine was made explicit enough. **Do not continue new implementation work until the existing first-block artifacts have been reconciled against this document.**

At the start of the next Astra session:

1. read this file before all other implementation work;
2. inspect every artifact created or changed in the first Astra block;
3. classify each artifact as `CONTROL_A`, `CONTROL_B`, `MASI_TARGET`, or `INFRASTRUCTURE`;
4. identify any assumption that a fine-tuned/pretrained general model is the intended final specialist;
5. identify any hidden coupling to one model family, tokenizer, representation, provider, or training stack;
6. identify any complexity that was added without a demonstrated capability deficit;
7. identify any useful generalist/LLM/Jev function that should be retained as a bounded component rather than removed reflexively;
8. preserve useful code, but relabel, narrow, or refactor anything whose architectural status was overstated;
9. record the reconciliation result in GitHub before beginning the next work packet.

The purpose is not to discard useful first-session work. It is to ensure that experimental scaffolding and general-model baselines do not become the architecture by inertia, while also preserving broad general capability where it solves a real integration problem.

## Permanent test

Before accepting a major MASI implementation decision, ask both questions:

> **If today's dominant LLM architecture did not exist, would we still design this specialist this way from the responsibility outward?**

and

> **If we removed the general-purpose model entirely, what useful breadth, translation, hypothesis-generation, or long-tail capability would we now have to rebuild badly by hand?**

A good MASI design should survive both tests: specialists should not be accidental narrowed LLMs, and the architecture should not discard useful general-purpose intelligence merely for ideological purity.
