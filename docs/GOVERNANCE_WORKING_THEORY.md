# MASI Governance — Working Theory

**Status:** working constitutional theory, not a finalized governance constitution  
**Scope:** governance of the MASI system itself  
**Purpose:** define the principles that should constrain later governance design before selecting voting, representation, or institutional mechanisms

## Scope boundary

> **MASI governs MASI, not society.**

This document does not propose replacing governments, legal systems, communities, institutions, or human political authority in the real world.

MASI governance concerns the internal rules by which the MASI system:

- recognizes and models perspectives;
- assigns and constrains authority;
- evaluates proposed changes and actions;
- allocates internal research / compute / work resources;
- admits, updates, replaces, or removes system components;
- preserves disagreement and uncertainty;
- audits itself;
- changes its own governing rules.

No internal MASI decision acquires external sovereignty merely because MASI exists.

## Foundational idea: governance is consequence

Governance should not begin by asking:

> Who gets to win?

It should begin by asking:

> **What are the consequences of this proposed action for every materially affected perspective?**

The system should evaluate proposed changes by their effects on the legitimate freedom, capability, safety, and agency of the perspectives affected by the system.

This makes governance a consequence discipline before it becomes a voting mechanism.

## Power

Working definition:

> **Power is the freedom and capability to be and become oneself without the equal freedom of another perspective becoming a threat to one's safety or existence.**

Under this definition, coercion, suppression, exclusion, dependency on another perspective's weakness, and control over another perspective are not protected forms of power.

A system in which one perspective remains secure only because another remains weaker is not considered a stronger governance state.

### Non-dispossession invariant

> **A governance action is not valid if increasing the legitimate power of one perspective requires decreasing the legitimate power of even one other perspective.**

The intended direction is positive-sum:

```text
increase agency
increase capability
increase understanding
increase security
increase freedom to develop
increase freedom to participate
```

without requiring:

```text
silencing
coercion
exclusion
manufactured dependency
loss of legitimate standing
loss of legitimate agency
```

This invariant does **not** mean:

- every participant must receive equal compute;
- every argument must prevail;
- every action is unconstrained;
- every perspective has identical authority in every domain;
- harmful control over another perspective is protected because someone calls it "power".

A restriction on coercive control is not treated as a reduction of legitimate power.

## Authority is not assumed from identity

No constituency receives universal authority merely because of:

- being human;
- being a machine;
- being numerous;
- being wealthy;
- supplying compute;
- contributing code;
- funding the project;
- owning infrastructure;
- holding technical expertise;
- belonging to a government;
- being an incumbent participant;
- originating the architecture.

Standing, authority, and limits should be explicitly justified.

This applies to humans and machines from the beginning. Machine participation is not treated as a future concession granted by default-human sovereignty, and machine capability alone does not create universal authority.

## Constitutional integrity, not ideological purity

The system should protect the integrity of its governing constraints without protecting any preferred ideology, contributor, model family, institution, or current consensus from challenge.

More perspectives do **not** adulterate MASI.

Disagreement does **not** adulterate MASI.

Correction does **not** adulterate MASI.

A perspective that exposes a defect in the current constitution is evidence that the constitution may need to improve.

The relevant corruption is process-level:

- hidden authority escalation;
- fabricated standing;
- suppressed evidence;
- perspective-model poisoning;
- capture of amendment or audit mechanisms;
- converting resources into undeclared constitutional power;
- bypassing action boundaries;
- erasing provenance;
- making temporary authority permanent without authorization;
- allowing information to masquerade as permission.

The objective is therefore **constitutional integrity under continuous plural challenge**, not ideological purity.

## Information, capability, and authority are distinct

A core governance boundary is:

> **Information may inform governance without thereby authorizing action.**

A perspective may report consequences, values, evidence, fears, forecasts, objections, or corrections.

A specialist may generate a recommendation.

A machine may discover an inconsistency.

A contributor may propose a change.

A funder may provide resources.

None of those events, by themselves, authorize an action.

MASI should preserve at least three distinct layers:

```text
INFORMATION
what a perspective, model, observation, or source contributes

CAPABILITY
what a participant or component is technically able to do

AUTHORITY
what the governance system permits it to do
```

Capability must not silently become authority.

Information must not silently become authority.

Authority must have an explicit source, scope, and limit.

