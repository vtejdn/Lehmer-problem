---
author: Yin
---
# Balanced buffered cross-term shears with a preserved full norm floor

Human author Yin.
The shear_arithmetic agent supplies the buffered shear proof and original phase calculation; root supplies the balanced extension and its direct numerator construction.
The cross_term_reuse agent supplies the all-parameter component screen added in this second physical version.
All three are contributors, and none can supply an independent review of this argument.
Version1 remains preserved with its earlier fixed-s screen; version2 adds the stronger all-(s,q) exclusion criterion without changing its arithmetic theorem.
The buffered q=1 argument was developed in D37 before this fixed reusable extension.
The unbuffered shear's different residual norm obligation remains there and is not adopted here.
No numerical test, useful Haar gap, original-root/Haar transfer or general-input coverage is asserted.

<a id="statement"></a>
## Exact theorem statement

Let F be a totally real number field of degree r and let a,b,c be nonzero algebraic integers in F.
Set e=b^2-a^3, f=2c^2-3a^5 and g=c^3-2b^5.
For every integer s and every integer q>=1 define

    H_(s,q)=q^2[(e+s g)^2+2g^2]+f^2.

Then H_(s,q) is totally positive and

    Norm_F(H_(s,q))>=(2q)^r.

For an original monic irreducible reciprocal nontorsion P in Z[t] of degree d=2r and constant coefficient1, assume its ACTUAL trace field F=Q(alpha+alpha^(-1)) is totally real.
Put K=Q(alpha) and use the nonzero integral trace quotients of C153v2.
Define

    H23=9P(t^2)^3-8P(t^3)^2,
    H25=75P(t^2)^5-64P(t^5)^2,
    H35=250P(t^3)^5-243P(t^5)^3,
    L=972000,
    A_(U,s)=[13500 t^(9d/2)H23+32s H35]^2+2*32^2 H35^2,
    A25=1215^2 t^(5d)H25^2,
    A_(s,q)=q^2 A_(U,s)+A25,
    B_(s,q)=t^(-15d) A_(s,q)/(q L^2).

All displayed exponents are integers.
A_(s,q) is an integer reciprocal polynomial of exact degree30d with leading and constant coefficient50176(s^2+2)q^2.
B_(s,q) has centered support[-15d,15d], evaluates at alpha to H_(s,q)/q, and satisfies the complete original norm identities

    Norm_K(B_(s,q)(alpha))=Norm_F(H_(s,q))^2/q^d>=2^d,
    Norm_K(B_(s,q)(alpha))=Res(P,A_(s,q))/(q L^2)^d.

The quotient H_(s,q)/q is not asserted integral.
For the exact centered circle functions

    E(t)=-t^(-3d)H23(t)/72,
    F_0(t)=-t^(-5d)H25(t)/800,
    G(t)=-t^(-15d/2)H35(t)/30375,
    U_s=(E+sG)^2+2G^2, V=F_0^2,

put J_(U,s)=integral log U_s dmu and J_V=integral log V dmu for normalized circle Haar measure mu.
These logarithms are integrable despite possible circle zeros.
For every real q>0, the circle expression has

    I_(s,q)=integral log(q U_s+q^(-1)V) dmu
           >=log2+(J_(U,s)+J_V)/2.

This comparison remains valid for real s as a circle statement; its algebraic norm assertion is restricted to integer s and integer q>=1.
For those integer parameters the complete scalar and radial normalizations are

    I_(s,q)=m(A_(s,q))-log q-2log L,
    J_(U,s)=m(A_(U,s))-2log L,
    J_V=2m(H25)-2log800,
    log2<=log Norm_K(B_(s,q)(alpha))/d
        <=log sup_circle B_(s,q)+30m(P).

A certified J_(U,s)+J_V>=0 therefore excludes I_(s,q)<log2 for every positive real q at that fixed P and fixed s.
No such numerical sign is asserted here.

There is also a screen independent of both parameters.
Put

    J_G=integral log G^2 dmu=2m(H35)-2log30375.

For every real s and every real q>0,

    I_(s,q)>=3log2/2+(J_G+J_V)/2.

Consequently J_G+J_V+log2>=0 excludes I_(s,q)<log2 for ALL real s and ALL positive real q on that fixed P.
This is a circle comparison only for nonintegral parameters and asserts no numerical sign or arithmetic norm theorem beyond the integer domain stated above.

<a id="argument"></a>
## Full arithmetic proof

Reuse the C153v2 pairwise exclusions e=g=0 and f=g=0 for nonzero a,b,c in the stated totally real field.
Thus a fixed nonzero defect exists, and the nonnegative sum H_(s,q) is positive at every real embedding.
The following cases exhaust all possibilities.

If f=0, the exclusion f=g=0 gives g!=0.
At every real embedding sigma,

    sigma(H_(s,q))>=2q^2 sigma(g)^2.

Hence Norm_F(H_(s,q))>=(2q^2)^r Norm_F(g)^2>=(2q)^r, since q>=1 and Norm_F(g) is a nonzero integer.
This includes e+s g=0, without requiring any stronger singleton norm estimate.

