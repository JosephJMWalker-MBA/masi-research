# Contributing

MASI Research is an open research program, not a feature-collection project.

Contributions should help answer a research question, strengthen a baseline, preserve evidence, reproduce a result, expose a confound, or falsify an assumption.

## Good contributions

Useful contributions may include:

- a reproduction or failed reproduction;
- a stronger or simpler baseline;
- a benchmark critique;
- a prior-art result that narrows MASI;
- an alternative module decomposition;
- a specialist implementation tied to a frozen experiment;
- a calibration or abstention method;
- a synthetic or real dataset with clear provenance and permission boundaries;
- an adversarial fixture;
- evidence that two proposed responsibilities should be merged;
- evidence that one proposed responsibility adds no measurable value;
- an outcome record that materially changes a prior conclusion.

## Contribution rule

> Do not contribute a feature merely because it sounds compatible with MASI.

Implementation should enter this repository because an accepted experiment or research obligation requires it.

## Preferred workflow

1. Identify the research question.
2. State the claim or hypothesis.
3. Define the baseline.
4. Define the test and success/failure conditions before results are visible.
5. Implement the smallest sufficient experiment.
6. Preserve configuration, model identity, data identity, environment, logs, and result artifacts where practical.
7. Separate observations from interpretations.
8. Report negative and inconclusive results without rewriting the original criteria.

## Module contributions

A model does not become "the Precision model" or "the Empathy model."

Describe it as an implementation of a responsibility, for example:

- `Precision-compatible implementation`
- `Empathy observation implementation`
- `Foresight scenario model`
- `Wisdom influence-update candidate`

Multiple implementations may coexist and disagree.

## Evidence expectations

Where applicable, contributions should document:

- exact model / checkpoint / revision;
- training or adaptation method;
- dataset identity and split rules;
- prompts or inference configuration;
- resource use;
- random seeds where meaningful;
- evaluation code;
- raw outputs or durable summaries;
- known limitations;
- licensing / redistribution constraints;
- whether an external provider restricts publication of performance information.

Do not present an uncalibrated score as a probability. Do not convert missing evidence into a negative finding. Do not silently discard failed runs.

## Human and sensitive data

Prefer synthetic, public, consented, or otherwise clearly authorized data during early research.

Do not commit private conversations, credentials, regulated data, personal psychological profiles, or proprietary corpora merely because they might improve a benchmark.

Human-state or care-related research must preserve the distinction between observable evidence, operational labels, and clinical claims.

## Discussion posture

Strong criticism is welcome when it attacks the claim, method, evidence, baseline, or architecture rather than the contributor.

A contribution that demonstrates MASI is unnecessary, inferior, overcomplicated, or incorrectly decomposed is valuable if the evidence supports it.

## Pull requests

Keep pull requests bounded to one research obligation when practical. Include:

- what question the change serves;
- what evidence it adds;
- what it does **not** establish;
- how it can be reproduced or reviewed;
- what would falsify the interpretation being proposed.
