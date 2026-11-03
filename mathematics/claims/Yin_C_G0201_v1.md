---
author: Yin
---
# Actual Salem two-five compatibility forces endpoint contact at unit endpoint norm

Date: 2026-10-20T16:33.
Human author Yin.
Root supplied the exact maximum-trace product formula and requested a bounded comparison with existing endpoint and contact results.
The retained_methods_audit agent supplied the M=1 endpoint exclusion, the complete single-factor and prefactor inequalities, and the exact trace/angle consequence below.
Both are mathematical contributors to this new candidate; neither independently reviews it.
The agent's earlier R632/R633 roles concern different fixed comparisons and do not review this proof.
The bounded local reuse check found the old endpoint norm identity and its degree-dependent limitation in C107, and different finite-frequency or projection-contact interfaces in C159/C168.
None of those inspected statements supplies the present coupled two-five product exclusion.
No broad novelty assertion, new source theorem, mathematical program, numerical scan or selected input is used.

<a id="statement"></a>
## Exact theorem statement

Let P in Z[z] be the monic irreducible minimal polynomial of a genuine Salem number lambda>1.
Precisely, P has degree d=2r>=4, constant coefficient1 and reciprocal symmetry, its two real roots are lambda and lambda^(-1), and all its other roots are nonreal numbers of modulus1 paired by inversion.
Use the TOTAL logarithmic Mahler measure m(P)=log lambda.
Write the actual reciprocal representation and fields as

    P(z)=z^r T(z+z^(-1)),
    K=Q(lambda), delta_0=lambda+lambda^(-1),
    F=Q(delta_0), [K:F]=2, [F:Q]=r.

Here T in Z[X] is the actual monic irreducible degree-r trace polynomial.
Its roots are delta_0>2 and distinct delta_j in(-2,2) for1<=j<=r-1.
For k>=0 define C_k by C_k(z+z^(-1))=z^k+z^(-k), so C_2(X)=X^2-2 and C_5(X)=X^5-5X^3+5X.
The actual quotient values are

    a=T(C_2(delta_0))/2=theta_2(delta_0),
    c=T(C_5(delta_0))/5=theta_5(delta_0),
    theta_p=rem_T(T(C_p))/p in Z[X], deg theta_p<r, p=2,5.

They are nonzero integral elements of this specified trace order Z[delta_0].
Assume the ACTUAL field identity

    f=2c^2-3a^5=0.                                  (EC1)

No second residual equation involving the three-prime coordinate b or g is assumed.
Put

    x=delta_0-2>0, t_j=2-delta_j in(0,4),
    M=|P(1)|=|T(2)|=x product_(j=1)^(r-1)t_j,
    a_k=C_k(2+x)-2, q_k=a_k/x, k=2,5.

Then M is a positive integer and the complete identity is

    75/64=M^(-3) A_*(x)
                product_(j=1)^(r-1)
                  [(1+a_5/t_j)^2/(1+a_2/t_j)^5],
    A_*(x)=(q_5-1)^2/(q_2-1)^5.                    (EC2)

If the additional hypothesis M=1 holds, at least one inner trace root satisfies the strict endpoint contact

    0<t_j=2-delta_j<a_2=x(4+x).                    (EC3)

Consequently, writing the corresponding inverse circle pair as exp(plus-or-minus i theta_j) with0<theta_j<pi, the exact scale is

    t_j=4sin(theta_j/2)^2
          <2cosh(2m(P))-2=4sinh(m(P))^2,
    sin(theta_j/2)<sinh(m(P)).                      (EC4)

When sinh(m(P))<1 this also gives theta_j<2arcsin(sinh(m(P))).
At larger m the sine statement is still valid but need not restrict the already known interval0<theta_j<pi.
This is a necessary condition on the stated genuine-Salem, M=1, actual f=0 class.
It supplies no actual member of that class, no contradiction from the contact alone, no uniform Mahler gap, and no endpoint-contact assertion for arbitrary reciprocal inputs or for M>=2.

<a id="argument"></a>
## Complete proof

### Actual endpoint norm and exact quotient product

