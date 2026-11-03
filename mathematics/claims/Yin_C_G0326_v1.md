---
author: Yin
---

# Complete finite-memory integer-filter and Walsh central-lift dichotomies

This retains the complete original 2026-10-07 [L121 mathematical argument](../ledger/Yin_L_G0121_v1.md).
The original ms25_source agent assembled this argument for Yin; the coordinator supplied the nonlinear Walsh extension and finite fourth-moment mechanism.
No current Task/E execution, source acquisition or mathematical program run is selected by this maintenance.

## Statement

Fix a positive-Mahler algebraic unit alpha with monic irreducible P and a unit-circle conjugate, and two-sided iid fair signs.
For every fixed nonzero integer polynomial filter R of degree L, the exact negative-power block identity (2) has at most 2L original input boundary signs and boundary entropy at most 2L log2, even for N<L.
If P does not divide R, its algebraic-sum entropy rate is the original positive h_1; if P divides R, that rate is zero and every block entropy is at most 2L log2.
Its specified noncompact central skew extension has a stationary probability lift and uniformly bounded central cocycles exactly when P divides R; an explicit bounded transfer on the iid preimage space proves sufficiency.
Both linear cases have full symbolic process entropy log2, with exact N log2<=H(v_0,...,v_(N-1))<=(N+L)log2.
These linear conclusions include L=0, fair bits, both algebraic power conventions and overlapping boundary intervals.
For every fixed finite-memory integer rule F, including constant or nonlinear rules, the rational translation-shape Walsh polynomials R_A in (12) give central variance V_beta=sum_A abs(R_A(beta))^2, the exact finite moment/escape bounds (14)--(16), and equivalence of this stationary central lift, central uniform tightness and P dividing every R_A.
In that case v=P(S)g for the explicit rational finite-memory bounded rule (17), and algebraic block entropy is at most 2d log card(Gamma), hence zero rate.
If L<d, central lift forces F constant.
No converse from zero algebraic-sum rate, full symbolic-rate claim for arbitrary nonlinear F, varying-memory conclusion or uniform Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:16 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(19): both boundary orientations and overlap, linear entropy/lift/symbolic/fair-bit dichotomies, full rational Walsh grouping and orthogonality, finite dependence moments and probability, exact divisibility, transfer and finite-range entropy, all nonlinear and fixed-memory limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(19): both boundary orientations and overlap, linear entropy/lift/symbolic/fair-bit dichotomies, full rational Walsh grouping and orthogonality, finite dependence moments and probability, exact divisibility, transfer and finite-range entropy, all nonlinear and fixed-memory limits. |
| dependency | [Exact retained input](Yin_C_G0287_v1.md#endpoint-gram-mahler-entropy) | Exact positive original algebraic-sum rate for m>0, from finite monic Gram/Jensen and posterior comparison, with unit-circle roots allowed. |
| dependency | [Exact retained input](Yin_C_G0319_v1.md#rotated-bernoulli-sums-not-tight) | Complete rotated-sign 1/12 moment estimate and arbitrary dependent lift-to-tightness endpoint argument, plus sufficient LS05 coordinate. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:20 |
| status | proved |
| reason | Adopt the exact complete original theorem and retained argument after actual whole self-review with resolved used inputs, preserving every nonlinear, boundary, moment, actual-noise, finite-window and input-dependent limitation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(19): both boundary orientations and overlap, linear entropy/lift/symbolic/fair-bit dichotomies, full rational Walsh grouping and orthogonality, finite dependence moments and probability, exact divisibility, transfer and finite-range entropy, all nonlinear and fixed-memory limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(19): both boundary orientations and overlap, linear entropy/lift/symbolic/fair-bit dichotomies, full rational Walsh grouping and orthogonality, finite dependence moments and probability, exact divisibility, transfer and finite-range entropy, all nonlinear and fixed-memory limits. |
| dependency | [Exact retained input](Yin_C_G0287_v1.md#endpoint-gram-mahler-entropy) | Exact positive original algebraic-sum rate for m>0, from finite monic Gram/Jensen and posterior comparison, with unit-circle roots allowed. |
| dependency | [Exact retained input](Yin_C_G0319_v1.md#rotated-bernoulli-sums-not-tight) | Complete rotated-sign 1/12 moment estimate and arbitrary dependent lift-to-tightness endpoint argument, plus sufficient LS05 coordinate. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0552_v1.md#current-filter-walsh-finding) | Exact current statement, complete original proof and directly used interfaces; self-reviewed, with exact original findings and actual relationships retained separately. |

## Complete retained argument

<a id="argument"></a>
Let alpha be an algebraic unit with monic irreducible P in Z[t], m=log M(P)>0, and at least one unit-circle conjugate.
Let xi_j, j in Z, be independent fair signs.
Fix a nonzero polynomial

    R(t)=sum_(k=0)^L r_k t^k in Z[t],   r_L!=0,
    v_j=sum_(k=0)^L r_k xi_(j+k).                      (1)

The filtered process v is stationary and takes values in a finite integer alphabet, contained in [-sum|r_k|,sum|r_k|].
It generally has dependent digits.
All logarithms are natural, and L is fixed throughout each word-length limit.
The case L=0 is included by interpreting empty sums and boundaries as zero.

<a id="finite-filter-exact-boundary"></a>
### The exact weighted block identity

For every nonzero complex x and every N>=1, put

    S_N(x)=sum_(i=0)^(N-1) xi_i x^(-i),
    T_N(x)=sum_(j=0)^(N-1) v_j x^(-j).

The change of index i=j+k gives

    T_N(x)=R(x)S_N(x)+B_N(x),                          (2)
    B_N(x)=sum_(k=0)^L r_k x^k [
                sum_(i=N)^(N+k-1) xi_i x^(-i)
                  -sum_(i=0)^(k-1) xi_i x^(-i)].

The displayed signs and powers matter: negative block powers pair with R(x), not R(x^(-1)).
The identity also holds for N<L; overlapping boundary indices cancel algebraically where appropriate.
In all cases B_N depends on at most the 2L inputs indexed by {0,...,L-1} union {N,...,N+L-1}.
Hence

    H(B_N(alpha))<=2L log2.                            (3)

For every unit-circle x, there is also the deterministic bound, uniform over N and all digit sequences,

    |B_N(x)|<=D_R:=2 sum_(k=0)^L k|r_k|.              (4)

No independence between this boundary and S_N is used.

<a id="finite-filter-algebraic-entropy-dichotomy"></a>
### Algebraic-sum entropy has an exact dichotomy

Write H_N=H(S_N(alpha)).
Multiplying S_N(alpha) by alpha^(N-1) and reversing the iid digits shows that H_N is exactly the entropy of the usual positive-power sign sum.
Thus H_N/N tends to its original rate h_1.

If P does not divide R, then R(alpha)!=0.
Multiplication by this field element is injective, and (2)--(3) imply

    |H(T_N(alpha))-H_N|<=2L log2.                       (5)

Indeed each of R(alpha)S_N and T_N is a function of the other together with B_N, so each entropy is at most the other plus H(B_N).
It follows that the filtered algebraic-sum rate exists and equals h_1.

If P divides R, then R(alpha)=0 and (2)--(3) give

    H(T_N(alpha))<=2L log2,
    lim_N H(T_N(alpha))/N=0.                           (6)

The original h_1 is strictly positive here by the direct algebraic-integer estimate in [L G0094](Yin_C_G0287_v1.md#endpoint-gram-mahler-entropy), since m>0.
This positivity is a stated retained input, not an inference from the symbolic rate below.

For comparison, the positive-power filtered block sum has main coefficient R(alpha^(-1)) and analogous boundary terms.
Its criterion is the reciprocal polynomial of P.
In the present unit-circle irreducible setting P is reciprocal up to a nonzero scalar: complex conjugation puts beta^(-1) among its roots, so its reciprocal polynomial shares a root with P and hence is proportional to P.
Thus the same divisibility dichotomy holds for that convention as well.
The proof (2)--(6) itself uses negative powers.

<a id="finite-filter-central-lift-dichotomy"></a>
### The center is tight exactly in the zero-rate case

Fix a unit-circle root beta of P.
Since P is monic and irreducible,

    R(beta)=0  iff  P divides R.                       (7)

If R(beta)!=0, the rotated-sign estimate in [L G0118](Yin_C_G0319_v1.md#rotated-bernoulli-sums-not-tight) and (2),(4) give

    P(|T_N(beta)|>=|R(beta)|sqrt(N/2)-D_R)>=1/12.       (8)

For every fixed radius the threshold eventually exceeds it, so these laws are not uniformly tight.
A possibly dependent bounded boundary cannot cancel this escape.
If R(beta)=0, (4) instead bounds T_N(beta) uniformly.

The exact LS05 central coordinate retained in L G0118 is beta^(N-1)T_N(beta)/P'(beta).
There are finitely many central roots, with nonzero derivatives.
Therefore the entire central cocycle is uniformly tight if and only if P divides R.
If P does not divide R, L G0118's endpoint argument excludes an invariant probability lift to this noncompact central skew extension, even when its central variable may depend on every digit.
This concerns that specified extension, not all possible toral factors.

There is an explicit invariant lift in the divisible case, requiring no use of the hard converse of the source's tightness theorem.
Identify the real central space with conjugation-symmetric tuples over the unit-circle roots.
Let

    (Uc)_beta=beta c_beta,       a_beta=1/P'(beta).

The skew map over the filtered digit law is (v,c)->(S v,Uc+v_0 a).
If P divides R then R(U)=0.
On the underlying iid sign space define the bounded, finite-valued central function

    b(xi)=sum_(j=0)^(L-1) xi_j
                 sum_(k=j+1)^L r_k U^(k-j-1)a.         (9)

The coefficients of xi_1,...,xi_L in b(Sxi)-Ub(xi) are r_1 a,...,r_L a.
Its coefficient of xi_0 is -sum_(k=1)^L r_k U^k a=r_0 a because R(U)a=0.
Consequently

    b(Sxi)-Ub(xi)=v_0 a.                              (10)

The pushforward of the iid law by xi->(v,b(xi)) is an invariant probability lift with bounded central support.
It is not asserted that this particular b is a function of v alone: the lift retains the possibly ambiguous preimage information.
Formula(10) also gives a deterministic bound for the complete cocycle orbit on every such lifted trajectory.

<a id="finite-filter-symbolic-entropy"></a>
### The symbolic process still has full entropy

Let V_N=(v_0,...,v_(N-1)).
It is a deterministic function of the N+L independent input signs.
Given V_N and the first L signs xi_0,...,xi_(L-1), the nonzero leading coefficient r_L permits the recursion

    xi_(j+L)=[v_j-sum_(k=0)^(L-1)r_k xi_(j+k)]/r_L

for j=0,...,N-1.
Thus every fiber of the input-to-output block map contains at most 2^L sign strings.
The chain rule yields the exact finite bounds

    N log2<=H(V_N)<=(N+L)log2,
    lim_N H(V_N)/N=log2.                              (11)

This includes leading zero coefficients and N<L.
For L=0 the nonzero scalar r_0 gives an injective coordinate map and equality H(V_N)=Nlog2.

In particular, P-divisible filtering supplies a stationary central lift and a full-entropy symbolic process while giving zero algebraic-sum entropy.
There is no contradiction with the restricted Salem coding theorem: its additional symbolic support and entropy-preserving hypotheses cannot be dropped.

The same rate conclusions hold for fair {0,1} inputs.
Replacing each sign xi_j by (1+xi_j)/2 makes every filtered algebraic block an injective affine image of the sign block, with a deterministic translation.
The symbolic recursion is unchanged.
For tightness, the central partial sum acquires the deterministic term (R(1)/2)sum_(j<N)beta^(-j), which is uniformly bounded because beta!=1.
Hence that affine digit conversion also preserves the tight/non-tight alternative, rather than merely preserving entropy.

<a id="nonlinear-finite-memory-central-dichotomy"></a>
### The obstruction extends to every finite-memory integer local rule

The coordinator proposed the following stronger extension, including its Walsh decomposition and fourth-moment counting mechanism.
Let now

    F:{-1,1}^{0,...,L}->Z,
    v_j=F(xi_j,...,xi_(j+L)),    mu=E v_0.

The rule may be nonlinear or constant.
Its finite Walsh expansion has rational coefficients, since each coefficient is an integer sum divided by 2^(L+1).
For a nonempty subset B of {0,...,L}, write B=A+ell with min A=0 and ell=min B.
Grouping the coefficients with the same translation shape A gives

    v_j-mu=sum_A R_A(S)Y_(A,j),
    Y_(A,j)=product_(i in A) xi_(j+i),
    R_A(t)=sum_(ell=0)^(L-max A) c_(A+ell)t^ell
                                                    in Q[t]. (12)

Distinct pairs (A,j) give distinct nonempty sets A+j of independent input indices.
Their Walsh characters have mean zero and satisfy exactly

    E[Y_(A,j)Y_(B,k)]=1 if (A,j)=(B,k), else 0.        (13)

They are orthogonal; no independence between all these characters is asserted.

Fix a unit-circle beta and set

    X_j=v_j-mu,      B_F=||X_0||_infinity,
    W_N=sum_(j=0)^(N-1) X_j beta^(-j),
    V_beta=sum_A |R_A(beta)|^2.

For N>=L, apply the index identity (2) separately to every shape.
Each character with time index i in {L,...,N-1} has coefficient beta^(-i)R_A(beta).
Only the at most 2L boundary indices per shape have different coefficients, all bounded in terms of the fixed R_A.
Orthogonality therefore proves

    E|W_N|^2=N V_beta+O_F(1),
    E|W_N|^2>=(N-L)V_beta.                             (14)

The remainder bound is independent of N; it follows by summing the finitely many squared boundary coefficients and subtracting L V_beta.

A separate finite-dependence calculation controls the fourth moment without a limit theorem.
Expand |W_N|^4 and sort the four time indices a<=b<=c<=d.
A nonzero expectation requires b-a<=L and d-c<=L: otherwise the extreme centered variable is independent of the other three, and the expectation is zero.
There are at most N^2(L+1)^2 such sorted choices and at most 24 orderings.
Each expectation has absolute value at most B_F^4, and every phase has modulus one.
Thus

    E|W_N|^4<=24(L+1)^2 B_F^4 N^2.                    (15)

Repeated indices obey the same count.
If V_beta>0, then B_F>0, and for N>=max(1,2L) the elementary second-moment argument of L G0118 gives

    P(|W_N|>=sqrt(N V_beta)/2)
       >=V_beta^2/[384(L+1)^2 B_F^4]>0.                (16)

The mean part of the original weighted sum is mu sum_(j<N)beta^(-j), uniformly bounded because beta!=1.
Therefore (16) proves failure of uniform tightness whenever V_beta>0.

If a central invariant probability lift exists, its necessary tightness condition consequently forces V_beta=0 for any central beta.
Every rational polynomial R_A then vanishes at beta, so irreducibility gives P|R_A in Q[t], for every shape.
Conversely, if all these divisibilities hold, define the rational-valued, bounded finite-memory rule

    g_j=mu/P(1)+sum_A (R_A/P)(S)Y_(A,j).               (17)

Here P(1)!=0, because P is irreducible and has positive Mahler measure.
Equation(12) gives exactly

    v=P(S)g.                                         (18)

Using (9)--(10) with R=P and the stationary input g in place of xi constructs an explicit bounded central lift.
That algebraic transfer identity did not require independent input digits.
Its pushforward from the iid input space still projects onto the actual filtered law.
This proves equivalence, for these finite-memory rules, between a stationary central lift, central uniform tightness, and the divisibilities P|R_A.
No difficult tightness-to-coboundary theorem is required for the converse in this class.

Apply (2) to the representation v=P(S)g.
Since P(alpha)=0, its negative-power algebraic block is determined by at most 2d values of g, where d=deg P.
The finite range Gamma of g gives

    H(sum_(j<N) v_j alpha^(-j))
                          <=2d log|Gamma|,           (19)

so its algebraic-sum entropy rate is zero.
For positive block powers the main coefficient is P(alpha^(-1))=0 by the reciprocity argument above; the same boundary conclusion holds without assuming time-reversibility of the correlated digit process.

There is an additional exact short-memory restriction.
If L<d, every R_A has degree at most L<d.
Divisibility by P forces all R_A to vanish, and (12) makes F constant.
For longer memory, nonconstant rules of the form (18) are possible, as the linear example R=P already demonstrates.

For general F no assertion gives symbolic entropy log2, and no converse from zero algebraic-sum entropy to the central condition is proved.
The full symbolic rate (11) belongs to the nonzero linear-filter case.

### Scope and limits

For every fixed nonzero integer polynomial filter, exactly one of the following occurs: it preserves the original positive algebraic-sum entropy and retains the stationary central-lift obstruction, or it removes that obstruction and leaves only bounded-boundary algebraic entropy.
Full symbolic entropy persists in both cases.

More generally, every finite-memory integer local rule that permits this stationary central lift has zero algebraic-sum entropy by (12)--(19).
This does not classify every zero-rate local rule.
It does not treat memory or coefficients varying with N, infinite-memory filters, arbitrary other input laws, or other central-state constructions.
No uniform Mahler gap follows.
