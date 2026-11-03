---
author: Yin
---
# Balanced H25 weighting with preserved full norm income and a logarithmic screen

Human author Yin.
Root develops this project deduction under the resumed G0001 authority, following the S1 balanced-weight specification.
A prior separate strategy discussion suggested the weighted case split; that contributor is not the independent reviewer of this argument.
This changes the actual algebraic auxiliary value and is a new statement, not a revision of the unweighted C155 theorem.
No numerical test or general-input coverage is asserted here.

## Statement

Let F be a totally real number field of degree r and let a,b,c be nonzero algebraic integers in F.
Set e=b^2-a^3, f=2c^2-3a^5 and g=c^3-2b^5.
For every integer q>=1, the integral element H_q=q^2(e^2+g^2)+f^2 is totally positive and

    Norm_F(H_q)>=(2q)^r.

For every monic irreducible reciprocal nontorsion integer-unit polynomial P of degree d=2r with ACTUAL totally real trace field F=Q(alpha+alpha^(-1)), put K=Q(alpha) and use the integral trace quotients of C153v2.
Define the integer polynomials

    H23=9P(t^2)^3-8P(t^3)^2,
    H25=75P(t^2)^5-64P(t^5)^2,
    H35=250P(t^3)^5-243P(t^5)^3,
    L=972000,
    A23=(L/72)^2 t^(9d) H23^2,
    A25=(L/800)^2 t^(5d) H25^2,
    A35=(L/30375)^2 H35^2,
    A_bal,q=q^2(A23+A35)+A25,
    B_bal,q=t^(-15d) A_bal,q/(q L^2).

Then A_bal,q is reciprocal of exact degree30d with leading and constant coefficient50176q^2, and B_bal,q has support[-15d,15d].
Its value at alpha is H_q/q, and

    Norm_K(B_bal,q(alpha))=Norm_F(H_q)^2/q^d>=2^d,
    Norm_K(B_bal,q(alpha))=Res(P,A_bal,q)/(q L^2)^d.

H_q/q is not asserted integral.
For normalized Haar measure mu on the unit circle, set

    U=|H23/72|^2+|H35/30375|^2, V=|H25/800|^2,
    J_U=integral log U dmu, J_V=integral log V dmu,
    I_bal(q)=integral log(q U+q^(-1)V) dmu.

Both component logarithms are integrable, including their possible circle zeros.
For every real q>0, the circle comparison gives

    I_bal(q)>=log2+(J_U+J_V)/2.

For integer q>=1 the original arithmetic bound and exact scalar Jensen identity both apply, with

    I_bal(q)=m(A_bal,q)-log q-2log L,
    log2<=log Norm_K(B_bal,q(alpha))/d
        <=log sup_circle B_bal,q+30m(P).

The real-q circle comparison does not assert an algebraic norm theorem for nonintegral q.
A nonnegative certified J_U+J_V excludes I_bal(q)<log2 for every positive real q on that fixed P; it does not exclude other P or other auxiliaries.
No original-root/Haar transfer bound, degree-uniform gap or automatic totally-real coverage is asserted.

<a id="argument"></a>
## Arithmetic proof with all support cases

Reuse C153v2's pairwise exclusions for the stated nonzero integral triple over a totally real field: e=g=0 and f=g=0 are impossible.
Thus at least one defect is nonzero, every embedding preserves its nonvanishing, and H_q is totally positive.
The following three cases are exhaustive.

If f!=0, at least one of e,g is nonzero, because otherwise e=g=0.
Choose that fixed nonzero integral defect x from e,g.
For every real embedding sigma,

    sigma(H_q)>=q^2 sigma(x)^2+sigma(f)^2
              >=2q |sigma(x)sigma(f)|.

Multiplying over all r embeddings gives Norm_F(H_q)>=(2q)^r |Norm_F(x)Norm_F(f)|>=(2q)^r.
The final inequality uses both nonzero integer norms; the defect choice is made in F, not separately at different embeddings.

If f=0 and e!=0, the exclusion f=g=0 gives g!=0.
Now H_q=q^2(e^2+g^2), hence

    Norm_F(H_q)>=q^(2r) 2^r |Norm_F(e)Norm_F(g)|
              >=(2q^2)^r>=(2q)^r.

If f=e=0, then g!=0 and C155's complete singleton argument gives Norm_F(g^2)>=5^r.
Therefore Norm_F(H_q)=q^(2r)Norm_F(g^2)>=(5q^2)^r>=(2q)^r.
This reuses the stronger singleton conclusion, including its rational-norm integrality, divisibility and full quadratic-subfield multiplicity; the weaker unweighted2^r floor alone is not being substituted for it.
These cases prove the stated integral-triple result for every integer q>=1.

<a id="original-return"></a>
## Original trace values, phases, norms and support

