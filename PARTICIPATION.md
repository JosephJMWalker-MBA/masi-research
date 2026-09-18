# Participation Compact

MASI Research is public because serious collaborative research requires more than visible code. It requires participants to understand the conditions under which their time, ideas, code, evidence, criticism, reputation, and other contributions will be received.

> **Open participation does not mean undefined participation.**

This document explains what participation in this repository means. It complements `CONTRIBUTING.md`, which explains how to make scientifically useful contributions.

## What this repository is

MASI Research is an **open experimental research program** for testing, narrowing, falsifying, reproducing, and improving claims about modular specialized intelligence.

Participation may include:

- proposing or sharpening a research question;
- contributing prior art;
- reproducing or failing to reproduce a result;
- contributing code, tests, datasets, fixtures, models, adapters, or evaluation methods;
- implementing a bounded specialist or control condition;
- identifying a confound, defect, unsupported claim, or unnecessary abstraction;
- contributing domain knowledge where the provenance and permission boundary are clear;
- performing independent audit or adversarial review;
- improving documentation, experimental procedure, or governance mechanisms.

A useful contribution does not have to support MASI. Evidence that a simpler approach works better, that a proposed responsibility is unnecessary, or that a claim should be abandoned is a successful research contribution.

## What participation does not mean

Participation in this repository does **not**, by itself, create:

- employment;
- a consulting relationship;
- partnership or joint venture;
- equity or an ownership interest in a company;
- a governance seat;
- a promise of compensation;
- a funding commitment;
- an exclusive right to implement MASI or any named responsibility;
- endorsement by the repository maintainers;
- scientific acceptance merely because a contribution is merged;
- a promise that accepted work will remain canonical or permanent.

If a separate employment, sponsorship, investment, commercialization, or institutional relationship is contemplated, it should be documented separately rather than inferred from GitHub participation.

## Participation is contribution to a research record

The repository should preserve the difference between:

```text
proposal
!= accepted research obligation
!= implementation
!= observed result
!= reproduced result
!= supported claim
!= canonical architecture
```

A merged artifact may later be:

- superseded by stronger evidence;
- narrowed after audit;
- replaced by a simpler implementation;
- retained as a control or historical record;
- shown to be unnecessary;
- preserved as a negative or inconclusive result.

Merge status is a repository action, not a declaration of truth.

## Expected contribution path

Where practical, substantial work should follow a visible path:

```text
question / proposal
        ↓
scope + prior-art check
        ↓
accepted research obligation or bounded experiment
        ↓
implementation / evidence
        ↓
independent review where warranted
        ↓
ACCEPT | REPAIR | NARROW | INCONCLUSIVE | REJECT
        ↓
durable research record
```

Not every contribution needs every step. A typo fix does not need an experiment. A new architectural claim usually does.

The important rule is that the path should be legible enough that a contributor can understand what is being evaluated and what acceptance would mean **before** investing substantial effort.

## Current repository authority

Repository permissions determine who can merge, close, label, or otherwise change the canonical GitHub repository state.

That operational authority is not the same thing as scientific authority.

A maintainer can merge a result without making it true. A contributor can produce evidence strong enough to overturn an earlier maintainer decision. A model, reviewer, maintainer, sponsor, or prominent contributor does not become epistemically authoritative by status alone.

The long-term governance model for MASI Research is a separate design question. **This participation compact does not settle who should ultimately govern the project or how that authority should be distributed.** Any formal governance structure adopted later should be documented explicitly and should distinguish repository administration, scientific evaluation, architectural stewardship, and any commercial authority.

## No hidden participation rules

Participants should be able to rely on the public repository as the governing record for contribution expectations.

Material participation rules should therefore be:

- written down;
- version-controlled;
- changed visibly;
- applied prospectively where practical;
- consistent with the repository license and existing accepted obligations;
- distinguishable from informal preferences or private conversations.

No contributor should be expected to infer an unpublished obligation merely because a maintainer, model, reviewer, sponsor, or long-time participant assumes it.

When rules change, the change should preserve enough history to understand what governed earlier work.

