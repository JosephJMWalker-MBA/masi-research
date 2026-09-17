# WP0 / WP1 — Bounded Contract Freeze

**Contract:** `wp1-support-v1`  
**Scope:** Sprint 001 WP0 and WP1; partial treatment of Issues #1 and #2, supporting Issue #4  
**Freeze rule:** commit this contract, the experiment protocol, fixture bytes, candidate revisions, and output mappings before observing candidate outputs. A changed contract or fixture creates a new version/run; retain earlier evidence.

This freeze makes one probe implementable. It does not close the broader thesis or responsibility-design issues, authorize learned-specialization training, or define a general MASI runtime.

## Question and acceptance boundary

Can unchanged experiment code invoke a deterministic baseline and two heterogeneous local implementations on the same bounded premise/claim task, preserving native output, normalized decisions, failures, and resource provenance?

The responsibility identifier is `precision.evidence_support`. The task asks whether the supplied premise supports the supplied claim. It does not judge truth beyond the premise, clinical state, moral acceptability, or the authority to take action.

WP1 passes its implementation gate when all three implementations run through the same calling interface and fixed synthetic fixtures; registered candidate selection replaces an implementation without changes to the experiment caller; valid, abstaining, and failed outputs retain their prescribed semantics; and raw output, normalization, revisions, and measured resources are recoverable. Contract and failure-path tests must pass. A lower-quality learned candidate is an admissible result, not a failed engineering gate. Invocation failure is preserved and does not count as a successful candidate run.

The probe fails the interchangeability gate if the caller requires implementation-specific branches, the shared task changes for a candidate, silent truncation changes evidence, native output cannot be recovered, or normalized output invents unsupported semantics. Repair or narrow the interface claim before proceeding. An unavailable candidate is a recorded non-execution, not evidence of poor task capability.

This is evidence for a bounded executable seam underlying H4. It establishes no architecture-wide benefit, calibration, learned-specialization gain, or system-level MASI superiority.

## Thesis and distinguishable controls

The program-level thesis is conditional: **on a preregistered task family, a governed composition may improve a declared task outcome over simpler alternatives under explicit resource conditions, and an appropriate control must distinguish the proposed mechanism.** A claim of equality requires a preregistered equivalence or non-inferiority margin; a claim of improvement requires a preregistered effect criterion. Neither follows from a smoke test.

| Hypothesis | Comparison that can distinguish it | Main confound / narrowing condition | WP1 status |
| --- | --- | --- | --- |
| H1: decomposition | Role decomposition versus the same model without decomposition, with stated input, pass, and resource controls | Extra calls, tokens, tools, or helpful context explain the difference | Not tested |
| H2: learned specialization | Adapted specialist versus its same untuned base on frozen held-out and adverse cases; prompt-only control where relevant | Prompting, leakage, tuning the test, or changed base capability explains the difference | Not tested; pretrained specialists are not evidence of MASI adaptation |
| H3: composition | Composition versus constituent candidates and a fixed simple aggregation baseline | Strongest constituent or ordinary aggregation reproduces the result | Not tested |
| H4: interchangeability | Substitute heterogeneous implementations under one fixed responsibility contract without rewriting calling logic | Model-specific task semantics or caller branches are required | Bounded interface feasibility only |
| H5: dynamic composition | Governed selection versus always-on and deterministic selection baselines | Ordinary selection or invocation savings reproduce the result; selection weakens governance | Not tested |
| H6: outcome-grounded adaptation | Outcome updates versus fixed influence and established simple updating methods on later comparable tasks | Leakage, drift, or ordinary calibration/bandit updates explain the result | Not tested |
| H7: local competitiveness | Local composition versus an identified larger general-purpose baseline on a preregistered family, with disclosed budgets and passes | Favorable fixture selection, unequal resources, or incomparable task access explains the result | Not tested |

Before any later efficacy experiment, freeze its target population/task family, outcome metric, success/failure or equivalence criterion, uncertainty treatment, controls, data split, resource conditions, and permitted interpretation. If those cannot distinguish its claimed mechanism, mark the question defective or narrow it before observation. Repeated controlled null or adverse results narrow the thesis; simpler methods remain eligible to win. The existing strong falsifiers in `RESEARCH_THESIS.md` remain in force.

## Common input and bounded invocation

Each fixture has a stable identifier, a `premise` string, and a `claim` string. Candidate adapters receive the same premise and claim; reference labels are evaluation data and must not be supplied to the candidate. The experiment protocol fixes the concrete fixture and record formats and their hash encoding.

