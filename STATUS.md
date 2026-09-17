# Status

**Current phase:** Phase 0 -> Phase 1 transition — bounded implementation

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

1. Close enough of Issues #1 and #2 to freeze the thesis, common responsibility envelope, and Reality Audit minimum.
2. Build the smallest candidate-probe layer needed to invoke interchangeable local implementations through one bounded experiment interface.
3. Run at least two heterogeneous local candidates through that interface, starting with Precision-friendly probes where practical.
4. Complete `MASI-E001` design gates and begin the first learned specialization only after split/metrics/controls are frozen.
5. Attempt a minimal heterogeneous composition smoke test only after individual candidate behavior is observable.

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

Work from `IMPLEMENTATION_SPRINT_001.md`: freeze WP0, then implement WP1's thin candidate-probe layer. Use Issues #1–#3 as the current research gates and preserve each Astra/Claude handoff in commits, PRs, tests, and issue records.
