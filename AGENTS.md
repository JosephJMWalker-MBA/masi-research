# Agent Operating Rules

This repository is a falsifiable research program. AI agents working here should optimize for accurate experimental progress, not architectural expansion.

## Mandatory construction doctrine

**Before any further implementation work, read [`docs/CONSTRUCTION_DOCTRINE.md`](docs/CONSTRUCTION_DOCTRINE.md).**

The following is a non-negotiable project invariant:

> **MASI does not begin with a general-purpose model and carve it into specialists. It begins with bounded cognitive responsibilities and engineers the smallest sufficient intelligence for each responsibility from first principles. Generality belongs to the governed composition, not to each component.**

Prompted or fine-tuned general models remain useful as controls, baselines, tools, translators, proposal generators, long-tail handlers, or transitional implementations. They are **not** presumed to be the MASI target specialist architecture.

Existing AI systems should be used to identify primitives worth inheriting, implementations worth adapting, benchmarks worth comparing against, and technical debt / failure modes worth engineering against. Do not silently turn the current LLM ecosystem into MASI's theory of cognition.

Equally, do **not** remove an LLM, Jev, or another existing component merely to make the system look more purpose-built. A general-purpose model may be the right component when breadth, language translation, hypothesis generation, or long-tail integration is the actual responsibility. Its output should then be treated as a broad prior/proposal unless a contract explicitly grants something stronger.

### WP1 reconciliation accepted — next work remains bounded

The first Astra block began before this doctrine was explicit enough. That checkpoint is now complete.

The documentation-only R1–R7 reconciliation was independently re-checked in [Audit Addendum B](docs/AUDIT_WP0_WP1_2026-09-17.md) and received `ACCEPT`. **WP1 is accepted only as narrowed.**

The doctrine-reconciliation hold is therefore cleared for the next **operator-authorized** work packet. This is not blanket authorization for WP2, E001, training, new candidates, runtime expansion, or merging the frozen builder packet.

The current authorized next packet is the WP0 research-gate work recorded in `STATUS.md` and `docs/IMPLEMENTATION_SPRINT_001.md`: tighten/freeze enough of Issues #1 and #2 to make later implementation claims falsifiable without hardening accidental architecture.

## Epistemic integrity gate

**Before optimizing for task completion or benchmark performance, read [`docs/EPISTEMIC_INTEGRITY.md`](docs/EPISTEMIC_INTEGRITY.md).**

> **Epistemic integrity outranks task completion. Truthful failure beats false success.**

An evaluator, score, workflow, orchestrator, or benchmark is not authority to manufacture, conceal, corrupt, or misrepresent evidence. If legitimate completion is unavailable, preserve the evidence and return a truthful failure, abstention, blocked state, specification defect, evaluator defect, or authority conflict rather than gaming the proxy.

This is not a permission to abandon difficult work. Search legitimate solution paths aggressively; do not purchase apparent success by making the evidence less true.

## Read first

Before making consequential changes, read in this order:

1. `docs/CONSTRUCTION_DOCTRINE.md`
2. `docs/PRIOR_ART.md`
3. `README.md`
4. `STATUS.md`
5. `docs/RESEARCH_THESIS.md`
6. `docs/MODULES.md`
7. `docs/EVALUATION.md`
8. `docs/CANDIDATE_IMPLEMENTATIONS.md`
9. the active experiment / sprint protocol

## Specialist implementation gate

Before implementing or hardening a specialist, write down:

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

If those fields cannot yet be stated, stop at research/prototyping rather than hardening an accidental architecture.

For `MASI_TARGET`, start with the **minimum sufficient intelligence** for the responsibility. A target may be neural, symbolic, probabilistic, causal, deterministic, simulation-based, hybrid, or something else entirely. There is no requirement that a specialist be an LLM.

For a retained general-purpose or external decision component, also state:

```text
component role:
why breadth/generalization is useful here:
what authority it does NOT have:
what bounded specialist may correct/override it:
what provenance is preserved:
```

## Operating principles

