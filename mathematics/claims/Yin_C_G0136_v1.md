---
author: Yin
---
# Genuine Salem inputs with contrasting small-prime return mechanisms

Date: 2026-10-15T09:56.
Author f_unitary_scope for Yin under root's continuing actual arithmetic inquiry.
Root supplied the question, not the construction or estimates developed here.
No native mathematical program or J is used.
C135 v1 is fixed but awaiting whole independent review at this starting point; its later adoption must not be presumed.

## Responsible question and exact reuse

Seek a structural actual-polynomial test beyond the C135 binary-binomial candidate, not a substitution of another fixed binomial count.
The proposed discriminator is a genuine Salem family whose chosen good-prime Frobenius is a nontrivial rational involution, with poor short-return coverage at that prime but an exact inexpensive certificate at a DIFFERENT small prime on the SAME original polynomial.
This would distinguish reciprocity/Salem root geometry from a useful prime-selection mechanism.
It will remain a fixed-positive-measure control, not a near-one counterexample.

The exact screen found [C71's full tailored dyadic gate](Yin_C_G0071_v1.md#tailored-dyadic-full-gate), including all multiplicities and its separate nonvanishing results.
This is a closer antecedent to C135's two-factor special case than its initial screen had recorded; root was informed and is handling fixed-version attribution.
That gate and its old implicit gap are not new results here.
[C243](Yin_C_G0243_v1.md#reciprocal-trace-domain) gives the exact reciprocal trace normalization and original doubled field costs.
[C242](Yin_C_G0242_v1.md#collision-layers-and-frobenius-defect) warns that a first-layer count is not a full valuation upper bound.
[C130v2](Yin_C_G0130_v2.md#statement) is the earlier nonreciprocal translation-Frobenius control; its family and binary exact depths will not be claimed for the present Salem inputs.

The actual Salem family screen read C22's complete circle-root count, its cyclotomic exclusion and the C41/C122 same-family scope.
Those existing inputs use the MINUS Salem-Boyd sequence for t-2 and do not give the present finite-field involution calculation.
The construction form is classical: [Hir06's already inspected Section3.1 equation4](../audits/literature/Hir06/readme.md#reciprocal-sequence-method-attribution) defines t^N f(t)+/-f*(t); the present t-3 PLUS sequence is an ordinary instance.
This source is attribution only.
Its root/convergence theorems are not imported; the proposed root count and irreducibility will be proved directly.
Local searches for rational involutions, q^2-1 root support and the exact four-term family found no matching retained control in the inspected passages, without establishing novelty.

<a id="statement"></a>
## Statement: a genuine Salem all-depth failure at5 and a paid certificate at3

For EVERY integer r>=1, put q=5^r and d=q+1.
The original polynomial P_q=t^d-3t^(d-1)-3t+1 is monic irreducible Salem of EXACT degree d, with coefficient height3, l1 norm8, and3<M(P_q)<4 tending to3.
No cyclotomic factor is deleted.
The rational prime5 is good, all d reduced roots lie in F_(q^2)^*, and their full return count satisfies h_q(n)<=2sqrt n for every positive integer n.

Writing C_n=|Norm_(Q(alpha)/Q)(alpha^n-1)| for a root alpha of P_q and L=2*5^10, EVERY valuation layer obeys

    v_5(C_n)<=2sqrt n+10(L-1), n>=1.

Thus for every fixed C>0, on every nonempty original window1<=n<=floor(Cd), the maximum of(log5)v_5(C_n)/d tends to0 as r tends to infinity.
This is a statement about the FULL original norm at the selected prime, not only the first layer.

For any selection of complete actual reduced order groups with original mass W>=gamma d, gamma>0, and any real1<=X<=Cd, its original ordered triple density and capture obey

    delta_X<=8 C^(5/2)/(gamma^3 sqrt d),
    H_X/W<=2sqrt(C)/(gamma sqrt d).

These bounds apply to EVERY such selection and every allowed original X.
In particular no complete linear-mass selection at prime5 retains fixed positive triple density or capture at linear time.
If a larger original window X<=BCd is specified, the same capture estimate uses BC in place of C; no cost is dropped.

The SAME inputs have an exact prime3 certificate, using all original roots and potentially unbounded modular multiplicities:

    alpha^d+1 in3Z[alpha], alpha^(3d)+1 in9Z[alpha],
    |Norm_(Q(alpha)/Q)(alpha^(3d)+1)|>=9^d,
    m(P_q)>=log(9/2)/3.

The auxiliary t^(3d)+1 has actual degree3d, l1 norm2 and squared coefficient norm2.
This positive bound is the already known scalar norm mechanism, not a new class-gap claim.
The comparison establishes an actual reason to retain bad-prime/full-order arithmetic and prime selection alongside good-prime root counting.
It does NOT assert failure at every prime, at every auxiliary, or in the near-one regime: these actual measures tend tolog3.
Neither unrestricted near-one coverage nor the Mahler gap is resolved.

The comparison also holds within the SAME cyclic-norm family C_n: v_3(C_(2d))>=d and v_3(C_(6d))>=2d.
Thus switching to3 supplies a positive normalized original cyclic income already at n=2d; the plus-binomial auxiliary only improves the displayed elementary Mahler certificate.

<a id="argument"></a>
<a id="salem-involution-actual-family"></a>
## 1. Complete actual family, original degree and measure

For every integer r>=1 put q=5^r, d=q+1=2h and retain the displayed P_q.
Define C_0=2,C_1=x,C_(j+1)=x C_j-C_(j-1), so C_j(t+t^-1)=t^j+t^-j by induction.
The formal reciprocal trace identity is therefore

    P_q(t)=t^h T_q(t+t^-1), T_q=C_h-3C_(h-1).

It is valid over Z before irreducibility is established; no trace-field degree assertion is assumed at this step.
For j0,...,h-1, set theta_j=j*pi/(h-1).
The identity h*theta_j=j*pi+theta_j gives

    T_q(2cos theta_j)=2(-1)^j(cos theta_j-3).           (1)

Every factor in parentheses is negative.
The h-1 disjoint open intervals between these descending nodes therefore contain h-1 distinct real zeros, all in(-2,2).
Since T_q(2)=-4 and T_q is monic of degree h, it also has a root greater than2.
These h roots exhaust its degree, so all are simple and there are no further trace roots.
Passing to the exact quadratic t^2-x t+1 gives d-2 simple nonreal unit-circle roots and one simple positive inverse pair lambda_q,lambda_q^-1, with lambda_q>1.

There is NO root of unity.
If zeta were one, then

    3(zeta^q+zeta)=zeta^(q+1)+1.

Every complex Galois conjugate of the algebraic integer zeta^q+zeta has modulus at most2/3.
If it were nonzero, its nonzero integer norm would have modulus strictly below1, impossible.
Thus zeta^q=-zeta.
Substitution in the original equation gives zeta^2=1, but q is odd so zeta^(q-1)=1, contradicting zeta^(q-1)=-1.
This exclusion needs no Mann theorem or list of possible cyclotomic orders.

Factor P_q into monic integer irreducibles.
Each has constant coefficient+/-1 because P_q does.
A factor containing lambda_q must also contain lambda_q^-1: otherwise the modulus of its constant coefficient would be lambda_q, since all its remaining roots have modulus1.
All other factors would have every root on the circle and hence be cyclotomic by the existing Kronecker characterization in Smy08-U001.
They have just been excluded.
Thus P_q is itself the ACTUAL irreducible Salem minimal polynomial of ORIGINAL degree d=q+1, and M(P_q)=lambda_q.

P_q(3)=-8 while P_q(4)=4^q-11>0.
Hence

    3<lambda_q<4,
    lambda_q-3=(3lambda_q-1)/lambda_q^q
                     <11/3^q ->0.                    (2)

Its total logarithmic measure tends to log3, not0.
Coefficient height is3 and coefficient l1 norm8 at every degree.
No sparse-input or Salem existence theorem is claimed new; the complete local proof removes any eventual threshold or hidden cyclotomic factor degree from the present arithmetic control.

<a id="salem-involution-return-count"></a>
## 2. A good-prime involution and all short return counts

Modulo5, differentiation gives P_q'(x)=x^q-3.
If both P_q(x) and this derivative vanished, substitution would give1-9=-8=0 in F5, a contradiction.
Thus5 is good for the full original degree-d polynomial.
The constant coefficient excludes zero roots, and x3 is not a root.
The exact reduction relation is

    x^q=R(x), R(x)=(3x-1)/(x-3), R(R(x))=x.          (3)

The rational involution identity follows by multiplying its matrix [[3,-1],[1,-3]], whose square is8I.
Its coefficients lie in F5, so q-th powering commutes with R wherever defined.
At a reduced root, R(x)=3 would force3x-1=3x-9, again impossible.
Consequently x^(q^2)=x, and ALL d distinct reduced roots lie in F_(q^2)^*.

Let h_q(n) count those d roots with x^n=1, for ANY positive integer n.
Put m_n=gcd(n,q^2-1), and let H be the unique subgroup of F_(q^2)^* of order m_n.
Set

    A=gcd(m_n,q-1), B=gcd(m_n,q+1).

The map x to x^(q+1) has image of size m_n/B on H.
At a root satisfying(3), this map equals xR(x).
For a fixed image value y, its equation is

    3x^2-(1+y)x+3y=0,

which has at most2 roots because its leading coefficient3 is nonzero.
Similarly x to x^(q-1) has image size m_n/A and equals R(x)/x; at a fixed value w its equation is

    w x^2-3(w+1)x+1=0,

again at most2 roots, including every possible degeneracy since its constant coefficient is1.
Denominator roots were already excluded.
Therefore

    h_q(n)<=2 min(m_n/A,m_n/B)<=2sqrt(m_n)<=2sqrt n.  (4)

For completeness AB>=m_n.
At every odd prime, q-1 and q+1 are coprime, so their gcd exponents with m_n sum to the full exponent of m_n.
At2 their exponents have minimum1; if the exponent of m_n is e, the sum min(e,v2(q-1))+min(e,v2(q+1)) is at least e, since e<=v2(q-1)+v2(q+1).
Thus AB>=m_n, which proves the middle inequality in(4).
All finite subgroups and all original roots are retained, rather than only one Frobenius orbit or an abstract capacity inventory.

<a id="salem-involution-finite-depth-exceptions"></a>
## 3. A fixed defect polynomial bounds EVERY exceptional5-adic depth

The first-layer estimate(4) alone would not control the full cyclic norm.
Work in a finite unramified5-adic splitting extension, justified by the squarefree original reduction and the existing L64 simple-root lifting interface.
Normalize v(5)=1 and let sigma be its arithmetic Frobenius.
For an original root alpha, let o be its reduced multiplicative order, so5 does not divide o, and put a_alpha=v(alpha^o-1)>=1.
Nontorsion makes this finite.

If a_alpha>=2, then sigma(alpha) and alpha^5 have the same residue and both their o-th powers are1 modulo25.
The geometric quotient of their o-th powers is a unit, so

    sigma(alpha)=alpha^5 (mod25), P_q(alpha^5)=0 (mod25).

The EXACT characteristic-zero equation alpha^q=R(alpha) and the fact that alpha-3 is a local unit give

    P_q(alpha^5)=N(alpha)/(alpha-3)^5,
    N(X)=(X^5-3)(3X-1)^5-(3X^5-1)(X-3)^5.          (5)

Every coefficient of N is divisible by5 by coefficientwise Frobenius.
Set D(X)=N(X)/5 in Z[X].
Its degree is10 and leading coefficient is(3^5-3)/5=48, which is nonzero modulo5.
Hence the reduction Dbar is a NONZERO polynomial of degree10.
Formula(5) proves

    a_alpha>=2 => Dbar(alpha_bar)=0.                 (6)

Since the d original residues are distinct, at most10 original roots have exceptional depth greater than1, uniformly in q.

Their depths are also uniformly bounded; their mere number would not suffice.
If Dbar(x)=0, the residue x has finite-field degree f<=10.
Its order o divides5^f-1, so o<=5^10-1.
Let omega be its Teichmuller lift, the unique o-th root of unity with the same residue, in the unramified field.
The geometric quotient gives a_alpha=v(alpha-omega).
Taylor expansion of P_q at alpha has unit linear coefficient and higher terms of strictly larger valuation, so

    a_alpha=v(P_q(omega)).                           (7)

This evaluation is nonzero by Section1's complete torsion exclusion.
In the cyclotomic field Q(omega), every complex conjugate of P_q(omega) has modulus at most8.
Its full norm is therefore a nonzero integer of modulus at most8^phi(o).
The5-adic valuation at the specified embedding is nonnegative and at most the full rational norm valuation (all other prime-ideal contributions are nonnegative).
Consequently

    a_alpha<=phi(o) log_5(8)<2phi(o)<L,
    L:=2*5^10.                                      (8)

This is a deliberately conservative absolute constant.
It is independent of r, original d and return time n.
The estimate keeps every cyclotomic conjugate and every5-adic norm weight; it is not an assertion that the residue degree alone bounds an arbitrary lift's depth.
It uses the actual four-term P_q at its bounded-height torsion evaluation.
The ordinary depth-one roots and all at most10 exceptions are now both controlled.

For n=5^v t with5 not dividing t, only roots whose residue order divides t contribute.
For such a root the elementary odd-prime lifting identity is

    v(alpha^n-1)=a_alpha+v.                           (9)

Raising first to t/o prime to5 preserves depth by a geometric unit.
When a unit u satisfies v(u-1)>=1, expansion of u^5-1 gives unique minimum v(u-1)+1: the remaining terms have strictly larger valuation at p5.
Induction proves(9), with no uncharged exceptional cancellation.

Let C_n=|Norm_(Q(alpha)/Q)(alpha^n-1)|, retaining the ORIGINAL full field and signed norm before absolute value.
Summing all d normalized root valuations, using h_q(n)=h_q(t), gives

    v_5(C_n)<=(v+1)h_q(t)+10(L-1)
             <=2sqrt n+10(L-1).                     (10)

Indeed(v+1)5^(-v/2)<=1 for every integer v>=0: it is1 at0 and the ratio of successive terms is at most2/sqrt5<1.
Thus(4) controls the depth-one part after paying all n's5-power multiplicity, and(8) controls the bounded set of extra depths.
Formula(10) is an ALL-depth upper bound, not only a distinct-residue estimate.

<a id="salem-involution-original-window-costs"></a>
## 4. Every original group selection and every fixed linear window

At the actual good prime5 let w_o count any selected complete original root groups of multiplicative order o, with W=sum_o w_o>0.
One may select complete order groups or complete Frobenius orbits and then combine equal orders; either convention yields

    h_A(n)=sum_(o|n)w_o<=h_q(n).

No possible selection is promoted from an arbitrary phi-capacity inventory.
These are actual original roots; all counts and original mass remain in the same law.
For a real X>=1 set H_X=max_(1<=n<=floor X)h_A(n), and let T_X be the ordered triple sum with lcm(o_1,o_2,o_3)<=X, retaining every repeated label.
Every compatible triple occurs at least once in sum_(n<=X)h_A(n)^3, at its least common multiple.
Thus(4) gives

    T_X<=sum_(1<=n<=floor X)h_A(n)^3<=8X^(5/2),
    H_X<=2sqrt X.                                    (11)

Define delta_X=T_X/W^3.
If W>=gamma d and1<=X<=Cd, division by the ORIGINAL mass gives

    delta_X<=8C^(5/2)/(gamma^3 sqrt d),
    H_X/W<=2sqrt C/(gamma sqrt d).                    (12)

These are uniform in every such choice of groups and X.
They cover all complete linear-mass selections, not only the full inventory W=d.
The empty selected law is excluded by W>0, while the time window is explicitly nonempty.
Enlarging X costs the stated constant; there is no residual-degree or conditional-mass renormalization.

The stronger full-depth bound(10), applied directly to the full original cyclic norm, gives for every fixed C>0 with floor(Cd)>=1

    max_(1<=n<=floor(Cd)) (log5)v_5(C_n)/d
       <=(log5)[2sqrt(Cd)+10(L-1)]/d ->0.             (13)

It includes all original roots, all exceptional local depths and every5-power in n.
The finite threshold may be very large because L is deliberately crude; only the stated explicit bound and its limit are claimed.
Other rational prime valuations and the total log C_n have no upper bound asserted here.
In particular(13) must not be converted into an all-prime or all-auxiliary income obstruction.

<a id="salem-involution-same-input-prime-switch"></a>
## 5. The same input is captured at3, even with unbounded modular multiplicity

The exact original equation gives

    alpha^d+1=3(alpha^q+alpha) in3O0,
    O0=Z[alpha].                                     (14)

Put beta=-alpha^d, so beta=1 modulo3O0.
Writing beta=1+3u with u in O0 and expanding its cube shows beta^3-1 in9O0.
Since beta^3-1=-(alpha^(3d)+1),

    alpha^(3d)+1 in9O0.                              (15)

Every displayed value is nonzero by nontorsion.
Multiplication on the original rank-d integral order gives a nonzero signed field norm divisible by9^d.
At each complex original conjugate the elementary binomial bound gives

    9^d<=|Norm_(Q(alpha)/Q)(alpha^(3d)+1)|
         <=2^d M(P_q)^(3d).

Taking logarithms proves

    m(P_q)>=log(9/2)/3.                              (16)

The auxiliary is ONE actual polynomial t^(3d)+1 of original degree3d, content1, l1 norm2 and squared coefficient norm2.
No sum over unrelated times is called a single norm; no powered subfield is substituted.
Even the unamplified(14) already yields m>=log(3/2).
These are standard applications of the old L67 scalar/divisibility mechanism, with the sign paid in beta and absolute original norms; neither numerical constant is claimed new.
The direct root estimate lambda_q>3 in Section1 is stronger for this known family, so(16) is an explicit arithmetic comparison, not an improved family gap.

Nor does the prime comparison require changing from cyclic norms to plus auxiliaries.
Multiplication by the other integral binomial gives

    alpha^(2d)-1 in3O0, alpha^(6d)-1 in9O0,
    v_3(C_(2d))>=d, v_3(C_(6d))>=2d.                 (17)

All these values are nonzero.
Their ORIGINAL exponents are2d and6d and their binomial coefficient norm squared is2.
Thus(13)'s all-depth failure at5 and(17)'s positive linear-time income at3 concern exactly the same full C_n family.
The stronger plus auxiliary in(16) is an additional, explicitly paid option.

Good reduction at3 is NOT needed and fails at unbounded multiplicities.
If r is odd, d=5^r+1 is divisible by3.
More precisely take r=3^s, s>=0.
The elementary odd-prime binomial argument gives v_3(5^(3^s)+1)=s+1: apply it to(-5)^(3^s)-1, starting from v_3(-5-1)=1; cubing raises each positive depth exactly by1 because its linear term has the unique least valuation.
In characteristic3,

    P_qbar(t)=t^d+1=(t^(d/3^(s+1))+1)^(3^(s+1)),

and the inner polynomial is squarefree since3 does not divide d/3^(s+1).
Thus this subsequence has modular multiplicity3^(s+1) tending to infinity, all retained by(14)--(16).
No claim about field ramification is inferred merely from repeated reduction of a monogenic polynomial.

At2, P_qbar=(t+1)(t^q+1) has the old two-factor C71 gate at exponents1,q and width d.
Since q is odd, the factor t+1 has multiplicity2 in P_qbar.
Reciprocal nontorsion supplies C71's nonzero-output guard.
This additional comparison is already known; it is not needed for the prime3 certificate or the all-depth prime5 bound.
C135's later adopted aggregate constant likewise is not a premise here.

## 6. What changes in the strategy and what does not

This control puts the failure and success on the SAME original irreducible Salem polynomial, with bounded coefficient height and exact unbounded degree.
Prime5 is always good and every one of its original cyclic-norm layers has sublinear income on linear time; its failure cannot be repaired on this family simply by invoking unspecified exceptional depths.
Prime3 supplies order-level divisibility at a linear auxiliary degree, including a subsequence with unbounded modular multiplicities.
Consequently a strategy that only certifies good-prime return inventories can lose a real cheap arithmetic certificate, even on a genuine Salem input.
This is an exact reason to retain prime switching and full possibly nonreduced order information.

It does not say that selecting prime3 works on arbitrary small-measure inputs.
These known examples have M approaching3, and their coefficient shape already gives the scalar congruence.
Their construction or class gap is not new; what was not supplied by the inspected earlier inputs is the rational-involution return analysis together with the fixed-defect/Teichmuller argument controlling ALL selected-prime valuation layers, and the precise same-input comparison.
The proposed leap toward automatic near-one coverage has therefore produced a discriminating control, not the desired general coverage theorem.
Near-one arithmetic must supply extra information beyond reciprocity, Salem root geometry, bounded coefficient height and an arbitrary chosen good prime.
No assertion is made that these features are jointly sufficient after some unspecified further prime choice.

The direct family proof uses only L66's elementary symmetric trace recurrence/normalization, reproduced before invoking any field facts, and the existing Kronecker characterization in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001).
[L159's actual finite-field root convention](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) supplies the standard cyclic finite-group and complete root-count interface, without substituting its abstract capacities for realized roots.
The complete local argument uses [C241's actual simple-root/unramified Frobenius interface](Yin_C_G0241_v1.md#direct-etale-frobenius-lift).
The Teichmuller root used here requires only the same simple-root lifting for X^o-1, with5 not dividing o: uniqueness and sigma action follow from that lift.
[C256](Yin_C_G0256_v1.md#content-versus-ideal-norm) fixes the full original norm convention.
The explicit scalar certificate uses [C244](Yin_C_G0244_v1.md#cyclic-prime-power-norm-floor); its needed cube and complex bounds were reproduced in full.
Hir06 is classical sequence-form attribution only, at its already inspected passage, not a new root-theorem premise.
C22/C41/C122, L65's depth warning, C71 and C130 are exact comparisons rather than substitutes for the new all-depth argument.
C135 was initially a fixed candidate; its actual v2 selected whole-reviewed decision and [R798 original binary-annihilator-v2](../audits/reviews/Yin_R_G0798_v1.md#binary-annihilator-v2-whole-independent-finding) were subsequently read and confirmed.
No C135 theorem is needed in(1)--(17).

All new calculations in this original are by f_unitary_scope.
Root assigned the research question and required honest original costs, but supplied no family, finite-field, defect or depth proof step.
No native mathematical computation, new J, source download or source proof upgrade is involved.
Full independent review remains separate from author checking and any future fixed adoption.

<a id="salem-involution-entire-author-freeze"></a>
## Entire author freeze

2026-10-15T10:09.
The f_unitary_scope author freezes this entire actual original: responsible question and exact reuse/attribution, full statement, Sections1--6 and equations(1)--(17), all complete family/field/norm/window costs, same-input prime comparison, modular multiplicities and near-one limitations.
The final contributing self-check reconstructed the formal trace identity before irreducibility, all h trace roots and d original roots, torsion exclusion and irreducibility without deleting a cyclotomic factor, exact original degree and fixed-positive-measure limit, squarefree5 reduction, both rational-fiber equations and the shared2-adic gcd factor, and every complete original selection and nonempty floor window.

The all-depth check reconstructed the sigma-versus-fifth-power congruence from an actual second-order return, the exact polynomial N and its nonzero degree10 reduction after division by5, at most10 distinct exceptional roots, finite residue degree versus actual lift depth, the unique root-of-unity lift and unit derivative equality, the full cyclotomic integer norm and coefficient8 price, every original5-adic embedding and odd-prime lifting layer.
The prime3 check retained its original monogenic order, signed nonzero full norms, plus-auxiliary degree3d, SAME cyclic exponents2d/6d and the unbounded reduction multiplicities at r=3^s.
No remaining gap was found by author checking; no independent review or Claim adoption is asserted.
The structural material check returned checked1 before this paragraph and is not a proof verdict.


## Fixed organization

Retain the entire frozen author account, all statements, numbered and unnumbered arguments, actual input costs, exceptional branches, source and contribution limits and author check.
Root supplied direction and reuse constraints but no new proof step.
This restricted result does not resolve G0001.

## Current assessment
[Selected decision](#decision-isolated-current-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T10:21 |
| status | open |
| reason | Complete frozen author argument retained for actual independent whole review; unrestricted coverage remains open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Complete final statement and every declared consequence and domain. |
| argument | [Entire proof](#argument) | Every numbered and unnumbered argument, all costs, branches, interfaces and provenance. |
| dependency | [Exact input](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Formal trace recurrence, reproduced before field use. |
| dependency | [Exact input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted Kronecker characterization. |
| dependency | [Exact input](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete actual finite-field roots and order groups. |
| dependency | [Exact input](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Simple-root unramified lifting and Frobenius. |
| dependency | [Exact input](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Full original norm and valuations. |
| dependency | [Exact input](../ledger/Yin_L_G0067_v1.md#cyclic-prime-power-norm-floor) | Integral-order prime-power certificate; local costs rederived. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T10:41 |
| status | proved |
| reason | Adopt actual [R798 original Salem-involution](../audits/reviews/Yin_R_G0798_v1.md#salem-involution-whole-independent-finding) whole noncontributor review: genuine original-degree Salem inputs exhibit all-depth failure at specified good prime5 and positive original cyclic income at3. Measures tend to log3; automatic near-one coverage and G0001 remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Complete final statement and every declared consequence and domain. |
| argument | [Entire proof](#argument) | Every numbered and unnumbered argument, all costs, branches, interfaces and provenance. |
| dependency | [Exact input](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Formal trace recurrence, reproduced before field use. |
| dependency | [Exact input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted Kronecker characterization. |
| dependency | [Exact input](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete actual finite-field roots and order groups. |
| dependency | [Exact input](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Simple-root unramified lifting and Frobenius. |
| dependency | [Exact input](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Full original norm and valuations. |
| dependency | [Exact input](../ledger/Yin_L_G0067_v1.md#cyclic-prime-power-norm-floor) | Integral-order prime-power certificate; local costs rederived. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0798_v1.md#salem-involution-whole-independent-finding) | Entire17-equation account, complete actual input interfaces, every original depth/window and same-input prime comparison. |


### Decision current-local-trace-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:51 |
| status | proved |
| reason | Select C241/C243 as the complete current responsible homes for the identical already used L64 unramified local or L66 reciprocal trace/order/module interfaces at the exact selected anchors below. The full original arguments, current extracted statements and used guards were read; this is same-content locator adoption. Status, selected statement/argument/finding, all relation scopes and every other current proof home remain unchanged. Prior dated decisions and R bindings keep their actual L64/L66 inputs; no new independent review, local assumption, cheaper entropy normalization or stronger arithmetic estimate is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete final statement and every declared consequence and domain. |
| argument | [Argument](#argument) | Every numbered and unnumbered argument, all costs, branches, interfaces and provenance. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Formal trace recurrence, reproduced before field use. |
| dependency | [Dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted Kronecker characterization. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete actual finite-field roots and order groups. |
| dependency | [Dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Simple-root unramified lifting and Frobenius. |
| dependency | [Dependency](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Full original norm and valuations. |
| dependency | [Dependency](../ledger/Yin_L_G0067_v1.md#cyclic-prime-power-norm-floor) | Integral-order prime-power certificate; local costs rederived. |
| review | [Review](../audits/reviews/Yin_R_G0798_v1.md#salem-involution-whole-independent-finding) | Entire17-equation account, complete actual input interfaces, every original depth/window and same-input prime comparison. |


### Decision current-scalar-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:08 |
| status | proved |
| reason | Select the complete C244 retained scalar/cyclic norm and actual power-order quotient proof as the identical current responsible home of the already used L67 interfaces. The complete original/current proof and exact used domains were read. Mathematical status, selected statement/argument/finding, all relation scopes and other current homes remain unchanged; original dated decisions and R bindings keep their actual L67 inputs. This routine locator adoption supplies no new independent review, two-factor coverage, universal period bound or stronger scalar assumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete final statement and every declared consequence and domain. |
| argument | [Argument](#argument) | Every numbered and unnumbered argument, all costs, branches, interfaces and provenance. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Formal trace recurrence, reproduced before field use. |
| dependency | [Dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted Kronecker characterization. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete actual finite-field roots and order groups. |
| dependency | [Dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Simple-root unramified lifting and Frobenius. |
| dependency | [Dependency](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Full original norm and valuations. |
| dependency | [Dependency](Yin_C_G0244_v1.md#cyclic-prime-power-norm-floor) | Integral-order prime-power certificate; local costs rederived. |
| review | [Review](../audits/reviews/Yin_R_G0798_v1.md#salem-involution-whole-independent-finding) | Entire17-equation account, complete actual input interfaces, every original depth/window and same-input prime comparison. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete final statement and every declared consequence and domain. |
| argument | [Argument](#argument) | Every numbered and unnumbered argument, all costs, branches, interfaces and provenance. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Formal trace recurrence, reproduced before field use. |
| dependency | [Dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted Kronecker characterization. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete actual finite-field roots and order groups. |
| dependency | [Dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Simple-root unramified lifting and Frobenius. |
| dependency | [Dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Full original norm and valuations. |
| dependency | [Dependency](Yin_C_G0244_v1.md#cyclic-prime-power-norm-floor) | Integral-order prime-power certificate; local costs rederived. |
| review | [Review](../audits/reviews/Yin_R_G0798_v1.md#salem-involution-whole-independent-finding) | Entire17-equation account, complete actual input interfaces, every original depth/window and same-input prime comparison. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:28 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete final statement and every declared consequence and domain. |
| argument | [Exact retained argument](#argument) | Every numbered and unnumbered argument, all costs, branches, interfaces and provenance. |
| dependency | [Exact retained dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Formal trace recurrence, reproduced before field use. |
| dependency | [Exact retained dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted Kronecker characterization. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete actual finite-field roots and order groups. |
| dependency | [Exact retained dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Simple-root unramified lifting and Frobenius. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Full original norm and valuations. |
| dependency | [Exact retained dependency](Yin_C_G0244_v1.md#cyclic-prime-power-norm-floor) | Integral-order prime-power certificate; local costs rederived. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0798_v1.md#salem-involution-whole-independent-finding) | Entire17-equation account, complete actual input interfaces, every original depth/window and same-input prime comparison. |


### Decision isolated-current-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:50 |
| status | proved |
| reason | Adopt the new isolated R798 whole finding for this exact highest physical statement and complete argument, after necessary fixed-mathematics/source inspection and subsequent comparison with all original review accounts. Preserve the complete current mathematical status, input relations and scopes, all original costs and open coverage limits. R798 separately retains the original unknown findings, dates, exact historical bindings, missing-table observations and negative predecessor findings; this new independent review does not retrospectively upgrade them or claim source-proof audits or Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete final statement and every declared consequence and domain. |
| argument | [Exact retained argument](#argument) | Every numbered and unnumbered argument, all costs, branches, interfaces and provenance. |
| dependency | [Exact retained dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Formal trace recurrence, reproduced before field use. |
| dependency | [Exact retained dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted Kronecker characterization. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete actual finite-field roots and order groups. |
| dependency | [Exact retained dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Simple-root unramified lifting and Frobenius. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Full original norm and valuations. |
| dependency | [Exact retained dependency](Yin_C_G0244_v1.md#cyclic-prime-power-norm-floor) | Integral-order prime-power certificate; local costs rederived. |
| review | [Isolated current whole finding](../audits/reviews/Yin_R_G0798_v1.md#g136-current-whole-independent) | Entire exact current statement and complete argument, every necessary original/current mathematical interface, original norms/weights/times/costs, source depth, finite controls and explicit limits; old physical-version and relationship findings remain separate in R798. |
