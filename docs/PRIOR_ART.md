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

## Relevant neighboring fields

At minimum, MASI experiments should remain aware of established work in:

- mixture-of-experts systems;
- ensemble learning;
- verifier / critic models;
- router models and learned dispatch;
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
- modular / compositional machine learning;
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

> If an existing router, ensemble, MoE, verifier, bandit, simulator, or workflow already provides the relevant capability, what MASI property remains to be tested?

If the answer is weak, reuse the existing method and narrow MASI.
