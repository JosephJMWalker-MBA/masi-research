# MASI Contribution DAO — Working Institutional Model

**Status:** working institutional and constitutional hypothesis; not a finalized legal entity, ownership agreement, token design, or deployed governance mechanism  
**Scope:** participation by specialized intelligences and their human/institutional contributors in a shared MASI system  
**Purpose:** make explicit how contribution, membership, specialization, cooperation, evaluation, learning, and authority relate without importing assumptions from reward-seeking multi-agent systems

## Starting assumption: excellence seeking, not power seeking

MASI does not begin from the assumption that specialized intelligences are political actors trying to accumulate power, maximize a shared reward, clear a queue, or force agreement.

The working assumption is simpler:

> **Builders will try to build the best intelligence they can for a bounded responsibility. MASI should make that excellence composable so that improving an individual specialist can also improve the governed system.**

A university, laboratory, company, independent researcher, or other contributor may train or construct a specialist using whatever lawful method best fits the responsibility: supervised learning, reinforcement learning, distillation where permitted, symbolic methods, causal models, simulation, deterministic verification, hybrid systems, or methods not yet represented here.

MASI does not prescribe one training philosophy for every contributor. It evaluates the resulting capability at the system boundary.

## The first members are responsibilities, not sovereign departments

The historical MASI responsibilities — Precision, Foresight, Empathy, and Wisdom — should be understood as the first differentiated seats in the intelligence ecology, not as subordinate departments owned by a central model.

Their purpose is not to converge into one generalized policy.

Their purpose is to remain excellent at distinct responsibilities while participating in a governed composition.

A role may eventually contain multiple independent implementations contributed by different institutions.

```text
MASI contribution ecology

Precision
├── University A implementation
├── University B implementation
└── independent implementation

Foresight
├── Lab C implementation
└── MASI reference implementation

Empathy
└── ...

Wisdom
└── ...
```

The role is durable. The implementation is replaceable.

## Membership by demonstrated contribution

The DAO hypothesis is **joint institutional ownership/standing by contribution**.

Membership should not depend on pleasing an incumbent maintainer, belonging to a preferred institution, using a preferred model family, or winning a political negotiation. A candidate should be able to demonstrate that it satisfies a published responsibility contract and contributes measurable value to the system.

That value should not collapse into one leaderboard score. Candidate evidence may include:

- bounded role performance;
- reliability and calibration over time;
- conformance to the role contract;
- marginal improvement to composed-system performance;
- unique coverage or non-redundant capability;
- detection of failure modes other members miss;
- useful disagreement that survives later verification;
- robustness under held-out and adversarial evaluation;
- provenance, licensing, and reproducibility sufficient for lawful participation;
- resource cost and operational reliability where relevant.

A high standalone score may be less valuable than a lower-scoring implementation that catches an important class of shared failures.

> **Membership should track demonstrated contribution to the intelligence ecology, not identity or institutional prestige.**

The exact mapping from evidence to membership remains a constitutional design problem and must be versioned, inspectable, and challengeable.

### Institutional ownership is not automatic copyright transfer

"Joint ownership by contribution" describes the proposed institutional standing of DAO members. It does not by itself mean that every member automatically acquires copyright, patent, data, model-weight, or other intellectual-property ownership in every other member's contribution.

Legal ownership, licensing, economic rights, governance rights, and technical participation are distinct and require explicit terms.

## Membership is not universal authority

Contribution may establish membership or role-level standing without granting every kind of authority.

```text
demonstrated contribution -> membership / attributable standing

membership != unrestricted tool authority
membership != authority over another role
membership != unilateral constitutional amendment
membership != ownership of another contributor's model
membership != permission to suppress contrary evidence
```

Authority remains typed, scoped, and provenance-bearing.

A strong Precision implementation may earn greater role-level influence under a frozen evaluation policy while still having no authority to rewrite Empathy, deploy an external action, change the constitution, or define its own audit standard.

This preserves the least-authority principle while allowing performance to matter.

## MASI does not optimize members toward agreement

A central correction to common multi-agent interpretations is:

> **MASI permits conclusions to converge without requiring intelligences to converge.**

The specialized intelligences have roles, not interests.

There is no architectural requirement that Empathy become more like Precision, that Wisdom anticipate what Foresight "wants," or that every member optimize toward a common scalar trust score.

Cross-role disagreement can be information.

A system that erases persistent differences among roles may be losing the very specialization it was built to preserve.

## Intra-role cooperation can use swarm methods

Multiple implementations of the same responsibility may cooperate, critique, verify, or reconcile one another using ensemble or swarm-like methods.

For example, multiple Precision implementations may independently solve the same bounded problem and later compare:

```text
shared task
   ├── Precision A -> result + evidence
   ├── Precision B -> result + evidence
   └── Precision C -> result + evidence
                 ↓
        comparison / verification
                 ↓
          role-level result
```

Warranted agreement can increase confidence when independent paths support the same conclusion.

However, agreement itself is not the objective.

The system should prefer a correct, well-supported dissenting result over a larger number of mutually reinforcing errors.

Where practical, first-pass judgments should be produced independently before cross-exposure so that later convergence is distinguishable from simple anchoring or sequential contamination.

