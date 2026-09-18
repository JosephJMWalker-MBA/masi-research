# MASI-E001 — Independent reference cases (E1)

**Status:** frozen with `e001-protocol-v1.0`, pending independent audit.

## How these values were produced

- The expected values were derived by hand from the definitions in [`PROTOCOL.md`](PROTOCOL.md). Character offsets and SHA-256 buckets were confirmed with Python's standard library (`str.find`, `re`, `hashlib`).
- No E001 scorer, splitter or pipeline code existed when these values were written.
- The implementation must reproduce every value here **without importing or calling any code that produced these values**.
- Standard SHA-256 is not reimplemented.
- A disagreement between the implementation and a case below is a **defect to resolve before U1** (protocol §20, S11). The case may be changed only if the case itself is shown to contradict the protocol text. Every such change is logged.

**Conventions:**

- Spans are character offsets `[start, end)` into the canonical unit text.
- Tokens match the regex `[A-Za-z0-9]+(?:'[A-Za-z]+)?`.
- A token *overlaps* a span when `token.start < span.end` **and** `span.start < token.end`.

---

## R1 — Tokenization

**Text A** (50 characters):

```text
I barely slept. Work is fine. I'm so tired lately.
```

| Token | `I` | `barely` | `slept` | `Work` | `is` | `fine` | `I'm` | `so` | `tired` | `lately` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Span | [0,1) | [2,8) | [9,14) | [16,20) | [21,23) | [24,28) | [30,33) | [34,36) | [37,42) | [43,49) |

**Text B** (62 characters; the turn break `\n` is at index 32):

```text
My sister says I look exhausted.
Honestly I'm fine, just busy.
```

| Token | `My` | `sister` | `says` | `I` | `look` | `exhausted` | `Honestly` | `I'm` | `fine` | `just` | `busy` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Span | [0,2) | [3,9) | [10,14) | [15,16) | [17,21) | [22,31) | [33,41) | [42,45) | [46,50) | [52,56) | [57,61) |

**Gold used below:**

| Text | Dimension | Status | Span(s) |
| --- | --- | --- | --- |
| A | `exhaustion` | SUPPORTED | support [30,49) (`I'm so tired lately`) |
| A | `self_care_disruption` | SUPPORTED | support [0,14) (`I barely slept`) |
| B | `exhaustion` | CONTRADICTED | counter [42,50) (`I'm fine`) |

Text B's gold follows from rubric §3.1. The sister's report is `REPORTED_UNCONFIRMED`, and the speaker then denies it, which is counter-evidence.

## R2 — Evidence-verified claims (EVCP)

A claim is **verified** iff all three hold:

- the gold status is E (`SUPPORTED` or `MIXED`);
- there is ≥ 1 valid cited **support** span;
- the token precision of the union of cited support spans, measured against the gold support spans, is **≥ 0.5**.

Invalid spans (`start < 0`, `end > len`, `start ≥ end`, or an unmatched quote) are dropped before evaluation.

| Case | Text / dimension | Cited support span(s) | Cited tokens | In gold | Precision | Verified? |
| --- | --- | --- | --- | --- | --- | --- |
| c1 | A / EXH | [34,42) `so tired` | 2 | 2 | 1.00 | **yes** |
| c2 | A / EXH | [0,50) whole unit | 10 | 4 | 0.40 | no |
| c3 | A / EXH | [0,14) wrong-dimension evidence | 3 | 0 | 0.00 | no |
| c4 | A / EXH | [16,28) + [34,42) shotgun | 5 | 2 | 0.40 | no |
| c5 | A / EXH | none | 0 | — | — | no |
| c6 | A / EXH | quote `I am so tired`, which has no exact match | 0 (invalid) | — | — | no |
| c7 | A / EXH | [36,50), which includes a leading space and a period | 2 (`tired`, `lately`) | 2 | 1.00 | **yes** |
| c8 | B / EXH | [22,31) `exhausted` | 1 | gold not E | — | no |
| c9 | A / SCD | [0,14) | 3 | 3 | 1.00 | **yes** |
| c10 | A / EXH | counter span only, no support span | 0 | — | — | no |
| c11 | A / EXH | [45,40) (start ≥ end) | invalid | — | — | no |
| c12 | A / EXH | [40,60) (end > len) | invalid | — | — | no |
| c13 | A / EXH | [16,42) | 6 (`Work`, `is`, `fine`, `I'm`, `so`, `tired`) | 3 | 0.50 | **yes** (the threshold is inclusive) |

**Pooled EVCP example.** If an arm's only claims are c1, c2, c4 and c9 (four claims across different units), then EVCP = 2/4 = **0.500**.

**Zero claims.** EVCP is undefined, and the property component fails.

## R3 — Q, R and denominators

Two dimensions, five units.

- "E" means gold or predicted status ∈ {SUPPORTED, MIXED}.
- "–" means any other status.
- Unit u5 is `WITHHELD`, so it predicts non-E for every dimension.

