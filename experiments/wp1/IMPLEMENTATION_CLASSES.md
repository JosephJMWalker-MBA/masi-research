# WP1 implementation classes — doctrine reconciliation

**Status:** documentation-only R1 record; independent audit outcome remains `CLAIM_NARROWING_REQUIRED` pending the scoped re-check.

This record adopts the artifact classifications and specialist-gate block from the [independent audit](../../docs/AUDIT_WP0_WP1_2026-09-17.md). It reconciles their interpretation against governing `main` at `a0ac9fe9cd400a6c03d6543d5b79f651bf89a3a5`, under the [construction doctrine](../../docs/CONSTRUCTION_DOCTRINE.md) and [epistemic-integrity doctrine](../../docs/EPISTEMIC_INTEGRITY.md).

The classified packet remains on [`codex/wp0-wp1-candidate-probe` at `81adfffa2d28e4a40a0b36fe1a21baa567d402ec`](https://github.com/JosephJMWalker-MBA/masi-research/tree/81adfffa2d28e4a40a0b36fe1a21baa567d402ec). Paths below identify artifacts in that historical packet; this record does not import or alter its code, frozen files, fixtures, tests, or evidence. Classification is retrospective documentation, not newly recorded metadata in the frozen registry or run manifests.

## Artifact classifications

| Artifact | Class | Notes |
| --- | --- | --- |
| `probe.py` (fixture runner, normalizer, evidence writer) | `INFRASTRUCTURE` | Evaluation harness. Contains candidate-keyed normalization (D3). |
| `probe_candidates.py` → `CANDIDATES` table, `MODEL_FILES`, `_verify_snapshot`, `load_candidate` | `INFRASTRUCTURE` | Registry and integrity checks. Frozen. Lacks an implementation-class field (D1); this record supplies the documentary classification without changing it. |
| `probe_candidates.py` → `ExactMatch` (`exact-match-v1`) | `INFRASTRUCTURE` (evaluation floor, “B0”) | Deliberately trivial transparent floor control. **Not** `MASI_TARGET` and not a credible minimal Precision specialist: it cannot emit `not_supported`. The four-class taxonomy has no slot for a transparent non-learned baseline, although Sprint WP3 uses `B0`; this reconciliation does not add a class. |
| `probe_candidates.py` → `LocalClassifier('hhem-2.1')` wrapping Vectara HHEM-2.1-Open | Wrapped model: **`CONTROL_B`** (research specimen). Adapter code: `INFRASTRUCTURE`. | General pretrained base (FLAN-T5-base) plus third-party role-specific fine-tuning (factual-consistency classification). Externally adapted: it is not a MASI-built control and not H2A evidence, since there is no same-base comparison. Training-data lineage is not documented on the card. |
| `probe_candidates.py` → `LocalClassifier('nli-deberta-small')` wrapping `tasksource/deberta-small-long-nli` | Wrapped model: **`CONTROL_B`** (research specimen). Adapter code: `INFRASTRUCTURE`. | General pretrained encoder (DeBERTa-v3-small) plus third-party extreme multitask NLI fine-tuning (the card lists 100+ datasets). Externally adapted, and not H2A evidence. Training lineage is broad and only partly knowable. |
| `scripts/prepare_probe_models.py` | `INFRASTRUCTURE` | Pinned, bounded snapshot download plus a hash manifest. |
| `scripts/verify_probe_evidence.py` | `INFRASTRUCTURE` | Integrity and repeatability verifier. |
| `tests/test_probe.py` | `INFRASTRUCTURE` | 22 stdlib/fake tests covering contract and failure paths. |
| `requirements-probe.lock`, `.gitignore` | `INFRASTRUCTURE` | Environment pinning; weights and caches excluded. |
| `docs/WP0_WP1_CONTRACT.md` | `INFRASTRUCTURE` (experiment contract) | Envelope, abstention, resources, Bus boundary and Reality Audit minimum are valid. Its **thesis matrix is superseded** governance text (D2). |
| `experiments/wp1/{protocol.json, freeze.json, fixtures.jsonl}` | `INFRASTRUCTURE` (evaluation assets) | Frozen and unchanged since `25638ae`, as verified by the audit. |
| `experiments/wp1/evidence/**` (12 runs, logs, verification) | `INFRASTRUCTURE` outputs | Observations of one B0 floor and two `CONTROL_B` specimens. No `MASI_TARGET` was observed. |
| `experiments/wp1/{README, RESULTS, SUPPORTING_REVIEW}.md`, `docs/HANDOFF_WP1_2026-09-17.md` | Documentation (claims about `INFRASTRUCTURE` and specimens) | Subject to D1–D3 narrowing; historical handoff corrections are appended as annotations. |
| Edits to `README.md`, `STATUS.md`, `docs/{CANDIDATE_IMPLEMENTATIONS, EVALUATION, IMPLEMENTATION_SPRINT_001, MODULES, RESEARCH_THESIS}.md` | Documentation (governance and status text) | Reconciled onto current governing `main`, preserving its doctrine and hold rather than restoring the builder's superseded governance (D4). |

No `CONTROL_A` artifact and no `MASI_TARGET` artifact exists in the packet. It contains two externally adapted `CONTROL_B`-class specimens, one `INFRASTRUCTURE`/B0 floor, and supporting infrastructure and documentation. No classifier or probe becomes canonical by this classification. The WP1 invocation observation says nothing yet about purpose-built targets.

## Specialist gate for the WP1 probe

```text
responsibility:        precision.evidence_support (WP1-local, binary premise/claim support)
allowed inputs:        premise, claim (nonempty strings, ≤4,096 chars each)
native state/ontology: candidate-native (boolean equality | 2-class consistency | 3-class NLI)
outputs:               wp1-support-v1 envelope; native record kept separately
uncertainty/abstention: tie at 0.5 and over-bound input abstain; no calibration
learning/update signal: none (no training, no outcome learning)
transparent baseline:  exact-match-v1 (B0 floor; deliberately non-competitive)
why more complexity:   not established; learned candidates are specimens, not justified complexity
implementation class:  exact-match-v1 = INFRASTRUCTURE (B0 floor);
                       hhem-2.1, nli-deberta-small = CONTROL_B-class specimens (externally adapted);
                       probe layer = INFRASTRUCTURE; no MASI_TARGET exists
```

The equality floor abstains when it does not find equality; it cannot emit `not_supported`. WP1 establishes no capability deficit for transparent or rule-based Precision approaches. The floor is not a competitive transparent baseline, and results on visible, author-created fixtures do not justify learned complexity.

## Coupling and lineage limits retained from the audit

- Normalization and artifact-manifest loading are caller-resident and candidate-keyed. The normalization accepts boolean equality or a scalar support score in `[0,1]` with a `0.5` cut. Uniform invocation is demonstrated only for the closed, pre-registered candidate set, not for arbitrary implementations or targets with different native ontologies.
- Heterogeneity is in architecture and objective. Both learned specimens share HF Hub snapshots, transformers, PyTorch, subword tokenization, a softmax-classifier output shape, and one adapter class. The WP1 contract's 512-model-token bound is candidate-shaped; the NLI model itself accepts 1,680 tokens. These disclosed, WP1-local choices are not the general Precision responsibility contract.
- The audit verified the pinned cards' Apache-2.0 declarations. Training-data lineage and dataset-level licensing were not reviewed by the builder or auditor. The HHEM card does not enumerate training data, and the NLI card lists more than 100 datasets. Those limitations help explain specimen/control status; they do not establish target lineage or qualification.
- No runtime, router, service, consensus mechanism, or outcome learner was added. Freeze, hashing, verification, and preservation of both evidence sets serve reproducibility. The learned classifiers were specimens, not a complexity increase justified by a measured deficit.
- No general-purpose LLM participated or was removed for architectural purity. Retaining the two classifiers preserves the bounded specimen/control comparison. Their scores grant no authority, canonical status, calibrated probability claim, or permission to act.

The frozen `wp1-support-v1` H1–H7 matrix remains an experiment-local historical record. The current [research thesis](../../docs/RESEARCH_THESIS.md), including H2A/H2B, `C_A/C_B/T`, and falsifiers 1–10, governs thesis claims; WP0's thesis-freeze deliverable remains open under Issue #1. Neither externally adapted specimen supplies a same-base H2A comparison, and no H2B target was tested.

Any future adapter-owned normalization, implementation-class schema field, or independent reference check for the verifier belongs to a separately authorized next contract. In particular, E1 is a next-contract lesson, not a WP1 repair. This record authorizes no code change or new inference.