If f!=0 and g!=0, the q^2 g^2 and f^2 summands alone give

    sigma(H_(s,q))>=q^2 sigma(g)^2+sigma(f)^2
                  >=2q |sigma(g)sigma(f)|.

Multiplying all r inequalities yields Norm_F(H_(s,q))>=(2q)^r|Norm_F(g)Norm_F(f)|>=(2q)^r.

If f!=0 and g=0, the exclusion e=g=0 gives e!=0.
Now e+s g=e, so the same argument applied to e,f gives the claimed norm floor.
Every choice of a nonzero element is made in F and holds simultaneously at every embedding.
All chosen norms are the complete integer norms, not norms at one real embedding or in a smaller own field without multiplicity.
This proves the general integral-triple theorem for every stated s,q.

The coefficient2 on g^2 is essential to this proof's singleton case.
The statement does not include the unbuffered form with coefficient1, whose transformed singleton relation f=0,e+s g=0 need not satisfy C155's different e=f=0 hypothesis.

<a id="original-return"></a>
## Exact trace phases, numerator and full norms

C153v2 gives P(t)=t^r T(t+t^(-1)) for the actual irreducible trace polynomial T in Z[x], degree r, and [K:F]=2.
Write C_0(x)=2,C_1(x)=x,C_(n+1)=x C_n-C_(n-1).
The actual elements

    a=rem_T(T(C_2)/2)(alpha+alpha^(-1)),
    b=rem_T(T(C_3)/3)(alpha+alpha^(-1)),
    c=rem_T(T(C_5)/5)(alpha+alpha^(-1))

are nonzero algebraic integers.
Reduction modulo T identifies their values at the original trace generator; it is not a global circle-function identity.
The exact C149/C153v2 phases are

    H23(alpha)=-72 alpha^(3d)e,
    H25(alpha)=-800 alpha^(5d)f,
    H35(alpha)=-30375 alpha^(15d/2)g.

Thus the centered functions E,F_0,G evaluate to e,f,g, respectively.
Their real reciprocal numerators have degrees6d,10d,15d and leading coefficients1,11,7.
Because d is even, every half-degree center is integral.
For a real reciprocal polynomial H of even degree N and a circle point t, t^(-N/2)H(t) is real.
It follows that E,F_0,G are real on the circle, and their squares equal |H23/72|^2, |H25/800|^2, |H35/30375|^2 respectively.

Direct expansion proves the exact rational Laurent identities

    t^(-15d) A_(U,s)/L^2=(E+sG)^2+2G^2,
    t^(-15d) A25/L^2=F_0^2,
    B_(s,q)=q[(E+sG)^2+2G^2]+q^(-1)F_0^2.

The first square uses the aligned numerator 13500 t^(9d/2)H23+32s H35; its two summands have common reciprocal center15d/2.
The shifted H23 summand has support[9d/2,21d/2], strictly inside[0,15d], and H35 has support[0,15d].
Thus A_(U,s) is reciprocal about15d.
Only the H35 terms contribute at the endpoints0,30d, with coefficient49*32^2(s^2+2)=50176(s^2+2)>0.
The A25 support[5d,25d] is strictly internal, proving the stated exact degree, endpoint coefficients and Laurent support for A_(s,q) and B_(s,q).
The supplied scalar qL^2 is retained even if a particular input permits cancellation.

Evaluating gives B_(s,q)(alpha)=H_(s,q)/q.
By the norm tower and [K:F]=2,

    Norm_K(H_(s,q)/q)=Norm_F(H_(s,q))^2/q^d>=2^d.

Since P is monic, even-degree and constant coefficient1, Norm_K(alpha)=1.
Taking the full K norm of the centered Laurent identity yields Res(P,A_(s,q))/(qL^2)^d, proving the other complete norm identity.
All original conjugates are retained, as are the repetitions when a value lies in a proper subfield.

For completeness, let M=sup_circle B_(s,q), which is positive.
The maximum principle applied to A_(s,q) on the disk gives |A_(s,q)(t)|<=qL^2 M for |t|<=1.
Its degree30d gives |A_(s,q)(t)|<=qL^2 M |t|^(30d) for |t|>=1, by applying the disk bound to the reciprocal polynomial.
Consequently, for every nonzero complex t,

    |B_(s,q)(t)|<=M max(|t|,|t|^(-1))^(15d).

Apply this at all d original roots, take logarithms and divide by d.
Because P is monic with constant coefficient1, sum_beta |log|beta||=2m(P), so the radial fee is exactly30m(P).
This establishes the claimed supremum return, without replacing the supremum by a Haar mean.

<a id="logarithmic-screen"></a>
## Integrable logarithms and the balancing screen

For any fixed real s, U_s>=2G^2 on the unit circle.
The nonzero H35 has only finitely many circle zeros, each of finite order, so log(2G^2) is integrable and supplies an almost-everywhere integrable lower bound for log U_s.
The continuous U_s is bounded above and nonzero except possibly at those finitely many points; hence its logarithm is integrable.
Likewise log V=2log|H25|-2log800 is integrable since H25 is nonzero.
This uses no numerical regularization or uniform strict-positivity assertion.

