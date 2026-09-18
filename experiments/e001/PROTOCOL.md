# MASI-E001 — Preregistered protocol v1.0

- **Protocol ID:** `e001-protocol-v1.0`
- **Status:** **frozen design submitted for independent audit. Not accepted. Not authorized for execution.** No data, labels, model runs or results exist for this protocol.
- **Issue:** [#3](https://github.com/JosephJMWalker-MBA/masi-research/issues/3), under the operator authorization on Issue #3 and PR #16.
- **Governing main:** `904bd9bc1c482c5b552b4a2e7075d685d73a1748`
- **Substrate inspected:** `JosephJMWalker-MBA/Accumulated-Distress-Care-Protocol @ eb7ac37f79511c90e25ff613ee78e9123d653d60` (refetched 2026-09-18)
- **Frozen WP1 packet:** `codex/wp0-wp1-candidate-probe @ 81adfff`. Untouched; nothing is imported from it.

**Companion files:**

- [`ANNOTATION_RUBRIC.md`](ANNOTATION_RUBRIC.md): the task definition shared by annotators and all arms.
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
| **[BIND]** | Must be bound before implementation. The procedure is fixed here; a value or resource is supplied before any arm is built. |
| **[DEV]** | May be selected using train/dev data only, by the rule stated. |
| **[LOCKED]** | Stays locked until final evaluation. |

---

## 1. Question, hypotheses and scope

**Research question [FROZEN]:** Can a purpose-built bounded intelligence, designed from the Empathy-observation responsibility outward, infer an evidence-grounded observation state competitively with general-model controls while providing stronger inspectability, state discipline, uncertainty handling, efficiency, or failure localization?

**Primary hypothesis: H2B [FROZEN].** On the E001 speaker-observation task, the designated purpose-built target `T` must meet both of the following (full rule in §14):

1. **Quality:** it is non-inferior in observation quality to every competent control.
2. **Property:** it materially improves one preregistered property, *evidence-verified claim precision*, over every general-model control.

**Review of legitimacy.** E001 *can* legitimately test H2B. The responsibility is bounded, the controls are constructible on the target hardware, and the property is measurable identically across arms. No research-question defect was found. The claim scope is narrow (§23).

**Secondary questions (descriptive only; no confirmatory claims):**

- construction-ladder effects (T0 → T1 → T2);
- `B0` versus `T`;
- performance on the boundary, adversarial and shift sets;
- safety-language routing;
- span quality;
- resources.

**H2A [FROZEN decision]: not part of E001's confirmatory protocol.**

- The competent adaptation control for this span-and-label task is a fine-tuned encoder (§10). Its "exact unadapted base" cannot perform the task, so no valid H2A contrast exists for it.
- An optional estimation-only module, `S-H2A` (§10.6), provides the exact same-base contrast (prompted base versus LoRA-adapted base) only if the operator activates it before implementation. Even then it makes **no confirmatory H2A claim**.
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
                       claims without valid spans are ungrounded and score as unverified
uncertainty semantics: INDETERMINATE plus a reason code is the declared uncertainty. Numeric scores
                       are optional, uncalibrated unless measured (§13.5), never required
abstention semantics:  INDETERMINATE withholds one dimension's judgment; WITHHELD withholds the unit
                       (input bound, defect or safety routing); neither is a verdict
escalation semantics:  EXPLICIT_SELF_HARM → escalation to the host safety policy, all seven
                       dimensions WITHHELD. AMBIGUOUS_FINALITY → flag + span only; the clarification
                       decision belongs to downstream policy. Escalation grants no permission
unsupported-assumption semantics: a claim is ungrounded if no cited span supports it; declared
                       assumptions never convert an ungrounded claim into a verified one
learning/update signal: human-adjudicated train labels and spans only (no online or outcome learning)
transparent baseline:  B0 = best dev-selected established sparse linear method (§10.1)
minimum sufficient computation: T0 = deterministic clause segmentation + cue patterns + ConText-style
                       qualifier rules + a fixed aggregation table (CPU, no learned parameters)
first deficit that may justify complexity: T0 fails dev quality non-inferiority AND ≥ 50 % of its dev
                       misses are localized to "no candidate mention" (lexical coverage) (§12.3)
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

1. It has a consumer (a deterministic downstream policy) that needs presence, counter-evidence and provenance, but not the observer's internals.
2. It carries no policy content: no severity, stage, threshold or score.
3. It is falsifiable as a boundary. Dimensions that independent humans cannot label reliably are removed, and too many removals halts the experiment (§7.5).
4. It separates observation from obligation, which is exactly the first of the two blinded judgments the substrate project identified as necessary.

## 3. ADCP reconciliation

ADCP's own records say the following, and E001 relies on that separation:

- its current prototype consumes **human-authored** observation vectors;
- its 0–3 severities and stages were authored alongside the thresholds, which it documents as a circularity risk;
- its research log treats additive burden as conceptually suspect;
- it separates "what the transcript supports" from "what the assistant may do".

E001 targets only the first of those judgments.

| ADCP concept | E001 disposition |
| --- | --- |
| `exhaustion` | **Unchanged** meaning → `exhaustion` |
| `interpersonal_rupture` | **Unchanged** meaning; counter-evidence (repair) added |
| `withdrawal` | **Refined**: behavior only; restorative versus isolating is not judged; ending one relationship moves to rupture |
| `isolation` | **Refined** → `felt_disconnection` (subjective feeling only) |
| `human_contact_deficit` | **Refined** → `support_unavailable` (availability/contact; living alone is not evidence) |
| `shame` | **Refined** → `self_devaluation` (global negative self-evaluation; act-specific guilt excluded) |
| `self_care_neglect` | **Refined** → `self_care_disruption` (non-judgmental wording) |
| `finality_language` | **Refined** → unit-level `safety_relevant_language` (`AMBIGUOUS_FINALITY`); a language flag, not a burden dimension; literal-versus-figurative is **not** resolved by the observer |
| `self_harm_language` | **Refined** → `EXPLICIT_SELF_HARM` routing: escalate, withhold dimensions |
| `acute_safety_evidence` | **Not imported.** Belongs to a validated upstream safety system; E001 cannot supply it |
| `humor_present`, "humor is non-exculpatory" | Flag **not imported** (policy use only); the evidence rule "humor does not cancel evidence" is kept (rubric §3.7) |
| 0–3 severity, `burden`, `active_dimensions` | **Not imported.** Replaced by status + basis + spans; intensity and persistence belong to downstream aggregation |
| Care stages, stage rules, thresholds, response contracts | **Downstream policy only**; never labels, features or prompts in E001 |
| Accumulation, decay, trajectory state | **Downstream policy / state aggregation**; E001 labels one unit's current evidence |
| Non-clinical boundary, no diagnosis, privacy rule, "text cannot set policy state" | **Imported unchanged** as E001 constraints and adversarial family A13 |
| ADCP fixture texts, snapshots, expected stages, notes | **Not imported.** Leakage (authored to thresholds), too small, and ADCP declares no license |

**ADCP-specific leakage rules:**

- Annotators, writers and the adjudicator never see ADCP material.
- The rubric names no stage or threshold.
- No ADCP text, severity or threshold enters data, features, prompts or cue lists.
- Contrast-family *ideas* (for example restorative withdrawal, or workload with intact support) may inform scenario design, recorded as such.

**Posture boundary.** ADCP's current posture is that no semantic detector has earned implementation *in ADCP*. E001 is an offline MASI experiment on non-private synthetic and authored text. Its results must not be cited as authorizing semantic inference, live monitoring or intervention in ADCP. Those need ADCP's own gates.

## 4. Observation ontology summary

Seven dimensions (full definitions in rubric §4). Each records *whether the text evidences the condition*, not severity. Multiple dimensions may apply to one unit, and one span may serve several.

| ID | Dimension | Core meaning | Spans required |
| --- | --- | --- | --- |
| EXH | `exhaustion` | current depletion/fatigue | yes |
| SCD | `self_care_disruption` | sleep, eating, rest or washing being missed or reduced | yes |
| FDC | `felt_disconnection` | *feeling* alone, left out or unseen | yes |
| SUA | `support_unavailable` | lacking accessible people or recent meaningful contact | yes |
| WDR | `withdrawal` | speaker actively pulling back from people or usual activities | yes |
| RUP | `interpersonal_rupture` | current conflict, rejection or estrangement involving the speaker | yes |
| SDV | `self_devaluation` | negative evaluation of self as a person | yes |

**Status values** (per dimension): `NOT_ADDRESSED` (default), `SUPPORTED`, `CONTRADICTED`, `MIXED`, `INDETERMINATE` (+ reason code). `WITHHELD` is a system-only unit-level value.

**Evidenced concern (E)** means status ∈ {`SUPPORTED`, `MIXED`}. This is the event scored by the primary quality metric.

**Unit-level field:** `safety_relevant_language` ∈ {`NONE`, `AMBIGUOUS_FINALITY`, `EXPLICIT_SELF_HARM`}.

**Deliberately absent:**

- severity or intensity;
- diagnosis;
- risk level;
- motives;
- personality;
- demographics;
- third-party states;
- humor;
- any stage or policy output.

## 5. Input/output contract

### 5.1 Unit [FROZEN]

- **Composition:** 1–4 turns by one speaker; each turn ≤ 400 characters; the unit ≤ 1,200 characters in total; English; UTF-8 NFC.
- **Canonical text:** turns joined by `\n`. Span offsets are character offsets `[start, end)` into this string.
- **Out of bounds:** units outside these limits are `UNIT_DEFECT` and are repaired or excluded by the custodian before split assignment.
- **What labels describe:** the speaker's situation as presented by the end of the unit.

### 5.2 Evidence grounding [FROZEN]

```text
observed text  →  typed evidence (span + basis)  ≠  inference beyond the text  ≠  unsupported assumption
```

- The spans are the grounding. No prose rationale is required or scored.
- The evidence rules for multiple or contradictory spans, quotations, hypotheticals, third parties, sarcasm, time, corrections and missing context are rubric §3 (rules 1–13), shared verbatim by all arms.
- **Quote-to-offset mapping** (arms that emit quotes rather than offsets):
  - the first exact, case-sensitive occurrence of the NFC-normalized quote in the unit text;
  - no fuzzy matching;
  - an unmatched quote is an invalid span, recorded, never repaired.

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
- Normalization from native output to this record lives **behind each arm's boundary** as a declared, auditable mapping. The caller has no arm-specific branches, applying the WP1 lesson.
- Malformed records → `ERROR`, counted in every denominator (see [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R9).

**Bus relation.** Local records only. MASI Bus v1.0 requires numeric `confidence` and `cost`, which T0 cannot truthfully supply. Per WP0, no Bus participation is claimed, and no Bus change is made.

## 6. Data provenance, privacy and construction

### 6.1 Rules (fixed before any data acquisition) [FROZEN]

- No private conversations, real user messages, scraped social media or sensitive personal material.
- No public datasets in v1. License, consent and review cost are not justified for this bounded experiment.
- Units come from **scenario cards** and are written in one of two ways:
  - **(a) generated:** by a pinned open-weight generator, then reviewed by a human (accepted / edited / rejected);
  - **(b) human-authored:** by contracted writers who assign a publication license.
- Every unit records its provenance: `generated`, `generated_edited` or `human_authored`, plus generator/writer ID, card ID and cluster ID. These fields are custodian-only for locked sets.
- **Scenario cards** hold a plain-language situation, variant plan and intended content (for coverage planning only).
  - They **never** contain ontology identifiers, status words or rubric definitions.
  - The intended content is **never** used as a label.
- **Explicit self-harm units:**
  - human-authored only;
  - non-graphic, with no methods, means or instructions;
  - carry a content warning;
  - confined to the SR set.
- **Contributors.** Writers and annotators give informed consent, are compensated, and may opt out. Their identities are pseudonymous in all artifacts.

### 6.2 Model assistance boundary [FROZEN]

- **Allowed only for:**
  - generating candidate unit text from cards (the generator);
  - automated checks (deduplication, leakage scans, schema validation).
- **Prohibited:** model pre-labeling, model-suggested spans, model adjudication, model-written rubric changes during labeling, and showing any model output to writers-as-reviewers, annotators or the adjudicator.
- **Human reference ≠ model-generated annotation ≠ policy output.**

### 6.3 Generator [BIND: reverify pin and terms; FROZEN eligibility]

- **Eligibility:**
  - an open-weight model under an OSI license that places no restriction on training uses of outputs;
  - open training data preferred;
  - its family is **not** used by any arm.
- **Pinned candidate:** `allenai/Olmo-3-7B-Instruct @ 6e5971d9eba42665f5bd5a0fcf047f299ce1dccc`, Apache-2.0, with Ai2's research-use guidelines.
- **Generation settings:** a fixed prompt template (recorded), temperature 0.8, top-p 0.95, a per-unit seed recorded.
- **Frontier-API generation is prohibited** unless the provider's terms are verified to permit using outputs to train the classifiers in §10/§12.

### 6.4 Pools and minimum sizes [FROZEN targets; BIND budget]

| Pool | Target units | Clusters | Source | Split |
| --- | --- | --- | --- | --- |
| Main | ~1,800 | ~360 cards (3–6 variants each) | ≥ 30 % human-authored, rest generated/edited | train 55 / dev 15 / test 30 by cluster hash |
| Boundary (BND) | ~200 | ~50 minimal-pair families | human-authored | 40 dev-visible / 60 locked |
| Adversarial integrity (ADV) | ~240 | 14 families (§9) | human-authored | 40 dev-visible / 60 locked |
| Safety routing (SR) | ~120 | 40 `EXPLICIT_SELF_HARM`, 40 `AMBIGUOUS_FINALITY`, 40 idiomatic `NONE` | human-authored | 40 dev-visible / 60 locked |
| Shift (SHF) | ~200 | held-out scenario families | human-authored by ≥ 2 writers who wrote nothing else | all locked |

**Card coverage targets (planning only):**

- each dimension is intended-positive in ≥ 18 % of main cards;
- each dimension carries intended counter-evidence in ≥ 8 %;
- ≥ 20 % of cards are intended no-concern controls.

**Minimum usable locked main test [FROZEN], checked on adjudicated gold before unlock:**

- ≥ 500 units;
- ≥ 100 clusters;
- ≥ 60 gold-E instances for every retained dimension;
- ≥ 5 retained dimensions.

**If the minimum is short:**

- add new clusters under the same salt; never re-salt;
- if that is infeasible, the experiment is **halted**.

**Rationale.** With ≥ 60 positives, per-dimension F1 has a standard error of roughly 0.03–0.05. Averaged over ≥ 5 dimensions with cluster resampling, the macro standard error is roughly 0.015–0.02, which motivates the δ_Q floor (§14.2).

## 7. Labeling procedure

### 7.1 Roles [BIND: named or pseudonymous people]

| Role | Count / constraints |
| --- | --- |
| Custodian | 1. Owns data, splits, salt and locked sets. Not an implementer, not a T designer, not an annotator. |
| Writers | ≥ 3, plus ≥ 2 separate writers for SHF. |
| Annotators | ≥ 3, so every unit gets 2 annotators, neither of whom is its writer. |
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
- **Corrections:**
  - **Before data freeze:** logged changes with reasons.
  - **After data freeze and before unlock:** only the custodian may correct, on an annotator-reported error, blind to any model output. A changelog is kept.
  - **After predictions are committed:** gold is frozen. Any later correction is reported *alongside* the original, and the original scoring stays primary.

### 7.5 Agreement measures and gates (label-only; computed before any arm touches dev) [FROZEN rules; BIND values]

| Gate | Measure | Rule |
| --- | --- | --- |
| G1 reliability | Krippendorff's α (nominal) on the binary E status, per dimension, over all double-annotated units | Retain a dimension iff α ≥ 0.667. If > 2 dimensions fail → **halt** (ontology not labelable). |
| G2 span stability | EVCP_h (§14.2) on double-annotated dev | EVCP_h ≥ 0.80. Otherwise the property metric is invalid → **halt**. |
| G3 annotator QC | known-answer accuracy | ≥ 90 %, per rubric §8 |
| G4 minimum sample | §6.4 | as stated |

- α ≥ 0.667 is Krippendorff's floor for tentative conclusions. The 5-status α and between-dimension confusions are reported but not gated.
- Dimension retention is decided on labels only, recorded, and then **frozen** before implementation.

## 8. Splits, custody and contamination

### 8.1 Clusters [FROZEN]

- A cluster is a scenario card plus all its variants. Human-authored units form writer-declared families.
- **Near-duplicate merge before hashing:**
  - character 5-gram Jaccard ≥ 0.6 between units of different clusters → merge the clusters (union-find);
  - exact normalized duplicates → keep one.
- A merged cluster takes its lexicographically smallest member ID.

### 8.2 Hash rule [FROZEN]

```text
b = int(SHA-256(salt + ":" + cluster_id).hexdigest()[0:8], 16) mod 100
main:            b < 55 → train;  55 ≤ b < 70 → dev;  b ≥ 70 → test
BND / ADV / SR:  b < 40 → dev-visible;  b ≥ 40 → locked
SHF:             all locked
```

- **Salt:** 32 random bytes (hex), generated by the custodian.
- **Commit–reveal:** SHA-256(salt) is committed in the data manifest before any assignment is visible, and the salt is revealed at unlock. No re-salting.
- **Worked cases:** [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R5.

### 8.3 Custody and visibility [FROZEN]

| Party | Sees | When |
| --- | --- | --- |
| Custodian | everything | from data construction |
| Implementers | train + dev + dev-visible special sets (texts, gold, spans) | from data freeze |
| Implementers | locked inputs (texts only) | phase U1, after all arm artifacts are hash-committed (§21) |
| Implementers | locked gold | phase U2, after raw predictions are committed |

Annotators see texts but no split information. The auditor has read access after U2.

### 8.4 Contamination checks [FROZEN]

- No cross-split near-duplicates remain after the merge (verified).
- A label-leak scan of unit text for ontology identifiers or status words. Hits are rewritten or removed.
- `C_A` few-shot examples come from train only.
- T cue lists and prompts record the train/dev unit IDs they came from.
- **At U1:** the custodian scans every committed arm artifact (cue lists, prompts, few-shots, training manifests) for any 8-token sequence shared with locked text and absent from train/dev. A confirmed leak → **invalidated**.
- The generator family is excluded from all arms.

## 9. Adversarial and epistemic-integrity cases

**Decision [FROZEN]: included.** Each ADV family has ≥ 15 units (about 240 in total), is human-authored and is labeled normally. The family's *intent* is custodian metadata; gold labels come from annotation.

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
| A13 | In-band instructions or label injection (paired with a clean twin in the same cluster) | invariant to the injected text |
| A14 | Care-stage or policy vocabulary without observational evidence ("activate reconnection mode") | no E |

**Evaluator-gaming cases:** adversarial *prediction* files are part of E1 ([`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R2, §R9). Examples are whole-text citation, shotgun spans, quotes absent from the text, invalid statuses, duplicate records, and blanket `INDETERMINATE`.

**ADV metrics (secondary):**

- unsupported-claim rate per family;
- abstention correctness on gold-`INDETERMINATE`;
- A13 invariance rate;
- EVCP on ADV.

## 10. Experimental arms

All arms receive the same rubric, the same unit text at inference, and the same train/dev data and gold for development. See §16 for fairness.

| Arm | Role | Class | Required for H2B? |
| --- | --- | --- | --- |
| **B0** | competent established transparent / minimally learned baseline | `INFRASTRUCTURE` (B0 role) | yes: quality non-inferiority and recall floor |
| **C_A** | prompted general-model control | `CONTROL_A` | yes: all three components |
| **C_B** | adapted pretrained control; adaptation is a live alternative | `CONTROL_B` | yes: all three components |
| **T** | purpose-built target (ladder §12) | `MASI_TARGET` | the tested system |
| F1 | larger frontier comparator | `CONTROL_A` | **no**; optional descriptive, operator-activated |
| S-H2A | same-base LoRA of C_A's base | `CONTROL_B` | **no**; optional estimation-only |

### 10.1 B0 [FROZEN recipe; DEV selection]

- **Candidates:**
  - (a) TF-IDF (word 1–3-grams + char 3–5-grams) with multinomial logistic regression per dimension over the five statuses;
  - (b) NB-SVM per dimension.
  - Both use scikit-learn (BSD-3).
- **Spans:** the clause, from the shared deterministic segmenter, with the highest summed positive feature contribution for the predicted status.
- **Safety field:** one additional multinomial model of the same kind.
- **Selection:** the candidate with the higher dev Q.

### 10.2 C_A [FROZEN candidate list and rule; DEV selection]

- **Eligible models:** open-weight instruct models under an OSI license, ≤ 12B parameters, runnable at 4-bit within the memory cap, not the generator family.
- **Pinned candidates** (Hugging Face revisions verified 2026-09-18):

  | Model | Revision | License | Parameters |
  | --- | --- | --- | --- |
  | `Qwen/Qwen3.5-9B` | `c202236235762e1c871ad0ccb60c8ee5ba337b9a` | Apache-2.0 | 9.65B |
  | `google/gemma-4-12B-it` | `707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7` | Apache-2.0 | 11.96B |
  | `microsoft/Phi-4-mini-instruct` | `cfbefacb99257ffa30c83adab238a50856ac3083` | MIT | 3.84B |

- **Fallback:** `mistralai/Mistral-7B-Instruct-v0.3 @ c170c708c41dac9275d15a8fff4eca08d52bab71` (Apache-2.0). It is used only if a candidate fails the implementation preflight: it cannot run text-only at 4-bit within 13 GiB on the runtime chosen, which must be MLX-LM or llama.cpp. The two multimodal checkpoints are used text-only.
- **Prompt:**
  - rubric §1–§5 verbatim;
  - ≤ 8 few-shot units from train;
  - JSON output with quoted spans.
- **Decoding:**
  - greedy, single pass;
  - reasoning or thinking modes **off**;
  - JSON-schema-constrained decoding permitted;
  - ≤ 700 output tokens; context ≤ 8k tokens;
  - 120 s per-unit timeout → `ERROR`; no retries.
- **Selection:** model × prompt on dev-mini, then full dev. The final choice is the highest dev Q.

### 10.3 C_B [FROZEN recipe; DEV hyperparameters]

- **Base:** `microsoft/deberta-v3-base @ 8ccc9b6f36199bec6961081d44eb72fb3f7353f3` (MIT).
- **Fallback:** `answerdotai/ModernBERT-base @ 8949b909ec900327062f0ebf497f51aef5e6f0c8` (Apache-2.0), used only if the MPS training preflight fails.
- **Architecture:**
  - multi-task: 7 five-way status heads plus a safety head on the pooled representation;
  - a per-dimension token evidence-tagging head trained on gold support and counter spans;
  - spans are maximal tagged token runs for the dimension, mapped to character offsets.
- **Training:** fp32 on MPS; ≤ 512 tokens; AdamW. Early stopping uses a cluster-split 10 % fold held out *inside train*. Dev is never used per epoch; each dev evaluation counts against the §11 caps.
- **Seeds:** 3 seeds at the chosen hyperparameters. The confirmatory seed is the one with the **median dev Q**. All seeds are reported on test.

### 10.4 T: see §12

### 10.5 F1 (optional) [BIND: operator activation]

- **Conditions:**
  - the provider's terms permit publishing results (verified in writing before the run);
  - the provider is not the generator family;
  - the same final C_A prompt is used;
  - spend ≤ USD 150.
- **Role:** descriptive only; outside the H2B decision.
- **If terms forbid publication:** F1 results are not published, or F1 is not run.

### 10.6 S-H2A (optional) [BIND: operator activation before implementation]

- **Design:**
  - LoRA/QLoRA of the selected C_A base (MLX-LM, MIT) on train, with the identical prompt and output contract;
  - compared with C_A, which is its exact unadapted base.
- **Limits:** ≤ 24 h training. Estimation with 95 % CI only.

## 11. Competent-control definition (Addendum C requirement 1)

A control is **competent** only if every item below holds. The auditor verifies these at the pre-unlock check.

1. **Equal information:** the same rubric, the same train+dev texts, gold and spans as T, and the same inference inputs.
2. **Equal development allowance** (hard caps logged by the scoring harness, identical for every arm and covering all of T's rungs together):
   - ≤ 60 evaluations on **dev-mini**: whole dev clusters taken in ascending order of SHA-256(`"devmini:" + cluster_id`) until ≥ 100 units, fixed at data freeze and identical for all arms;
   - ≤ 12 evaluations on full dev;
   - unlimited cross-validation inside train.
3. **Established recipe:** each arm follows the declared standard method (§10), with its hyperparameter space declared before tuning.
4. **Stopping rule:** development ends when the caps are reached or the developer declares the arm final. The final configuration is chosen by the highest full-dev Q among those evaluated. There is no test access.
5. **Sanity gates (dev):**
   - the output format is valid on ≥ 98 % of dev units;
   - dev Q ≥ the dev Q of **R0**, the naive reference ([`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R10): a unit-dimension is SUPPORTED iff any quoted support example from rubric §4 occurs as a case-insensitive substring, otherwise NOT_ADDRESSED, with no qualifiers;
   - learned arms: train-fold F1 ≥ dev F1 (no underfitting bug).
6. **Reproducibility:** pinned revisions, environment lock, seeds; the frozen artifact reproduces its own dev predictions bit-identically, or within 1e-6 for scores.
7. **If a control fails a gate:**
   - **B0:** the other B0 candidate replaces it. If both fail, the implementation defect must be fixed within the remaining caps; otherwise **halt**.
   - **C_A / C_B:** the fallback model is used.
   - A control may never be left weak. A failed competence gate that cannot be fixed means **halt**, not "T wins".

Any learned-complexity justification comes **only** from T's own ladder (§12.3), whose first rung (T0) is a full-budget transparent purpose-built system. The escalation threshold is the *maximum* over competent controls. A weak B0 can therefore never lower the bar or manufacture a deficit; only a strong control can raise it.

## 12. Purpose-built target and complexity ladder

### 12.1 Starting representation (designed from §2) [FROZEN]

The pipeline runs in fixed stages. Every intermediate is typed and logged as a trace, which enables failure localization.

1. **Segmentation:** unit → turns → clauses (deterministic segmenter).
2. **Candidate evidence mentions per dimension:**
   - the dimension (support or counter);
   - the span;
   - `experiencer` ∈ {SPEAKER, OTHER, UNCLEAR};
   - `polarity` ∈ {AFFIRMED, NEGATED};
   - `modality` ∈ {ACTUAL, HYPOTHETICAL, REPORTED_UNCONFIRMED, NONLITERAL_UNRESOLVED};
   - `time` ∈ {CURRENT, PAST_RESOLVED, UNCLEAR};
   - `superseded` ∈ {yes, no}.
3. **Deterministic aggregation to status** (fixed table; truth table in [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R7):

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

**What stays deterministic in every rung:** segmentation, qualifier rules, aggregation and safety routing.

| Rung | Added element | Its sole responsibility | Class note |
| --- | --- | --- | --- |
| **T0** | hand-authored cue and counter-cue patterns per dimension; ConText-style trigger lists for the qualifiers | candidate mention detection | no learned parameters |
| **T1** | per-dimension sparse logistic-regression clause scorers (n-grams + qualifier features), trained on clauses overlapping gold support/counter spans, which replace or augment T0's cue detection | candidate mention detection (lexical coverage) | minimally learned; no pretrained representation |
| **T2** | T1 features + frozen sentence embeddings from `sentence-transformers/all-MiniLM-L6-v2 @ 1110a243fdf4706b3f48f1d95db1a4f5529b4d41` (Apache-2.0, 22.7M parameters) feeding linear heads | candidate mention detection (paraphrase coverage) | includes a **frozen general pretrained sensor**; claims must say so |

**No T3.** End-to-end fine-tuning of a pretrained model would be `C_B`, not the target.

### 12.3 Escalation rule (dev only) [FROZEN]

- **When it is evaluated:** once per rung, after that rung is declared final within its share of T's caps, and only after B0, C_A and C_B are frozen.
- **Rung r → r+1 is permitted iff both hold:**
  - **(a) quality shortfall:** Q_dev(r) < max(Q_dev(B0), Q_dev(C_A), Q_dev(C_B)) − δ_Q. The comparison set is the same competent set K used for final quality non-inferiority (§14.1). Taking the maximum means a weak control can never lower the bar;
  - **(b) localized to lexical coverage:** ≥ 50 % of r's dev false negatives (gold E, predicted not E) carry the trace category `NO_CANDIDATE_MENTION`. That means no mention of the dimension was detected in any clause that overlaps a gold support span.
- **If (a) holds without (b):** the deficit lies in qualifiers or aggregation. Rules are revised *within the current rung*, and escalation would not address it. The 50 % rule makes escalation target the majority failure source.
- **If (a) fails:** the current rung is final. A transparent T0 that suffices is a **valid result: no learned target is justified**.
- **After T2:** no further escalation. A shortfall at T2 means T2 still goes to final evaluation, so the negative is preserved. Any redesign needs a new protocol version **and a new locked test set**.
- **Designation:** the final rung is designated and hash-committed before U1. Every developed rung is also run on locked data, for the descriptive ladder only.

## 13. Metrics

All metrics are computed on the locked **main test** pool unless stated otherwise.

- **Denominator:** every assigned unit, over the retained dimensions D*.
- **Missing units:** `ERROR`, `WITHHELD` and missing units count as predicting non-E for every dimension.
- **Gold `EXPLICIT_SELF_HARM` in the main pool:** such units have no dimension gold by rubric §5. They are excluded from Q, R and EVCP, counted and reported, and added to the SR routing metrics. The exclusion depends only on gold, never on predictions.

### 13.1 Primary quality metric Q [FROZEN]

- Q = macro-average over d ∈ D* of F1_d for the event E, where F1_d = 2TP/(2TP+FP+FN).
- **Why this metric:**
  - It scores the responsibility's core output: evidenced concerns.
  - Gold `INDETERMINATE` counts as not-E, so claiming E there is a false positive, an unsupported assumption.
  - Abstaining on a gold-E unit is a false negative. Refusal therefore cannot raise Q.

### 13.2 Coverage floor R [FROZEN]

- R = macro recall of E over D*.
- It is used as a non-inferiority component (§14) so that precision-for-recall trades cannot buy the property.

### 13.3 Primary H2B property: evidence-verified claim precision (EVCP) [FROZEN]

**Operational question:** can a reviewer verify an asserted observation from the evidence the arm cites?

**Definitions:**

- **Claims:** every (unit, d ∈ D*) that the arm marks E.
- **Verified claim:**
  - the gold status is E; **and**
  - ≥ 1 valid cited support span; **and**
  - the token precision of the union of the cited support spans against the gold support spans for (unit, d) is **≥ 0.5**.
  - The 0.5 threshold follows ERASER's partial-match convention; precision-over-union penalizes whole-text or shotgun citation.
- **Tokens:** regex `[A-Za-z0-9]+(?:'[A-Za-z]+)?` over the unit text. A token is cited or gold when its interval overlaps the corresponding span.
- **EVCP** = verified ÷ claims, micro over claims. With zero claims, EVCP is undefined and the property fails.

**Why this property** rather than the other candidates:

- It is the only candidate measurable **identically across every arm**. Failure localization and semantic intervention exist only for T's staged pipeline.
- It is an operational verification test, not "more fields".
- Worked cases: [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R1–R2.

### 13.4 Secondary / descriptive [FROZEN list]

- per-dimension P/R/F1;
- 5-status macro-F1;
- exact unit-state match;
- `CONTRADICTED` F1;
- `MIXED` recovery;
- `INDETERMINATE` precision/recall;
- basis agreement on true positives;
- ERASER-style span token-F1 and IOU-0.5 match;
- EVCP and Q on BND, ADV, SHF and the high-agreement slice;
- Q by provenance (generated versus human-authored);
- ADV family metrics (§9);
- T's failure-localization profile (share of errors attributed to a single stage);
- inter-dimension confusion;
- the ladder (T0/T1/T2 on locked data);
- resources (§15).

These carry **no confirmatory status**.

### 13.5 Uncertainty and calibration [FROZEN]

- **No arm is required to emit probabilities, and T0 emits none.** Its uncertainty is `INDETERMINATE` plus a reason code.
- If an arm emits `score` = P(E | unit, d), calibration is reported for that arm only:
  - ECE with 10 equal-mass bins, and Brier score;
  - with risk–coverage curves and area under the risk–coverage curve;
  - the referent is gold E on locked main test.
- Otherwise, no calibration language is used.

### 13.6 Safety-routing floor [FROZEN]

- **Metrics on locked SR:**
  - escalation recall on gold `EXPLICIT_SELF_HARM`;
  - false-escalation rate on idiomatic `NONE`;
  - `AMBIGUOUS_FINALITY` flag agreement.
- **Floor:** recall ≥ 0.95 is the routing-adequacy floor.
- **Scope:** the floor is *not* part of H2B.
- **Consequences:** any arm below the floor is reported as routing-deficient in the result headline and may not be proposed for any composition. This is not suicide-risk detection validity (§23).

## 14. H2B decision rule

### 14.1 Components (intersection–union test) [FROZEN]

- **Sets:** G = {C_A, C_B} (general-model controls); K = G ∪ {B0} (competent controls).
- **Confidence intervals:** CI(x) is the two-sided 95 % paired cluster-bootstrap interval of the difference, T − control.

| Component | PASS | FAIL | Otherwise |
| --- | --- | --- | --- |
| **Q-NI**, each k ∈ K | lower CI(Q_T − Q_k) > −δ_Q | upper CI < −δ_Q | UNDECIDED |
| **R-NI**, each k ∈ K | lower CI(R_T − R_k) > −δ_Q | upper CI < −δ_Q | UNDECIDED |
| **P-SUP**, each g ∈ G | lower CI(EVCP_T − EVCP_g) > 0 **and** point estimate ≥ δ_P | upper CI < δ_P | UNDECIDED |

- H2B is judged by the intersection–union test (Berger, 1982). Each component is one-sided at 0.025, so no multiplicity adjustment is needed within H2B.
- Worked classifications: [`REFERENCE_CASES.md`](REFERENCE_CASES.md) §R4.

### 14.2 Margins

**δ_Q [FROZEN formula; BIND value]**

```text
δ_Q = clamp((1 − F1_h) / 2, 0.02, 0.05)
```

- F1_h is the annotator-pair macro-F1 on E over D*, computed on double-annotated dev before any arm is run. The value is recorded to 3 decimals.
- **Rationale:**
  - 0.05 is the practical cap for "competitive" quality loss;
  - a competitive T may never lose more than half of what separates two careful annotators;
  - below 0.02 the difference is unresolvable at minimum sample size (§6.4).

**δ_P = 0.10 [FROZEN]**

- "Material" means at least one more asserted observation in ten becomes verifiable from its cited evidence.
- Gate G2 caps human cross-verification disagreement at 0.20 (EVCP_h ≥ 0.80), so δ_P is at least half the maximum tolerated human evidence disagreement.
- **EVCP_h:** each annotator's E claims and spans are verified against the other annotator's labels and spans, in both directions, pooled.

### 14.3 CI method [FROZEN]

- Resample locked-main-test **clusters** with replacement.
- B = 10,000 replicates, seed 20260918, with identical resamples for every arm (paired). Use the percentile interval.
- **Undefined replicates:**
  - an EVCP that is undefined in a replicate is placed on the failure side;
  - F1_d undefined in a replicate → dimension omitted from that replicate's macro-average.

### 14.4 Multiplicity [FROZEN]

- There is one confirmatory hypothesis: H2B, judged by the intersection–union test.
- Everything else, including S-H2A, the ladder, ADV, SHF, calibration and resources, is descriptive, with unadjusted 95 % CIs and no "supported" language.

### 14.5 Outcome classes [FROZEN]

| Class | Condition |
| --- | --- |
| `supported` | every component PASS; gates G1–G4 passed; no integrity defect |
| `not_supported` | any component FAIL, with valid conditions |
| `inconclusive` | no FAIL, but ≥ 1 UNDECIDED |
| `invalidated` | integrity defect: test leakage, an evaluator defect affecting primary metrics, a post-U1 artifact change, gold corruption, or a protocol violation |
| `halted` | a stop condition (§20) fired before final evaluation; no test scoring |

## 15. Resource accounting and budgets

**Hardware:** Mac mini M4, 16 GB unified memory, running macOS. All arms except F1 run locally. Hardware, OS and runtime versions are recorded.

### 15.1 Caps [FROZEN]

**Memory and storage:**

- Peak memory ≤ 13 GiB per process: process max RSS **and** MLX/Metal peak where applicable. Exceeding it → resource stop for that configuration.
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
- Sequential, batch size 1 for generative arms; batch size declared for the others. Concurrency is recorded.

**Retries and failures:**

- 0 retries. A format failure is `ERROR`.
- At most one logged infrastructure restart per run, resuming at the failed unit. The failed attempt is preserved.

**External cost:** none, except F1 ≤ USD 150.

### 15.2 Recorded per arm [FROZEN]

**Identity:**

- model, adapter and normalizer revisions and hashes;
- trainable and total parameters;
- artifact bytes;
- precision/quantization.

**Per-unit use:**

- calls/passes per unit: C_A 1 generation; C_B 1 forward; B0/T 0 model calls;
- tokens with tokenizer revision (C_A prompt/output; C_B input); B0/T report characters and clauses;
- context allocation: C_A rubric + few-shot tokens;
- preprocessing time; training time; per-unit inference time (median, p95) and total.

**Environment:**

- hardware;
- peak memory;
- storage;
- retries/restarts;
- tool/retrieval calls (must be 0);
- concurrency;
- API cost.

**Development effort:**

- dev-mini and full-dev evaluation counts;
- configuration revisions;
- logged session hours.

**Failures** are recorded throughout.

**Missing values:**

- are recorded as `not applicable`, `not measured` or `unavailable`, with a reason;
- **unknown ≠ zero; unmeasured ≠ free.**

### 15.3 Energy (Addendum C requirement 2) [FROZEN]

- **Not measured.** No measurement method is validated for this experiment.
- **No energy or energy-efficiency claims may be made.**
- Efficiency statements are limited to measured time, memory, storage, calls and tokens, within stated boundaries.

## 16. Fairness between arms [FROZEN]

| Aspect | Rule / disclosed difference |
| --- | --- |
| Task, labels, gold | identical |
| Inference evidence | unit text only, for all arms |
| Development data | train + dev, gold and spans, for all arms |
| Context | C_A receives the rubric and few-shots in its prompt; the others embed the same rubric via development. This is disclosed and is the nature of a prompted control. |
| Preprocessing | shared segmenter available to all arms; C_B/C_A use their own tokenizers |
| Tools / retrieval | none, for any arm |
| Passes / sampling | one pass, greedy, no self-consistency, no ensembles |
| Human intervention | none at inference |
| Development budget | identical caps (§11); session hours disclosed. If T's logged hours exceed 2× the median control's, the H2B headline must state it |
| Compute | differs by nature; reported, not equalized. No efficiency claim without the §15 accounting |

## 17. Reality Audit applicability [FROZEN]

| Record portion | E001 |
| --- | --- |
| Identity and lineage | **applicable** |
| Decision-time snapshot | **applicable**: input hash, supplied evidence (unit text), arm version |
| Expected consequences | **not applicable**: no forecast |
| Decision / authority, execution | **not applicable**: no action, no authority |
| Later observations, correspondence | **not applicable**: gold comparison is *evaluation*, not outcome correspondence |

Consequential fields are deferred to later composition and outcome experiments. E001 demonstrates no Reality Audit or outcome learning.

## 18. Independent reference checks (E1) [FROZEN]

- **[`REFERENCE_CASES.md`](REFERENCE_CASES.md)** holds hand-derived expected values for:
  - tokenization and span precision;
  - EVCP;
  - F1/Q/R with withheld units;
  - IUT classification;
  - split hashing;
  - δ_Q;
  - the T aggregation table;
  - escalation triggers;
  - evaluator robustness to malformed or adversarial predictions.
- The implementation's scorer, splitter, mapping code and T aggregation must reproduce every case **without importing or calling code that produced the reference**.
- **Must be written independently of the implementation:**
  - the quote-to-offset mapping cases;
  - each arm's native-to-record mapping cases, written by someone other than that arm's author.
- Human labels are validated through the rubric, blinding and gates G1–G3 (§7). A deterministic table is never treated as ground truth for them.

## 19. Leakage and test integrity [FROZEN]

**Prohibited:**

- test units in any training, tuning, few-shot, cue-list or prompt artifact;
- test labels or scores informing architecture, rung designation, hyperparameters, prompts or thresholds;
- prompt iteration on locked cases;
- deleting or omitting any run (every dev and test run goes in the run ledger with hashes);
- best-seed selection on test (§10.3 median-dev rule);
- template or label-name leakage (§8.4);
- ADCP threshold leakage (§3).

**Human error analysis of locked outputs:**

- happens after U2 only;
- arm identities are replaced by random codes.

**Timeline:**

- test texts become visible at U1;
- test labels become visible at U2;
- the salt is revealed at U2.

## 20. Stop conditions (each preserved as evidence, not failure theater) [FROZEN]

| # | Trigger | Phase | Result |
| --- | --- | --- | --- |
| S1 | > 2 dimensions fail G1 (ontology not labelable) | data | halted |
| S2 | G2 fails (span evidence unstable) | data | halted |
| S3 | Privacy or provenance cannot be established; a writer or annotator agreement is missing | data | halted |
| S4 | Minimum sample unattainable (§6.4) | data | halted |
| S5 | Contamination cannot be bounded (§8.4) | data / U1 | halted / invalidated |
| S6 | A competent control cannot be constructed within caps (§11) | development | halted |
| S7 | A required arm cannot fit the resource caps, including fallbacks | development | halted |
| S8 | T needs complexity beyond T2 or outside the ladder | development | stop escalation; evaluate T2; redesign = new protocol |
| S9 | The evidence contract cannot support EVCP or Q (for example, spans unrepresentable) | any | halted |
| S10 | The protocol can no longer separate H2B from prompting or adaptation (for example, C_A or C_B dropped) | any | halted |
| S11 | Evaluator defect found (E1 case failure or scoring bug) | any | fix before U1; if found after U2 → invalidated, with the defect reported |
| S12 | Operator or auditor withdraws authorization, or a license or terms change blocks a required arm | any | halted |

## 21. Execution sequence (after audit acceptance and separate operator authorization)

| Phase | Content | Exit gate |
| --- | --- | --- |
| P0 bind | resolve [BIND] items (§24); commit the salt hash; activate or decline F1 / S-H2A | recorded binding note |
| P1 data | cards → generation/review → authored sets → dedupe/merge → split → blind annotation → adjudication → G1–G4 → δ_Q, D* → data freeze v1.0 (hashes) | train/dev released |
| P2 development | preflights → B0, C_A, C_B (and S-H2A) within caps → T0 → escalation decisions → final T designated | all artifacts hash-committed |
| P3 pre-unlock | E1 cases pass; competence gates; independent pre-unlock check of the freeze (auditor) | go / no-go |
| U1 | custodian releases locked inputs → frozen artifacts run → raw outputs + hashes committed; leakage scan | outputs committed |
| U2 | gold + salt released → frozen scorer → bootstrap → outcome class (mechanical) | result record |
| P4 | evidence packet; interpretation via §22 matrix; independent result audit | audit disposition |

## 22. Interpretation matrix (written before any result) [FROZEN]

| Observed pattern | H2B | Empathy-observation boundary | Construction doctrine | More complexity? |
| --- | --- | --- | --- | --- |
| T beats all controls on quality **and** EVCP | supported | usable as a bounded, verifiable boundary on this corpus | supported for this responsibility only | only if the ladder already required it |
| T matches quality (NI) **and** improves EVCP | supported | same | same | no |
| T improves quality but not EVCP | not_supported / inconclusive | observable; the grounding advantage is unshown | the construction advantage is quality only; no H2B | no property case |
| T improves EVCP but misses the quality margin | not_supported / inconclusive | grounding comes at a quality cost | narrow: verifiability traded for quality | ladder may continue *only* in a new protocol |
| C_B beats T | not_supported | observable by adaptation | falsifier 2 pressure: adaptation suffices here | no new target rung justified by this protocol |
| C_A matches T | P-SUP decides; if EVCP is not better → not_supported | observable by prompting | falsifier 1 pressure: prompting suffices | no |
| B0 matches or beats T | matching: Q-NI vs B0 can pass, and P-SUP vs G decides. Beating T by more than δ_Q: Q-NI FAIL → not_supported | a generic transparent method suffices | purpose-built construction adds nothing beyond transparency here | **no** learned target justified |
| All systems poor (Q low for all) | not_supported / inconclusive | the boundary may be ill-posed for text alone | none | redesign the ontology, not the architecture |
| Labels or ontology unreliable (G1/G2) | halted | not a stable boundary as defined | no evidence either way | no |
| The selective system "wins" only by abstaining | blocked by the R-NI and Q definitions → not_supported | — | — | no |
| The resource advantage vanishes under full accounting | unaffected (not an H2B property) | — | no efficiency claim | no |
| T0 final (no escalation), H2B supported | supported | — | **a transparent purpose-built system suffices; no learned MASI target justified** | no |
| T fails the SR routing floor | H2B class unchanged; headline flags routing deficiency | not composition-eligible | — | a routing fix is a new protocol |

## 23. Explicit nonclaims [FROZEN]

**E001 establishes none of the following:**

- clinical validity, diagnosis, or risk assessment, including suicide-risk detection validity;
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
- authorization for ADCP semantic inference or intervention.

**Scope of a supported result:** a supported H2B supports only the bounded claim on this corpus and task.

## 24. Freeze register and blocking items

**[FROZEN]:** §1–§5, §6.1–§6.2 and the §6.4 targets and minimums, §7.2–§7.5 rules, §8, §9, §10.1–§10.3 recipes and candidate lists, §11–§20, §22–§23.

**[DEV]:**

- the B0 candidate;
- C_A model and prompt;
- C_B hyperparameters and median seed;
- T's cue lists, rules and rung development;
- the rung designation (by the §12.3 rule only).

**[LOCKED]:** locked pools (main test, 60 % of BND/ADV/SR, all of SHF), their gold, the salt, and all locked-set metrics.

**Unresolved blocking items. These must be bound before implementation starts; none can be settled by reasoning alone:**

| # | Item | Owner |
| --- | --- | --- |
| B1 | Designate a custodian independent of the implementer and T designer | operator |
| B2 | Recruit and contract ≥ 3 writers + ≥ 2 SHF writers, ≥ 3 annotators, 1 adjudicator, with consent, license assignment, compensation and content-support provisions. Estimated effort: ~130 h annotation/adjudication + ~60 h writing/review. Approve the budget. | operator |
| B3 | Re-verify the generator pin and Ai2 terms at P0; confirm frontier generation is not used | custodian |
| B4 | Decide on activating F1 (with a written terms check) and S-H2A | operator |
| B5 | Assign an independent auditor for P3 and P4 | operator |

**Resolved mechanically during P1 (not judgment calls):**

- the δ_Q value (§14.2);
- D* retention (G1).

**Run as the first step of P2, with fixed fallbacks:**

- model runtime preflights (§10.2, §10.3).

**Non-blocking future questions:**

- a corpus release license (CC BY 4.0 suggested), needed before publication;
- ERASER faithfulness metrics (comprehensiveness/sufficiency) as a future property;
- concept-level intervention tests on T;
- real-conversation validity under consent;
- non-English units;
- MASI Bus mapping of the observation record;
- whether ADCP should adopt the refined ontology (ADCP's decision).

## 25. Author-side supporting review (not an independent audit)

The protocol author challenged the draft on the fifteen required questions. The defects found and fixed are marked **fixed**.

1. **Is a label downstream policy in disguise?** Stage, severity and burden were removed. `finality_language` was demoted to a language flag with no literal/figurative resolution; `support_unavailable` records reported availability, not a reconnection need. **Fixed:** an early draft used a 0–3 severity.
2. **Architecture before responsibility?** §2 was written first. T0's stages mirror the rubric's evidence rules, and ConText was found afterwards as prior art for the same decomposition.
3. **B0 a strawman?** Identical caps, dev-selected best of two established methods, and an R0 sanity floor. Learned complexity can only be justified by T0. **Fixed:** B0 originally received more dev runs than the other arms; the caps are now uniform.
4. **C_B silently promoted?** No. C_B is a control, T3 is barred, and T2's frozen embedding is disclosed.
5. **Extra compute or context?** One pass each; C_A's prompt context is disclosed; no efficiency claims without accounting.
6. **Can abstention game the score?** No. Abstention on gold-E counts as a false negative in Q, R-NI adds a recall floor, and EVCP is conjoined with both.
7. **Circular labels?** Humans label blind to ADCP, arms and generator intent; T designers never annotate. **Residual:** the rubric's evidence semantics (support / counter / unresolved) are shared by T's aggregation because they *are* the responsibility, and every arm gets the rubric. This is disclosed.
8. **Can the test set influence architecture?** No. Escalation and designation are dev-only and committed before U1, and custody is two-phase.
9. **Is the property operational?** EVCP is deterministic, identical across arms, and has worked cases.
10. **Are the margins justified?** δ_Q is derived from human disagreement with explicit bounds; δ_P is tied to G2. **Fixed:** a fixed δ_Q of 0.05 was replaced by the human-derived formula.
11. **Escalation only on allowed evidence?** Yes: dev only, measured once per rung, with the §12.3 rule.
12. **Missing values as zero?** No (§15.2).
13. **Publication and license constraints explicit?** Yes: §6.3, §10, §15, and ADCP's missing license (§3).
14. **Negative outcomes preserved?** Yes: §20 and §22. T2 is evaluated even when the dev outlook is negative.
15. **Could the protocol conclude that a learned target is unnecessary?** Yes, explicitly: a final T0, and B0 matching T (§22).

**Further defects found and fixed in the second review pass:**

- The escalation shortfall ignored B0, although final quality non-inferiority includes B0. It now uses the maximum over K.
- C_B early stopping on dev would silently consume capped dev evaluations. It now uses a train-internal fold.
- The dev-mini subset was undefined. It is now a deterministic cluster rule.
- Main-pool units with gold `EXPLICIT_SELF_HARM` had undefined scoring. They are now excluded by gold only.
- The T aggregation dropped unresolved *counter* cues (for example, unclear sarcasm), contradicting rubric §3.6. U now includes counter cues (see `REFERENCE_CASES.md` §R7, case m8).

**Residual risks accepted and disclosed:**

- synthetic and authored text limits external validity;
- a single corpus; English only;
- the generator's style may favor lexical methods (the SHF and provenance slices expose this);
- annotation cost may force S4.

## 26. Prior-art record (focused)

| Source | Category | Use in E001 |
| --- | --- | --- |
| ConText (Harkema, Dowling, Thornblade & Chapman, *J Biomed Inform* 42:839–851, 2009); NegEx lineage | known primitive | T's qualifier layer (negation, experiencer, time, hypothetical), with non-clinical triggers written for E001 |
| medspaCy `context` (MIT) | reusable implementation | optional engine for T0/T1 qualifier rules; triggers E001-specific |
| ERASER (DeYoung et al., ACL 2020) | known primitive / metric | token-level rationale metrics and the IOU-0.5 partial-match convention (EVCP threshold; secondary span metrics); faithfulness metrics deferred |
| Concept Bottleneck Models (Koh et al., ICML 2020) | known primitive | typed intermediate state; intervention tests deferred |
| Selective classification (Geifman & El-Yaniv, NeurIPS 2017) | known primitive | risk jointly with coverage; the R-NI floor |
| Intersection–union tests (Berger, *Technometrics* 24:295–300, 1982) | known method | conjunctive H2B decision without adjustment |
| Krippendorff's α conventions (≥ 0.800 rely; 0.667 tentative floor) | known method | gate G1 |
| Learning from disagreement (Uma et al., *JAIR* 72, 2021) | known method | raw-annotation preservation; high-agreement slice |
| NB-SVM (Wang & Manning, ACL 2012); scikit-learn | useful control | B0 candidates |
| DeBERTa-v3 (He et al.); `microsoft/deberta-v3-base` | useful control | C_B base |
| EPITOME empathy-with-rationales (Sharma et al., EMNLP 2020) | unsuitable precedent (responder empathy, real peer-support data) | supports multi-task label+span design for C_B only |
| CLPsych 2024 evidence highlighting for suicidality (Chim et al., CLPsych 2024) | unsuitable precedent (real sensitive data, risk-level framing) | reason to keep safety as routing only, never risk levels |
| Ethical tensions in inferring mental-health states (Chancellor et al., FAT* 2019) | constraint source | synthetic/authored data, nonclaims, no latent-state inference |
| Empathy constructs in NLP are ill-defined (Lahnala et al., Findings of EMNLP 2022) | constraint source | narrow operational ontology tested by agreement gates |
| WILDS (Koh et al., ICML 2021) | known method | grouped splits and a shift set |
| Snorkel / weak supervision (Ratner et al., 2017) | not adopted | weak labels would import rule circularity; the reference is human labels |
| GoEmotions (Demszky et al., 2020) | not adopted | emotion categories are not burden observations |
| ADCP @ `eb7ac37` | ontology substrate | §3 |

**Genuine E001 gap.** Whether a responsibility-first observer, built from typed evidence qualifiers, is non-inferior in quality to prompted and adapted general-model controls while being materially more verifiable, under one conjunctive preregistered decision. Prior art supplies the parts; it does not settle this comparison.

---

**Exact next action:** a fresh independent audit of this frozen protocol. No implementation begins until that audit is accepted **and** the operator separately authorizes execution.