## License, reuse, and contribution rights

Unless otherwise noted, original repository content is distributed under the Apache License 2.0 in `LICENSE`.

Contributors are responsible for submitting only material they have the right to contribute and for identifying third-party restrictions, licenses, confidential information, data-use limits, or publication constraints that affect the contribution.

Accepted contribution does not make third-party material Apache-2.0 merely because it appears in or is referenced by this repository.

The practical expectation is that original material intentionally contributed for inclusion may be reused, modified, and redistributed under the repository's applicable license terms. The `LICENSE` file governs where this summary and the license differ.

Participation does not grant an exclusive claim over MASI, a named responsibility, later implementations, or future commercial activity.

## Attribution and provenance

Research investment should remain attributable where practical.

Git history, commit authorship, pull requests, experiment records, citations, provenance files, and acknowledgments may all be used to preserve who contributed what.

Attribution does not imply:

- ownership of the entire architecture;
- permanent authority over a research direction;
- a veto over later evidence;
- a guarantee of attribution in every downstream derivative beyond what the applicable license requires.

Where a contribution materially affects a published experiment or claim, the project should preserve enough provenance to reconstruct that contribution's role.

## Time, expertise, and code are investments

The project should treat serious non-financial contribution as real investment.

A researcher spending forty hours reproducing an experiment, a domain expert externalizing years of tacit knowledge, or an engineer building a bounded implementation is making a meaningful commitment even when no money changes hands.

Before requesting substantial work, the project should make reasonably clear:

- the research question;
- the expected scope;
- the decision path;
- the applicable license;
- the evidence standard;
- what acceptance would and would not confer;
- whether compensation or sponsorship exists;
- who currently has repository decision authority;
- how disagreement or rejection will be recorded.

The goal is not to guarantee a contributor's preferred outcome. It is to make the rules legible enough for a rational decision about whether to participate.

## Financial sponsorship and commercial relationships

This repository does not, by itself, define an investment vehicle, sponsorship program, procurement process, or commercial partnership.

Money contributed to or around the project should not silently purchase:

- scientific conclusions;
- benchmark outcomes;
- authority over evidence;
- canonical specialist status;
- suppression of negative results;
- governance rights not otherwise documented.

Any financial sponsorship, grant, commercial license, employment arrangement, or investment relationship should state its terms separately and should not be inferred from ordinary repository participation.

## Forking, reuse, and exit

A contributor does not have to win an upstream architectural disagreement in order to continue exploring an idea.

Subject to the applicable license and third-party restrictions, participants may fork, reuse, adapt, or independently test repository material.

Rejection upstream therefore means:

> **this repository is not adopting this contribution under the current research program**

—not:

> **the contributor is forbidden from pursuing the idea elsewhere.**

This is an important protection against centralizing scientific permission in repository maintainers.

## Discussion and disagreement

Criticism should target claims, methods, evidence, baselines, interfaces, architecture, governance, or experimental design rather than the contributor.

Disagreement is not a process failure. In a research repository, preserved disagreement can be useful evidence.

Participants should be able to say:

- "the claim is unsupported";
- "the baseline is too weak";
- "the architecture is overbuilt";
- "this module adds no measurable value";
- "the contribution is useful but belongs outside this repository";
- "the evidence is inconclusive";
- "the governing question itself is defective".

Those conclusions should be evaluated by evidence and argument rather than contributor status.

## Relationship to `CONTRIBUTING.md`

Use this document to answer:

> **What does it mean to participate here?**

Use `CONTRIBUTING.md` to answer:

> **What makes a contribution scientifically and operationally useful?**

Both apply.

## Governance boundary

This compact intentionally stops short of defining MASI's long-term governance system.

It establishes a simpler prerequisite:

> **People should be able to understand the rules of participation before being asked to invest in the project.**

Who should hold architectural stewardship, merge authority, scientific-review authority, conflict-resolution authority, funding authority, and long-term constitutional authority remains a separate question that should be addressed explicitly rather than smuggled into contribution mechanics.
