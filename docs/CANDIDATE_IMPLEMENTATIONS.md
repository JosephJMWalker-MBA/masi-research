# Candidate Implementation Registry

**Status:** exploratory registry  
**Last reviewed:** 2026-09-17

This document tracks candidate implementations, substrates, and baselines for MASI responsibilities. It is intentionally inclusive. Inclusion is **not** endorsement, qualification, or architectural authority.

The governing rule is:

> MASI responsibilities are stable only to the extent that experiments justify them. Implementations remain interchangeable.

A candidate may be a learned model, deterministic system, simulator, statistical learner, external service, or composition of several tools. No candidate becomes canonical because it performs well once or because it currently occupies a named role.

Licenses and provider terms can change. License notes below are preliminary research notes and must be re-verified before integration, redistribution, publication of benchmark results, or commercial use.

## Control plane and routing

### Telos — candidate governance / orchestration substrate

Repository: https://github.com/JosephJMWalker-MBA/Telos

Telos is the leading internal candidate for the **governance/control plane**, especially for preserving human-governed intent, authority, permission, continuity, and legitimate change. Its role should be distinguished from learned task routing.

Proposed separation:

```text
Telos
  -> what is governing?
  -> who has authority?
  -> what is permitted?
  -> what continuity must be preserved?

Router / selector
  -> which available competence is relevant?

MASI specialists
  -> what does each bounded responsibility report?

Wisdom / outcome learner
  -> which implementations have earned influence under comparable conditions?
```

Telos is a candidate, not a mandatory MASI dependency. A simpler governance baseline should remain available for comparison.

### Routing candidates and baselines

