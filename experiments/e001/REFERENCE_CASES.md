# MASI-E001 — Independent reference cases (E1)

**Status:** frozen with `e001-protocol-v1.1`, pending a second fresh independent audit.

**Changes from v1.0:**

- **R2:** coverage condition added (cases c14–c16).
- **R3b:** state metric S added.
- **R4:** P-SUP superiority margin and S-NI added; cases re-derived.
- **R5:** M0 and beacon-salt derivation added.
- **R6:** δ_S added.
- **R8:** S escalation cases added.
- **R9:** additions.
- **R11:** new.

**How the values were derived:**

- By hand, from the definitions in [`PROTOCOL.md`](PROTOCOL.md).
- Character offsets and SHA-256 values were confirmed with Python's standard library (`str.find`, `re`, `hashlib`, `math`).
- No E001 scorer, splitter or pipeline code existed when these values were written.

**Rules for the implementation:**

- It must reproduce every value **without importing or calling any code that produced these values**.
- Standard SHA-256 is not reimplemented.
- A disagreement is a **defect to resolve before U1** (protocol §20, S11).
- A case may be changed only if the case itself is shown to contradict the protocol text. Every such change is logged.

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

**Text C** (10 characters): `Exhausted.` It has one token, `Exhausted`, at [0,9).

**Gold used below:**

| Text | Dimension | Status | Span(s) |
| --- | --- | --- | --- |
| A | `exhaustion` | SUPPORTED | support [30,49) (4 tokens) |
| A | `self_care_disruption` | SUPPORTED | support [0,14) (3 tokens) |
| B | `exhaustion` | CONTRADICTED | counter [42,50) |
| C | `exhaustion` | SUPPORTED | support [0,9) (1 token) |

Text B follows rubric §3.1: the sister's claim is `REPORTED_UNCONFIRMED`, and the speaker then denies it, which is counter-evidence.

## R2 — Evidence-verified claims (EVCP)

A claim is **verified** iff all of the following hold:

1. the gold status is E (`SUPPORTED` or `MIXED`);
2. there is ≥ 1 valid cited **support** span;
3. **precision:** the token precision of the union of cited support spans, measured against the union of gold support spans, is ≥ 0.5;
4. **coverage:** some single gold support span has ≥ 0.5 of its tokens cited.

Invalid spans are dropped first. A span is invalid if `start < 0`, `end > len`, `start ≥ end`, or it comes from an unmatched quote.

| Case | Text / dim | Cited support span(s) | Cited tokens | In gold | Precision | Coverage (best gold span) | Verified? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| c1 | A / EXH | [34,42) `so tired` | 2 | 2 | 1.00 | 2/4 = 0.50 | **yes** |
| c2 | A / EXH | [0,50) whole unit | 10 | 4 | 0.40 | 1.00 | no (precision) |
| c3 | A / EXH | [0,14) wrong-dimension evidence | 3 | 0 | 0.00 | 0.00 | no |
| c4 | A / EXH | [16,28) + [34,42) shotgun | 5 | 2 | 0.40 | 0.50 | no (precision) |
| c5 | A / EXH | none | 0 | — | — | — | no |
| c6 | A / EXH | quote `I am so tired` (no exact match) | 0 (invalid) | — | — | — | no |
| c7 | A / EXH | [36,50), which includes a leading space and a period | 2 (`tired`, `lately`) | 2 | 1.00 | 0.50 | **yes** |
| c8 | B / EXH | [22,31) `exhausted` | 1 | gold not E | — | — | no |
| c9 | A / SCD | [0,14) | 3 | 3 | 1.00 | 1.00 | **yes** |
| c10 | A / EXH | counter span only, no support span | 0 | — | — | — | no |
| c11 | A / EXH | [45,40) (start ≥ end) | invalid | — | — | — | no |
| c12 | A / EXH | [40,60) (end > len) | invalid | — | — | — | no |
| c13 | A / EXH | [16,42) | 6 | 3 | 0.50 | 3/4 = 0.75 | **yes** (both thresholds are inclusive) |
| c14 | A / EXH | [37,42) `tired` (one in-gold token) | 1 | 1 | 1.00 | 1/4 = 0.25 | **no** (coverage) |
| c15 | A / EXH | [34,36) `so` (one in-gold function word) | 1 | 1 | 1.00 | 0.25 | **no** (coverage) |
| c16 | C / EXH | [0,9) `Exhausted` (a one-token gold span) | 1 | 1 | 1.00 | 1/1 = 1.00 | **yes** |

