# WP1 candidate probe

**Documentation reconciliation only.** This README is brought forward from `codex/wp0-wp1-candidate-probe @ 81adfff` onto current `main` at `a0ac9fe9cd400a6c03d6543d5b79f651bf89a3a5`. Builder code, frozen files and evidence remain solely in the pinned packet and are not merged here. The [independent audit](../../docs/AUDIT_WP0_WP1_2026-09-17.md) requires claim narrowing; implementation remains on hold pending a scoped Claude re-check of R1–R7.

**Observed scope (R5):** three pre-registered implementations — an `INFRASTRUCTURE`/B0 equality floor and two externally adapted pretrained transformer classifiers (`CONTROL_B`-class specimens) — used uniform invocation by changing only the candidate identifier and reproduced bit-identically on one host. Normalization is caller-resident and candidate-keyed. This demonstrates selection within the closed registered set, not arbitrary new implementations or purpose-built targets with different ontologies. The protocol's inference-branching condition was not triggered; the contract's broader caller-branch condition holds only for invocation, not normalization. Heterogeneity is limited to architecture/objective within one shared stack and adapter class. See [classes](IMPLEMENTATION_CLASSES.md) and [narrowed results](RESULTS.md).

**Thesis supersession (R2):** `wp1-support-v1`'s H1–H7 matrix remains a frozen WP1-local historical record. Current [RESEARCH_THESIS.md](../../docs/RESEARCH_THESIS.md) governs thesis interpretation through H2A/H2B, `C_A/C_B/T` and falsifiers 1–10. Issue #1's WP0 thesis-freeze deliverable remains open. No frozen contract is rewritten. WP1 established no capability deficit justifying learned complexity; the equality rule is a deliberately non-competitive floor.

This is Sprint 001's engineering probe, not MASI-E001 and not a performance benchmark. The frozen question, limits and acceptance criteria are in [protocol.json](https://github.com/JosephJMWalker-MBA/masi-research/blob/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/experiments/wp1/protocol.json) and [the WP0 contract](https://github.com/JosephJMWalker-MBA/masi-research/blob/81adfffa2d28e4a40a0b36fe1a21baa567d402ec/docs/WP0_WP1_CONTRACT.md). Twelve original synthetic, visible fixtures contain six support and six non-support references. There is no training, held-out split, routing, composition or outcome learning.

## Prior-art and candidate decision (2026-09-17, before runs)