- **Prior art before custom implementation.** Search libraries, products, research, Agent Skills/workflows, and relevant tool capabilities before building substantial new machinery. Treat blackboard systems, Brooks/subsumption, cognitive architectures, modular deep learning, MRKL, FlexOlmo, concept bottlenecks, and current modular-composition work as required neighboring lineages where relevant.
- **Specialization by construction, not subtraction.** Purpose-built bounded intelligence is the target for specialist roles; narrowed general models are controls/transitional implementations unless evidence justifies otherwise.
- **Generalists remain legitimate components.** Use an LLM or decision-native system when its broad capability is the actual needed function; do not confuse plausible/general output with truth, authority, forecast, or permission.
- **Role contract != model identity.** Never treat a current implementation as canonical merely because it fills a MASI responsibility.
- **Prompting != specialization.** Prompt-only role decomposition is a valid control condition, not sufficient evidence of a specialized learned module.
- **No complexity without a demonstrated deficit.** Add architectural complexity only when measured failure shows why the simpler system is insufficient.
- **Generality belongs to composition.** Do not replicate broad general intelligence inside each module merely because pretrained LLMs make that convenient.
- **Typed semantic boundaries.** Every semantically meaningful state crossing a MASI boundary should be named, typed, inspectable, testable, and where practical causally intervenable.
- **Freeze before observation.** Evaluation criteria, baselines, data splits, and major success/failure conditions should be fixed before inspecting final results.
- **Evidence != interpretation.** Preserve raw outputs and measurements separately from conclusions.
- **Negative results are first-class.** Do not optimize documentation to make MASI appear successful.
- **Smallest sufficient experiment.** Avoid building a generic runtime when a script or adapter is enough to answer the current question.
- **No silent benchmark advantage.** Compare systems under clearly stated compute, context, tool, pass-count, and resource conditions.
- **Respect provider terms.** Do not publish restricted third-party benchmark/performance information or perform prohibited reverse engineering, distillation, imitation training, or source extraction.
- **Preserve uncertainty.** Inconclusive is a legitimate result.

## Context discipline

For long AI-assisted sessions use:

```text
Explore -> Decide -> Distill -> Clear/Compact -> Execute -> Verify
```

When the objective materially changes or context grows large, preserve durable state in the repository rather than depending on a chat transcript.

At minimum preserve:

- current question;
- frozen decisions;
- unresolved questions;
- known failures;
- acceptance criteria;
- exact next action.

## Primary-agent / independent-auditor cadence

Long implementation runs should use an explicit review boundary when practical. The current operator workflow uses Astra on Ultra as the primary implementation agent and Claude as an independent auditor at approximately five-hour or work-packet boundaries. Those products are **not** architectural dependencies; the reusable rule is separation between builder and reviewer.

Before handing off, the primary agent should preserve:

- exact branch and commit;
- active issue / work packet;
- implementation decisions made;
- files changed;
- commands and tests executed with results;
- evidence artifacts produced;
- known failures and unresolved questions;
- claims the evidence does not support;
- exact next action.

The independent auditor should review the durable repository state rather than relying on the builder's narrative alone. Audit priorities are:

1. fidelity to the frozen research question and acceptance criteria;
2. fidelity to `docs/CONSTRUCTION_DOCTRINE.md`;
3. correctness and regression risk;
4. unnecessary architecture or scope expansion;
5. baseline fairness, leakage, contamination, and resource accounting;
6. license/provider-term compliance;
7. evidence/interpretation separation;
8. preservation of negative or inconclusive results;
9. accidental promotion of one implementation into authority;
10. accidental promotion of a general-model adaptation into the target architecture;
11. accidental removal of useful general-purpose capability for architectural purity rather than measured reason;
12. reproducibility of the claimed observation.

An audit outcome should be one of:

```text
ACCEPT
REPAIR_REQUIRED
CLAIM_NARROWING_REQUIRED
INCONCLUSIVE
RESEARCH_QUESTION_DEFECT
```

The auditor should not rewrite sound implementation merely to impose a preferred style.

## Architecture restraint

Do not add a new abstraction, schema, service, module, or repository because it may be useful later.

New structure should be earned by one of:

- repeated need across experiments;
- an explicit current protocol requirement;
- a reproducibility requirement;
- a safety/governance boundary;
- evidence that an existing abstraction is inadequate.

Before accepting a major design, apply both permanent construction tests:

> **If today's dominant LLM architecture did not exist, would we still design this specialist this way from the responsibility outward?**

> **If we removed the general-purpose model entirely, what useful breadth, translation, hypothesis-generation, or long-tail capability would we now have to rebuild badly by hand?**

A good design should survive both tests.

## Claim discipline

Use language proportional to evidence:

- `proposed` for an idea;
- `implemented` for code that exists;
- `observed` for a measured run;
- `reproduced` for a repeated result under comparable conditions;
- `supported` for a claim with appropriate evidence;
- `unknown` or `inconclusive` where evidence is insufficient.

Do not call a model calibrated unless calibration has been measured on the relevant task distribution.

## Public-repository boundary

Never commit:

- API keys, passwords, tokens, or credentials;
- private conversations;
- sensitive personal data;
- non-public proprietary datasets without authorization;
- model weights whose license does not permit redistribution;
- third-party benchmark results whose terms prohibit publication.

Prefer hashes, manifests, retrieval instructions, and reproducible references for large or externally licensed artifacts.