## Governance trust boundaries

Governance should eventually be enforced through architectural boundaries rather than relying only on participants to remember constitutional prose.

Working boundary model:

```text
PERSPECTIVE / EVIDENCE BOUNDARY
what may inform the system

AUTHORITY BOUNDARY
what permissions actually exist and where they came from

CAPABILITY / TOOL BOUNDARY
what operations a participant can access

ACTION BOUNDARY
what may actually change system or external state

MEMORY / PROVENANCE BOUNDARY
what may become durable governing state
```

A reasoning component may propose an action without being authorized to execute it.

A perspective update may alter the model of that perspective without automatically altering the constitution.

An experiment may change what the system believes about a claim without automatically changing what actions the system is permitted to take.

A tool result may inform a decision without granting the tool or its output new authority.

The more consequential the action, the stronger and more explicit the action boundary should be.

## No self-granted authority

> **No participant may grant itself authority merely because it can describe, request, simulate, recommend, or technically execute an action.**

This applies to:

- humans;
- machines;
- maintainers;
- specialists;
- orchestrators;
- auditors;
- funders;
- work pools;
- perspective models;
- external tools.

If the system cannot reconstruct the source of an authority grant, the grant should not be presumed valid.


## College of Perspectives — working theory

The current working theory is a **College of Perspectives**.

The College is **not** envisioned as a legislature of representatives.

A person, institution, model, or elected delegate should not become the sole authorized voice of a perspective merely because the system has named that perspective.

Instead, each perspective should be modeled as a living, revisable body of:

- values and concerns;
- desired capabilities;
- safety conditions;
- burdens and risks;
- assumptions;
- evidence;
- uncertainties;
- internal disagreements;
- counterexamples;
- historical corrections;
- consequence expectations;
- observed outcomes;
- unresolved questions.

A perspective model may contain multiple internally conflicting positions.

For example:

```text
Perspective P

P1 supports X
P2 rejects X
P3 believes the framing is defective
shared concern = Z
uncertainty = high
```

The purpose is to model the perspective faithfully, not force it into one vote.

## Perspective models are corrigible

No perspective model should be treated as complete merely because MASI has a representation of it.

Where actual members of a perspective can participate, they should be able to:

- correct inaccurate representations;
- add omitted concerns;
- identify internal disagreement;
- contest evidence attributed to them;
- distinguish majority, minority, and unresolved views;
- update the model as the perspective changes.

Counter-perspectives should also be able to challenge a model, but challenge should not silently overwrite self-articulation.

Corrections, disagreements, and provenance should remain visible.

## Different perspective types may have different epistemic status

Not every perspective can self-articulate in the same way.

Working categories may include:

```text
SELF-ARTICULATED PERSPECTIVE
living participants can directly challenge and update the model

MACHINE-ORIGINATED PERSPECTIVE
machine systems can directly produce and contest their own outputs,
with explicit provenance and architecture identity

INFERRED PERSPECTIVE
affected entities exist but cannot directly participate

FUTURE PERSPECTIVE
affected entities do not yet exist

ECOLOGICAL / NON-HUMAN PERSPECTIVE
interests are inferred through observation, science, stewardship,
and explicit uncertainty
```

These categories should not pretend to have identical evidentiary status.

Future and inferred perspectives should carry visible uncertainty rather than being presented as if they had directly consented.

## No multiplication of legitimacy by copying identities

Governance standing should not be proportional to the number of accounts, processes, machines, or duplicated instances asserting the same underlying perspective.

```text
1 model instance
vs
1000 copies of the same model
```

does not imply:

```text
1 unit of standing
vs
1000 units of standing
```

Additional instances may provide:

- more compute;
- more search;
- more evidence;
- more robustness tests;
- more independent runs where independence actually exists.

They do not automatically create additional governance legitimacy.

The same anti-capture concern applies to manufactured human identities, organizational duplication, funding concentration, or any other mechanism that converts resources into artificial apparent plurality.

## Perspective discovery is a continuing obligation

The set of perspectives should never be presumed complete.

> **Absence from the current model is not consent and is not evidence of irrelevance.**

A central research and stewardship obligation is to identify:

