# Status

**Current phase:** Phase 0 — research foundation

**Primary objective:** turn MASI from a conceptual/disclosure lineage into a falsifiable experimental program without prematurely freezing model identities, module implementations, or orchestration mechanics.

## Current decisions

- `masi-research` is the public experimental home for ongoing MASI work.
- `masi-bus` remains the communication/reference artifact; it is not replaced by this repository.
- No model is canonical merely because it implements a named MASI responsibility.
- Precision, Foresight, Empathy, and Wisdom are current architectural abstractions whose boundaries remain revisable.
- Prompt-only role decomposition is an experimental baseline, not the intended definition of specialization.
- New implementation should be justified by a frozen experiment, not added because it sounds compatible with MASI.

## Immediate sequence

1. Freeze the research thesis and falsification criteria.
2. Define implementation-independent responsibility contracts.
3. Define evaluation baselines and resource accounting.
4. Design `MASI-E001`.
5. Only then add the code, data, training, and schemas required by that experiment.

## Proposed first experiment

**MASI-E001 — Empathy semantic-observation specialist**

Research question:

> Can a small locally specialized model infer a bounded, evidence-grounded human-impact / care observation state more reliably than the same untuned local model, and how does it compare with a larger general-purpose baseline?

The first candidate substrate is the Accumulated Distress Care Protocol (ADCP), because ADCP already separates human-authored observations from deterministic downstream policy. MASI-E001 should target the observation layer only; it should not train a model to imitate ADCP's policy thresholds.

## Not yet authorized

- building a general MASI runtime;
- creating separate repositories for individual MASI modules;
- treating Jev or any other external model as canonical Precision;
- training a Wisdom model before an auditable outcome record exists;
- publishing third-party performance benchmarks where provider terms prohibit publication;
- adding large-scale infrastructure before an experiment requires it.

## Next durable action

Complete issues #1–#3 in order, with #3 remaining design-first until the evaluation contract and data split are frozen.