C153v2 gives P(t)=t^r T(t+t^(-1)) for the actual irreducible integral trace polynomial T, of degree r, and [K:F]=2.
With C_0(x)=2,C_1(x)=x,C_(n+1)=x C_n-C_(n-1), the elements

    a=rem_T(T(C_2)/2)(alpha+alpha^(-1)),
    b=rem_T(T(C_3)/3)(alpha+alpha^(-1)),
    c=rem_T(T(C_5)/5)(alpha+alpha^(-1))

are the nonzero integral trace quotients proved there.
They are defined at the actual trace generator; reduction modulo T is not a circle-polynomial identity.
The exact C149/C153v2 evaluations are

    H23(alpha)=-72 alpha^(6r)e,
    H25(alpha)=-800 alpha^(10r)f,
    H35(alpha)=-30375 alpha^(15r)g.

Consequently t^(-15d)A23/L^2, t^(-15d)A25/L^2 and t^(-15d)A35/L^2 evaluate to e^2,f^2,g^2 respectively, since d=2r.
This proves B_bal,q(alpha)=q(e^2+g^2)+q^(-1)f^2=H_q/q.
The full norm tower is Norm_K(H_q)=Norm_F(H_q)^2, and Norm_K(q)=q^d.
Thus the stated full norm lower bound follows without an integrality claim about the quotient.
Since P is monic of even degree and constant coefficient1, Norm_K(alpha)=1.
Taking the norm of the exact centered Laurent formula therefore also gives the displayed resultant identity, retaining all original conjugates and every smaller-own-field multiplicity.

C149's H23,H25,H35 are reciprocal of degrees6d,10d,15d with leading coefficients1,11,7 respectively.
The A23,A25 supports lie in[9d,21d],[5d,25d], whereas A35 has full endpoints0,30d, each50176.
Their common reciprocal center is15d, proving the exact asserted support, degree and endpoints for A_bal,q.
The supplied denominator qL^2 is retained even if a particular polynomial admits cancellation.
For a circle point z, reciprocity of a real polynomial H of even degree N gives z^(-N)H(z)^2=|H(z)|^2.
Applying this to the three summands proves B_bal,q(z)=qU(z)+q^(-1)V(z).

The same polynomial maximum-principle argument used in C153v2/C155 bounds the centered Laurent value at each original root beta by sup_circle B_bal,q times max(|beta|,|beta|^(-1))^(15d).
Summing logarithms over all d roots and dividing by d costs

    15 sum_beta |log|beta||=30m(P),

because P is monic with constant coefficient1.
This proves the stated supremum return, with no replacement of that supremum by a Haar average.

<a id="logarithmic-screen"></a>
## Integrable logarithms and the parameter-independent screen

The nonzero H25 has degree10d and leading coefficient11, so V is nonzero except at finitely many circle points.
Similarly U is nonzero except possibly at finitely many points, since it contains the nonzero H35 square.
Their logarithmic integrals are finite: log V=2log|H25|-2log800, while U is bounded above and U>=|H35/30375|^2 gives an integrable lower bound for log U.
A nonzero polynomial has only finite-order zeros, whose logarithmic singularities on the circle are integrable.
Thus no strict-positivity assumption or numerical regularization is needed.

For any fixed real q>0 and every circle point with U V>0, weighted arithmetic-geometric mean gives

    qU+q^(-1)V>=2sqrt(UV),
    log(qU+q^(-1)V)>=log2+(log U+log V)/2.

The exceptional set is finite and the right side is integrable.
The left logarithm is integrable as well, by its bounded upper value and lower bound log(qU) almost everywhere.
Integration proves the lower envelope for every positive real q.
Equality would require a compatible pointwise ratio; no attainment by a constant q is claimed.

The useful exact component normalizations are

    J_U=m(A23+A35)-2log L,
    J_V=2m(H25)-2log800.

Indeed the centering monomials have zero Haar logarithm, and the displayed circle identities retain the entire leading scalar and root multiplicities.
The same nonmonic/Laurent Jensen identity from F109 gives I_bal(q)=m(A_bal,q)-log q-2log L for integer q>=1 (and the corresponding real-coefficient identity for real q>0).
This identity accommodates all circle zeros and supplies no estimate comparing Haar measure to the original-root measure.

## Author check and boundary

Root checked the exhaustive three cases, every nonzero integer norm, the exact phases and squared field multiplicity, q^d in the full norm denominator, endpoints50176q^2, logarithmic integrability and the30m return.
This candidate is ready for a separate whole review; the earlier strategy discussion and this author check are not independent acceptance.
The proposed finite computational test has not been executed in this material.

