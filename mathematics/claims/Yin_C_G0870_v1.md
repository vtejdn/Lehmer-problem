---
author: Yin
---

# Small Mahler probabilities and the counterexample criterion

The purpose of this bounded sampling analysis is the search for a counterexample to a uniform positive Mahler gap.
It distinguishes a small positive probability, a positive probability lower bound, and an actual family with measures tending to one.
It supplies no such counterexample family and makes no height-one completeness assertion.

<a id="statement"></a>
## Exact probability law and conclusions

Let d,N>=1, q=2N+1, and let P be uniform on the q^d monic polynomials of degree d whose non-leading integer coefficients lie in [-N,N].
This is the [coefficient-box law in C869](Yin_C_G0869_v1.md#statement).
Let theta=1.324717... be the real root greater than one of x^3-x-1 and define
\[
 p_{d,N}(\varepsilon)=\mathbb P\{1<M(P)<1+\varepsilon\}.
\]

For 0<epsilon<theta-1, one has the finite uniform upper bound
\[
 p_{d,N}(\varepsilon)\le\frac{A_d(q)}{q^d}
 \le5q^{-\lceil d/2\rceil},
\tag{1}
\]
where
\[
 A_{2n}(q)=\frac{(q+3)q^n-4}{q-1}\quad(n\ge1),
 \qquad
 A_{2n+1}(q)=\frac{(3q+1)q^n-4}{q-1}\quad(n\ge0).
\tag{2}
\]
A_d(q) counts the entire set of box polynomials that become reciprocal or anti-reciprocal after removing their maximal power of x; it is not asserted to count the small positive-measure event exactly.
For the smaller event that P is also irreducible, its probability is zero in odd degree and at most q^(-d/2) in even degree.

Put
\[
 B_d=2\binom d{\lfloor d/2\rfloor}.
\]
For 0<epsilon<1 and N>=B_d,
\[
 p_{d,N}(\varepsilon)=\frac{K_d(\varepsilon)}{(2N+1)^d},
\tag{3}
\]
where K_d(epsilon) is the finite number of all monic integer polynomials of degree d with 1<M(P)<1+epsilon, without any coefficient restriction.
For each fixed d there is an epsilon_d>0 for which K_d(epsilon)=0 whenever 0<epsilon<=epsilon_d.
Thus varying N at a fixed degree cannot produce a sequence of positive logarithmic measures tending to zero.

The absence of a uniform positive gap is equivalent to
\[
 \forall\varepsilon>0\ \exists d,N:\quad
 p_{d,N}(\varepsilon)>0.
\tag{4}
\]
One may restrict (4) to N=B_d and arbitrarily small epsilon.
Equivalently, one may seek positive small-measure probability in the reciprocal unit model
\[
 \mathcal R_{n,N}=
 \left\{x^{2n}+\sum_{j=1}^{2n-1}a_jx^j+1:
 a_j=a_{2n-j},\ |a_j|\le N,\ a_j\in\mathbb Z\right\},
\tag{5}
\]
which has q^n elements, with n and N allowed to vary.
For sufficiently small positive epsilon, any polynomial witnessing (4) has an irreducible noncyclotomic reciprocal unit factor of positive even degree and measure in the same interval.
The degree and coefficient height of this factor need not equal those of the sampled polynomial.

<a id="source-interfaces"></a>
## Source inputs and exact comparison scope

[Smy71-U001](../audits/literature/Smy71/Yin_U001.md#smy71-statement-and-conventions) supplies the primary nonreciprocal theorem: a monic irreducible integer polynomial with nonzero constant coefficient and 1<M<theta is reciprocal.
Its seven-page published proof has already been inspected at the precise scope retained in that unit.
The factorwise application below accepts that theorem and [Kronecker's boundary](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), without a new proof audit of those external results.

BDM07's published abstract, printed p. 347/PDF p. 1, gives
\[
 m(F)\ge\frac{\log5}{4}\frac{r}{r+1}
\tag{6}
\]
for an odd-coefficient polynomial F of degree r with no cyclotomic factors.
The [selected source inspection](../audits/literature/BDM07/Yin_U001.md#odd-coefficient-gap-interface) accepts this exact statement, without a new full-source proof audit.
It applies in particular to irreducible noncyclotomic Littlewood polynomials.
It is not transferred to a factor that has lost the odd-coefficient condition or to the ternary law {-1,0,1}.
This is a model-selection comparison, not a premise of (1)-(4).

BV19c, Breuillard--Varju, Irreducibility of random polynomials of large degree, Acta Mathematica 223 (2019), printed p. 235/PDF p. 41, Proposition 38, gives a separate estimate for having a small positive-measure divisor.
The [selected published original and reading scope](../audits/literature/BV19c/readme.md) distinguish this unconditional Section 7 result from the paper's RH-conditional irreducibility theorems.
For the box law, set tau=1-1/q.
Its interior collision probability is sum_x mu(x)^2=1/q=1-tau, and the deterministic monic leading coefficient is permitted because the collision bound excludes the two endpoints.
For sufficiently large d with N<=exp(d^(1/10)), the probability of an irreducible divisor Q with
\[
 1<M(Q)<e^{\tau/10}
\]
is at most
\[
 2e^{-c\tau d^{4/5}},
\tag{7}
\]
where c>0 is absolute.
The application explicitly excludes Q=x and measure-one cyclotomic factors; only the positive-measure part of the stated source event is used.
The source statement, hypotheses and Section 7 proof outline were inspected, accepting the published theorem without reconstructing its original Dubickas--Konyagin and Dobrowolski proofs.
A polynomial can have a small-measure divisor while its own measure is large, so (7) concerns a larger event than (1) in its applicable threshold range.
For the entire sampled polynomial's measure, the direct reciprocity count (1) is stronger and needs no support restriction N<=exp(d^(1/10)).
Equation (7) is a source comparison rather than a dependency of (1)-(4).

<a id="argument"></a>
## Complete counting and existence argument

### Reciprocity of the nonzero-root core

Write P=x^kR, where R(0)!=0 unless R=1.
Multiplication by x^k preserves Mahler measure.
Factor R into monic irreducible integer polynomials, retaining multiplicities.
Every factor has measure at least one and at most M(P).
If 1<M(P)<theta, then every factor of positive logarithmic measure is reciprocal by Smyth's theorem.
Every factor of measure one is cyclotomic by Kronecker's theorem, since R has no zero root, and hence is reciprocal or anti-reciprocal.
It follows that R is reciprocal or anti-reciprocal.
Also |R(0)|<=M(R)<theta<2, so R(0)=1 or -1.
The same conclusion holds for M(P)=1 by Kronecker, with the pure monomial x^d handled separately.

### Exact count of the possible cores

For a core of odd degree D=2j+1, either sign of its constant coefficient leaves j independent coefficients, giving 2q^j possibilities.
For a core of even degree D=2j, constant coefficient 1 gives j independent coefficients, while constant coefficient -1 forces the middle coefficient to zero and leaves j-1 independent coefficients.
Thus the even-degree count is q^j+q^(j-1).
These alternatives are disjoint because the constant coefficients differ.
For fixed original degree d, each core degree D determines exactly one power x^(d-D), so the cases do not overlap.
Including x^d itself gives
\[
 A_d(q)=1+
 \sum_{\substack{1\le D\le d\\D\text{ odd}}}2q^{(D-1)/2}
 +\sum_{\substack{2\le D\le d\\D\text{ even}}}
   \bigl(q^{D/2}+q^{D/2-1}\bigr).
\tag{8}
\]
Summing the geometric series proves (2).
For q>=3, (q+3)/(q-1)<=3 and (3q+1)/(q-1)<=5.
Hence A_d(q)<=5q^floor(d/2), proving (1).

An irreducible polynomial in the small positive-measure event has no zero root and is reciprocal.
Anti-reciprocity gives a root 1, and odd-degree reciprocity gives a root -1, so neither can occur for an irreducible noncyclotomic polynomial.
It must therefore have even degree and constant coefficient 1.
There are exactly q^(d/2) reciprocal unit polynomials of that even degree in the box, proving the stated irreducible-event bound.
The geometric-series formulas were checked by exact arithmetic, and direct ternary enumeration through degree five agrees with the count of all deflated reciprocal and anti-reciprocal cores.

### Height bounds and atom size

For P(x)=product_(l=1)^d(x-alpha_l), the coefficient a_j is a sum of binomial(d,j) products of roots.
The modulus of every such product is at most product_l max(1,|alpha_l|)=M(P).
Consequently
\[
 |a_j|\le\binom dj M(P),\qquad 0\le j<d.
\tag{9}
\]
If M(P)<2, all coefficients lie in [-B_d,B_d], proving the finiteness and exact saturation formula (3).
For fixed d the finite set with M<2 has only finitely many values greater than one, so those values have positive minimum distance from one, proving the fixed-degree assertion.

The discrete uniform law also gives the exact arithmetic alternative
\[
 p_{d,N}(\varepsilon)=0\quad\hbox{or}\quad
 p_{d,N}(\varepsilon)\ge q^{-d}.
\tag{10}
\]
Thus an upper bound of order q^(-d/2) can coexist with individual small positive-measure polynomials, whose probability may be only q^(-d).
For fixed d, increasing N beyond B_d makes the probability tend to zero even if K_d(epsilon)>0.
Neither that decay nor a small-probability upper estimate implies the small-value event is empty.
A gap proof using this full-box atom argument would need an upper bound strictly below q^(-d) at one fixed epsilon for every covering degree; no such estimate is established here.

### Counterexample criterion and reciprocal conditioning

Equation (4) follows directly from full support of the finite box laws and the union over d,N of all monic integer polynomials.
For measures below two, integer polynomials of arbitrary nonzero leading coefficient reduce to the monic case after a sign change, since the absolute leading coefficient is an integer at most M(P).
Thus the restriction to monic polynomials loses no possible sequence with M tending to one from above.
Equation (9) permits N=B_d, and the factorwise argument supplies an irreducible noncyclotomic reciprocal factor at each sufficiently small target.
The factor has constant coefficient 1 and even degree, so it lies in some model (5).
Conversely, positive probability of a small positive measure in (5) immediately gives an integer polynomial with that measure.
This proves the reciprocal-model existence equivalence when n,N may vary.

Uniform sampling from (5) uses n independent integer coordinates instead of 2n independent box coordinates.
Inside the original degree-2n box this reciprocal unit subset has probability q^(-n).
If p^R_(n,N)(epsilon) is the small positive-measure probability for (5), then
\[
 p_{2n,N}(\varepsilon)\ge q^{-n}p^R_{n,N}(\varepsilon).
\tag{11}
\]
Conditioning removes the automatically wasted reciprocal-constraint factor; it does not itself make p^R positive.
A counterexample program needs epsilon_j tending to zero and actual parameters n_j,N_j with a proved positive lower bound for p^R, or an explicit polynomial witness for each target.
No lower bound tending to zero can be inferred by reversing an upper bound, and a mean estimate or a limiting root measure supplies no such positivity statement.

<a id="model-selection-and-remaining-target"></a>
## Model selection and the remaining lower-bound target

N=1 is a convenient first coefficient scale rather than the only random-polynomial model.
Monic Littlewood sampling uses independent coefficients -1 or 1, so its squared coefficient norm is exactly d+1 and all coefficients are odd.
The present N=1 box has coefficients -1,0,1, includes zero coefficients and has different arithmetic constraints.
Equation (6) excludes an irreducible noncyclotomic Littlewood counterexample sequence; allowing zeros avoids that particular odd-coefficient theorem.
This does not prove completeness of the ternary box for the unrestricted counterexample problem.
Dividing a polynomial by N changes the leading coefficient and integrality, so variance normalization in a central-limit theorem is not an arithmetic reduction to N=1.

The already retained [C869 expectation](Yin_C_G0869_v1.md#statement) describes the bulk, where the measure has order N sqrt(d) at its stated fixed-N scope.
The target here is the much rarer positive shell next to one.
The relevant remaining task for this sampling approach is a genuine lattice count or constructive family in the reciprocal unit class, retaining total Mahler measure and excluding the measure-one cyclotomic mass.
In particular p_(d,N)(epsilon)=P(M<1+epsilon)-P(M=1), so a positive lower bound for the first probability alone may consist entirely of measure-one polynomials.
No coefficient-box limit, continuous thin-shell volume or unconditioned rarity estimate alone establishes that count is positive.
The [existing coefficient-lattice comparison](../ledger/Yin_L_G0449_v2.md) retains its own precise neighborhood costs and limitations; its source or geometric estimates are not used as a lattice lower bound here.

## Current assessment

[Selected self-reviewed probability comparison](#decision-small-shell-probability)

## Assessment history

### Decision small-shell-probability

| Field | Value |
| --- | --- |
| date | 2026-11-07T15:25 |
| status | proved |
| reason | The complete factorwise counting argument and discrete positivity criterion were self-reviewed with the exact source interfaces and model restrictions retained. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Small-shell probability conclusions](#statement) | Finite coefficient-box bounds, exact parity counts, covering heights and counterexample criteria. |
| argument | [Complete counting and existence proof](#argument) | Smyth factorization reduction, zero-root handling, exact counting, height and atom bounds and reciprocal conditioning. |
| review | [Whole comparison self-review](../audits/reviews/Yin_R_G1094_v1.md#small-shell-probability-finding) | Exact statement, complete proof, source comparisons and remaining lower-bound scope; self-reviewed, without an independent-review assertion. |
