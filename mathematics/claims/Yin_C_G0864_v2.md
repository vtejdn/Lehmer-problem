---
author: Yin
---
# A uniform original-window gap for supplied binary four-pair auxiliaries

Human author Yin.
Root supplied the finite-exception-to-binary-period bridge and its explicit bounded-frequency version.
The sign_obstruction contributor checked the normalization and full-ring arithmetic, supplied the direct original-degree binomial norm return, and developed the complete argument below.
These are proof contributions, not an independent review.

## Revision scope and exact inputs

On 2026-11-04 this version strengthens the original-input binary auxiliary result: every supplied reflected binary residue with at most eight terms and a degree-linear window gives a uniform positive total-Mahler gap.
It removes the analytic four-pair phase requirement on that supplied class without asserting a good sign on every remaining circle.
The [adopted v1](Yin_C_G0864_v1.md#decision-whole-independent-review-2026-11-04) and its [R1082 review](../audits/reviews/Yin_R_G1082_v1.md#whole-arithmetic-consequence) retain all their conclusions at their original delta(C), host and counting scope.
No old assessment is transferred to the new argument.
The selected assessment of this version is recorded in its decision below.

The [adopted C863 v4 theorem](Yin_C_G0863_v4.md#decision-whole-independent-review-2026-11-04) supplies its exact Part4 bound on primitive circle frequencies, at the scope of [R1083 v2](../audits/reviews/Yin_R_G1083_v2.md#whole-v4-and-complete-fourier-envelope).
That upstream review does not inspect the new binary-period bridge in the present version.
This version's own independent review is selected separately in that decision.

| Input | Actual role |
| --- | --- |
| [C863 v4 circle reduction](Yin_C_G0863_v4.md#explicit-finite-circle-reduction) | A primitive positive four-tuple with maximum greater than128^3 has a sign of measure below33/50, hence below log2-127/4050; fixed upstream proof and native limits remain its own. |
| [C141 selected zero-removal input](Yin_C_G0141_v1.md#decision-isolated-whole-review-20261023-m04) | Only Section1, at support/length bounds8, denominator2 and the exact margin below, including an initially zero auxiliary value and original degree d. |
| [C862 selected theorem](Yin_C_G0862_v1.md#decision-whole-independent-review-2026-11-04) | Uniform original-window gap for one, two or three reflected pairs, with its inherited C139/C92/source limits. |
| [C864 v1](Yin_C_G0864_v1.md#decision-whole-independent-review-2026-11-04) | Unchanged old conclusions and the exact sign-lift, parity, full modular divisibility, monomial normalization and trace-code interfaces referenced below. |
| [C50 period mechanism](Yin_C_G0050_v1.md#statement) | Prior full characteristic-two period and original binomial-cost mechanism; the needed finite-ring and full O_K norm arguments are supplied directly below, without broadening its restricted packet domain. |

No new computation is used.
The enormous period bound below is symbolic; no exceptional-circle list or enormous integer is constructed.

## Statement

Keep all conclusions of C864 v1 at its original threshold and hypotheses.
For the new assertions put

    A_0=128^3=2097152,
    L_*=2^(2A_0)-1,
    eta_2=127/4050,
    eta_3=(1/8)log(128/105),
    K0=(log2/4)/(2*36^8*5^64).

For every C>0 set

    Gamma_3(C)=min{g(6,6,C,eta_3), K0*6^(-64)/C},
    Gamma_4(C)=min{g(8,8,C,eta_2), K0*8^(-64)/C},
    Gamma_b(C)=log2/(2L_* C),
    Gamma_bin(C)=min{Gamma_3(C),Gamma_4(C),Gamma_b(C)}>0. (BP1)

Here g is the same positive constant in [C139](Yin_C_G0139_v1.md#statement), used through C141, with the retained absolute source constant and original proof-inspection limits.
No numerical comparison with v1's delta(C) is asserted.

Let alpha be an actual nontorsion algebraic integer unit with monic irreducible minimal polynomial P, original field K=Q(alpha), original degree d and total logarithmic Mahler measure m(P)>0.
All quotient values are in the full ring of integers O_K.

A. Suppose an integer polynomial V has degree T>=1, T<=Cd, integral V(alpha)/2, allowing zero, and coefficientwise reduction

    V(x) mod2=sum_(j=1..s)(x^(T-e_j)+x^(e_j)),
    1<=s<=4, 0=e_1<...<e_s<T/2.                       (BP2)

   Then

    m(P)>Gamma_bin(C).                                 (BP3)

   All reflection pairs are disjoint and the two endpoint residues are nonzero.
   No phase separation, squarefree reduction, good-prime or power-degree-preservation assumption is imposed.

B. In particular, (BP3) holds for every supplied binary energy-four phase

    H in Z[x], H(0)!=0, deg H=k, sum h_j^2<=4,
    H different from the constants +/-2,
    n in Z_(>=1), sigma in {+1,-1},
    V=x^n H+sigma H*, H*(x)=x^k H(1/x),
    V(alpha)/2 integral, n+k<=Cd.                     (BP4)

   It also holds for every normalized binary reciprocal word with two, four, six or eight terms and span at most Cd whose full polynomial is divisible by P mod2.
   Repeated factors are retained.
   More generally only integral half-value of one coefficientwise lift is needed; divisibility by P mod2 is sufficient but not necessary.

C. Consequently, if 0<m(P)<=Gamma_bin(C), none of the auxiliaries in A or B exists.
   Suppose also that P is reciprocal, put F=Q(alpha+alpha^(-1)), and write O_F for its full ring of integers.
   For every integer N>=1 with 2N<=Cd, define the same trace residues and code as in v1:

    tau_a=(alpha^a+alpha^(-a)) mod2O_F, 1<=a<=N,
    Phi_N:F_2^N -> O_F/2O_F, e_a -> tau_a,
    C_N=ker Phi_N, A_N={tau_1,...,tau_N}.

   The code C_N has no nonzero word of weight at most four.
   Thus its minimum nonzero weight is at least five, with the zero code allowed.
   The N residues are distinct and nonzero, and every unordered sum of two distinct residues is different from every other such sum.
   Precisely,

    |A_N+A_N|=1+N(N-1)/2,
    A_N intersect (A_N+A_N) is empty,
    2^(d/2)>=1+N(N+1)/2,
    E_N=3N^2-2N,                                      (BP5)

   where E_N counts ordered quadruples with tau_a+tau_b=tau_c+tau_e.

Parts A and B do not require reciprocity of P; C uses it only for the trace field and degree d/2.
These assertions apply in particular to the reciprocal power-stable core of the unrestricted problem.
They still do not construct an auxiliary, prove the finite remaining pure circle sign inequalities or resolve unrestricted Lehmer.

<a id="inherited-original-normalization"></a>
## The inherited normalization on the original input

For (BP2), let R_tilde be the canonical integer polynomial with coefficient1 at each displayed supported exponent.
Then V-R_tilde has every coefficient even, so integral V(alpha)/2 implies integral R_tilde(alpha)/2.
Every antisymmetric sign lift

    A_epsilon(x)=sum_(j=1..s)epsilon_j
                         (x^(T-e_j)-x^(e_j))

is coefficientwise congruent to R_tilde modulo2.
It is nonzero, has true degree and span T and coefficient length2s, and A_epsilon(alpha)/2 is integral in the same O_K, even if its value is zero.

These are exactly the [same-input lift facts](Yin_C_G0864_v1.md#same-input-signs-and-parity) of v1.
The [full-divisibility argument](Yin_C_G0864_v1.md#normalization-and-original-integrality) also remains unchanged: monic division by P shows that a full P mod2 multiple has integral half-value in Z[alpha], and unit monomial shifts may be removed before measuring the true span.
No replacement of O_K by a smaller order is made in the new theorem.

For s<=3, the adopted C862 original-window result already gives m(P)>Gamma_3(C).
It remains to treat s=4.

For those four pairs set b=T-2e_j and sort increasingly.
Then all b_j are positive distinct integers with the parity of T and b_4=T.
The v1 parity substitution proves

    m(A_epsilon)=m_(H_b)(F_epsilon),
    H_b={ (z^(b_1),...,z^(b_4)):z in T }.              (BP6)

For odd T this uses pi-periodicity after replacing theta by2u, and for even T it gives the same identity.
It is an analytic substitution only; the original field, original degree and evaluated polynomials are unchanged.

<a id="large-primitive-frequency-branch"></a>
## Large primitive frequencies have a supplied logarithmic margin

Let k=gcd(b_1,b_2,b_3,b_4) and a=b/k.
Then a is a strictly increasing positive primitive integer tuple, and

    b=k a, T=k a_4, H_b=H_a.

The equality of circles holds because the k-th power map preserves circle Haar measure.
It changes no original arithmetic datum of alpha.

If a_4>A_0, C863 v4 Part4 supplies a sign with

    m(A_epsilon)=m_(H_a)(F_epsilon)
                 <33/50<log2-eta_2.                  (BP7)

C141's exact zero-removal assembly applies with support bound8, coefficient length8, denominator2, margin eta_2 and original window constant C.
It therefore gives m(P)>Gamma_4(C), including the possible zero value of the chosen A_epsilon(alpha).
No two-sided limit or small-value numerical estimate is used here.

<a id="finite-frequency-period-branch"></a>
## Bounded primitive frequencies yield an actual short binary period

Suppose instead that a_4<=A_0.
Define the actual integer polynomial

    B_a(x)=sum_(j=1..4)
                (x^(a_4+a_j)+x^(a_4-a_j)).            (BP8)

Its eight exponents are distinct, it has constant coefficient1, and it is monic of degree2a_4.
Let Bbar_a denote its full reduction over F_2, without removing repeated factors.

The finite quotient ring

    R_a=F_2[x]/(Bbar_a)

has exactly2^(2a_4) elements.
The class of x is a unit because Bbar_a(0)=1.
Its successive powers lie in the finite unit group, whose cardinality is at most2^(2a_4)-1.
Thus there is an integer L_a such that

    1<=L_a<=2^(2a_4)-1<=L_*,
    Bbar_a divides x^(L_a)-1 in F_2[x].               (BP9)

This is a statement in the quotient by the full polynomial and automatically retains every nilpotent multiplicity.
It requires neither factorization nor a squarefree or field quotient.
It is the same finite-period mechanism retained in C50, applied here to a fixed bounded-degree binary polynomial.
L_* is only a size bound; it is not asserted to be a common period or a multiple of every L_a.

The actual integer identity connecting the original word to (BP8) is

    R_tilde(x^2)=B_a(x^k).                             (BP10)

Indeed T=k a_4 and b_j=k a_j give the original exponents (T+/-b_j)/2, and replacing x by x^2 gives exactly the exponents in B_a(x^k).
This covers both parity cases; it does not assume that a itself has a common parity.

Coefficientwise Frobenius congruence over F_2 gives an integer polynomial Q_R with

    R_tilde(x^2)=R_tilde(x)^2+2Q_R(x).

If u=R_tilde(alpha)/2 is integral, then

    B_a(alpha^k)/2=R_tilde(alpha^2)/2
                 =2u^2+Q_R(alpha) in O_K.             (BP11)

The same K and original degree d are retained.
The argument does not use the minimal polynomial or degree of alpha^2 or alpha^k.
It is valid also when u or B_a(alpha^k) is zero.

Lift the quotient in (BP9) to an integer polynomial Q_a.
There is an integer polynomial W_a such that

    x^(L_a)-1=B_a(x)Q_a(x)+2W_a(x).

Evaluating at alpha^k and using (BP11) proves

    (alpha^(kL_a)-1)/2 in O_K.
    n_0=kL_a<=kL_*<=L_*T<=L_*C*d.                    (BP12)

All changes are genuine polynomial identities or coefficientwise congruences evaluated on the original unit.
No primitive part, selected residue factor or changed number field replaces the original input.

<a id="original-binomial-norm-return"></a>
## The full original binomial norm pays the complete period

Here is the needed form of the old dyadic-binomial original-root expense, supplied directly to include full O_K integrality.
Let alpha be any actual nontorsion algebraic integer unit of original degree d, and suppose

    v=(alpha^n-1)/2 in O_K, n in Z_(>=1).

Both v and v+1 are nonzero: a zero would give alpha^n=1 or -1, contradicting nontorsion.
Consequently

    (alpha^(2n)-1)/4=v(v+1) in O_K\{0},
    |Norm_(K/Q)(alpha^(2n)-1)|>=4^d.                  (BP13)

On the other hand every original conjugate alpha_j satisfies

    |alpha_j^(2n)-1|<=1+|alpha_j|^(2n)
                       <=2max{1,|alpha_j|^(2n)}.

At least one original conjugate has modulus different from1 because m(P)>0, so the second comparison is strict for that factor.
Every factor is nonzero, and multiplication over all d original embeddings gives

    |Norm_(K/Q)(alpha^(2n)-1)|
       <2^d exp(2n m(P)).

Combining with (BP13) yields

    m(P)>d log2/(2n).                                 (BP14)

This is the familiar period price underlying C50's width-h dyadic packet.
The displayed proof keeps the full original norm and remains valid even when powers of alpha lose degree or Z[alpha] is not maximal.

Applying (BP14) to n=n_0 from (BP12) gives

    m(P)>d log2/(2n_0)>=log2/(2L_* C)=Gamma_b(C).       (BP15)

Thus every possible bounded primitive frequency tuple, including any unresolved pure circle sign case, is covered arithmetically on a supplied original input.

<a id="uniform-supplied-phase-gap"></a>
## Completing the supplied-class gap

For s<=3 the measure exceeds Gamma_3(C).
For s=4 and a_4>A_0 it exceeds Gamma_4(C).
For s=4 and a_4<=A_0 it exceeds Gamma_b(C).
These exhaust every actual support in (BP2), so all branches give the strict inequality (BP3).

For (BP4), the [unconditional seed/reflection calculation](Yin_C_G0864_v1.md#binary-seed-return) shows that every nonzero seed coefficient is +/-1, that V has actual span n+k with odd endpoint coefficients, and that its reduction has between one and four disjoint reflected pairs.
The central coefficient is even.
Its canonical residue lift has the same integral half-value property, so A applies and proves B.
The full P mod2-divisor consequence uses the inherited monic-division argument with all multiplicities.

This argument does not establish a uniformly good sign for every four-frequency circle.
It instead uses an actual integral auxiliary to turn each remaining bounded primitive support into an actual binomial integral value with a completely bounded original-degree cost.
No exceptional tuple is enumerated or tested, and no pure circle inequality is inferred for those tuples.

<a id="trace-code-weight-five"></a>
## Near-one trace codes have no words of weight at most four

Assume 0<m(P)<=Gamma_bin(C), P reciprocal and 2N<=Cd.
The [trace-field argument](Yin_C_G0864_v1.md#trace-code-and-additive-energy) gives [F:Q]=d/2 and the injection O_F/2O_F -> O_K/2O_K.
Each tau_a is a well-defined residue of an actual integral trace in F.

If C_N had a nonzero word on distinct indices a_1<...<a_s with 1<=s<=4, then sum_j(alpha^(a_j)+alpha^(-a_j)) would belong to2O_F.
As in the same v1 interface, every sign lift

    x^(a_s)sum_j epsilon_j(x^(a_j)-x^(-a_j))

would have integral half-value in O_K.
Its reduction has exactly s reflected pairs and its true span is2a_s<=2N<=Cd.
Part A would force m(P)>Gamma_bin(C), a contradiction.
Thus no such codeword exists.

Weights one and two exclude zero and repeated residues.
Weight three excludes A_N intersect (A_N+A_N), including the cases of repeated summands.
If two unordered pairs of distinct indices had the same sum, a shared index would force equality of the other two residues, and disjoint pairs would give a weight-four word.
Both are excluded.
All binom(N,2) distinct-index sums are nonzero and pairwise different, while every diagonal sum is0.
This proves

    |A_N+A_N|=1+binom(N,2).

Adding the disjoint N-element set A_N gives the cardinality lower bound in (BP5), since |O_F/2O_F|=2^(d/2).
Finally, every zero-sum ordered quadruple has all indices with even multiplicity; there are N all-equal quadruples and6binom(N,2) doubled-pair quadruples.
Thus E_N=3N^2-2N, completing C.

## Contribution and remaining supply boundary

The new arithmetic bridge combines the fixed bounded primitive-frequency remainder with a full binary quotient-ring period and a norm estimate on the same original unit.
The binomial-period mechanism itself is already present in the older arithmetic work; the new use closes all supplied four-pair residue cases without completing the finite pure-circle sign question.
Every power, norm, residue multiplicity and original window cost is retained.

No new auxiliary-existence theorem follows.
The new trace code is allowed to have no weight-four word and indeed must have none below the threshold.
The exact sumset bound remains compatible with a degree-linear N because2^(d/2) grows much faster than N^2.
The surviving original problem is to supply some actual short integral auxiliary or a different paid mechanism for every sufficiently near-one input.
Neither the old necessary confinement theorem nor this supplied-class gap resolves unrestricted G0001.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T19:00 |
| status | proved |
| reason | Adopt the complete supplied binary auxiliary gap and exact near-one trace-code consequences after independent R1082 v2. The large-primitive-frequency branch uses adopted C863 v4, while every bounded primitive pattern is returned through a full binary period and the same original degree-d norm. No candidate-circle enumeration or automatic auxiliary supply is asserted; unrestricted G0001 remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact supplied-class statement](#statement) | All new A--C and BP1--BP5, original unit/field/degree, positive uniform fixed-C threshold, actual seed and full residue domains, code weights and exact Sidon counts; unchanged v1 scope retained. |
| argument | [Complete arithmetic assembly](#inherited-original-normalization) | BP6--BP15 and full branch, seed, trace-code and remaining-supply arguments, including parity, full quotient-ring periods and original norms. |
| dependency | [Adopted circle reduction](Yin_C_G0863_v4.md#decision-whole-independent-review-2026-11-04) | Part4's primitive frequency cutoff and favorable-sign margin with its exact accepted Fourier/native and independent-review limits. |
| dependency | [Adopted zero-removal input](Yin_C_G0141_v1.md#decision-isolated-whole-review-20261023-m04) | Only Section1 at K=S=8, q=2 and eta=127/4050, allowing zero auxiliary values and preserving inherited C139/C92/source/self-review boundaries. |
| dependency | [Adopted low-pair theorem](Yin_C_G0862_v1.md#decision-whole-independent-review-2026-11-04) | Original-window Gamma_3(C) for one to three reflected pairs at its exact accepted scope. |
| dependency | [Adopted v1 theorem and interfaces](Yin_C_G0864_v1.md#decision-whole-independent-review-2026-11-04) | Unchanged old conclusions and the unconditional normalization, sign/parity, full divisibility, seed and trace-field interfaces; no numerical threshold comparison is assumed. |
| review | [Independent whole supplied-class finding](../audits/reviews/Yin_R_G1082_v2.md#whole-v2-supplied-class-gap) | Complete new statement and proof plus exact retained interfaces, actual upstream acceptance and all non-supply limits; no new native computation or original-source proof audit. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
