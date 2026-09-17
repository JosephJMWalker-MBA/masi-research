# Human Knowledge Compilation — From Ordinary AI Use to Purpose-Built Specialist

**Status:** proposed experimental track  
**Date:** 2026-09-17

## Research pressure

Classical expert systems and blackboard architectures were constrained not only by compute, but by the cost of knowledge engineering: domain expertise had to be elicited, formalized, implemented, tested, and maintained by scarce specialists.

Modern general-purpose AI and coding agents may change that economics.

The proposed MASI construction loop is:

```text
ordinary human AI use
(ChatGPT / Claude / equivalent)
        ↓
conversation, examples, corrections,
exceptions, uncertainty, decisions
        ↓
Hermeneia-like interpretive governance
        ↓
explicit epistemic objects and lineage
        ↓
Memory Lab-like continuity / reassessment
        ↓
current knowledge + historical context + delta
        ↓
compact specialist-construction package
        ↓
Codex / coding agent
        ↓
purpose-built bounded specialist
        ↓
tests + human review + field outcomes
        ↓
new conversation / correction / evidence
        ↺
```

The hypothesis is **not** that chat history itself is a specialist.

The hypothesis is that ordinary AI-assisted work can become a low-friction knowledge-acquisition surface, while governed interpretation, epistemic continuity, and coding agents convert selected durable knowledge into a testable bounded intelligence.

## Why the governance layers matter

A raw conversation mixes epistemically different things:

- source evidence;
- human observations;
- human claims;
- AI proposals;
- hypotheses;
- examples;
- counterexamples;
- uncertainty;
- decisions;
- corrections;
- later changes of mind;
- accepted and rejected suggestions.

A specialist must not inherit these as an undifferentiated corpus.

The conversion path therefore needs to preserve distinctions such as:

```text
what the source showed
!= what the human asserted
!= what the AI proposed
!= what the human accepted
!= what remained unresolved
!= what later evidence supported
!= what was later corrected or narrowed
```

Hermeneia is a candidate interpretive substrate because it already separates source, observation, machine proposal, interpretation, stewardship, synthesis, expression, and evaluation while preserving ancestry.

Memory Lab is a candidate continuity substrate because it separates canonical source, retrieval machinery, and derived interpretations; preserves historical state; supports reassessment; and treats changes as deltas rather than requiring a full corpus rebuild.

Neither repository is presumed to be the final runtime. They are existing research substrates whose tested distinctions can reduce reinvention.

## Proposed role of the general-purpose model

The general-purpose model is useful here as a **knowledge-acquisition and translation instrument**.

It may:

- help a human articulate tacit distinctions;
- ask for examples and counterexamples;
- surface apparent contradictions;
- propose candidate concepts;
- translate ordinary language into candidate schemas;
- identify missing conditions;
- help distinguish stable rules from unresolved hypotheses;
- generate candidate test fixtures;
- explain specialist behavior back to the human.

It does not gain authority merely because it participated in the conversation.

A useful pattern is:

```text
human expertise
    +
general-purpose conversational assistance
    +
governed interpretation
    +
epistemic continuity
    +
coding-agent compilation
        ↓
purpose-built specialist
```

## Specialist-construction package

The bridge into a coding agent should be deliberately compact. It should not repeatedly send the entire conversation history.

A candidate package may contain:

```text
AGENTS.md
SPECIALIST_SPEC.md
DOMAIN_ONTOLOGY.yaml
CONTRACT.yaml
CURRENT_KNOWLEDGE.md
UNKNOWNS.md
PROVENANCE.jsonl
FIXTURES/
NEGATIVE_CONTROLS/
TESTS/
CHANGELOG.md
DELTA.md
```

The exact artifact names are not canonical. The required semantic content is more important than file layout.

### Stable core + delta

The default update pattern should be:

```text
stable specialist knowledge package
        +
small provenance-bearing knowledge delta
        ↓
coding agent identifies affected artifacts only
        ↓
proposed patch + tests
        ↓
human review
        ↓
new specialist version
```

This is intended to reduce token use, prevent unnecessary rewrites, and preserve the difference between historical knowledge and current participation.

## First experiment — MASI-K001

### Question

Can governed conversion of ordinary AI-assisted domain reasoning produce a more faithful, maintainable, and auditable specialist than directly giving a coding agent raw or summarized chat history?

