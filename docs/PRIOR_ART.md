# Prior-Art Posture

MASI Research does not treat novelty as the objective.

The objective is to determine the smallest architecture that accurately solves the research problem while reusing mature methods where they fit.

## Default search order

For substantial additions, search roughly in this order:

```text
libraries / packages
-> existing products / applications
-> academic and industrial research
-> Agent Skills / workflow libraries
-> MCP / tool capabilities
-> custom implementation
```

## Focused lineage for the construction doctrine

The current MASI construction doctrine — purpose-built bounded intelligences composed into broader system-level capability — has substantial antecedents. These should be treated as engineering data, not threats.

### Blackboard systems / Hearsay-II

Hearsay-II and later blackboard architectures are important ancestors for heterogeneous specialist cooperation. The blackboard model separates independent knowledge sources, a shared problem state, and control/scheduling. Hearsay-II used distinct knowledge sources for tasks such as signal segmentation, phoneme identification, word hypotheses, syntax, and semantic interpretation.

Useful references:

- Nii, H. P. (1986), *The Blackboard Model of Problem Solving and the Evolution of Blackboard Architectures*, AI Magazine. DOI: `10.1609/aimag.v7i2.537`
- Nii, H. P. (1986), *Blackboard Application Systems, Blackboard Systems and a Knowledge Engineering Perspective*, AI Magazine. DOI: `10.1609/aimag.v7i3.550`
- Erman et al. (1980), *The Hearsay-II Speech-Understanding System: Integrating Knowledge to Resolve Uncertainty*.

**MASI lesson:** heterogeneous expertise plus explicit shared state and separate control is old and proven enough that MASI should not reinvent it casually. The research question is what changes when the specialists are learned, interchangeable, outcome-accountable, and governed through typed semantic contracts.

### Brooks / subsumption architecture

Rodney Brooks' 1986 layered robot-control architecture built increasing competence from asynchronous, relatively simple task-achieving modules rather than starting with one monolithic world model. Lower-level capabilities continued operating as higher-level capability was added.

Reference:

- Brooks, R. A. (1986), *A Robust Layered Control System for a Mobile Robot*, IEEE Journal of Robotics and Automation, DOI: `10.1109/JRA.1986.1087032`.

**MASI lesson:** build competence incrementally from bounded behavior and add complexity only as capability requires it. This is strongly aligned with the `minimum sufficient intelligence` rule, although MASI differs in governance, semantic contracts, interchangeability, and heterogeneous cognitive responsibilities.

### Global Workspace / IDA / LIDA

Global Workspace-inspired cognitive architectures such as IDA/LIDA use many relatively small processes/modules inside a larger integrated architecture rather than assuming cognition is one indivisible procedure.

Reference:

- Baars, B. J. & Franklin, S. (2007), *An architectural model of conscious and unconscious brain functions: Global Workspace Theory and IDA*, Neural Networks, DOI: `10.1016/j.neunet.2007.09.013`.

**MASI lesson:** system-level cognition emerging from many bounded processes has deep prior art. MASI should study these architectures for coordination, memory, action-selection, and failure modes while avoiding unsupported anthropomorphic transfer.

### Neural Module Networks and modular deep learning

Neural Module Networks dynamically compose reusable learned modules rather than requiring one network to perform every subtask through one undifferentiated path. The broader modular-deep-learning literature separates computation from routing and studies local module updates, transfer, causal inference, program induction, and planning.

References:

- Andreas et al. (2016), *Neural Module Networks*, CVPR, DOI: `10.1109/CVPR.2016.12`.
- Pfeiffer et al. (2023), *Modular Deep Learning*, arXiv:`2302.11529`.

**MASI lesson:** learned modularity and routing are established research areas. MASI-specific work must distinguish purpose-built responsibility contracts, heterogeneous computational paradigms, governance, disagreement, and outcome-grounded influence from generic modular neural computation.

### MRKL systems

MRKL explicitly argues for a systems approach combining large language models with external knowledge sources, neural modules, and discrete reasoning rather than treating the language model as the whole intelligence system.

Reference:

- Karpas et al. (2022), *MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning*, arXiv:`2205.00445`.

**MASI lesson:** retaining an LLM as a language/generalization component while delegating bounded work to specialists is strong prior art. MASI should not claim that idea alone. The sharper research question is whether the LLM can be treated as broad prior/proposal/translation intelligence while bounded specialists, governance, and outcome history retain independent authority.

### Universe Routing / explicit epistemic control

Wang (2026), *Universe Routing: Why Self-Evolving Agents Need Epistemic Control*, formalizes a routing problem in which a system first classifies a question into a reasoning framework or "belief space" and then invokes the corresponding heterogeneous solver rather than averaging incompatible frameworks inside one soft mixture.

