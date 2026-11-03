---
author: Yin
---

# Cyclotomic stabilization costs and compressed upper-unitriangular realizations

Date: 2026-10-10.
Fixed retention of the complete D G0057 proof and its full separate noncontributor review under the coordinator's explicit adoption instruction.
The coordinating AI for Yin assigned the realization question and suggested its Pfaffian endpoint test; orbit_research supplied the arguments and constructions; resultant_research independently checked the whole combined proof.
This provenance remains distinct from author self-checking and retention.

<a id="cyclotomic-stabilization-fixed-scope"></a>
## Adopted scope

For an even-degree monic reciprocal integer P with constant term one, the complete argument below gives the exact minimum degree of a cyclotomic product that repairs the Pfaffian square condition while retaining a nonzero value at minus one.
Negative P(-1) forces a Phi2 factor in any exact realization.
This endpoint repair is necessary arithmetic, not a sufficient matrix-realization criterion.

An explicit integral upper-unitriangular weighted-tree construction realizes P_p=t^2-(p-2)t+1 times Phi2 Phi3^(r-1), for primes p>=5, in dimension at most 6 floor(log_4(p-1))+7 with all coefficient and energy costs retained.
Any cyclotomic realization of that same P_p whose multiplier is nonzero at minus one needs dimension at least p+1.
The independently reviewed rank-three congruence also excludes the minimally stabilized polynomial (t+1)(t^2+3t+1), so simply killing the endpoint is not sufficient.

The constructed quadratic family has growing Mahler measure and growing matrix entries.
No universal cyclotomic-stabilized realization, optimized small-measure cover cost or unrestricted G0001 conclusion is adopted.
The classical endpoint fact retains D9's existing source attribution; no new source theorem, J or computation was introduced.
Historical pending-review wording records chronology; this adoption and the complete retained finding determine current scope.
Only heading depth and relative navigation are relocated.

<a id="retained-cyclotomic-stabilization-proof"></a>
## Cyclotomic stabilization at minus one: exact costs and compressed quadratic realizations

Date: 2026-10-10.
Responsible structural/algebraic author inquiry by orbit_research for Yin.
The coordinator assigned the realization question and suggested testing the even-rank Pfaffian condition and odd-rank minus-one factor.
The arguments and constructions below were developed by this agent; no independent review is claimed yet.
G0001 remains active and unresolved.

### Reuse and precise question