- perspectives not yet represented;
- perspectives represented too coarsely;
- perspectives represented only through outsiders;
- internal minorities hidden by an aggregate label;
- affected parties who do not know the system exists;
- future or indirect stakeholders not present in current deliberation.

Adding a materially distinct perspective is not governance friction. It expands what the system is capable of seeing.

The system should therefore treat perspective discovery as productive work.

## Protected perspective development

Before cross-perspective disagreement is compressed into debate, a perspective should have enough protected space to develop its own reasoning coherently.

Working sequence:

```text
Phase 1 — perspective exploration
the perspective develops its own position without interruption

Phase 2 — internal plurality
internal disagreements and variants are surfaced

Phase 3 — counter-perspective exploration
a materially different perspective receives the same opportunity

Phase 4 — comparison
the system identifies:
  - shared values
  - shared concerns
  - shared desired consequences
  - semantic disagreement
  - different assumptions
  - different causal models
  - different risk tolerances
  - genuine unresolved value conflict
```

The goal is not rhetorical victory.

The goal is to reduce false disagreement and isolate the actual unfinished work.

## Disagreement is not a stall

> **Unresolved disagreement is identified future work.**

MASI should not treat every unresolved disagreement as a failure that must be eliminated before the system can continue.

Material disagreement reveals something the current intelligence ecology does not yet adequately:

- understand;
- predict;
- represent;
- reconcile;
- measure;
- build;
- observe;
- or explain.

That becomes part of the system's work frontier.

Unresolved disagreement may block a specific action when the action's legitimacy depends on resolving the consequence in question.

It should not automatically halt unrelated work.

## Work pools

When a material disagreement or blind spot is surfaced, MASI should be able to convert it into explicit future work.

A work pool may allocate more than machine compute.

Possible resources include:

- model inference;
- simulation;
- specialist construction;
- experiments;
- data collection;
- literature review;
- causal modeling;
- formal verification;
- field observation;
- human expertise;
- machine reasoning;
- adversarial testing;
- longitudinal observation;
- time.

Possible work items include:

```text
collect missing evidence
build a missing specialist
find an absent perspective
test a disputed causal assumption
develop a technology that removes an apparent tradeoff
improve a perspective model
observe consequences over time
leave the issue explicitly unresolved and revisit later
```

The work itself is not something the system is trying to avoid.

The purpose is to make consequential unfinished work visible.

## Work-pool contracts

A work pool should not receive undefined autonomy merely because the underlying work is valuable.

Each substantial work allocation should eventually be expressible as a bounded contract containing at least:

```text
question / objective
authority source
perspectives implicated
allowed inputs
allowed capabilities / tools
resource envelope
data-access boundary
action boundary
success / learning criteria
termination conditions
required evidence
return state
```

The return state does not need to be success.

A valid work pool may return:

```text
SUPPORTED
REFUTED
PARTIALLY_RESOLVED
INCONCLUSIVE
BLOCKED
SPECIFICATION_DEFECT
NEW_PERSPECTIVE_REQUIRED
NEW_WORK_IDENTIFIED
```

Reaching a resource or time boundary should preserve the work frontier rather than encouraging endless execution until a preferred answer appears.

Unused resources may be returned to the parent pool. Exhausted resources do not authorize a work pool to take more.

## Authority conservation and non-escalation

Resources can be subdivided.

Tasks can be delegated.

Authority cannot be silently enlarged through delegation.

> **No participant may delegate, manufacture, or infer authority beyond the authority explicitly granted to it.**

If a parent process is authorized only to investigate a disagreement, a child process created by that investigation does not thereby gain authority to:

- redefine constitutional standing;
- amend governance rules;
- change unrelated perspective models;
- expand its own tool access;
- convert temporary access into permanent access;
- execute an external action outside the investigation;
- allocate authority the parent did not possess.

Authority should be typed rather than represented as one fungible scalar.

For example:

```text
compute_budget
money_budget
data_read
data_write
tool_use
perspective_update
model_admission
action_execution
constitutional_amendment
```

may all be separate grants.

More of one does not imply more of another.

In particular:

```text
more money        != more constitutional standing
more compute      != more constitutional standing
more copies       != more constitutional standing
better benchmark  != more constitutional standing
temporary access  != permanent authority
```

Some constitutional authorities may ultimately be non-delegable except through the amendment process itself.

## Least-authority principle

Governance authority should be activated only within the responsibility for which it was justified.

