# MASI-E001 — Preregistered protocol v1.3

- **Protocol ID:** `e001-protocol-v1.3`
- **Status:** **repaired freeze submitted for final independent verification of A1 and A6. Not accepted. Not authorized for execution.** No data, labels, model runs or results exist for this protocol.
- **Revision:**
  - v1.0 was frozen at commit `d1d9bfc40c40e607f0a476bb620bb665c3b8830a`. Its [independent audit](https://github.com/JosephJMWalker-MBA/masi-research/pull/17#issuecomment-5735626914) returned `REPAIR_REQUIRED` (R1–R7).
  - v1.1 was frozen at commit `b13daa94a608ef075474f6ac35cdd59650478423`. It repaired R1–R7 and closed the non-blocking EVCP-citation observation (§27).
  - The independent GPT-5.6 Sol audit of v1.1, relayed by the operator on 2026-09-19, returned six blocking findings, A1–A6. v1.2 repaired them (§28).
  - v1.2 was frozen at commit `00783025e65ead1acc6da5b2183040fc576411ed`. Its independent re-audit returned `REPAIR_REQUIRED`: A2–A5 pass; A1 and A6 remain blocking. v1.3 repairs only A1 and A6 and their direct consequences (§29).
  - The v1.0, v1.1 and v1.2 texts (git history) and the v1.0 audit comment (on the PR) are preserved unchanged.
- **Issue:** [#3](https://github.com/JosephJMWalker-MBA/masi-research/issues/3), under the operator authorization on Issue #3 and PR #16.
- **Governing main:** `904bd9bc1c482c5b552b4a2e7075d685d73a1748`
- **Substrate inspected:** `JosephJMWalker-MBA/Accumulated-Distress-Care-Protocol @ eb7ac37f79511c90e25ff613ee78e9123d653d60` (refetched 2026-09-18)
- **Frozen WP1 packet:** `codex/wp0-wp1-candidate-probe @ 81adfff`. Untouched; nothing is imported from it.

**Companion files:**

- [`ANNOTATION_RUBRIC.md`](ANNOTATION_RUBRIC.md): the task definition shared by annotators and all arms. Rubric v1.1: in protocol v1.2, only rubric §6's `UNIT_DEFECT` sentence changed (units are removed, never repaired; §8.1). §1–§5, the text every arm receives, are unchanged.
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
first deficit that may justify complexity: T0's best dev Q (or S, if G5 passed) is short of the
                       competent-control threshold AND, for every short metric, correcting only its
                       "no candidate mention" errors would close the shortfall and would recover at
                       least as much as correcting all other errors (§12.3)
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
- **Out of bounds:** units outside these limits are `UNIT_DEFECT`. Before the cluster manifest M0 is frozen, the custodian repairs or excludes them. After M0, a `UNIT_DEFECT` unit is removed, never repaired (§8.1).
- **Identity:** a unit's identity is its unit ID **and** the SHA-256 of the UTF-8 bytes of its NFC canonical text, both committed in M0 (§8.1). The record field `input_sha256` (§5.3) must equal that committed hash.
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
| QC team | ≥ 3. Authors and key-labels the qualification/QC pool (§7.7). Excluded roles are listed in §7.7. |

Implementers, T designers and the protocol author do not annotate or adjudicate.

### 7.2 Blinding and order [FROZEN]

- **Annotators see only:** the unit text and rubric §1–§5.
- **Annotators never see:** split, set, provenance, card, cluster, other labels, model output, ADCP or stage material.
- **Order:** each annotator's queue is a random permutation mixing all pools, with about 5 % known-answer items from the QC pool (§7.7).

### 7.3 Coverage [FROZEN]

- **Double annotation plus adjudication:** dev, test, BND, ADV, SR and SHF.
- **Train:** single annotation, with a random 20 % double-annotated for QC. Train labels are declared lower-assurance.

### 7.4 Adjudication, disagreement preservation, versioning [FROZEN]

- Rubric §7 governs adjudication.
- Raw annotations are immutable and retained. Gold is a separate versioned record (`gold v1.0`).
- The high-agreement subset (both annotators agree on E status) is reported as a secondary slice.

**Corrections:**

Corrections apply to labels and spans only. Unit text is never corrected after M0 (§8.1).

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
| G3 annotator QC | known-answer accuracy against the frozen QC key (§7.7) | ≥ 90 %, per rubric §8 |
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

### 7.7 Qualification and QC pool: the reference key [FROZEN rules; BIND people]

**Purpose.** The QC pool supplies rubric §8's practice units, qualification test and in-queue known-answer items. Its key measures annotator competence (G3) and nothing else.

- It is **never** a source of gold, labels, features, prompts, examples, cue lists or metrics for any arm.
- It never enters M0, any split, RS, D\*, the margins or any H2B metric.

**Composition [FROZEN minimums]:** three disjoint sets.

- **Practice set:** 40 units.
- **Qualification set:** 30 units.
- **Known-answer set:** ≥ 80 units, and large enough that no annotator sees any known-answer item twice.

**Authorship:**

- QC units are **human-authored** by QC-team members, from QC briefs written for this pool only.
  - A QC brief is never an experimental scenario card.
  - No QC unit is written from, paraphrased from or modeled on an experimental unit.
- No model output is used: no generated text, and no model-suggested edits, labels or spans. §6.2 applies in full.
- QC units obey the unit bounds (§5.1) and contain no explicit self-harm language (§6.1).

**Key labeling:**

- Each QC unit is labeled by **two** QC-team members who did not write it.
  - They label independently, under rubric §1–§6.
  - They are blind to each other, to the author's brief, and to everything on the §7.2 blinding list.
- **Qualification and known-answer items** are admitted only where both key labelers independently agree on the status of all seven dimensions. The agreed statuses are the key.
  - The adjudicator reviews each agreed item against the rubric and may **drop** it, with a written reason that cites a rubric rule.
  - The adjudicator may never change a key value.
- **Practice items** may also include disagreements, resolved by the adjudicator under rubric §7. Practice items are discussed, never scored.
- Scoring uses statuses only (rubric §8). Key spans follow rubric §7 and are used only in practice discussion.

**Raw disagreement is preserved:**

- All raw key labels are retained immutable, including those of dropped and non-admitted items.
- The key is a separate, versioned record.
- The admission rate and per-dimension key-labeler agreement are reported, as descriptive results.

**Exclusions.** No QC-team member is:

- a T designer, an implementer or the protocol author;
- an experimental annotator (they would recognize known-answer items);
- the adjudicator or the custodian;
- an SHF writer (SHF writers write nothing else; §6.4).

QC-team members may also write main, BND, ADV or SR units. The §3 ADCP leakage rules apply to them, and they never see any model output.

**No overlap with any experimental pool:**

- After M0 is frozen, the custodian runs the §8.1 near-duplicate check (exact normalized duplicates, and character 5-gram Jaccard ≥ 0.6) between every QC unit and every M0 unit, across all pools, active and reserve. It is rerun against any restart M0's new units (§8.1).
- Any hit drops the QC unit. M0 is never changed for the QC pool.

**Freeze, version and hash:**

- The key file `qc-key v1.0` lists, per item: the set, the QC unit ID, the SHA-256 of the canonical text and the key statuses.
- It is frozen after the overlap check and **before any annotator sees any unit** (§21, P1 step 5).
- The custodian posts SHA-256(key file) on Issue #3. This is the **QC-key commitment**.
- The custodian holds the pool and key. They are released to the auditor at P3, and to no implementer or arm before U2.

**Correction procedure:**

- After the QC-key commitment, no key value and no QC unit text is ever edited.
- A defective item (a key that contradicts the rubric, or a unit defect) is **retired**.
  - The adjudicator decides, with a written reason that cites a rubric rule.
  - The retirement is logged with the reason, the reporter and the date.
  - Annotators failing an item is not, by itself, a reason to retire it.
- G3 and qualification results are recomputed without the retired items. The original and recomputed results are both logged, and the recomputed ones apply.
- New items enter only through a new key version (`qc-key v1.1`), built under this section in full, with its own commitment, before any of them is used.

**Ownership:** under B2 (§24), the operator recruits and contracts the QC team. The custodian runs the overlap check, holds and commits the key, and keeps the logs.

**Why the key cannot become a hidden circular ground truth:**

- Its authors and labelers are disjoint from T designers, implementers, the protocol author and experimental annotators.
- No model contributes to any QC unit or key value.
- The key never enters gold, RS, any metric or any arm.
- A key value exists only where two labelers agreed independently, so no single person's reading defines the annotators' benchmark.

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

- `canonical_text` is the §5.1 canonical text (NFC, turns joined by `\n`), and `sha256` is taken over its UTF-8 bytes.
- M0 therefore commits every cluster ID, every unit ID and every unit's canonical-text hash, for active and reserve clusters alike.

**Commitment.** The custodian posts `SHA-256(M0 bytes)` as a comment on Issue #3. This is the **M0 commitment**, and its server timestamp is authoritative.

- The first such comment is binding.
- A later, different M0 is a protocol violation (S13), except for the single pre-salt restart M0 permitted below.

**After M0: canonical text is immutable [FROZEN].**

- No unit's canonical text may change while it keeps its committed identity. There are no text repairs, amendments or re-encodings: the committed bytes are the unit.
- No cluster or unit may be added, except by reserve activation (§8.2). Reserve units are already in M0, so activation adds no new text.
- **Hash verification.** The custodian recomputes every unit's canonical-text hash and compares it with M0:
  - at data freeze, P3, U1 (before locked inputs are released) and U2;
  - the scorer also checks each record's `input_sha256` against M0. A mismatching record is scored as `ERROR` and logged. If the text the custodian delivered for that unit itself mismatches M0, that is S13.
- **Any post-M0 mismatch** between a unit's text and its M0 hash is an integrity violation (S13). NFC normalization does not excuse a mismatch; the comparison is byte-exact.

**Removal: the only remedy for a defective unit after M0 [FROZEN].** A unit may be removed only on one of these triggers:

| Code | Trigger | Decided from |
| --- | --- | --- |
| X1 | `UNIT_DEFECT`: outside the §5.1 bounds, not valid UTF-8 NFC, or not English | the text itself |
| X2 | explicit self-harm outside SR (§7.6) | raw annotation |
| X3 | privacy, consent or provenance defect, including a contributor's opt-out | the provenance record |
| X4 | a label-leak hit that the pre-M0 scan (§8.4) missed, on a unit not on the integrity quarantine register | the §8.4 scan, rerun |
| X5 | a cross-cluster near-duplicate that the pre-M0 merge missed: **both** units are removed | the §8.1 check, rerun |

- Every removal is prediction-blind. None uses adjudicated locked gold.
- A removed unit keeps its M0 line unchanged. It is excluded from every pool, RS and every metric. Its cluster keeps its ID and bucket.
- Removals happen before data freeze. After data freeze only X3 is permitted; it applies identically to every arm, and the count per split is reported.
- Removals may lower G4 counts. The only remedy is reserve activation (§8.2); otherwise S4. Removal never triggers a new draw.

**Replacement text: one restart, only before any salt can exist [FROZEN].** A defect whose remedy needs *different* canonical text cannot be fixed inside the committed experiment. The randomization is single-shot: once a split can be known, it is never redrawn.

**The restart window.** A restart is possible only while no salt from the committed M0 can exist.

- The restart notice's Issue #3 server timestamp must be **strictly earlier** than the release time of the original R\* (§8.2).
- The window therefore closes, irrevocably, when R\* is released. That is before any split, annotation, gate result or locked count exists, so nothing about the first assignment can inform the decision.

**Restart procedure:**

1. **Irrevocable notice.** The custodian posts on Issue #3 the reason, the affected unit IDs, the superseded M0 hash and the operator's written authorization. From that moment the original M0 is superseded permanently. Its salt is never derived or used, even after its round becomes public.
2. **Scope.** The restart M0 differs from the superseded M0 only in the units the notice lists. Each listed unit is removed, or replaced by a unit with a **new** unit ID. A unit ID never maps to two different hashes. All other units keep their IDs and bytes.
3. **New M0, then a new salt.** The restart M0 is committed on Issue #3, citing the notice. Its salt comes from a new round R\*, the first round released ≥ the restart M0 commitment + 24 h, under §8.2 in full.
4. **QC overlap.** The §7.7 overlap check is rerun against the new units. A hit retires the QC item.
5. **Disclosure.** The superseded M0, the notice and all logs are preserved. The restart is reported in the result headline.
6. **Limit.** At most one restart.

**After the salt round is released** (the original R\*, or the restart's R\*), there is **no in-protocol re-randomization**:

- A defect is handled by a permitted removal (X1–X5). If removal cannot handle it, the experiment is **halted** (S13).
- Different canonical text can enter only a **new protocol version with a genuinely new locked evaluation**: a new locked test set built from clusters not in this M0.

**Custodian log.** Every attempted addition, activation, removal, restart and hash verification is preserved in an append-only custodian log.

Worked cases: [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R5d.

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
- **Selection:** rule J (§11.1) with dev Q as the designation criterion. B0 is not a P-SUP comparator, so its EVCP plays no role, but its designation must be quality-competitive on Q, S and R jointly. If the two candidates trade off beyond the margins, both are designated B0 comparators.

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

**Selection:** model × prompt are screened on dev-mini, and finalists are evaluated on full dev. The designated configuration, or designated set, is chosen by **rule J** (§11.1) over all full-dev-evaluated configurations, never by a single metric alone.

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
- **Configurations and seeds.** Each (hyperparameters, seed) pair evaluated on full dev is one configuration.
  1. Hyperparameter candidates are trained with seed 1 and evaluated on full dev.
  2. Rule J (§11.1) picks the leading hyperparameters: those of its designation, or of its primary designation if it designates a set. Seeds 2 and 3 are then trained at those hyperparameters and evaluated on full dev.
  3. Rule J is applied again over **all** full-dev-evaluated configurations. Its result is the designated configuration (or set), and so the confirmatory seed or seeds.
  - All three seeds of the leading hyperparameters are reported on test, descriptively.

### 10.4 T — see §12

### 10.5 F1 (optional) [BIND: operator activation]

**Conditions:**

- the provider's terms permit publishing results, verified in writing before the run;
- the provider is not the generator family;
- the same final C_A prompt is used: that of C_A's primary designation (§11.1);
- spend ≤ USD 150.

**Role:** descriptive only; outside the H2B decision.

**If terms forbid publication:** F1 results are not published, or F1 is not run.

### 10.6 S-H2A (optional) [BIND: operator activation before implementation]

**Design:**

- LoRA/QLoRA (MLX-LM, MIT) of the base model of C_A's primary designation (§11.1), on main-pool train, with the identical prompt and output contract;
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
   - **B0, C_A, C_B and T** (T within its designated rung): the designation is made by rule J (§11.1). B0's criterion is dev Q; the others' is dev EVCP.
   - There is no test access.
5. **Sanity gates.** These replace v1.0's invalid "train-fold F1 ≥ dev F1" (§27, R6) and v1.1's loss-reduction ratio (§28, A2). A failure indicates a broken implementation, not ordinary variance.
   - **(a) All arms, format:** ≥ 98 % of dev outputs are valid records.
   - **(b) All arms, competence floor:** dev Q ≥ the dev Q of **R0**, the naive reference ([`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R10). R0 marks a unit-dimension SUPPORTED iff any quoted support example from rubric §4 occurs as a case-insensitive substring, and NOT_ADDRESSED otherwise, with no qualifiers.
   - **(c) Learned arms and rungs (B0, C_B, T1, T2, S-H2A), training integrity:**
     - **finite values:** no NaN or Inf in any loss, gradient or parameter, at any step or at the end. Any non-finite value is numerical divergence;
     - **completion:** convex solvers report convergence within their declared iteration limit. Gradient training runs its declared schedule to completion, or stops under the declared inner-validation early-stopping rule, without a crash;
     - **diagnostic only:** the per-epoch mean training loss and inner-validation loss are recorded and reported. **No loss-reduction ratio is a pass/fail condition**, and loss values never trigger a halt or a fallback.
   - **(d) Learned arms and rungs, fit floor:** inner-validation-fold Q ≥ R0's Q on the same fold.
   - **(e) All arms, reproducibility:** a re-run of the frozen pipeline reproduces the dev-mini predictions.
     - Deterministic arms (B0, T0, T1, and C_A with greedy decoding): identically.
     - MPS-trained C_B and T2 heads: ≥ 99 % identical per-pair statuses, with scores within 1e-6 when emitted.
6. **Reproducibility provenance:** pinned revisions, environment lock and seeds are recorded.
7. **If a control fails a gate:**
   - **B0:** the other B0 candidate replaces it. If both fail, the implementation defect must be fixed within the remaining caps; otherwise **halt**.
   - **C_A / C_B:** the fallback model is used.
   - A control may never be left weak. A failed competence gate that cannot be fixed means **halt**, not "T wins".

**Learned complexity is justified only from T's own ladder** (§12.3), whose first rung (T0) is a full-budget, transparent, purpose-built system. The escalation threshold is the *maximum* over the designated control configurations (§11.1), so a weak B0 can never lower the bar or manufacture a deficit; only a strong control can raise it.

### 11.1 Dev selection rule J for the conjunctive H2B [FROZEN]

H2B requires T to be quality non-inferior on Q, S **and** R, **and** EVCP-superior. A control chosen on one metric alone could therefore be weak on another quality metric or on EVCP, while a stronger, equally competitive configuration was discarded. Rule J closes both paths: every quality metric gets its own anchor, and among configurations competitive on all of them the best-grounded is chosen.

**Applies to:**

- the competent controls B0, C_A and C_B;
- T's configurations within its designated rung;
- S-H2A.

**Inputs.** Φ_a is every configuration of arm a that was evaluated on full dev within the §11 caps and passes sanity gates (a)–(d).

- Each C_B (hyperparameters, seed) pair is one configuration. B0's configurations are its two candidates (§10.1).
- The checked quality metrics are Q, R and, if G5 passed, S.
- All values are full-dev values, computed in exact rational arithmetic.

**Designation criterion c_a:**

- **dev EVCP** for C_A, C_B, T and S-H2A. A configuration with zero dev E claims has undefined EVCP and ranks below every defined value.
- **dev Q** for B0, which is not a P-SUP comparator.
- **Tie-break:** higher Q, then higher S (if G5 passed), then higher R, then earliest in the run ledger.

**Steps:**

1. **Independent per-metric anchors.** Q^max(a), R^max(a) and, if G5 passed, S^max(a) are the maxima over Φ_a. Each metric has its own anchor; they may come from different configurations.
2. **Joint quality envelope.** E_a is every φ ∈ Φ_a with all of:
   - Q(φ) ≥ Q^max(a) − δ_Q;
   - R(φ) ≥ R^max(a) − δ_Q;
   - if G5 passed, S(φ) ≥ S^max(a) − δ_S.
3. **Designation when E_a is non-empty.** The single designated configuration φ\*(a) is the configuration in E_a that ranks highest on c_a.
4. **Designation when E_a is empty** (the arm has a genuine quality tradeoff larger than the margins). For each checked metric M, E_M(a) is every φ with M(φ) ≥ M^max(a) − δ_M, and φ\*_M(a) is its highest-ranked configuration on c_a.
   - **Controls (B0, C_A, C_B):** the designated **set** D_a is {φ\*_M(a)} over the checked metrics, with duplicates merged. It has at most three members.
     - Every member is a comparator in K, and, for C_A and C_B, in G.
     - Every member faces every H2B component (§14.1).
   - **T and S-H2A:** the single designation is φ\*_Q(a). Their choice can only affect themselves; no comparator needs protecting.
5. **Primary designation.** The single designation, or φ\*_Q(a) of a set.
   - It runs the descriptive locked pools. C_A's primary also supplies S-H2A's base model (§10.6) and F1's prompt (§10.5).
   - Every other member of a set runs on the locked main test only.
   - All of an arm's locked runs share its §15.1 locked-inference cap. If they cannot fit, S7 applies.
6. **Competence.** If a designated configuration then fails gate (e), it is removed from Φ_a and J is re-applied from step 1. If Φ_a becomes empty, §11 item 7 applies: the fallback model, or **halt**.

**Record.** Φ_a, the per-metric anchors, E_a (and each E_M where used), the designation or designated set, and every configuration's dev Q, S, R and EVCP are recorded and hash-committed with the arm's artifacts before U1.

**Escalation thresholds (§12.3)** use the dev values of all designated control configurations, the members of K.

**Why this is sufficient:**

- **No metric is anchored to another.** A configuration strong on S or R cannot disappear because another had slightly higher Q. A designated control is within the NI margin of the family's best on every checked metric. When no single configuration achieves that, a configuration competitive on each metric is itself a comparator (§R13b, §R13d).
- **The property cannot be manufactured.** Among quality-competitive configurations, the best-grounded is designated, so P-SUP cannot be won by discarding a better-grounded competitive configuration.
- **Disclosed tolerance.** A single designation may sit up to δ below the family's best on a metric. That δ is the preregistered meaning of "quality-competitive", the same margin the NI test uses. v1.2's Δ-reduced margins are removed (§29).
- **Determinism.** Every step is deterministic, uses dev only, and is committed before U1.

Worked cases: [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R13.

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

**Principle.** No complexity without a demonstrated capability deficit that the added mechanism is designed to address.

- T1 and T2 add capacity to exactly one stage: candidate-mention detection (§12.2).
- Escalation is therefore permitted only when the measured dev shortfall is attributable to **missing candidate mentions**, with every other error source kept in the accounting.

**When it is evaluated:**

- only after B0, C_A and C_B are frozen, so their designations are fixed (§11.1);
- whenever T's developer requests escalation from rung r. The check uses dev results already obtained and consumes no evaluation.
- If a request is refused, the developer may revise rung r within the remaining §11 caps and request again.

**Definitions** (full dev; exact rational arithmetic):

- **Metrics checked:** Q, and S if G5 passed.
- **Rung capacity:** M^best(r) is the maximum dev value of M over rung r's full-dev-evaluated configurations that pass sanity gates (a)–(d). φ_M(r) is the configuration attaining it; ties go to the earliest in the run ledger.
- **Threshold:** τ_M = max over k ∈ K of M_dev(k) − δ_M, where K is every designated control configuration (§11.1, §14.1). The margin is δ_Q for Q and δ_S for S.
- **Error pairs of M**, for φ_M(r):
  - for Q, the (unit, d ∈ D\*) pairs whose predicted E status differs from gold;
  - for S, the pairs whose predicted four-class state (including `NONE_OUTPUT`) differs from gold.
- **Error categories.** Each error pair gets exactly one, from φ_M(r)'s stage trace, checked in this order:

  | # | Category | Condition |
  | --- | --- | --- |
  | 1 | `NO_OUTPUT` | the unit's record is `ERROR`, `WITHHELD` or missing |
  | 2 | `NO_GOLD_SPAN` | gold has no span for (unit, d): for example gold `NOT_ADDRESSED`, or gold `INDETERMINATE` without a span |
  | 3 | `NO_CANDIDATE_MENTION` (NCM) | no candidate mention of d (support or counter, any qualifiers) was detected in any clause overlapping any gold span of (unit, d) |
  | 4 | `MENTION_PRESENT` | a candidate mention of d was detected in a clause overlapping a gold span, but the state is still wrong (a qualifier or aggregation error) |

- **Counterfactual recomputations.** Nothing in the rung changes; these only measure where the deficit lies.
  - **M^NCM:** M recomputed after replacing the prediction of every NCM error pair with its gold value (E status for Q, four-class state for S). All other predictions are unchanged.
  - **M^other:** M recomputed after correcting every error pair in categories 1, 2 and 4, leaving the NCM errors unchanged.
  - **gain_NCM** = M^NCM − M^best(r), and **gain_other** = M^other − M^best(r).

**Rung r → r+1 is permitted iff both (a) and (b) hold.**

- **(a) Shortfall.** At least one checked metric is short: M^best(r) < τ_M.
- **(b) Attribution.** For **every** short metric M:
  - **(b1) Closure:** M^NCM ≥ τ_M. Perfect mention coverage alone would close the shortfall. If it would not, the next rung cannot close the measured deficit by itself.
  - **(b2) Dominance:** gain_NCM ≥ gain_other. Missing mentions are the largest recoverable deficit.

False positives, spanless errors, missing outputs and qualifier/aggregation errors all stay in (b2)'s comparison. None of them is conditioned away.

**Outcomes:**

- **(a) fails:** rung r is final. A transparent T0 that suffices is a **valid result: no learned target is justified**.
- **(a) holds and (b) fails:** escalation is refused. The deficit lies wholly or mainly outside mention detection, so the next rung is not designed to address it.
  - The developer may revise rung r's rules within the remaining caps and request again.
  - Otherwise rung r is final.
- **(a) and (b) hold:** rung r+1 may be developed.
- **After T2:** no further escalation.
  - A shortfall at T2 means T2 still goes to final evaluation, so the negative result is preserved.
  - Any redesign needs a new protocol version **and a new locked test set**.

**Designation:** the final rung (the last rung reached) is designated, its configuration is chosen by rule J (§11.1), and both are hash-committed before U1. Every developed rung is also run on locked data, for the descriptive ladder only.

**Record:** every request's category counts, M^best, M^NCM, M^other, gains and decision are logged and committed with T's artifacts.

Worked cases: [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R8.

## 13. Metrics

All metrics are computed on the locked **main test** pool unless stated otherwise.

- **Denominator:** every assigned, non-quarantined unit, over the retained dimensions D\*.
- **Missing predictions:** `ERROR`, `WITHHELD` and missing units:
  - count as predicting non-E for every dimension in Q, R and EVCP;
  - count as the non-class `NONE_OUTPUT` in S (§13.1), which is wrong for every gold class.
- **Explicit-self-harm units:** those quarantined under §7.6 are excluded everywhere, by a pre-freeze, prediction-independent rule. There is no gold-driven, post-assignment exclusion.

### 13.1 Primary quality metrics Q and S [FROZEN]

**Q (evidenced-concern quality).** Q is the macro-average over d ∈ D\* of F1_d for the event E, where F1_d = 2TP/(2TP+FP+FN).

- A dimension with no gold-E pair in a given computation is omitted **for every arm** in that computation (§14.3). After G4, every retained dimension is present in the full locked main test.

- Gold `INDETERMINATE` counts as not-E. Claiming E there is a false positive: an unsupported assumption.
- Abstaining on a gold-E unit is a false negative. Refusal therefore cannot raise Q.

**S (observation-state quality; confirmatory when G5 passes).**

- **Pairs:** all (unit, d ∈ D\*) pairs, pooled across dimensions.
- **Gold class:** E, CON, IND or NA (§4). The arm's status is mapped the same way.
- **`NONE_OUTPUT`:** `ERROR`, `WITHHELD` and missing predictions map to `NONE_OUTPUT`, which matches no gold class. Withholding therefore never earns credit on gold-NA pairs.
- **Per-class F1:** F1_c = 2TP_c/(2TP_c+FP_c+FN_c).
- **S:** the unweighted mean of F1_c over the four classes. A class with no gold pair in a given computation is omitted **for every arm** in that computation, whether or not any arm predicted it (§14.3). Predictions of an omitted class still count as errors against the gold class of those pairs.

**Why both.** Q scores the responsibility's core output: evidenced concerns. S makes the declared observation state consequential: confusing CONTRADICTED, INDETERMINATE and NOT_ADDRESSED lowers S and can defeat H2B. The SUPPORTED-versus-MIXED split stays descriptive because MIXED is expected to be rare.

### 13.2 Coverage floor R [FROZEN]

- R is the macro recall of E over D\*, with the same dimension-omission rule as Q.
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

**EVCP** = verified ÷ claims, micro-averaged over claims. With zero claims, EVCP is undefined. §14.3 fixes every resulting disposition, in the full sample and in bootstrap replicates.

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

- **G** is every designated configuration of C_A and C_B (the general-model controls). **K** is G plus every designated configuration of B0 (the competent controls).
  - Normally each control has one designated configuration. Where rule J designates a set (§11.1), every member is a separate comparator.
  - More comparators can only make a PASS harder, so the intersection–union test needs no adjustment.
- **CI(x)** is the two-sided 95 % paired cluster-bootstrap interval of the difference T − control.

| Component | PASS | FAIL | Otherwise |
| --- | --- | --- | --- |
| **Q-NI**, each k ∈ K | lower CI(Q_T − Q_k) > −δ_Q | upper CI < −δ_Q | UNDECIDED |
| **S-NI**, each k ∈ K (removed if G5 failed) | lower CI(S_T − S_k) > −δ_S | upper CI < −δ_S | UNDECIDED |
| **R-NI**, each k ∈ K | lower CI(R_T − R_k) > −δ_Q | upper CI < −δ_Q | UNDECIDED |
| **P-SUP**, each g ∈ G | lower CI(EVCP_T − EVCP_g) **> δ_P** | upper CI < δ_P | UNDECIDED |

- P-SUP is **superiority by margin δ_P**, repaired from v1.0 (§27, R2). The data must establish an improvement greater than 0.10 at one-sided 0.025.
- When full-sample EVCP is undefined for T or for g, P-SUP against g is **FAIL** or **UNDEFINED** without a bootstrap (§14.3).
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

**No selection-dependent margins.** Every NI margin is δ_Q (for Q and R) or δ_S (for S), against every comparator. v1.2's Δ-reduced margins are removed (§29): they altered a held-out margin by a dev-set gap, which is not equivalent to testing against the discarded configuration. Rule J's per-metric anchors and designated sets address the selection problem directly (§11.1).

### 14.3 CI method and undefined values [FROZEN]

**Arithmetic.** Every metric, difference and margin comparison uses **exact rational arithmetic**. Metrics are ratios of integer counts, and margins are the recorded three-decimal values. This makes the strict inequalities of §14.1 implementation-independent.

**Resampling (paired cluster bootstrap):**

- **Cluster list.** C = [c_1, …, c_n] is the locked-main-test clusters with ≥ 1 scored unit, in ascending byte-wise order of cluster ID.
- **Draws.** For replicate b = 1, …, B and draw j = 1, …, n:

  ```text
  i(b, j) = int(SHA-256("e001-boot-v1:20260918:" + str(b) + ":" + str(j)).hexdigest()[0:16], 16) mod n
  ```

  Replicate b is the multiset {c_(i(b,j)+1) : j = 1…n}.
- B = 10,000, and 20260918 is the frozen seed. Every arm is scored on the same multisets (paired).
- **Scoring a replicate.** Each drawn cluster contributes all its scored units, once per draw. Counts are pooled with multiplicity, then the §13 metrics are computed.

**Percentile interval (exact order statistics).**

- m = ⌊0.025·B⌋. For B = 10,000, m = 250.
- lower = the (m+1)-th smallest value of the lower vector v⁻.
- upper = the (B−m)-th smallest value of the upper vector v⁺.
- For B = 10,000 these are the 251st and 9,750th smallest values. No interpolation is used.

**Undefined values in a replicate.** A component's replicate difference is undefined when either arm's metric is undefined in that replicate. For EVCP, that is zero claims by T, by the comparator, or by both.

- An undefined replicate difference enters v⁻ as **−1** and v⁺ as **+1**: the two extremes of the difference range [−1, 1].
- Undefined replicates can therefore only widen the interval. They can never produce a PASS or a FAIL.
- If more than m replicates are undefined for a component, its lower bound is −1 and its upper bound is +1. The component is UNDECIDED, unless a full-sample disposition below applies.

**Absent dimensions and classes.** These make a replicate *narrower*, not undefined, and the rule is identical for every arm:

- **Q and R:** a dimension with no gold-E pair in the replicate is omitted for every arm.
- **S:** a class with no gold pair in the replicate is omitted for every arm, whether or not any arm predicted it.
- Q, R or S is undefined only if every dimension (or class) is absent. That replicate is then treated as undefined, above.

**Full-sample EVCP dispositions for P-SUP against g.** These are fixed before any bootstrap.

| T's claims | g's claims | P-SUP against g |
| --- | --- | --- |
| 0 | any | **FAIL**: T makes no evidenced-concern claim, so it cannot be more verifiable. No bootstrap is run. |
| ≥ 1 | 0 | **UNDEFINED**: g produced no claim, a control defect. It blocks `supported` and is reported as a control defect; T never wins by a control's failure. No bootstrap is run. |
| ≥ 1 | ≥ 1 | bootstrap, as above |

- Full-sample Q, R and S are always defined after G4. A class absent from the full-sample gold is omitted for every arm.

Worked cases: [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R12.

### 14.4 Multiplicity [FROZEN]

- There is one confirmatory hypothesis: H2B, decided by the intersection–union test.
- Everything else is descriptive, with unadjusted 95 % CIs and no "supported" language. That includes S-H2A, the ladder, ADV, SHF, calibration and resources.

### 14.5 Outcome classes [FROZEN]

| Class | Condition |
| --- | --- |
| `supported` | every active component PASS; gates G1–G4 passed (G5 as recorded); no integrity defect |
| `not_supported` | any component FAIL, under valid conditions |
| `inconclusive` | no FAIL, and ≥ 1 UNDECIDED or UNDEFINED (§14.3) |
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
| Development material | train + dev + dev-visible special sets, for all arms; never the QC pool or its key (§7.7) |
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
- IUT classification, including designated comparator sets and undefined components;
- M0-based salt derivation and split hashing;
- M0 immutability checks and the restart path;
- δ_Q and δ_S;
- the T aggregation table;
- escalation triggers and their counterfactual attribution;
- evaluator robustness to malformed or adversarial predictions;
- bootstrap resampling indices, order-statistic intervals and undefined replicates;
- rule-J configuration selection.

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
- best-seed or best-configuration selection on test (selection is by rule J on dev, §11.1);
- template or label-name leakage (§8.4);
- ADCP threshold leakage (§3);
- post-M0 additions other than reserve activation, any re-salting outside the single pre-salt restart, and any post-M0 edit to canonical text (§8.1–§8.2);
- the QC pool or its key as development material, or as a source of gold (§7.7).

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
| S13 | An M0 or salt violation: a post-M0 canonical-text hash mismatch; a second M0 outside the single pre-salt restart (§8.1); a restart notice not strictly before the original R\* release; a post-M0 addition outside reserve activation; or a salt not derived per §8.2. Also: a defect that removal cannot handle, or a need for new canonical text, after the salt round is released | data / any | halted (if found before U1) / invalidated (violations found after U1) |

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

1. Scenario cards → generation and human review → authored sets. In parallel, the QC team authors and key-labels the QC pool (§7.7).
2. Explicit-self-harm screening, and the label-leak scan with the quarantine register.
3. Deduplication and cluster merging.
4. **M0 freeze and commitment.** From here on, canonical text is immutable (§8.1).
5. **QC overlap check against M0; QC-key freeze and commitment** (§7.7).
6. drand round R\* → salt → split.
7. Qualification → blind annotation → §7.6 quarantine → adjudication. Post-M0 defects are handled by removal only (§8.1).
8. **RS gates G1, G2 and G5, plus G3. Record δ_Q, δ_S and D\*.**
9. G4 on locked data (custodian-only), with reserve activation if needed.
10. Data freeze v1.0 (hashes, verified against M0).

The P1 exit is the release of train/dev to implementers. The single permitted restart (§8.1) returns to step 4. Its notice must precede the release of the original R\* (step 6). After that release there is no re-randomization: removal or halt only.

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
| A general-model control produces no E claim on the locked test | P-SUP against it is UNDEFINED → at best inconclusive (§14.3) | not decidable against that control | no evidence; the control defect is reported | no |
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
- the rules in §7.2–§7.7;
- §8 and §9;
- the recipes and candidate lists in §10.1–§10.3;
- §11–§20;
- §22–§23.

**[DEV]:**

- the C_A model and prompt;
- C_B hyperparameters and seed, by rule J (§11.1);
- the designated configurations, or designated sets, of B0, C_A and C_B, by rule J (§11.1);
- T's cue lists, rules and rung development;
- the rung designation, by the §12.3 rule only, and T's configuration within it, by rule J.

**[LOCKED]:**

- the locked pools (main test, 60 % of BND/ADV/SR, all of SHF) and their gold;
- the locked mapping of M0;
- locked-pool agreement;
- all locked-set metrics.

**Unresolved blocking items.** These must be bound before implementation starts; none can be settled by reasoning alone.

| # | Item | Owner |
| --- | --- | --- |
| B1 | Designate a custodian independent of the implementer and the T designer. | operator |
| B2 | Recruit and contract writers, annotators, an adjudicator and the QC team (§7.7), with consent, license assignment, compensation and content-support provisions, and approve the budget. See the details below the table. | operator |
| B3 | Reverify the generator pin and Ai2 terms at P0; confirm frontier generation is not used. | custodian |
| B4 | Decide whether to activate F1 (with a written terms check) and S-H2A. | operator |
| B5 | Assign an independent auditor for P3 and P4. | operator |

**B2 in detail:**

- **People:** ≥ 3 writers plus ≥ 2 separate SHF writers; ≥ 3 annotators; 1 adjudicator; a QC team of ≥ 3, subject to the §7.7 exclusions.
- **Budget:**
  - about 130 h of annotation and adjudication;
  - about 60 h of writing and review;
  - about 40 h for the QC pool (§7.7): writing, two independent key labels per unit, and adjudicator review;
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

### v1.2 author-side re-review (not an independent audit)

After applying A1–A6, the author re-checked each repair against the rest of the protocol:

- **A1 and the reserve.** Reserve units are hashed in M0, so activation never introduces text. Immutability and activation are consistent.
- **A1 and earlier repairs.** The §7.6 quarantine (R7) is removal trigger X2, with unchanged logic. Label-leak rewrites (R3) happen only before M0; after M0 a missed leak is removal X4, and registered units stay exempt.
- **A1 and the salt (R4).** The single restart derives a new salt from a new M0 and a new drand round. It is authorized, public, disclosed, limited to one, and closed at the P1 exit. No implementer has seen any data before that exit, so a restart cannot be aimed at any arm's behavior. *(Superseded in v1.3: the re-audit showed that partition shopping needs no implementer access. The restart window now closes at the original R\* release; see §29, A1.)*
- **A2.** No loss-based halt or fallback remains. Competence rests on the R0 floors (gates b and d), integrity (c) and reproducibility (e).
- **A3 and rule J.** The shortfall uses the rung's best dev value per metric, so designating a weaker configuration cannot manufacture a shortfall. The thresholds use the controls' quality anchors, which are the configurations v1.1 used for B0 and C_A. *(v1.3: thresholds now use the designated control configurations; see §29, A6.)*
- **A3 regression.** Reference cases e2, e3a and e3b are escalations that v1.1's 50 % rule would have permitted and v1.2 refuses (§R8).
- **A4 and the boundary cases.** Exact rational arithmetic and exact order statistics make §R4's equality cases H and K implementation-independent.
- **A4 and S (R5).** Class omission is now gold-based and identical for every arm, so S differences are always paired. §R3b's values are unchanged because all four classes have gold there.
- **A5 and G3.** The QC key's only consumers are qualification and G3. It never touches RS, gold, metrics or arms.
- **A6 and non-inferiority.** Without a correction, rule J could have eased NI by up to δ. The Δ-reduced margins remove that, so v1.2 is never easier than an anchor comparison on NI, and it is harder on P-SUP. *(Superseded in v1.3: the Δ-reduced margins are removed; see §29, A6.)*
- **A6 and B0.** B0 is not a P-SUP comparator. Its quality-only selection is unchanged. *(Superseded in v1.3: B0 now uses rule J with dev Q as its criterion; see §29, A6.)*

**Additional residual risks, accepted and disclosed:**

- rule J and the Δ margins rely on dev estimates, and test-set gaps may differ from dev gaps;
- the §12.3 counterfactual is an upper bound on what the next rung can recover, so a permitted escalation may still fall short (T2 then goes to final evaluation);
- the QC team adds about 40 h and at least three contributors to B2;
- one data-freeze restart is permitted, and it is disclosed if used.

### v1.3 author-side re-review (not an independent audit)

After repairing A1 and A6, the author re-checked both repairs against the rest of the protocol:

- **A1 and R4.** The restart window now closes when the original R\* is released. Before that moment no salt exists, so no split, annotation, gate result or locked count can inform the decision. After it, the only responses to a defect are removal and halt. No path yields a second partition.
- **A1 and timing.** "Strictly before the release time" is decidable from the Issue #3 server timestamp and the drand schedule alone (§R5d).
- **A1 and A5.** A restart can add new units after the QC key is committed, so the QC overlap check is rerun against them, and a hit retires the QC item.
- **A6 and the auditor's counterexample.** With independent anchors, a configuration that is strong on S can no longer be displaced by one that is S-weak but anchored on Q (§R13b).
- **A6 and empty envelopes.** A genuine tradeoff produces a designated set, and each member faces every component. No strong configuration disappears, and the extra runs stay inside the existing §15.1 caps (S7 if they cannot fit).
- **A6 and B0.** The same multi-metric hole existed for B0 on S-NI and R-NI, so B0 now uses rule J with dev Q as its criterion.
- **A6 and escalation.** The thresholds use every designated control configuration, which is exactly the set the final NI test uses.
- **Δ removal.** Every NI margin is again the plain δ. The one tolerance left is that a single designation may sit up to δ below the family's best on a metric. That tolerance is disclosed, and it equals the preregistered meaning of "quality-competitive".

**Additional residual risks, accepted and disclosed:**

- a designated set adds locked main-test runs, which may exhaust an arm's locked-inference cap (S7);
- the restart window is short (at least 24 h), so a defect found later can only be removed or halt the experiment.

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

This table is the v1.1 record and is kept as written. v1.2 supersedes two parts of it: R4's allowance for post-M0 `UNIT_DEFECT` text repairs (by A1), and R6's loss-reduction check (by A2). See §28.

## 28. Revision record — v1.1 → v1.2 (independent audit, findings A1–A6)

**Source:** the independent GPT-5.6 Sol audit of v1.1 head `b13daa94a608ef075474f6ac35cdd59650478423`, relayed by the operator on 2026-09-19. It returned six blocking findings, A1–A6. The v1.0 and v1.1 texts remain in git history, and the v1.0 audit comment on PR #17 is unchanged.

**Scope of change.** v1.2 repairs A1–A6 and their direct consistency and reference consequences, and nothing else.

- **Unchanged:** the research question, the seven-dimension ontology, H2B's components, δ_Q, δ_S, δ_P, G5, the logic of the R1, R2, R3, R5 and R7 repairs, the EVCP thresholds, the resource budgets, Reality Audit scope and the ADCP boundary.
- **Two direct consequences, disclosed:**
  - NI margins against C_A and C_B are reduced by the rule-J give-up Δ (A6). When J designates the quality anchor, Δ = 0 and the margins are exactly v1.1's.
  - S's class-omission rule is now gold-based, which keeps S differences paired in every replicate (A4).

| Finding | Defect (summary) | Repair in v1.2 | Where |
| --- | --- | --- | --- |
| **A1** | After M0, `UNIT_DEFECT` text could be repaired in place while keeping its committed identity. | Canonical text is **immutable after M0**. M0 commits cluster IDs, unit IDs and canonical-text hashes. Hashes are verified byte-exactly at data freeze, P3, U1 and U2, and on every record's `input_sha256`. A defective unit can only be **removed**, under closed triggers X1–X5. Different text needs the **single restart**: authorized, disclosed, new unit IDs, new M0, then a new salt, only before the P1 exit. Any post-M0 hash mismatch is S13. Rubric §6 now says "removed", not "repaired". | §5.1, §7.4, §8.1, §19, §20 (S13), §21, §25, rubric §6, §R5d |
| **A2** | "final-epoch loss ≤ 0.5 × first-epoch loss" was an arbitrary halt/fallback trigger, not a test of implementation correctness. | **Removed.** Training integrity is now finite losses, gradients and parameters, plus solver or schedule completion. Loss curves are diagnostic only. Competence rests on the R0 floors and reproducibility. | §11 item 5 |
| **A3** | Escalation could set aside false-positive and qualifier errors, then find `NO_CANDIDATE_MENTION` among the remaining false negatives. | **Counterfactual attribution on the full metric.** Four exhaustive error categories. For every short metric: **closure** (correcting only NCM errors reaches the threshold) and **dominance** (the NCM gain ≥ the gain from correcting all other errors). The shortfall uses the rung's best dev value against the controls' quality anchors. | §2, §11, §12.3, §25, §R8 |
| **A4** | "Undefined EVCP → failure side" was prose, not an executable rule. | **Exact semantics:** SHA-256-indexed paired resampling; exact order-statistic percentiles; exact rational arithmetic; undefined replicate differences enter the lower vector as −1 and the upper as +1; gold-based dimension/class omission for every arm; full-sample dispositions (T with zero claims → FAIL; a comparator with zero claims → UNDEFINED, which blocks `supported`). | §13.1–§13.3, §14.1, §14.3, §14.5, §22, §R4, §R12 |
| **A5** | The provenance of the qualification and QC reference key was undefined. | **QC pool (§7.7).** Human-authored by a separate QC team; two independent non-author key labels; a key value only where they agree; the adjudicator can drop but never re-key; role exclusions; an overlap check against every M0 unit; `qc-key v1.0` committed on Issue #3 before any annotation; retire-only corrections with recomputation; raw disagreement preserved; operator ownership under B2. | §7.1, §7.2, §7.5 (G3), §7.7, §16, §19, §21, §24 |
| **A6** | C_A and C_B were selected by dev Q alone, so a better-grounded, equally competitive configuration could be discarded. | **Rule J:** quality anchor → competitive Q/S/R envelope → highest dev EVCP, with deterministic tie-breaks. It applies to C_A (model × prompt), C_B (hyperparameters × seed; the median-Q seed rule is removed), T within its rung, and S-H2A. **Δ-reduced NI margins** stop J from easing non-inferiority. B0 is unchanged. | §10.1–§10.3, §11 item 4, §11.1, §12.3, §14.1, §14.2, §19, §24, §25, §R4, §R13 |

This table is the v1.2 record and is kept as written. v1.3 supersedes two parts of it: A1's restart timing (the window now closes at the original R\* release) and A6's Q-anchored envelope and Δ-reduced margins. See §29.

## 29. Revision record — v1.2 → v1.3 (independent re-audit: A1 and A6)

**Source:** the independent GPT-5.6 Sol re-audit of v1.2 head `00783025e65ead1acc6da5b2183040fc576411ed`, relayed by the operator on 2026-09-19. Disposition `REPAIR_REQUIRED`: A2, A3, A4 and A5 pass; A1 and A6 remain blocking. The v1.0, v1.1 and v1.2 texts remain in git history, and the v1.0 audit comment on PR #17 is unchanged.

**Scope of change.** v1.3 repairs only A1 and A6, with their direct reference and manifest consequences.

- **Unchanged:** A2–A5 are not reopened. Also unchanged: the research question, the ontology, H2B's components, δ_Q, δ_S, δ_P, G5, the R1, R2, R3, R5 and R7 logic, the EVCP thresholds, the resource budgets, Reality Audit scope and the ADCP boundary.
- **One direct consequence, disclosed:** v1.2's Δ-reduced NI margins are removed, so every NI margin is again the plain δ. The re-audit noted that a dev-set gap altering a held-out margin is not equivalent to testing against the discarded configuration, and the corrected rule J makes the mechanism unnecessary.

| Finding | Re-audit defect (summary) | Repair in v1.3 | Where |
| --- | --- | --- | --- |
| **A1** | The single restart was permitted until the P1 exit. By then the first salt, split, annotation, RS gates, G5 and G4 counts could be known, so a second partition could be drawn after seeing the first. | The restart notice must be committed **strictly before the original R\* is released**, while no salt can exist. The notice is irrevocable, and the restart M0 may differ only in the listed units. After the salt round is released there is **no in-protocol re-randomization**: a defect means removal (X1–X5) or halt, and new text needs a new protocol version with a genuinely new locked test set. | §8.1, §7.7, §19, §20 (S13), §21, §25, §R5d |
| **A6** | Rule J anchored the S and R envelope to the Q-best configuration's own S and R, so an S- or R-strong configuration could be displaced by an S- or R-weak one. The Δ correction did not catch this (Δ^S = 0 in the counterexample). | **Independent per-metric anchors:** Q ≥ Q^max − δ_Q, R ≥ R^max − δ_Q, S ≥ S^max − δ_S, then the highest dev EVCP. **An empty envelope** (a genuine tradeoff) designates a **set** of per-metric-competitive configurations, each a comparator facing every component, within the existing caps. B0 uses the same rule with dev Q as its criterion. Escalation thresholds use the designated configurations. **Δ margins removed.** | §10.1–§10.3, §11 item 4, §11, §11.1, §12.3, §14.1, §14.2, §24, §25, §R4, §R8, §R13 |

---

**Exact next action:** **final independent GPT-5.6 Sol verification of A1 and A6**, plus regression and scope checks, of this repaired freeze (v1.3). No implementation, annotation, training, inference, unlock or merge happens until that audit is accepted **and** the operator separately authorizes execution. The protocol author does not accept this protocol.
