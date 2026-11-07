---
author: Yin
---

# MSS15-U001: finite free coefficient normalization and failure of integer closure

<a id="mss15-u001"></a>
## Source and inspected scope

Date: 2026-11-07.
Human record author: Yin.
The coordinating AI agent read the selected original and performed ordinary exact checks of the examples below.
The [source notes](readme.md#yin-arxiv-v2) identify arXiv:1504.00350v2, submitted 3 July 2019, whose title page is dated 4 July 2019.
The retained original has 37 PDF pages.
Complete printed/PDF pp. 1-4 were text-read and visually inspected, including the supplied contents, Definitions 1.1, 1.4 and 1.7, equations (1), (4) and (7), and the neighboring matrix and real-rootedness statements.
The matrix identities and real-rootedness assertions in Theorems 1.2, 1.3, 1.5, 1.6, 1.8 and 1.9 were read as source statements; their proofs in later sections were not audited.
The definitions and direct coefficient substitutions suffice for the arithmetic question here.
This is selected source inspection and ordinary calculation, with no independent whole-paper proof review or new project Claim assessment.

<a id="finite-free-definitions"></a>
## Three finite free convolutions and their coefficient conventions

**Definition (finite free polynomial convolutions at dimension d).**
Fix an integer d>=1 and write two complex polynomials of degree at most d as
\[
 p(x)=\sum_{i=0}^d(-1)^ia_i x^{d-i},\qquad
 q(x)=\sum_{i=0}^d(-1)^ib_i x^{d-i}.
\]
The signed coefficients a_i and b_i are the ordinary monomial-basis coefficients with the displayed signs, not coefficients divided by binomial factors.
Monic degree-d inputs have a_0=b_0=1.
The parameter d is part of the operation even when either input has smaller degree.

Definition 1.1, printed/PDF p. 2, equation (1), defines the symmetric additive convolution by
\[
 (p\boxplus_d q)(x)
 =\sum_{k=0}^d(-1)^k x^{d-k}
   \sum_{i+j=k}\frac{(d-i)!(d-j)!}{d!(d-k)!}a_i b_j.
\tag{A}
\]
Definition 1.4, printed/PDF p. 3, equation (4), defines the symmetric multiplicative convolution by
\[
 (p\boxtimes_d q)(x)
 =\sum_{i=0}^d(-1)^i x^{d-i}\frac{a_i b_i}{\binom di}.
\tag{M}
\]
Definition 1.7, printed/PDF p. 4, equation (7), defines the asymmetric additive convolution by
\[
 (p\boxplus_d^{\mathrm{asym}} q)(x)
 =\sum_{k=0}^d(-1)^k x^{d-k}
   \sum_{i+j=k}\left(\frac{(d-i)!(d-j)!}{d!(d-k)!}\right)^2a_i b_j.
\tag{AA}
\]
The superscript asym is this unit's notation for the source's asymmetric operation, to keep it separate from (A).
All three formulas are algebraic definitions on complex polynomials; real-rootedness is a separate property with the source's stated hypotheses.
The source states that (A) preserves real-rootedness, while (M) and (AA) preserve nonnegative real-rootedness.
The counterexamples below satisfy even the latter input restriction.
For monic degree-d inputs all three outputs remain monic of degree d.
The rational normalization factors do not in general preserve integer coefficients.

<a id="degree-two-integer-counterexamples"></a>
## Exact degree-two counterexamples

Take
\[
 d=2,\qquad p(x)=q(x)=x^2-x,
 \qquad (a_0,a_1,a_2)=(b_0,b_1,b_2)=(1,1,0).
\]
Both inputs are monic integer polynomials with simple nonnegative real roots 0 and 1.
Substitution in (A), (M) and (AA) gives
\[
 \begin{aligned}
 p\boxplus_2p&=x^2-2x+\tfrac12,\\
 p\boxtimes_2p&=x^2-\tfrac12x,\\
 p\boxplus_2^{\mathrm{asym}}p&=x^2-2x+\tfrac14.
 \end{aligned}
\tag{1}
\]
In (A), the i=j=1 summand has weight 1/2; in (AA), the same summand has weight 1/4.
In (M), the coefficient indexed by i=1 is divided by binomial(2,1)=2.
Thus none of the three operations maps all monic integer inputs back into Z[x], even in the nonnegative real-rooted domain.
The three outputs still have nonnegative real roots, namely 1 plus or minus 1/sqrt(2), the pair 0 and 1/2, and 1 plus or minus sqrt(3)/2, respectively.
This separates arithmetic closure from preservation of the permitted root region.

The multiplicative failure persists for irreducible reciprocal unit inputs.
For
\[
 u(x)=x^2-3x+1,
 \qquad
 (u\boxtimes_2u)(x)=x^2-\tfrac92x+1.
\tag{2}
\]
The input has discriminant 5, hence is irreducible over Q, and its two roots (3 plus or minus sqrt(5))/2 are positive algebraic units.
The middle coefficient 9/2 prevents integer closure, despite preservation of the constant coefficient one.
The evaluations in (1)-(2) were checked directly and by Python Fraction arithmetic, without floating-point root calculations.
These are direct specializations of the displayed source definitions, not counterexamples to the paper's theorems.

<a id="rationality-divisibility-and-denominators"></a>
## Rationality, divisibility and denominator clearing

For integer coefficients a_i,b_i, all three outputs lie in Q[x].
For (M), integer output is equivalent to the coefficientwise divisibility conditions
\[
 \binom di\mid a_i b_i\qquad(0\le i\le d).
\tag{3}
\]
There is a single product in each output coefficient, so (3) is both necessary and sufficient.
Integer input coefficients by themselves do not impose these conditions.
For (A) and (AA), the corresponding sums of rationally weighted products must be integral; cancellation can occur, but is not automatic.

The displayed definitions also give the sufficient common denominator bounds
\[
 d!\,(p\boxplus_dq)\in\mathbb Z[x],\qquad
 d!\,(p\boxtimes_dq)\in\mathbb Z[x],\qquad
 (d!)^2(p\boxplus_d^{\mathrm{asym}}q)\in\mathbb Z[x].
\tag{4}
\]
For (A), multiplying a weight by d! leaves (d-i)!(d-j)!/(d-i-j)!, an integer because the factorial in the denominator divides (d-i)!.
For (AA), the same integer is squared after multiplying the weight by (d!)^2.
For (M), d!/binomial(d,i)=i!(d-i)! is integral.
These are sufficient bounds, not claims that the smallest common denominator always has that size.

For a monic rational output r with a fractional coefficient, multiplying by an integer N that clears its denominators gives an integer polynomial with leading coefficient N.
The roots are unchanged but
\[
 m(Nr)=\log N+m(r).
\tag{5}
\]
Thus this scalar operation must retain its leading-coefficient cost in a Lehmer comparison.
It does not establish closure in the original monic integer class.

<a id="arithmetic-brown-application-boundary"></a>
## Boundary for the arithmetic Brown-measure formulation

The [finite arithmetic Brown-measure conditions in L459](../../../ledger/Yin_L_G0459_v1.md#finite-arithmetic-constraints) require the full monic characteristic polynomial to lie in Z[x] at its specified dimension.
Equations (1)-(2) show that the three normalized finite free operations cannot be used as general closure operations for that domain.
The source's expected-characteristic-polynomial interpretation explains why a coefficient average can be rational even when particular sampled characteristic polynomials are integral.
An arithmetic use needs additional divisibility, a specified integral realization, or denominator costs retained in the actual comparison.
Real-rootedness and root bounds alone do not supply those missing arithmetic conditions.
No conclusion about a uniform Lehmer gap is obtained from this inspection.