Read the [signed-cover and endpoint discussion in D9](../claims/Yin_C_G0002_v1.md), [exact adjacent surgery in D12](../claims/Yin_C_G0003_v1.md), the fixed [cycle/congruence boundary in L184](Yin_L_G0184_v1.md#cycle-surgery-fixed-scope), and the [positive-cover cost and shared-triangle family in L185](Yin_L_G0185_v1.md#positive-cover-cost-fixed-scope).
Those results do not prove unrestricted reciprocal-polynomial realization, and the fixed-rank cycle obstruction is not an obstruction under arbitrary cyclotomic stabilization.
D9 already attributes the classical endpoint-square condition to the retained de la Pena source; it is reused here and is not presented as a new discovery.
No further source theorem, classification or claim of historical novelty is adopted.

For an integral upper-unitriangular n by n matrix V, set

    p_V(t)=det(tV+V^T).

It is monic, reciprocal, of degree n and constant term one.
The question is whether an even-degree monic reciprocal integer polynomial P with P(0)=1 has an exact realization p_V=P C, where C is a product of monic cyclotomic polynomials.
All factors, multiplicities, matrix dimensions and coefficient costs are retained.
Cyclotomic stabilization means this polynomial identity, not an unspecified operation on an existing matrix.

This round separates two allowable classes of C: those with C(-1) nonzero, and those permitting Phi_2=t+1.
It gives an exact necessary endpoint cost in the first class, an explicit logarithmic-dimension construction in the second for a growing-measure quadratic family, and a residual minimal-rank obstruction after a single Phi_2.
It supplies no necessary-and-sufficient criterion for general integral upper-unitriangular realization.

<a id="nonzero-endpoint-stabilization-cost"></a>
### 1. The exact minimum cyclotomic degree that repairs the nonzero endpoint condition

At t=-1, V^T-V is an integral alternating matrix.
In even rank its determinant is the square of its integer Pfaffian; in odd rank its determinant is zero.
Therefore

    n even implies p_V(-1) is a nonnegative integer square;
    n odd implies (t+1) divides p_V(t).                         (1)

This is only a necessary condition.
The odd assertion also follows from reciprocity.

Let C be a cyclotomic product with C(0)=1 and C(-1) nonzero.
Its Phi_1=t-1 multiplicity is even, since that is the only monic cyclotomic polynomial with constant term minus one.
Its Phi_2 multiplicity is zero.
All its remaining factors have even degree.
Consequently deg C is even and C(-1)>0.
The complete evaluations are

    Phi_1(-1)=-2,        Phi_2(-1)=0;
    Phi_(2^k)(-1)=2 for k>=2;
    Phi_(2 p^k)(-1)=p for odd prime p and k>=1;
    Phi_n(-1)=1 in every other case n>2.                      (2)

For completeness, the familiar evaluations at one follow without any classification input.
From t^N-1=product_(e|N) Phi_e(t), division by t-1 and evaluation at one give

    N=product_(e|N,e>1) Phi_e(1).

Induction on N gives Phi_(p^k)(1)=p and Phi_N(1)=1 if N>1 is not a prime power: the proper prime-power divisors already contribute N in the latter case, and contribute p^(k-1) in the former.
For odd n>1, Phi_n(-t)=Phi_(2n)(t), so Phi_n(-1)=1.
For n=2m with m odd>1, the same identity gives Phi_(2m)(-1)=Phi_m(1).
If 4 divides n, negation permutes primitive nth roots, so Phi_n is even and Phi_n(-1)=Phi_n(1).
This proves (2), with n=1,2 checked directly.

Suppose a=P(-1) is nonzero.
If a<0, no C with nonzero endpoint can satisfy (1), because a C(-1)<0.
Thus every cyclotomic realization of such a P must include Phi_2.
This is a genuine necessary factor condition, not a proof that including that factor suffices.

If a>0, let delta be its positive squarefree part: a=s^2 delta with s a positive integer.
Define

    lambda(2)=2,       lambda(p)=p-1 for odd primes p;
    D(delta)=sum_(p|delta) lambda(p).                         (3)

Then D(delta) is the exact minimum degree of a cyclotomic C with C(0)=1, C(-1) nonzero, and a C(-1) a square.
Indeed for every odd prime p dividing delta, (2) requires an odd total multiplicity of factors Phi_(2p^k); each has degree p^(k-1)(p-1)>=p-1.
No other factor contributes that prime to the endpoint.
If 2 divides delta, the Phi_1 contribution has even valuation, so an odd number of factors Phi_(2^k), k>=2, is necessary; each has degree at least two.
These disjoint requirements prove deg C>=D(delta).

Equality is attained at the endpoint level by the explicit polynomial

    C_delta(t)=Phi_4(t)^(1 if 2|delta else 0)
                      * product_(odd p|delta) Phi_(2p)(t).     (4)

It is monic reciprocal, has constant term one, degree D(delta), measure zero and C_delta(-1)=delta.
Hence a C_delta(-1)=(s delta)^2.
When delta=1 the empty product is one and D=0.
No upper-unitriangular matrix for P C_delta has been constructed or inferred from this endpoint calculation.
If a=0, condition (1) already imposes no nonzero-square requirement, and (3)--(4) are not an assertion about that separate case.

<a id="compressed-weighted-arm-realization"></a>
### 2. One minus-one factor permits an explicit compressed construction

The following elementary weighted-arm construction changes the unweighted interacting-triangle family in L185.
Take r>=1 nonzero integers b_1,...,b_r and use vertices 0,a_1,c_1,...,a_r,c_r in that order.
Let V have diagonal one and exactly the strict upper entries

    V_(0,a_j)=-b_j,        V_(a_j,c_j)=-1.

For the cost discussion take all b_j positive.
This is an integral upper-unitriangular weighted tree.
Put s=t+1, F=t^2+t+1 and A=sum_j b_j^2.
Then

    p_V(t)=s F^(r-1) [t^2+(1-A)t+1].                         (5)

To prove the full identity, each two-vertex arm contributes the block

    D=[[s,-t],[-1,s]],       det D=F.

Its coupling row from the central vertex is (-t b_j,0), and the reverse column is (-b_j,0)^T.
The scalar Schur contribution is t b_j^2 s/F.
Thus the determinant in the rational function field is

    F^r [s-t s A/F]=s F^(r-1)(F-A t).

After clearing denominators this is a polynomial identity; no factor is lost at F=0.
All r arms and all integer weights are covered directly, without extrapolation from a finite calculation.

For any integer A>=1 write its base-four expansion A=sum_(j=0)^k d_j 4^j, with d_j in {0,1,2,3}, d_k nonzero and k=floor(log_4 A).
Choose d_j copies of the positive weight 2^j.
Then

    r=sum_j d_j <=3(k+1),
    sum_i b_i^2=A,        max_i b_i=2^k<=sqrt(A).             (6)

The exact dimension is 2r+1, at most 6 floor(log_4 A)+7.
The sum of squared strict upper entries is A+r.
The cyclotomic factor in (5) is precisely Phi_2 Phi_3^(r-1), of degree 2r-1, and has zero logarithmic Mahler measure.
No four-square theorem or unproved compression hypothesis is needed.

For A>=4 the remaining quadratic has a positive expanding root and its reciprocal, so its full logarithmic measure is

    m(p_V)=arcosh((A-1)/2).

Because this V is already its all-negative absolute presentation, the signed double cover from D9 has full polynomial p_V^2 and logarithmic measure exactly 2m(p_V); the extra cover cost equals m(p_V).
This is an achieved cost for these explicit matrices.
It gives neither a global optimum nor canonical simple-graph Coxeter coverage: weights b_j can be larger than one.
The degree compression is accompanied by explicit growing integral entries and growing squared-entry energy.

<a id="prime-endpoint-dimension-separation"></a>
### 3. A necessary large cost versus a realized logarithmic cost for the same target

Let p>=5 be a prime and set

    P_p(t)=t^2-(p-2)t+1.                                    (7)

This is a monic reciprocal irreducible nontorsion unit polynomial.
Its discriminant is p(p-4), which has odd valuation at p and is therefore not an integer square.
Its trace p-2 exceeds two, so its expanding root is real and greater than one.
Its endpoint is P_p(-1)=p.

Every exact cyclotomic realization p_W=P_p C with C(-1) nonzero must, by Section 1, have

    deg C>=p-1,       rank W=2+deg C>=p+1.                   (8)

This is a necessary dimension lower bound for any such representation, not only a tree or adjacent-mutation orbit.
The minimum in (8) is an endpoint minimum; existence of a matrix at that minimum is not asserted.

On the other hand set A=p-1 in (5)--(6).
The explicit weighted-tree V satisfies

    p_V=P_p Phi_2 Phi_3^(r-1),
    rank V=2r+1<=6 floor(log_4(p-1))+7,
    max|V_ij|<=sqrt(p-1),
    sum_(i<j)V_ij^2=p-1+r.                                  (9)

Thus a single Phi_2, together with explicitly controlled Phi_3 factors, changes the required dimension scale from at least linear in p to an achieved logarithmic scale.
Arbitrarily large primes give an unbounded separation.
This does not assert that all polynomials with a repaired endpoint are realizable.

For a small exact instance, p=17 has A=16=4^2 and r=1.
The three by three matrix

    V=[[1,-4,0],[0,1,-1],[0,0,1]]

has p_V=(t+1)(t^2-15t+1), whereas every realization of the same quadratic by a cyclotomic product nonvanishing at minus one has total rank at least 18.
This follows from the symbolic identity, not a numerical root or determinant test.

The measure in this family is arcosh((p-2)/2), which tends to infinity, approximately log p.
The construction therefore tests stabilization mechanisms and their dimension/height tradeoff away from the near-one regime.
It supplies no hypothetical small-measure counterexample, and its quadratic inputs already have a fixed positive gap.

<a id="single-phi2-rank-three-obstruction"></a>
### 4. A single Phi_2 does not by itself solve realization

At rank three write

    V=[[1,a,b],[0,1,c],[0,0,1]],       a,b,c in Z.

Direct determinant expansion gives

    p_V=(t+1)[t^2+(2-a^2-b^2-c^2+abc)t+1].                  (10)

Consequently the derivative at minus one is the integer

    p_V'(-1)=a^2+b^2+c^2-abc.                              (11)

This integer can never be 3 modulo 4.
If all three entries are even it is 0;
if exactly one is odd it is 1;
if exactly two are odd, the square sum is 2 and the product is 0 or 2 modulo 4;
if all are odd, the square sum is 3 and the product is 1 or 3.
Thus the remaining cases give 0 or 2.

For the reciprocal irreducible unit P(t)=t^2+3t+1, one has P(-1)=-1.
Its nonzero-endpoint stabilization is impossible by Section 1.
Adding just Phi_2 kills that endpoint obstruction, but an exact rank-three realization of (t+1)P would force p_V'(-1)=-1, contrary to (11) modulo 4.
Therefore neither the unchanged polynomial nor that minimally stabilized polynomial belongs to the required determinant class.
More cyclotomic factors, or a larger multiplicity of Phi_2, are not excluded by this argument.
The same calculation excludes any rank-three target (t+1)(t^2+q t+1) with q congruent to 3 modulo 4.

This is a coefficient-level constraint after the endpoint has been made zero.
It is deliberately rank-specific; no unsupported all-rank derivative congruence is inferred.
In particular the proof does not classify every integer value of the cubic expression in (11).

### 5. What changed and the next discriminating boundary

The established endpoint condition has an exact stabilization price when its value is kept nonzero.
That price can be genuinely large even for degree-two targets.
The explicit weighted-arm identity then shows that allowing a minus-one root can bypass that price with controlled neutral degree and explicit coefficient/energy growth.
A separate minimal-rank congruence shows that annihilating the endpoint is not itself a realization theorem.
These findings distinguish necessary arithmetic repair, actual matrix construction and the unresolved general sufficiency problem.

The next useful question is whether a nontrivial invariant remains after arbitrary Phi_2/Phi_3 stabilization, or whether a constructive integral upper-unitriangular procedure can handle higher-degree reciprocal targets while tracking every neutral factor, dimension and coefficient cost.
A proposed construction must preserve diagonal ones and full determinant, not just exhibit a rational bilinear form or realize a factor.
The fixed cycle-congruence obstructions and the positive-cover cost theorem remain relevant but do not answer this changed stabilization question.

This round used written exact identities only; no continuing program or J was required, no broad scan was launched, and no new source theorem was adopted.
The author checked the cyclotomic endpoint classification and its parity guard, disjoint prime-valuation lower bounds, denominator clearing in the weighted Schur complement, every base-four cost, irreducibility and measure of (7), and all rank-three congruence cases.
These are self-checks; a complete separate review remains required before fixed adoption.
No universal coverage or unrestricted G0001 conclusion is claimed.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0089_v1.md#cyclotomic-stabilization-independent-review), with its original inspected scope and relationship.



<a id="cyclotomic-stabilization-retention-record"></a>
## Retention record

The complete D57 proof, contribution account and independent finding are retained here at their original scopes.
Actual consumers and the current S1/S3/S6 descriptions point to this fixed home.
No older fixed mathematical version or program/output is changed.
Subsequent substantive work requires a separate responsible draft or version and appropriate review.