### Two different meanings of convergence

MASI should distinguish:

1. **Intra-role evidential convergence** — independently developed implementations of the same responsibility resolve toward a common conclusion because evidence supports it.
2. **Cross-role homogenization** — distinct responsibilities increasingly behave as though they share one objective or one policy.

The first may be useful evidence. The second may indicate loss of specialization.

The conclusion may converge while the intelligences remain distinct and independently attributable.

## Measurement is not reinforcement

MASI should not equate evaluation with reinforcement learning.

The system may measure:

- performance;
- calibration;
- failures;
- disagreements;
- marginal contribution;
- downstream outcomes;
- resource use;
- reliability.

Those observations do not require the evaluated model to receive a reward signal, update its weights, or optimize toward the evaluation metric.

> **MASI can learn about a specialist without causing the specialist to learn from MASI.**

System-level routing or influence may change because evidence changes. That is distinct from retraining the underlying specialist.

A contributor may later choose to use MASI evidence to improve a new model version. Another contributor may interpret the same evidence differently. This methodological pluralism is desirable because a single shared reward function could itself create convergence pressure across otherwise independent implementations.

Reinforcement learning may be used inside a contributor's implementation. It is not a constitutional requirement of MASI.

## MASI as an evidence and training-data institution

A governed composition naturally produces valuable longitudinal evidence:

```text
input
  -> specialist outputs
  -> evidence and assumptions
  -> disagreement
  -> verification / resolution / abstention
  -> authorized action or non-action
  -> observed outcome where available
```

Preserved with provenance, this record can support future research, evaluation, calibration, distillation where lawful, supervised training, adversarial testing, or other model-development methods.

The system should preserve inspectable artifacts such as outputs, proofs, citations, constraint states, forecasts, declared uncertainty, disagreements, decisions, and outcomes where available. It does **not** require disclosure of hidden chain-of-thought from models that do not expose it.

The institutional loop is therefore:

```text
contributors build models
        ↓
models contribute to MASI
        ↓
MASI records evidence and outcomes
        ↓
shared research corpus improves
        ↓
contributors independently study the evidence
        ↓
new or revised models compete to contribute
```

This is an evidence loop, not necessarily a reinforcement loop.

## Benchmark governance is part of the constitution

Transparent mathematical criteria reduce discretionary gatekeeping, but no fixed benchmark should be assumed ungameable.

Benchmark gaming, overfitting, evaluator capture, and metric substitution are part of the threat model.

Membership and role-standing evaluation should therefore use controls such as:

- preregistered criteria where practical;
- held-out and rotating evaluation sets;
- adversarial evaluation;
- longitudinal reliability;
- negative-result retention;
- marginal-system contribution rather than standalone score alone;
- explicit versioning of metrics and thresholds;
- independent replication;
- separation between evaluator design and unilateral admission authority where practical.

The mathematics that maps evidence to standing is itself governed.

No founder, maintainer, contributor, model, laboratory, or incumbent coalition should be able to silently redefine the success function and then claim that the resulting outcome is objectively mandated by mathematics.

Metric definitions, weights, admission thresholds, and amendment procedures require provenance and constitutional change control.

## Capabilities must be enforced outside model prose

Specialization by construction should extend to action capability.

A role should not lack authority merely because a system prompt tells it not to act.

Where a capability matters, the environment should enforce the boundary:

```text
specialist output
      ↓
governance / authorization boundary
      ↓
capability check
      ↓
tool or external state
```

A compromised or mistaken specialist should be unable to manufacture execution authority through language alone.

Identity, recommendation, confidence, benchmark rank, or membership does not create a credential.

## Centralization test

A contribution DAO is still centralized in practice if one actor can unilaterally control:

- which benchmarks count;
- benchmark weights;
- membership thresholds;
- constitutional amendments;
- evaluation evidence;
- model admission or removal;
- execution credentials;
- audit visibility.

The intended architecture therefore separates at least:

```text
CONTRIBUTION
what capability is supplied

EVALUATION
what the evidence shows

MEMBERSHIP
what demonstrated contribution qualifies for participation/standing

AUTHORITY
what actions or governance operations are permitted

CONSTITUTION
how these mappings may change
```

These layers may interact but should not silently collapse into one power center.

## Research questions

This working model creates testable questions rather than settled claims:

1. Can role-level swarms improve performance without erasing useful implementation diversity?
2. Which measures best capture marginal contribution rather than benchmark imitation?
3. Can independent-first evaluation measurably reduce anchoring and correlated error?
4. How should useful dissent be valued when it catches errors shared by higher-scoring members?
5. Which system-level influence updates improve outcomes without becoming hidden reinforcement of a common objective?
6. How can benchmark and membership criteria evolve without enabling evaluator capture?
7. What governance and legal structure can represent joint ownership/standing by contribution without confusing participation with automatic IP transfer or universal authority?
8. Does an evidence-producing MASI ecology create higher-quality training and evaluation material than isolated model development under comparable provenance constraints?

## Working invariant

> **Build the best specialist you can. Preserve what it uniquely contributes. Measure that contribution faithfully. Let conclusions converge when evidence warrants it, but do not train away the distinctions that make the ecology useful.**