| Candidate | Why it matters | Initial posture |
| --- | --- | --- |
| [vLLM Semantic Router](https://github.com/vllm-project/semantic-router) | Programmable Mixture-of-Models routing/control layer across heterogeneous model paths; strong prior art and implementation baseline for MASI routing. | High-priority baseline / possible infrastructure reuse |
| [RouteLLM](https://github.com/lm-sys/RouteLLM) | Learned routing strategies and local-model routing; useful scientific baseline for strong-vs-weak selection. | Baseline |
| [Plano-Orchestrator-4B](https://huggingface.co/katanemo/Plano-Orchestrator-4B) | Specialized orchestration model that selects agents/models and sequencing. | Research comparator; verify license constraints |
| [Arch-Router-1.5B](https://huggingface.co/katanemo/Arch-Router-1.5B) | Small learned router aligned to user-defined preferences/domains. | Research comparator; verify license constraints |
| [Salesforce xRouter](https://huggingface.co/Salesforce/xRouter) | Learned routing with quality/cost tradeoff objective. | Research comparator; verify current noncommercial terms |
| [Aurelio Semantic Router](https://github.com/aurelio-labs/semantic-router) | Cheap embedding-space routing baseline. | Baseline MASI should be able to beat where routing is claimed to matter |

## Precision candidates

Precision should not mean "a model prompted to sound precise." Candidate implementations should be evaluated for bounded judgment, evidence support, contradiction, constraint satisfaction, abstention, calibration, or verification.

| Candidate | Candidate capability | Initial posture |
| --- | --- | --- |
| **Jev / TypeSafe AI** | Decision-native bounded outputs, scores/probabilities, fast repeated judgments. | External comparator / possible implementation; provider benchmark-publication terms must be respected |
| [Vectara HHEM-2.1-Open](https://huggingface.co/vectara/hallucination_evaluation_model) | Evidence-premise vs generated-claim factual consistency. | High-priority local verifier; Apache-2.0 at review time |
| [DeBERTa-v3 Tasksource NLI](https://huggingface.co/sileod/deberta-v3-base-tasksource-nli) | Entailment / contradiction / zero-shot bounded classification. | High-priority local baseline; verify current model card/license |
| [DeBERTa-v3 large MNLI/FEVER/ANLI/WANLI](https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli) | Claim support and adversarial NLI exposure. | Precision comparator; verify current model card/license |
| [Skywork Reward V2 Qwen3 family](https://huggingface.co/Skywork/Skywork-Reward-V2-Qwen3-0.6B) | Small reward/judgment models from 0.6B upward; useful for ranking/evaluation experiments. | High-priority research candidate; Qwen3 variants Apache-2.0 at review time |
| Custom small base-model specialist | Train directly on MASI Precision contracts rather than general chat behavior. | Intended learned-specialization path |

## Foresight candidates

Foresight should use domain-appropriate prediction machinery when possible rather than forcing all future-state estimation through prose generation.

| Candidate | Candidate capability | Initial posture |
| --- | --- | --- |
| [Amazon Chronos](https://github.com/amazon-science/chronos-forecasting) | Specialized zero-shot time-series forecasting family. | High-priority quantitative Foresight candidate |
| Chronos-Bolt family | Very small forecasting specialists; useful for testing whether tiny domain models add disproportionate value. | High-priority local candidate |
| [Google TimesFM](https://github.com/google-research/timesfm) | Time-series foundation models with multivariate/covariate support in current generations. | High-priority comparator; version-specific weight license must be checked |
| [Salesforce Moirai / uni2ts](https://github.com/SalesforceAIResearch/uni2ts) | Universal forecasting and Moirai-family specialists; Moirai Agent is relevant prior art for expert selection. | Research comparator; verify version-specific noncommercial terms |
| [Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning) | Compact reasoning model for qualitative/scenario Foresight where a numerical forecaster is insufficient. | Candidate substrate; MIT at review time |
| Custom small scenario specialist | Train for branch generation, conditional consequences, delayed effects, and explicit uncertainty. | Intended learned-specialization path |

## Empathy candidates

Empathy is not emotional style or agreement. Candidate implementations should represent stakeholders, burdens, agency, relationship consequences, care-sensitive observations, and uncertainty about inferred human states.

| Candidate | Candidate capability | Initial posture |
| --- | --- | --- |
| [Accumulated Distress Care Protocol](https://github.com/JosephJMWalker-MBA/Accumulated-Distress-Care-Protocol) derived observer | Bounded semantic observation of accumulated distress/care signals while deterministic policy remains outside the model. | Leading first custom-training substrate (`MASI-E001`) |
| [RoBERTa GoEmotions](https://huggingface.co/SamLowe/roberta-base-go_emotions) | Multi-label emotion sensor; useful as one signal, not a complete Empathy implementation. | Small local sensor; MIT at review time |
| [CounselReflect empathy models](https://huggingface.co/CounselReflect) | Research decomposition of empathy-related reactions/interpretations/explorations and rationale extraction. | Prior art / candidate sensors; verify individual model licenses |
| NLI / evidence-support models | Detect when attributed motives or human states outrun textual evidence. | Cross-role Precision component inside Empathy |
| Custom ADCP / stakeholder-impact specialist | Train against bounded observations with evidence spans, negative controls, and abstention. | Intended learned-specialization path |

## Wisdom / outcome-learning candidates

The first Wisdom implementation should not be assumed to be an LLM. The core problem resembles contextual influence learning from observed consequences.

| Candidate | Candidate capability | Initial posture |
| --- | --- | --- |
| [MABWiser](https://github.com/fidelity/mabwiser) | Contextual multi-armed bandit policies including LinUCB, LinTS, Thompson Sampling, UCB, clustering/neighborhood methods. | High-priority first Wisdom baseline; Apache-2.0 at review time |
| [Vowpal Wabbit contextual bandits](https://vowpalwabbit.org/docs/vowpal_wabbit/python/latest/examples/contextual_bandit.html) | Online contextual-bandit learning and policy evaluation. | High-priority baseline / possible implementation |
| [Skywork Reward V2 Qwen3](https://huggingface.co/Skywork/Skywork-Reward-V2-Qwen3-0.6B) | Generic learned preference/reward signal that can be compared with reality-grounded influence updates. | Candidate input or comparator, not presumed Wisdom itself |
| [ArmoRM-Llama3](https://huggingface.co/RLHFlow/ArmoRM-Llama3-8B-v0.1) | Multi-objective reward modeling with learned context-dependent weighting. | Conceptual prior art / comparator; verify license and hardware fit |
| Custom Reality-Audit learner | Learn `context x specialist x prediction x observed outcome -> conditional influence` from MASI Reality Audit records. | Intended long-horizon research path |

## Candidate training substrates

These are not role assignments. They are plausible open bases for creating role-compatible learned specialists.

| Family | Why it is interesting | Preliminary posture |
| --- | --- | --- |
| **Qwen3.5 small/base checkpoints** | Small sizes, strong current open-model ecosystem, suitable for LoRA/full fine-tuning depending size. | High-priority; verify exact checkpoint license and hardware fit |
| [IBM Granite 4.0 Micro / H-Micro](https://huggingface.co/ibm-granite/granite-4.0-micro) | Apache-2.0 compact/hybrid model family designed for practical local workloads. | High-priority substrate |
| **SmolLM3 3B** | Small open reasoning/tool-use substrate. | Candidate; verify current checkpoint/license |
| [Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning) | Compact reasoning-specialized base, MIT. | Candidate Foresight/Precision substrate |
| **GPT-OSS-20B / larger local-capable models** | Useful upper local baseline where hardware permits, but not first fine-tuning target. | Later comparison |

## Candidate record requirements

Before a candidate is integrated into an experiment, record at minimum:

```text
candidate_id
responsibility / function
source + exact version / revision
license + terms review date
model class / parameter count where applicable
runtime / memory requirements
input / output contract
claimed strengths (source-attributed)
known limitations
why MASI needs it
baseline it competes against
experiment(s) in which it is authorized
publication restrictions
observed evidence after testing
```

## Initial fleet for implementation probing

The first executable fleet should be deliberately heterogeneous and should not attempt to install every candidate at once.

```text
GOVERNANCE / CONTROL
  Telos (candidate)
  + simple deterministic governance baseline

ROUTING
  vLLM Semantic Router and/or RouteLLM baseline
  + minimal deterministic router

PRECISION
  HHEM-2.1-Open
  DeBERTa NLI
  Jev as external comparator where terms permit

FORESIGHT
  Chronos or TimesFM for quantitative forecasting
  compact reasoning model for qualitative scenarios

EMPATHY
  ADCP-derived semantic observer
  GoEmotions as a bounded auxiliary sensor

WISDOM
  MABWiser or Vowpal Wabbit contextual-bandit baseline
  Reality Audit record designed before learned outcome weighting
```

The point of this fleet is not to prove that these are the right models. It is to make **interchangeability executable** and begin collecting evidence about where specialized systems add value.

## WP1 bounded integration checkpoint — 2026-09-17

Only `exact-match-v1`, `hhem-2.1` and `nli-deberta-small` are integrated in the fixed [WP1 probe](../experiments/wp1/README.md). Exact model revisions, source/license review dates and model classes are in `probe_candidates.py`; downloaded file hashes and measured parameter counts are in each retained run manifest. The compact `tasksource/deberta-small-long-nli` replaces the registry's deprecated `sileod` candidate for this probe following its model-card recommendation.

All three are authorized only for the WP1 premise/claim support interface, competing against the same deterministic rule and visible synthetic references. They were observed and locally repeated, with [resource measurements and explicit limitations](../experiments/wp1/RESULTS.md). No weights are redistributed; reviewed pinned artifacts declare Apache-2.0. This does not qualify any implementation as canonical, calibrated, independently validated, or ready for broader MASI responsibilities.