## Current assessment
[Selected decision](#decision-current-haar-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T09:05 |
| status | open |
| reason | Register the complete balanced-weight arithmetic and logarithmic-screen candidate for independent whole review before numerical use in the resumed G0001 test. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete balanced-weight statement](#statement) | All integral triples, exact original totally-real trace domain, every integer q>=1, full norms, exact costs and the real-positive-q circle screen. |
| argument | [Complete proof](#argument) | All support cases, original return, integrable logarithms and lower-envelope proof, including the later original-return and logarithmic-screen sections. |
| dependency | [Corrected pairwise exclusions](Yin_C_G0153_v2.md#argument) | The impossible simultaneous pairs e=g=0 and f=g=0 over a totally real field for nonzero integral a,b,c. |
| dependency | [Actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Nonzero integral trace quotients, degrees r and2r, actual total reality and the exact original phases. |
| dependency | [Strong singleton floor](Yin_C_G0155_v1.md#argument) | The e=f=0 case Norm_F(g^2)>=5^r, with its full field-norm and integer-divisibility proof. |
| dependency | [Original numerator formulas](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Exact H23,H25,H35, degrees, reciprocity, leading coefficients and supplied denominators. |
| dependency | [Existing supremum-return method](Yin_C_G0155_v1.md#original-polynomial-return) | Polynomial maximum principle for centered support[-15d,15d]; the changed-value scalar and full norm are proved locally. |
| dependency | [Scalar Jensen normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Nonmonic/Laurent identity, complete root multiplicities and integrable circle zeros. |

### Decision whole-reviewed-2026-10-18

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T09:08 |
| status | proved |
| reason | Adopt the complete balanced-weight theorem after the actual whole R376 independent review. All support cases, actual trace domain, full rational normalization, support and radial costs, and logarithmic-zero treatment are resolved at the exact stated scope. This accepts the mathematical gate for the bounded Stage1 diagnostic, not any numerical outcome or original-root/Haar transfer theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete balanced-weight statement](#statement) | All integral triples, exact original totally-real trace domain, every integer q>=1, full norms, exact costs and the real-positive-q circle screen. |
| argument | [Complete proof](#argument) | All support cases, original return, integrable logarithms and lower-envelope proof, including the later original-return and logarithmic-screen sections. |
| dependency | [Corrected pairwise exclusions](Yin_C_G0153_v2.md#argument) | The impossible simultaneous pairs e=g=0 and f=g=0 over a totally real field for nonzero integral a,b,c. |
| dependency | [Actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Nonzero integral trace quotients, degrees r and2r, actual total reality and the exact original phases. |
| dependency | [Strong singleton floor](Yin_C_G0155_v1.md#argument) | The e=f=0 case Norm_F(g^2)>=5^r, with its full field-norm and integer-divisibility proof. |
| dependency | [Original numerator formulas](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Exact H23,H25,H35, degrees, reciprocity, leading coefficients and supplied denominators. |
| dependency | [Existing supremum-return method](Yin_C_G0155_v1.md#original-polynomial-return) | Polynomial maximum principle for centered support[-15d,15d]; the changed-value scalar and full norm are proved locally. |
| dependency | [Scalar Jensen normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Nonmonic/Laurent identity, complete root multiplicities and integrable circle zeros. |
| review | [Whole independent finding](../audits/reviews/Yin_R_G0376_v1.md#balanced-weight-whole-independent-finding) | Complete statement and argument, all six declared interfaces, every support case, phase and norm scalar, radial fee and integrable logarithmic screen. |

### Decision current-haar-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:45 |
| status | proved |
| reason | Select adopted C_F6 as the current complete responsible home of the identical retained scalar Haar/Jensen normalization. Its actual selected adoption and complete normalization section were read and matched to the original fixed L_F5 text, including Laurent shifts, leading coefficients, all root multiplicities and integrable circle zeros. Only that normalization is reused here, with every original scalar, phase and cost retained; no Gram optimization, root-distribution transfer or new review is supplied. Mathematical status, statement, full argument, selected findings and every relation scope remain unchanged; original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete balanced-weight statement](#statement) | All integral triples, exact original totally-real trace domain, every integer q>=1, full norms, exact costs and the real-positive-q circle screen. |
| argument | [Complete proof](#argument) | All support cases, original return, integrable logarithms and lower-envelope proof, including the later original-return and logarithmic-screen sections. |
| dependency | [Corrected pairwise exclusions](Yin_C_G0153_v2.md#argument) | The impossible simultaneous pairs e=g=0 and f=g=0 over a totally real field for nonzero integral a,b,c. |
| dependency | [Actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Nonzero integral trace quotients, degrees r and2r, actual total reality and the exact original phases. |
| dependency | [Strong singleton floor](Yin_C_G0155_v1.md#argument) | The e=f=0 case Norm_F(g^2)>=5^r, with its full field-norm and integer-divisibility proof. |
| dependency | [Original numerator formulas](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Exact H23,H25,H35, degrees, reciprocity, leading coefficients and supplied denominators. |
| dependency | [Existing supremum-return method](Yin_C_G0155_v1.md#original-polynomial-return) | Polynomial maximum principle for centered support[-15d,15d]; the changed-value scalar and full norm are proved locally. |
| dependency | [Scalar Jensen normalization](Yin_C_F0006_v1.md#scalar-capacity-normalization) | Nonmonic/Laurent identity, complete root multiplicities and integrable circle zeros. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0376_v1.md#balanced-weight-whole-independent-finding) | Complete statement and argument, all six declared interfaces, every support case, phase and norm scalar, radial fee and integrable logarithmic screen. |
