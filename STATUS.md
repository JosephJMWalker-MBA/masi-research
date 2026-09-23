# Status

**Current phase:** deliberate plateau after acceptance and merge of MASI-E001 protocol v1.4.

MASI-E001 is now a durable, independently accepted preregistered experiment. It is **not authorized for execution** and is intentionally allowed to remain dormant while cheaper experiments reduce uncertainty first.

The repository currently has no open pull requests.

## Current authority and operating reality

For now, the repository has one human maintainer/operator: **Joseph J. M. Walker**.

AI systems may assist with research, implementation, verification, documentation, long-running experiments, and independent review when explicitly assigned those roles. They do not self-grant repository, scientific, or execution authority. Durable state belongs in GitHub rather than in any model session.

Working reality:

```text
human maintainer/operator
        +
AI research/engineering/audit assistance
        ↓
explicit bounded work
        ↓
GitHub durable record
```

No artificial organizational structure should be invented merely to imitate a larger team before one exists.

## E001 — accepted and intentionally dormant

**Experiment:** MASI-E001 — Empathy speaker-observation specialist.

**Accepted protocol:** `e001-protocol-v1.4`

**Accepted audited commit:** `9edd737764815a49929bfe60f104ff7b5a0e40e9`

**Protocol PR:** #17 — merged.

The independent audit history ended in `ACCEPT` at v1.4. Acceptance means the experimental design/preregistration is sound enough to execute as written. It does **not** mean the scientific hypothesis is supported.

The accepted protocol should not be edited merely to update status language. If E001 is executed later, it should use the accepted v1.4 freeze unless a genuinely new protocol version is deliberately created and audited.

### Why E001 is not being rushed

E001 is now closer to a serious validation experiment than a cheap first proof of concept.

Its main cost is human coordination, not compute.

Approximate frozen human-work budget:

- ~60 h writing/review;
- ~130 h annotation/adjudication;
- ~40 h QC-pool work;
- ~230 h baseline human work before reserve effects;
- roughly ~20% additional burden if reserve activation is needed.

It also requires independent role boundaries that cannot truthfully be collapsed into one maintainer plus AI:

- B1 — independent custodian;
- B2 — writers, annotators, adjudicator, QC team, budget and contributor protections;
- B3 — generator pin / terms reverification;
- B4 — F1 and S-H2A activation decisions;
- B5 — independent P3/P4 auditor;
- separate explicit operator execution authorization after those bindings.

The compute portion is comparatively modest and was frozen around the Mac mini M4 environment. Do not silently migrate E001 to the Jetson Orin without a new protocol decision.

## Long-horizon Empathy research program

The broader Empathy direction has now been recorded in [`docs/EMPATHY_RESEARCH_PROGRAM.md`](docs/EMPATHY_RESEARCH_PROGRAM.md).

The approved successor research sequence is:

```text
E001 evidence-grounded observation
  -> E002 stakeholder and perspective representation (#20)
  -> E003 perspective counterfactuals (#21)
  -> E004 missing-perspective detection (#22)
  -> E005 Empathy-governed composition (#23)
```

This sequence formalizes Empathy as bounded **other-regarding intelligence**: explicit representation of affected stakeholders, evidence and uncertainty, agency/consent, burdens and benefits, relational consequences, and eventually missing-perspective detection.

It does **not** change the current execution priority. E002-E005 are research questions only. They are not authorized for implementation, and they do not expand or amend accepted E001 v1.4.

A core invariant for later Empathy work is:

```text
inference about another being != fact about that being
```

The program also preserves a second architectural boundary: improved social modeling can support cooperation but can also improve manipulation, so Empathy capability must remain bounded by explicit governance and authority.

## Strategic decision at this plateau

**Run a smaller, human-light experiment before deciding whether to spend the human resources required by E001.**

This is a prioritization decision, not a rejection of E001.

The smaller experiment should exploit the project's currently abundant resource:

> a small amount of human design attention followed by long unattended local compute.

The Jetson Orin is a good candidate execution substrate for that experiment because unattended multi-day runs are acceptable and desirable.

### What the smaller experiment should answer

The next experiment should reduce one upstream uncertainty:

> **Does specialization-by-construction show a measurable operating region at all before we pay the human cost required to test it on a difficult human-semantic boundary?**

The preferred shape is:

- mechanically known ground truth rather than human adjudication;
- bounded semantic responsibility;
- synthetic but controlled scenario generation;
- transparent deterministic specialist first;
- learned complexity only if a measured deficit justifies it;
- a small general-purpose control;
- large unattended perturbation/stress sweeps on the Orin.

Candidate controlled factors may include:

- speaker vs. other-person attribution;
- current vs. past state;
- actual vs. hypothetical;
- affirmation vs. negation;
- support vs. counter-evidence;
- retraction / supersession;
- signal vs. distractor;
- paraphrase and lexical shift;
- longer context and noise;
- adversarial wording;
- class imbalance.

A minimal comparison could eventually include:

```text
R0   trivial / naive reference
T0   transparent deterministic specialist
T1   small learned specialist, only if justified
C_A  small prompted general-purpose control
```

The exact task, metrics, model set, and architecture are **not yet frozen**.

## Firewall around E001

The smaller experiment may influence **whether or when E001 is worth executing**.

It may **not** retroactively modify E001 v1.4 after seeing results.

If the smaller experiment reveals a better design, that belongs in:

- a later experiment;
- an E001 successor;
- or a deliberately new E001 protocol version with fresh audit.

Do not mutate the accepted v1.4 freeze to accommodate pilot findings.

## What not to do next

Do not:

- recruit an E001 human team merely because the protocol is now accepted;
- spend money on B2 before deciding E001 is the next best use of resources;
- start E001 annotation, training, inference, unlock, or result observation;
- invent a new MASI organization or governance hierarchy just to fill empty roles;
- let the smaller experiment grow into another sprawling architecture project;
- create a new repository before the smaller experiment has a crisp research question;
- treat long-running compute as a reason to add unnecessary complexity.

## Resume point

When MASI work resumes, start here.

The next task is **not implementation**.

Write a short design note for the smaller pre-E001 experiment that answers only:

1. What single MASI uncertainty will this experiment reduce?
2. Why is the Jetson Orin the right substrate?
3. How is ground truth generated mechanically and independently of the tested systems?
4. What is the minimum comparison set?
5. What observations would justify:
   - proceeding toward E001,
   - running another smaller experiment,
   - or revising the construction doctrine?

Then stop and review that design before creating code, a branch, a new repo, training anything, or committing to a long run.

## Durable historical state

- WP1 remains accepted only as narrowed.
- WP0 research gates remain accepted for bounded experiment design.
- The frozen WP1 builder artifact remains `codex/wp0-wp1-candidate-probe @ 81adfffa2d28e4a40a0b36fe1a21baa567d402ec`.
- E001 protocol v1.4 is accepted and merged.
- The public participation compact is merged.
- The MASI governance working theory is merged.
- The DeepSeek V4.1 MASI research note is merged.
- No open PR backlog remains at this handoff.

**Current posture:** no rush. Preserve E001, design the cheaper experiment deliberately, and use unattended compute where it buys real information.
