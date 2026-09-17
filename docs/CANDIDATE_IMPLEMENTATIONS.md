# Candidate Implementation Registry

**Status:** exploratory registry  
**Last reviewed:** 2026-09-17

This document tracks candidate implementations, substrates, baselines, reusable primitives, and cautionary evidence for MASI responsibilities. It is intentionally inclusive. Inclusion is **not** endorsement, qualification, architectural authority, or evidence that the candidate should become part of the target architecture.

The governing rules are:

> MASI responsibilities are stable only to the extent that experiments justify them. Implementations remain interchangeable.

> **Existing AI systems are research specimens. They may reveal primitives worth inheriting, implementations worth adapting, baselines worth beating, or technical debt/failure modes worth engineering against. They do not define MASI's theory of cognition.**

See [`CONSTRUCTION_DOCTRINE.md`](CONSTRUCTION_DOCTRINE.md).

A candidate may be a learned model, deterministic system, simulator, statistical learner, external service, or composition of several tools. No candidate becomes canonical because it performs well once or because it currently occupies a named role.

Licenses and provider terms can change. License notes below are preliminary research notes and must be re-verified before integration, redistribution, publication of benchmark results, commercial use, or any form of architectural inspection that terms may restrict.

## Candidate posture vocabulary

Use these labels deliberately:

- **primitive source** — demonstrates a mechanism/objective worth understanding or independently reproducing where lawful;
- **adaptable implementation** — sufficiently bounded, transparent, and licensed to participate directly in MASI experiments;
- **benchmark / comparator** — useful for establishing capability or cost pressure without being inherited architecturally;
- **cautionary evidence** — exposes opacity, coupling, training-lineage debt, state failure, calibration failure, authority confusion, or another design hazard;
- **CONTROL_A** — general-purpose model + role prompt;
- **CONTROL_B** — general/pretrained base + role-specific adaptation/fine-tuning;
- **MASI_TARGET** — purpose-built bounded intelligence designed from the responsibility outward;
- **INFRASTRUCTURE** — routing, evaluation, logging, governance, transport, etc.