| Source | Reuse and scope decision |
| --- | --- |
| [HHEM pinned model card](https://huggingface.co/vectara/hallucination_evaluation_model/blob/8e4a2e6e96c708cc76c2344f7e4757df2515292c/README.md) and [implementation](https://huggingface.co/vectara/hallucination_evaluation_model/blob/8e4a2e6e96c708cc76c2344f7e4757df2515292c/modeling_hhem_v2.py) | Reuse its T5 encoder consistency classifier; raw class logits/scores retained. Index 1 is consistent. Direct forward exposes native output that the convenience predict method hides. |
| [DeBERTa small long NLI pinned card](https://huggingface.co/tasksource/deberta-small-long-nli/blob/9a77395d4d3751be9e2a69c4ae318491d9b3fffb/README.md) | Reuse a different model architecture and three-class NLI objective. Entailment is index 0, neutral 1, contradiction 2; preserve all three scores. The registry's [older candidate](https://huggingface.co/sileod/deberta-v3-base-tasksource-nli) recommends this successor. |
| [FLAN-T5 base pinned card](https://huggingface.co/google/flan-t5-base/blob/7bcac572ce56db69c1ea7c8af255c5d7c9672fc2/README.md) | HHEM's nested configuration/tokenizer dependency; fetch only six configuration/tokenizer/card files, not foundation weights. Override its floating foundation name with this local snapshot. |
| [Transformers inference APIs](https://huggingface.co/docs/transformers/v4.57.6/en/model_doc/auto) and [Hub snapshot download](https://huggingface.co/docs/huggingface_hub/v0.36.0/en/guides/download) | Existing loaders/tokenizers are sufficient. No inference framework, scheduler, server or plugin mechanism is needed. |
| [MASI Bus pinned schema](https://github.com/JosephJMWalker-MBA/masi-bus/blob/b9d8d632f7a3d1b4528d80bfad6c743e4e3ed490/schema/masi-bus-schema.json) | Reuse its conceptual message boundary later; do not duplicate its schema or invent confidence now. See the contract's explicit field ownership. |

Available skills/tools were reviewed: connectors can retrieve source evidence but do not supply this fixed local inference interface. Agent/workflow orchestration and routing products in the registry exceed this question. The only custom machinery is a fixed candidate table, adapters, a local record normalizer and fixture runner. All three downloaded model/tokenizer cards declare Apache-2.0; this review authorizes only the pinned local probe and publication of original synthetic probe records. Upstream weights/code stay excluded from Git. Model licenses remain upstream; this repository does not relicense them.

The deterministic rule is deliberately weak: stripped casefold equality yields support; otherwise it abstains. Native learned scores are uncalibrated. `not_supported` combines insufficient support and contradiction and must not be read as falsehood. HHEM and NLI are heterogeneous architectures/objectives within a single text-classification interface; this is not evidence of heterogeneous MASI responsibilities.

## Reproduce

The commands below are retained instructions for a separate checkout of the pinned builder packet, where the referenced code exists. They are historical reproduction instructions, **not authorization to run inference during R1–R7 or the scoped re-check**. This documentation-only checkout cannot execute them. The scoped re-check may run the existing read-only evidence verifier against an unchanged builder export; it must not invoke models.

Validated environment is Python 3.11 on Apple arm64. Other environments remain unverified. From the repository root:

```sh
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements-probe.lock
.venv/bin/python scripts/prepare_probe_models.py --model-root .models
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python probe.py --candidate exact-match-v1 --output local-runs/baseline-1
.venv/bin/python probe.py --candidate hhem-2.1 --output local-runs/hhem-1
.venv/bin/python probe.py --candidate nli-deberta-small --output local-runs/nli-1
```

Run the same commands again with new output directories for replication. The baseline also runs with standard-library Python and no downloaded model dependencies. Candidate selection is the only experiment change. All inference runs are offline and sequential, CPU float32, one intra/inter-op thread, batch one, seed zero, deterministic algorithms enabled. Each successful learned fixture uses one forward call. Tokenization uses model-required templates, counts special tokens, rejects more than 512 tokens and never truncates. Fixed fixture fields are bounded to 4,096 characters each. No label/category is supplied to `infer(premise, claim)`.

Preparation is the only network step for artifacts. The three pinned snapshots use 19 allowed files; the loader verifies their size/hash and revisions before importing HHEM's reviewed custom code. Download failures are setup non-execution, not model results. Model preparation can resume incomplete downloads. The runner does not download missing weights and writes explicit load errors if artifacts are unavailable or changed.

## Evidence format

Every run creates a **new** directory and refuses overwrite:

- `manifest.json`: freeze identity, source hashes, Git identity/status, candidate metadata, exact model artifact hashes, installed package versions, runtime settings, start/finish state, load timing, process memory and output-file hashes.
- `raw.jsonl`: native outputs or errors, one row per fixture. No model rationale is fabricated.
- `normalized.jsonl`: common contract with identity and input/raw hashes, plus measured per-invocation resources.
- `summary.json`: all-fixture denominator, correctness count, coverage, abstentions, errors and call accounting. No winning candidate is automatically selected.

Hashes of records use UTF-8 bytes of Python `json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)` with the default `ensure_ascii=True`. Input hashes cover exactly `{premise, claim}` before adapter formatting. File hashes cover exact file bytes. Invalid/non-finite output is an error; when invalid native values cannot be represented in JSON, their Python representation is retained separately. Available native output survives normalization failure.

The freeze manifest hashes the contract, protocol, fixtures and candidate source before first fixed-fixture observation. The runner fails before inference on a changed frozen file. Revisions to that freeze require a new declared protocol/run and retention of the earlier files/evidence. Source changes outside the frozen files are independently hashed in each run.

An interrupted run may leave `state: started` and partial rows; it is not complete and must not be overwritten. Process peak RSS includes imports/model load and is not incremental per-call memory. Wall times are descriptive local measurements; setup, tokenization and model sizes differ. Energy and amortized cost are unmeasured; zero external inference charges do not mean zero resource cost.

Verify the retained final run set without downloading or invoking models:

```sh
python3 scripts/verify_probe_evidence.py --evidence experiments/wp1/evidence/accounting-repair
```

The initial six-run set remains at `experiments/wp1/evidence` in the pinned builder packet; the final set repeats the same frozen experiment after a resource-accounting repair. No real-world action or outcome is measured here. Broader Issues #1/#2 and E001 remain open. E001 targets purpose-built Empathy-observation intelligence; base selection/fine-tuning is only an optional `CONTROL_B` arm, with no E001 work authorized here. See [results](RESULTS.md) and the appended corrections in the [historical handoff](../../docs/HANDOFF_WP1_2026-09-17.md). The exact next action is a scoped Claude re-check, not WP2.

E1 remains a next-contract lesson: the existing verifier shares runner helpers and is not an independent check of their logic. A separately authorized future contract may add a reference check; WP1 code and evidence stay unchanged.
