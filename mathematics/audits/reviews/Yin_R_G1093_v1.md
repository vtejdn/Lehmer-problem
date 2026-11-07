---
author: Yin
---

# Self-review of the coefficient-box Mahler expectation argument

Review time: 2026-11-07T15:01 UTC.
The reviewer is the coordinating AI agent that developed the argument, so this is a self-review.
The inspected input is Yin_C_G0869_v1, its complete statement, source interface and argument in the current authored revision.
This review does not claim independence, formal verification, a new proof of the external source theorem or a priority determination.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Coefficient-box expectation finding](#coefficient-box-expectation-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Coefficient-box expectation finding](#coefficient-box-expectation-finding) | [C869 statement](../../claims/Yin_C_G0869_v1.md#statement) | The exact independent uniform integer sampling law, finite bounds, degree-one formulas, fixed-N logarithmic L2 limit and arithmetic-mean asymptotic. |
| [Coefficient-box expectation finding](#coefficient-box-expectation-finding) | [C869 argument](../../claims/Yin_C_G0869_v1.md#argument) | The entire finite-bound proof, conditional-sign reduction, logarithmic uniform integrability, one- and two-angle characteristic functions, concentration and bounded exponential transfer. |
| [Coefficient-box expectation finding](#coefficient-box-expectation-finding) | [C869 source interface](../../claims/Yin_C_G0869_v1.md#source-interface) | NNS13 arXiv v1 Corollary 1.2, printed/PDF p. 3, its normalization and finite-coefficient conditional application; source statement accepted without proof re-audit. |

<a id="coefficient-box-expectation-finding"></a>
## Whole argument finding

The checked argument establishes the stated bounds and fixed-N asymptotics under the exact sampling law.
The following points are decisive for the mathematical assessment.

The lower finite bounds follow from max(1,|a_0|), not from an assumed norm lower bound.
The upper bounds use angular Jensen and Parseval followed by scalar concavity, and the degree-one expectations and coefficient variance agree with direct exact finite sums.
Adding an independent leading sign preserves the law of the entire absolute-value function after a global sign change because every lower coefficient has a symmetric independent law.
Conditional on coefficient magnitudes, the signed Fourier polynomial divided by sqrt(S_d) has coefficient squared norm exactly one, so every hypothesis of NNS13 Corollary 1.2 is satisfied even when some coefficients vanish.
Its bound is integrated over both signs and angle; it is not misread as a pointwise bound at angles where cancellation can have positive probability.
The bounded-square concentration argument controls the random normalization, including the exponentially rare small-norm event and its logarithmic cost.

The trigonometric covariance averages give circular Gaussian single-angle limits and independent circular Gaussian two-angle limits outside an angular null set.
The deterministic monic term vanishes after division by sigma sqrt(d), and the characteristic-function remainder sums to zero for each fixed N.
The fourth logarithmic moment gives a uniform second moment for mixed products by Cauchy--Schwarz, so first and second angular moments pass to their Gaussian limits.
The resulting limit of the centered logarithmic measure is in L2, which is stronger than its mean-value conclusion.
Exponentiation is handled separately using the deterministic coefficient-norm bound, so the arithmetic mean is not confused with the geometric mean.

No uniform moving-N error, conditioned real-root or unit law, minimum positive Mahler value or Lehmer gap is established by this proof.
The source proof is accepted at its recorded statement scope; all coefficient-law conversions and limiting steps specific to this Claim were checked here.
The self-review found no unresolved mathematical dependency affecting these conclusions.
