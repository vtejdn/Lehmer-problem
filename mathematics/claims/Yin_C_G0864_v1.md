---
author: Yin
---
# Near-one binary reflection congruences lie in finitely many frequency planes

Human author Yin.
The sign_obstruction contributor developed this arithmetic consequence of the accepted four-pair torus theorem under the original G0001 auxiliary-supply inquiry.
The proof is contributor work, not an independent review.
The selected assessment and separate independent review are recorded in the decision below.
It concerns the same original minimal polynomial, unit field, full algebraic integrality and degree-linear window throughout.

## Exact inputs and contribution

The [adopted C863 v2](Yin_C_G0863_v2.md#decision-whole-independent-review-2026-11-04) supplies the finite bad rank-two hosts and exceptional circles at its precise fixed margin.
The [adopted C141 zero-removal assembly](Yin_C_G0141_v1.md#decision-isolated-whole-review-20261023-m04), specifically [Section 1](Yin_C_G0141_v1.md#reuse-zero-removal), transfers a supplied sparse auxiliary's strict logarithmic margin to the original unit, including a possibly zero value.
The [adopted C862](Yin_C_G0862_v1.md#decision-whole-independent-review-2026-11-04) excludes at most three reflected pairs below its original-window threshold.
These are the mathematical dependencies.

The new contribution is the original-input support confinement with complete parity and normalization, its quadratic count of possible normalized binary words, and the resulting additive-energy bound for a reciprocal unit's dyadic trace code.
It supplies a necessary restriction on hypothetical near-one inputs rather than automatic existence of an auxiliary.
The hosts, their rational planes and the count constants are qualitative finite objects; no effective enumeration is supplied by the input theorem.

## Statement

Fix once and for all

    eta_0=11/12150, eta_*=eta_0/2=11/24300,
    b_0=log2-eta_*.

Choose the finite host tori H_1,...,H_r and exceptional circles E_1,...,E_t furnished by C863 v2 Part 9 at this threshold.
Let W_i=L(H_i)^perp subset R^4 and U_j=L(E_j)^perp subset R^4, where L denotes the integer annihilator lattice.
Then each W_i is a rational plane of dimension two and each U_j a rational line.
These finite collections depend only on the fixed four-pair template and threshold, not on a polynomial, its degree or a window constant.

For C>0 define

    K0=(log2/4)/(2*36^8*5^64),
    Delta_8(C)=min{g(8,8,C,eta_*), K0*8^(-64)/C},
    eta_3=(1/8)log(128/105),
    Gamma_3(C)=min{g(6,6,C,eta_3), K0*6^(-64)/C},
    delta(C)=(1/2)min{Delta_8(C),Gamma_3(C)}>0.           (SC1)

Here g is exactly the positive bounded-term constant in [C139](Yin_C_G0139_v1.md#statement), used through C141.
It retains the accepted fixed Turan--Nazarov source constant and source-inspection limits.
No numerical value of delta(C) is asserted.

Let alpha be an actual nontorsion algebraic integer unit with monic irreducible minimal polynomial P of original degree d and total logarithmic Mahler measure m(P).
Assume

    0<m(P)<=delta(C).                                  (SC2)

Write K=Q(alpha), and let O_K be its full ring of integers.
A normalized binary reciprocal word means a polynomial R in F_2[x] with constant coefficient1, degree T>=1, R(x)=x^T R(1/x), and exactly 2s nonzero coefficients for some 1<=s<=4.
Write its canonical integer lift, with all displayed coefficients equal to1, as

    R_tilde(x)=sum_(j=1..s)(x^(T-e_j)+x^(e_j)),
    0=e_1<e_2<...<e_s<T/2.                            (SC3)

The following conclusions assume (SC2), with each auxiliary condition imposed only where stated.

A. For every word (SC3) satisfying T<=Cd and algebraically integral R_tilde(alpha)/2 in O_K, allowing zero, necessarily s=4.
   Order the four positive integers b=T-2e_j increasingly, so

    0<b_1<b_2<b_3<b_4=T,   b_j congruent to T modulo2.

   The vector b belongs to at least one W_i or U_j.
   Equivalently, every admissible eight-term reflected support on a sufficiently near-one original input satisfies two independent fixed rational linear frequency relations from the finite plane list, or lies on one of the finite exceptional lines.

B. In particular, under A's window condition, A applies whenever the full polynomial P mod2 divides R in F_2[x], with all reduction multiplicities retained.
   No squarefree reduction, good prime, maximal-order equality or power-degree preservation hypothesis is required.
   An arbitrary monomial shift of a binary word may be removed before applying this assertion, and the window is its true normalized exponent span.

C. For each integer N>=1 with N<=Cd, the number of normalized binary reciprocal words with exactly eight terms, span at most N and integral R_tilde(alpha)/2 is at most

    r N^2+t N.                                         (SC4)

   The same bound holds for the subset of those words divisible by P mod2.
   There are no corresponding integral normalized words with two, four or six terms.
   The count concerns binary supports, not the number of integer lifts, signs or monomial shifts.

D. Suppose in addition that P is reciprocal.
   Put F=Q(alpha+alpha^(-1)), so [F:Q]=d/2, and let O_F be its full ring of integers.
   For every integer N>=1 with 2N<=Cd define

    tau_a=(alpha^a+alpha^(-a)) mod2O_F, 1<=a<=N,
    Phi_N:F_2^N -> O_F/2O_F, e_a -> tau_a,
    C_N=ker Phi_N,
    A_N={tau_1,...,tau_N}.

   The linear code C_N has no nonzero word of weight at most three.
   If B_4(N) is its number of weight-four words, then

    B_4(N)<=r N^2+t N.                                 (SC5)

   In particular A_N has N distinct nonzero elements and is disjoint from A_N+A_N.
   Its ordered additive energy satisfies the exact identity and upper bounds

    E_N=#{(a,b,c,e) in {1,...,N}^4:
                    tau_a+tau_b=tau_c+tau_e}
       =3N^2-2N+24B_4(N)
       <=(3+24r)N^2+(24t-2)N
       <=C_* N^2,   C_*=3+24(r+t).                    (SC6)

   Consequently

    |A_N+A_N|>=N^2/C_*,
    2^(d/2)>=N+N^2/C_*.                               (SC7)

E. Consider any actual integer seed H with H(0)!=0, degree k, coefficient energy at most4 and H different from the constants +2 and -2.
   Let n be a positive integer, sigma in {+1,-1}, H*(x)=x^k H(1/x), and V=x^n H+sigma H*.
   Under (SC2), integral V(alpha)/2 and n+k<=Cd, the full reduction V mod2 must have exactly four reflected pairs, and its frequencies obey A with T=n+k.
   This is a restriction on every supplied seed and shift; it constructs neither.

Parts A--C and E do not require reciprocity or power stability of the original P.
Part D uses reciprocity only for the trace field and degree d/2.
Thus all conclusions apply to the reciprocal power-stable near-one core selected by the original research problem.
No hypothetical sequence with m(P) tending to zero is asserted to exist.

<a id="normalization-and-original-integrality"></a>
## Original-field integrality and monomial normalization

For a monic unit minimal polynomial P, its constant coefficient is +/-1.
Thus alpha^(-1) belongs to Z[alpha], and every integral monomial shift of alpha is a unit in both Z[alpha] and O_K.
Removing such a shift preserves algebraic integrality of a quotient value divided by2.

Let an unnormalized nonzero binary polynomial be x^u R, with R(0)=1.
If P mod2 divides x^u R, then it divides R: P mod2 has constant coefficient1 and is relatively prime to x.
This argument uses full polynomial divisibility and does not discard repeated factors.

For a normalized R, perform integer monic division of its canonical lift:

    R_tilde=P Q+S,   Q,S in Z[x], deg S<d.

If P mod2 divides R, reduction of this monic division gives S mod2=0.
Hence R_tilde(alpha)/2=(S/2)(alpha) belongs to Z[alpha] and therefore to O_K.
There is no assumption that Z[alpha] is the full ring of integers.

More generally, any two integer or Laurent lifts of the same binary word differ coefficientwise by twice an integer Laurent polynomial.
Since alpha and alpha^(-1) are algebraic integers, their quotient values divided by2 are simultaneously integral.
This explains why the theorem may begin with any actually integral lift, even without full monogenic-order divisibility.
It does not assert that full O_K integrality conversely implies divisibility by P mod2.

A normalized reciprocal binary word of even weight has no nonzero central coefficient: all noncentral coefficients occur in reflection pairs, so a central term would give odd weight.
Its endpoints are nonzero, giving the expression (SC3).
The stated T is its true exponent span after normalization.

<a id="same-input-signs-and-parity"></a>
## Every sign lift on the same original input

For the supported pairs in (SC3), every sign choice gives

    A_epsilon(x)=sum_(j=1..s) epsilon_j
                         (x^(T-e_j)-x^(e_j)).          (SC8)

All these polynomials reduce to R modulo2.
Thus A_epsilon(alpha)/2 is integral in the same O_K whenever R_tilde(alpha)/2 is integral.
The 2s terms are distinct; the nonzero constant and leading coefficients are +/-1.
Each A_epsilon has actual degree and span T, coefficient length 2s and at most eight terms.
No choice of sign changes the field, original degree, denominator or physical window.

For s<=3, the adopted C862 original-window assertion gives m(P)>Gamma_3(C).
This contradicts m(P)<=delta(C)<Gamma_3(C), proving s=4.

For four pairs, put b=T-2e_j and reorder b increasingly.
Each b_j is positive, the entries are distinct, all have the parity of T, and their maximum is T.
Equation (SC8) becomes

    A_epsilon(x)=sum_(j=1..4)epsilon_j
        (x^((T+b_j)/2)-x^((T-b_j)/2)).                 (SC9)

On x=exp(i theta) its absolute value is

    |A_epsilon(exp(i theta))|
       =|2sum_j epsilon_j sin(b_j theta/2)|.

With u=theta/2, the normalized logarithmic integral becomes the mean over u in [0,pi].
Because all b_j have the same parity, replacing u by u+pi changes the entire sine sum by the common sign (-1)^T.
Its absolute value is pi-periodic.
The mean on [0,pi] therefore equals its normalized full-circle mean, giving

    m(A_epsilon)=m_(H_b)(F_epsilon),
    H_b={ (z^(b_1),...,z^(b_4)): z in T }.              (SC10)

This handles both even T and odd T without adjoining roots, changing alpha to a power or replacing its original degree.
All logarithms are integrable because the actual polynomials are nonzero.

<a id="strict-original-threshold-and-confinement"></a>
## The original near-one threshold forces a bad torus

Suppose some sign in (SC8) satisfied m(A_epsilon)<=log2-eta_*.
The exact C141 zero-removal assembly applies with support bound8, coefficient length8, denominator2, margin eta_* and the original window constant C.
It applies even if A_epsilon(alpha)=0.
It would give

    m(P)>Delta_8(C).

But (SC2) and (SC1) give m(P)<=delta(C)<=Delta_8(C)/2<Delta_8(C).
This is impossible.
Consequently every sign satisfies the strict inequality

    m_(H_b)(F_epsilon)=m(A_epsilon)>log2-eta_*=b_0,
    g(H_b)>b_0.                                       (SC11)

The half-sized cutoff is deliberate: no equality case at the transfer boundary is hidden.
The four positive distinct frequencies ensure H_b belongs to the admissible torus space of C863 v2.
Its finite-host conclusion now implies H_b subset H_i for some i, or H_b=E_j for some j.

For any c in Z^4 the character z^c restricted to H_b equals z^(c dot b).
It is identically one precisely when c dot b=0.
Therefore H_b subset H_i is equivalent to b in L(H_i)^perp=W_i.
Likewise H_b=E_j implies b in U_j.
Conversely a nonzero b in that line gives a connected circle contained in E_j, hence the same circle.
This proves A and the confinement portion of B directly on the original arithmetic input.

No limiting sequence of input polynomials or two-sided Mahler convergence is needed in this argument.
The finite hosts are used at their already proved fixed threshold, after the actual C141 original-window comparison.

<a id="quadratic-support-count"></a>
## Counting normalized eight-term binary supports

For a normalized eight-term word, the sorted vector b uniquely determines T=b_4 and all eight exponents by (SC9).
Its entries lie in {1,...,N} when the span is at most N.
The common parity and strict ordering conditions only reduce the number of such vectors.

Every two-dimensional real linear plane in R^4 has two coordinate projections whose combined restriction is injective.
To see this, take a matrix whose columns form a basis of the plane; its rank is two, so two rows are linearly independent.
The resulting pair of coordinates determines the plane vector uniquely.
Hence each W_i contains at most N^2 integer vectors in {1,...,N}^4, regardless of the heights or denominators of a rational basis.
Similarly a nonzero coordinate is an injective projection of each one-dimensional U_j, giving at most N such vectors.

Taking the union yields rN^2+tN.
The map from normalized words to sorted b is injective, proving (SC4).
The result counts all integral lifts at the level of their binary supports, and therefore also bounds the subset of full P mod2 multiples.
It does not count arbitrary translates as distinct normalized words.

<a id="trace-code-and-additive-energy"></a>
## The reciprocal trace code and what linearity adds

Assume P is reciprocal.
The map alpha -> alpha^(-1) is a nontrivial order-two automorphism of K: alpha^(-1) is another root of the irreducible P, lies in K, and is distinct from alpha because alpha is nontorsion.
It fixes beta=alpha+alpha^(-1).
Since alpha satisfies x^2-beta*x+1=0, one has [K:Q(beta)]=2, proving [F:Q]=d/2.

Each t_a=alpha^a+alpha^(-a) is an algebraic integer in F.
For example t_0=2, t_1=beta and t_(a+1)=beta*t_a-t_(a-1) give membership directly.
There is a natural injection

    O_F/2O_F -> O_K/2O_K.

Indeed, if u in O_F belongs to2O_K, then u/2 belongs to K and is integral; it also lies in F, so u/2 belongs to O_F.
Thus integrality inferred from a trace-code relation uses the same full original ring, without a hidden index loss at2.

A weight-s word of C_N consists of distinct indices a_1<...<a_s for which sum_j t_(a_j) belongs to2O_F.
Write K_a=a_s.
For every sign choice, the polynomial

    A_epsilon(x)=x^(K_a)sum_(j=1..s)
                         epsilon_j(x^(a_j)-x^(-a_j))

has integral A_epsilon(alpha)/2 in O_K.
This follows because its Laurent numerator is congruent modulo2 to sum_j(x^(a_j)+x^(-a_j)), and multiplication by the unit alpha^(K_a) preserves integrality.
Its actual span is 2K_a<=2N<=Cd, and its reduction has exactly s reflected pairs.

If 1<=s<=3, C862 contradicts (SC2), so the code has no such nonzero word.
For s=4, the preceding confinement applies to b=2(a_1,a_2,a_3,a_4).
The planes and lines are linear through zero, so a itself belongs to the same W_i or U_j.
The coordinate-projection count now bounds the number of increasing index quadruples by rN^2+tN, proving (SC5).

The absence of weight-one and weight-two words says that the tau_a are nonzero and pairwise distinct.
If an element of A_N were a sum of two elements of A_N, equal summands would give zero, a repetition with the target would force another zero element, and three distinct indices would give a weight-three word.
All cases are excluded.
Thus A_N intersect (A_N+A_N) is empty.

For the energy identity, a quadruple with sum zero in characteristic two either has every index with even multiplicity or has four distinct indices forming a weight-four word.
A pattern with multiplicities3+1 or2+1+1 would force equality of two distinct tau values and is impossible.
The all-equal quadruples contribute N.
Two distinct doubled indices contribute6 binom(N,2)=3N(N-1).
Each distinct four-element codeword contributes all24 orderings.
This proves the exact formula (SC6); its displayed upper bounds follow from (SC5) and N>=1.

Let r(y) count ordered pairs from A_N summing to y.
Then sum_y r(y)=N^2 and sum_y r(y)^2=E_N.
Cauchy--Schwarz gives N^4<=|A_N+A_N|E_N, proving the first part of (SC7).
The disjoint sets A_N and A_N+A_N lie in O_F/2O_F, which has2^[F:Q]=2^(d/2) elements.
This proves the second part of (SC7), with the original degree retained.

Linearity does not force a weight-four word to exist.
The possibility B_4(N)=0 is consistent with every displayed bound, and no minimum distance of at least five is asserted.
The degree inequality remains compatible with arbitrarily large d and N proportional to d; it is not by itself a positive Mahler gap.

<a id="binary-seed-return"></a>
## Return to an actual energy-four binary phase seed

In the setting of E, every nonzero seed coefficient is +/-1.
Indeed a coefficient of absolute value2 already consumes the entire energy budget4; the nonzero constant term would then force H to be one of the excluded constants +/-2.
Thus H has at most four nonzero coefficients.

With T=n+k, reversal about T gives V*=sigma V.
Modulo2 this is reciprocal.
Its constant coefficient is sigma h_k and its leading coefficient is h_k, both odd because n>0 and h_k is +/-1.
A central coefficient, when present, is either0 or2h for an integer h, and hence vanishes modulo2.
There are at most eight supported residues and at least one reflected pair.
Consequently the full V mod2 is a normalized binary reciprocal word with 1<=s<=4, actual span T and integral canonical lift divided by2.

Part E now follows from Part A: under (SC2), s must be four and the associated frequency vector must lie in the fixed finite plane/line union.
No degree increase, new seed, new field or discarded original conjugate enters this application.

## Reuse and remaining original-input problem

[C50](Yin_C_G0050_v1.md#statement) retains its exact restricted dyadic packet capacity and denominator-growth obstruction.
Its minimum-weight-two/three classification is not being reproved here.
[C144](Yin_C_G0144_v1.md#zero-measure-all-prime-control) retains genuine torsion controls showing that short sparse supply cannot follow merely from zero measure and finite local-window conditions.
The present theorem assumes an actual nontorsion input with positive measure and does not relabel those controls as counterexamples to near-one supply.
[C231](Yin_C_G0231_v1.md#statement) supplies the separate all-power degree descent for the unrestricted infimum; the current arithmetic result already applies to every selected reciprocal power-stable endpoint without changing it.

The [C275 original-orbit energy interface](Yin_C_G0275_v1.md#faithful-high-moment-arithmetic-interface) and [C276](Yin_C_G0276_v1.md#statement) concern different original-power and high-moment counts.
The present fixed fourth-order energy is in the mod2 trace quotient, at a degree-linear window.
It supplies neither their linear-order moment hypotheses nor an entropy gap.
The displayed combinatorial energy calculation is elementary and makes no novelty claim or new external-source assertion.

For any hypothetical sequence of actual reciprocal power-stable units with m(P) tending to zero, each fixed C eventually meets (SC2).
Every supplied short binary phase then obeys the same fixed frequency confinement, and every corresponding trace code obeys (SC5)--(SC7).
This sharpens what such a sequence would have to satisfy.
It does not produce a sparse word, a seed, a shift, a bad host, an exception or any member of that hypothetical sequence.
Automatic auxiliary supply, the behavior inside the possible low-dimensional obstruction families and the unrestricted Lehmer contract remain unresolved.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T18:29 |
| status | proved |
| reason | Adopt Parts A--E and SC1--SC11 after independent R1082: the same original near-one input has fixed finite frequency-plane confinement, quadratic support counts and the stated dyadic trace-code energy consequences. The result supplies necessary conditions, not auxiliary existence or an unrestricted Mahler gap; inherited source and self-review limits remain explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact original-input statement](#statement) | All Parts A--E, actual original degree and field, strict fixed-C threshold, normalized supports, trace code and supplied-seed scope. |
| argument | [Complete arithmetic argument](#normalization-and-original-integrality) | Full normalization, sign/parity, original threshold, frequency confinement, support counting, trace-code energy and seed return through the stated limits. |
| dependency | [Adopted zero-removal input](Yin_C_G0141_v1.md#decision-isolated-whole-review-20261023-m04) | Only Section 1 at K=S=8 or 6, denominator2 and original C, including zero values and inherited C139/C92/source/self-review boundaries. |
| dependency | [Adopted low-pair theorem](Yin_C_G0862_v1.md#decision-whole-independent-review-2026-11-04) | Exact one-to-three reflected-pair original-window exclusion and its selected review scope. |
| dependency | [Adopted finite-host theorem](Yin_C_G0863_v2.md#decision-whole-independent-review-2026-11-04) | Part 9 at b_0=log2-11/24300, with its finite qualitative hosts, exceptional circles and inherited evidence limits. |
| review | [Independent whole arithmetic finding](../audits/reviews/Yin_R_G1082_v1.md#whole-arithmetic-consequence) | Every statement and complete argument, exact dependency interfaces, positive-integer exponent clarification and non-supply limits; no new native run or source-proof audit. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
