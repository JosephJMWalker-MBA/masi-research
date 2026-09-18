# WP1 observed results — 2026-09-17

**Reconciled result (R5):** under `wp1-support-v1`, three pre-registered implementations — a deterministic equality floor (`INFRASTRUCTURE`/B0) and two externally adapted pretrained transformer classifiers (`CONTROL_B`-class specimens) — ran through one caller with uniform invocation, changing only the candidate identifier, and reproduced bit-identically on one host. Normalization into the common envelope is caller-resident and candidate-keyed, so substitution is demonstrated for a closed registered set, not for arbitrary new implementations or purpose-built targets with different native ontologies. The protocol's inference-branching failure condition was not triggered; the contract's broader caller-branch condition is met only for invocation, not normalization. This supersedes the original blanket "gate passed" interpretation; no H1–H7 effect is established.

This non-frozen document is reconciled from the historical version at `81adfff` onto governing `main` at `a0ac9fe9cd400a6c03d6543d5b79f651bf89a3a5`. The [independent audit](../../docs/AUDIT_WP0_WP1_2026-09-17.md) returned `CLAIM_NARROWING_REQUIRED`. Its implementation and evidence findings survive unchanged. This documentation-only branch does not contain or merge the builder's code, frozen contract or evidence; links below identify that immutable packet. No new execution is reported here. Scoped Claude re-check remains next.

**Thesis supersession (R2):** the frozen `wp1-support-v1` H1–H7 matrix is WP1-local and superseded for thesis purposes by current [RESEARCH_THESIS.md](../../docs/RESEARCH_THESIS.md): H2A adaptation value, H2B purpose-built specialization value, `C_A/C_B/T` controls and falsifiers 1–10 govern. The WP0 thesis-freeze deliverable remains open under Issue #1. The frozen interface contract is unchanged; neither these externally adapted specimens nor WP1's comparisons establish H2A or H2B.

## Evidence and protocol identity

