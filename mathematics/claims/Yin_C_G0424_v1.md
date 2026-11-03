---
author: Yin
---

# Complete uniform primitive-trinomial positive limit and exact rational certificate

The entire original D44 proof is retained from [L179](../ledger/Yin_L_G0179_v1.md#retained-trinomial-limit-argument).
The orbit_research author supplied every limit/section/integral/certificate derivation and explicitly self-checked the complete argument, retained in [R78](../audits/reviews/Yin_R_G0078_v1.md#trinomial-limit-original-author-check-finding).
The coordinator assigned the question without those derivations; the original [whole finding](../audits/reviews/Yin_R_G0078_v1.md#trinomial-limit-independent-review) has unestablished actual initial progress/shared-context contents and remains unknown for independent-review purposes.
The accepted full Lawton statement and its uninspected original-proof boundary are explicit, while every local application and integral estimate is present here.
No new source/PDF read, numerical integral, enlarged45-row scan, native program or Task/E execution is added.

## Statement

For every integer pair 0<b<a with gcd(a,b)=1 put

    f_(a,b)(t)=t^a-t^b-1,
    f*_(a,b)(t)=t^a f_(a,b)(1/t),
    G_(a,b)(t)=[(f*_(a,b))^2 f_(a,b)(t^2)
                            +f_(a,b)^2 f*_(a,b)(t^2)]/2,
    Delta_(a,b)=log2+m(G_(a,b))-3m(f_(a,b)).

All m are full logarithmic Mahler measures, including every leading coefficient and factor.
No seed irreducibility is assumed and no cyclotomic or auxiliary factor is dropped.
Let

    F(u,v)=uv-u-1, H(u,v)=1-v-uv,
    G(u,v)=[H(u,v)^2 F(u^2,v^2)+F(u,v)^2 H(u^2,v^2)]/2.

The complete fixed integer expansion of G is retained below.
Substitution(u,v)=(t^b,t^(a-b)) gives exactly f,f*,G_(a,b), with nonzero specializations.
There is one real constant

    Delta_infinity=log2+m(G)-3m(F)>1/250

such that Delta_(a,b) converges to it uniformly over the entire primitive pair class as a tends to infinity.
Consequently there exists an integer A_0 such that every a>=A_0 in that class has Delta_(a,b)>1/500.
Only finitely many primitive pairs have Delta<=1/500, in particular Delta<=0.
Neither an effective A_0 nor emptiness of the remaining finite exception set is proved.

The only non-elementary dependency is the already accepted full Lawton statement at Den09-U002, for arbitrary integer specialization vectors and polynomials with zeros, as the sup-norm relation parameter tends to infinity.
Here q(b,a-b)=max(b,a-b)>=a/2.
A sequence contradiction gives uniformity without a bound on b/a or a convergence rate.
Den09's invertible-only result would not suffice, and the original Lawton proof is not audited.

The full local sectional calculation gives

    m(G)=(2/pi) integral_0^(pi/6)
        arcosh((4cos^2(theta)-1)(2cos^2(theta)-1)) dtheta,
    m(F)=(2/pi) integral_0^(pi/3) log(2cos(theta)) dtheta.

Its rotated reciprocal quartic has trace roots
xi_+=-A+sqrt(A^2+D^2), xi_-=-A-sqrt(A^2+D^2),
where A=cos(3theta),D=4cos^2(theta)-1 and A^2+D^2>0.
All interior/exterior/double-endpoint branches, bounded positive/negative logarithmic parts and Fubini through torus zeros are proved below.
The exact complete two-variable phase integral also equals Delta_infinity.

Two elementary lower intervals and the concavity upper bound give

    m(G)>log48/12,
    3m(F)<=log(1+sqrt3)<log(11/4),
    Delta_infinity>(1/12)log(48*8^12/11^12)>1/250.

The final strict margin has the displayed integer certificate, without quadrature or root approximation.
The earlier45 discovery decimals are not a premise.
This excludes an arbitrarily large primitive-trinomial negative-balance sequence, including the seed-Phi6 cases, at the complete balance only.
It does not settle all finite degrees, supply an effective cutoff, construct a near-one or Salem family, or transfer a full measure/phase inequality to a selected irreducible factor.
The broader height-one negative construction has a different seed class and is compatible with this theorem.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:13 |
| status | open |
| reason | Retain the entire primitive-trinomial all-offset Lawton application, full rotated-quartic/Jensen/integrability calculation and exact positive rational certificate, with every factor, external-proof boundary and ineffective finite-exception limit. Current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete uniform positive-limit theorem](#statement) | Entire original D44 Sections1--5/formulas(1)--(17): all primitive 0<b<a/gcd(a,b)=1 trinomials without irreducibility, complete original-degree doubling auxiliary/all factors/leading coefficients, exact fixed F/H/G specialization and q=max(b,a-b)>=a/2, accepted full qualitative Lawton including zeros and all-offset uniformity without a rate, full two-variable phase identity and log-integrability, rotated reciprocal quartic/trace-root/Jensen/hyperbolic calculation including all endpoint cases, exact two-angle/concavity/integer certificate Delta_infinity>1/250, eventual Delta>1/500 and finite possible exceptions with no effective degree cutoff, no all-degree sign/near-one/gap or selected-factor transfer. |
| argument | [Entire original analytic proof and certificate](#argument) | Entire original D44 Sections1--5/formulas(1)--(17): all primitive 0<b<a/gcd(a,b)=1 trinomials without irreducibility, complete original-degree doubling auxiliary/all factors/leading coefficients, exact fixed F/H/G specialization and q=max(b,a-b)>=a/2, accepted full qualitative Lawton including zeros and all-offset uniformity without a rate, full two-variable phase identity and log-integrability, rotated reciprocal quartic/trace-root/Jensen/hyperbolic calculation including all endpoint cases, exact two-angle/concavity/integer certificate Delta_infinity>1/250, eventual Delta>1/500 and finite possible exceptions with no effective degree cutoff, no all-degree sign/near-one/gap or selected-factor transfer. |
| dependency | [Complete sparse seed/auxiliary identities](Yin_C_G0412_v1.md#sparse-trinomial-auxiliary) | Only exact original-degree F/H/G expansion, seed-Phi6/nonmonic exceptions and full untruncated phase normalization, retaining all factors and leading coefficients. The earlier45 discovery decimals are unused. |
| dependency | [Accepted full Lawton statement including zeros](../audits/literature/Den09/Yin_U002.md#den09-u002) | Only the retained Theorem14/Example15 for arbitrary integer specialization vectors, sup-norm relation parameter and full polynomial Mahler limit including zeros; its original proof is not audited and no effective rate or invertible-only substitute is supplied. |
| support | [Complete earlier uniform all-offset argument](Yin_C_G0271_v1.md#essential-family-mahler-limit) | The exact sequence-contradiction method for uniformity in an all-vector Lawton limit. The present q/F/G/integrability/certificate proof is local, with no reuse of the different essential-family constant or effective cutoff. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:16 |
| status | proved |
| reason | Adopt after actual whole current self-check of the entire fixed F/H/G/all-offset full-Lawton application, reciprocal quartic/trace/Jensen/integrability calculation, exact two-interval/concavity/integer positive-margin certificate and ineffective finite-exception conclusion. Every original factor/source-proof/degree/offset limitation was checked, not inferred from old PASS or45 discovery decimals. No substantive defect or missing hypothesis was found; this whole SELF does not close the original whole UNKNOWN arrangement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire original D44 Sections1--5/formulas(1)--(17): all primitive 0<b<a/gcd(a,b)=1 trinomials without irreducibility, complete original-degree doubling auxiliary/all factors/leading coefficients, exact fixed F/H/G specialization and q=max(b,a-b)>=a/2, accepted full qualitative Lawton including zeros and all-offset uniformity without a rate, full two-variable phase identity and log-integrability, rotated reciprocal quartic/trace-root/Jensen/hyperbolic calculation including all endpoint cases, exact two-angle/concavity/integer certificate Delta_infinity>1/250, eventual Delta>1/500 and finite possible exceptions with no effective degree cutoff, no all-degree sign/near-one/gap or selected-factor transfer. |
| argument | [Exact retained argument](#argument) | Entire original D44 Sections1--5/formulas(1)--(17): all primitive 0<b<a/gcd(a,b)=1 trinomials without irreducibility, complete original-degree doubling auxiliary/all factors/leading coefficients, exact fixed F/H/G specialization and q=max(b,a-b)>=a/2, accepted full qualitative Lawton including zeros and all-offset uniformity without a rate, full two-variable phase identity and log-integrability, rotated reciprocal quartic/trace-root/Jensen/hyperbolic calculation including all endpoint cases, exact two-angle/concavity/integer certificate Delta_infinity>1/250, eventual Delta>1/500 and finite possible exceptions with no effective degree cutoff, no all-degree sign/near-one/gap or selected-factor transfer. |
| dependency | [Exact retained dependency](Yin_C_G0412_v1.md#sparse-trinomial-auxiliary) | Only exact original-degree F/H/G expansion, seed-Phi6/nonmonic exceptions and full untruncated phase normalization, retaining all factors and leading coefficients. The earlier45 discovery decimals are unused. |
| dependency | [Exact retained dependency](../audits/literature/Den09/Yin_U002.md#den09-u002) | Only the retained Theorem14/Example15 for arbitrary integer specialization vectors, sup-norm relation parameter and full polynomial Mahler limit including zeros; its original proof is not audited and no effective rate or invertible-only substitute is supplied. |
| support | [Exact retained support](Yin_C_G0271_v1.md#essential-family-mahler-limit) | The exact sequence-contradiction method for uniformity in an all-vector Lawton limit. The present q/F/G/integrability/certificate proof is local, with no reuse of the different essential-family constant or effective cutoff. |
| review | [Complete actual current whole self finding](../audits/reviews/Yin_R_G0626_v1.md#current-trinomial-limit-whole-finding) | Entire original D44 Sections1--5/formulas(1)--(17): all primitive 0<b<a/gcd(a,b)=1 trinomials without irreducibility, complete original-degree doubling auxiliary/all factors/leading coefficients, exact fixed F/H/G specialization and q=max(b,a-b)>=a/2, accepted full qualitative Lawton including zeros and all-offset uniformity without a rate, full two-variable phase identity and log-integrability, rotated reciprocal quartic/trace-root/Jensen/hyperbolic calculation including all endpoint cases, exact two-angle/concavity/integer certificate Delta_infinity>1/250, eventual Delta>1/500 and finite possible exceptions with no effective degree cutoff, no all-degree sign/near-one/gap or selected-factor transfer. Actual current whole relationship is self-reviewed; original unknown whole and explicitly recorded author self-check scopes remain separate. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:20 |
| status | proved |
| reason | Adopt the actual new isolated whole finding after complete reading of the exact proof and original whole/all-input/source/negative scopes. Preserve original UNKNOWN/SELF, real dates and all finite/accepted-external limitations; no original finding retirement or Task/E completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original D44 Sections1--5/formulas(1)--(17): all primitive 0<b<a/gcd(a,b)=1 trinomials without irreducibility, complete original-degree doubling auxiliary/all factors/leading coefficients, exact fixed F/H/G specialization and q=max(b,a-b)>=a/2, accepted full qualitative Lawton including zeros and all-offset uniformity without a rate, full two-variable phase identity and log-integrability, rotated reciprocal quartic/trace-root/Jensen/hyperbolic calculation including all endpoint cases, exact two-angle/concavity/integer certificate Delta_infinity>1/250, eventual Delta>1/500 and finite possible exceptions with no effective degree cutoff, no all-degree sign/near-one/gap or selected-factor transfer. |
| argument | [Complete selected argument](#argument) | Entire original D44 Sections1--5/formulas(1)--(17): all primitive 0<b<a/gcd(a,b)=1 trinomials without irreducibility, complete original-degree doubling auxiliary/all factors/leading coefficients, exact fixed F/H/G specialization and q=max(b,a-b)>=a/2, accepted full qualitative Lawton including zeros and all-offset uniformity without a rate, full two-variable phase identity and log-integrability, rotated reciprocal quartic/trace-root/Jensen/hyperbolic calculation including all endpoint cases, exact two-angle/concavity/integer certificate Delta_infinity>1/250, eventual Delta>1/500 and finite possible exceptions with no effective degree cutoff, no all-degree sign/near-one/gap or selected-factor transfer. |
| dependency | [Exact accepted input](Yin_C_G0412_v1.md#sparse-trinomial-auxiliary) | Only exact original-degree F/H/G expansion, seed-Phi6/nonmonic exceptions and full untruncated phase normalization, retaining all factors and leading coefficients. The earlier45 discovery decimals are unused. |
| dependency | [Exact accepted input](../audits/literature/Den09/Yin_U002.md#den09-u002) | Only the retained Theorem14/Example15 for arbitrary integer specialization vectors, sup-norm relation parameter and full polynomial Mahler limit including zeros; its original proof is not audited and no effective rate or invertible-only substitute is supplied. |
| support | [Exact support](Yin_C_G0271_v1.md#essential-family-mahler-limit) | The exact sequence-contradiction method for uniformity in an all-vector Lawton limit. The present q/F/G/integrability/certificate proof is local, with no reuse of the different essential-family constant or effective cutoff. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0647_v1.md#isolated-trinomial-limit-whole-finding) | Entire exact current Statement and Argument and corresponding original complete whole scope, all source/input/negative/finite-evidence boundaries and original author-check distinctions. |

## Complete retained argument

<a id="argument"></a>
<a id="retained-trinomial-limit-argument"></a>

<a id="trinomial-eventual-positive-balance"></a>
### 1. Exact statement and retained source boundary

For integers 0<b<a with gcd(a,b)=1, put

    f_(a,b)(t)=t^a-t^b-1,
    f*_(a,b)(t)=t^a f_(a,b)(1/t),
    G_(a,b)(t)=[(f*_(a,b))^2 f_(a,b)(t^2)
                         +f_(a,b)^2 f*_(a,b)(t^2)]/2,
    Delta_(a,b)=log2+m(G_(a,b))-3m(f_(a,b)).             (1)

Every m here is the full logarithmic Mahler measure, including leading coefficients and all factors.
The seed is not assumed irreducible.
C412 proves G_(a,b)(1)=-1, its exact monomial normalization and the exceptional nonmonic residual at(2,1).
No factor is removed in(1).

There exists a real constant Delta_infinity such that

    Delta_(a,b) -> Delta_infinity uniformly over gcd(a,b)=1,
                  0<b<a, as a -> infinity,
    Delta_infinity > 1/250.                            (2)

Consequently there is an integer A_0 such that

    Delta_(a,b)>1/500 for every a>=A_0,
                   0<b<a and gcd(a,b)=1.              (3)

In particular there are only finitely many pairs in this class with Delta_(a,b)<=0, or even with Delta_(a,b)<=1/500.
This proves neither that this finite exceptional set is empty nor an effective upper bound on its degrees.

The sole non-elementary input is the previously accepted full Lawton specialization statement: for a fixed nonzero Laurent polynomial P in two variables,

    M(P(t^r,t^s)) -> M(P)
    as q(r,s)=min{max(|i|,|j|): (i,j) != (0,0), ir+js=0}
       -> infinity.                                  (4)

Den09-U002 retains this full theorem, including its treatment of zeros, as an external statement; the original Lawton proof was not audited there or here.
The invertible-only determinant approximation elsewhere in that unit would not suffice.
C271 already retains this exact all-vector limit to obtain uniformity over offsets; that method is reused, with the following polynomials and a new direct limiting-integral estimate.
No rate is available from the input used here.

<a id="trinomial-universal-mahler-limit"></a>
### 2. One fixed two-variable polynomial controls every offset

Define

    F(u,v)=uv-u-1,             H(u,v)=1-v-uv,
    G(u,v)=[H(u,v)^2 F(u^2,v^2)+F(u,v)^2 H(u^2,v^2)]/2.

The exact integer expansion retained in C412 is

    G=u^4 v^3-u^4 v^2+u^3 v^4-2u^3 v^2+u^3 v
                         -u^2 v^2+u v^3-2u v^2+u-v^2+v. (5)

Substitution at (u,v)=(t^b,t^(a-b)) gives precisely f_(a,b), f*_(a,b), and G_(a,b).
Both specializations are nonzero for all these inputs.
Since gcd(b,a-b)=1, every integral relation with (b,a-b) is an integer multiple of (a-b,-b).
Therefore

    q(b,a-b)=max(b,a-b)>=a/2.                          (6)

Applying(4) separately to the two fixed polynomials F and G, and taking logarithms of their positive Mahler measures, gives(2)'s convergence with

    Delta_infinity=log2+m(G)-3m(F).                    (7)

It is uniform over the stated offsets: otherwise a sequence of exceptions with a tending to infinity would, by(6), contradict the all-vector limit in(4).
No assumption on convergence of b/a is required.
The following explicit integrals in particular verify positivity and finiteness of M(F),M(G).

On the two-dimensional unit torus, H=uv conjugate(F), so R=H/F has modulus one almost everywhere.
The same exact factorization as in C412 gives, almost everywhere,

    G=[F(u,v)^2 F(u^2,v^2)/2]
                         [R(u,v)^2+R(u^2,v^2)].

The integrability justified below and invariance of torus Haar measure under coordinatewise squaring show that(7) is also the full two-variable phase integral

    Delta_infinity=integral_(T^2)
                    log|R(u,v)^2+R(u^2,v^2)| dmu.     (8)

Thus the limit concerns the complete balance, including all signed phase contributions.
It is not a sum of limits of selected Fourier modes.

<a id="trinomial-quartic-section-integral"></a>
### 3. A rotated reciprocal quartic and its exact Jensen integral

Write u=exp(2i theta), with0<=theta<=pi, and set v=exp(i(phi-theta)).
For fixed theta this is only a rotation of the v circle and preserves its normalized measure.
The divisor u^2 v^2 has unit modulus, and dividing(5) by it gives the real expression

    G/(u^2 v^2)=2cos(2phi)+4cos(3theta)cos(phi)
                           -2cos(4theta)-4cos(2theta)-1. (9)

Put c=cos(theta), A=cos(3theta)=4c^3-3c and D=4c^2-1.
With z=exp(i phi) and x=z+z^(-1), the right side of(9) is

    x^2+2A x-D^2.

Indeed -2cos(4theta)-4cos(2theta)-3=-(4c^2-1)^2.
Its two real trace roots are

    xi_+=-A+sqrt(A^2+D^2),
    xi_-=-A-sqrt(A^2+D^2),
    A^2+D^2=1+c^2(4c^2-1)^2>0.                       (10)

After multiplication by z^2, the section is the monic reciprocal quartic

    (z^2-xi_+ z+1)(z^2-xi_- z+1).

For a real x the logarithmic Mahler measure of z^2-xz+1 is

    J(x)=0 if |x|<=2, and J(x)=arcosh(|x|/2) if |x|>2.

This follows directly from the two roots with product one, including the double-root endpoints.
Hence the inner v integral is I(theta)=J(xi_+)+J(xi_-), which is nonnegative.
Evaluating the trace quadratic at +/-2 gives

    4+4A-D^2=(2c-1)^2(3-4c^2),
    4-4A-D^2=(2c+1)^2(3-4c^2).                        (11)

Since xi_+>=0 and xi_-<=0, both roots lie in[-2,2] when |c|<=sqrt(3)/2.
Equality at c=+/-1/2 merely gives an endpoint trace root and still zero inner measure.
When |c|>sqrt(3)/2, both roots have modulus greater than2.
Replacing c by -c exchanges xi_+ and -xi_-, so I(theta) is unchanged by theta -> pi-theta.

For0<=theta<pi/6, D>2.
The product xi_+(-xi_-) is D^2, while(11) gives

    sqrt((xi_+^2-4)(xi_-^2-4))=D(D-2).

The addition formula for hyperbolic cosine therefore implies

    cosh(I(theta))=[D^2+D(D-2)]/4=D(D-1)/2,
    I(theta)=arcosh((4cos^2(theta)-1)(2cos^2(theta)-1)). (12)

Both sides are nonnegative, so inversion by arcosh is legitimate.
The formula extends continuously to theta=pi/6 with value zero.
It follows that

    m(G)=(2/pi) integral_0^(pi/6)
             arcosh((4cos^2(theta)-1)(2cos^2(theta)-1)) dtheta.
                                                               (13)

No unproved interchange across torus zeros is used.
On T^2 one has |G|<=13 from(5), so its positive logarithmic part is bounded.
For each fixed theta the monic quartic's Jensen integral is I(theta)>=0, hence the inner negative logarithmic integral is at most its positive logarithmic integral, which is at most log13.
Tonelli bounds the full negative part as well.
This proves integrability of log|G| and justifies Fubini and(13).

For F, Jensen in v gives max(0,log|1+u|).
The same positive/negative-part argument, using |F|<=3 and its nonnegative inner integral, proves integrability.
Thus

    m(F)=(2/pi) integral_0^(pi/3) log(2cos(theta)) dtheta. (14)

These facts also justify the integrable identity(8): its last logarithm is the difference of the three integrable polynomial logarithms in the preceding exact factorization, away from their null zero sets.
Coordinatewise squaring preserves normalized Haar measure, so the factor F(u^2,v^2) has the same integral as F.

<a id="positive-trinomial-limit-certificate"></a>
### 4. Two elementary integral estimates give a positive rational margin

The integrand in(13) is decreasing on[0,pi/6], since D decreases from3 to2 and D(D-1)/2 is increasing as a function of D on that range.
At the two exact angles,

    cosh(I(pi/12))=(3+sqrt3)/2 > 17/8=cosh(log4),
    cosh(I(pi/8))=1+sqrt2/2 > 5/3=cosh(log3).

The strict inequalities use only sqrt3>5/4 and sqrt2>4/3.
Integrating the corresponding constant lower bounds on[0,pi/12] and[pi/12,pi/8], and using nonnegativity on the rest, gives

    m(G)>(log4)/6+(log3)/12=log48/12.                 (15)

For the seed, log(2cos(theta)) is concave on[0,pi/3].
Apply its midpoint Jensen bound separately on[0,pi/6] and[pi/6,pi/3].
Since

    (2cos(pi/12))(2cos(pi/4))=1+sqrt3,

equation(14) yields

    3m(F)<=log(1+sqrt3)<log(11/4),                    (16)

where sqrt3<7/4 follows by squaring.
Consequently

    Delta_infinity>log(8/11)+log48/12
                  =(1/12)log(48*8^12/11^12)>1/250.   (17)

Here the last strict inequality has an elementary integer certificate.
Put

    U=48*8^12=3298534883328,
    V=11^12=3138428376721.

For U>V>0, log(U/V)>(U-V)/U.
Moreover

    250(U-V)=40026626651750
        >12U=39582418599936.

Combining these two comparisons proves the last step of(17).
The displayed integer arithmetic was directly checked with exact integers; no numerical quadrature, algebraic-root approximation or Mahler scan is needed.

Choose the error in the uniform convergence(2) to be less than1/500.
Equations(2) and(17) then imply(3).
Finitely many integer a lie below A_0 and each admits finitely many b, proving the stated finiteness of small or nonpositive balances.

### 5. What this changes, and what it leaves open

The exact limiting discriminator is positive.
Consequently an attempted negative family obtained only by sending coprime trinomial exponents to infinity cannot work, regardless of their ratio or oscillation.
The seed-Phi_6 cases from C412 are included: cyclotomic reduction preserves Delta, and their original coprime exponent vectors still satisfy(6).
No universal sign theorem follows for the remaining finite, presently unbounded range of degrees, and the existing45 numerical positives do not close it.
The next useful step is an effective specialization-error bound strong enough to give a concrete finite cutoff, or a direct inequality covering those finite-degree possibilities without such a cutoff.
A blind larger parameter scan is not justified by the present non-effective reduction.

This also does not construct low-measure negative balances in a broader seed class.
The current theorem is specific to the three occupied coefficients and coprime exponents.
The separately retained negative cubic controls have growing height/measure and do not contradict it; the coordinator's broader height-one cancellation experiment is not covered.
The two-variable limit and eventual positivity are useful structure for this precise class, not a near-one Mahler gap, a new Salem-family construction, or a uniform arithmetic-income theorem for G0001.

## Original scope and checking boundary

The original author check, separate whole finding, source inspection, day precision and pending/fixed-retention dispositions remain at their exact L179/R78 homes.
The valid full Lawton input remains a dependency here; no original source proof or quantitative specialization estimate is added.
The separate height-one negative proof has its own effective elementary averaging and original native certificate, and does not contradict this primitive three-term limit.
No current whole finding may replace this complete proof by the old PASS or by selected positive modes.