The adopted [C153v2 trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) supplies the displayed monic T, actual field degrees, integral remainders and nonzero quotient values.
The genuine Salem root configuration makes F totally real: every trace embedding is one of the displayed delta_j.
The endpoint identity is also the one already retained in [C107's signed-norm assessment](Yin_C_G0107_v1.md#signed-norm-gap-assessment), not a new independent norm income.
Directly factoring at2 gives

    T(2)=(2-delta_0)product_(j=1)^(r-1)(2-delta_j)
         =-x product_j t_j<0.

Since P(1)=T(2) is a nonzero integer, M=-T(2) is a positive integer.
Every factor t_j is strictly positive; the endpoints+/-2 are excluded by the genuine Salem minimal-polynomial hypotheses.
No trace embedding or inverse pair has been removed from this factorization.

For k=2,5, the explicit polynomials give a_k>x>0, and hence

    T(C_k(delta_0))
      =T(2+a_k)
      =(a_k-x)product_j(a_k+t_j)
      =M(q_k-1)product_j(1+a_k/t_j).               (EC5)

This is an identity for the SAME original T at both exponents.
It uses no assertion of independence among the t_j, no reduction of their number, and no replacement of the actual quotient by a freely chosen positive element.
All terms in(EC5) are positive at this largest trace embedding.
Clearing the two actual denominators in(EC1) gives

    64 T(C_5(delta_0))^2
       =75 T(C_2(delta_0))^5.

Dividing by the nonzero positive fifth power and substituting(EC5) proves(EC2), with precisely M^(2-5)=M^(-3).
The equality holds under f=0 in F; no unsupported implication from a numerical approximate equality is involved.

### Complete single-factor estimate on the proposed noncontact region

Direct expansion gives

    a_2=4x+x^2,
    a_5=25x+50x^2+35x^3+10x^4+x^5,
    R(x)=a_5/a_2>=25/4.                            (EC6)

Indeed

    a_5-(25/4)a_2
       =x^2(175/4+35x+10x^2+x^3)>0

for x>0.
For a positive t put y=a_2/t and

    h_R(y)=(1+R y)^2/(1+y)^5.

If t>=a_2, then0<y<=1 and h_R(y)>=h_(25/4)(y), because its numerator is increasing in R.
For R=25/4 the logarithmic derivative is

    (d/dy)log h_R(y)
       =2R/(1+R y)-5/(1+y)
       =(2R-5-3R y)/[(1+R y)(1+y)].               (EC7)

The denominator is positive and the numerator vanishes only at y=2/5.
Thus h_(25/4) increases on[0,2/5] and decreases on[2/5,1], so its minimum on[0,1] is the smaller endpoint value.
Those exact endpoint values are

    h_(25/4)(0)=1, h_(25/4)(1)=841/512>1.

It follows that

    t>=a_2 implies
    (1+a_5/t)^2/(1+a_2/t)^5>=1.                    (EC8)

This estimate is uniform in the trace degree and contains no fixed-degree limit or approximation in x.
It is asserted only on the specified noncontact region t>=a_2; for smaller positive t no such lower bound is inserted.

### Exact monotonic prefactor and the M=1 contradiction

The same expansions give

    q_2-1=x+3,
    p(x):=q_5-1=x^4+10x^3+35x^2+50x+24,
    A_*(x)=p(x)^2/(x+3)^5.

Every factor is positive for x>=0.
Its logarithmic derivative has positive denominator (x+3)p(x) and numerator

    2(x+3)p'(x)-5p(x)
        =3x^4+34x^3+145x^2+270x+180>0.            (EC9)

Therefore A_* is strictly increasing on[0,infinity), and for x>0

    A_*(x)>A_*(0)=24^2/3^5=64/27>75/64.           (EC10)

The last inequality is the exact positive-integer comparison4096>2025.
Suppose now M=1 and every t_j>=a_2.
Each factor in(EC2) is at least1 by(EC8), so its right side is at least A_*(x), which is strictly greater than75/64 by(EC10).
This contradicts(EC2).
Since there are r-1>=1 inner trace roots, the negation supplies at least one t_j<a_2, proving(EC3).
All inequalities at the proposed boundary t_j=a_2 are included; no equality case is omitted.

### Exact original measure and circle angle

The genuine Salem hypothesis means that lambda is the only original root outside the unit circle.
The ordinary scalar Mahler convention in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) therefore gives total m(P)=log lambda, not m(P)/d.
Thus

    delta_0=2cosh(m(P)),
    x=2cosh(m(P))-2,
    x(4+x)=delta_0^2-4
           =2cosh(2m(P))-2=4sinh(m(P))^2.          (EC11)

For the selected delta_j in(-2,2), choose the unique theta_j in(0,pi) with delta_j=2cos theta_j.
Its two original roots are exp(i theta_j) and exp(-i theta_j), and t_j=2-2cos theta_j=4sin(theta_j/2)^2.
The positive square roots of(EC3) and(EC11) yield(EC4).
If sinh(m(P))<1, the sine function is strictly increasing on(0,pi/2), so applying its inverse gives the stated angle bound.
No inverse-sine expression outside its real domain is used.
The exact trace upper scale is asymptotic to4m(P)^2 and the angle upper scale to2m(P) as m(P) decreases to0, as follows from the elementary hyperbolic/trigonometric functions in(EC11).
These scales describe a necessary contact along any hypothetical sequence in this restricted class; they assert no such sequence exists.

<a id="scope-and-unpaid-product"></a>
## What the endpoint product does not pay

For M>=2 the exact equation retains M^(-3), or equivalently

    product_j [(1+a_5/t_j)^2/(1+a_2/t_j)^5]
            =75 M^3/[64 A_*(x)].                  (EC12)

