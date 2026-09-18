# Status

**Current phase:** WP0 minimum frozen; WP1 implemented and locally observed; independent audit pending

**Primary objective:** turn MASI from a conceptual/disclosure lineage into falsifiable executable research while preserving model interchangeability, explicit governance, fair baselines, and claim discipline.

## Current decisions

- `masi-research` is the public experimental home for ongoing MASI work.
- `masi-bus` remains the communication/reference artifact; it is not replaced by this repository.
- No model is canonical merely because it implements a named MASI responsibility.
- Precision, Foresight, Empathy, and Wisdom are current architectural responsibility abstractions whose boundaries remain revisable.
- Prompt-only role decomposition is an experimental baseline, not the intended definition of specialization.
- Telos is a leading **candidate** for governance/control-plane orchestration, especially intent/authority/permission continuity; it is not thereby a mandatory dependency or the learned task router.
- The candidate fleet should be heterogeneous: language models, classifiers, forecasters, reward models, bandits, deterministic systems, and external decision-native services may all compete for bounded responsibilities.
- New implementation must be justified by a frozen experiment or interface need, not added because it sounds compatible with MASI.

## Candidate landscape

The working registry is now maintained in [`docs/CANDIDATE_IMPLEMENTATIONS.md`](docs/CANDIDATE_IMPLEMENTATIONS.md).

Initial high-priority probes include:

- **Routing:** vLLM Semantic Router / RouteLLM plus a deterministic routing baseline;
- **Precision:** HHEM-2.1-Open, NLI classifiers, Jev as an external comparator where terms permit;
- **Foresight:** Chronos / TimesFM-class numerical forecasters plus a compact qualitative scenario model;
- **Empathy:** an ADCP-derived semantic observer plus bounded auxiliary sensors;
- **Wisdom:** MABWiser / Vowpal Wabbit contextual-bandit baselines before assuming Wisdom should be an LLM;
- **Governance/control:** Telos plus a simpler deterministic governance baseline.

## Active implementation sprint

[`docs/IMPLEMENTATION_SPRINT_001.md`](docs/IMPLEMENTATION_SPRINT_001.md) defines the current execution plan.

Current operator cadence:

```text
Astra on Ultra — primary implementation/research block
        ↓
commit + tests + evidence + unknowns
        ↓
Claude — independent audit at ~5-hour / work-packet boundary
        ↓
accept / repair / narrow / mark inconclusive
        ↓
next Astra block
```

GitHub is the durable state boundary. No model session is the system of record.

## Immediate sequence

1. Independently audit the [WP1 handoff](docs/HANDOFF_WP1_2026-09-17.md), frozen contract and retained evidence.
2. Accept, repair, narrow, or mark the bounded result inconclusive before further work packets.
3. Only in a separately authorized packet, complete `MASI-E001` design gates; training remains gated on frozen splits, labels, metrics and controls.
4. Composition, routing and outcome learning remain later experiments.

## Observed WP0 / WP1 checkpoint

The [bounded contract](docs/WP0_WP1_CONTRACT.md) freezes only enough of Issues #1/#2 to implement WP1. It defines support, abstention/error, native score meaning, a documentation-only Reality Audit minimum, and the MASI Bus boundary without a new transport schema.

The [probe](experiments/wp1/README.md) runs a deterministic exact-match baseline, HHEM-2.1 and a compact DeBERTa NLI candidate through one fixed interface. Two runs per implementation reproduced native outputs exactly; the accounting-repaired source was rerun with the same result. Raw outputs, normalized records, hashes, resources and original observations are preserved. All 22 unit tests pass. [Results and limits](experiments/wp1/RESULTS.md) support only a bounded interchangeability seam, not efficacy or system-level MASI claims.

The formal independent Claude audit is pending. Issues #1, #2 and #4 have not been closed. No E001 training, generic runtime, router, composition or outcome learner was built.

## First learned-specialization experiment

**MASI-E001 — Empathy semantic-observation specialist**

Research question:

> Can a small locally specialized model infer a bounded, evidence-grounded human-impact / care observation state more reliably than the same untuned local model, and how does it compare with a larger general-purpose baseline?

The first candidate substrate is the Accumulated Distress Care Protocol (ADCP), because ADCP already separates human-authored observations from deterministic downstream policy. MASI-E001 targets the observation layer only; it must not train a model to imitate ADCP's policy thresholds.

## Not yet authorized

- building a general-purpose MASI platform before bounded experiments require it;
- creating separate repositories for individual MASI modules;
- treating Telos, Jev, ADCP, any router, or any local model as canonical MASI;
- allowing routing convenience to become governance authority;
- training a Wisdom language model before an auditable outcome record and simpler baselines exist;
- publishing third-party performance benchmarks where provider terms prohibit publication;
- installing the entire candidate registry at once;
- changing held-out evaluation criteria after observing results.

## Next durable action

Use [HANDOFF_WP1_2026-09-17.md](docs/HANDOFF_WP1_2026-09-17.md) for exact commits, commands, evidence, unknowns and the independent audit request. Review WP0/WP1 before authorizing a new work packet. Keep Issues #1–#3 as broader research gates.