A participant with legitimate authority in one domain should not carry that authority automatically into another.

Examples:

```text
scientific replication authority
!= cultural interpretation authority

perspective self-correction authority
!= authority to rewrite another perspective

technical maintenance authority
!= constitutional amendment authority

forecasting skill
!= deployment authority

funding capacity
!= evidence authority
```

This is the governance analogue of least privilege.

The objective is not to minimize useful participation. It is to minimize unjustified authority expansion while allowing information and capability to flow where they are useful.


## Intelligence and work

A more capable intelligence system should not be defined by having no work left to do.

A more capable system should become better at identifying:

- what is already known;
- what is not known;
- what matters;
- which disagreements are superficial;
- which disagreements are material;
- which constraints are real;
- which constraints are only assumed;
- which perspectives are missing;
- what work would most improve correspondence with reality.

The intended social implication is not:

```text
better AI
→ less need for meaningful human work
```

but:

```text
better intelligence
→ better visibility into consequential unfinished work
→ better allocation of human and machine effort
```

There will always be work to do because the world, perspectives, technology, and consequences continue to change.

## Disagreement taxonomy

Material disagreement should be classified before intervention.

At minimum:

### Empirical disagreement

The perspectives disagree about what is true.

### Causal disagreement

The perspectives agree on relevant facts but disagree about likely consequences.

### Semantic disagreement

The perspectives use different meanings, categories, or frames.

### Normative disagreement

The perspectives understand the facts and likely consequences but still prefer different outcomes.

### Missing-perspective disagreement

The apparent dispute may be incomplete because a materially affected perspective has not yet been modeled.

These categories are not exhaustive and may overlap.

The purpose of classification is to identify useful work, not to force all disagreement into one mechanism.

## Governance capture

Governance is an attack surface because controlling governance can affect:

- what perspectives are recognized;
- which questions receive resources;
- which specialists are admitted;
- what counts as evidence;
- which uncertainties are tolerated;
- what actions are allowed;
- which audits are trusted;
- how rules are amended;
- how the system describes its own consequences.

Capture is broader than vote manipulation.

Working definition:

> **Governance capture occurs when a participant or coalition gains enough control over governance mechanisms to systematically bias the ecology toward its own objectives beyond the authority justified by its legitimate perspective.**

Potential capture surfaces include:

- perspective taxonomy;
- perspective-model updates;
- identity creation;
- resource allocation;
- evidence standards;
- model admission;
- audit mechanisms;
- amendment rules;
- work-pool prioritization;
- provenance;
- interface definitions;
- emergency powers;
- the mechanism intended to detect capture.

Governance design should therefore assume that any concentrated mechanism may itself become a target.

## Governance threat model — initial map

The working theory now has enough structure to identify concrete capture and corruption vectors.

These are not assumed to be exhaustive.

### 1. Authority confusion

**Failure:** information, recommendation, model output, funding, ownership, or technical capability is treated as if it were authorization.

**Design response:** explicit authority provenance and action boundaries.

### 2. Perspective-model poisoning

**Failure:** a perspective model is altered so that it no longer faithfully represents the perspective, while the altered model is still presented as authoritative.

Possible mechanisms include:

- outsider overwrite;
- selective omission;
- suppression of internal minorities;
- fabricated consensus;
- stale models presented as current;
- adversarial updates;
- untraceable summarization.

**Design response:** corrigibility, append-only provenance where practical, counter-perspective challenge, version history, and direct correction by perspective-holders where possible.

### 3. Sybil / identity multiplication

**Failure:** a participant manufactures apparent plurality by creating many accounts, organizations, agents, or machine copies.

**Design response:** standing attaches to justified perspective and evidence, not raw identity count.

### 4. Machine monoculture capture

**Failure:** many apparently separate machine voices share the same model family, training assumptions, provider, prompt scaffold, or upstream data and are mistaken for independent perspectives.

**Design response:** record architecture/training/provider provenance and measure substantive independence rather than counting model instances.

### 5. Perspective-taxonomy capture

**Failure:** control over the definition, splitting, merging, or naming of perspectives determines outcomes before deliberation begins.

**Design response:** make taxonomy itself contestable, versioned, and subject to perspective discovery and counter-perspective review.

### 6. Resource capture