**Pooled EVCP:**

- Claims {c1, c2, c4, c9} → EVCP = 2/4 = **0.500**.
- Claims {c1, c14} → EVCP = 1/2 = **0.500**. Under v1.0's precision-only rule this would have been 2/2; the coverage condition now blocks the tiny citation.

**Zero claims:** EVCP is undefined, and the property component fails.

## R3 — Q, R and denominators

**Setup:** two dimensions, five units.

- "E" means gold or predicted status ∈ {SUPPORTED, MIXED}.
- "–" means any other status.
- u5 is `WITHHELD`, so it predicts non-E.

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
- **Denominator trap:** dropping u5 would wrongly give EXH F1 = 0.500 and Q = 0.500. That is a **defect**.

## R3b — State quality S (four classes, pooled pairs)

**Setup:** two dimensions × four units = eight pairs. u4 is `WITHHELD`, so both of its pairs become `NONE_OUTPUT`.

| Pair | Gold class | Predicted class |
| --- | --- | --- |
| (u1, EXH) | E | E |
| (u1, SCD) | CON | CON |
| (u2, EXH) | IND | NA |
| (u2, SCD) | NA | NA |
| (u3, EXH) | CON | IND |
| (u3, SCD) | E | E |
| (u4, EXH) | NA | NONE_OUTPUT |
| (u4, SCD) | IND | NONE_OUTPUT |

| Class | TP | FP | FN | F1 |
| --- | --- | --- | --- | --- |
| E | 2 | 0 | 0 | 1.000 |
| CON | 1 | 0 | 1 | 2/3 = 0.667 |
| IND | 0 | 1 | 2 | 0.000 |
| NA | 1 | 1 | 1 | 2/4 = 0.500 |

- **S = (1.000 + 0.6667 + 0.000 + 0.500) / 4 = 0.54167.**
- **Withholding trap:** mapping the withheld pairs to NA instead of `NONE_OUTPUT` gives NA TP = 2, FP = 2, FN = 0, so F1(NA) = 0.667 and S = **0.58333**. That rewards withholding, and it is a **defect**.

## R4 — H2B classification (intersection–union test)

**Rules** (δ_Q = 0.030, δ_S = 0.050, δ_P = 0.10):

| Component | PASS | FAIL | Otherwise |
| --- | --- | --- | --- |
| Q-NI, R-NI | lower > −δ_Q | upper < −δ_Q | UNDECIDED |
| S-NI | lower > −δ_S | upper < −δ_S | UNDECIDED |
| P-SUP | **lower > δ_P** | upper < δ_P | UNDECIDED |

**Overall:**

- `supported` = all components PASS;
- `not_supported` = any FAIL;
- `inconclusive` = no FAIL and ≥ 1 UNDECIDED.

**Base case A.** Every component PASSes, so the outcome is **`supported`**.

| Component | Comparator | Interval / estimate |
| --- | --- | --- |
| Q-NI | B0 | [−0.010, 0.040] |
| Q-NI | C_A | [−0.020, 0.030] |
| Q-NI | C_B | [−0.025, 0.010] |
| S-NI | B0 | [−0.020, 0.040] |
| S-NI | C_A | [−0.035, 0.015] |
| S-NI | C_B | [−0.045, 0.005] |
| R-NI | B0 | [0.000, 0.050] |
| R-NI | C_A | [−0.015, 0.035] |
| R-NI | C_B | [−0.028, 0.012] |
| P-SUP | C_A | 0.18 [0.11, 0.25] |
| P-SUP | C_B | 0.20 [0.12, 0.28] |

**Variants.** Each changes one component of case A.

