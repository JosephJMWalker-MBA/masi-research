# Experiments

MASI experiments should be small, precommitted, reproducible, and capable of producing negative results.

## Naming

Use:

```text
MASI-E###
```

Examples:

- `MASI-E001` — first specialization-by-construction experiment (Empathy speaker observation)
- `MASI-E002` — next independently scoped experiment

Do not encode success claims into experiment names.

## Required protocol fields

Each experiment should define before final evaluation:

1. **Research question**
2. **Hypothesis**
3. **Why this matters to MASI**
4. **Systems / conditions compared**
5. **Dataset / fixture identity**
6. **Train / validation / test split logic**, if applicable
7. **Metrics**
8. **Resource accounting**
9. **Success conditions**
10. **Falsifiers / failure conditions**
11. **Known confounds**
12. **Publication / licensing constraints**
13. **Reproduction procedure**

## Experiment lifecycle

```text
question
  ↓
prior-art check
  ↓
protocol freeze
  ↓
implementation
  ↓
preflight
  ↓
execution
  ↓
evidence preservation
  ↓
interpretation
  ↓
replication / challenge
  ↓
revision or next experiment
```

## Result classes

Use explicit result language:

- `supported`
- `not_supported`
- `inconclusive`
- `halted`
- `invalidated`

Do not rename a failed result as a successful "exploration" after the fact.

## MASI-E001

**Title:** Empathy speaker-observation specialist — purpose-built target versus general-model controls.

**Status:** the preregistered protocol [`e001/PROTOCOL.md`](e001/PROTOCOL.md) (`e001-protocol-v1.4`) is a **repaired freeze** awaiting independent verification of its A1 restart-replacement screening. It is **not accepted and not authorized for execution**. No data, labels, model runs or results exist.

**History:**

- v1.0 was audited [`REPAIR_REQUIRED`](https://github.com/JosephJMWalker-MBA/masi-research/pull/17#issuecomment-5735626914). Repairs R1–R7 (v1.1) are recorded in protocol §27.
- The independent audit of v1.1 returned six blocking findings, A1–A6. Their repairs (v1.2) are recorded in protocol §28.
- The re-audit of v1.2 passed A2–A5 and kept A1 and A6 blocking. Their repairs (v1.3) are recorded in protocol §29.
- The verification of v1.3 closed A6 and A1's second-draw defect, and found that restart replacement units skipped the pre-M0 checks. That repair (v1.4) is recorded in protocol §30.

**Question** ([Issue #3](https://github.com/JosephJMWalker-MBA/masi-research/issues/3)): can a purpose-built bounded intelligence, designed from the Empathy-observation responsibility outward, infer an evidence-grounded observation state competitively with general-model controls while providing stronger inspectability, state discipline, uncertainty handling, efficiency, or failure localization?

**Primary claim:** H2B. It is a conjunctive decision:

- **quality:** the target `T` is non-inferior to the competent controls `B0`, `C_A` and `C_B` on evidenced-concern quality, observation-state quality and recall;
- **property:** `T` improves evidence-verified claim precision over `C_A` and `C_B` by a superiority margin of at least 0.10, with the lower confidence bound above the margin.

The state-quality component can be narrowed only by a preregistered reliability gate that is evaluated before implementation.

**H2A** is not confirmatory. A fine-tuned model is a `CONTROL_B` arm, **not** the presumed target.

**Target construction:** a transparent first rung, `T0`. Learned complexity (`T1`, `T2`) may be added only when a preregistered development-data deficit is shown **and** is attributable to the capability the next rung adds.

**Substrate:** ADCP supplies ontology concepts. ADCP stages, thresholds, severities and fixture labels are **not** imported (see protocol §3).

**Companion documents:**

- [`e001/ANNOTATION_RUBRIC.md`](e001/ANNOTATION_RUBRIC.md): the shared task definition;
- [`e001/REFERENCE_CASES.md`](e001/REFERENCE_CASES.md): the E1 independent reference checks;
- [`e001/PROTOCOL_MANIFEST.json`](e001/PROTOCOL_MANIFEST.json): preregistration facts.

**Next action:** independent verification of the restart-replacement screening, plus a scope regression, of the repaired protocol. No implementation, annotation, training or inference takes place until that audit is accepted **and** the operator separately authorizes execution.
