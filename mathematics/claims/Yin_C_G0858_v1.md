---
author: Yin
---
# All-place Hankel divisibility and its degree-dependent disk comparison

This fixes the complete author derivation from the continuing S9 determinant investigation on 2026-11-05.
The local-lifting idea originates in [L445](../ledger/Yin_L_G0445_v1.md#paid-lifting); the simultaneous valuation sum, full rational descent and disk-cost comparison below are the present argument.
The selected decision below owns the assessment and exact review evidence.

## Statement

Let P be a monic irreducible reciprocal noncyclotomic integer polynomial of degree d, with unit roots alpha_i, such that every positive power of a root still has degree d.
Put P_n(x)=product_i(1-alpha_i^n x), U=P_2, V=P_4, and H=max_i|alpha_i|.
Let q be an odd prime, zeta a primitive q-th root of unity, K=Q(zeta), and O a full Galois orbit of a nonempty subset I of Z/qZ.
For J in O put D_J(x)=product_(j in J)U(zeta^j x), N_J(x)=product_(j in J)V(zeta^j x), and G_J=(N_J/D_J)^(1/2) with constant coefficient 1.
Assume N_J-D_J belongs to 8 O_K[x] for every J in O.
Let f=sum_(J in O)G_J=sum_(n>=0)a_n x^n and B=d|I||O|.
Then f is an integral nonrational power series, and its shifted Hankel determinants Delta_k=det(a_(i+j+1))_(0<=i,j<k) obey, with L=floor((k-1)/B),

    v_2(Delta_k)>=2k+Lk-B L(L+1)/2.

The valuation of zero is infinity.
The supplied conditions consequently imply log H >= (log 2)/(8B) and m(P)>=(log 2)/(8B).
This conditional bound is weaker than the retained unconditional degree-d house bound; no uniform positive total Mahler gap or automatic all-place mask supply is asserted.

## Preparation and exact remaining inputs

The finite rational-series/Hankel mechanism is already recorded in [the selected HR08 inspection](../audits/literature/HR08/readme.md#selected-hankel-factorization-inspection) and [the formal BR10 convention](../audits/literature/BR10/Yin_U002.md#formal-hankel-rank).
The argument below uses a finite coefficient recurrence and makes no bounded infinite-operator assertion.
The elementary-divisor counting mechanism is already used in [C237](../claims/Yin_C_G0237_v1.md#argument); the finite valuation comparison needed here is proved directly below.
For rationality, [BNZ22, arXiv v3, Section 2.2, Corollary 2.3, printed pp. 5--6](../literature/pdf/BNZ22.pdf) states the exact eventual leading-Hankel-vanishing criterion over a field.
The source defines Delta_(0,m) as the (m+1)-square matrix of coefficients indexed i+j; applying it to (f-f(0))/x matches the shifted determinants below.
The coordinating author read the definitions, Lemma 2.1, Corollary 2.2 and Corollary 2.3 in that edition on 2026-11-05, checking the finite Pad茅 comparison and applicability; no whole-paper proof review is claimed.
The previous local approximation alone supplies neither simultaneous divisibility at every place above 2 nor a complex upper bound smaller than the resulting finite-place contribution.
These are separate necessary hypotheses for the proposed rational determinant comparison.

<a id="all-place-hankel-budget"></a>
## Complete argument

### Simultaneous rank bounds, with rational descent paid

Use the power-stable original input, odd rotation prime q, cyclotomic field K and normalized products G_I from L445.
Let O be one orbit of a nonempty mask I under the full Galois group of K over Q.
For each mask J in O, write D_J and N_J as in L445 and assume the global coefficient condition

    N_J-D_J in 8 O_K[x].

This is an explicit supplied condition at every prime above 2, not a consequence asserted from a relation at one chosen residue place.
Put B=sum_(J in O) deg D_J=d |I| |O|, and define

    f(x)=sum_(J in O) G_J(x)=sum_(n>=0) a_n x^n.

The expansion below proves that every G_J has algebraic-integral coefficients; their Galois-invariant sum therefore has coefficients a_n in Z.
For each J put A_J=(N_J-D_J)/8, so G_J=(1+8 A_J/D_J)^(1/2), with A_J(0)=0 and D_J(0)=1.
For n>=1 the exact coefficient valuation is

    v_2(8^n binom(1/2,n))=2n-v_2(n!)=n+s_2(n)>=n+1,

where s_2(n) is the number of binary digits equal to one.
For s>=2, truncation at n=s-2 therefore gives a rational approximation modulo 2^s with denominator D_J^(s-2) and numerator degree at most (s-2)deg D_J.
For s=1 the constant 1 suffices.
Summing the conjugate approximations over O and using the product of their denominators gives R_s=A_s/Q_s in Q(x), with

    A_s,Q_s in Z[x], Q_s(0)=1,
    deg A_s, deg Q_s <= b_s=B max(s-2,0),
    f-R_s in 2^s Z[[x]].

Indeed the common denominator and numerator are Galois invariant and algebraic integral, and coefficient divisibility at all primes above 2 descends to divisibility by 2^s in Z.
The common denominator may admit cancellation; using its full degree B is a sufficient paid bound and makes no minimality assertion.

Let H_k=(a_(i+j+1))_(0<=i,j<k), and let Delta_k=det H_k.
The shifted coefficient Hankel matrix of each R_s has rank at most b_s over Q_2.
To see this without an operator theorem, the shifted series (R_s-R_s(0))/x has numerator degree less than b_s and denominator degree at most b_s, with unit constant coefficient.
Its coefficients satisfy the denominator recurrence from index b_s onward, so every column from index b_s onward lies in the span of the first b_s columns.
When b_s=0 the shifted series is zero.

For any k-by-k matrix M over Z_2, let e_1<=...<=e_k be its elementary-divisor valuations, allowing infinity for a zero divisor.
If M is congruent modulo 2^s to an integral matrix of Q_2-rank at most b_s, then at most b_s of its e_i are less than s.
For a direct check, put M in diagonal elementary-divisor coordinates.
If e_(b_s+1)<s, the leading (b_s+1)-square block of the approximating matrix has determinant of valuation sum_(i<=b_s+1)e_i: factor 2^e_i from row i and reduce the remaining block modulo 2.
Its reduction is the identity, contradicting the assumed rank bound.
The diagonal coordinates themselves follow by repeatedly choosing an entry of least valuation, clearing its row and column by integral invertible operations, and applying the same step to the remaining block.

Applying this comparison for every s to the same H_k, and summing the counts of e_i>=s, gives

    v_2(Delta_k) >= sum_(s>=1) max(k-b_s,0)
                 =2k+sum_(l>=1) max(k-lB,0).

The inequality includes Delta_k=0 with valuation infinity.
Writing L=floor((k-1)/B), its right-hand side is exactly

    2k+Lk-B L(L+1)/2.

In particular its quadratic coefficient is 1/(2B), whereas optimizing only one of the bounds s(k-b_s) gives quadratic coefficient 1/(4B).
This improvement comes from counting all valuation levels of one determinant; it supplies no new masks and does not remove the factor B=d |I| |O|.

## The actual return to the original gap is still missing

For a nonzero integer Delta_k the proved finite-place comparison would imply

    log|Delta_k| >= (log 2)(2k+Lk-B L(L+1)/2).

Thus a useful complex estimate must beat the quadratic coefficient (log 2)/(2B), with the same input, orbit and determinant convention.
A bound at a different mask, a single local place, or a degree-normalized Mahler measure does not supply that comparison.
For completeness, power-stability excludes a root-of-unity quotient between distinct conjugates of P, since a common positive power would collapse the powered degree.
Coincidence up to a root of unity between a squared and a fourth-powered conjugate is also impossible: their positive absolute Weil heights would be respectively 2h(alpha) and 4h(alpha).
Thus all rotated P_2 P_4 radicands have simple zeros private to their rotation, and parity of valuations at those zeros makes their square classes independent in K(x).
In the resulting multiquadratic extension, the products indexed by distinct masks are linearly independent over K(x), as is seen by applying each sign-change automorphism and the corresponding character projection.
The normalized nonempty-mask terms differ from those products only by nonzero factors in K(x), so their sum f cannot belong to K(x).
The stated Kronecker criterion then ensures that Delta_k is nonzero for infinitely many k.

<a id="cauchy-radius-cost"></a>
## Completing the elementary disk comparison gives only a paid house bound

Let H=max_i |alpha_i|>1 for the original polynomial P.
Every rotated normalized factor G_J is holomorphic on |x|<H^(-4), since neither P_2 nor P_4 has a zero there.
For fixed 0<rho<H^(-4), write M_rho=max_(|x|=rho)|f(x)|.
Cauchy's coefficient estimate gives |a_n|<=M_rho rho^(-n).
Factoring rho^(-i) from row i and rho^(-(j+1)) from column j of H_k, then using the Euclidean row bound on the remaining matrix, gives

    log|Delta_k| <= -k^2 log rho + k log M_rho + (k/2)log k

whenever Delta_k is nonzero.
Here the total factored exponent is sum_i i+sum_j(j+1)=k^2; M_rho is fixed before k tends to infinity.
Along the infinitely many nonzero determinants, compare with the valuation lower bound, divide by k^2, and then let rho increase to H^(-4).
This gives only

    log H >= (log 2)/(8B),
    m(P) >= (log 2)/(8d |I| |O|).

The implication is conditional on the supplied all-place mask condition and the original power-stability hypotheses.
It is already weaker than the unconditional house bound log H>=(log 2)/(4d) retained in [Smy08 U001](../audits/literature/Smy08/Yin_U001.md#smy08-house), since |I| |O|>=1.
The direct primary comparison is Dimitrov's [arXiv:1912.12545v1, Theorem 1, p. 1](https://arxiv.org/pdf/1912.12545v1#page=1), whose statement was checked here; its original proof was not reviewed in this work.
Consequently the simultaneous valuation gain, rational trace and elementary Cauchy estimate together add no Mahler-gap coverage.
The next useful determinant step must improve the actual complex quadratic cost relative to B, or reduce the true approximation-rank cost beyond this full-product denominator bound, on a genuinely uncovered near-one class.
An automatic supply of masks by itself would not close that interface.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T16:28 |
| status | proved |
| reason | Adopt the all-place rational descent, simultaneous Hankel valuation bound and conditional disk consequence after independent R1074 F2. The global divisibility premise is supplied, and the resulting degree-dependent bound is weaker than the retained unconditional house bound; no new gap coverage or Task completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire stated theorem, with all supplied hypotheses, quantifiers and comparison limitations. |
| argument | [Complete argument](#all-place-hankel-budget) | Entire fixed argument through its final consequences and source/application boundaries. |
| support | [Existing house comparison](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only the smy08-house subsection's Dimitrov v1 Theorem 1 at its retained statement/applicability depth, used to compare the weaker conditional consequence. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1074_v1.md#hankel-all-place-whole) | Complete exact statement and argument, including source and comparison interfaces at the finding's stated depth. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
