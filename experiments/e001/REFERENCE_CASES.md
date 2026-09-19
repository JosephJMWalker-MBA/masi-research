# MASI-E001 — Independent reference cases (E1)

**Status:** frozen with `e001-protocol-v1.3`, pending final independent verification of A1 and A6.

**Changes in v1.3 (re-audit findings A1 and A6):**

- **R4:** the Δ-reduced margins are gone, so every NI margin is δ again. Case N is replaced by a designated-set case.
- **R5d:** restart-window timing cases added (d7 and d8 rewritten).
- **R8:** the thresholds are described as designated control configurations. All values are unchanged.
- **R13:** rewritten. Independent per-metric anchors, the re-audit's counterexample, an empty envelope that yields a designated set, and B0 under rule J.

**Changes in v1.2 (findings A1–A6):**

- **R2:** the zero-claim sentence now points to R12e (A4).
- **R4:** Δ-reduced margins, undefined components and exact arithmetic added (cases N, O, P, V, W).
- **R5d:** new. M0 immutability checks and the restart path (A1).
- **R8:** rewritten. Counterfactual escalation attribution (A3).
- **R9:** input-hash mismatch row added (A1).
- **R12:** new. Bootstrap draws, replicate scoring, absent dimensions and classes, order statistics, undefined replicates and full-sample dispositions (A4).
- **R13:** new. Rule-J configuration selection (A6).

**Changes in v1.1:**

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

**Zero claims:** EVCP is undefined. The resulting P-SUP dispositions are fixed in §R12e.

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
- All four classes have gold here, so v1.2's gold-based class-omission rule (§R12c) leaves S unchanged.

## R4 — H2B classification (intersection–union test)

**Rules** (δ_Q = 0.030, δ_S = 0.050, δ_P = 0.10). Each designated control configuration is a separate comparator (§R13).

| Component | PASS | FAIL | Otherwise |
| --- | --- | --- | --- |
| Q-NI, R-NI | lower > −δ_Q | upper < −δ_Q | UNDECIDED |
| S-NI | lower > −δ_S | upper < −δ_S | UNDECIDED |
| P-SUP | **lower > δ_P** | upper < δ_P | UNDECIDED |

**Overall:**

- `supported` = all components PASS;
- `not_supported` = any FAIL;
- `inconclusive` = no FAIL, and ≥ 1 UNDECIDED or UNDEFINED.

**Base case A.** Rule J designated one configuration per control. Every component PASSes, so the outcome is **`supported`**.

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
| **N** | C_A has an empty joint envelope, so rule J designates the set {ψ3, ψ4} (§R13d). Against ψ3, every component is as in case A. Against ψ4: Q-NI [−0.020, 0.030], R-NI [−0.015, 0.035], P-SUP 0.15 [0.11, 0.19], but S-NI [−0.070, −0.010] | S-NI ψ4 UNDECIDED; everything else PASS | `inconclusive`. Designating ψ3 alone would have given `supported`: the S-strong configuration would have disappeared |
| **O** | T makes no E claim on the locked main test | P-SUP FAIL against C_A and C_B, with no bootstrap (§R12e) | `not_supported` |
| **P** | C_B makes no E claim on the locked main test; everything else as case A | P-SUP C_B UNDEFINED (§R12e) | `inconclusive`; the control defect is reported |
| **V** | Case P plus case G's R-NI B0 FAIL | UNDEFINED and FAIL | `not_supported` (a FAIL decides) |
| **W** | Q-NI C_A: the bounding replicate has Q_T = 33/100 and Q_k = 36/100, so the exact lower bound is −3/100 = −δ_Q | UNDECIDED (strict inequality, exact arithmetic; §R12f) | `inconclusive`. Floating point gives 0.33 − 0.36 = −0.02999999999999997 > −0.03, a false PASS: a **defect** |

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

### R5d — M0 immutability and the restart path (§8.1)

The committed M0 is the one in §R5b (hash `5324a7c7…fafd`). Hashes are SHA-256 of the UTF-8 bytes of the canonical text, compared byte-exactly.