Reference:

- Wang, Z. G. (2026), *Universe Routing: Why Self-Evolving Agents Need Epistemic Control*, arXiv:2603.14799, https://arxiv.org/abs/2603.14799

The paper reports a 465M-parameter router over seven epistemic universes, compares hard routing with soft MoE, tests out-of-distribution routing, and studies expansion to new universes under continual learning. These are author-reported results and should be independently reproduced before being imported as MASI evidence.

**MASI lesson:** routing can be an epistemic-control responsibility rather than merely a cost/latency optimization. This is strong convergence with MASI's separation between bounded specialists and a control/routing layer. However, MASI should not inherit the assumption that every real task belongs to exactly one mutually exclusive universe. Many consequential tasks may legitimately require composition across statistical, legal, engineering, human, or other responsibilities.

The highest-value experiment is therefore adversarial rather than confirmatory: reproduce a hard-routing baseline, then construct cross-responsibility tasks where single-universe routing should fail and compare it with typed multi-specialist composition plus explicit disagreement/abstention.

### Decision-native System One models: Jev and Laya

TypeSafe AI publicly introduced Jev on 2026-09-15 as a decision-native "System One" model: unstructured state in, typed probabilistic decisions out, with bounded answer schemas rather than autoregressive string generation.

Within days, open Laya implementations made the same broad interface pattern locally inspectable. The public Laya stack exposes `choice`, `score`, and binary-probability (`noul`) questions in one non-autoregressive forward pass; open Python checkpoints are accompanied by an ONNX/Node runtime. Public project documentation reports Apache-2.0 model weights, while the Receptron Node wrapper is MIT-licensed. Exact licenses and revisions still require per-experiment verification.

Relevant sources:

- TypeSafe AI, *Introducing System One Models & Jev* (2026-09-15): `https://typesafe.ai/blog/introducing-system-one-models-and-jev`
- Laya reference / research repository: `https://github.com/NandhaKishorM/laya`
- Laya benchmark record: `https://github.com/NandhaKishorM/laya/blob/main/BENCHMARKS.md`
- Receptron ONNX / Node implementation: `https://github.com/receptron/laya`

The public Laya evidence is especially useful because it exposes both strengths and limitations. It reports very fast batched local inference, but also substantial task/checkpoint variance, overconfidence before domain calibration, confident failures under language shift, option-budget pressure on high-cardinality choices, and large gains from task-specific fine-tuning. Published Laya-versus-Jev figures are not a single controlled MASI head-to-head and should not be imported as comparative evidence without reproduction.

**MASI lesson:** typed probabilistic decision models are rapidly becoming a reusable implementation class rather than a proprietary one-off. That narrows MASI's claim surface: "use bounded typed decisions instead of prose" is useful prior art, not a sufficient MASI contribution. The research contribution must remain in responsibility-first construction, heterogeneous specialist composition, explicit governance/authority, preserved disagreement, independently measured calibration, provenance, and outcome-grounded influence. Laya is therefore valuable both as an adaptable local comparator and as cautionary evidence against treating confidence-shaped output as authority.

### OpenTelemetry GenAI / MCP observability

OpenTelemetry's current GenAI semantic-conventions work includes development-stage conventions for agent invocation, workflow execution, planning, inference, retrieval/memory operations, tool execution, tool-call metrics, and Model Context Protocol (MCP) tracing.

Primary sources:

- https://github.com/open-telemetry/semantic-conventions-genai
- https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md
- https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md
- https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md

This matters because MASI does not need a bespoke observability protocol merely to preserve mechanical facts such as which agent/workflow ran, which tool was called, which MCP operation occurred, how long it took, or where an execution error surfaced.

**MASI lesson:** execution observability is rapidly becoming commodity infrastructure. MASI-specific work should focus on the semantics that ordinary tracing does not establish: evidence meaning, calibration, disagreement, authority, legitimate execution, governing basis, outcome accountability, and how later outcomes change future influence. A trace is evidence about execution, not epistemic or governance authority.

The privacy boundary is also important. Some OpenTelemetry GenAI attributes that may contain tool arguments or model content are opt-in or sensitive. MASI should preserve enough execution evidence for reproducibility and audit without treating maximal capture as a default.

### FlexOlmo

FlexOlmo independently trains domain experts and later integrates them through domain-informed routing, supporting flexible inclusion/exclusion without joint expert training.

References:

- Shi et al. (2025), *FlexOlmo: Open Language Models for Flexible Data Use*, arXiv:`2507.07024`.
- Code: `https://github.com/allenai/FlexOlmo`

The public implementation describes experts branched from a shared public-mix language-model expert and then trained on their respective domains.