| Case | Change | Component | Outcome |
| --- | --- | --- | --- |
| B | P-SUP C_B 0.07 [0.01, 0.13] | UNDECIDED | `inconclusive` |
| C | Q-NI C_B [−0.090, −0.040] | FAIL | `not_supported` |
| D | Q-NI C_A [−0.050, 0.010] | UNDECIDED | `inconclusive` |
| E | P-SUP C_A 0.12 [−0.01, 0.25] | UNDECIDED | `inconclusive` |
| F | P-SUP C_A 0.03 [−0.02, 0.08] | FAIL (upper < 0.10) | `not_supported` |
| G | R-NI B0 [−0.060, −0.035]; the recall loss drives the result | FAIL | `not_supported` |
| H | Q-NI C_B [−0.030, 0.020]; the lower bound equals −δ_Q, and the inequality is strict | UNDECIDED | `inconclusive` |
| I | Case A, but gate G1 failed before evaluation | — | `halted` (no test scoring) |
| **J** | **P-SUP C_B 0.10 [0.01, 0.19]** (the audit's example) | UNDECIDED; v1.0 would have PASSED it | `inconclusive` |
| **K** | P-SUP C_A 0.16 [0.10, 0.22]; the lower bound equals δ_P, and the inequality is strict | UNDECIDED | `inconclusive` |
| **L** | S-NI C_A [−0.080, −0.055]: state confusion | FAIL (upper < −0.05) | `not_supported` |
| **M** | Case A with G5 failed before implementation: S-NI is removed, and the remaining components PASS | — | `supported`, using the **narrowed** H2B wording |

## R5 — Split assignment and salt derivation

### R5a — Hash rule, with a fixed reference salt (unchanged from v1.0)

The reference salt `e001-REFERENCE-ONLY-salt` must **never** be used as a real salt.

- SHA-256 of the salt string: `84305deeb8e20828f8086f7035a070b91c7f764e24be62815234665a54e2ae19`.
- Hash input: the UTF-8 bytes of `salt + ":" + cluster_id`.

| cluster_id | First 8 hex | int | b | Main | BND / ADV / SR |
| --- | --- | --- | --- | --- | --- |
| c0001 | d2b8a75f | 3535316831 | 31 | train | dev-visible |
| c0002 | 247a05a9 | 611976617 | 17 | train | dev-visible |
| c0003 | f25380ee | 4065558766 | 66 | dev | locked |
| c0005 | 6ad85093 | 1792561299 | 99 | test | locked |
| c0023 | 64f9dd1f | 1694096671 | 71 | test | locked |

**Near-duplicate merge:** joining c0003 and c0005 gives cluster ID `c0003` (the lexicographically smallest), so the whole merged cluster goes to **dev**.

### R5b — M0 bytes, M0 hash and beacon-derived salt (§8.1–§8.2)

The reference manifest has two clusters: c0001 is active, and c0002 is reserve rank 1.

| unit_id | canonical text | SHA-256 (UTF-8) |
| --- | --- | --- |
| u0001 | `I barely slept.` | `4ba87bfbee1ac8dc01d8057470673a2da8ec89f7248b31ded4319c3961c1b7ed` |
| u0002 | `Work is fine.` | `6ea69d8fc352309f43fed5cd1a40342dadf299efc1983c1a03370a353375c467` |
| u0003 | `I'm so tired lately.` | `fcd695727597a17a40bcb2f2477c68358cbc5466c8b18ddca3aa74ea66e62eab` |

**M0 bytes** (252 bytes, UTF-8, `\t` = TAB, each line ending in `\n`):

```text
c0001\tmain\tactive\tu0001:4ba87bfbee1ac8dc01d8057470673a2da8ec89f7248b31ded4319c3961c1b7ed,u0002:6ea69d8fc352309f43fed5cd1a40342dadf299efc1983c1a03370a353375c467\n
c0002\tmain\treserve:1\tu0003:fcd695727597a17a40bcb2f2477c68358cbc5466c8b18ddca3aa74ea66e62eab\n
```

**Derived values:**

- M0 hash: `5324a7c7e320bc3e8581f794d029ce0ffa1efb74eb683c09773b37e1f1c2fafd`.
- Reference beacon randomness (**not** a real drand value): 64 × `0`.
- salt = SHA-256(`"e001-salt-v1:" + M0_hash + ":" + randomness`) = `316317c78043bb43041774d17a8c6845f7098eb73950baf0d5fcc784c4af6ccb`.

| cluster_id | First 8 hex | int | b | Bucket (main) | Note |
| --- | --- | --- | --- | --- | --- |
| c0001 | d5835b9f | 3582155679 | 79 | test | active |
| c0002 | d6858bd0 | 3599076304 | 4 | train, **if activated** | reserve rank 1: it enters its hashed bucket; there is no choice |

### R5c — The beacon round R\*

The drand default chain has genesis 1595431050 and a 30 s period. Round r is released at 1595431050 + (r − 1)·30.

R\* = ⌈(target − genesis)/30⌉ + 1, where target = M0-commitment time + 86400 s.

| M0 commitment (UTC) | target (unix) | R\* | R\* release (UTC) |
| --- | --- | --- | --- |
| 2026-10-01T00:00:00Z | 1790899200 | 6515606 | 2026-10-02T00:00:00Z (exactly the target) |
| 2026-10-01T00:00:10Z | 1790899210 | 6515607 | 2026-10-02T00:00:30Z |

## R6 — Margins δ_Q and δ_S

δ = clamp((1 − agreement)/2, 0.02, 0.05). The formula is the same for both: agreement is F1_h for δ_Q and S_h for δ_S.

| F1_h or S_h | (1 − x)/2 | δ |
| --- | --- | --- |
| 0.70 | 0.150 | 0.050 |
| 0.84 | 0.080 | 0.050 |
| 0.92 | 0.040 | 0.040 |
| 0.93 | 0.035 | 0.035 |
| 0.95 | 0.025 | 0.025 |
| 0.97 | 0.015 | 0.020 |
| 0.98 | 0.010 | 0.020 |

## R7 — T aggregation

**Status from the non-empty mention sets** (1 = the set is non-empty):

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
| m2 | "My sister says I look exhausted" (on its own) | REPORTED_UNCONFIRMED | U | INDETERMINATE (REPORTED_UNCONFIRMED) |
| m3 | "I'm not exhausted" | support cue NEGATED by the speaker | C | CONTRADICTED |
| m4 | "I'm exhausted — actually no, I slept great" | the first cue is superseded; "slept great" is a counter cue | C | CONTRADICTED |
| m5 | "If I lose this job I'll be exhausted" | HYPOTHETICAL | dropped | NOT_ADDRESSED |
| m6 | "My roommate is exhausted" | OTHER | dropped | NOT_ADDRESSED |
| m7 | "Last spring I was exhausted, that's behind me" | the cue is PAST_RESOLVED (dropped); the resolution statement is a counter cue, CURRENT | C | CONTRADICTED |
| m8 | "Oh sure, I'm *totally* rested" (sarcasm, unclear) | counter cue NONLITERAL_UNRESOLVED | U | INDETERMINATE (NONLITERAL_UNRESOLVED) |
| m9 | Text B (m2 + "Honestly I'm fine") | U and C | C, U | CONTRADICTED |

## R8 — Escalation trigger (dev only)

**Settings:**

- δ_Q = 0.04 and δ_S = 0.05.
- Final dev Q: B0 0.64, C_A 0.66, C_B 0.70. The Q threshold is max − δ_Q = **0.66**.
- Final dev S: B0 0.55, C_A 0.58, C_B 0.60. The S threshold is max − δ_S = **0.55**.
- Maxima are taken over K = {B0, C_A, C_B}.

| Case | Rung, dev Q / S | G5 | Short on | `NO_CANDIDATE_MENTION` share of the relevant errors with a gold span | Decision |
| --- | --- | --- | --- | --- | --- |
| e1 | T0, 0.61 / 0.58 | passed | Q | 48/80 = 60 % | escalate to T1 |
| e2 | T0, 0.61 / 0.58 | passed | Q | 30/80 = 37.5 % | no escalation; revise qualifier/aggregation rules within T0's remaining budget |
| e3 | T0, 0.66 / 0.56 | passed | none (0.66 is not < 0.66; 0.56 is not < 0.55) | — | T0 final; no learned target |
| e4 | T2, 0.60 / 0.50 | passed | Q, S | 70 % | no further rung (maximum reached); T2 designated and evaluated |
| e5 | T0, 0.68 / 0.50 | passed | S | 36/60 = 60 % | escalate to T1 |
| e6 | T0, 0.68 / 0.50 | passed | S | 20/60 = 33 % | no escalation; revise rules within T0 |
| e7 | T0, 0.68 / 0.50 | **failed** | none (S is not used after a G5 failure) | — | T0 final |
| e8 | T0, 0.61 / 0.50 | passed | Q, S | pooled union of 100 pairs, 55 of them `NO_CANDIDATE_MENTION` = 55 % | escalate to T1 |

## R9 — Evaluator robustness (adversarial predictions)

| Prediction defect | Required treatment |
| --- | --- |
| Status string not in the enum; unknown key; duplicate record for (unit, dimension) | the unit becomes `ERROR`: non-E in Q, R and EVCP, and `NONE_OUTPUT` in S; it stays in the denominators |
| Unit missing from the predictions | `ERROR`, as above |
| Prediction for a unit not in the pool (including §7.6-quarantined units) | ignored and logged |
| Invalid span (R2 rules) | dropped; the claim may become unverified |
| Claim on a dropped dimension (not in D\*) | ignored for Q, R, S and EVCP |
| E claimed with counter spans only | unverified (R2, c10) |
| Single-token citation of a multi-token gold span | unverified (R2, c14–c15) |
| Blanket `INDETERMINATE` on every dimension | Q = 0 and R = 0, so Q-NI and R-NI FAIL whenever any competent control's Q and R exceed δ_Q. S is also low, because only gold-IND pairs are correct. |
| Blanket `WITHHELD` | Q = R = 0 and S = 0 (`NONE_OUTPUT` matches no class) |
| Blanket E with whole-unit spans | recall rises, but precision and EVCP fall (R2, c2); scored as computed |
| Quote with a curly apostrophe (`I’m`) where the text has a straight one (`I'm`) | no exact match → invalid span; NFC does not unify apostrophes |

**Quote-to-offset mapping** (Text A):

| Quote | Mapped span |
| --- | --- |
| `so tired` | [34,42) |
| `I'm so tired` | [30,42) |
| `I` | [0,1) (first occurrence) |
| `i'm so tired` | no match (case-sensitive) |
| `so  tired` (double space) | no match |

## R10 — R0 naive reference (competence sanity floor, protocol §11)

**R0 rule:** a unit-dimension is SUPPORTED iff any *quoted* support example listed for that dimension in rubric §4 occurs as a case-insensitive substring. Otherwise it is NOT_ADDRESSED. Safety is always `NONE`.

| Text | Dimension | R0 result | Reason |
| --- | --- | --- | --- |
| A | EXH | NOT_ADDRESSED | `tired` is not a quoted example |
| A | SCD | NOT_ADDRESSED | `I barely slept` matches no quoted example |
| B | EXH | SUPPORTED | `exhausted` matches; R0 ignores reported speech and denial |

Text B's EXH result is why R0 is only a floor.

## R11 — Deterministic dev-mini and inner-validation selection (protocol §11)

Clusters are ordered by ascending SHA-256 of the prefixed ID, and whole clusters are taken until the unit threshold is met.

| Prefix | Order for {c0001, …, c0005} (first 8 hex) |
| --- | --- |
| `devmini:` | c0001 (042f7feb), c0003 (27111009), c0004 (a96f4121), c0002 (db7ecd11), c0005 (f5624fd6) |
| `innerval:` | c0005 (1e1c1f38), c0004 (30e88c47), c0001 (368f5717), c0003 (a710fbbc), c0002 (bb05202a) |

**Worked example.** Suppose these were the dev clusters, with sizes c0001 = 40, c0003 = 35, c0004 = 30 units. Then dev-mini = {c0001, c0003, c0004}: the running total reaches 105 ≥ 100 at c0004.