- Freeze: `wp1-support-v1`, first committed at `25638aea30bda4b4a5ef9fb0dd8e5193a578a584`. The [freeze manifest](https://github.com/JosephJMWalker-MBA/masi-research/blob/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/experiments/wp1/freeze.json) retains file hashes and its pre-observation timestamp. The contract, fixtures, candidate adapter and dependency lock have not changed since that freeze.
- Initial invocation source: `5888d2c` (path-test repair only after the freeze). Six original runs remain under [evidence](https://github.com/JosephJMWalker-MBA/masi-research/tree/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/experiments/wp1/evidence), with [verification-initial.json](https://github.com/JosephJMWalker-MBA/masi-research/blob/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/experiments/wp1/evidence/verification-initial.json).
- Final invocation source: `7adfeb9ef5ce928d0ba1568d33d3702694d2f63f`. Six additional runs are under [evidence/accounting-repair](https://github.com/JosephJMWalker-MBA/masi-research/tree/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/experiments/wp1/evidence/accounting-repair). A reviewer found and the builder repaired loss of already-reported call counts on normalization errors. This changes failure accounting, not inputs, thresholds, candidate code or verdict mapping. No initial observations were overwritten.
- [Final verification](https://github.com/JosephJMWalker-MBA/masi-research/blob/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/experiments/wp1/evidence/accounting-repair/verification.json) checks file hashes, raw/input linkage, complete fixture rows, normalization, same caller/adapter bytes, model artifacts, environment and numerical reproduction within the frozen absolute tolerance `1e-6`.

## Observations

Each cell below describes one 12-fixture run; the second final run has identical native outputs and decisions.

| Implementation | Implementation class | Model class / parameters | Reference matches / all fixtures | Answered | Abstained | Errors | Model calls |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `exact-match-v1` | `INFRASTRUCTURE` (B0 evaluation floor) | Deterministic equality / 0 | 3 / 12 | 3 | 9 | 0 | 0 |
| `hhem-2.1` | `CONTROL_B`-class specimen, externally adapted; adapter `INFRASTRUCTURE` | T5 encoder consistency verifier / 109,630,082 | 12 / 12 | 12 | 0 | 0 | 12 |
| `nli-deberta-small` | `CONTROL_B`-class specimen, externally adapted; adapter `INFRASTRUCTURE` | DeBERTa NLI classifier / 141,897,219 | 12 / 12 | 12 | 0 | 0 | 12 |

See [implementation classes](IMPLEMENTATION_CLASSES.md) for the complete R1 artifact table and specialist-gate record. No `MASI_TARGET` or `CONTROL_A` was observed.

**No demonstrated capability deficit (R4):** WP1 establishes no capability deficit for transparent or rule-based Precision approaches. `exact-match-v1` is a floor, not a competitive transparent baseline, and the 12/12 learned counts do not justify learned complexity. The fixtures were visible and author-created with candidates known; their canonical NLI phenomena overlap the NLI specimen's documented training mixture (audit N7). This contamination risk rules out a capability interpretation of these counts.

Abstentions count as unmatched in the all-fixture denominator. The baseline makes no negative judgment on the other nine cases. `not_supported` does not distinguish insufficient evidence from contradiction; native NLI scores preserve that distinction. Learned scores remain uncalibrated and must not be averaged or ranked as comparable probabilities.

All three final repeat pairs had maximum absolute native-output difference **0** and identical normalized decisions. Across initial and final run sets, 12 runs preserve 144 fixture records and 96 learned forward calls, with no candidate execution errors. The additional set verifies the resource-accounting repair; it is not an independent dataset replication.

## Resource observations

Host preflight: Darwin arm64, 16 GiB memory, 10 logical CPUs; Python 3.11.15, torch 2.8.0, transformers 4.57.6. The [dependency lock](https://github.com/JosephJMWalker-MBA/masi-research/blob/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/requirements-probe.lock) and each run manifest preserve the full package environment. Inference used one CPU intra/inter-op thread, float32, batch one, seed zero, deterministic algorithms, one call per learned fixture, no retrieval, tools, retries, truncation or quantization.

| Implementation | Final run load time range | Median invocation time range | Process lifetime peak RSS range | Total input tokens per 12 fixtures |
| --- | --- | --- | --- | --- |
| Baseline | under 0.001 s | approximately 0.00001 s | 25.6–25.8 MiB | Not applicable |
| HHEM | 1.570–2.956 s | 0.02009–0.02066 s | 738.1–757.5 MiB | 439 |
| NLI | 1.820–1.826 s | 0.01667–0.01745 s | 937.8–1002.7 MiB | 215 |

These are descriptive sequential measurements, not a controlled efficiency benchmark. Load time includes file integrity checks and imports; invocation includes tokenization. RSS is process high-water memory including model load, not isolated inference allocation. Model-specific formatting changes token counts despite identical textual evidence. Energy, amortized hardware cost and cross-platform behavior remain unmeasured. Downloaded artifacts total 1,020,544,559 bytes, below the declared 3 GiB storage budget; no weights are committed.

## Verification, negative paths and warnings

- **22 unit tests pass**, using stdlib and fake classifiers; see [test log](https://github.com/JosephJMWalker-MBA/masi-research/blob/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/experiments/wp1/evidence/tests-22.log). Tests cover invalid/duplicate fixtures, token bounds without truncation, threshold ties and nonfinite scores, unknown/missing/changed model artifacts, frozen-file changes, labels excluded from inference, evidence linkage, overwrite refusal, load/invocation/normalization errors, and resource accounting.
- The repeat/integrity checker passed on both six-run sets. Dependency consistency and compilation checks passed. No hosted CI or different-host reproduction has run.
- An initial macOS temporary-path alias assertion failed and was corrected before model runs. During the later test edit, an indentation error was caught and fixed before the passing suite and final invocation source were committed. These were implementation/test failures, not candidate performance observations.
- The initial package fetch was blocked by sandbox network resolution; an authorized network retry completed. No restricted inference service was called.
- Pinned HHEM emits an upstream `HHEMv2Config` / `HHEMv2` naming warning; transformers emits a `torch_dtype` deprecation warning. Both are retained in [the final inference log](https://github.com/JosephJMWalker-MBA/masi-research/blob/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/experiments/wp1/evidence/accounting-repair/inference.log). They did not prevent execution. Dependency upgrades are unverified; do not silently change the lock.

## Interpretation and remaining uncertainty

The two learned candidates differ in architecture and training objective only: both share one Hugging Face/transformers/PyTorch softmax-classifier stack and one adapter class. The 512-token limit and caller-resident score mapping are WP1-local couplings, not a general Precision contract. Closed-set selection here does not validate the four-responsibility architecture, cross-paradigm interchangeability or a `MASI_TARGET`. The visible, synthetic fixtures provide no independently reviewed held-out quality estimate; their NLI contamination risk (N7) rules out capability conclusions. There is no MASI training, router, consensus policy, outcome learner or general runtime.

The freeze guard covers its explicitly listed files. `probe.py` is recorded by per-run source hash and Git commit, rather than included in that selected-file guard. Output-mapping semantics remain frozen in the contract/protocol; the verifier recomputes them. Future implementation changes require their own recorded source and verification, and changed experiment criteria require a new version retaining this evidence.

The historical supporting same-family review was not the independent audit. Claude subsequently audited the frozen packet and returned `CLAIM_NARROWING_REQUIRED`; code and evidence require no repair. R1–R7 are documentation-only corrections submitted for a scoped Claude re-check. Issue #1's WP0 thesis-freeze deliverable stays open; Issue #2 remains broader than this interface and Issue #4 broader than WP1. E001 concerns a purpose-built bounded Empathy-observation target; any base selection or fine-tuning is an optional `CONTROL_B` arm. E001 work remains unauthorized here.

**E1 — next-contract lesson, not a WP1 repair:** the verifier imports normalization and hashing helpers from the runner. It checks integrity and drift but is not independent validation of those helpers. The audit independently checked the mapping and upstream behavior. A future separately authorized contract may add an independent reference table or verifier; no current code, evidence, contract or evaluator change follows from E1.