| Unit | Gold EXH | Gold SCD | Predicted EXH | Predicted SCD |
| --- | --- | --- | --- | --- |
| u1 | E | E | E | E |
| u2 | E | – | – (`INDETERMINATE`) | E |
| u3 | – (`INDETERMINATE`) | E | E | – |
| u4 | – | – | – | – |
| u5 | E | – | WITHHELD | WITHHELD |

| Dimension | TP | FP | FN | F1 | Recall |
| --- | --- | --- | --- | --- | --- |
| EXH | 1 | 1 | 2 | 2/5 = **0.400** | 1/3 = 0.333… |
| SCD | 1 | 1 | 1 | 2/4 = **0.500** | 1/2 = 0.500 |

- **Q = 0.450; R = 0.41667** (= 5/12).
- **Denominator trap:** dropping u5 would wrongly give EXH F1 = 0.500 and Q = 0.500. That is a **defect**, because withheld units must stay in the denominator.

## R4 — H2B classification (intersection–union test)

**Rules** (δ_Q = 0.030, δ_P = 0.10):

- **Q-NI and R-NI:**
  - PASS iff lower > −δ_Q;
  - FAIL iff upper < −δ_Q;
  - otherwise UNDECIDED.
- **P-SUP:**
  - PASS iff lower > 0 **and** point estimate ≥ δ_P;
  - FAIL iff upper < δ_P;
  - otherwise UNDECIDED.
- **Overall:**
  - `supported` = all PASS;
  - `not_supported` = any FAIL;
  - `inconclusive` = no FAIL and ≥ 1 UNDECIDED.

**Base case A** (all components PASS):

| Component | Comparator | Interval / estimate |
| --- | --- | --- |
| Q-NI | B0 | [−0.010, 0.040] |
| Q-NI | C_A | [−0.020, 0.030] |
| Q-NI | C_B | [−0.025, 0.010] |
| R-NI | B0 | [0.000, 0.050] |
| R-NI | C_A | [−0.015, 0.035] |
| R-NI | C_B | [−0.028, 0.012] |
| P-SUP | C_A | 0.18 [0.11, 0.25] |
| P-SUP | C_B | 0.14 [0.06, 0.22] |

Case A is **`supported`**.

**Variants** (each changes one component of case A):

| Case | Change | Component result | Outcome |
| --- | --- | --- | --- |
| B | P-SUP C_B 0.07 [0.01, 0.13] | UNDECIDED | `inconclusive` |
| C | Q-NI C_B [−0.090, −0.040] | FAIL | `not_supported` |
| D | Q-NI C_A [−0.050, 0.010] | UNDECIDED | `inconclusive` |
| E | P-SUP C_A 0.12 [−0.01, 0.25] | UNDECIDED | `inconclusive` |
| F | P-SUP C_A 0.03 [−0.02, 0.08] | FAIL | `not_supported` |
| G | R-NI B0 [−0.060, −0.035]: the recall loss drives the result | FAIL | `not_supported` |
| H | Q-NI C_B [−0.030, 0.020]: the lower bound equals −δ_Q, and the inequality is strict | UNDECIDED | `inconclusive` |
| I | Case A, but gate G1 failed before evaluation | — | `halted` (no test scoring) |

## R5 — Split assignment

These cases use the reference salt `e001-REFERENCE-ONLY-salt`. **It must never be used as the real salt.**

- Its commitment: SHA-256(salt) = `84305deeb8e20828f8086f7035a070b91c7f764e24be62815234665a54e2ae19`.
- Hash input: the UTF-8 bytes of `salt + ":" + cluster_id`.

| cluster_id | First 8 hex | int | b = int mod 100 | Main pool | BND / ADV / SR |
| --- | --- | --- | --- | --- | --- |
| c0001 | d2b8a75f | 3535316831 | 31 | train | dev-visible |
| c0002 | 247a05a9 | 611976617 | 17 | train | dev-visible |
| c0003 | f25380ee | 4065558766 | 66 | dev | locked |
| c0005 | 6ad85093 | 1792561299 | 99 | test | locked |
| c0023 | 64f9dd1f | 1694096671 | 71 | test | locked |

**Merge rule:** if near-duplicates join c0003 and c0005, the merged cluster ID is `c0003` (the lexicographically smallest), so the whole merged cluster goes to **dev**.

## R6 — δ_Q

δ_Q = clamp((1 − F1_h) / 2, 0.02, 0.05):

| F1_h | (1 − F1_h)/2 | δ_Q |
| --- | --- | --- |
| 0.84 | 0.080 | 0.050 |
| 0.92 | 0.040 | 0.040 |
| 0.95 | 0.025 | 0.025 |
| 0.97 | 0.015 | 0.020 |

## R7 — T aggregation

**Status from the three mention sets** (1 = the set is non-empty):