### Candidate conditions

```text
K0  human writes a minimal specialist specification manually
K1  raw chat-history package -> coding agent
K2  ordinary AI summary / compression -> coding agent
K3  governed pipeline:
    conversation
    -> Hermeneia-like epistemic separation
    -> Memory Lab-like continuity / delta
    -> compact construction package
    -> coding agent
```

K0 is useful as a human-effort baseline, not necessarily a performance ceiling.

### Hold constant where practical

- the same domain material;
- the same coding agent family/version;
- the same specialist responsibility;
- the same held-out fixtures;
- the same allowed implementation budget;
- the same human reviewer.

### Measure

At minimum:

- specialist task quality on held-out cases;
- knowledge fidelity to human-stewarded material;
- leakage of unaccepted AI proposals into implemented behavior;
- preservation of uncertainty and abstention;
- provenance recoverability;
- contradiction / supersession handling;
- update locality after one material knowledge change;
- token/context cost of the coding-agent package;
- human correction burden;
- reproducibility of the resulting specialist build;
- number and severity of regressions after incremental update.

## Update-locality test

The experiment should include at least one staged change after the first specialist build.

Example:

```text
v1 knowledge:
rule R applies broadly

later conversation / evidence:
R should apply only under condition C
```

The pipeline should preserve:

```text
historical R
new qualification C
reason for change
supporting source / conversation provenance
current-view effect
```

Then the coding-agent package should identify only the specialist artifacts plausibly affected by the change and generate regression tests for the old and new boundary cases.

A pipeline that requires resending or reinterpretating the entire corpus for every change has not yet solved the maintenance problem.

## Human interaction design

The intended end-user experience should remain much simpler than the internal machinery.

A person should be able to use AI normally. Friction should concentrate around moments when conversational material is proposed for durable specialist knowledge.

Candidate interactions:

```text
"This appears to be a durable domain rule. Should it be retained?"
[accept] [qualify] [leave unresolved] [reject]

"This conflicts with an earlier retained rule. What changed?"
[earlier rule was wrong]
[conditions changed]
[both are context-dependent]
[not enough evidence]
```

The exact UI is future work. The research requirement is that the system not silently convert conversational fluency into specialist authority.

## Relationship to MASI construction doctrine

This track extends specialization-by-construction.

The domain expert need not become an ML engineer. The coding agent need not become the domain authority. The conversation model need not become the specialist.

Instead:

```text
human supplies / develops domain knowledge
Hermeneia-like layer disciplines interpretation
Memory Lab-like layer preserves continuity and change
coding agent compiles governed knowledge into technical artifacts
MASI evaluates and composes the resulting specialist
```

The specialist remains responsible for one bounded function and must still satisfy the normal MASI construction gate:

```text
responsibility
allowed inputs
native state / ontology
outputs
uncertainty / abstention
learning or update signal
transparent baseline
complexity justification
```

## Repositories as research instruments

This experiment deliberately reuses existing repositories rather than treating each repository as a permanent product obligation.

A repository may function as:

- a research site where one distinction is isolated;
- a reusable conformance harness;
- a source of schemas, tests, or protocols;
- a historical record of a failed approach;
- a component that participates in a later experiment;
- a substrate that is eventually replaced after its useful knowledge is extracted.

The burden is not the count of repositories. The burden is unmanaged duplication, ambiguous authority, or architecture that cannot explain why a repository still exists.

The MASI research program should therefore mine prior repositories for validated distinctions and reusable artifacts while allowing their implementation status to narrow, plateau, merge, or become historical evidence.

## Stop / falsification conditions

Narrow or reject this pipeline if controlled experiments show that:

- raw or ordinary summarized chat performs equivalently with materially less human effort;
- governance layers do not reduce AI-proposal leakage or knowledge loss;
- incremental deltas do not reduce update cost or regressions;
- provenance does not improve debugging or correction;
- the resulting artifact is merely a personalized generalist rather than a bounded specialist;
- the human review burden is too high to be practical;
- existing knowledge-engineering tooling already provides the same end-to-end capability more simply.

## Iteration doctrine

The first implementation is an experiment, not the product architecture.

Build the smallest end-to-end slice capable of producing evidence. Then use the observed friction, failures, omissions, token costs, human corrections, and specialist behavior to determine the next iteration.

The first result should teach the next design.