| Case | Event after M0 | Check | Result |
| --- | --- | --- | --- |
| d1 | u0001 is delivered as `I barely slept.` | `4ba87bfbee1ac8dc01d8057470673a2da8ec89f7248b31ded4319c3961c1b7ed` equals the M0 entry | pass |
| d2 | u0001 is "repaired" to `I barely slept` (period removed) and keeps ID u0001 | `bd6bbdbca3207decf0191bd5b42828bfb3776584b6eb27cbef15f3edc234da52` ≠ M0 entry | **S13**: halted before U1, invalidated after |
| d3 | u0001 is delivered with a trailing space, `I barely slept. ` | `67fcae90fa3adbfe7d5c832f7f8e29f8ab150cc9bd5ce16fe34418cf3ab4c04a` ≠ M0 entry | **S13** |
| d4 | u0002 is removed under X1 (`UNIT_DEFECT`) | M0 bytes and hash are unchanged; c0001 keeps bucket 79 (test) | allowed and logged; u0002 is excluded from every pool and metric |
| d5 | replacement text `Work is fine, mostly.` is added to c0001 as u0004, without a restart | a post-M0 addition outside reserve activation | **S13** |
| d6 | a unit committed as NFC `I skipped lunch at the café.` (28 characters, 29 bytes, `4f866ee2b56198cb3a95c7cc5af3d454261007bd765347ee141761f648469a6b`) is delivered in NFD (29 characters, 30 bytes) | `dfb0adb59cf1828cd4a92ad79dde56771375102283b9bd8df08ef42d85005103` ≠ M0 entry | **S13**; renormalizing is not a defense |

**d7 — the restart window.** The original M0 is committed at 2026-10-01T00:00:00Z, so the original R\* is round 6515606, released at 2026-10-02T00:00:00Z (§R5c).

