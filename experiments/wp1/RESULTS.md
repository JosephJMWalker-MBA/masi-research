# WP1 observed results — 2026-09-17

**Result:** the frozen bounded interchangeability engineering gate passed locally. A deterministic baseline, HHEM and DeBERTa NLI ran through the same caller, and each reproduced its native outputs and normalized decisions under the same conditions. This supports only an executable seam underlying H4. It does not establish useful MASI composition, specialization gains, calibration, generalization or superiority.

## Evidence and protocol identity

- Freeze: `wp1-support-v1`, first committed at `25638aea30bda4b4a5ef9fb0dd8e5193a578a584`. The [freeze manifest](freeze.json) retains file hashes and its pre-observation timestamp. The contract, fixtures, candidate adapter and dependency lock have not changed since that freeze.
- Initial invocation source: `5888d2c` (path-test repair only after the freeze). Six original runs remain under [evidence](evidence/), with [verification-initial.json](evidence/verification-initial.json).
- Final invocation source: `7adfeb9ef5ce928d0ba1568d33d3702694d2f63f`. Six additional runs are under [evidence/accounting-repair](evidence/accounting-repair/). A reviewer found and the builder repaired loss of already-reported call counts on normalization errors. This changes failure accounting, not inputs, thresholds, candidate code or verdict mapping. No initial observations were overwritten.
- [Final verification](evidence/accounting-repair/verification.json) checks file hashes, raw/input linkage, complete fixture rows, normalization, same caller/adapter bytes, model artifacts, environment and numerical reproduction within the frozen absolute tolerance `1e-6`.

## Observations

Each cell below describes one 12-fixture run; the second final run has identical native outputs and decisions.

| Implementation | Class / parameters | Reference matches / all fixtures | Answered | Abstained | Errors | Model calls |
| --- | --- | --- | --- | --- | --- | --- |
| `exact-match-v1` | Deterministic equality / 0 | 3 / 12 | 3 | 9 | 0 | 0 |
| `hhem-2.1` | T5 encoder consistency verifier / 109,630,082 | 12 / 12 | 12 | 0 | 0 | 12 |
| `nli-deberta-small` | DeBERTa NLI classifier / 141,897,219 | 12 / 12 | 12 | 0 | 0 | 12 |

Abstentions count as unmatched in the all-fixture denominator. The baseline makes no negative judgment on the other nine cases. `not_supported` does not distinguish insufficient evidence from contradiction; native NLI scores preserve that distinction. Learned scores remain uncalibrated and must not be averaged or ranked as comparable probabilities.

All three final repeat pairs had maximum absolute native-output difference **0** and identical normalized decisions. Across initial and final run sets, 12 runs preserve 144 fixture records and 96 learned forward calls, with no candidate execution errors. The additional set verifies the resource-accounting repair; it is not an independent dataset replication.

## Resource observations

Host preflight: Darwin arm64, 16 GiB memory, 10 logical CPUs; Python 3.11.15, torch 2.8.0, transformers 4.57.6. The [dependency lock](../../requirements-probe.lock) and each run manifest preserve the full package environment. Inference used one CPU intra/inter-op thread, float32, batch one, seed zero, deterministic algorithms, one call per learned fixture, no retrieval, tools, retries, truncation or quantization.

| Implementation | Final run load time range | Median invocation time range | Process lifetime peak RSS range | Total input tokens per 12 fixtures |
| --- | --- | --- | --- | --- |
| Baseline | under 0.001 s | approximately 0.00001 s | 25.6–25.8 MiB | Not applicable |
| HHEM | 1.570–2.956 s | 0.02009–0.02066 s | 738.1–757.5 MiB | 439 |
| NLI | 1.820–1.826 s | 0.01667–0.01745 s | 937.8–1002.7 MiB | 215 |

These are descriptive sequential measurements, not a controlled efficiency benchmark. Load time includes file integrity checks and imports; invocation includes tokenization. RSS is process high-water memory including model load, not isolated inference allocation. Model-specific formatting changes token counts despite identical textual evidence. Energy, amortized hardware cost and cross-platform behavior remain unmeasured. Downloaded artifacts total 1,020,544,559 bytes, below the declared 3 GiB storage budget; no weights are committed.

## Verification, negative paths and warnings

- **22 unit tests pass**, using stdlib and fake classifiers; see [test log](evidence/tests-22.log). Tests cover invalid/duplicate fixtures, token bounds without truncation, threshold ties and nonfinite scores, unknown/missing/changed model artifacts, frozen-file changes, labels excluded from inference, evidence linkage, overwrite refusal, load/invocation/normalization errors, and resource accounting.
- The repeat/integrity checker passed on both six-run sets. Dependency consistency and compilation checks passed. No hosted CI or different-host reproduction has run.
- An initial macOS temporary-path alias assertion failed and was corrected before model runs. During the later test edit, an indentation error was caught and fixed before the passing suite and final invocation source were committed. These were implementation/test failures, not candidate performance observations.
- The initial package fetch was blocked by sandbox network resolution; an authorized network retry completed. No restricted inference service was called.
- Pinned HHEM emits an upstream `HHEMv2Config` / `HHEMv2` naming warning; transformers emits a `torch_dtype` deprecation warning. Both are retained in [the final inference log](evidence/accounting-repair/inference.log). They did not prevent execution. Dependency upgrades are unverified; do not silently change the lock.

## Interpretation and remaining uncertainty

The two learned candidates differ in architecture and training objective, but both are text classifiers implementing this single bounded responsibility. Substitution here does not validate the four-responsibility architecture. The 12 visible, synthetic, author-labeled fixtures are simple engineering cases; they provide no independently reviewed held-out quality estimate. Perfect descriptive counts are not evidence of MASI superiority. There is no MASI training, router, consensus policy, outcome learner or general runtime.

The freeze guard covers its explicitly listed files. `probe.py` is recorded by per-run source hash and Git commit, rather than included in that selected-file guard. Output-mapping semantics remain frozen in the contract/protocol; the verifier recomputes them. Future implementation changes require their own recorded source and verification, and changed experiment criteria require a new version retaining this evidence.

A supporting same-family reviewer found no blocking leakage/contract defect and accepted the bounded accounting repair after rerunning all 22 tests. This is **not** the planned independent Claude audit. Full work-packet acceptance remains pending that audit. Issues #1/#2 remain only partially frozen, Issue #4 remains broader than WP1, and E001 remains unexecuted.
