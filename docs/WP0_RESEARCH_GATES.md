# WP0 research gates — 2026-09-18

**Status: documentation freeze submitted for independent Claude audit; not yet accepted.** This packet supplies design gates for Issues #1/#2, not an executable contract or permission to begin an experiment.

## Authority and preserved state

- Branch: `astra/wp0-research-gates`; governing main: `8de8bbdf956cd41d94c8dc1758b71f07f2b9b8e6`. The packet is the commit adding this record on that branch; resolve its exact identity with `git log -1 --format=%H -- docs/WP0_RESEARCH_GATES.md`.
- Scope: [Issue #1](https://github.com/JosephJMWalker-MBA/masi-research/issues/1), [Issue #2](https://github.com/JosephJMWalker-MBA/masi-research/issues/2), and the [latest operator disposition in Issue #4](https://github.com/JosephJMWalker-MBA/masi-research/issues/4#issuecomment-5725807257), read with all #4 comments. The older #4 body is not authorization to train or begin WP2.
- Governing [construction doctrine](CONSTRUCTION_DOCTRINE.md), [epistemic integrity](EPISTEMIC_INTEGRITY.md) and [AGENTS.md](../AGENTS.md) are unchanged. General-purpose components remain useful without becoming authority. Increased specialist complexity requires a measured capability deficit; bounded infrastructure/contracts may be justified by an explicit current protocol or reproducibility need.
- WP1 remains **accepted only as narrowed**, per [Audit Addendum B](AUDIT_WP0_WP1_2026-09-17.md). Builder `codex/wp0-wp1-candidate-probe @ 81adfffa2d28e4a40a0b36fe1a21baa567d402ec` remains frozen and unmerged. Its code, fixtures, tests, evidence, frozen contract and historical records are untouched.

## Decision and issue coverage

**Can the next experiment be designed without inventing thesis, boundary, outcome-record or resource rules during implementation? Yes, at the design-gate level, subject to this packet's independent audit.** The invariants below are frozen for review. Task-specific bindings must be resolved in a separately authorized protocol before implementation; final assets/revisions must be frozen before final observation. Documentation readiness is neither execution readiness nor empirical validation.

| Requirement | Decision frozen in this packet | Governing detail |
| --- | --- | --- |
| #1 strongest claim and distinguishable hypotheses | Retain H1–H7, H2A/H2B and falsifiers 1–10. H7 is the untested system claim; a later construction claim is H2B, requiring quality competitiveness **and** a preregistered property improvement. H2A needs its own same-base contrast; interface-only work may target bounded H4. | [Thesis](RESEARCH_THESIS.md#wp0-claim-and-decision-gate) |
| #1 controls and confounds | Claim-linked contrasts distinguish decomposition, construction/adaptation, aggregation, routing, extra inference and feedback. Missing controls block attribution; null/simple-system wins remain valid. Confounds and reject/narrow/inconclusive rules are explicit. | [Control matrix](RESEARCH_THESIS.md#required-controls) and [falsifiers](RESEARCH_THESIS.md#strong-falsifiers) |
| #2 responsibility boundary | Identity/class, input references, native output, required bounded state, uncertainty, dispositions, assumptions, provenance and resources; no common internals or fabricated confidence/rationale. Multiple implementations and unresolved disagreement remain visible. | [Boundary and family distinctions](MODULES.md#minimum-semantic-boundary--wp0-gate) |
| #2 Reality Audit | Linked decision-time evidence, prediction/proposal, assumptions, action/authority, horizon, later evidence and correspondence assessment; append-only temporal separation. No learner. | [Minimum record](MODULES.md#minimum-reality-audit-record) |
| #2 Bus ownership | Reuse existing message semantics; experiment records supply research provenance and actual gaps. No Bus fork or new universal envelope. | Ownership table below |
| #1/#2 credible resource comparison | Required observations, missingness reasons, scope/units, failed-attempt accounting and limits on comparability. | [Resource minimum](EVALUATION.md#resource-accounting) |
| E1 future-contract decision | Independent reference tables/checks required for claim-critical deterministic semantics; frozen rubric/independent assessment for non-deterministic quality. No WP1 repair. | [E1 decision](EVALUATION.md#independent-reference-checks--e1-decision) |

Issue #1 is addressed at research-gate granularity, not by choosing a benchmark. Issue #2 is addressed at semantic-contract granularity, not by implementing all four responsibilities or a transport. Issue acceptance/closure remains an operator/auditor disposition; no issue state is changed here.

## MASI Bus ownership and gaps

Current MASI Bus was inspected before drafting the boundary: default-branch head `b9d8d632f7a3d1b4528d80bfad6c743e4e3ed490`, freshly checked for this packet. Inspected [README](https://github.com/JosephJMWalker-MBA/masi-bus/blob/b9d8d632f7a3d1b4528d80bfad6c743e4e3ed490/README.md), [v1.0 schema](https://github.com/JosephJMWalker-MBA/masi-bus/blob/b9d8d632f7a3d1b4528d80bfad6c743e4e3ed490/schema/masi-bus-schema.json) and [critique example](https://github.com/JosephJMWalker-MBA/masi-bus/blob/b9d8d632f7a3d1b4528d80bfad6c743e4e3ed490/examples/03_foresight_critique.json). The README describes a reference artifact, not an operating runtime or certification authority.

The categories identify semantic ownership, not mandatory new JSON keys. A manifest/reference can satisfy experiment-owned information. Responsibility-specific semantics must be fixed by the task profile; they do not become a universal schema merely because a record carries them. Local experiments need not emit Bus messages; if they do, preserve the existing Bus meanings and reference the original message rather than creating a competing envelope.

| Candidate information | Ownership | Existing semantics / bounded disposition |
| --- | --- | --- |
| Message kind, sending role, task association | `BUS-OWNED` | Reuse `message_type`, `sender_role`, `task_id` (UUID). Role is not exact implementation identity or contract version. |
| Message timestamp, previous-message link, conflicts | `BUS-OWNED` | Reuse `audit_trail.timestamp`, `previous_message_id`, `conflicts`. These alone do not identify evidence snapshots or outcome availability. |
| Actual textual analysis/assertions/proposed action | `BUS-OWNED` | Reuse `content.analysis`, `assertions`, `proposed_action` when those values really exist. A proposal is not a selected or executed action. Do not generate prose merely to fill the field. |
| Reported scalar confidence/cost and optional risk values | `BUS-OWNED` | Preserve `metrics.confidence`, `cost`, `risk_quantification` when meaningful. Their presence proves neither calibration nor common units. Detailed semantics/measurements below do not redefine these fields. |
| Contract/profile and implementation identity/class | `EXPERIMENT-RECORD-OWNED` | Link the bounded profile and existing candidate record: component, adapter/mapping, source/revision, class, license/lineage status. `sender_role` cannot distinguish competing implementations of one role. |
| Experiment/run/attempt/output identity and input/evidence/native-artifact references | `EXPERIMENT-RECORD-OWNED` | Stable scoped references, versions/hashes where available, input→native→normalized derivation, actual attempt/source and transformation history. The schema has `previous_message_id` but no declared top-level message ID. Retain existing external message references; an experiment reference does not add a Bus field. |
| Input/output ontology and native format, normalized bounded state and mapping semantics | `RESPONSIBILITY-SPECIFIC` | Profile declares allowed evidence/capacity, units, state meaning and any lost distinctions. Retain native artifacts; neither `analysis` nor an untyped extension defines these semantics. |
| Uncertainty meaning, assumptions, abstention and escalation criteria | `RESPONSIBILITY-SPECIFIC` | Domain/referent, method, calibration status, reason/scope and unsupported assumptions; no mandatory probability. An actual escalation message reuses Bus `ESCALATION`; abstention is a judgment disposition, not automatically a message type or execution failure. |
| Execution status, failure/blockage, escalation request/disposition and actual authority/action references | `EXPERIMENT-RECORD-OWNED` | Distinguish successful computation, withheld judgment, failed execution, request, permission and action. Bus message types and credentials do not encode or enforce this history. |
| Resource observations and measurement methods | `EXPERIMENT-RECORD-OWNED` | Calls/passes, volume/context, timing, hardware/memory/storage, cost provenance, retries, tools and concurrency. Link any existing Bus cost; no second unexplained cost scalar. |
| Reality Audit linkage, decision-time snapshot, later evidence, observation/availability times and assessment provenance | `EXPERIMENT-RECORD-OWNED` | Reuse message/task/input/output references. Separate immutable earlier state from later observations; ordinary message timestamps do not establish this distinction. |
| Prediction/target, action conditions, consequence units/horizon and error/correspondence rule | `RESPONSIBILITY-SPECIFIC` | Defined for the bounded forecast/decision/observation family, not a universal utility or confidence score. Linked in the Reality Audit record. |
| Global trust/utility score, automatic influence update, certification authority, common latent state, universal rationale/probability | `NOT YET JUSTIFIED` | Bus has optional `trust_score_delta` and `module_cert_id`, but they establish no validated scoring method or authority. No new field, service or mandatory use is earned in this packet. |

**Documented compatibility gap:** Bus v1.0 requires `content.analysis` as a string, `metrics.confidence` as a number in [0,1], and `metrics.cost` as a nonnegative number. It does not define unknown/not-applicable values, confidence referents/calibration or cost units. A deterministic proof or unavailable cost cannot truthfully satisfy those requirements by inventing a probability, zero or rationale. Top-level extra properties are prohibited; `content` permits extras but supplies no standard native-output semantics. Permissive nesting is not semantic interoperability.

**Decision:** keep truthful native/experiment records with the declared semantic profile. If Bus participation is later necessary, test compatibility and propose only the specific missing representation through Bus's own review; mark unresolved participation as blocked rather than claiming v1.0 conformance. No Bus change is necessary for this documentation/design packet. A future mandatory-Bus experiment may have that small compatibility blocker; a local experiment does not need a Bus implementation to be designed.

## Focused prior-art reuse

These primary sources were inspected for narrow obligations, alongside existing [PRIOR_ART.md](PRIOR_ART.md). This is not a new candidate search or a claim of standards conformance.

| Source | Reused primitive / decision | What is not adopted or established |
| --- | --- | --- |
| MASI Bus v1.0 at the pin above | Existing message/task/role/proposal/audit meanings; explicit ownership and gaps. | No fork, transport or claim that schema validation proves competence/authority. |
| [W3C PROV-DM, Recommendation 2013-04-30](https://www.w3.org/TR/2013/REC-prov-dm-20130430/) | Entity/activity/agent and usage/derivation distinctions for input, output and decision/outcome provenance. | No RDF store, provenance platform or causal guarantee. |
| [CloudEvents v1.0.2, identity](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#id) | Scope a record's stable ID to its source; retransmission is not a new observation. A new computational attempt gets its own reference. | No second event envelope, broker or transport dependency. |
| [MLPerf inference policies at `d3eba2f`](https://github.com/mlcommons/inference_policies/blob/d3eba2f21026d868ad65cdcad2bb81e4a17ce3d3/inference_rules.adoc) | System-under-test boundaries, pre/postprocessing and scenario-aware resource reporting. | No MLPerf benchmark, score or compliance claim. |
| [Self-Consistency, Wang et al., v4](https://arxiv.org/abs/2203.11171v4) | Same-model extra-sampling/simple-aggregation control for a claimed composition gain. | No MASI effect inferred from that paper; no model added. |
| [Selective Classification, Geifman and El-Yaniv, 2017](https://proceedings.neurips.cc/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html) | Quality/risk evaluated jointly with coverage. | No imported guarantee or compulsory probability output. |
| [Concept Bottleneck Models, Koh et al., 2020](https://proceedings.mlr.press/v119/koh20a.html) | Existing prior-art basis for testing semantic intervention when inspectability is claimed. | No universal internal representation or new target architecture. |

Established concepts plus linked records suffice. No custom schema package, runtime, router or learner is justified by these gaps.

## Still provisional and deliberately unselected

- **Experiment choice and authorization:** no next task family, E001/K001 execution or DeepSeek/state-calibration implementation is selected. K001 remains a candidate later bounded experiment.
- **Protocol bindings:** primary estimand, competent baseline implementations, actual data/labels, numeric margins/coverage floor, uncertainty/sample plan, metrics, budget caps, timing methods and stop rules. These must be settled before implementing the experiment; this packet creates no splits or candidates.
- **Family profile:** exact native/normalized types, allowed inputs, limits, uncertainty/abstention/escalation thresholds, and authority destination. No universal confidence or consensus rule is frozen.
- **Reality Audit application:** target/horizon, outcome sources, availability rules, correspondence/error metric and treatment of missing/censored evidence. The record can preserve these facts but cannot by itself identify causal benefit or remove selection bias.
- **Transport and reference checks:** serialization and any needed Bus compatibility proposal remain unimplemented; experiment-specific independent expected cases and reviewers must be bound before final observation.

The smallest blocker to implementation is a **separately authorized, audited bounded protocol that binds these choices**, after this WP0 audit. It is not a need for more general MASI architecture. No capability deficit has been established that would justify learned complexity.

## Handoff and checks

Changed files are limited to:

```text
README.md
STATUS.md
docs/RESEARCH_THESIS.md
docs/MODULES.md
docs/EVALUATION.md
docs/IMPLEMENTATION_SPRINT_001.md
docs/WP0_RESEARCH_GATES.md
```

This is a documentation-only packet. No new model inference, tests of model behavior, training, candidate selection, split creation, runtime, outcome learner, Wisdom implementation or Bus mutation was performed. No WP1 artifact is imported or modified. No H1–H7 result, efficacy, calibration, generalization, open-set/cross-paradigm substitution, composition/governance benefit or capability deficit is established.

Pre-commit checks performed against governing `8de8bbdf956cd41d94c8dc1758b71f07f2b9b8e6`:

- `git diff --cached --name-status 8de8bbdf956cd41d94c8dc1758b71f07f2b9b8e6`: exactly the seven Markdown files above (six modified, one added), matched to an explicit allowlist. No non-documentation change or builder artifact import.
- `git diff --cached --check 8de8bbdf956cd41d94c8dc1758b71f07f2b9b8e6`: PASS over the actual staged packet, not an empty working-tree check.
- Read-only byte comparison of every other tracked path against `git show <governing-main>:<path>`: all **15** unchanged, including doctrine, AGENTS, registry, audit, historical handoff/reconciliation and WP1 documents. Builder-only code, frozen files and evidence remain absent.
- Local Markdown link/heading scan across the seven documents: **66** local links resolve, including fragments; **3** existing builder-pinned links resolve to paths in `81adfff` through Git object lookup. External primary sources were inspected as cited above; this is not a blanket external-link uptime test.
- Git ancestry/ref checks: the branch descends from exact governing main; `origin/main` remains at `8de8bbd`; both local and remote-tracking builder refs remain at `81adfff`. The isolated worktree leaves the original checkout and its untracked assets untouched.
- Text comparison against governing main: all eight existing hypothesis headings (including H2A/H2B) and all ten numbered falsifiers are unchanged.

A supporting same-family reader reviewed request coverage and identified two drafting defects: an overly broad exception to the specialist-complexity gate and an overly broad ban on using implementation identity. Both were corrected: measured deficits remain required for increased specialist complexity, and declared provenance/measured history may inform a future frozen policy without granting identity-based authority. This is supporting review, not Claude's independent audit.

No model tests or stored-evidence verifiers were run in this documentation packet. No historical WP1 test/verifier result is claimed as a fresh check.

**Exact proposed next action:** independent Claude audit of this branch's documentation diff against `8de8bbdf956cd41d94c8dc1758b71f07f2b9b8e6`: check Issue #1/#2 coverage, doctrine fidelity, Bus ownership/gap accuracy, resource comparability, E1 independence requirements, frozen versus provisional decisions, and absence of code/evidence changes. Record an audit disposition. Do not reopen WP1, start WP2/E001/K001, merge the builder branch or infer implementation authority from this packet. Stop here for that audit and subsequent operator decision.