It is not legitimate to drop M^3 or replace this full product by1 merely because x is small.
The number and positions of the inner trace roots vary with the original input.
Even under a separate noncontact hypothesis t_j>=a_2, the proof gives only the lower bound1 for each factor, not a degree-uniform upper bound or a convergent product.
The contradiction at M=1 consequently does not establish the same conclusion for M>=2.

The old endpoint identity alone gives x>=4^(-(r-1)) from M>=1 and t_j<4, at a degree-dependent scale.
C107 already explains that limitation.
The new deduction instead uses actual f=0 to require an inner trace root at the scale(EC3) on the M=1 subclass.
Neither that old endpoint lower bound nor the new necessary contact proves the contact impossible.
No distribution theorem for these inner roots, lower bound for their separation from2, or paid upper estimate for the original mixed resultant has been supplied here.

The proof concerns the actual two-five quotients of the original genuine Salem polynomial.
It does not replace the unreduced G circle function by a canonical remainder, identify an original full norm with a Haar mean, invoke a torsion control, or settle the signed discrepancy in C195.
It applies in particular if a full residual input additionally satisfies its hypotheses, but the second residual equation, g!=0 and the trace-order index are not needed or established.
The M=1 arithmetic subclass and the genuine Salem root configuration remain essential stated restrictions of this candidate.

<a id="exact-inputs"></a>
## Exact inputs and review boundary

| Input | Actual role and limit |
| --- | --- |
| [C153v2 actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual P=z^rT, K/F degree2, trace roots, nonzero integral quotient remainders and phase definitions; no arbitrary reciprocal total-reality inference. |
| [C107 endpoint comparison](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Credit for M=abs(P(1))=-T(2)=x product t_j and its existing degree-dependent limitation; not a prior proof of EC2 or EC3. |
| [Smy08-U001 scalar convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Total logarithmic Mahler root product, giving m(P)=log lambda in this exact Salem configuration; no new source-proof audit. |

The new product, elementary scalar inequalities and all applications are proved in full above.
The author checked the expansions, quotient denominators2 and5, fifth-versus-square exponents, M^(-3), every strict endpoint, all degree labels and the real inverse-sine domain.
This author check is not independent review and makes no adoption decision.
A separate whole review of the actual candidate, its original-domain restrictions and complete argument is still required.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-21)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T16:33 |
| status | open |
| reason | Register the complete original genuine-Salem f=0 product identity and M=1 endpoint-contact necessity, with full scalar costs, exact trace/angle scale and unrestricted-product limitations. Root and the assigned endpoint author are contributors; whole independent review and adoption remain pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Genuine Salem d=2r>=4, actual integral two-five quotients, f=0, exact all-M product, strict M=1 inner endpoint contact and its full original-measure/angle scale. |
| argument | [Complete argument](#argument) | Every EC1--EC12 identity/inequality, original endpoint factorization, single-factor minimum, monotonic prefactor, all strict boundaries and noncoverage at M>=2. |
| dependency | [Actual reciprocal trace theorem](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Same actual P/T/K/F, integral nonzero trace quotients and original quadratic degree; the genuine Salem configuration supplies total reality. |
| dependency | [Scalar Mahler convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Full original root product gives total m=log lambda, without dividing by d or losing inverse/circle pairs. |
| support | [Prior endpoint identity and limitation](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Existing endpoint evaluation and degree-dependent floor, reused with its precise scope and rederived for the current variables. |

### Decision whole-reviewed-2026-10-21

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T16:37 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft inquiries. |
| reason | Adopt the entire actual genuine-Salem two-five endpoint theorem through whole independent R488 after reading its full proof and finding. Preserve the all-M product and M^(-3) cost, the strict M=1 contact and exact total-measure/angle scope, all original quotient and source relations, and the absence of an actual realization, M>=2 contact conclusion or uniform gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Genuine Salem d=2r>=4, actual integral two-five quotients, f=0, exact all-M product, strict M=1 inner endpoint contact and its full original-measure/angle scale. |
| argument | [Complete argument](#argument) | Every EC1--EC12 identity/inequality, original endpoint factorization, single-factor minimum, monotonic prefactor, all strict boundaries and noncoverage at M>=2. |
| dependency | [Actual reciprocal trace theorem](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Same actual P/T/K/F, integral nonzero trace quotients and original quadratic degree; the genuine Salem configuration supplies total reality. |
| dependency | [Scalar Mahler convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Full original root product gives total m=log lambda, without dividing by d or losing inverse/circle pairs. |
| support | [Prior endpoint identity and limitation](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Existing endpoint evaluation and degree-dependent floor, reused with its precise scope and rederived for the current variables. |
| review | [Whole independent endpoint finding](../audits/reviews/Yin_R_G0488_v1.md#salem-endpoint-contact-whole-finding) | Entire actual EC1--EC12, both dependencies and sole support, full original root and scalar conventions, all inequalities and strict boundaries, exact contact scale and unpaid M>=2/varying-product limits; actual R516 and source scopes preserved with no reviewer proof contribution. |