For each real q>0 and almost every circle point,

    qU_s+q^(-1)V>=2sqrt(U_s V),
    log(qU_s+q^(-1)V)>=log2+(log U_s+log V)/2.

The left logarithm is integrable by its bounded upper value and the lower bound log(qU_s).
Integrating proves the lower envelope simultaneously as a statement for every fixed real s and q>0.
No attainment by a constant q is asserted.

For integer s and q>=1 the exact Laurent identities and F109's nonmonic scalar Jensen identity give all three displayed Mahler normalizations.
The same circle identities hold with real coefficients for real parameters, but they do not imply algebraic integrality or the arithmetic norm theorem there.
A nonnegative component sum excludes a sub-log2 Haar average for the entire positive-q family at that fixed input and s only.
The circle screen is logically distinct from comparing original conjugate averages with Haar averages.

The lower bound U_s>=2G^2 also gives

    J_(U,s)>=log2+J_G,
    J_G=2m(H35)-2log30375.

The complete scalar and every root multiplicity remain in this equality.
Substitution into the preceding lower envelope yields I_(s,q)>=3log2/2+(J_G+J_V)/2 for every real s and q>0.
Equivalently, the pointwise inequality qU_s+q^(-1)V>=2sqrt(2G^2 V) can be integrated directly away from the finitely many zeros.
Both logarithms on its right are integrable as already established, so these exceptional points create no gap.
If J_G+J_V+log2>=0, its right side is at least log2, proving the all-parameter exclusion criterion.
The bound need not be attained by any constant parameters.

## Author check and limits

The drafting author checked the complete three-case arithmetic proof, the absence of a C155 singleton dependency, exact phases and half-degree shifts, numerator endpoints, full q^d norm denominator, scalar Jensen terms, integrable zeros and30m radial fee.
At this version's original stage, the [unbuffered residual](../ledger/Yin_L_G0438_v1.md#unbuffered-reduction) remained unresolved, with no asserted solution; that dated responsibility is retained there.
This candidate is ready for a separate whole review.
No independent acceptance or numerical output is supplied by the author check.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-18)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T10:02 |
| status | open |
| reason | Register the complete balanced buffered shear theorem as the arithmetic and exact-normalization gate for a possible bounded cross-term diagnostic under active G0001 authority. The unbuffered residual is explicitly excluded; this second version adds the elementary all-(s,q) component screen before whole review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete balanced buffered statement](#statement) | All nonzero integral triples in a totally real field, every integer s and integer q>=1, exact original trace domain, full norms and costs, and both the fixed-s and all-(s,q) real-parameter circle screens. |
| argument | [Complete proof](#argument) | All three arithmetic cases, exact original-return section, scalar and norm multiplicities, and logarithmic-screen section including zero integrability. |
| dependency | [Totally real pairwise exclusions](Yin_C_G0153_v2.md#argument) | Only e=g=0 and f=g=0 are excluded for the actual nonzero integral triple; no transformed singleton estimate is imported. |
| dependency | [Actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual total reality, integral nonzero trace quotients, degrees r and2r, and exact phases. |
| dependency | [Original numerator formulas](Yin_C_G0149_v1.md#original-polynomials-and-norms) | H23,H25,H35, supplied denominators, reciprocity, degrees and leading coefficients. |
| dependency | [Scalar Jensen normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Complete nonmonic/Laurent identity with root multiplicities and integrable circle zeros. |

### Decision whole-reviewed-2026-10-18

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T10:07 |
| status | proved |
| reason | Adopt the complete integer-parameter buffered-shear norm theorem, exact original return and both circle screens after the actual whole R378 review of this second physical version. The new buffer handles the transformed singleton without importing C155's different case. This accepts the gate for the bounded component diagnostic, not its unevaluated sign or an unrestricted gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete balanced buffered statement](#statement) | All nonzero integral triples in a totally real field, every integer s and integer q>=1, exact original trace domain, full norms and costs, and both the fixed-s and all-(s,q) real-parameter circle screens. |
| argument | [Complete proof](#argument) | All three arithmetic cases, exact original-return section, scalar and norm multiplicities, and logarithmic-screen section including zero integrability. |
| dependency | [Totally real pairwise exclusions](Yin_C_G0153_v2.md#argument) | Only e=g=0 and f=g=0 are excluded for the actual nonzero integral triple; no transformed singleton estimate is imported. |
| dependency | [Actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual total reality, integral nonzero trace quotients, degrees r and2r, and exact phases. |
| dependency | [Original numerator formulas](Yin_C_G0149_v1.md#original-polynomials-and-norms) | H23,H25,H35, supplied denominators, reciprocity, degrees and leading coefficients. |
| dependency | [Scalar Jensen normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Complete nonmonic/Laurent identity with root multiplicities and integrable circle zeros. |
| review | [Whole independent finding](../audits/reviews/Yin_R_G0378_v1.md#buffered-shear-whole-independent-finding) | Complete v2 statement and argument, all four dependency interfaces, all integer parameters, exact full normalization and both real-parameter screens with integrable zeros. |
