---
author: Yin
---

# A conjugate-evaluation resultant bound for the fixed degree-56 trace cell

This auxiliary calculation asks whether the single [fixed cell](trace56_cell.json) contains any monic integer trace polynomial not divisible by the positive-exterior-root Lehmer trace.
It uses the existing [integer resultant mechanism](trace64-resultant.md), but evaluates candidate polynomials at the five Lehmer trace conjugates instead of bounding a degree-nine control at the unknown candidate roots.
No separator, parent, degree or coefficient domain is varied.
The calculation was developed and implemented by its author and has passed the separate [independent auxiliary finding](../../../audits/reviews/Yin_R_G1111_v14.md#fixed-resultant-bound-review).
Its author's checks do not themselves constitute an independent review of the auxiliary argument or the cell preparation.

The [program](trace56_resultant.py) has been executed on that frozen mathematical input.
The separate-maximum resultant criterion fails decisively: its exact value is greater than 537718784, rather than less than one.
This is a failure of the specified sufficient bound, not a feasible integer point or an exclusion of the cell.

## Exact sufficient condition

Let
\[
 A(t)=t^5+t^4-5t^3-5t^2+4t+3
\]
be the monic irreducible positive-exterior-root Lehmer trace, with real roots \(\alpha_0,\ldots,\alpha_4\).
For the fixed ordered rational nodes \(s_0<\cdots<s_{28}\), put
\[
 S(t)=\prod_{i=0}^{28}(t-s_i),\qquad V_i(t)=S(t)/(t-s_i).
\]
Every polynomial in the closed vertex simplex has the form
\[
 Q(t)=\sum_{i=0}^{28}\lambda_iV_i(t),\qquad
 \lambda_i\ge0,\quad\sum_i\lambda_i=1.
\]
This includes the strict alternating-sign cell, for which all weights are positive.
Define the exact real quantities
\[
 b_j=\max_{0\le i\le28}|V_i(\alpha_j)|,
 \qquad B=\prod_{j=0}^4 b_j.
\]
The triangle inequality and the weight sum give \(|Q(\alpha_j)|\le b_j\) for every \(j\).
For integer \(Q\), the monicity of \(A\) gives
\[
 \operatorname{Res}(A,Q)=\prod_{j=0}^4Q(\alpha_j)\in\mathbb Z.
\]
If \(A\nmid Q\), irreducibility makes this resultant nonzero, and hence
\[
                         1\le|\operatorname{Res}(A,Q)|\le B.
\]
Consequently \(B<1\) would force \(A\mid Q\) for every integer point in the full simplex, without a coefficient-height assumption.
Division by the monic integer \(A\) then has integer quotient.

The five separate maxima discard the fact that the same vector \((\lambda_i)\) occurs at every conjugate.
If the bound is at least one, this sufficient test does not decide whether the simplex contains an integer point outside the divisor subspace.
It also does not decide the stronger common-weight resultant bound.
No such optimization is part of this calculation.

## Exact enclosure and finite scope

The program uses standard-library integer and `Fraction` arithmetic throughout.
It first verifies irreducibility of \(A\) modulo two by division by every monic polynomial of degrees one and two.
A reducible degree-five polynomial must have a factor of degree at most two, so these six nonzero remainders suffice.
The polynomial is monic and its degree is unchanged modulo two, giving irreducibility over the rationals.

The five rational sign-changing intervals are
\[
 (-2,-3/2),\quad(-3/2,-1),\quad(-1,0),\quad(0,1),\quad(2,5/2).
\]
They supply five distinct roots and exhaust the degree, so each contains exactly one simple root.
Exactly eighty rational bisections are performed on each interval, without a numerical root solver or an accuracy-dependent retry.
The program checks the final signs, expected widths and disjointness, and that no frozen node lies in a final root bracket.

For every one of the \(5\cdot29=145\) pairs, interval multiplication encloses
\[
 V_i(\alpha_j)=\prod_{k\ne i}(\alpha_j-s_k).
\]
Taking the absolute-value interval and then the maximum of its lower and upper endpoints gives lower and upper bounds for each \(b_j\).
Multiplying these nonnegative endpoints encloses \(B\).
An upper endpoint below one proves the sufficient divisor conclusion.
A lower endpoint at least one proves that this separate-maximum criterion itself cannot have value below one on the frozen cell.
An enclosure straddling one leaves the criterion undecided at the prescribed finite precision.
The exact rational intervals determine these classifications; outward-rounded decimal endpoints are only a readable presentation.

No Mahler estimate, candidate search, factorization, MILP, separator adjustment or height-box optimization is performed.
The existing degree-64 resultant exclusions remain confined to their own inputs and are not transferred to this cell.

## Reproduction and result

The input is the degree-56, trace-degree-28 protocol `S10-fixed-D56-all-real-trace-cell` in [trace56_cell.json](trace56_cell.json).
Its mathematical nodes and qL are read directly; cached vertex coefficients are not used as numerical oracles.
The program checks the specified observation 11542 / DP seed 32 / proposal 448 source locator and whole-variable sign change, the seven specified cyclotomic orders, the exact qL coefficients, strict parent signs at every node, and exact divisibility of the parent trace by qL.
The cell author's [preparation and checks](trace56_cell.py) own the original-parent reconstruction, deterministic separator selection and remaining cell data.
This auxiliary check does not claim a separate independent review of those preparations.

The executed command, normalized to a portable invocation from the repository root, is:

~~~text
python -B mathematics/computations/programs/Yin_J_G0144/trace56_resultant.py --input mathematics/computations/programs/Yin_J_G0144/trace56_cell.json --output mathematics/computations/outputs/Yin_J_G0144/trace56_resultant.json
~~~

The program uses only the Python standard library and refuses to overwrite an existing output.
The executed runtime was CPython 3.14.7.
Use a fresh output path for reproduction.
The generated native [result](../../outputs/Yin_J_G0144/trace56_resultant.json) retains all five final rational root brackets, all 145 vertex-value rational intervals, the five maximum intervals, their product interval, input scope and finite checks.
The fixed cell input, its preparation program and this auxiliary program are the required reproducibility inputs.

The following are outward-rounded decimal enclosures of the exact quantities \(b_j\), with roots in increasing order:

| Root index | Lower endpoint | Upper endpoint |
| --- | ---: | ---: |
| 0 | 252.963549653596 | 252.963549653597 |
| 1 | 9.543346575704 | 9.543346575705 |
| 2 | 47.417198498264 | 47.417198498265 |
| 3 | 9.344354839742 | 9.344354839743 |
| 4 | 502.702855986882 | 502.702855986883 |

The exact rational product interval lies inside
\[
 537718784.872951328062
 \le B\le
 537718784.872951328063.
\]
In particular the rational lower endpoint is greater than one.
The failure is therefore not due merely to an unresolved comparison or an insufficient upper enclosure.
The argument stops at this first separate-maximum bound: no common-weight optimization, additional resultant, alternate separator, new parent, candidate solver or sampling run was attempted.

The author checked the resultant orientation and integer floor, the convex-weight inequality, irreducibility and complete five-root coverage, exact interval multiplication and absolute-value/max operations, and the correspondence of the saved input and displayed output to the stated finite calculation.
The script completed every prescribed check and reported `simple_maximum_product_criterion_insufficient`.
These are ordinary author checks of this auxiliary derivation and program.
The separate independent finding reconstructs every interval and verifies the sufficient criterion and actual failure, without a new project Claim assessment or a cell-feasibility conclusion.