- Each input string is limited to 4,096 characters. Empty or out-of-scope input must not produce an ordinary verdict.
- A learned candidate may consume at most 512 model tokens, including candidate-required prompt/template/special tokens. Tokenization is candidate-specific, and its measured length is recorded. Inputs exceeding that bound abstain before inference; do not truncate them.
- One bounded invocation per candidate/fixture; no retrieval, tools, retries, training, critique passes, or aggregation.
- Candidate-required formatting belongs in its adapter, is fixed before observation, and must preserve the complete semantic input within the bound.
- Fixtures are public synthetic engineering smoke cases. They are not a held-out benchmark or a generalization claim. Labels are task references, not real-world observed consequences.

## Common normalized output

The experiment-local envelope has the following fields. Implementations may preserve extra native information in their separate raw record; native output does not redefine these fields.

| Field | Required meaning |
| --- | --- |
| `contract_version` | Exactly `wp1-support-v1` |
| `run_id`, `fixture_id`, `candidate_id` | Stable linkage to the run, input fixture, and registered implementation; a candidate identity is not a responsibility or authority |
| `responsibility` | Exactly `precision.evidence_support` |
| `input_sha256` | Digest linking the exact common input, using the experiment protocol's fixed encoding |
| `raw_record_sha256` | Digest linking the separate preserved native-output or failure record, using the fixed record encoding |
| `status` | `ok`, `abstain`, or `error` |
| `verdict` | `supported` or `not_supported` only when `status` is `ok`; otherwise `null` |
| `support_score` | Candidate-native support score, or `null` when unavailable; finite numeric scores use the candidate's documented meaning and range |
| `score_semantics` | Explicit score meaning and origin, including unavailable score semantics; numbers from different candidates are not presumed comparable |
| `calibration` | Exactly `not_measured` |
| `evidence_refs` | `["premise", "claim"]`; these identify supplied inputs, not a claim that either is externally true or that the model identified supporting spans |
| `unsupported_assumptions` | List of explicitly reported unsupported assumptions; the initial adapters emit `[]` |
| `assumption_reporting` | `not_available` when the implementation cannot expose assumptions, or `none_reported` when it reports none; neither establishes their verified absence |
| `escalation_requested` | Boolean request for review, with no execution or authority effect |
| `reason` | String explaining the verdict, abstention, or failure and any escalation request |

`not_supported` means the candidate did not establish support. It does not establish that a claim is false or contradicted. Native NLI labels and class scores remain in raw output, including neutral/contradiction distinctions that this deliberately binary common task does not express.

For learned candidates, use the native support/entailment score with the frozen mapping: strictly greater than `0.5` means `supported`; strictly less than `0.5` means `not_supported`; exactly `0.5` means `abstain`. Thresholds are engineering conventions, not measured calibration or optimized decision rules. The candidate record must identify the native class/score mapping. Native scores may be retained for a threshold-tie abstention; abstention before inference has no score. Error records have neither verdict nor score.

The deterministic baseline compares the nonempty inputs after trimming surrounding whitespace and case folding. Equality yields `supported`; any other pair yields `abstain`. Its score is `null`. This narrow rule makes no general semantic judgment.

An abstention is a deliberate inability to answer inside the contract, including an input bound or tie. An error is an execution, integrity, malformed-output, or normalization failure. Preserve errors separately rather than disguising them as ordinary abstentions. Default escalation for abstention/error is `true`; ordinary successful output uses `false`. An escalation only records that review is needed and does not invoke another model or authorize an action.

Multiple implementations may coexist for this responsibility. Preserve their outputs separately, including incompatible verdicts; WP1 has no consensus, voting, trust weighting, final authority, or winner-selection policy.

## Resource and provenance record

Metrics belong in the per-invocation run record, separate from the normalized responsibility envelope. Record candidate source, exact source/model revision, license and terms review date, model/runtime identity, device/hardware, dtype/quantization where applicable, actual model-call count, input token count where available, supplied context, inference latency, and load latency separately. Preserve native scores/output and the normalization version independently of interpretation.

Record process peak memory when measurable with its units, measurement method, and scope. Process high-water memory is not per-inference allocation and is not necessarily accelerator memory. For unavailable memory, token, energy, monetary-cost, or other measures, use an explicit unavailable value/reason; do not report unknown as zero. Local execution does not establish zero compute, energy, or amortized cost. The deterministic baseline has no model inference calls. Attempted and successful learned calls must remain distinguishable when failure occurs.