| Restart notice (Issue #3 server time) | Strictly before 2026-10-02T00:00:00Z? | Result |
| --- | --- | --- |
| 2026-10-01T18:00:00Z | yes | restart permitted |
| 2026-10-01T23:59:59Z | yes | restart permitted |
| 2026-10-02T00:00:00Z | no (equal) | no restart: removal (X1–X5) or halt (S13) |
| any later time, for example after annotation, RS gates or G4 | no | no restart: removal or halt |

**d8 — a permitted restart.**

- **Notice:** posted at 2026-10-01T18:00:00Z, listing u0002, with the operator's authorization.
- **Replacement:** u0002 is replaced by a **new** unit u0004, `Work is fine, mostly.` (`98292a0d973721657c4ab6e7d713fedeb261191334ecad4d809666c75dfeddaa`).
- **New round:** the restart M0 is committed at 2026-10-01T20:00:00Z. The new R\* is round 6518006, released at 2026-10-02T20:00:00Z, exactly the target. Round 6515606 is never used to derive a salt.

Restart M0 bytes (252 bytes, same format):

```text
c0001\tmain\tactive\tu0001:4ba87bfbee1ac8dc01d8057470673a2da8ec89f7248b31ded4319c3961c1b7ed,u0004:98292a0d973721657c4ab6e7d713fedeb261191334ecad4d809666c75dfeddaa\n
c0002\tmain\treserve:1\tu0003:fcd695727597a17a40bcb2f2477c68358cbc5466c8b18ddca3aa74ea66e62eab\n
```

- Restart M0 hash: `ea40007438d7aaaa8cef8b02e6ac7ffd192b3032baf347216a9dbcd3b060d643`.
- The new round's reference randomness is 64 × `1` (**not** a real drand value).
- Salt = SHA-256(`"e001-salt-v1:" + restart_M0_hash + ":" + randomness`) = `728f10636274d658d6ecfdf5f82c505cec316fa217cd57458a50e7ce7202f9cd`.

| cluster_id | First 8 hex | int | b | Bucket (main) |
| --- | --- | --- | --- | --- |
| c0001 | dced2f5a | 3706531674 | 74 | test |
| c0002 | a4173089 | 2752983177 | 77 | test, if activated |

- The restart M0 may differ from the superseded M0 only in u0002, the unit the notice listed. Any other difference is S13.
- This is the only split this experiment ever draws. No salt was derived for the superseded M0.

**d9 — after the salt round.** A second restart, a notice after the original R\* release, or a need for new text after the salt round → **no re-randomization**. The unit is removed (X1–X5), or the experiment halts (S13). New text needs a new protocol version with a genuinely new locked test set.

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

## R8 — Escalation trigger and deficit attribution (dev only; protocol §12.3)

**Rule.** Escalate from rung r iff:

- **(a)** some checked metric is short: M^best(r) < τ_M; and
- **(b)** for **every** short metric:
  - **closure:** M^NCM ≥ τ_M;
  - **dominance:** gain_NCM ≥ gain_other.

**Settings (all cases):**

- δ_Q = 0.04 and δ_S = 0.05.
- Designated control configurations (one per control), dev Q: B0 0.64, C_A 0.66, C_B 0.70. So τ_Q = 0.70 − 0.04 = **0.66**.
- The same configurations' dev S: B0 0.62, C_A 0.66, C_B 0.70. So τ_S = 0.70 − 0.05 = **0.65**.
- Inputs are given per metric. A short metric gets its full error breakdown on φ_M(r); a metric that is not short gets only its best value. The cases test the rule's arithmetic.
- **Category abbreviations:** NCM = `NO_CANDIDATE_MENTION`, MP = `MENTION_PRESENT`, NGS = `NO_GOLD_SPAN`, NO = `NO_OUTPUT`.
- **Correcting** an error pair sets its prediction to gold: a false negative becomes a true positive, and a false positive becomes a true negative.

### R8a — Q inputs (two dimensions, 100 gold-E pairs each)

| Case | Dim | TP | FN (NCM / MP) | FP (NGS / MP) | F1 | F1, NCM corrected | F1, all other errors corrected |
| --- | --- | --- | --- | --- | --- | --- | --- |
| e1 | EXH | 50 | 50 (42 / 8) | 12 (8 / 4) | 50/81 = 0.61728 | 46/51 = 0.90196 | 58/79 = 0.73418 |
| e1 | SCD | 60 | 40 (32 / 8) | 14 (10 / 4) | 20/29 = 0.68966 | 92/103 = 0.89320 | 17/21 = 0.80952 |
| e2 | EXH | 70 | 30 (24 / 6) | 60 (48 / 12) | 14/23 = 0.60870 | 94/127 = 0.74016 | 19/22 = 0.86364 |
| e2 | SCD | 72 | 28 (22 / 6) | 50 (40 / 10) | 24/37 = 0.64865 | 47/61 = 0.77049 | 78/89 = 0.87640 |
| e3a | EXH | 56 | 44 (22 / 22) | 24 (14 / 10) | 28/45 = 0.62222 | 78/101 = 0.77228 | 78/89 = 0.87640 |
| e3a | SCD | 60 | 40 (20 / 20) | 22 (14 / 8) | 60/91 = 0.65934 | 80/101 = 0.79208 | 8/9 = 0.88889 |
| e3b | EXH | 37 | 63 (53 / 10) | 90 (80 / 10) | 74/227 = 0.32599 | 9/14 = 0.64286 | 94/147 = 0.63946 |
| e3b | SCD | 36 | 64 (54 / 10) | 88 (78 / 10) | 9/28 = 0.32143 | 90/139 = 0.64748 | 46/73 = 0.63014 |

| Input | Q^best | Q^NCM | Q^other | gain_NCM | gain_other | Closure | Dominance | v1.1 share (NCM among false negatives only) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e1 | 0.65347 | 0.89758 | 0.77185 | 0.24411 | 0.11838 | yes | yes | 74/90 = 82.2 % |
| e2 | 0.62867 | 0.75532 | 0.87002 | 0.12665 | 0.24135 | yes | **no** | 46/58 = 79.3 % |
| e3a | 0.64078 | 0.78218 | 0.88265 | 0.14140 | 0.24187 | yes | **no** | 42/84 = 50.0 % |
| e3b | 0.32371 | 0.64517 | 0.63480 | 0.32146 | 0.31109 | **no** (0.64517 < 0.66) | yes | 107/127 = 84.3 % |

### R8b — S inputs (pooled pairs, 800 per case)

Rows are gold classes and columns are predicted classes. Off-diagonal cells show their error categories.

**e5:**

| Gold \ predicted | E | CON | IND | NA | `NONE_OUTPUT` |
| --- | --- | --- | --- | --- | --- |
| E (200) | 102 | 4 MP | 6 MP | 88 (NCM 80, MP 8) | 0 |
| CON (100) | 6 MP | 38 | 4 MP | 52 (NCM 46, MP 6) | 0 |
| IND (100) | 6 MP | 4 MP | 34 | 56 (NCM 50, MP 6) | 0 |
| NA (400) | 20 NGS | 6 NGS | 10 NGS | 362 | 2 NO |

**e6:**

| Gold \ predicted | E | CON | IND | NA | `NONE_OUTPUT` |
| --- | --- | --- | --- | --- | --- |
| E (200) | 120 | 10 MP | 16 MP | 54 (NCM 14, MP 40) | 0 |
| CON (100) | 14 MP | 48 | 8 MP | 30 (NCM 8, MP 22) | 0 |
| IND (100) | 16 MP | 8 MP | 44 | 32 (NCM 8, MP 24) | 0 |
| NA (400) | 40 NGS | 10 NGS | 20 NGS | 330 | 0 |

| Input | Computation | F1_E | F1_CON | F1_IND | F1_NA | S |
| --- | --- | --- | --- | --- | --- | --- |
| e5 | as predicted | 102/167 | 1/2 | 34/77 | 362/479 | **0.57702** |
| e5 | NCM corrected | 182/207 | 28/33 | 14/17 | 362/391 | 0.86927 |
| e5 | all other errors corrected | 3/4 | 54/77 | 2/3 | 50/61 | 0.73441 |
| e6 | as predicted | 8/13 | 6/11 | 22/47 | 110/141 | **0.60227** |
| e6 | NCM corrected | 67/101 | 14/23 | 26/49 | 55/68 | 0.65287 |
| e6 | all other errors corrected | 186/193 | 23/24 | 23/24 | 80/83 | 0.96106 |

- **e5:** gain_NCM = 0.29225 ≥ gain_other = 0.15739, and closure holds (0.86927 ≥ 0.65).
- **e6:** closure holds (0.65287 ≥ 0.65), but gain_NCM = 0.05061 < gain_other = 0.35880, so dominance fails.

### R8c — Decisions

| Case | Rung | G5 | Q input | S input | Short on | (b) for each short metric | Decision | v1.1 decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e1 | T0 | passed | R8a e1 | best 0.68 | Q | Q: both hold | **escalate to T1**: missing mentions are the dominant, closable deficit | escalate |
| e2 | T0 | passed | R8a e2 | best 0.68 | Q | Q: dominance fails | **refused**: false positives and qualifier errors dominate, with few missing mentions; revise T0 within the caps | escalate (79.3 %) |
| e3a | T0 | passed | R8a e3a | best 0.68 | Q | Q: dominance fails | **refused**: a mixed deficit whose mention share is below the other errors' | escalate (50.0 %) |
| e3b | T0 | passed | R8a e3b | best 0.68 | Q | Q: closure fails | **refused**: even perfect mention coverage leaves Q short of 0.66 | escalate (84.3 %) |
| e4 | T0 | passed | best 0.66 | best 0.66 | none (0.66 is not < 0.66; 0.66 is not < 0.65) | — | **T0 final**: competent T0, no learned target | T0 final |
| e5 | T0 | passed | best 0.68 | R8b e5 | S | S: both hold | **escalate to T1** | — |
| e6 | T0 | passed | best 0.68 | R8b e6 | S | S: dominance fails | **refused** | — |
| e7 | T0 | **failed** | best 0.68 | R8b e6 (not used) | none | — | **T0 final**: S is not checked after a G5 failure | T0 final |
| e8 | T0 | passed | R8a e1 | R8b e6 | Q, S | Q: both hold; S: dominance fails | **refused**: (b) must hold for every short metric | — |
| e9 | T2 | passed | R8a e1 | best 0.68 | Q | Q: both hold | **no further rung**: T2 is the maximum; T2 is designated and evaluated | same |

The "—" entries in the v1.1 column are cases that use v1.2's new S inputs and have no v1.1 counterpart.

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
| Record whose `input_sha256` differs from the unit's M0 hash | the unit becomes `ERROR`, as above, and the event is logged. If the text the custodian delivered itself mismatches M0, that is S13 (§R5d). |

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

## R12 — Bootstrap semantics (protocol §14.3)

### R12a — Resampling draws

The draw rule is `i(b, j) = int(SHA-256("e001-boot-v1:20260918:" + str(b) + ":" + str(j)).hexdigest()[0:16], 16) mod n`, over the cluster list in ascending byte order.

Reference list (n = 5): [c0001, c0002, c0003, c0005, c0023]. Each cell shows the first 16 hex digits → i → cluster.

| b | j = 1 | j = 2 | j = 3 | j = 4 | j = 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | `cf17b2e0bf38c272` → 2 → c0003 | `549d225bcbe25965` → 0 → c0001 | `c4c1637c94bb81ea` → 0 → c0001 | `da5155c73dc177ac` → 3 → c0005 | `adaaa0b4a9df64a6` → 1 → c0002 |
| 2 | `36cce663c611c259` → 0 → c0001 | `62da0f0443e8bddb` → 2 → c0003 | `f6fbb1a2a4fe555a` → 4 → c0023 | `959d4f5138572817` → 2 → c0003 | `dc9ddcf1f93dfdca` → 3 → c0005 |
| 3 | `04b462d66b2eb87f` → 0 → c0001 | `0ff3aec809fe7315` → 1 → c0002 | `e3461c04fafad9fc` → 3 → c0005 | `bfeedb87b8430ad0` → 2 → c0003 | `e4e240da0a16e9ff` → 1 → c0002 |

**Replicate multisets:**

- b = 1: {c0001 × 2, c0002, c0003, c0005}. There is no c0023.
- b = 2: {c0001, c0003 × 2, c0005, c0023}.
- b = 3: {c0001, c0002 × 2, c0003, c0005}.

### R12b — Scoring a replicate: multiplicity and an absent dimension

Per-cluster counts, for two dimensions and two arms (T and comparator k). Counts are TP / FP / FN.

| Cluster | EXH gold-E | T EXH | k EXH | SCD gold-E | T SCD | k SCD | T claims / verified | k claims / verified |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| c0001 | 2 | 2 / 0 / 0 | 1 / 1 / 1 | 0 | 0 / 0 / 0 | 0 / 1 / 0 | 2 / 2 | 3 / 1 |
| c0002 | 1 | 0 / 1 / 1 | 1 / 0 / 0 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 1 / 0 | 1 / 0 |
| c0003 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 | 0 / 1 / 0 | 0 / 0 / 0 | 1 / 0 | 0 / 0 |
| c0005 | 1 | 1 / 0 / 0 | 0 / 0 / 1 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 1 / 1 | 0 / 0 |
| c0023 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 2 | 1 / 0 / 1 | 2 / 0 / 0 | 1 / 1 | 2 / 1 |

| Sample | Q_T | Q_k | Q_T − Q_k | R_T | R_k | EVCP_T | EVCP_k | EVCP_T − EVCP_k |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| full | 5/8 | 24/35 | −17/280 | 5/8 | 3/4 | 2/3 | 1/3 | 1/3 |
| b = 1 (SCD absent) | 5/6 | 6/11 | **19/66** = 0.28788 | 5/6 | 1/2 | 5/7 | 2/7 | 3/7 |
| b = 2 | 7/10 | 3/5 | 1/10 | 3/4 | 2/3 | 2/3 | 2/5 | 4/15 |

- **b = 1:** no drawn cluster has gold-E for SCD, so SCD is omitted from Q and R **for both arms**. Q is EXH alone.
- **Defect:** omitting a dimension only when TP = FP = FN = 0 would keep SCD in b = 1, because T and k both have SCD false positives. Each arm's SCD F1 would be 0, giving Q_T = 5/12, Q_k = 3/11 and a difference of 19/132 = 0.14394, half the correct value.
- **EVCP has no omission.** Every claim counts, including SCD claims in a replicate where SCD is absent from Q.

### R12c — An absent class in S

Four pairs. Gold: E, E, NA, NA. T predicts E, IND, NA, NA. k predicts E, E, NA, NA.

- Classes with gold: E and NA. IND has no gold, so it is omitted **for both arms**, even though T predicted it.
- T: F1_E = 2/3 and F1_NA = 1, so S_T = **5/6**. k: S_k = 1. The difference is −1/6.
- T's IND prediction still costs it: it is a false negative for E.
- **Defect:** including IND for T because T predicted it gives S_T = (2/3 + 1 + 0)/3 = 5/9, while k averages over {E, NA}. The arms would then be scored on different class sets.

### R12d — Order statistics and undefined replicates

m = ⌊0.025·B⌋. The lower bound is the (m+1)-th smallest value of v⁻, and the upper bound is the (B−m)-th smallest value of v⁺. An undefined difference enters v⁻ as −1 and v⁺ as +1.

| B | m | Lower bound | Upper bound |
| --- | --- | --- | --- |
| 10,000 | 250 | 251st smallest | 9,750th smallest |
| 40 | 1 | 2nd smallest | 39th smallest |
| 20 | 0 | minimum | maximum |

**P-SUP cases (δ_P = 0.10, B = 40):**

| Case | Replicate differences | Lower (v⁻) | Upper (v⁺) | Component |
| --- | --- | --- | --- | --- |
| u1 | 39 defined: 0.105, 0.110, …, 0.295 (step 0.005); 1 undefined (T made no claims) | 0.105 | 0.295 | **PASS** |
| u2 | 38 defined: 0.105, …, 0.290; 2 undefined (one T with no claims, one comparator with no claims) | −1 | +1 | **UNDECIDED** (2 > m = 1) |
| u3 | 39 defined: 0.000, 0.002, …, 0.076; 1 undefined | 0.000 | 0.076 | **FAIL** (0.076 < 0.10) |
| u4 | 38 defined: 0.000, …, 0.074; 2 undefined | −1 | +1 | **UNDECIDED** |

- Undefined replicates only ever widen the interval. They can produce neither a PASS nor a FAIL.
- **Interpolation defect:** for u1, linear interpolation at 2.5 % on v⁻ gives 0.025 × (−1) + 0.975 × 0.105 = 0.077375, which is UNDECIDED. The frozen rule gives PASS. Any interpolated percentile is a defect.

### R12e — Full-sample EVCP dispositions (P-SUP against g)

| T's claims | g's claims | Disposition | R4 case |
| --- | --- | --- | --- |
| 0 | 12 | **FAIL**, with no bootstrap | O |
| 0 | 0 | **FAIL**: T's zero takes precedence | — |
| 150 | 0 | **UNDEFINED**, with no bootstrap; blocks `supported` | P, V |
| 150 | 140 | bootstrap, per R12a–R12d | A |

### R12f — Exact arithmetic at a margin boundary

- **Case:** the bounding replicate for Q-NI has Q_T = 33/100 and Q_k = 36/100, with δ_Q = 0.030.
- **Exact:** the difference is −3/100 = −δ_Q, which is not > −δ_Q. The component is **UNDECIDED** (§R4, case W).
- **Defect:** IEEE-754 doubles give 0.33 − 0.36 = −0.02999999999999997, which is > −0.03, a false PASS. Floating-point comparison against a margin is a defect.

## R13 — Rule J configuration selection (protocol §11.1)

**Settings:** δ_Q = 0.030 and δ_S = 0.050, and G5 passed. Every configuration listed passes sanity gates (a)–(d). The dev values are exact.

**Rule:**

1. **Per-metric anchors:** Q^max, S^max and R^max, each the maximum over all configurations. They may come from different configurations.
2. **Joint envelope:** Q ≥ Q^max − 0.030, S ≥ S^max − 0.050 and R ≥ R^max − 0.030.
3. **Non-empty envelope:** designate its highest-ranked configuration. The criterion is EVCP for C_A, C_B and T, and dev Q for B0.
4. **Empty envelope:** a control gets the designated set {φ\*_Q, φ\*_S, φ\*_R}, one per single-metric envelope. T and S-H2A get φ\*_Q.

### R13a — C_A (model × prompt)

| Config | Ledger # | Model / prompt | dev Q | dev S | dev R | dev EVCP |
| --- | --- | --- | --- | --- | --- | --- |
| φ1 | 3 | Qwen3.5-9B / P1 | 0.720 | 0.600 | 0.700 | 0.550 |
| φ2 | 4 | gemma-4-12B-it / P1 | 0.700 | 0.590 | 0.690 | 0.800 |
| φ3 | 5 | Phi-4-mini / P2 | 0.650 | 0.560 | 0.640 | 0.900 |
| φ4 | 6 | Qwen3.5-9B / P2 | 0.715 | 0.520 | 0.710 | 0.820 |

1. **Anchors:** Q^max = 0.720 (φ1), S^max = 0.600 (φ1) and R^max = 0.710 (φ4).
2. **Envelope:** Q ≥ 0.690, S ≥ 0.550 and R ≥ 0.680, which gives {φ1, φ2}. φ3 is out on Q (0.650), and φ4 is out on S (0.520).
3. **Designated:** φ2, with EVCP 0.800 against φ1's 0.550.

**Contrast.** Selecting by dev Q alone would designate φ1, whose EVCP is 0.250 lower. A T with dev EVCP 0.70 would clear δ_P against φ1 (by 0.15) but not against φ2 (by −0.10). Rule J blocks that manufactured P-SUP.

### R13b — The re-audit's counterexample (A6)

| Config | dev Q | dev S | dev R | dev EVCP |
| --- | --- | --- | --- | --- |
| φ1 | 0.800 | 0.500 | 0.800 | 0.600 |
| φ2 | 0.790 | 0.800 | 0.800 | 0.800 |
| φ3 | 0.790 | 0.510 | 0.800 | 0.900 |

- **v1.2 rule (anchored on the Q-best configuration, φ1):** the S bound is 0.500 − 0.050 = 0.450, so all three enter. φ3 is designated, with S = 0.510, while φ2's S = 0.800 disappears. This is a **defect**.
- **v1.3 rule (independent anchors):** Q^max = 0.800, S^max = 0.800 and R^max = 0.800. The envelope (Q ≥ 0.770, S ≥ 0.750, R ≥ 0.770) is {φ2}, so **φ2** is designated.

### R13c — C_B (hyperparameters × seed)

| Config | Ledger # | (hyperparameters, seed) | dev Q | dev S | dev R | dev EVCP |
| --- | --- | --- | --- | --- | --- | --- |
| κ1 | 1 | (h1, 1) | 0.700 | 0.600 | 0.690 | 0.700 |
| κ2 | 2 | (h2, 1) | 0.710 | 0.610 | 0.700 | 0.720 |
| κ3 | 3 | (h3, 1) | 0.690 | 0.580 | 0.680 | 0.760 |
| κ4 | 4 | (h3, 2) | 0.705 | 0.600 | 0.695 | 0.740 |
| κ5 | 5 | (h3, 3) | 0.675 | 0.570 | 0.665 | 0.790 |

1. **First application, over κ1–κ3:** the anchors are Q^max = 0.710, S^max = 0.610 and R^max = 0.700, all from κ2. The envelope (Q ≥ 0.680, S ≥ 0.560, R ≥ 0.670) is {κ1, κ2, κ3}. κ3 has the highest EVCP, so the leading hyperparameters are h3, and seeds 2 and 3 of h3 are trained (κ4, κ5).
2. **Second application, over κ1–κ5:** the anchors are unchanged, so the envelope is the same. κ5 is out on Q (0.675) and R (0.665), which leaves {κ1, κ2, κ3, κ4}. The designated configuration is **κ3** (EVCP 0.760).

### R13d — An empty envelope gives a designated set (C_A)

| Config | Ledger # | dev Q | dev S | dev R | dev EVCP |
| --- | --- | --- | --- | --- | --- |
| ψ1 | 1 | 0.760 | 0.560 | 0.760 | 0.700 |
| ψ2 | 2 | 0.700 | 0.680 | 0.700 | 0.750 |
| ψ3 | 3 | 0.750 | 0.600 | 0.755 | 0.780 |
| ψ4 | 4 | 0.705 | 0.670 | 0.690 | 0.820 |

1. **Anchors:** Q^max = 0.760, S^max = 0.680 and R^max = 0.760.
2. **Joint envelope** (Q ≥ 0.730, S ≥ 0.630, R ≥ 0.730): **empty**. ψ1 and ψ3 fail on S; ψ2 and ψ4 fail on Q.
3. **Single-metric envelopes:**
   - E_Q = {ψ1, ψ3}, so φ\*_Q = ψ3 (EVCP 0.780);
   - E_S = {ψ2, ψ4}, so φ\*_S = ψ4 (EVCP 0.820);
   - E_R = {ψ1, ψ3}, so φ\*_R = ψ3.
4. **Designated set:** {ψ3, ψ4}. Both are comparators in K and G and face every component (§R4, case N).
5. **Primary:** ψ3. It runs every locked pool; ψ4 runs the locked main test only.

### R13e — B0 under rule J (criterion: dev Q)

| Case | TF-IDF logistic regression (Q / S / R) | NB-SVM (Q / S / R) | Envelope | Designated B0 |
| --- | --- | --- | --- | --- |
| b1 | 0.640 / 0.400 / 0.620 | 0.630 / 0.550 / 0.640 | Q ≥ 0.610, S ≥ 0.500, R ≥ 0.610 → {NB-SVM} | **NB-SVM**. Selecting by Q alone would pick the S-weak TF-IDF model. |
| b2 | 0.640 / 0.540 / 0.620 | 0.630 / 0.550 / 0.640 | both | **TF-IDF logistic regression** (higher Q) |
| b3 | 0.640 / 0.400 / 0.640 | 0.580 / 0.550 / 0.580 | empty | **both**: the set {TF-IDF logistic regression (φ\*_Q, φ\*_R), NB-SVM (φ\*_S)} |

B0's EVCP plays no role in any case.

### R13f — T with an empty envelope

T's configurations are θ1 (Q 0.700, S 0.500, R 0.700, EVCP 0.850) and θ2 (Q 0.600, S 0.620, R 0.600, EVCP 0.900).

- The anchors are 0.700 / 0.620 / 0.700. The joint envelope is empty: θ1 fails on S (0.500 < 0.570), and θ2 fails on Q.
- T gets a **single** designation, φ\*_Q = θ1. T's choice can only affect T, so no set is formed.

### R13g — Tie-breaks and edge cases

| Case | Situation | Result |
| --- | --- | --- |
| t1 | Two envelope configurations have EVCP 160/200 and 4/5 (exactly equal), with dev Q 0.705 and 0.700 | the one with Q 0.705 |
| t2 | Equal EVCP, Q, S and R | the earlier ledger entry |
| t3 | A configuration makes zero dev E claims | its EVCP is undefined, and it ranks below every defined value |
| t4 | A designated configuration fails reproducibility (gate e) | it is removed from Φ and J is re-applied from step 1 |
| t5 | Φ is empty after removals | §11 item 7: the fallback model, else halt |
| t6 | A designated set's extra locked main-test runs cannot fit the arm's §15.1 cap | S7 (resource halt); no member is dropped to fit |