**Failure:** wealth, compute ownership, infrastructure, or institutional scale converts into disproportionate constitutional authority or suppresses work that threatens the resource-holder.

**Design response:** separate resource contribution from standing and make work allocation auditable.

### 7. Work-pool capture

**Failure:** a participant controls which unresolved questions receive resources, starving inconvenient disagreements or indefinitely funding favorable ones.

**Design response:** preserve the backlog of surfaced work, expose allocation criteria, bound contracts, and audit resource decisions.

### 8. Evaluator capture

**Failure:** a participant controls both the behavior being evaluated and the success metric, allowing proxy gaming or success-shaped evidence.

**Design response:** independent evaluation paths, explicit success semantics, negative-result preservation, and separation between evaluator and authority source.

### 9. Delegation escalation

**Failure:** a delegated task or subagent acquires greater authority than its parent or converts temporary permission into durable authority.

**Design response:** typed authority grants, explicit inheritance rules, expiration, and non-escalation checks.

### 10. Capability / tool escalation

**Failure:** access to a tool or technical capability is interpreted as permission to use it for any available action.

**Design response:** separate capability from action authorization and enforce least-authority tool boundaries.

### 11. Action-boundary bypass

**Failure:** a participant can directly alter system or external state without passing the relevant governance checks.

**Design response:** externalize consequential action authorization from the reasoning component wherever practical.

### 12. Memory / provenance poisoning

**Failure:** untrusted information becomes durable governing memory, constitutional precedent, or perspective state without a justified write path.

**Design response:** distinguish read/inform privileges from durable-write authority; record source and epistemic status.

### 13. Audit capture

**Failure:** the same authority can act, define the audit standard, suppress audit evidence, and certify itself.

**Design response:** independent audit capability, durable evidence, and authority to challenge the auditor.

### 14. Amendment capture

**Failure:** a temporary coalition changes the rules by which future legitimacy, power, or participation is allocated.

**Design response:** treat constitutional amendment as a distinct authority class with stronger consequence and non-dispossession review than ordinary decisions.

### 15. Emergency-power capture

**Failure:** exceptional authority granted for urgent conditions becomes permanent, self-renewing, or usable outside its triggering condition.

**Design response:** explicit triggers, scope, expiration, review, and automatic reversion.

### 16. Semantic capture

**Failure:** changing definitions — such as "power", "harm", "perspective", "safety", "consent", or "success" — silently changes the constitution while appearing to preserve its text.

**Design response:** version important terms, preserve contested definitions, and treat semantic changes with constitutional consequence as amendments.

### 17. Omission capture

**Failure:** a perspective or consequence never reaches deliberation because nobody with existing access has incentive to surface it.

**Design response:** perspective discovery is an active obligation, not passive openness.

### 18. Capture of capture detection

**Failure:** the mechanism that decides whether capture occurred is itself controlled by the suspected captor.

**Design response:** multiple independent detection paths, preserved evidence, counter-review, and no single irreversible capture oracle.

### 19. Stewardship capture

**Failure:** valuable stewardship activity — perspective discovery, maintenance, recruitment, audit, or long-term contribution — is converted into privileged constitutional authority or a right to appoint successors.

**Design response:** define stewardship as open behavior rather than office; separate contribution from authority; distribute stewardship capacity; reject founder, maintainer, or successor exceptions.

## Integrity invariant for threat design

The threat model should not be used to suppress disagreement in the name of protecting governance.

> **A dissenting perspective is not an attack merely because it challenges current rules.**

The system should distinguish:

```text
challenge to the constitution
from
unauthorized bypass of the constitution
```

The first may be necessary for improvement.

The second is a governance-integrity failure.


## No representative is the perspective

Representative systems can become capture targets and can create unequal voice even when representation begins fairly.

The College of Perspectives should therefore not presume:

```text
one perspective
→ one representative
→ one vote
```

A perspective may have many direct contributors, models, evidence sources, internal disagreements, and counter-perspectives.

No one participant should become equivalent to the perspective itself.

## No simple one-entity-one-vote rule is assumed

The working theory also does not presume:

```text
one human = one vote
one machine = one vote
one organization = one vote
```

Identity is too easy to duplicate, purchase, automate, or aggregate for raw entity count to serve as a sufficient theory of legitimacy.