**MASI lesson:** independently trained experts, modular inclusion/removal, and routing are pre-existing modern prior art. FlexOlmo is therefore an important `CONTROL_B`-class comparison: specialization remains inside a shared language-model family rather than starting from each bounded responsibility's minimum sufficient computational form.

### Concept Bottleneck Models

Concept Bottleneck Models first predict human-meaningful concepts and then use those concepts for downstream prediction. Their design supports direct intervention on concept values and examination of how the final prediction changes.

Reference:

- Koh et al. (2020), *Concept Bottleneck Models*, ICML / PMLR 119:5338-5348, `https://proceedings.mlr.press/v119/koh20a.html`.

**MASI lesson:** this is a strong construction primitive for specialists requiring explicit ontologies and causally intervenable intermediate state. MASI should also test for leakage or hidden representations that allow a supposedly explicit bottleneck to be bypassed.

### Modulith (2026 convergence)

Modulith publicly describes independently trained, permanently frozen specialist modules, sparse composition/routing, capability add/remove, attribution, bounded compute, and formal verification goals.

Public source: `https://www.modulith.ai/`

The public site identifies 2026 patent/research activity. That makes it relevant contemporary convergence, not something to ignore. This repository makes **no legal priority conclusion** from public dates alone.

**MASI lesson:** independently trained frozen specialists plus routing and capability control is an active contemporary research direction. MASI must distinguish its own experimental claims through responsibility-first construction, heterogeneous computational forms, explicit governance/authority, preserved disagreement, and Reality-Audit/outcome learning rather than modularity alone.

## Working synthesis

The focused search suggests that the strongest MASI research question is **not** whether specialist composition is novel. It is not.

The more defensible question is whether a system can combine:

```text
purpose-built bounded intelligences
+ potentially different computational paradigms
+ explicit semantic contracts
+ replaceability / interchangeability
+ general-purpose LLM capability where breadth is genuinely useful
+ external governance / authority boundaries
+ preserved disagreement and uncertainty
+ conditional influence earned from measured outcomes
```

without collapsing back into one monolithic general model or one hidden shared representation.

A useful historical hypothesis is that earlier modular systems often paid a large engineering cost for representation translation, natural-language interaction, long-tail inputs, and hand-built integration glue. Modern LLMs may reduce that cost dramatically. This is **a hypothesis to test**, not an established historical explanation.

That gives MASI a balanced posture:

> **Do not ask specialists to reproduce generality, and do not throw away general-purpose models when they provide useful breadth, translation, hypothesis generation, or integration.**

General-purpose models are components. Purpose-built specialists are components. Decision-native systems such as Jev and Laya are components. Governance, provenance, and outcome learning determine how those components may participate and how much authority they earn.

## Relevant neighboring fields

At minimum, MASI experiments should remain aware of established work in:

- blackboard systems and knowledge-source architectures;
- behavior-based / subsumption robotics;
- cognitive architectures and global-workspace systems;
- expert systems;
- mixture-of-experts systems;
- ensemble learning;
- verifier / critic models;
- router models and learned dispatch;
- neural module networks;
- modular deep learning;
- neuro-symbolic systems;
- concept bottleneck / concept-based models;
- multi-agent debate and deliberation;
- tool-using agents;
- model cascades;
- contextual bandits;
- reinforcement learning;
- calibration and selective prediction;
- uncertainty estimation;
- decision theory;
- causal and counterfactual modeling;
- simulation and planning;
- truth-maintenance / provenance systems;
- human-in-the-loop decision support;
- outcome-based evaluation and online learning.

Finding close prior art should narrow or improve MASI, not be treated as a threat.

## Internal lineage

MASI Research currently inherits conceptual lineage from:

- the original MASI defensive disclosure on coordinated heterogeneous model composition under shared governance and audit;
- `masi-bus`, the reference communication schema and example artifact;
- the later disclosure on Deliberative Intelligence, Iterative Consensus, Agreement Matrices, disagreement classification, and Reality Backpropagation;
- related research repositories that may provide bounded experimental substrates.

These documents establish historical continuity. They do not exempt any mechanism from comparison with stronger existing methods.

## Prior-art record standard

When prior art materially changes an experiment, record:

- source / citation;
- what responsibility it already solves;
- what MASI-specific claim remains, if any;
- whether the method is directly reusable, adaptable, or only conceptually adjacent;
- what experiment would distinguish the approaches;
- whether custom implementation is still justified.

## Kill test

Before building substantial custom machinery, ask:

> If an existing blackboard, router, ensemble, MoE, verifier, bandit, simulator, concept model, neuro-symbolic system, or workflow already provides the relevant capability, what MASI property remains to be tested?

If the answer is weak, reuse the existing method and narrow MASI.
