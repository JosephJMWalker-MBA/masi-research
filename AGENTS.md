# Agent Operating Rules

This repository is a falsifiable research program. AI agents working here should optimize for accurate experimental progress, not architectural expansion.

## Read first

Before making consequential changes, read:

1. `README.md`
2. `STATUS.md`
3. `docs/RESEARCH_THESIS.md`
4. `docs/MODULES.md`
5. `docs/EVALUATION.md`
6. `docs/CANDIDATE_IMPLEMENTATIONS.md`
7. the active experiment / sprint protocol

## Operating principles

- **Prior art before custom implementation.** Search libraries, products, research, Agent Skills/workflows, and relevant tool capabilities before building substantial new machinery.
- **Role contract != model identity.** Never treat a current implementation as canonical merely because it fills a MASI responsibility.
- **Prompting != specialization.** Prompt-only role decomposition is a valid control condition, not sufficient evidence of a specialized learned module.
- **Freeze before observation.** Evaluation criteria, baselines, data splits, and major success/failure conditions should be fixed before inspecting final results.
- **Evidence != interpretation.** Preserve raw outputs and measurements separately from conclusions.
- **Negative results are first-class.** Do not optimize documentation to make MASI appear successful.
- **Smallest sufficient experiment.** Avoid building a generic runtime when a script or adapter is enough to answer the current question.
- **No silent benchmark advantage.** Compare systems under clearly stated compute, context, tool, pass-count, and resource conditions.
- **Respect provider terms.** Do not publish restricted third-party benchmark/performance information.
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
2. correctness and regression risk;
3. unnecessary architecture or scope expansion;
4. baseline fairness, leakage, contamination, and resource accounting;
5. license/provider-term compliance;
6. evidence/interpretation separation;
7. preservation of negative or inconclusive results;
8. accidental promotion of one implementation into authority;
9. reproducibility of the claimed observation.

An audit outcome should be one of:

```text
ACCEPT
REPAIR_REQUIRED
CLAIM_NARROWING_REQUIRED
INCONCLUSIVE
RESEARCH_QUESTION_DEFECT
```

The auditor should not rewrite sound implementation merely to impose preferred style.

## Architecture restraint

Do not add a new abstraction, schema, service, module, or repository because it may be useful later.

New structure should be earned by one of:

- repeated need across experiments;
- an explicit current protocol requirement;
- a reproducibility requirement;
- a safety/governance boundary;
- evidence that an existing abstraction is inadequate.

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