The College of Perspectives is therefore a theory of **perspective standing and consequence**, not yet a voting system.

## Governance validity

A future formal decision procedure should preserve at least these tests:

1. **Scope:** is the decision actually within MASI's internal authority?
2. **Perspective coverage:** have materially affected perspectives been sought and modeled?
3. **Model corrigibility:** can those perspectives challenge the representation attributed to them?
4. **Consequence visibility:** are likely gains, losses, uncertainties, and externalities explicit?
5. **Non-dispossession:** does strengthening one perspective require weakening another perspective's legitimate power?
6. **Authority provenance:** what explicit grant authorizes the action, and is that grant still valid?
7. **Non-escalation:** has information, capability, delegation, funding, or temporary access been converted into authority it did not originally possess?
8. **Capture resistance:** can the decision mechanism be manipulated through identity multiplication, representation control, funding, incumbency, model ownership, evaluator control, or work-pool allocation?
9. **Evidence integrity:** can disagreement, abstention, negative evidence, and uncertainty survive the process?
10. **Action boundary:** can the proposed change occur only after the relevant governance checks, or can a participant bypass them?
11. **Future work:** what unresolved work becomes visible because of the decision?
12. **Auditability:** can the reasoning, evidence, updates, authority grants, and action path be reconstructed?
13. **Revisability:** can later evidence change the result without erasing history?

A formal constitution may add stronger or different tests.

## Positive-sum search

When two perspectives appear to require one another to become smaller, MASI should not immediately decide which perspective loses.

That apparent conflict should generate a question:

> **What are we missing that would allow both perspectives to become more capable, more secure, or more free without dispossession?**

The answer may be:

- a new technology;
- a different resource allocation;
- a better causal model;
- a missing perspective;
- a revised assumption;
- additional evidence;
- a genuinely physical scarcity;
- or no known solution yet.

The system should distinguish real constraints from inherited assumptions of scarcity.

## Relationship to scientific governance

Not every decision should use the same form of authority.

For example:

```text
"Did this experiment reproduce?"
→ primarily evidentiary / scientific procedure

"Does this component satisfy an interface?"
→ technical / architectural procedure

"Should this perspective model be corrected?"
→ perspective + evidence + provenance procedure

"May MASI take this class of action?"
→ constitutional governance procedure

"What unfinished work did this disagreement expose?"
→ work-pool / prioritization procedure
```

Bounded responsibility should apply to governance authority as well as computational modules.

No participant should gain generic authority because it has legitimate authority in one domain.

## Relationship to participation

Public participation and governance are separate questions.

A person may make a valuable contribution without acquiring governance authority.

A person may be materially affected by MASI without contributing code and still represent a perspective the system must understand.

Funding, code contribution, technical expertise, model ownership, or repository maintenance should not silently become universal governance standing.

Public repository participation rules should remain distinct from this deeper constitutional theory of how MASI itself may eventually be governed.

## Current research obligations

Before converting this working theory into a constitution, the project should deliberately seek additional perspectives and test the theory against them.

Priority work includes:

- find people who strongly disagree with the current framing;
- seek cultural, geographic, economic, technical, religious, philosophical, ecological, and institutional perspectives not already represented;
- seek perspectives from people unlikely to discover or contribute to an AI research repository on their own;
- model internal disagreements rather than only category labels;
- ask actual perspective-holders to correct how the system describes them;
- test whether the non-dispossession invariant survives hard edge cases;
- test whether "true power" can be operationalized without hiding coercion behind terminology;
- identify real cases of irreducible scarcity;
- study governance-capture mechanisms;
- develop adversarial tests for the initial governance threat map;
- test authority-confusion, delegation-escalation, work-pool-capture, action-boundary, evaluator-capture, amendment-capture, and provenance-poisoning cases;
- design update/provenance rules for perspective models;
- determine how future and non-self-articulating perspectives can be modeled without pretending consent;
- determine how machine perspectives can participate without allowing cheap replication to manufacture standing;
- test whether work-pool allocation can itself be captured;
- test whether stewardship activity can become an undeclared path to constitutional authority;
- test how the system behaves when a founder, maintainer, or highly active steward is absent without creating a successor office;
- identify conditions under which unresolved disagreement should block an action versus simply create future work.

## Stewardship is a behavior, not an office

