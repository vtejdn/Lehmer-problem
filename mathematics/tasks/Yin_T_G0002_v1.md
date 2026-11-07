---
author: Yin
---
# Resolve Lehmer's problem in full generality

## Contract

### Original question

Resolve Lehmer's problem for the full class of nonzero polynomials with integer coefficients.
For
\[
f(x)=a_d\prod_{j=1}^{d}(x-\alpha_j)\in\mathbb Z[x]\setminus\{0\},
\]
define its total Mahler measure by
\[
M(f)=|a_d|\prod_{j=1}^{d}\max\{1,|\alpha_j|\},
\qquad m(f)=\log M(f).
\]
Roots are counted with multiplicity, zero roots contribute a factor of one, and the leading coefficient is retained.
For a nonzero constant polynomial the empty product is one.
Put
\[
L=\inf\{M(f):f\in\mathbb Z[x]\setminus\{0\},\ M(f)>1\}.
\]
Determine whether \(L>1\), or \(L=1\).
Equivalently, decide whether the positive values of the total logarithmic measure \(m(f)\) have a uniform gap above zero.

### Scope

Degree and integer coefficients are unrestricted.
The domain includes nonprimitive, nonmonic, reducible and nonreciprocal polynomials, as well as polynomials with roots on the unit circle.
No degree normalization is applied to either measure.
No particular research method, polynomial family or sufficient certificate is imposed by this common contract.
Equivalent arithmetic, dynamical, group-theoretic or operator-theoretic formulations may be used when their implications for this full polynomial problem are rigorously justified.
Any reduction to a smaller class must justify why it resolves the full question.
Determining the optimal numerical value of \(L\) is not required to resolve the positive-gap question.

### Completion criteria

Resolve the common question by one of the following alternatives:

1. Prove that there exists a constant \(c>1\), independent of degree and coefficients, such that every nonzero \(f\in\mathbb Z[x]\) satisfies \(M(f)=1\) or \(M(f)\ge c\).
2. Prove that for every \(\varepsilon>0\) there exists a nonzero \(f\in\mathbb Z[x]\) with \(1<M(f)<1+\varepsilon\), for example by rigorously establishing a sequence of positive logarithmic measures tending to zero.

A result restricted to a special class, a degree-dependent lower bound, a finite numerical search or a single improved positive example is partial progress unless a rigorous argument resolves the full alternative above.
Completion requires an argument covering the whole common contract and an applicable completion review bound to the exact contract and adopted mathematical support.
The review must check the full chain, including any reductions, external premises and uniformity in unbounded parameters, and identify its actual checking relationship and limitations.
No mathematical resolution or completion review is asserted by establishing this Task.

## Task coordination

| Field | Value |
| --- | --- |
| task-type | joint |

This Task owns the common mathematical contract.
Individual participation, strategies and execution conditions remain with each participant's ordinary Task and its applicable execution boundary under the [joint-Task rules](../../framework/rules/tasks.md#joint-tasks-and-participation).
The common Task has no direct strategy or execution boundary.

## Current decision

[Selected decision](#decision-initial)

## Lifecycle and completion

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-11-07T07:46 |
| status | active |
| authority | Yin instructed that a joint Task be established for G0001, with the general Lehmer problem and no additional mathematical restrictions as its common objective. |
| reason | Establish the authorized common contract for collaboration. This setup does not activate or resume an individual's research execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Common Lehmer contract](#contract) | Full integer-polynomial positive Mahler gap or rigorously established arbitrarily small positive logarithmic measures, with unrestricted degree and coefficients and the completion criteria above. |
