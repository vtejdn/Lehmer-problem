---
author: Yin
---

# Monic residual quotient with an actual-order factor 1000 and paid normalization

Human author Yin.
This physical successor retains the complete [C611v1 statement](Yin_C_G0611_v1.md#statement), its full proof, selected adoption and [R813 finding](../audits/reviews/Yin_R_G0813_v1.md#monic-residual-quotient-whole-finding) at their exact unchanged scope.
Root supplied the new expanded-numerator congruences modulo 8 and 125 and the proposed factor 1000 in the original order on 2026-10-23 UTC.
Paid_comparison checked and developed the complete integer identities, monic cancellation, original-order remainder, norm normalization and paid sufficient class below.
Both are contributors to this new mathematics; neither is its independent reviewer.
The earlier R813 is not enlarged to this extension.
No mathematical program, parameter scan, source acquisition or new original-source proof inspection is used.

## Statement

Use the ENTIRE original domain of v1.
Explicitly, P in Z[z] is monic irreducible reciprocal nontorsion, constant coefficient1, degree d=2r>=2, with root alpha and K=Q(alpha).
Put delta=alpha+alpha^(-1), assume the actual trace field Q(delta) is totally real, and let T be its monic minimal trace polynomial.
Use C_p(z+z^(-1))=z^p+z^(-p), theta_p=rem_T T(C_p)/p for p=2,3,5, and the actual integral values a=theta_2(delta), b=theta_3(delta), c=theta_5(delta).
For e=b^2-a^3, f=2c^2-3a^5 and g=c^3-2b^5 assume

    f=e+s g=0, g!=0, s in{1,-1}.

Retain the SAME full polynomials

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    h=9d/2, Z=z^(5d)+1,
    F_s=3375s z^h H23+8H35-5Z H25,
    D_s=F_s/P, N_s=H35 D_s,
    J_s=3375s z^(h-1)(hH23+zH23')+8H35'-5Z H25'.

**A. Complete unchanged v1 scope.**
All of v1 Parts A--C remain part of this statement: exact content4 of W_s, primitive quotients, monic reciprocal integral F_s/D_s of degrees15d/14d and constant coefficient1, primitive reciprocal N_s of degree29d with endpoint coefficients7, the original J_s criterion and signed norm ratio, the full all-sign ninth-power endpoint bound and the original RAW normalization conclusion.
Their complete necessary arguments remain in [physical v1](Yin_C_G0611_v1.md#complete-argument), selected as a fixed dependency.
In particular the exact original nonvanishing test is still

    D_s(alpha)!=0 iff P does not divide J_s,
    Norm_K D_s(alpha)=Res(P,J_s)/Res(P,P').          (1)

The denominator is nonzero and a zero numerator remains possible.

**B. New actual-order divisibility.**
In the ordinary integer polynomial ring, with ideal notation (A,m), one has

    F_s in(P^2,8), F_s in(P^5,125),
    D_s in(P,8), D_s in(P^4,125),
    rem_P D_s in1000 Z[z].                         (2)

Consequently the ACTUAL original-order element satisfies

    D_s(alpha)/1000 in Z[alpha].                   (3)

If the equivalent nonzero conditions in (1) hold, then

    abs Norm_K D_s(alpha)
       =1000^d abs Norm_K(D_s(alpha)/1000)
       >=1000^d.                                 (4)

No maximal-order saturation, discarded index, derivative division or discriminant estimate is used to establish (3)--(4).
The exact ratio in (1) is compatible with (4), not a loss to be subtracted again.
The monic constant-one POLYNOMIAL D_s is not coefficientwise divisible by1000.
Its rational polynomial normalization v_s=D_s/1000 has leading and constant coefficients1/1000, while its value at alpha is integral.
The integral polynomial b_s=(rem_P D_s)/1000 of degree<d represents that value; it is not substituted for v_s in any Haar or coefficient comparison.

**C. Fully paid normalized sufficient class.**
Put k0=30375, tau=(12/11)log2 and J_G=2m(H35)-2log k0, with TOTAL logarithmic Mahler measure throughout.
Fix independently of P a constant eta>0, integers K_0>=2,S_0>=1, and a positive rational q with

    exp(tau/2-eta/2)<=q<exp(tau/2)=2^(6/11).

On the explicitly supplied class satisfying

    P does not divide J_s,
    J_G+2m(D_s)-2log1000<=tau-2eta,
    #supp(N_s)<=K_0,
    ||N_s||_1/(30375000q)<=S_0,                   (5)

the actual ordinary rational polynomial

    u_s=N_s/(30375000q)

has degree29d, the stated support and coefficient budgets, and

    abs Norm_K u_s(alpha)
       =abs Norm_K g * abs Norm_K(D_s(alpha)/1000)/q^d
       >=(2^(6/11)/q)^d>1,
    m(u_s)=J_G/2+m(D_s)-log1000-log q<=-eta/2.      (6)

Therefore the COMPLETE C196v5 NF1--NF8 theorem applies with C_0=29 and eta_0=min{eta/2,1}, yielding

    m(P)>h_star(K_0,S_0,eta_0)/29>0.               (7)

The function h_star is the exact finite positive constant of that fixed theorem; it has not been numerically inverted here.
All original degrees, rational scalars, nonzero norms and actual coefficients remain charged.
No integrality of u_s(alpha) is asserted; (6) supplies the norm-only hypothesis.

A useful split-budget corollary replaces the combined Mahler condition in (5) by

    J_G<=tau-2eta,
    m(D_s)<=log1000+eta/4.                        (8)

With the same nonvanishing and actual numerator budgets, (7) then holds with eta_0=min{eta/4,1}.
If the second bound is strengthened to m(D_s)<=log1000, the stronger eta_0=min{eta/2,1} is valid.
Thus the proved actual-order income permits the D_s Mahler ceiling to increase bylog1000 and its full coefficient denominator to increase by1000, with the scalar paid on both sides.
Neither ceiling nor the actual sparse coefficient budgets have been proved automatically.

**D. Endpoint cost after the new normalization.**
The unchanged v1 bound gives

    ||u_s||_1>=700|P(1)|^9/(30375000q).            (9)

In particular ||u_s||_1<=1 implies |P(1)|<=3.
This is only a necessary bound for this newly normalized polynomial.
The old raw statement at divisor30375q still implies |P(1)|=1 and remains unchanged.
No bounded-endpoint input, nonzero value, useful Mahler ceiling, uniform sparse numerator, original near-one sequence or unrestricted G0001 conclusion is constructed.

## Reuse and changed proof responsibility

The author actually read v1's selected adoption and exact proof, C605's complete normalization and all its missing-budget qualifications, C196v5 NF1--NF8, and the retained original-order Frobenius quotient convention before this derivation.
A targeted search for factor1000, the modulo125 quotient and this F_s found no earlier exact retained account.
The root-proposed argument uses the direct coefficientwise Frobenius congruences already standard in the project, but its application to the monic residual quotient is written fully below.
The fixed actual g norm floor is [C191v2](Yin_C_G0191_v2.md#statement), with its matched original phase and degree in [C587v2 DR1--DR5](Yin_C_G0587_v2.md#full-residual-direct-original-polynomial-reuse).
The final analytic theorem is the complete [C196v5 norm-only proof](Yin_C_G0196_v5.md#norm-only-sparse-transfer).
Its source constants, original powered-degree accounting, finite regularization, radial and Fourier expenses are reused without enlargement or reproof.
The scalar Mahler conventions and multiplicativity are the already inspected [Smy08-U001 normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
No additional external result or source proof is required.

The old v1 norm conclusion used only that a nonzero D_s(alpha) is integral.
The NEW statement proves a specified scalar divisibility in the actual free power-basis order, yielding (4) and allowing the rational POLYNOMIAL v_s with integral original value.
This is new arithmetic income, not a coefficientwise content extraction from the primitive N_s or monic D_s.
Nonvanishing is a separate condition, exactly as in v1.
Root's proof contribution and the author's present checking/development prevent either from independently reviewing this new extension.

## Complete proof of the extension

The entire unchanged v1 statement and proof are used at their exact fixed scopes.
In particular F_s=P D_s with both polynomials integral, d is even, P is monic, the original phase h is integral, and the complete original nonvanishing and endpoint criteria hold.
No step below infers those facts from a navigation record or mutable draft.

### 1. Full expanded numerator and integer Frobenius differences

Write P_j=P(z^j).
Expanding the ACTUAL definition of F_s gives exactly

    F_s=30375s z^h P_2^3-27000s z^h P_3^2
          +2000P_3^5-1944P_5^3
          -375ZP_2^5+320ZP_5^2.                  (10)

The phases and the common Z=z^(5d)+1 are retained.
These are expansions of the same polynomials, not replacements modulo P or constructions with independent inputs.

For p=2 or5 put

    Delta_p=(P(z^p)-P(z)^p)/p in Z[z].

To check coefficientwise integrality, reduce in F_p[z].
The binomial identity in characteristic p eliminates mixed terms, and every integer coefficient satisfies a^p=a modulo p.
Hence P(z)^p=P(z^p) there, proving the stated divisibility over Z coefficient by coefficient.
No quotient order or irreducibility premise is needed for this identity.
Consequently

    P_2=P^2+2Delta_2,
    P_5=P^5+5Delta_5.                             (11)

### 2. The exact modulo 8 and modulo 125 memberships

In (10), the coefficients27000,2000,1944 and320 are all divisible by8.
Thus modulo8 only30375s z^hP_2^3 and-375ZP_2^5 need to be checked.
The first expansion is

    P_2^3=P^6+6P^4Delta_2+12P^2Delta_2^2
                                    +8Delta_2^3,

so it belongs to(P^2,8).
In the fifth-power expansion of(P^2+2Delta_2)^5, every term except the last contains P^2, while the last is32Delta_2^5 and is divisible by8.
Therefore P_2^5 also belongs to(P^2,8).
Multiplying by the actual integer scalars and phases in (10) and adding the other terms proves

    F_s in(P^2,8).                                (12)

For modulus125, the coefficients30375,27000,2000 and375 are divisible by125.
The two surviving terms are-1944P_5^3 and320ZP_5^2.
By (11),

    P_5^3=P^15+15P^10Delta_5+75P^5Delta_5^2
                                      +125Delta_5^3,
    320ZP_5^2=320ZP^10+3200ZP^5Delta_5
                                      +8000ZDelta_5^2.

Every term except the last in each line contains P^5.
The final terms are divisible by125, including8000=64*125 in the second line.
Thus

    F_s in(P^5,125).                              (13)

The coefficient320 is not itself divisible by125; its factor25 from the squared Frobenius difference was essential.
Equations (12)--(13) retain all cross terms and do not infer the stronger coefficientwise divisibility of F_s by8 or125.

### 3. Cancellation by monic P in the original integer order

Here is the precise cancellation needed for these ideals.
If an integer polynomial P is monic, F=P D with D integral, and

    F=P^j A+m B, A,B in Z[z], j>=1, m>=1,

then P divides m B.
Take the unique monic remainder R=rem_P B in Z[z], of degree<d.
Since the remainder of m B is m R and vanishes, every coefficient of m R is zero in Z.
Therefore R=0 and B=P C for an integer polynomial C.
Cancelling P in the integral polynomial domain now gives

    D=P^(j-1)A+m C,
    D in(P^(j-1),m).                              (14)

This uses neither coprimality of P with m in a polynomial ring nor division by m in an integral order.
It is valid even if P has repeated factors modulo a prime divisor of m.

Apply (14) to (12) with j=2,m=8 and to (13) with j=5,m=125.
This proves

    D_s in(P,8), D_s in(P^4,125).

The remainder R_s^*=rem_P D_s therefore has every coefficient divisible by8 and also by125.
Since these two integers are coprime, every coefficient is divisible by1000.
Writing b_s=R_s^*/1000 in Z[z] gives the exact original-value identity

    D_s(alpha)=1000 b_s(alpha), deg b_s<d.          (15)

The ring Z[alpha] is the actual quotient Z[z]/(P), free over Z in its usual degree-d basis.
Equation (15) proves (3) in this order itself, without passing to an overorder.
It also covers b_s=0, equivalently D_s(alpha)=0.
The unchanged J_s criterion decides exactly that zero branch; no positive norm is assigned there.

When b_s(alpha)!=0 its full K norm is a nonzero integer.
Taking the norm of (15) over all d original embeddings gives (4).
The original ratio in (1) consequently is divisible by1000^d as an integer whenever it is nonzero; its derivative denominator does not reduce the newly proved original-order floor.
No assertion of optimality of1000 or exact valuation is made.

The equality D_s(alpha)/1000=b_s(alpha) concerns VALUES.
Because D_s has leading coefficient1 and constant coefficient1, D_s/1000 is not in Z[z].
Neither its degree14d nor the degree29d of N_s is lowered in the analytic construction below.
Replacing it by b_s would change the circle function and its Mahler cost, and no such replacement is made.

### 4. Complete norm and scalar Mahler normalization

Assume the nonvanishing condition P does not divide J_s.
By v1 and (15), this is precisely b_s(alpha)!=0.
The fixed original residual theorem gives

    abs Norm_K g>=2^(6d/11),
    H35(alpha)=-k0 alpha^(15d/2)g,
    Norm_K alpha=1,
    k0=30375.                                    (16)

All roots and the full field degree d are retained.
The exponent15d/2 is integral because d is even.
For the ACTUAL rational polynomial u_s=N_s/(1000k0q), the evaluation is

    u_s(alpha)=-alpha^(15d/2)g b_s(alpha)/q.

The sign and unit phase have absolute norm1.
Hence the exact original norm is

    abs Norm_K u_s(alpha)
       =abs Norm_K g * abs Norm_K b_s(alpha)/q^d
       >=(2^(6/11)/q)^d>1.                        (17)

The factor1000 has cancelled through the proved equality of original values (15), not through a conjectured coefficient content.
The rational q still contributes the FULL q^d denominator.
The original normalized polynomial value need not be integral, which is why the actual norm-only theorem is invoked.

For the Haar cost use the same scalar normalization on the whole circle polynomial:

    m(u_s)=m(H35)+m(D_s)-log(1000k0q)
           =J_G/2+m(D_s)-log1000-log q.            (18)

Every polynomial here is nonzero, so its finite circle zeros have integrable logarithms under the retained scalar Mahler convention.
The rational polynomial v_s=D_s/1000 has m(v_s)=m(D_s)-log1000, but this identity does not assert a bound on either side.
The combined condition in (5), together with log q>=tau/2-eta/2, gives

    m(u_s)<=tau/2-eta-(tau/2-eta/2)=-eta/2.

The actual degree is29d, the support is exactly that of N_s, and its coefficient norm is exactly||N_s||_1/(30375000q).
The endpoint coefficients are7/(30375000q), not integer unit coefficients.
Thus all of C196v5 NF1 are supplied at C_0=29, K_0,S_0 and eta_0=min{eta/2,1}.
Its complete NF2--NF8 proof then yields (7), with every finite analytic and source expense unchanged.
This verifies all hypotheses rather than treating the factor1000 as an uncharged scalar improvement.

### 5. Split savings, endpoint cost and precise open obligations

Under (8), equation (18) instead gives

    m(u_s)<=tau/2-eta+eta/4-(tau/2-eta/2)
           =-eta/4.

The same exact degree, support, coefficient and norm identities prove the stated corollary using eta_0=min{eta/4,1}.
If m(D_s)<=log1000, the same calculation removes the eta/4 term and gives-eta/2.
All constants, including eta,q,K_0,S_0, are fixed before the input class is chosen; an empty class is permitted and no actual member is supplied by this conditional implication.

The complete old endpoint theorem is||N_s||_1>=700|P(1)|^9.
Applying the NEW denominator1000k0q gives (9).
For |P(1)|>=4 and q<2^(6/11)<2, its right side is strictly greater than

    700*4^9/(60750000)
       =183500800/60750000>1.

Thus||u_s||_1<=1 implies|P(1)|<=3.
The raw denominator in v1 was k0q rather than1000k0q, so its earlier unit-endpoint conclusion remains correct at that different normalization.
The ninth-power obstruction still excludes a fixed coefficient budget for this candidate on any class with unbounded|P(1)|.

The new arithmetic result supplies a genuine original-order normalization and a larger permitted Mahler ceiling.
It does not prove P does not divide J_s, the combined or split Mahler upper bound, uniform support, or actual normalized coefficient control on the remaining bounded-endpoint class.
The exact open algebraic test remains J_s modulo P; the analytic test is now the paid quantity J_G+2m(D_s)-2log1000 and the actual degree29d numerator.
Those conditions cannot be replaced by the lower degree of the integer remainder b_s or by monicity of D_s.
No new original input, numerical diagnostic, original-root/Haar equality or unrestricted gap is claimed.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision actual-order-normalization-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T16:30 |
| status | open |
| reason | Register the substantive v2 extension with complete actual-order factor1000, exact norm and scalar normalization, combined/split paid sufficient classes and the adjusted endpoint cost. Retain complete v1 and its review at their unchanged scope. Root and paid_comparison are contributors; separate whole review and adoption are required. No automatic nonvanishing, useful Mahler/sparse class or Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire v2 statement](#statement) | All unchanged v1 Parts A--C plus new actual-order memberships/factor1000, full norms, rational polynomial versus integral value, complete combined/split sufficient classes and new endpoint normalization. |
| argument | [Complete new proof and predecessor use](#complete-proof-of-the-extension) | Every exact expansion, monic cancellation, original remainder, zero/nonzero branch, scalar Mahler/full norm, actual support/degree/coefficient and finite analytic application, together with the explicitly retained whole v1 proof. |
| dependency | [Complete physical v1](Yin_C_G0611_v1.md#complete-argument) | Entire original domain, exact F_s=P D_s, all content/reciprocity/degree/endpoint data, precise J_s/nonvanishing/signed-norm identities and complete all-sign ninth-power bound. |
| dependency | [Actual residual norm floor](Yin_C_G0191_v2.md#statement) | Full original field bound abs Norm_K(g)>=2^(6d/11) with actual trace/full residual hypotheses, unchanged original degree and all embeddings. |
| dependency | [Matched original normalization](Yin_C_G0587_v2.md#full-residual-direct-original-polynomial-reuse) | Exact same H35, k0, alpha^(15d/2) phase, J_G and original norm convention in (16)--(18). |
| dependency | [Complete norm-only analytic theorem](Yin_C_G0196_v5.md#norm-only-sparse-transfer) | Entire NF1--NF8 at C_0=29 and the actually supplied fixed K_0,S_0,eta_0, retaining every finite/source/radial/Fourier and powered-degree cost. |
| dependency | [Scalar Mahler convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only its Mahler normalization section: exact scalar shift, multiplicativity, total measure and integrable circle zeros, at the existing source-inspection scope. |
| support | [Old sufficient multiplier scope](Yin_C_G0605_v1.md#statement) | Earlier integer-multiplier budget and exact scalar boundary; this extension proves the new actual-value divisibility instead of silently applying that old integer-polynomial premise to D_s/1000. |
| support | [Unchanged v1 review](../audits/reviews/Yin_R_G0813_v1.md#monic-residual-quotient-whole-finding) | Existing independent evidence for physical v1 only, not a review or adoption of the new factor1000 and its normalized transfer. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T16:43 |
| status | proved |
| reason | Adopt the whole v2 including retained v1, exact original-order factor1000, full norm and rational-circle normalization, combined/split paid sufficient classes and revised endpoint budget after isolated whole R814. Original nonvanishing, useful Mahler bounds, uniform expanded numerator budgets and actual input coverage remain hypotheses, not achieved results. The accepted source and predecessor boundaries remain unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire v2 statement](#statement) | All unchanged v1 Parts A--C plus new actual-order memberships/factor1000, full norms, rational polynomial versus integral value, complete combined/split sufficient classes and new endpoint normalization. |
| argument | [Complete new proof and predecessor use](#complete-proof-of-the-extension) | Every exact expansion, monic cancellation, original remainder, zero/nonzero branch, scalar Mahler/full norm, actual support/degree/coefficient and finite analytic application, together with the explicitly retained whole v1 proof. |
| dependency | [Complete physical v1](Yin_C_G0611_v1.md#complete-argument) | Entire original domain, exact F_s=P D_s, all content/reciprocity/degree/endpoint data, precise J_s/nonvanishing/signed-norm identities and complete all-sign ninth-power bound. |
| dependency | [Actual residual norm floor](Yin_C_G0191_v2.md#statement) | Full original field bound abs Norm_K(g)>=2^(6d/11) with actual trace/full residual hypotheses, unchanged original degree and all embeddings. |
| dependency | [Matched original normalization](Yin_C_G0587_v2.md#full-residual-direct-original-polynomial-reuse) | Exact same H35, k0, alpha^(15d/2) phase, J_G and original norm convention in (16)--(18). |
| dependency | [Complete norm-only analytic theorem](Yin_C_G0196_v5.md#norm-only-sparse-transfer) | Entire NF1--NF8 at C_0=29 and the actually supplied fixed K_0,S_0,eta_0, retaining every finite/source/radial/Fourier and powered-degree cost. |
| dependency | [Scalar Mahler convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only its Mahler normalization section: exact scalar shift, multiplicativity, total measure and integrable circle zeros, at the existing source-inspection scope. |
| support | [Old sufficient multiplier scope](Yin_C_G0605_v1.md#statement) | Earlier integer-multiplier budget and exact scalar boundary; this extension proves the new actual-value divisibility instead of silently applying that old integer-polynomial premise to D_s/1000. |
| support | [Unchanged v1 review](../audits/reviews/Yin_R_G0813_v1.md#monic-residual-quotient-whole-finding) | Existing independent evidence for physical v1 only, not a review or adoption of the new factor1000 and its normalized transfer. |
| review | [Whole isolated independent finding](../audits/reviews/Yin_R_G0814_v1.md#actual-order-normalization-whole-finding) | Entire v2 and unchanged v1, every selected input, all ideal/order/norm/degree/scalar identities, complete NF1--NF8 application and exhaustive endpoint arithmetic, with actual source limits preserved. |