Candidate-specific tokenization means equal textual evidence is not equal token count. Record the difference. Timing is a local descriptive observation and must not be presented as a controlled hardware benchmark. Fixed fixtures, exact revisions, deterministic runtime settings where available, and retained raw records support reproduction; they do not guarantee bit-identical learned inference across platforms.

## MASI Bus boundary

The existing communication reference was inspected at commit [`b9d8d632f7a3d1b4528d80bfad6c743e4e3ed490`](https://github.com/JosephJMWalker-MBA/masi-bus/tree/b9d8d632f7a3d1b4528d80bfad6c743e4e3ed490) on 2026-09-17. Its [v1.0 schema](https://github.com/JosephJMWalker-MBA/masi-bus/blob/b9d8d632f7a3d1b4528d80bfad6c743e4e3ed490/schema/masi-bus-schema.json) owns the message envelope: required message type, sender role, UUID task identifier, content analysis, numeric confidence/cost metrics, and timestamped audit trail. Optional fields cover assertions/actions, trust/risk metadata, credentials, prior-message references, and conflicts. Top-level extra properties are disallowed; `content` permits extensions.

That schema does not define this task's fixture IDs, candidate revisions, score interpretation, abstention/error distinction, resource units, or Reality Audit outcome semantics. Its required numeric confidence cannot honestly represent unavailable confidence, and its cost field does not settle accounting units. The [pinned README](https://github.com/JosephJMWalker-MBA/masi-bus/blob/b9d8d632f7a3d1b4528d80bfad6c743e4e3ed490/README.md) also distinguishes protocol structure from calibrated confidence, authoritative trust, certification, and an implemented runtime.

WP1 therefore stores an experiment-local result and does not claim to emit MASI Bus messages. Do not copy, fork, or extend the Bus schema here, invent confidence/cost numbers to satisfy it, or make Bus transport a dependency. If later work needs messaging, specify a mapping using Bus content extensions and references to experiment/audit artifacts; separately resolve unavailable metric semantics with the upstream protocol. Model metadata, frozen task policy, resource detail, and outcome records remain experiment evidence rather than protocol authority.

## Minimum Reality Audit record — defined, not implemented

Before outcome-based influence learning, a local audit record must preserve the following information and explicitly distinguish missing, pending, and not-applicable values:

| Information | Minimum semantics |
| --- | --- |
| Identity and provenance | Audit, task, prediction, candidate/version, input/evidence, protocol version, and timestamps linked to preserved source artifacts |
| Prediction | The candidate's stated prediction or bounded judgment, its stated assumptions, uncertainty/score meaning, and calibration status, as recorded before the outcome |
| Action | Proposed action, action actually taken, decision authority, and time; distinguish recommendation from execution and record no action explicitly |
| Expected outcome | Observable target, expected value/state, comparison criterion, relevant context, and time horizon, fixed before observation |
| Observed outcome | Observation status, actual value/state and observation time, source/method, uncertainty, missingness, and any confounding intervention |
| Discrepancy/error | Expected-versus-observed comparison using the frozen criterion; retain both favorable and adverse observations and unresolvable attribution |
| Horizons and follow-up | Which horizon has matured, which remains pending, and the next observation due; an early observation cannot silently settle later consequences |

Do not retroactively rewrite a prediction or expectation using its outcome. Corrections and interpretation must remain distinguishable from raw observations. A model's agreement with another model is not an externally observed outcome. Influence changes, if later authorized, must identify the outcome record and update rule separately from any retraining.

For WP1, the supplied synthetic reference label can support a smoke-test comparison only. No consequential action is taken and no real-world outcome has been observed. Record those limits; do not fabricate an outcome sequence to imply Reality Audit capability. Implementing an outcome learner, audit service, governance engine, router, or general composition system is outside this freeze.

## Handoff and remaining gates

Preserve exact branch/commit, changed files, frozen protocol and fixture hashes, candidate/license records, commands and test results, raw run artifacts, normalized results, failures/non-executions, unknowns, unsupported claims, and the next action at the WP1 boundary. Separate descriptive observations from interpretation and request an independent audit against this freeze.

Issues #1 and #2 remain broader research gates: responsibility-wide contracts, empirical efficacy thresholds, calibration studies, transport integration, and real outcome learning are unresolved. E001 split/label/metric/training authorization remains separate. Completing WP1 does not authorize WP2–WP5 execution automatically.