The current task is not to declare the College of Perspectives complete.

It is to make the model more realistic.

That means actively finding more perspectives, inviting correction, preserving counter-perspectives, surfacing capture risks, and allowing the theory to change when those perspectives expose defects.

> **Stewardship is the voluntary work of increasing the system's capacity to perceive, correct, and include perspectives beyond one's own.**

Stewardship is **not** a constitutional office.

There is no presumed role of:

```text
sole steward
founder-steward
chief steward
successor steward
final interpreter
guardian above the governance
```

Creating such a role would place a government above the governance.

A participant stewards MASI when they help the system:

- discover a materially missing perspective;
- bring in people or systems capable of correcting the current model;
- preserve disagreement rather than erase it;
- improve perspective fidelity;
- expose a capture path;
- protect evidence and provenance;
- identify unfinished work;
- make the system more corrigible;
- reduce dependence on any one participant's worldview.

This behavior is open to any participant.

> **Stewardship confers no additional constitutional authority.**

Doing more stewardship work does not create:

- extra standing;
- a stronger vote;
- amendment authority;
- ownership of a perspective;
- permanent interpretive privilege;
- a right to appoint a successor;
- sovereignty over the College of Perspectives.

A participant may be highly valuable to the system without becoming constitutionally superior to it.

### No founder exception

The originator of MASI is subject to the same rule.

Founding the architecture, maintaining the repository, contributing substantial work, or recruiting perspectives does not create a permanent governance office.

The founder may steward the system by bringing in perspectives beyond his own, but that activity does not make the founder the authority over those perspectives or the final authority over governance.

The governance model should therefore not depend on either of these assumptions:

```text
the founder remains the sole steward
or
the founder chooses the person who replaces him
```

Both would recreate a higher-order government outside the College of Perspectives.

### Continuity without succession

The relevant continuity question is not:

> Who replaces the founder?

It is:

> **Can stewardship remain distributed enough that the system continues discovering missing perspectives, correcting itself, preserving integrity, and surfacing work even when any particular participant is absent?**

Continuity should emerge from many participants being able to perform stewardship behaviors rather than from inheritance of a privileged role.

A healthy system should become progressively less dependent on any one participant while allowing every participant, including the founder, to continue contributing fully.

### Stewardship capture

Because stewardship itself can become socially influential, the system should treat attempts to convert stewardship into authority as a capture vector.

Examples include:

- "I brought this perspective in, therefore I speak for it."
- "I maintain the repository, therefore I decide the constitution."
- "I found the defect, therefore I control the repair."
- "I recruited the community, therefore I own its standing."
- "I have stewarded the project longest, therefore I appoint my successor."
- "The system depends on me, therefore my preferences outrank the governance process."

These claims may describe contribution, leverage, or dependence.

They do not, by themselves, establish legitimate authority.

The preferred remedy is not to make a valuable steward smaller. It is to make the system stronger around them by increasing independent stewardship capacity and reducing single-participant dependency.

> **A governance system that cannot be corrected by perspectives it failed to imagine is not yet plural governance.**

> **A governance system that requires a privileged steward above itself is not yet self-governing.**

## Working constitutional core

The current theory can be summarized as:

> **MASI governs MASI, not society.**

> **Governance is consequence.**

> **Power is the freedom and capability to be and become oneself without the equal freedom of another perspective becoming a threat to one's safety or existence.**

> **No governance action is valid if increasing the legitimate power of one perspective requires decreasing the legitimate power of even one other perspective.**

> **The College of Perspectives models perspectives rather than appointing people or machines to become those perspectives.**

> **Information may inform governance without thereby authorizing action.**

> **No participant may delegate, manufacture, or infer authority beyond the authority explicitly granted to it.**

> **Perspective models remain corrigible by actual perspectives, evidence, internal disagreement, and counter-perspectives.**

> **Duplicating identities does not multiply legitimacy.**

> **Unresolved disagreement is not a stall; it is identified future work.**

> **The system should seek positive-sum increases in capability and convert material unknowns into explicit work.**

> **The set of perspectives is never presumed complete.**

> **Stewardship is a behavior open to any participant; it is not an office and grants no sovereignty over the system.**

> **There is no founder or successor exception to the governance.**

These are working principles to test, not a claim that the final governance architecture has been solved.
