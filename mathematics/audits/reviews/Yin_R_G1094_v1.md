---
author: Yin
---

# Self-review of the small-Mahler probability comparison

Review time: 2026-11-07T15:23 UTC.
The reviewer is the coordinating AI agent that developed C870, so the relationship is self-reviewed.
The inspected revision is Yin_C_G0870_v1, including its exact sampling statement, complete counting and existence proof, source interfaces and counterexample-oriented model comparison.
The review accepts the stated external theorem interfaces at their recorded reading depth; it is not an independent review, a formal verification or a new audit of the external proofs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Small-shell probability finding](#small-shell-probability-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Small-shell probability finding](#small-shell-probability-finding) | [C870 statement](../../claims/Yin_C_G0870_v1.md#statement) | Exact box law, uniform small-value upper bound, all parity counts, finite-height saturation, atom size and counterexample equivalences with varying degree and height. |
| [Small-shell probability finding](#small-shell-probability-finding) | [C870 argument](../../claims/Yin_C_G0870_v1.md#argument) | Complete factorwise reciprocity, zero-root deflation, disjoint core counts, coefficient height bound, finite-degree gap, reciprocal conditioning and positivity logic. |
| [Small-shell probability finding](#small-shell-probability-finding) | [C870 source interfaces](../../claims/Yin_C_G0870_v1.md#source-interfaces) | Exact Smy71 application and the separate BDM07 odd-coefficient and BV19c positive-divisor comparisons, with all stated restrictions and source-proof limitations. |
| [Small-shell probability finding](#small-shell-probability-finding) | [C870 model-selection boundary](../../claims/Yin_C_G0870_v1.md#model-selection-and-remaining-target) | Distinction of Littlewood and ternary laws, lack of a height-one reduction in this argument, exclusion of measure-one mass and the remaining positive lower-bound obligation. |

<a id="small-shell-probability-finding"></a>
## Whole probability comparison finding

The checked proof establishes the complete statement under its exact hypotheses.
The Smyth input is used on irreducible positive-measure factors; zero roots are removed explicitly and measure-one factors are handled by Kronecker.
This justifies reciprocal or anti-reciprocal structure of the entire remaining core, even for reducible sampled polynomials.
The parity counts treat constant coefficients 1 and -1 separately, force the anti-reciprocal middle coefficient to zero in even degree, and count pure monomials once.
The geometric-series identities and constant-five bound agree with exact arithmetic and ternary enumeration through degree five.
The irreducible-event bound correctly excludes anti-reciprocal and odd-degree cases by their roots at 1 or -1.

The elementary-symmetric-function bound retains total Mahler measure and every root multiplicity.
It proves both the covering height B_d and the exact fixed-degree saturation law, including a genuine degree-dependent gap rather than a uniform one.
The smallest positive atom is q^(-d), which is smaller than the proved rarity bound; the upper bound supplies no positivity or exclusion at that scale.
Every positive shell witness supplies an irreducible reciprocal unit factor at a possibly different degree and height, and every such factor is covered by a reciprocal coefficient box.
The conditioning factor q^(-n) is obtained by counting the q^n reciprocal unit polynomials inside q^(2n) unrestricted coefficient vectors.
The comparison explicitly subtracts measure-one mass and does not infer a lower bound from an upper bound or a continuous-volume approximation.

BDM07 is kept at its no-cyclotomic-factor and odd-coefficient hypotheses, so its restriction is not incorrectly imposed on ternary inputs or arbitrary extracted factors.
BV19c Proposition 38 is used only for a positive-measure divisor and under its support and collision-probability hypotheses; its Section 7 estimate is kept separate from RH-conditional results and from the entire-polynomial event.
Neither comparison is a hidden premise of the elementary reciprocity count.
No counterexample sequence, height-one completeness theorem, uniform moving-parameter shell lower bound or new general Lehmer gap is established.
No unresolved mathematical dependency affecting the selected conclusions was found in this self-review.
