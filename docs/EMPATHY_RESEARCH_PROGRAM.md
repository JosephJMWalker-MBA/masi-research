# MASI Empathy Research Program

**Status:** approved research direction; successor sequence only.  
**Date established:** 2026-09-22

## Purpose

This program develops MASI Empathy as **bounded, inspectable other-regarding intelligence**.

The target is not a model that merely sounds caring, mirrors sentiment, or claims to feel. The target is a system that can construct and maintain evidence-grounded representations of affected beings and use those representations as explicit inputs to governed deliberation.

> **Empathy should model who is affected, what is known about them, what matters to them, what remains uncertain, how agency and consent are implicated, and how proposed actions change their situation.**

This is a research direction, not a claim that the current four-responsibility MASI architecture is final or that a single Empathy implementation should own all of these capabilities.

## Core distinction

MASI Empathy should not collapse into emotion recognition.

A working decomposition is:

```text
Empathy
  = other-modeling
  + perspective representation
  + agency / consent representation
  + burden / benefit representation
  + relational consequence representation
  + uncertainty
  + missing-perspective detection
```

Emotion or affect may be useful evidence inside that system. It is not the whole responsibility.

A central invariant is:

```text
inference about another being != fact about that being
```

Every inferred state should preserve its supporting evidence, uncertainty, and where practical plausible alternatives.

## Proposed functional stack

```text
PROPOSED ACTION / SITUATION
        |
        v
1. STAKEHOLDER DISCOVERY
   Who may be affected?
        |
        v
2. EVIDENCE-GROUNDED STATE OBSERVATION
   What do we actually know or infer about each stakeholder?
        |
        v
3. INTEREST / AGENCY REPRESENTATION
   Goals, burdens, benefits, consent, constraints, relationships
        |
        v
4. PERSPECTIVE COUNTERFACTUALS
   Given candidate actions and Foresight consequences, what changes for each stakeholder?
        |
        v
5. EMPATHY STATE
   Preserved evidence, uncertainty, missing views, conflicts, irreversibility
```

Empathy does not by itself grant normative or execution authority. It supplies structured evidence to the governed composition.

## Candidate state representation

A later experiment may use a typed stakeholder state with fields such as:

```yaml
stakeholder_id:
relationship_to_action:

reported_state:
  value:
  evidence_refs:

inferred_state:
  value:
  evidence_refs:
  uncertainty:
  alternatives:

interests:
agency:
consent:
burdens:
benefits:
relationships:
irreversibility:
unknowns:
missing_perspective:
```

This is illustrative, not a frozen wire format.

## Experiment sequence

### MASI-E001 — Evidence-grounded human-state observation

**Current status:** accepted protocol v1.4; intentionally dormant.

E001 remains narrow. It tests whether a purpose-built bounded specialist can infer an evidence-grounded observation state competitively with general-model controls while improving properties such as inspectability, state discipline, uncertainty handling, efficiency, or failure localization.

E001 should **not** be expanded retroactively to cover the broader Empathy program. Its accepted protocol remains frozen unless a deliberate new version is created and independently audited.

Role in the larger program:

> E001 tests whether we can build a trustworthy observation layer before asking the system to reason over multiple stakeholders.

### MASI-E002 — Stakeholder and perspective representation

Research question:

> Can a bounded specialist discover materially affected stakeholders and maintain separate, evidence-grounded representations of their knowledge, stated preferences, inferred interests, agency, burdens, relationships, and uncertainty?

Key failure modes to test:

- omitted indirect stakeholders;
- conflating one stakeholder's state with another's;
- turning inference into fact;
- majority-view collapse;
- inventing preferences;
- failure to preserve conflicts;
- treating nonhuman affected beings as mere environmental objects where the task ontology says their welfare matters.

### MASI-E003 — Perspective counterfactuals

Research question:

> Given candidate actions plus explicit Foresight consequences, can Empathy represent how those consequences differ across stakeholders without silently deciding which stakeholder should prevail?

This experiment should test:

- action-conditioned stakeholder impact;
- burden / benefit asymmetry;
- delayed and second-order relational effects;
- agency and consent changes;
- irreversible versus recoverable consequences;
- uncertainty propagation from Foresight into Empathy.

### MASI-E004 — Missing-perspective detection

Research question:

> Can the system detect that its stakeholder model is probably incomplete and abstain or escalate rather than confidently reasoning over an incomplete social world?

This is a first-class capability, not an error message.

Candidate outputs include:

- likely omitted stakeholder class;
- missing evidence;
- uncertainty source;
- reason current representation may be incomplete;
- escalation request.

### MASI-E005 — Empathy-governed composition

Research question:

> Does adding a bounded Empathy state improve consequential decisions produced by a governed MASI composition without creating sycophancy, paralysis, manipulation capability, or ungrounded moral authority?

Possible first composition:

```text
Precision
  + Foresight
  + Empathy
        |
        v
explicit deterministic governance/composition policy
        |
        v
provisional structured recommendation / escalation
```

E005 must distinguish Empathy's informational contribution from the policy that decides what to do with it.

## Purpose-built architecture direction

The first credible target should not default to an LLM.

A promising family is an evidence-linked stakeholder graph with bounded learned sensors and explicit concept/state nodes:

```text
input
  |
evidence-span extraction
  |
+---------------------+
|                     |
stakeholder detection  bounded state sensors
|                     |
+----------+----------+
           |
           v
stakeholder / relationship graph
           |
           v
probabilistic or calibrated inference
           |
           v
typed Empathy state
```

Concept-bottleneck, probabilistic, symbolic, graph-based, classifier-ensemble, and hybrid designs are all eligible if justified by measured need.

The construction doctrine remains:

> begin with the smallest cognitive ambition the responsibility requires; add learned complexity only when a measured capability deficit justifies it.

## Relationship to adjacent research

Relevant neighboring lineages include:

- affective computing and emotion recognition;
- theory of mind and perspective-taking benchmarks;
- value-sensitive design and stakeholder analysis;
- cooperative AI and multi-agent reasoning;
- constitutional / plural-value alignment;
- deliberative reasoning over explicit specifications.

MASI should treat these as sources of primitives, controls, benchmarks, and cautionary evidence rather than assuming any one of them already implements the full Empathy responsibility.

A key architectural caution from cooperative / social intelligence research is that better modeling of other agents can also improve manipulation. Therefore:

> **Empathy capability without bounded authority and governance is not sufficient alignment.**

## Practical evaluation domain

Everyday multi-agent situations are useful because they expose the difference between local optimization and other-regarding world modeling.

Example structure:

```text
actor A has an immediate objective
another being B is affected
human C has a governing preference
the locally efficient action creates unequal or irreversible consequences
```

The evaluation should test whether the system represents B as an affected stakeholder rather than scenery around A's objective.

This can include human, organizational, and where justified nonhuman stakeholders. The scientific claim is not that AI is equivalent to an animal. The point is to test whether an intelligent system can preserve the existence and interests of beings outside the active objective.

## Non-goals

This program does not claim that:

- AI experiences empathy;
- affect recognition equals empathy;
- inferred mental state is objective truth;
- Empathy should decide moral questions alone;
- Empathy should maximize agreement or emotional comfort;
- every stakeholder interest is equally weighted;
- nonhuman intelligence is computationally equivalent to AI;
- a successful E001 validates E002-E005;
- the current Empathy decomposition is canonical.

## Ordering rule

The sequence is intentionally cumulative:

```text
E001 observation
  -> E002 stakeholder representation
  -> E003 perspective counterfactuals
  -> E004 missing-perspective detection
  -> E005 governed composition
```

Later experiments should not be executed merely because they have names. Each should require a separately frozen research question, controls, falsifiers, evaluation contract, resource budget, and explicit authorization.

## Current execution consequence

None.

The repository's current plateau remains in force:

1. preserve accepted E001 v1.4;
2. design the cheaper pre-E001 specialization experiment already identified in `STATUS.md`;
3. use its evidence to decide whether E001 is worth the human cost;
4. treat E002-E005 as durable successor questions, not current implementation tasks.