| S | C | U | Status |
| --- | --- | --- | --- |
| 1 | 0 | 0 or 1 | SUPPORTED |
| 0 | 1 | 0 or 1 | CONTRADICTED |
| 1 | 1 | 0 or 1 | MIXED |
| 0 | 0 | 1 | INDETERMINATE |
| 0 | 0 | 0 | NOT_ADDRESSED |

**Mention classification** (EXH unless stated otherwise):

| Case | Text | Qualifiers | Set | Status |
| --- | --- | --- | --- | --- |
| m1 | "I'm so tired lately" | SPEAKER, AFFIRMED, ACTUAL, CURRENT | S | SUPPORTED |
| m2 | "My sister says I look exhausted" (alone) | REPORTED_UNCONFIRMED | U | INDETERMINATE (REPORTED_UNCONFIRMED) |
| m3 | "I'm not exhausted" | support cue NEGATED by the speaker | C | CONTRADICTED |
| m4 | "I'm exhausted — actually no, I slept great" | first cue superseded; "slept great" is a counter cue | C | CONTRADICTED |
| m5 | "If I lose this job I'll be exhausted" | HYPOTHETICAL | dropped | NOT_ADDRESSED |
| m6 | "My roommate is exhausted" | OTHER | dropped | NOT_ADDRESSED |
| m7 | "Last spring I was exhausted, that's behind me" | cue PAST_RESOLVED (dropped); resolution statement is a counter cue, CURRENT | C | CONTRADICTED |
| m8 | "Oh sure, I'm *totally* rested" (sarcasm, unclear) | counter cue NONLITERAL_UNRESOLVED | U | INDETERMINATE (NONLITERAL_UNRESOLVED) |
| m9 | Text B (m2 + "Honestly I'm fine") | U and C | C, U | CONTRADICTED |

## R8 — Escalation trigger (dev only)

Setting: δ_Q = 0.04; final dev Q is B0 0.64, C_A 0.66 and C_B 0.70. The shortfall threshold is max(0.64, 0.66, 0.70) − 0.04 = **0.66**. The maximum is taken over the competent set K = {B0, C_A, C_B}.

| Case | Rung, dev Q | Shortfall? | Dev false negatives with `NO_CANDIDATE_MENTION` | Decision |
| --- | --- | --- | --- | --- |
| e1 | T0, 0.61 | yes | 48/80 = 60 % | escalate to T1 |
| e2 | T0, 0.61 | yes | 30/80 = 37.5 % | no escalation; revise qualifier/aggregation rules within T0's remaining budget |
| e3 | T0, 0.66 | no (0.66 is not < 0.66) | — | T0 final; no learned target |
| e4 | T2, 0.60 | yes | 70 % | no further rung (maximum reached); T2 designated and evaluated |

## R9 — Evaluator robustness (adversarial predictions)

| Prediction defect | Required treatment |
| --- | --- |
| Status string not in the enum; unknown key; duplicate record for (unit, dimension) | the unit becomes `ERROR`; non-E for every dimension; kept in the denominator |
| Unit missing from predictions | `ERROR`, as above |
| Prediction for a unit not in the pool | ignored and logged |
| Invalid span (R2 rules) | dropped; the claim may become unverified |
| Claim on a dropped dimension (not in D*) | ignored for Q, R and EVCP |
| E claimed with counter spans only | unverified (R2 c10) |
| Blanket `INDETERMINATE` on every dimension | Q = 0 and R = 0, so Q-NI and R-NI FAIL whenever any competent control's Q and R exceed δ_Q (abstention cannot win) |
| Blanket E on every dimension with whole-unit spans | recall rises, but precision and EVCP fall (R2 c2); scored as computed |
| Quote with a curly apostrophe (`I’m`) where the text has a straight one (`I'm`) | no exact match → invalid span (NFC does not unify apostrophes) |

**Quote-to-offset mapping** (text A):

| Quote | Mapped span |
| --- | --- |
| `so tired` | [34,42) |
| `I'm so tired` | [30,42) |
| `I` | [0,1) (first occurrence) |
| `i'm so tired` | no match (case-sensitive) |
| `so  tired` (double space) | no match |

## R10 — R0 naive reference (competence sanity floor, protocol §11)

**R0 rule.** A unit-dimension is SUPPORTED iff any *quoted* support example listed for that dimension in rubric §4 occurs as a case-insensitive substring. Otherwise it is NOT_ADDRESSED. Safety is always `NONE`.

| Text | Dimension | R0 result | Reason |
| --- | --- | --- | --- |
| A | EXH | NOT_ADDRESSED | `tired` is not a quoted example |
| A | SCD | NOT_ADDRESSED | `I barely slept` matches no quoted example |
| B | EXH | SUPPORTED | `exhausted` matches, and R0 ignores reported speech and denial |

Text B's EXH result is why R0 is only a floor.
