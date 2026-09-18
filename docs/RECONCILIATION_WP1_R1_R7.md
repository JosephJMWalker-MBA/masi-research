# WP1 documentation reconciliation — R1–R7

**Status:** corrections submitted for scoped Claude re-check; the independent outcome remains `CLAIM_NARROWING_REQUIRED`. The construction-doctrine hold remains in force. This record does not accept WP1 or authorize WP2.

## Governing state and scope

- Reconciliation branch: `astra/wp1-claim-narrowing`.
- Governing current `main`: `a0ac9fe9cd400a6c03d6543d5b79f651bf89a3a5`, verified against `origin/main` before edits and after the interrupted session resumed.
- Frozen builder artifact: `codex/wp0-wp1-candidate-probe @ 81adfffa2d28e4a40a0b36fe1a21baa567d402ec`; its ref and tree remain unchanged.
- Authority: [construction doctrine](CONSTRUCTION_DOCTRINE.md), [epistemic integrity](EPISTEMIC_INTEGRITY.md), `AGENTS.md`, and [Claude's audit including Addendum A](AUDIT_WP0_WP1_2026-09-17.md). The eight operator-specified documents were read in order before edits.
- The audit's earlier main checkpoints (`775b7a8`, then `33d4e6e`) are historical provenance. Reconciliation uses current `a0ac9fe`, including the merged audit and epistemic-integrity addendum.

Current main does not contain the builder's code or evidence. This branch therefore brings forward only three non-frozen documents from `81adfff`: the WP1 README, RESULTS and historical HANDOFF. The README/RESULTS are reconciled as current documentation, with links pinned to absent builder artifacts. The HANDOFF preserves its entire original byte sequence and receives append-only annotations. The class record and this reconciliation record are new documentation. No merge or cherry-pick of the implementation packet is performed.

Shared documents start from current main's text. The old branch's STATUS, registry and thesis conflict resolutions are expressed as bounded documentation changes that retain current doctrine, rather than by merging the old versions. README and sprint retain the doctrine hold. No governance document or audit is replaced with an older copy.

## R1–R7 disposition

| Requirement | Documentation disposition | Re-check status |
| --- | --- | --- |
| R1 — implementation classes | [IMPLEMENTATION_CLASSES.md](../experiments/wp1/IMPLEMENTATION_CLASSES.md) reproduces the audit artifact table and specialist-gate block; [RESULTS.md](../experiments/wp1/RESULTS.md) adds implementation class alongside model class. Two externally adapted `CONTROL_B` specimens, an `INFRASTRUCTURE`/B0 floor, supporting infrastructure and documentation; no `CONTROL_A` or `MASI_TARGET`. | Implemented; pending scoped Claude re-check |
| R2 — thesis matrix supersession | RESULTS, WP1 README and [RESEARCH_THESIS.md](RESEARCH_THESIS.md) explicitly supersede the frozen WP1-local matrix for thesis purposes. Current H2A/H2B, `C_A/C_B/T` and falsifiers 1–10 govern. Issue #1's WP0 thesis-freeze deliverable stays open; the frozen contract is unchanged. | Implemented; pending scoped Claude re-check |
| R3 — E001 framing | STATUS uses the current purpose-built bounded Empathy-observation target; any base selection/fine-tuning is an optional `CONTROL_B` arm. The [historical handoff](HANDOFF_WP1_2026-09-17.md) corrects the old wording through an appended supersession, without rewriting the original. | Implemented; pending scoped Claude re-check |
| R4 — no established capability deficit | RESULTS explicitly says that WP1 establishes no deficit of transparent/rule-based Precision approaches and does not justify learned complexity. The equality rule is a floor, not a competitive transparent baseline. Visible author-created fixtures and canonical NLI/training-mixture overlap (N7) remain explicit confounds alongside the counts. | Implemented; pending scoped Claude re-check |
| R5 — narrow interchangeability | RESULTS, both READMEs, STATUS and the appended HANDOFF annotation state uniform invocation of a closed pre-registered set on one host. Normalization is caller-resident and candidate-keyed; the broader caller-branch condition holds only for invocation, not normalization. No open-set, cross-paradigm or target-ontology substitution is claimed. | Implemented; pending scoped Claude re-check |
| R6 — current-main reconciliation | Current-main STATUS, registry, thesis, README and sprint are retained and reconciled; the implementation hold remains. Registry wording records the already-observed NLI successor in current posture/class terms without adding a candidate. EVALUATION/MODULES crosslinks are limited to the historical interface and defer thesis authority to current main. | Implemented; pending scoped Claude re-check |
| R7 — historical validation erratum | The HANDOFF's original `git diff --check` / `# PASS.` lines remain byte-for-byte visible. An appended erratum limits that pass to an empty working-tree diff and records the two packet-range whitespace findings in the frozen contract, intentionally unedited. | Implemented; pending scoped Claude re-check |

## Preserved interpretation and limits

The implementation and evidence survived the independent audit; nothing in this reconciliation repairs or reruns them. WP1's valid observation is closed-set invocation and same-host repeatability, with separate raw and normalized records and explicit failure/abstention semantics. It does not establish an H1–H7 effect, adaptation value without a same-base comparison, purpose-built specialization, capability/efficiency superiority, calibration, generalization, an adequate transparent baseline or a capability deficit justifying learned complexity. HHEM and DeBERTa remain useful specimens without target or authority status.

E1 is **only a next-contract lesson**. The verifier shares helpers with the evaluated runner, so it cannot independently validate those helpers' logic. A future separately authorized contract may add an independent expected-normalization table or verifier. No such change is made here. Other audit observations remain as recorded; this packet does not repair missing historic logs, training-lineage gaps, the freeze's runner omission or any cosmetic code issue.

## Checks and their exact scope

The following checks concern preserved artifacts and documentation, not new inference or new empirical findings:

- Verified current remote main at `a0ac9fe` and the frozen remote builder at `81adfff`. The reconciliation worktree is isolated from the original main checkout and its untracked local model/environment assets.
- Recomputed all **five** `freeze.json` hashes from a temporary exact `git archive 81adfff` export: all match. The export contains no model weights or local environment.
- Ran `python3 -B scripts/verify_probe_evidence.py` in that export: PASS on the original six-run set; output exactly equals committed `verification-initial.json`.
- Ran `python3 -B scripts/verify_probe_evidence.py --evidence experiments/wp1/evidence/accounting-repair`: PASS on the final six-run set; output exactly equals committed `verification.json`.
- Each verifier reports maximum native difference 0 for all three existing pairs. These are checks of stored evidence only. All **82 exported files** remained byte-identical afterward, with no new files. No model was loaded, downloaded or invoked; no training or tests were run in this reconciliation.
- Re-ran `git diff --check c918252 81adfff`: exit 2, with exactly two trailing-whitespace findings at frozen `docs/WP0_WP1_CONTRACT.md:3-4`. This corroborates R7 and is **not** reported as a pass.

**Pre-commit checks completed:** the staged diff matched an explicit twelve-document allowlist; zero protected paths were changed or imported; all five frozen hashes matched; the historical handoff's entire **11,864-byte prefix** matched `81adfff`; local-link checks found zero missing targets; current-main and builder refs were unchanged; and the doctrine hold remained in README, STATUS and sprint. `git diff --cached --check a0ac9fe9cd400a6c03d6543d5b79f651bf89a3a5` passed over the actual staged documentation patch. This pass is separate from the historical builder-packet check, whose two findings remain recorded above.

A separate supporting reader reviewed R1–R7 coverage and found no blocking omission, independently confirming the unchanged handoff prefix. This supporting review is not Claude's scoped re-check and does not change the audit outcome.

## Files in this reconciliation

```text
README.md
STATUS.md
docs/CANDIDATE_IMPLEMENTATIONS.md
docs/EVALUATION.md
docs/HANDOFF_WP1_2026-09-17.md
docs/IMPLEMENTATION_SPRINT_001.md
docs/MODULES.md
docs/RECONCILIATION_WP1_R1_R7.md
docs/RESEARCH_THESIS.md
experiments/wp1/IMPLEMENTATION_CLASSES.md
experiments/wp1/README.md
experiments/wp1/RESULTS.md
```

The final commit identifies this twelve-document diff against governing `a0ac9fe`; use the branch ref or `git log -1 --format=%H` for its exact ID. Frozen WP1 files, `probe.py`, adapters, tests, fixtures, dependencies and evidence are neither changed nor imported. The original `81adfff` branch is not modified. No new candidate, runtime, training, inference, E001 work or issue-state change is part of this packet.

## Exact next action

**Scoped Claude re-check of R1–R7 only.** Review the documentation diff against `a0ac9fe`, confirm the handoff's append-only corrections, frozen/protected-file preservation and existing evidence-verifier results, and record whether the requested claim narrowing is sufficient. The present outcome remains `CLAIM_NARROWING_REQUIRED` until that disposition. Do not start WP2/E001 or merge either branch as part of this handoff; those decisions require separate operator authorization.
