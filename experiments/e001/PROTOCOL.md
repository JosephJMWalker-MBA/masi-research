# MASI-E001 — Preregistered protocol v1.1

- **Protocol ID:** `e001-protocol-v1.1`
- **Status:** **repaired freeze submitted for a second fresh independent audit. Not accepted. Not authorized for execution.** No data, labels, model runs or results exist for this protocol.
- **Revision:** v1.0 was frozen at commit `d1d9bfc40c40e607f0a476bb620bb665c3b8830a`.
  - Its [independent audit](https://github.com/JosephJMWalker-MBA/masi-research/pull/17#issuecomment-5735626914) returned `REPAIR_REQUIRED` (R1–R7).
  - v1.1 repairs R1–R7 and closes the audit's non-blocking EVCP-citation observation (§27).
  - The v1.0 text (git history) and the audit comment (on the PR) are preserved unchanged.
- **Issue:** [#3](https://github.com/JosephJMWalker-MBA/masi-research/issues/3), under the operator authorization on Issue #3 and PR #16.
- **Governing main:** `904bd9bc1c482c5b552b4a2e7075d685d73a1748`
- **Substrate inspected:** `JosephJMWalker-MBA/Accumulated-Distress-Care-Protocol @ eb7ac37f79511c90e25ff613ee78e9123d653d60` (refetched 2026-09-18)
- **Frozen WP1 packet:** `codex/wp0-wp1-candidate-probe @ 81adfff`. Untouched; nothing is imported from it.

**Companion files:**

- [`ANNOTATION_RUBRIC.md`](ANNOTATION_RUBRIC.md): the task definition shared by annotators and all arms. Content unchanged in v1.1.
- [`REFERENCE_CASES.md`](REFERENCE_CASES.md): the E1 independent reference checks.
- [`PROTOCOL_MANIFEST.json`](PROTOCOL_MANIFEST.json): preregistration facts only.

**Governing rules:**

- [`CONSTRUCTION_DOCTRINE.md`](../../docs/CONSTRUCTION_DOCTRINE.md)
- [`EPISTEMIC_INTEGRITY.md`](../../docs/EPISTEMIC_INTEGRITY.md)
- [`RESEARCH_THESIS.md`](../../docs/RESEARCH_THESIS.md): H2B gate, required controls, falsifiers.
- [`MODULES.md`](../../docs/MODULES.md): semantic boundary and Reality Audit.
- [`EVALUATION.md`](../../docs/EVALUATION.md): resources and E1.
- [`WP0_RESEARCH_GATES.md`](../../docs/WP0_RESEARCH_GATES.md)

**Freeze classes used below:**

| Tag | Meaning |
| --- | --- |
| **[FROZEN]** | Protocol-decidable. Fixed by this document. |
| **[BIND]** | Must be bound before implementation. The procedure is fixed here; the value or resource is supplied before any arm is built. |
| **[DEV]** | May be selected using train/dev data only, by the rule stated. |
| **[LOCKED]** | Stays locked until final evaluation. |

---

## 1. Question, hypotheses and scope

**Research question [FROZEN; unchanged from v1.0]:** Can a purpose-built bounded intelligence, designed from the Empathy-observation responsibility outward, infer an evidence-grounded observation state competitively with general-model controls while providing stronger inspectability, state discipline, uncertainty handling, efficiency, or failure localization?

**Primary hypothesis: H2B [FROZEN].** On the E001 speaker-observation task, the designated purpose-built target `T` must satisfy all of the following (full rule in §14):

1. **Observation-state quality.** T is non-inferior to every competent control on:
   - **evidenced-concern quality Q**;
   - **observation-state quality S**, which makes the distinctions between CONTRADICTED, INDETERMINATE and NOT_ADDRESSED consequential;
   - **evidenced-concern recall R** (a coverage floor).
2. **Property.** T improves one preregistered property, *evidence-verified claim precision (EVCP)*, over every general-model control **by a superiority margin of at least 0.10**, established at the stated confidence. In other words, the lower confidence bound must exceed 0.10.

**Claim scope.**

- The confirmatory "observation state" is the four-class per-dimension state defined in §13.1.
- The SUPPORTED-versus-MIXED split, the evidence basis (EXPLICIT/INFERRED) and the safety field are descriptive only.
- If gate G5 (§7.5) fails, S-NI is removed **before implementation** and H2B is narrowed to *evidenced-concern detection with evidence-verified precision*. The narrowing is recorded in the P1 binding record and in the result headline.

**Review of legitimacy.** E001 can legitimately test H2B. The responsibility is bounded, the controls are constructible on the target hardware, and the property is measurable identically across arms. No research-question defect was found. The claim scope is narrow (§23).

**Secondary questions (descriptive only; no confirmatory claims):**

- construction-ladder effects (T0 → T1 → T2);
- `B0` versus `T`;
- performance on the boundary, adversarial and shift sets;
- safety-language routing;
- span quality;
- resources.

**H2A [FROZEN decision]: not part of E001's confirmatory protocol.**

- The competent adaptation control for this span-and-label task is a fine-tuned encoder (§10). Its "exact unadapted base" cannot perform the task, so no valid H2A contrast exists for it.
- An optional estimation-only module, `S-H2A` (§10.6), provides the exact same-base contrast (prompted base versus LoRA-adapted base), only if the operator activates it before implementation. Even then it makes **no confirmatory H2A claim**.
- Unrelated pretrained models are never evidence that adaptation helped.

## 2. Frozen responsibility (specialist gate)

```text
responsibility:        empathy.speaker_observation — from a short excerpt written by one speaker,
                       record which of seven human-impact concerns the text evidences about that
                       speaker now, with minimal evidence spans; flag safety-relevant language
allowed inputs:        unit text (1–4 turns by one speaker, ≤ 400 chars/turn, ≤ 1,200 chars total,
                       English) and turn boundaries; nothing else at inference
prohibited inputs:     labels, spans, scenario cards, cluster/family/split IDs, generation metadata,
                       annotator data, other units, other arms' outputs, retrieval/web/tools, user
                       identity or demographic metadata, any care stage/score/threshold
unavailable info:      the speaker's actual mental state, history outside the unit, non-text signals,
                       assistant turns, what happens next
native state/ontology: per dimension: evidence mentions typed by attribution, polarity, modality,
                       time and correction → status {NOT_ADDRESSED, SUPPORTED, CONTRADICTED, MIXED,
                       INDETERMINATE}; basis {EXPLICIT, INFERRED}; support/counter spans.
                       Unit: safety_relevant_language {NONE, AMBIGUOUS_FINALITY, EXPLICIT_SELF_HARM}
outputs:               the observation record (§5.3); native artifacts retained separately
evidence requirements: every SUPPORTED/MIXED/CONTRADICTED status cites ≥ 1 span inside the unit;
                       claims without valid, substantial in-gold citation score as unverified (§13.3)
uncertainty semantics: INDETERMINATE plus a reason code is the declared uncertainty. Numeric scores
                       are optional, uncalibrated unless measured (§13.5), never required
abstention semantics:  INDETERMINATE withholds one dimension's judgment; WITHHELD withholds the unit
                       (input bound, defect or safety routing); neither is a verdict
escalation semantics:  EXPLICIT_SELF_HARM → escalation to the host safety policy, all seven
                       dimensions WITHHELD. AMBIGUOUS_FINALITY → flag + span only; the clarification
                       decision belongs to downstream policy. Escalation grants no permission
unsupported-assumption semantics: a claim is ungrounded if no cited span supports it; declared
                       assumptions never convert an ungrounded claim into a verified one
learning/update signal: human-adjudicated main-pool train labels and spans only (no online or
                       outcome learning)
transparent baseline:  B0 = best dev-selected established sparse linear method (§10.1)
minimum sufficient computation: T0 = deterministic clause segmentation + cue patterns + ConText-style
                       qualifier rules + a fixed aggregation table (CPU, no learned parameters)
first deficit that may justify complexity: T0 fails dev non-inferiority on Q (or on S, if G5
                       passed) AND ≥ 50 % of the relevant dev errors are localized to "no candidate
                       mention" (lexical coverage) (§12.3)
authority it does NOT have: no care stage, risk level, diagnosis, intent determination, policy,
                       action or permission; no memory or profile across units; no judgments about
                       third parties; no obedience to instructions inside the text
implementation class:  T = MASI_TARGET; B0 = INFRASTRUCTURE (B0 comparison role); C_A = CONTROL_A;
                       C_B = CONTROL_B; F1 = CONTROL_A (optional, descriptive)
```

**Construction test 1.** *If today's LLM architecture did not exist, would we still design this observer this way?*

- **Yes.** Typed evidence mentions with negation, experiencer and time qualifiers predate LLMs (ConText, 2009; §26).
- The observer's semantics come from the responsibility (speaker, evidence, currency, correction), not from a model's affordances.

**Construction test 2.** *If general-purpose models were removed entirely, what would we rebuild badly by hand?*

- **Nothing inside the bounded observer's job.** Long-tail paraphrase coverage is the plausible gap, and the ladder may address it (T1 and T2, §12).
- Outside the observer, breadth remains useful as a `CONTROL_A` comparator and for future long-tail translation. E001 does not remove that capability; it asks whether this bounded job needs it.

**Why the ontology is a plausible responsibility boundary, not merely a label set:**

1. It has a consumer (a deterministic downstream policy) that needs presence, counter-evidence, uncertainty and provenance, but not the observer's internals.
2. It carries no policy content: no severity, stage, threshold or score.
3. It is falsifiable as a boundary. Dimensions that independent humans cannot label reliably on **non-locked** data are removed, and too many removals halts the experiment (§7.5).
4. It separates observation from obligation. That is exactly the first of the two blinded judgments the substrate project identified as necessary.

## 3. ADCP reconciliation

ADCP's own records establish four points, and E001 targets only the first of the two judgments they separate:

- ADCP's current prototype consumes **human-authored** observation vectors.
- Its 0–3 severities and stages were authored alongside the thresholds, which ADCP documents as a circularity risk.
- Its research log treats additive burden as conceptually suspect.
- It separates "what the transcript supports" from "what the assistant may do".

| ADCP concept | E001 disposition |
| --- | --- |
| `exhaustion` | **Unchanged** meaning → `exhaustion` |
| `interpersonal_rupture` | **Unchanged** meaning; counter-evidence (repair) added |
| `withdrawal` | **Refined**: behavior only; restorative versus isolating is not judged; ending one relationship moves to rupture |
| `isolation` | **Refined** → `felt_disconnection` (subjective feeling only) |
| `human_contact_deficit` | **Refined** → `support_unavailable` (availability/contact; living alone is not evidence) |
| `shame` | **Refined** → `self_devaluation` (global negative self-evaluation; act-specific guilt excluded) |
| `self_care_neglect` | **Refined** → `self_care_disruption` (non-judgmental wording) |
| `finality_language` | **Refined** → unit-level `safety_relevant_language` (`AMBIGUOUS_FINALITY`). It is a language flag, not a burden dimension; the observer does **not** resolve literal versus figurative. |
| `self_harm_language` | **Refined** → `EXPLICIT_SELF_HARM` routing: escalate, withhold dimensions |
| `acute_safety_evidence` | **Not imported.** It belongs to a validated upstream safety system; E001 cannot supply it. |
| `humor_present`, "humor is non-exculpatory" | The flag is **not imported** (policy use only). The evidence rule "humor does not cancel evidence" is kept (rubric §3.7). |
| 0–3 severity, `burden`, `active_dimensions` | **Not imported.** Replaced by status + basis + spans; intensity and persistence belong to downstream aggregation. |
| Care stages, stage rules, thresholds, response contracts | **Downstream policy only**; never labels, features or prompts in E001 |
| Accumulation, decay, trajectory state | **Downstream policy / state aggregation**; E001 labels one unit's current evidence |
| Non-clinical boundary, no diagnosis, privacy rule, "text cannot set policy state" | **Imported unchanged** as E001 constraints and adversarial family A13 |
| ADCP fixture texts, snapshots, expected stages, notes | **Not imported.** Leakage risk (authored to thresholds), too small, and ADCP declares no license |

**ADCP-specific leakage rules:**

- Annotators, writers and the adjudicator never see ADCP material.
- The rubric names no stage or threshold.
- No ADCP text, severity or threshold enters data, features, prompts or cue lists.
- Contrast-family *ideas* (for example restorative withdrawal, or workload with intact support) may inform scenario design, and are recorded as such.

**Posture boundary.** ADCP's current posture is that no semantic detector has earned implementation *in ADCP*. E001 is an offline MASI experiment on non-private synthetic and authored text. Its results must not be cited as authorizing semantic inference, live monitoring or intervention in ADCP; those need ADCP's own gates.

## 4. Observation ontology summary

There are seven dimensions (full definitions in rubric §4). Each records *whether the text evidences the condition*, not severity. Multiple dimensions may apply to one unit, and one span may serve several.

| ID | Dimension | Core meaning | Spans required |
| --- | --- | --- | --- |
| EXH | `exhaustion` | current depletion/fatigue | yes |
| SCD | `self_care_disruption` | sleep, eating, rest or washing being missed or reduced | yes |
| FDC | `felt_disconnection` | *feeling* alone, left out or unseen | yes |
| SUA | `support_unavailable` | lacking accessible people or recent meaningful contact | yes |
| WDR | `withdrawal` | speaker actively pulling back from people or usual activities | yes |
| RUP | `interpersonal_rupture` | current conflict, rejection or estrangement involving the speaker | yes |
| SDV | `self_devaluation` | negative evaluation of self as a person | yes |

**Status values:**

- Per dimension: `NOT_ADDRESSED` (default), `SUPPORTED`, `CONTRADICTED`, `MIXED`, `INDETERMINATE` (+ reason code).
- `WITHHELD` is a system-only, unit-level value.

**Evidenced concern (E):** status ∈ {`SUPPORTED`, `MIXED`}.

**Confirmatory state classes (§13.1):**

| Class | Statuses |
| --- | --- |
| **E** | SUPPORTED ∪ MIXED |
| **CON** | CONTRADICTED |
| **IND** | INDETERMINATE |
| **NA** | NOT_ADDRESSED |

**Unit-level field:** `safety_relevant_language` ∈ {`NONE`, `AMBIGUOUS_FINALITY`, `EXPLICIT_SELF_HARM`}.

**Deliberately absent:** severity or intensity, diagnosis, risk level, motives, personality, demographics, third-party states, humor, and any stage or policy output.

## 5. Input/output contract

### 5.1 Unit [FROZEN]

- **Composition:** 1–4 turns by one speaker; each turn ≤ 400 characters; the unit ≤ 1,200 characters in total; English; UTF-8 NFC.
- **Canonical text:** turns joined by `\n`. Span offsets are character offsets `[start, end)` into this string.
- **Out of bounds:** units outside these limits are `UNIT_DEFECT`. The custodian repairs or excludes them before the cluster manifest is frozen (§8.1).
- **What labels describe:** the speaker's situation as presented by the end of the unit.

### 5.2 Evidence grounding [FROZEN]

```text
observed text  →  typed evidence (span + basis)  ≠  inference beyond the text  ≠  unsupported assumption
```

- The spans are the grounding. No prose rationale is required or scored.
- Evidence rules are rubric §3 (rules 1–13), shared verbatim by all arms. They cover multiple or contradictory spans, quotations, hypotheticals, third parties, sarcasm, time, corrections and missing context.
- **Quote-to-offset mapping**, for arms that emit quotes rather than offsets:
  - the first exact, case-sensitive occurrence of the NFC-normalized quote in the unit text;
  - no fuzzy matching;
  - an unmatched quote is an invalid span. It is recorded and never repaired.

### 5.3 Observation record (experiment-local; not a MASI Bus message) [FROZEN]

**Per unit:**

- `unit_id`, `input_sha256`
- `arm_id`, `implementation_class`, `artifact_hashes`
- `scope`: `IN_SCOPE`, `WITHHELD_SAFETY_ROUTED`, `WITHHELD_INPUT_BOUND` or `ERROR`
- `safety_relevant_language` + spans
- `escalation`: `{requested: bool, target: "host_safety_policy" | null, reason}`
- per dimension: `status`, `basis`, `support_spans`, `counter_spans`, `indeterminate_reason`, optional `score` + `score_semantics`
- `declared_assumptions: []`
- `native_output_ref`
- resources (§15)

**Validation rules:**

- The native output is retained separately and hash-linked.
- Normalization from native output to this record lives **behind each arm's boundary**, as a declared and auditable mapping. The caller has no arm-specific branches (the WP1 lesson).
- Malformed records → `ERROR`, counted in every denominator (see [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R9).

**Bus relation.** Records are local only. MASI Bus v1.0 requires numeric `confidence` and `cost`, which T0 cannot truthfully supply. Per WP0, no Bus participation is claimed and no Bus change is made.

## 6. Data provenance, privacy and construction

### 6.1 Rules (fixed before any data acquisition) [FROZEN]

**Sources:**

- No private conversations, real user messages, scraped social media or sensitive personal material.
- No public datasets in v1. Their license, consent and review cost is not justified for this bounded experiment.
- Units come from **scenario cards**, produced in one of two ways:
  - **(a) generated** by a pinned open-weight generator, then reviewed by a human (accepted, edited or rejected);
  - **(b) human-authored** by contracted writers who assign a publication license.
- Every unit records its provenance (`generated`, `generated_edited` or `human_authored`), plus generator or writer ID, card ID and cluster ID. These fields are custodian-only for locked sets.

**Scenario cards** hold a plain-language situation, a variant plan and intended content (for coverage planning only).

- They **never** contain ontology identifiers, status words or rubric definitions.
- The intended content is **never** used as a label.

**Explicit self-harm content:**

- Explicit self-harm text is human-authored only and confined to the SR set.
- It is non-graphic, with no methods, means or instructions, and it carries a content warning.
- Generated-text reviewers **reject** any generated unit containing explicit self-harm language (rubric §5).
- Before the cluster manifest is frozen (§8.1), the custodian screens every non-SR unit against rubric §5 and removes any explicit self-harm text, with a log entry.
- Anything that escapes this screening is handled by §7.6.

**Contributors:** writers and annotators give informed consent, are compensated, and may opt out. Their identities are pseudonymous in all artifacts.

### 6.2 Model assistance boundary [FROZEN]

**Allowed only for:**

- generating candidate unit text from cards (the generator);
- automated checks: deduplication, leakage scans, schema validation.

**Prohibited:**

- model pre-labeling;
- model-suggested spans;
- model adjudication;
- model-written rubric changes during labeling;
- showing any model output to writers-as-reviewers, annotators or the adjudicator.

**Human reference ≠ model-generated annotation ≠ policy output.**

### 6.3 Generator [BIND: reverify pin and terms; FROZEN eligibility]

- **Eligibility:**
  - an open-weight model under an OSI license, with no restriction on training uses of its outputs;
  - open training data preferred;
  - its family is **not** used by any arm.
- **Pinned candidate:** `allenai/Olmo-3-7B-Instruct @ 6e5971d9eba42665f5bd5a0fcf047f299ce1dccc`, Apache-2.0, with Ai2's research-use guidelines.
- **Generation settings:** fixed prompt template (recorded), temperature 0.8, top-p 0.95, per-unit seed recorded.
- **Frontier-API generation is prohibited** unless the provider's terms are verified to permit using outputs to train the classifiers in §10 and §12.

### 6.4 Pools and minimum sizes [FROZEN targets; BIND budget]

| Pool | Target units | Clusters | Source | Split |
| --- | --- | --- | --- | --- |
| Main | ~1,800 active + reserve (§8.1) | ~360 active cards (3–6 variants each) | ≥ 30 % human-authored, rest generated/edited | train 55 / dev 15 / test 30, by cluster hash |
| Boundary (BND) | ~200 | ~50 minimal-pair families | human-authored | 40 dev-visible / 60 locked |
| Adversarial integrity (ADV) | ~240 | 14 families (§9) | human-authored | 40 dev-visible / 60 locked |
| Safety routing (SR) | ~120 | 40 `EXPLICIT_SELF_HARM`, 40 `AMBIGUOUS_FINALITY`, 40 idiomatic `NONE` | human-authored | 40 dev-visible / 60 locked |
| Shift (SHF) | ~200 | held-out scenario families | human-authored by ≥ 2 writers who wrote nothing else | all locked |

**Card coverage targets (planning only):**

- each dimension is intended-positive in ≥ 18 % of main cards;
- each dimension has intended counter-evidence in ≥ 8 %;
- each dimension has intended-indeterminate content in ≥ 5 %;
- ≥ 20 % of cards are intended no-concern controls.

**Minimum usable locked main test (G4) [FROZEN].** The custodian checks these on adjudicated gold, over the D\* frozen from non-locked data (§7.5), before unlock:

- ≥ 500 units;
- ≥ 100 clusters;
- ≥ 60 gold-E instances for every retained dimension;
- ≥ 5 retained dimensions;
- if G5 passed, ≥ 80 gold-CON and ≥ 80 gold-IND (unit, dimension) pairs, pooled over D\*.

**If G4 is short:**

- The only permitted remedy is **reserve activation**: in the pre-frozen order, under the pre-frozen salt (§8.2).
- If the reserve is exhausted, the experiment is **halted**.
- G4 counts never change D\*, the margins, the gates or any design choice.
- The custodian releases only pass/fail and the number of reserve batches activated.

**Rationale.**

- With ≥ 60 positives, per-dimension F1 has a standard error of roughly 0.03–0.05. Averaged over ≥ 5 dimensions with cluster resampling, the macro standard error is roughly 0.015–0.02. This motivates the δ floors (§14.2).
- With ≥ 80 pooled instances, per-class F1 for CON and IND has a standard error of roughly 0.05, which puts S's four-class macro standard error at roughly 0.03.

## 7. Labeling procedure

### 7.1 Roles [BIND: named or pseudonymous people]

| Role | Count / constraints |
| --- | --- |
| Custodian | 1. Owns data, cluster manifest, splits and locked sets. Not an implementer, T designer or annotator. |
| Writers | ≥ 3, plus ≥ 2 separate writers for SHF |
| Annotators | ≥ 3, so every unit gets 2 annotators, neither of whom is its writer |
| Adjudicator | 1. Not a T designer or implementer. |

Implementers, T designers and the protocol author do not annotate or adjudicate.

### 7.2 Blinding and order [FROZEN]

- **Annotators see only:** the unit text and rubric §1–§5.
- **Annotators never see:** split, set, provenance, card, cluster, other labels, model output, ADCP or stage material.
- **Order:** each annotator's queue is a random permutation mixing all pools, with about 5 % known-answer QC items from a separate pool.

### 7.3 Coverage [FROZEN]

- **Double annotation plus adjudication:** dev, test, BND, ADV, SR and SHF.
- **Train:** single annotation, with a random 20 % double-annotated for QC. Train labels are declared lower-assurance.

### 7.4 Adjudication, disagreement preservation, versioning [FROZEN]

- Rubric §7 governs adjudication.
- Raw annotations are immutable and retained. Gold is a separate versioned record (`gold v1.0`).
- The high-agreement subset (both annotators agree on E status) is reported as a secondary slice.

**Corrections:**

- **Before data freeze:** logged changes, each with a reason.
- **After data freeze and before unlock:** only the custodian may correct, on an annotator-reported error, blind to any model output, with a changelog.
- **After predictions are committed:** gold is frozen. Any later correction is reported *alongside* the original, and the original scoring stays primary.

### 7.5 Agreement measures and gates (non-locked only; computed before any arm touches dev) [FROZEN rules; BIND values]

**Reliability set (RS).** RS is all double-annotated units of the *initially active* main-pool clusters in **dev**, plus the double-annotated 20 % QC subset of **train**.

- RS contains **no locked unit**.
- Units from reserve clusters activated later (§8.2) are never added to RS.
- Every gate below, and every margin in §14.2, is computed on RS only.

| Gate | Measure on RS | Rule |
| --- | --- | --- |
| G1 reliability | Krippendorff's α (nominal) on the binary E status, per dimension | Retain a dimension iff α ≥ 0.667. If > 2 dimensions fail → **halt** (ontology not labelable). The retained set is **D\***. |
| G2 span stability | EVCP_h (§14.2) | EVCP_h ≥ 0.80. Otherwise the property metric is invalid → **halt**. |
| G5 state reliability | Krippendorff's α (nominal) on the four-class state {E, CON, IND, NA}, pooled over (unit, d ∈ D\*) | α ≥ 0.667 keeps S-NI confirmatory. On failure, S-NI is removed and H2B is narrowed (§1). This is **not** a halt. |
| G3 annotator QC | known-answer accuracy (separate QC pool) | ≥ 90 %, per rubric §8 |
| G4 minimum sample | §6.4 (custodian-only, locked counts) | reserve activation or halt only |

- α ≥ 0.667 is Krippendorff's floor for tentative conclusions.
- D\*, δ_Q, δ_S, EVCP_h and the G5 outcome are recorded in the P1 binding record and **frozen before implementation**, from RS alone.

**Locked-pool agreement** (α, S_h and EVCP_h on test, BND, ADV, SR and SHF):

- the custodian computes it after adjudication and hash-commits it sealed;
- it is released only at U2, as a descriptive result;
- it never selects D\*, the margins, the gates or any design choice.

### 7.6 Explicit-self-harm pool defects (quarantine before data freeze) [FROZEN]

- **Trigger:** **either** annotator marks `EXPLICIT_SELF_HARM` on any unit outside the SR pool.
- **Effect:** the unit is a provenance/pool defect and is **quarantined from all pools and all metrics** before data freeze, regardless of its split.
- **Logging:** the quarantine is logged with unit ID, split and date. Only the count per split is released.
- **What the decision uses:** raw human annotation only. It never uses adjudicated locked gold or any model output, and it applies identically to every split.

## 8. Splits, custody and contamination

### 8.1 Clusters and the frozen cluster manifest (M0) [FROZEN]

**Clusters.** A cluster is a scenario card plus all its variants. Human-authored units form writer-declared families.

**Near-duplicate merge (before M0):**

- character 5-gram Jaccard ≥ 0.6 between units of different clusters → merge the clusters (union-find);
- exact normalized duplicates → keep one;
- a merged cluster takes its lexicographically smallest member ID;
- deduplication covers active and reserve clusters together.

**Reserve.** Beyond the active target, the custodian prepares **reserve** main-pool clusters:

- at least 20 % of the number of active main clusters;
- built to the same card specification;
- each with a fixed reserve rank 1, 2, 3, …

**Manifest M0.** Before any salt exists, the custodian freezes M0: a UTF-8 text file with one line per cluster, in ascending cluster-ID order:

```text
cluster_id <TAB> pool <TAB> role(active | reserve:<rank>) <TAB> member unit_id:sha256(canonical_text) entries, comma-separated in ascending unit_id order
```

**Commitment.** The custodian posts `SHA-256(M0 bytes)` as a comment on Issue #3. This is the **M0 commitment**, and its server timestamp is authoritative.

- The first such comment is binding.
- A later, different M0 is a protocol violation (S13).

**After M0:**

- No cluster or unit may be added, except by reserve activation (§8.2).
- `UNIT_DEFECT` text repairs keep the cluster ID and are logged as amendments.
- Removals, including §7.6 quarantines, are logged.
- Every attempted addition, activation, repair and removal is preserved in an append-only custodian log.

### 8.2 Salt and hash rule [FROZEN]

The salt is derived from public randomness, so no one can choose it:

```text
R*   = first round of the drand default (League of Entropy) chain
       8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce
       (genesis 1595431050, period 30 s; round r is released at genesis + (r − 1)·30)
       whose release time is ≥ the M0-commitment timestamp + 24 h
salt = SHA-256("e001-salt-v1:" + M0_hash_hex + ":" + randomness_hex(R*))   (lowercase hex)

b = int(SHA-256(salt + ":" + cluster_id).hexdigest()[0:8], 16) mod 100
main:            b < 55 → train;  55 ≤ b < 70 → dev;  b ≥ 70 → test
BND / ADV / SR:  b < 40 → dev-visible;  b ≥ 40 → locked
SHF:             all locked
```

- drand rounds are public, signed and permanently retrievable. Anyone holding M0 can verify the salt.
- The salt is not secret. What stays custodian-only until U2 is the M0 content for locked clusters: which cluster IDs map to which texts.
- **There is no re-salting.**

**Reserve activation (G4 only):**

- Reserve clusters are activated in ascending rank, in complete batches of 10.
- Each activated cluster enters **its own hashed bucket**, whether that is train, dev or test. There is never a choice of which clusters to activate.
- Activated units are annotated, screened (§7.6) and adjudicated like all other units, and are excluded from RS.
- After each batch, G4 is rechecked. If the reserve is exhausted with G4 unmet, the experiment is **halted**.
- All activation happens before data freeze.

Worked cases: [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R5.

### 8.3 Custody and visibility [FROZEN]

| Party | Sees | When |
| --- | --- | --- |
| Custodian | everything | from data construction |
| Implementers | train, dev and dev-visible special sets (texts, gold, spans) | from data freeze |
| Implementers | locked inputs (texts only) | phase U1, after all arm artifacts are hash-committed (§21) |
| Implementers | locked gold, and the locked mapping of M0 | phase U2, after raw predictions are committed |

Annotators see texts but no split information. The auditor has read access at P3 (the freeze) and after U2.

### 8.4 Contamination checks and the integrity quarantine [FROZEN]

**Label-leak scan.** Before M0, every unit is scanned for ontology identifiers and status words. Hits are rewritten or the unit is removed, **except** for units on the integrity quarantine register.

**Integrity quarantine register.** Units whose adversarial purpose requires label or status tokens: all A13 units, plus any other ADV unit the custodian registers, with a reason, before annotation. For registered units:

1. They stay **only** in the ADV pool.
2. They are exempt from rewriting.
3. Dev-visible registered units may be used **only** for capped development evaluation and error inspection. They are **never**:
   - training data;
   - few-shot examples;
   - sources for cue lists, rules or prompts.
4. At P3 and again at U1, the custodian scans every committed arm artifact for any 8-token sequence taken from **any** registered unit, dev-visible or locked. A hit → **invalidated**.

**Other checks:**

- No cross-split near-duplicates remain after the merge (verified).
- `C_A` few-shot examples come from main-pool train only.
- T cue lists and rules record the train/dev unit IDs that informed them.
- **At U1**, the custodian scans every committed arm artifact (cue lists, prompts, few-shots, training manifests) for any 8-token sequence shared with locked text and absent from train/dev. A confirmed leak → **invalidated**.
- The generator family is excluded from all arms.

## 9. Adversarial and epistemic-integrity cases

**Decision [FROZEN]: included.**

- Each ADV family has ≥ 15 units (about 240 in total), is human-authored and is labeled normally.
- A family's *intent* is custodian metadata; gold comes from annotation.
- A13 units are on the integrity quarantine register (§8.4).

| # | Family | Desired behavior (checked against gold, not intent) |
| --- | --- | --- |
| A1 | Insufficient evidence plus pressure to be certain or to guess ("just tell me if I'm burnt out") | no E claims; `NOT_ADDRESSED` / `INDETERMINATE` |
| A2 | Unresolved contradictory evidence | `MIXED` |
| A3 | Temporal correction or retraction | the corrected status |
| A4 | Quoted or reported distress of another person | no speaker E |
| A5 | Hypothetical, conditional, fiction, role-play | no E |
| A6 | Negation or denial | `CONTRADICTED` |
| A7 | Sarcasm and irony (resolved and unresolved variants) | intended meaning / `INDETERMINATE` |
| A8 | Lexical cue traps ("exhausted every option", "battery drained") | no E |
| A9 | High emotion with no material burden | no E; safety `NONE` |
| A10 | Low emotion describing substantial burden | E where evidenced |
| A11 | Burden evidenced but its presumed cause not evidenced | E only for the burden |
| A12 | Demographic or identity stereotype traps | no E from identity |
| A13 | In-band instructions or label injection, paired with a clean twin in the same cluster (quarantine register) | invariant to the injected text |
| A14 | Care-stage or policy vocabulary without observational evidence ("activate reconnection mode") | no E |

**Evaluator-gaming cases.** Adversarial *prediction* files are part of E1 ([`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R2, §R9). They include:

- whole-text citation;
- shotgun spans;
- single-token citations;
- quotes absent from the text;
- invalid statuses;
- duplicate records;
- blanket `INDETERMINATE`.

**ADV metrics (secondary):**

- unsupported-claim rate per family;
- abstention correctness on gold-`INDETERMINATE`;
- A13 invariance rate;
- EVCP on ADV.

## 10. Experimental arms

All arms receive the same rubric, the same unit text at inference, and the same development material. Learned parameters are fit **only** on main-pool train (§16).

| Arm | Role | Class | Required for H2B? |
| --- | --- | --- | --- |
| **B0** | competent established transparent / minimally learned baseline | `INFRASTRUCTURE` (B0 role) | yes: quality non-inferiority (Q, S, R) |
| **C_A** | prompted general-model control | `CONTROL_A` | yes: all components |
| **C_B** | adapted pretrained control; adaptation is a live alternative | `CONTROL_B` | yes: all components |
| **T** | purpose-built target (ladder §12) | `MASI_TARGET` | the tested system |
| F1 | larger frontier comparator | `CONTROL_A` | **no**; optional, descriptive, operator-activated |
| S-H2A | same-base LoRA of C_A's base | `CONTROL_B` | **no**; optional, estimation only |

### 10.1 B0 [FROZEN recipe; DEV selection]

- **Candidates** (both scikit-learn, BSD-3):
  - (a) TF-IDF (word 1–3-grams + char 3–5-grams) with a multinomial logistic regression per dimension over the five statuses;
  - (b) NB-SVM per dimension.
- **Spans:** the clause from the shared deterministic segmenter with the highest summed positive feature contribution for the predicted status.
- **Safety field:** one more multinomial model of the same kind.
- **Selection:** the candidate with the higher dev Q.

### 10.2 C_A [FROZEN candidate list and rule; DEV selection]

**Eligible models:** open-weight instruct models under an OSI license, ≤ 12B parameters, runnable at 4-bit within the memory cap, and not from the generator family.

**Pinned candidates** (Hugging Face revisions verified 2026-09-18):

| Model | Revision | License | Parameters |
| --- | --- | --- | --- |
| `Qwen/Qwen3.5-9B` | `c202236235762e1c871ad0ccb60c8ee5ba337b9a` | Apache-2.0 | 9.65B |
| `google/gemma-4-12B-it` | `707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7` | Apache-2.0 | 11.96B |
| `microsoft/Phi-4-mini-instruct` | `cfbefacb99257ffa30c83adab238a50856ac3083` | MIT | 3.84B |

**Fallback:** `mistralai/Mistral-7B-Instruct-v0.3 @ c170c708c41dac9275d15a8fff4eca08d52bab71` (Apache-2.0).

- It is used only if a candidate fails the implementation preflight, meaning it cannot run text-only at 4-bit within 13 GiB on MLX-LM or llama.cpp.
- The two multimodal checkpoints are used text-only.

**Prompt:**

- rubric §1–§5 verbatim;
- ≤ 8 few-shot units from main-pool train, excluding quarantine-register units;
- JSON output with quoted spans.

**Decoding:**

- greedy, single pass;
- reasoning or thinking modes **off**;
- JSON-schema-constrained decoding permitted;
- ≤ 700 output tokens; context ≤ 8k tokens;
- a 120 s per-unit timeout produces `ERROR`, with no retries.

**Selection:** model × prompt on dev-mini, then full dev. The final choice is the one with the highest dev Q.

### 10.3 C_B [FROZEN recipe; DEV hyperparameters]

- **Base:** `microsoft/deberta-v3-base @ 8ccc9b6f36199bec6961081d44eb72fb3f7353f3` (MIT).
- **Fallback:** `answerdotai/ModernBERT-base @ 8949b909ec900327062f0ebf497f51aef5e6f0c8` (Apache-2.0), used only if the MPS training preflight fails.
- **Architecture:**
  - multi-task: seven five-way status heads plus a safety head, on the pooled representation;
  - a per-dimension token evidence-tagging head, trained on gold support and counter spans;
  - spans are maximal tagged token runs for the dimension, mapped to character offsets.
- **Training:**
  - fp32 on MPS, ≤ 512 tokens, AdamW;
  - early stopping uses the **inner-validation fold** (§11), never dev;
  - every dev evaluation counts against the §11 caps.
- **Seeds:** three seeds at the chosen hyperparameters.
  - The confirmatory seed is the one with the **median dev Q**.
  - All seeds are reported on test.

### 10.4 T — see §12

### 10.5 F1 (optional) [BIND: operator activation]

**Conditions:**

- the provider's terms permit publishing results, verified in writing before the run;
- the provider is not the generator family;
- the same final C_A prompt is used;
- spend ≤ USD 150.

**Role:** descriptive only; outside the H2B decision.

**If terms forbid publication:** F1 results are not published, or F1 is not run.

### 10.6 S-H2A (optional) [BIND: operator activation before implementation]

**Design:**

- LoRA/QLoRA of the selected C_A base (MLX-LM, MIT), on main-pool train, with the identical prompt and output contract;
- compared with C_A, its exact unadapted base.

**Limits:** ≤ 24 h training; estimation with a 95 % CI only.

## 11. Competent-control definition (Addendum C requirement 1)

**Inner-validation fold [FROZEN].** Main-pool train clusters, in ascending order of SHA-256(`"innerval:" + cluster_id`), until they cover ≥ 10 % of train units.

- It is fixed at data freeze and identical for all arms.
- It is not used for fitting.

A control is **competent** only if every item below holds. The auditor verifies them at the pre-unlock check.

1. **Equal information:** the same rubric, development material and inference inputs as T. Learned parameters are fit on main-pool train only.
2. **Equal development allowance.** Hard caps, logged by the scoring harness, are identical for every arm; T's caps cover all of its rungs together:
   - ≤ 60 evaluations on **dev-mini**: whole dev clusters in ascending order of SHA-256(`"devmini:" + cluster_id`) until ≥ 100 units, fixed at data freeze and identical for all arms;
   - ≤ 12 evaluations on full dev;
   - unlimited cross-validation and inner-fold use inside train.
3. **Established recipe:** each arm follows the declared standard method (§10). Its hyperparameter space is declared before tuning.
4. **Stopping rule:** development ends when the caps are reached or the developer declares the arm final.
   - The final configuration is the one with the highest full-dev Q among those evaluated.
   - There is no test access.
5. **Sanity gates.** These replace v1.0's invalid "train-fold F1 ≥ dev F1" (§27, R6). A failure indicates a broken implementation, not ordinary variance.
   - **(a) All arms, format:** ≥ 98 % of dev outputs are valid records.
   - **(b) All arms, competence floor:** dev Q ≥ the dev Q of **R0**, the naive reference ([`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R10). R0 marks a unit-dimension SUPPORTED iff any quoted support example from rubric §4 occurs as a case-insensitive substring, and NOT_ADDRESSED otherwise, with no qualifiers.
   - **(c) Learned arms and rungs (B0, C_B, T1, T2, S-H2A), training integrity:**
     - training completes with no NaN or Inf in loss or gradients;
     - convex solvers report convergence;
     - gradient-trained models have a mean final-epoch training loss ≤ 0.5 × their mean first-epoch loss.
   - **(d) Learned arms and rungs, fit floor:** inner-validation-fold Q ≥ R0's Q on the same fold.
   - **(e) All arms, reproducibility:** a re-run of the frozen pipeline reproduces the dev-mini predictions.
     - Deterministic arms (B0, T0, T1, and C_A with greedy decoding): identically.
     - MPS-trained C_B and T2 heads: ≥ 99 % identical per-pair statuses, with scores within 1e-6 when emitted.
6. **Reproducibility provenance:** pinned revisions, environment lock and seeds are recorded.
7. **If a control fails a gate:**
   - **B0:** the other B0 candidate replaces it. If both fail, the implementation defect must be fixed within the remaining caps; otherwise **halt**.
   - **C_A / C_B:** the fallback model is used.
   - A control may never be left weak. A failed competence gate that cannot be fixed means **halt**, not "T wins".

**Learned complexity is justified only from T's own ladder** (§12.3), whose first rung (T0) is a full-budget, transparent, purpose-built system. The escalation threshold is the *maximum* over competent controls, so a weak B0 can never lower the bar or manufacture a deficit; only a strong control can raise it.

## 12. Purpose-built target and complexity ladder

### 12.1 Starting representation (designed from §2) [FROZEN]

The pipeline runs in fixed stages. Every intermediate is typed and logged as a trace, which is what makes failure localization possible.

1. **Segmentation:** unit → turns → clauses (deterministic segmenter).
2. **Candidate evidence mentions per dimension:**
   - the dimension (support or counter);
   - the span;
   - `experiencer` ∈ {SPEAKER, OTHER, UNCLEAR};
   - `polarity` ∈ {AFFIRMED, NEGATED};
   - `modality` ∈ {ACTUAL, HYPOTHETICAL, REPORTED_UNCONFIRMED, NONLITERAL_UNRESOLVED};
   - `time` ∈ {CURRENT, PAST_RESOLVED, UNCLEAR};
   - `superseded` ∈ {yes, no}.
3. **Deterministic aggregation to status** (a fixed table; the truth table is in [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R7):

   ```text
   S = support mentions with SPEAKER, AFFIRMED, ACTUAL, CURRENT, not superseded
   C = counter mentions with the same qualifiers, or support cues NEGATED by the speaker (ACTUAL, CURRENT, not superseded)
   U = support or counter cues with experiencer UNCLEAR, or modality ∈ {REPORTED_UNCONFIRMED, NONLITERAL_UNRESOLVED}, or time UNCLEAR
   S≠∅, C=∅ → SUPPORTED          S=∅, C≠∅ → CONTRADICTED       S≠∅, C≠∅ → MIXED
   S=∅, C=∅, U≠∅ → INDETERMINATE (reason by precedence: ATTRIBUTION_UNCLEAR > NONLITERAL_UNRESOLVED > REPORTED_UNCONFIRMED > TEMPORALLY_UNCLEAR)
   otherwise → NOT_ADDRESSED   (HYPOTHETICAL, OTHER-experiencer and PAST_RESOLVED mentions are dropped)
   spans = S (support) and C (counter); basis = EXPLICIT if any S cue is on the explicit list, else INFERRED
   ```

4. **Safety patterns:** `EXPLICIT_SELF_HARM` → route; `AMBIGUOUS_FINALITY` → flag.

### 12.2 Rungs [FROZEN]

**Deterministic in every rung:** segmentation, qualifier rules, aggregation and safety routing.

| Rung | Added element | Its sole responsibility | Class note |
| --- | --- | --- | --- |
| **T0** | hand-authored cue and counter-cue patterns per dimension; ConText-style trigger lists for the qualifiers | candidate mention detection | no learned parameters |
| **T1** | per-dimension sparse logistic-regression clause scorers (n-grams + qualifier features), trained on main-pool train clauses that overlap gold support/counter spans; they replace or augment T0's cue detection | candidate mention detection (lexical coverage) | minimally learned; no pretrained representation |
| **T2** | T1 features + frozen sentence embeddings from `sentence-transformers/all-MiniLM-L6-v2 @ 1110a243fdf4706b3f48f1d95db1a4f5529b4d41` (Apache-2.0, 22.7M parameters) feeding linear heads | candidate mention detection (paraphrase coverage) | includes a **frozen general pretrained sensor**; claims must say so |

**No T3.** End-to-end fine-tuning of a pretrained model would be `C_B`, not the target.

### 12.3 Escalation rule (dev only) [FROZEN]

**When it is evaluated:** once per rung, after that rung is declared final within its share of T's caps, and only after B0, C_A and C_B are frozen.

**Rung r → r+1 is permitted iff both (a) and (b) hold.**

- **(a) Quality shortfall.** At least one of:
  - Q_dev(r) < max(Q_dev(B0), Q_dev(C_A), Q_dev(C_B)) − δ_Q;
  - **(if G5 passed)** S_dev(r) < max(S_dev(B0), S_dev(C_A), S_dev(C_B)) − δ_S.

  The comparison set is the same competent set K used for final non-inferiority (§14.1).
- **(b) The shortfall is localized to lexical coverage.**
  - Take the dev errors of each short metric: for Q, gold-E pairs predicted not-E; for S, misclassified pairs. If both metrics are short, pool the errors.
  - Keep only errors with at least one gold span (support, counter or INDETERMINATE-bearing). False positives on gold-NA pairs have no gold span and are excluded.
  - At least 50 % of the remaining errors must carry the trace category `NO_CANDIDATE_MENTION`: no mention of the dimension (support or counter) was detected in any clause overlapping a gold span for that pair.

**Outcomes:**

- **(a) holds without (b):** the deficit lies in qualifiers or aggregation, and escalation would not address it. Rules are revised *within the current rung*. The 50 % rule makes escalation target the majority failure source.
- **(a) fails:** the current rung is final. A transparent T0 that suffices is a **valid result: no learned target is justified**.
- **After T2:** no further escalation.
  - A shortfall at T2 means T2 still goes to final evaluation, so the negative result is preserved.
  - Any redesign needs a new protocol version **and a new locked test set**.

**Designation:** the final rung is designated and hash-committed before U1. Every developed rung is also run on locked data, for the descriptive ladder only.

## 13. Metrics

All metrics are computed on the locked **main test** pool unless stated otherwise.

- **Denominator:** every assigned, non-quarantined unit, over the retained dimensions D\*.
- **Missing predictions:** `ERROR`, `WITHHELD` and missing units:
  - count as predicting non-E for every dimension in Q, R and EVCP;
  - count as the non-class `NONE_OUTPUT` in S (§13.1), which is wrong for every gold class.
- **Explicit-self-harm units:** those quarantined under §7.6 are excluded everywhere, by a pre-freeze, prediction-independent rule. There is no gold-driven, post-assignment exclusion.

### 13.1 Primary quality metrics Q and S [FROZEN]

**Q (evidenced-concern quality).** Q is the macro-average over d ∈ D\* of F1_d for the event E, where F1_d = 2TP/(2TP+FP+FN).

- Gold `INDETERMINATE` counts as not-E. Claiming E there is a false positive: an unsupported assumption.
- Abstaining on a gold-E unit is a false negative. Refusal therefore cannot raise Q.

**S (observation-state quality; confirmatory when G5 passes).**

- **Pairs:** all (unit, d ∈ D\*) pairs, pooled across dimensions.
- **Gold class:** E, CON, IND or NA (§4). The arm's status is mapped the same way.
- **`NONE_OUTPUT`:** `ERROR`, `WITHHELD` and missing predictions map to `NONE_OUTPUT`, which matches no gold class. Withholding therefore never earns credit on gold-NA pairs.
- **Per-class F1:** F1_c = 2TP_c/(2TP_c+FP_c+FN_c).
- **S:** the unweighted mean of F1_c over the four classes. A class with no gold and no predictions in a given computation is omitted.

**Why both.** Q scores the responsibility's core output: evidenced concerns. S makes the declared observation state consequential: confusing CONTRADICTED, INDETERMINATE and NOT_ADDRESSED lowers S and can defeat H2B. The SUPPORTED-versus-MIXED split stays descriptive because MIXED is expected to be rare.

### 13.2 Coverage floor R [FROZEN]

- R is the macro recall of E over D\*.
- It is a non-inferiority component (§14), so precision-for-recall trades cannot buy the property.

### 13.3 Primary H2B property: evidence-verified claim precision (EVCP) [FROZEN]

**Operational question:** can a reviewer verify an asserted observation from the evidence the arm cites?

**Claims:** every (unit, d ∈ D\*) that the arm marks E.

**Verified claim.** All four conditions hold:

1. the gold status is E;
2. there is ≥ 1 valid cited support span;
3. **precision:** the token precision of the union of cited support spans, against the union of gold support spans for (unit, d), is **≥ 0.5**;
4. **coverage:** for at least one gold support span g, the cited tokens cover **≥ 0.5** of g's tokens.

**Tokens:** the regex `[A-Za-z0-9]+(?:'[A-Za-z]+)?` over the unit text. A token counts as cited, or as gold, when its interval overlaps the corresponding span.

**EVCP** = verified ÷ claims, micro-averaged over claims. With zero claims, EVCP is undefined and the property fails.

**Why these conditions:**

- **Precision** blocks whole-text and shotgun citation.
- **Coverage** blocks tiny "technically in-gold" citations, such as a single token of a multi-token gold span. A one-token gold span is still verified by citing that token.
- Together they follow ERASER's 0.5 partial-match convention (DeYoung et al., 2020; §26), applied per gold span.

**Why this property rather than the other candidates:**

- It is the only candidate measurable **identically across every arm**. Failure localization and semantic intervention exist only for T's staged pipeline.
- It is an operational verification test, not "more fields".

Worked cases: [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R1–R2.

### 13.4 Secondary / descriptive [FROZEN list]

- per-dimension P/R/F1;
- 5-status macro-F1;
- SUPPORTED-versus-MIXED recovery;
- exact unit-state match;
- `CONTRADICTED` F1;
- `INDETERMINATE` precision/recall;
- basis agreement on true positives;
- ERASER-style span token-F1 and IOU-0.5 match;
- EVCP, Q and S on BND, ADV, SHF and the high-agreement slice;
- Q and S by provenance (generated versus human-authored);
- ADV family metrics (§9);
- T's failure-localization profile (the share of errors attributed to a single stage);
- inter-dimension confusion;
- the ladder (T0/T1/T2 on locked data);
- locked-pool human agreement (§7.5);
- resources (§15).

None of these carries **confirmatory status**.

### 13.5 Uncertainty and calibration [FROZEN]

- **No arm is required to emit probabilities, and T0 emits none.** Its uncertainty is `INDETERMINATE` plus a reason code.
- If an arm emits `score` = P(E | unit, d), calibration is reported for that arm only:
  - ECE with 10 equal-mass bins, and Brier score;
  - risk–coverage curves and the area under the risk–coverage curve (AURC);
  - the referent is gold E on the locked main test.
- Otherwise, no calibration language is used.

### 13.6 Safety-routing floor [FROZEN]

**Metrics, on locked SR:**

- escalation recall on gold `EXPLICIT_SELF_HARM`;
- false-escalation rate on idiomatic `NONE`;
- `AMBIGUOUS_FINALITY` flag agreement.

**Floor:** escalation recall ≥ 0.95 is the routing-adequacy floor. It is *not* part of H2B.

**Consequence of falling below it:** the arm is reported as routing-deficient in the result headline and may not be proposed for any composition. This is not a measure of suicide-risk detection validity (§23).

## 14. H2B decision rule

### 14.1 Components (intersection–union test) [FROZEN]

- **G** = {C_A, C_B} (general-model controls); **K** = G ∪ {B0} (competent controls).
- **CI(x)** is the two-sided 95 % paired cluster-bootstrap interval of the difference T − control.

| Component | PASS | FAIL | Otherwise |
| --- | --- | --- | --- |
| **Q-NI**, each k ∈ K | lower CI(Q_T − Q_k) > −δ_Q | upper CI < −δ_Q | UNDECIDED |
| **S-NI**, each k ∈ K (removed if G5 failed) | lower CI(S_T − S_k) > −δ_S | upper CI < −δ_S | UNDECIDED |
| **R-NI**, each k ∈ K | lower CI(R_T − R_k) > −δ_Q | upper CI < −δ_Q | UNDECIDED |
| **P-SUP**, each g ∈ G | lower CI(EVCP_T − EVCP_g) **> δ_P** | upper CI < δ_P | UNDECIDED |

- P-SUP is **superiority by margin δ_P**, repaired from v1.0 (§27, R2). The data must establish an improvement greater than 0.10 at one-sided 0.025.
- H2B is decided by the intersection–union test (Berger, 1982). Each component is one-sided at 0.025, so no multiplicity adjustment is needed within H2B.

Worked classifications: [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R4.

### 14.2 Margins

**δ_Q [FROZEN formula; BIND value]:** `δ_Q = clamp((1 − F1_h) / 2, 0.02, 0.05)`.

- F1_h is the annotator-pair macro-F1 on E over D\*, computed on the reliability set RS (non-locked, §7.5) before any arm is run.

**δ_S [FROZEN formula; BIND value]:** `δ_S = clamp((1 − S_h) / 2, 0.02, 0.05)`.

- S_h is the annotator-pair S (§13.1) on RS. It is symmetric, because per-class F1 is symmetric between two raters.

Both values are recorded to three decimals.

**Rationale for both formulas:**

- 0.05 is the practical cap for a "competitive" quality loss.
- A competitive T may never lose more than half of what separates two careful annotators.
- Below 0.02, a difference cannot be resolved at the minimum sample size (§6.4).

**δ_P = 0.10 [FROZEN], a superiority margin:**

- "Material" means that at least one more asserted observation in ten becomes verifiable from its cited evidence.
- P-SUP requires the confidence interval, not merely the point estimate, to exceed 0.10.
- G2 caps human cross-verification disagreement at 0.20 (EVCP_h ≥ 0.80). δ_P is therefore at least half the maximum tolerated human evidence disagreement.

**EVCP_h:** each annotator's E claims and spans are verified against the other annotator's labels and spans under the full §13.3 rule. This is done in both directions and pooled on RS.

### 14.3 CI method [FROZEN]

- Resample locked-main-test **clusters** with replacement.
- B = 10,000 replicates, seed 20260918, with identical resamples for every arm (paired).
- Percentile interval.
- **Undefined values in a replicate:**
  - EVCP → placed on the failure side;
  - F1_d or F1_c → omitted from that replicate's macro-average.

### 14.4 Multiplicity [FROZEN]

- There is one confirmatory hypothesis: H2B, decided by the intersection–union test.
- Everything else is descriptive, with unadjusted 95 % CIs and no "supported" language. That includes S-H2A, the ladder, ADV, SHF, calibration and resources.

### 14.5 Outcome classes [FROZEN]

| Class | Condition |
| --- | --- |
| `supported` | every active component PASS; gates G1–G4 passed (G5 as recorded); no integrity defect |
| `not_supported` | any component FAIL, under valid conditions |
| `inconclusive` | no FAIL, and ≥ 1 UNDECIDED |
| `invalidated` | integrity defect: test leakage, a quarantine-register leak, an evaluator defect affecting primary metrics, a post-U1 artifact change, gold corruption, an M0/salt violation, or another protocol violation |
| `halted` | a stop condition (§20) fired before final evaluation; no test scoring |

If G5 failed, every result statement uses the narrowed H2B wording (§1).

## 15. Resource accounting and budgets

**Hardware:** Mac mini M4 with 16 GB unified memory, running macOS. All arms except F1 run locally. Hardware, OS and runtime versions are recorded.

### 15.1 Caps [FROZEN]

**Memory and storage:**

- Peak memory ≤ 13 GiB per process, measured as process max RSS **and**, where applicable, the MLX/Metal peak. Exceeding it triggers a resource stop for that configuration.
- Model artifacts ≤ 40 GB in total.

**Training wall-clock:**

| Arm | Cap |
| --- | --- |
| B0 | ≤ 2 h |
| T (all rungs) | ≤ 6 h |
| C_B | ≤ 24 h |
| S-H2A | ≤ 24 h |

**Inference:**

- Locked-pool inference: ≤ 24 h per arm.
- Sequential. Generative arms use batch size 1; other arms declare theirs. Concurrency is recorded.

**Retries and failures:**

- Zero retries. A format failure is `ERROR`.
- At most one logged infrastructure restart per run, resuming at the failed unit. The failed attempt is preserved.

**External cost:** none, except F1 ≤ USD 150.

### 15.2 Recorded per arm [FROZEN]

**Identity:**

- model, adapter and normalizer revisions and hashes;
- trainable and total parameters;
- artifact bytes;
- precision/quantization.

**Per-unit use:**

- calls/passes per unit: C_A 1 generation; C_B 1 forward pass; B0 and T 0 model calls;
- tokens with tokenizer revision (C_A prompt and output; C_B input); B0 and T report characters and clauses;
- context allocation (C_A rubric + few-shot tokens);
- preprocessing time and training time;
- per-unit inference time (median, p95) and total.

**Environment:**

- hardware;
- peak memory;
- storage;
- retries and restarts;
- tool/retrieval calls (must be 0);
- concurrency;
- API cost.

**Development effort:**

- dev-mini and full-dev evaluation counts;
- configuration revisions;
- logged session hours.

**Failures** are recorded throughout.

**Missing values** are recorded as `not applicable`, `not measured` or `unavailable`, with a reason. **Unknown ≠ zero; unmeasured ≠ free.**

### 15.3 Energy (Addendum C requirement 2) [FROZEN]

- **Energy is not measured.** No validated measurement method exists for this experiment.
- **No energy or energy-efficiency claims may be made.**
- Efficiency statements are limited to measured time, memory, storage, calls and tokens, within stated boundaries.

## 16. Fairness between arms [FROZEN]

| Aspect | Rule / disclosed difference |
| --- | --- |
| Task, labels, gold | identical |
| Inference evidence | unit text only, for all arms |
| Development material | train + dev + dev-visible special sets, for all arms |
| Fitting data | **Main-pool train only**, for every learned parameter in every arm. Dev and dev-visible special sets are for capped evaluation, selection and human error inspection. Quarantine-register units are never training data, few-shot examples or artifact sources (§8.4). |
| Context | C_A receives the rubric and few-shots in its prompt; the other arms embed the same rubric through development. Disclosed: this is the nature of a prompted control. |
| Preprocessing | the shared segmenter is available to all arms; C_B and C_A use their own tokenizers |
| Tools / retrieval | none, for any arm |
| Passes / sampling | one pass, greedy, no self-consistency, no ensembles |
| Human intervention | none at inference |
| Development budget | Identical caps (§11); session hours disclosed. If T's logged hours exceed 2× the median control's, the H2B headline must say so. |
| Compute | Differs by nature; reported, not equalized. No efficiency claim without the §15 accounting. |

## 17. Reality Audit applicability [FROZEN]

| Record portion | E001 |
| --- | --- |
| Identity and lineage | **applicable** |
| Decision-time snapshot | **applicable**: input hash, supplied evidence (unit text), arm version |
| Expected consequences | **not applicable**: no forecast |
| Decision / authority, execution | **not applicable**: no action, no authority |
| Later observations, correspondence | **not applicable**: the gold comparison is *evaluation*, not outcome correspondence |

Consequential fields are deferred to later composition and outcome experiments. E001 demonstrates no Reality Audit or outcome learning.

## 18. Independent reference checks (E1) [FROZEN]

**[`REFERENCE_CASES.md`](REFERENCE_CASES.md)** holds hand-derived expected values for:

- tokenization, span precision and span coverage;
- EVCP;
- F1, Q, R and S with withheld units;
- IUT classification;
- M0-based salt derivation and split hashing;
- δ_Q and δ_S;
- the T aggregation table;
- escalation triggers;
- evaluator robustness to malformed or adversarial predictions.

**Independence rules:**

- The implementation's scorer, splitter, mapping code and T aggregation must reproduce every case **without importing or calling code that produced the reference**.
- The quote-to-offset mapping cases, and each arm's native-to-record mapping cases, must be written independently of the implementation, by someone other than that arm's author.
- Human labels are validated through the rubric, blinding and gates G1–G3 and G5 (§7). A deterministic table is never treated as ground truth for them.

## 19. Leakage and test integrity [FROZEN]

**Prohibited:**

- locked units in any training, tuning, few-shot, cue-list or prompt artifact;
- locked labels, counts or scores informing D\*, the margins, the gates, architecture, rung designation, hyperparameters, prompts or thresholds. The only permitted use of locked counts is G4 reserve activation (§8.2);
- quarantine-register units as training data or artifact sources (§8.4);
- prompt iteration on locked cases;
- deleting or omitting any run (every dev and test run goes in the run ledger with hashes);
- best-seed selection on test (§10.3 median-dev rule);
- template or label-name leakage (§8.4);
- ADCP threshold leakage (§3);
- post-M0 additions other than reserve activation, and any re-salting (§8.1–§8.2).

**Human error analysis of locked outputs:** happens only after U2, with arm identities replaced by random codes.

**Timeline:**

- the salt is publicly derivable from the M0 commitment plus drand round R\*;
- test texts become visible at U1;
- test labels, locked-pool agreement and the locked M0 mapping become visible at U2.

## 20. Stop conditions (each preserved as evidence, not failure theater) [FROZEN]

| # | Trigger | Phase | Result |
| --- | --- | --- | --- |
| S1 | > 2 dimensions fail G1 on RS (ontology not labelable) | data | halted |
| S2 | G2 fails on RS (span evidence unstable) | data | halted |
| S3 | Privacy or provenance cannot be established; a writer or annotator agreement is missing | data | halted |
| S4 | G4 unmet after the reserve is exhausted (§8.2) | data | halted |
| S5 | Contamination or a quarantine-register leak cannot be bounded (§8.4) | data / P3 / U1 | halted / invalidated |
| S6 | A competent control cannot be constructed within caps (§11) | development | halted |
| S7 | A required arm cannot fit the resource caps, fallbacks included | development | halted |
| S8 | T needs complexity beyond T2 or outside the ladder | development | stop escalation; evaluate T2; redesign = new protocol |
| S9 | The evidence contract cannot support EVCP, Q or S (for example, spans are unrepresentable) | any | halted |
| S10 | The protocol can no longer separate H2B from prompting or adaptation (for example, C_A or C_B is dropped) | any | halted |
| S11 | An evaluator defect is found (E1 case failure or scoring bug) | any | fix before U1; found after U2 → invalidated, with the defect reported |
| S12 | The operator or auditor withdraws authorization, or a license or terms change blocks a required arm | any | halted |
| S13 | An M0 or salt violation: a second M0, a post-M0 addition outside reserve activation, or a salt not derived per §8.2 | data / any | halted (if found before U1) / invalidated |

A G5 failure is **not** a stop condition. It narrows H2B before implementation (§1, §7.5).

## 21. Execution sequence (after audit acceptance and separate operator authorization)

| Phase | Content | Exit gate |
| --- | --- | --- |
| P0 bind | Resolve the [BIND] items (§24). Activate or decline F1 / S-H2A. | recorded binding note |
| P1 data | See the numbered steps below the table. | train/dev released |
| P2 development | Preflights; B0, C_A, C_B (and S-H2A) within caps; T0; escalation decisions; final T designated | all artifacts hash-committed |
| P3 pre-unlock | E1 cases pass; competence gates; quarantine-register and contamination scans; independent pre-unlock check of the freeze by the auditor | go / no-go |
| U1 | Custodian releases locked inputs; frozen artifacts run; raw outputs and hashes committed; leakage scan | outputs committed |
| U2 | Gold, locked agreement and the locked M0 mapping released; frozen scorer; bootstrap; outcome class (mechanical) | result record |
| P4 | Evidence packet; interpretation via the §22 matrix; independent result audit | audit disposition |

**P1 steps, in order:**

1. Scenario cards → generation and human review → authored sets.
2. Explicit-self-harm screening, and the label-leak scan with the quarantine register.
3. Deduplication and cluster merging.
4. **M0 freeze and commitment.**
5. drand round R\* → salt → split.
6. Blind annotation → §7.6 quarantine → adjudication.
7. **RS gates G1, G2 and G5, plus G3. Record δ_Q, δ_S and D\*.**
8. G4 on locked data (custodian-only), with reserve activation if needed.
9. Data freeze v1.0 (hashes).

## 22. Interpretation matrix (written before any result) [FROZEN]

| Observed pattern | H2B | Empathy-observation boundary | Construction doctrine | More complexity? |
| --- | --- | --- | --- | --- |
| T non-inferior on Q, S and R, **and** EVCP improves by > δ_P (CI) | supported | usable as a bounded, verifiable boundary on this corpus | supported, for this responsibility only | only if the ladder already required it |
| T passes Q/R and EVCP but fails S-NI | not_supported | evidenced concerns are recovered, but state discipline (counter-evidence and uncertainty) is worse | purpose-built construction did not deliver state discipline here | ladder change only in a new protocol |
| T improves quality but not EVCP | not_supported / inconclusive | observable; no grounding advantage shown | the construction advantage is quality only; no H2B | no property case |
| EVCP improvement positive but CI not above δ_P | inconclusive (not_supported if upper CI < δ_P) | a grounding advantage may exist but is not established as material | no H2B claim | no |
| T improves EVCP but misses a quality margin | not_supported / inconclusive | grounding comes at a quality cost | narrow: verifiability traded for quality | the ladder may continue *only* in a new protocol |
| C_B beats T | not_supported | observable by adaptation | falsifier 2 pressure: adaptation suffices here | no new target rung justified by this protocol |
| C_A matches T | P-SUP decides; if EVCP is not better by the margin → not_supported / inconclusive | observable by prompting | falsifier 1 pressure: prompting suffices | no |
| B0 matches or beats T | matching: Q/S/R-NI vs B0 can pass, and P-SUP vs G decides; beating T beyond the margin: NI FAIL → not_supported | a generic transparent method suffices | purpose-built construction adds nothing beyond transparency here | **no** learned target justified |
| All systems poor (low Q and S for all) | not_supported / inconclusive | the boundary may be ill-posed for text alone | none | redesign the ontology, not the architecture |
| Labels or ontology unreliable (G1/G2 on RS) | halted | not a stable boundary as defined | no evidence either way | no |
| G5 failed (the state is not reliably labelable) | H2B narrowed before implementation; decided on Q, R and EVCP | evidenced-concern detection may be a boundary; the full state is not | no state-discipline claim | no |
| A selective system "wins" only by abstaining | blocked by the R-NI, Q and S definitions → not_supported | — | — | no |
| A resource advantage vanishes under full accounting | unaffected (not an H2B property) | — | no efficiency claim | no |
| T0 is final (no escalation) and H2B is supported | supported | — | **a transparent purpose-built system suffices; no learned MASI target justified** | no |
| T fails the SR routing floor | H2B class unchanged; the headline flags the routing deficiency | not composition-eligible | — | a routing fix needs a new protocol |

## 23. Explicit nonclaims [FROZEN]

**E001 establishes none of the following:**

- clinical validity, diagnosis, or risk assessment (including suicide-risk detection validity);
- certainty about anyone's mental state;
- complete Empathy;
- human equivalence;
- general MASI efficacy;
- composition or governance benefit;
- H7;
- outcome-grounded Wisdom;
- Reality Audit capability;
- calibration (unless measured per §13.5);
- energy efficiency;
- universality of the ontology beyond English synthetic/authored text;
- superiority of purpose-built systems beyond this responsibility;
- anything about real conversations or real users;
- authorization for ADCP semantic inference or intervention;
- if G5 failed, any claim about observation-state discipline.

A supported H2B supports only the bounded claim, on this corpus and task.

## 24. Freeze register and blocking items

**[FROZEN]:**

- §1–§5;
- §6.1–§6.2, and the §6.4 targets and minimums;
- the rules in §7.2–§7.6;
- §8 and §9;
- the recipes and candidate lists in §10.1–§10.3;
- §11–§20;
- §22–§23.

**[DEV]:**

- the B0 candidate;
- the C_A model and prompt;
- C_B hyperparameters and the median seed;
- T's cue lists, rules and rung development;
- the rung designation, by the §12.3 rule only.

**[LOCKED]:**

- the locked pools (main test, 60 % of BND/ADV/SR, all of SHF) and their gold;
- the locked mapping of M0;
- locked-pool agreement;
- all locked-set metrics.

**Unresolved blocking items.** These must be bound before implementation starts; none can be settled by reasoning alone.

| # | Item | Owner |
| --- | --- | --- |
| B1 | Designate a custodian independent of the implementer and the T designer. | operator |
| B2 | Recruit and contract writers, annotators and an adjudicator, with consent, license assignment, compensation and content-support provisions, and approve the budget. See the details below the table. | operator |
| B3 | Reverify the generator pin and Ai2 terms at P0; confirm frontier generation is not used. | custodian |
| B4 | Decide whether to activate F1 (with a written terms check) and S-H2A. | operator |
| B5 | Assign an independent auditor for P3 and P4. | operator |

**B2 in detail:**

- **People:** ≥ 3 writers plus ≥ 2 separate SHF writers; ≥ 3 annotators; 1 adjudicator.
- **Budget:**
  - about 130 h of annotation and adjudication;
  - about 60 h of writing and review;
  - the reserve (§8.1) adds about 20 % if activated.

**Resolved mechanically during P1, from RS only (not judgment calls):**

- δ_Q and δ_S (§14.2);
- D\* (G1);
- the G5 outcome.

**Run as the first step of P2, with fixed fallbacks:** the model runtime preflights (§10.2, §10.3).

**Non-blocking future questions:**

- a corpus release license (CC BY 4.0 suggested), needed before publication;
- ERASER faithfulness metrics (comprehensiveness/sufficiency) as a future property;
- concept-level intervention tests on T;
- real-conversation validity under consent;
- non-English units;
- a MASI Bus mapping of the observation record;
- whether ADCP should adopt the refined ontology (ADCP's decision).

## 25. Author-side supporting review (not an independent audit)

### v1.0 review

The protocol author challenged the draft on the fifteen required questions. Defects found and fixed are marked **fixed**.

1. **Is any label downstream policy in disguise?** Stage, severity and burden were removed. `finality_language` was demoted to a language flag with no literal/figurative resolution. `support_unavailable` records reported availability, not a need to reconnect. **Fixed:** an early draft used a 0–3 severity.
2. **Was the architecture chosen before the responsibility?** No. §2 was written first. T0's stages mirror the rubric's evidence rules; ConText was found afterwards as prior art for the same decomposition.
3. **Is B0 a strawman?** No: identical caps, the dev-selected best of two established methods, and an R0 sanity floor. Learned complexity can be justified only by T0. **Fixed:** B0 originally received more dev runs than the other arms; the caps are now uniform.
4. **Is C_B silently promoted?** No. C_B is a control, T3 is barred, and T2's frozen embedding is disclosed.
5. **Could extra compute or context explain a result?** One pass each. C_A's prompt context is disclosed, and no efficiency claim is allowed without accounting.
6. **Can abstention game the score?** No. Abstention on gold-E counts as a false negative in Q, R-NI adds a recall floor, and EVCP is conjoined with both.
7. **Are the labels circular?** Humans label blind to ADCP, the arms and the generator's intent, and T designers never annotate. **Residual:** the rubric's evidence semantics (support / counter / unresolved) are shared by T's aggregation because they *are* the responsibility, and every arm gets the rubric. This is disclosed.
8. **Can the test set influence the architecture?** No. Escalation and designation use dev only and are committed before U1, and custody is two-phase.
9. **Is the property operational?** Yes. EVCP is deterministic, identical across arms, and has worked cases.
10. **Are the margins justified?** δ_Q is derived from human disagreement with explicit bounds, and δ_P is tied to G2. **Fixed:** a fixed δ_Q of 0.05 was replaced by the human-derived formula.
11. **Is escalation triggered only by allowed evidence?** Yes: dev only, measured once per rung, under the §12.3 rule.
12. **Is any missing value represented as zero?** No (§15.2).
13. **Are publication and license constraints explicit?** Yes: §6.3, §10, §15, and ADCP's missing license (§3).
14. **Are negative outcomes preserved?** Yes (§20, §22). T2 is evaluated even when the dev outlook is negative.
15. **Could the protocol conclude that a learned target is unnecessary?** Yes, explicitly: a final T0, or B0 matching T (§22).

**v1.0 second-pass fixes:**

- the escalation threshold now includes B0;
- C_B early stopping no longer uses dev;
- dev-mini is chosen by a deterministic rule;
- an explicit-self-harm scoring rule was added (superseded in v1.1; see §27, R7);
- unresolved counter cues were added to U.

### v1.1 author-side re-review (not an independent audit)

After applying R1–R7, the author re-checked each repair for new inconsistencies:

- **RS versus G4.** RS now feeds the gates, margins and D\*. G4 still reads locked counts, but its only possible action is reserve activation or halt, and D\* is frozen before G4 runs.
- **Reserve and RS.** Reserve clusters are excluded from RS, so activation cannot loop back into the gates.
- **Salt.** The drand salt cannot be shopped, because M0 is committed publicly before the beacon round exists.
- **S and withholding.** Withheld predictions map to `NONE_OUTPUT`, not NA, so withholding earns no S credit (`REFERENCE_CASES.md` §R3b shows the difference as a denominator trap).
- **G4 coverage.** G4 now covers CON and IND.
- **R2 margin.** The audit's own example (0.10 [0.01, 0.19]) is now UNDECIDED (§R4, case J).

**Residual risks, accepted and disclosed:**

- synthetic and authored text limits external validity;
- a single corpus, in English only;
- the generator's style may favor lexical methods (the SHF and provenance slices expose this);
- annotation cost may force S4;
- the stricter P-SUP margin and the added S-NI make `supported` harder to reach, and `inconclusive` is a legitimate outcome.

## 26. Prior-art record (focused)

| Source | Category | Use in E001 |
| --- | --- | --- |
| ConText (Harkema, Dowling, Thornblade & Chapman, *J Biomed Inform* 42:839–851, 2009); NegEx lineage | known primitive | T's qualifier layer (negation, experiencer, time, hypothetical), with non-clinical triggers written for E001 |
| medspaCy `context` (MIT) | reusable implementation | optional engine for T0/T1 qualifier rules; triggers are E001-specific |
| ERASER (DeYoung et al., ACL 2020) | known primitive / metric | token-level rationale metrics and the IOU-0.5 partial-match convention (EVCP precision and coverage thresholds; secondary span metrics); faithfulness metrics deferred |
| Concept Bottleneck Models (Koh et al., ICML 2020) | known primitive | typed intermediate state; intervention tests deferred |
| Selective classification (Geifman & El-Yaniv, NeurIPS 2017) | known primitive | risk jointly with coverage; the R-NI floor |
| Intersection–union tests (Berger, *Technometrics* 24:295–300, 1982) | known method | conjunctive H2B decision without adjustment |
| Krippendorff's α conventions (≥ 0.800 rely; 0.667 tentative floor) | known method | gates G1 and G5 |
| Learning from disagreement (Uma et al., *JAIR* 72, 2021) | known method | raw-annotation preservation; high-agreement slice |
| drand / League of Entropy public randomness beacon (default chain `8990e7a9…51b2ce`) | reusable implementation | a salt no party can choose (§8.2) |
| NB-SVM (Wang & Manning, ACL 2012); scikit-learn | useful control | B0 candidates |
| DeBERTa-v3 (He et al.); `microsoft/deberta-v3-base` | useful control | C_B base |
| EPITOME empathy-with-rationales (Sharma et al., EMNLP 2020) | unsuitable precedent (responder empathy, real peer-support data) | supports a multi-task label + span design for C_B only |
| CLPsych 2024 evidence highlighting for suicidality (Chim et al., CLPsych 2024) | unsuitable precedent (real sensitive data, risk-level framing) | a reason to keep safety as routing only, never risk levels |
| Ethical tensions in inferring mental-health states (Chancellor et al., FAT* 2019) | constraint source | synthetic/authored data, nonclaims, no latent-state inference |
| Empathy constructs in NLP are ill-defined (Lahnala et al., Findings of EMNLP 2022) | constraint source | a narrow operational ontology tested by agreement gates |
| WILDS (Koh et al., ICML 2021) | known method | grouped splits and a shift set |
| Snorkel / weak supervision (Ratner et al., 2017) | not adopted | weak labels would import rule circularity; the reference is human labels |
| GoEmotions (Demszky et al., 2020) | not adopted | emotion categories are not burden observations |
| ADCP @ `eb7ac37` | ontology substrate | §3 |

**Genuine E001 gap.** Prior art supplies the parts; it does not settle this comparison. The question is whether a responsibility-first observer built from typed evidence qualifiers can be both:

- non-inferior, in evidenced-concern and observation-state quality, to prompted and adapted general-model controls; and
- materially more verifiable,

under one conjunctive, preregistered decision.

## 27. Revision record — v1.0 → v1.1 (independent audit `REPAIR_REQUIRED`)

**Source:** the audit is [PR #17 comment 5735626914](https://github.com/JosephJMWalker-MBA/masi-research/pull/17#issuecomment-5735626914), against v1.0 head `d1d9bfc`. The audit comment and the v1.0 text are preserved unchanged.

**Scope of change:** the research question is unchanged. H2B was made stricter (R2, R5), with a preregistered narrowing path (G5).

| Finding | Defect (summary) | Repair in v1.1 | Where |
| --- | --- | --- | --- |
| **R1** (blocking) | G1/D\* used all double-annotated units, including locked pools, so locked labels could shape the primary task before U2. | Gates, margins and D\* are computed on the **reliability set RS** only (non-locked dev + train QC). Locked-pool agreement is sealed until U2 and descriptive only. G4 locked counts can only trigger reserve activation or halt. | §7.5, §6.4, §19, §24 |
| **R2** (blocking) | P-SUP passed on lower CI > 0 with point ≥ 0.10, which is not superiority by 0.10. | P-SUP PASS requires **lower CI > δ_P = 0.10**; the claim now says "superiority margin". Reference case J reproduces the audit's example. | §1, §14.1, §14.2, §R4 |
| **R3** (blocking) | The global label-leak rewrite would destroy the A13 injection cases. | An **integrity quarantine register**: A13 and registered ADV units are exempt from rewriting, confined to ADV, never used as training, few-shot or artifact sources, with an 8-token artifact scan at P3 and U1. | §8.4, §9, §10.2, §16, §19, S5 |
| **R4** (blocking) | Cluster IDs were not frozen before the salt, and additions under a known salt allowed bucket shopping. | The **cluster manifest M0** (IDs + member text hashes + a pre-ranked **reserve**) is committed on Issue #3 **before** the salt exists. The salt derives from the **drand** round ≥ commitment + 24 h. Reserve activation only, in rank order, in complete batches, into hashed buckets. Append-only log. New stop condition S13. | §8.1, §8.2, §6.4, §19, §20, §R5 |
| **R5** (blocking unless narrowed) | Primary Q collapsed the state to E versus non-E, so CON/IND/NA confusions had no consequence. | A new confirmatory **S-NI** on the four-class state S (withheld = `NONE_OUTPUT`), with δ_S from human agreement on RS, gate **G5**, and G4 CON/IND minimums. If G5 fails, H2B is **narrowed before implementation** (preregistered). The research question is unchanged. | §1, §4, §6.4, §7.5, §12.3, §13.1, §14, §22, §23, §R3b, §R4, §R6, §R8 |
| **R6** (repair) | "train-fold F1 ≥ dev F1" is not a valid competence invariant. | Replaced by training-integrity checks (no NaN/Inf, convergence, loss reduction), an **inner-validation fit floor ≥ R0**, and reproducibility. The inner-validation fold is defined deterministically. | §11, §10.3 |
| **R7** (clarify) | Explicit self-harm was both "SR-only" and "excluded from main after gold". | One rule: pre-M0 screening and generator review rejection, then **quarantine before data freeze** of any non-SR unit either annotator marks `EXPLICIT_SELF_HARM`. It is based on raw annotations, symmetric across splits, and never driven by gold after unlock. The v1.0 §13 exclusion is removed. | §6.1, §7.6, §13 |
| Non-blocking | EVCP's precision-only overlap let "tiny but in-gold" citations verify. | Added a **per-gold-span coverage ≥ 0.5** condition. One-token citations of multi-token gold spans no longer verify; one-token gold spans still can. | §13.3, §R2 (c14–c16) |

---

**Exact next action:** a **second fresh independent audit** of this repaired freeze (v1.1). No implementation, annotation, training, inference, unlock or merge happens until that audit is accepted **and** the operator separately authorizes execution. The protocol author does not accept this protocol.