A single system may occupy more than one posture depending on the experiment.

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
| [vLLM Semantic Router](https://github.com/vllm-project/semantic-router) | Programmable Mixture-of-Models routing/control layer across heterogeneous model paths; strong prior art for MASI routing. | Infrastructure baseline / possible reusable implementation |
| [RouteLLM](https://github.com/lm-sys/RouteLLM) | Learned routing strategies and local-model routing; useful scientific baseline for strong-vs-weak selection. | Benchmark / routing primitive source |
| [Plano-Orchestrator-4B](https://huggingface.co/katanemo/Plano-Orchestrator-4B) | Specialized orchestration model that selects agents/models and sequencing. | Comparator / cautionary licensing review |
| [Arch-Router-1.5B](https://huggingface.co/katanemo/Arch-Router-1.5B) | Small learned router aligned to user-defined preferences/domains. | Comparator / primitive source; verify license constraints |
| [Salesforce xRouter](https://huggingface.co/Salesforce/xRouter) | Learned routing with quality/cost tradeoff objective. | Comparator / primitive source; verify current noncommercial terms |
| [Aurelio Semantic Router](https://github.com/aurelio-labs/semantic-router) | Cheap embedding-space routing baseline. | Baseline MASI should beat where routing is claimed to matter |

## Precision research specimens

Precision should not mean "a model prompted to sound precise." Research should identify the minimum machinery required for bounded judgment, evidence support, contradiction, constraint satisfaction, abstention, calibration, and verification.

| Candidate | What it can teach / test | Initial posture |
| --- | --- | --- |
| **Jev / TypeSafe AI** | Decision-native bounded outputs, scores/probabilities, repeated judgments; useful evidence that intelligence can be designed around decision primitives rather than chat. | External comparator / primitive source only within provider terms |
| [Vectara HHEM-2.1-Open](https://huggingface.co/vectara/hallucination_evaluation_model) | Evidence-premise vs generated-claim factual consistency. | Adaptable verifier / benchmark; inspect architecture and limitations |
| [DeBERTa-v3 Tasksource NLI](https://huggingface.co/sileod/deberta-v3-base-tasksource-nli) | Entailment / contradiction / zero-shot bounded classification. | Adaptable baseline / primitive source |
| [DeBERTa-v3 large MNLI/FEVER/ANLI/WANLI](https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli) | Claim support and adversarial NLI exposure. | Comparator / primitive source |
| [Skywork Reward V2 Qwen3 family](https://huggingface.co/Skywork/Skywork-Reward-V2-Qwen3-0.6B) | Small reward/judgment models; useful for ranking/evaluation experiments. | Comparator / CONTROL_B-family research specimen |
| Fine-tuned small general base | Tests whether ordinary adaptation is enough. | **CONTROL_B, not presumed target** |

### Purpose-built Precision target direction

Begin from the responsibility outward: explicit evidence objects, constraints, contradiction states, uncertainty, abstention, and calibration. Candidate architectures may combine small classifiers, probabilistic models, constraint solvers, evidence graphs, monotonic models, or other bounded machinery. Complexity must be earned by measured deficits.

## Foresight research specimens

Foresight should use domain-appropriate prediction machinery rather than forcing all future-state estimation through prose generation.

| Candidate | What it can teach / test | Initial posture |
| --- | --- | --- |
| [Amazon Chronos](https://github.com/amazon-science/chronos-forecasting) | Specialized zero-shot time-series forecasting family. | Primitive source / adaptable quantitative baseline |
| Chronos-Bolt family | Very small forecasting specialists; tests whether tiny domain systems add disproportionate value. | Primitive source / benchmark |
| [Google TimesFM](https://github.com/google-research/timesfm) | Time-series foundation models with multivariate/covariate support in current generations. | Comparator / primitive source; check version-specific terms |
| [Salesforce Moirai / uni2ts](https://github.com/SalesforceAIResearch/uni2ts) | Universal forecasting and expert-selection prior art. | Comparator / primitive source; verify version-specific terms |
| [Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning) | Compact general reasoning baseline for qualitative scenarios. | CONTROL_A / CONTROL_B substrate, not target by default |
| Fine-tuned small scenario model | Tests adaptation value for qualitative future reasoning. | **CONTROL_B** |

### Purpose-built Foresight target direction

Start from explicit world state, intervention/state-transition representation, temporal horizon, uncertainty, causal assumptions, simulation, and forecast error. Different subproblems may require different bounded mechanisms rather than one universal Foresight network.

## Empathy research specimens

Empathy is not emotional style or agreement. Research should model stakeholders, burdens, agency, relationship consequences, care-sensitive observations, and uncertainty about inferred human states.

| Candidate | What it can teach / test | Initial posture |
| --- | --- | --- |
| [Accumulated Distress Care Protocol](https://github.com/JosephJMWalker-MBA/Accumulated-Distress-Care-Protocol) | Bounded observation ontology with deterministic downstream policy separated from semantic interpretation. | Leading ontology / evaluation substrate for `MASI-E001` |
| [RoBERTa GoEmotions](https://huggingface.co/SamLowe/roberta-base-go_emotions) | Multi-label emotion sensor; demonstrates a narrow learned detector. | Primitive source / auxiliary baseline |
| [CounselReflect empathy models](https://huggingface.co/CounselReflect) | Decomposition of empathy-related reactions/interpretations/explorations and rationale extraction. | Prior art / primitive source / comparator |
| NLI / evidence-support models | Detect when attributed motives or states outrun evidence. | Cross-role primitive / adaptable bounded component |
| Fine-tuned general-model semantic observer | Tests whether standard adaptation is enough. | **CONTROL_B** |

### Purpose-built Empathy target direction

Define the native ontology first: evidence spans, stakeholder identity, burden, agency, isolation/rupture/shame/exhaustion or other justified care concepts, unsupported inference, relationship risk, and uncertainty. Then engineer the minimum system capable of recovering and updating those concepts. Generative empathy style is not the objective.

## Wisdom / outcome-learning research specimens

The first Wisdom implementation should not be assumed to be an LLM. The core problem resembles conditional influence learning from observed consequences.

| Candidate | What it can teach / test | Initial posture |
| --- | --- | --- |
| [MABWiser](https://github.com/fidelity/mabwiser) | Contextual multi-armed bandit policies. | High-priority adaptable baseline / primitive source |
| [Vowpal Wabbit contextual bandits](https://vowpalwabbit.org/docs/vowpal_wabbit/python/latest/examples/contextual_bandit.html) | Online contextual-bandit learning and policy evaluation. | High-priority baseline / possible adaptable implementation |
| [Skywork Reward V2 Qwen3](https://huggingface.co/Skywork/Skywork-Reward-V2-Qwen3-0.6B) | Generic learned preference/reward signal. | Comparator; not presumed Wisdom |
| [ArmoRM-Llama3](https://huggingface.co/RLHFlow/ArmoRM-Llama3-8B-v0.1) | Multi-objective reward modeling with learned context-dependent weighting. | Conceptual prior art / comparator |
| Generic language-model "Wisdom" fine-tune | Tests whether stylistic/general adaptation contributes anything. | CONTROL_B only unless evidence radically changes the design case |

### Purpose-built Wisdom target direction

Begin with explicit Reality Audit records and inspectable updates over `context × specialist × prediction × confidence × observed outcome -> conditional influence`. Compare deterministic weighting, Bayesian updates, and contextual-bandit methods before introducing opaque neural complexity.

## General/pretrained model substrates

These are **not intended role assignments**. They are useful for `CONTROL_B`, tooling, translators, synthetic-data experiments, and upper/lower baselines.

| Family | Why it is interesting | Preliminary posture |
| --- | --- | --- |
| **Qwen3.5 small/base checkpoints** | Small sizes and mature adaptation ecosystem. | CONTROL_B substrate; verify exact checkpoint license/hardware fit |
| [IBM Granite 4.0 Micro / H-Micro](https://huggingface.co/ibm-granite/granite-4.0-micro) | Compact/hybrid model family designed for local workloads. | CONTROL_B substrate / tooling candidate |
| **SmolLM3 3B** | Small open reasoning/tool-use substrate. | CONTROL_B / baseline candidate |
| [Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning) | Compact reasoning-specialized base. | CONTROL_A/B substrate |
| **GPT-OSS-20B / larger local-capable models** | Useful upper local baseline where hardware permits. | Comparator / tooling, not first target |

## Candidate record requirements

Before a candidate is integrated into an experiment, record at minimum:

```text
candidate_id
responsibility / function
implementation_class: CONTROL_A | CONTROL_B | MASI_TARGET | INFRASTRUCTURE
research_posture: primitive_source | adaptable | comparator | caution
source + exact version / revision
license + terms review date
model/system class + parameter count where applicable
runtime / memory requirements
input / output contract
claimed strengths (source-attributed)
known limitations / architectural debt
what MASI is trying to learn from it
baseline it competes against
experiment(s) in which it is authorized
publication / inspection restrictions
observed evidence after testing
```

For every `MASI_TARGET`, also record:

```text
bounded responsibility
allowed inputs
native ontology / state
outputs
uncertainty / abstention semantics
learning / update signal
transparent baseline
capability deficit justifying each major complexity increase
```

## Initial fleet for implementation probing

The first executable fleet remains deliberately heterogeneous, but its purpose is **measurement and architectural learning**, not fleet selection.

```text
GOVERNANCE / CONTROL
  Telos (candidate infrastructure)
  + simple deterministic governance baseline

ROUTING
  vLLM Semantic Router and/or RouteLLM
  + minimal deterministic router

PRECISION SPECIMENS
  HHEM-2.1-Open
  DeBERTa NLI
  Jev as external comparator where terms permit

FORESIGHT SPECIMENS
  Chronos or TimesFM for quantitative forecasting
  general reasoning model only as qualitative control

EMPATHY SPECIMENS
  ADCP ontology / fixtures
  GoEmotions / CounselReflect as narrow sensors or prior art
  adapted general model as CONTROL_B

WISDOM SPECIMENS
  explicit weighting
  MABWiser / Vowpal Wabbit
  Reality Audit record before neural complexity
```

The point of this fleet is to make interchangeability executable and learn what should be **built differently**. Existing model success is evidence about useful primitives or baselines; it is not proof that the final MASI specialist should inherit the same architecture.
