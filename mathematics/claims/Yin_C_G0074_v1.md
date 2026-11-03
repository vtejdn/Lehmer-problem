---
author: Yin
---
# Multiplicity and dimension prices for legal finite rational-delay words

Date: 2026-10-12T14:03.
Human author Yin.
Root authored the entire original D29 and writes this extraction.
Independent whole R297 supports the actual21:48 original body only; the new statement/wrapper needs a separate actual extraction review.
No adoption or draft retirement occurs at registration.
The entire original history and proof follow.

## Statement

Fix the ACTUAL monic irreducible minimal polynomial P of a nontorsion algebraic integer unit alpha, ORIGINAL degree d>=2, K=Q(alpha), O0=Z[alpha], nu=Norm_K(alpha) in{+1,-1}, and total m=m(P)>0.
All norms retain all d original embeddings.
Star on real rational Laurent polynomials means t maps to t^-1.
All constructed packets retain N indexed labels at weights1/N, so FINAL M=N and energy E1.

Use c=log2/4,h0=c exp(-20), b(u)=max{u,sqrt(u/c)log(sqrt(c/u))} and epsilon(u)=min{1,15sqrt(b(u))+4u} on0<u<=h0, with their accepted source limits.
Put K0=c/[2*36^8*5^64] and eta_R=K0 R^(-64) for integers R>=1.
Then eta_R<h0/2 and

    exp(2eta_R)[4/5+8R epsilon(eta_R)+32R eta_R]<1,
    (5R)^8[epsilon(2eta_R)+12eta_R]<1.

**A. Local repeated-monomial theorem.**
Let f_i=epsilon_i t^(a_i), epsilon_i in{+1,-1}, with arbitrary integer exponents, repetitions allowed, span A and maximum exponent multiplicity R.
For primitive nonzero v in Z^N, s=sum v_i^2, Pi=vv^T/s and ANY nonzero integer k of either sign set

    U=I-Pi+t^k Pi, V=sum_i v_i epsilon_i t^(a_i),
    H=(t^k-1)V, g_i=f_i+v_i H/s, B=A+abs(k), u=B*m/d.

The clean output has exact covariance sum_i g_i g_i*=N, actual denominator q dividing s and common width T_g<=B.
All actual values are in O0 iff H(alpha)/s is in O0; nonvanishing is separate.
If V(alpha)!=0 and this gate holds, the full nonzero norm floor implies at0<u<=h0

    1<=exp(2u)[4R/s+(8R-4R/s)epsilon(u)+32R*u].

The proof retains possibly nonprimitive H, with ||H||_2^2<=4Rs and rho=||H||_1^2/||H||_2^2<=2s.
If every g_i(alpha) is nonzero in O0 and u<=eta_R, all output values are signed powers of alpha: s1 is a coordinate shift; s>=5R forces V(alpha)=0 and every value is unchanged; at2<=s<5R every CLEAN output polynomial is itself a signed monomial by C71 with q<=s.
Each changing branch has new exponent multiplicity at most6R and span at most B; the unchanged branch preserves R.
No equality q=s is assumed.

**B. Finite legal-word theorem.**
Starting with the clean signed-monomial vector F^(0) of span A0 and multiplicity R0, form TRUE Laurent vectors F^(j)=U_j F^(j-1) for1<=j<=L, L>=1, using such primitive directions and nonzero integer delays in fixed dimension N.
Require every coordinate at every stage0,...,L to be a NONZERO element of the SAME O0.
Charge B_word=A0+sum_j abs(k_j), U_word=B_word*m/d.
If

    U_word<=eta_(min{N,6^L R0}),

every intermediate ACTUAL value is a signed power of alpha and final full norm income Lambda and E1 surplus are ZERO.
Separately U_word<=eta_N suffices for ANY finite L, and U_word<=eta_(6^L R0) suffices independent of N.
Clean representatives have the same actual evaluation as true vectors and their OWN newly established E1 covariance; they do not replace polynomials inside an old covariance identity.

**C. Necessary dimension and length prices.**
Every legal word of B with positive final income satisfies BOTH

    U_word>K0 N^(-64), U_word>K0(6^L R0)^(-64),
    N>(K0/U_word)^(1/64),
    L>log[K0/(U_word R0^64)]/[64 log6].

The last bound is informative only when its right side is positive.
On ANY HYPOTHETICAL sequence of actual m_j->0 with positive income and B_word,j<=C d_j, fixed C>0, necessarily N_j>(K0/(C m_j))^(1/64)->infinity.
If R0,j<=Rbar is also fixed, L_j>log[K0/(C m_j Rbar^64)]/[64 log6]->infinity.
No existence, optimality or sufficient construction is asserted.
Positive income requires a first departure from signed powers, but such a departure can still be to a different norm-one unit.

**D. TRUE costs and limitations.**
After ONE common polynomial normalization, let q_L be the TRUE final packet's actual denominator, T_final its actual common union width, D_i its full signed coordinate norms and B_i=q_L F_i^(L).
Then

    q_L divides product_j s_j, T_final<=B_word, FINAL M=N,
    Res(P,B_i)=q_L^d D_i,
    product_i Res(P,B_i)=q_L^(dN) product_i D_i,
    (1/N)sum_i||B_i||_2^2=q_L^2,
    Lambda=(1/(dN))sum_i log abs(D_i),
    I_int=log q_L+Lambda, surplus=Lambda<=T_final*m/d.

A common shift t^b contributes nu^b per norm and nu^(bN) to the copied product.
Under B's threshold the actual product is (product_i(epsilon_i')^d)nu^(sum_i a_i'), giving Lambda0 even if true representatives/q_L are complicated.
Neither denominator equality nor norm-product invariance from det U_j is asserted.

The theorem charges CUMULATIVE absolute delays, potentially much larger than final width.
Intermediate legality, fixed dimension, equal indexed weights, rank-one delay factors and a signed-monomial seed are essential.
Constant rational orthogonal rotations, higher-rank factors without a legal rank-one decomposition, changing metrics/dimension, nonmonomial seeds, nonintegral or zero intermediate values, and a short final window with large cumulative expense remain outside.
Repeated exponents and either sign of individual delay ARE covered.
The unrestricted G0001 gap remains unresolved.

## Current assessment
[Selected decision](#decision-independent-current-whole-review-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T14:03 |
| status | open |
| reason | Register the repeated-exponent/either-sign local obstruction, explicit legal finite-word threshold, necessary coordinate/length prices and true signed costs. Entire original D29 retained. Whole R297 covers the actual original only; new actual extraction review remains required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, original domain, strict thresholds, local/word quantifiers, true costs and exclusions. |
| argument | [Entire original body](#argument) | ENTIRE21:48 D29 candidate/reuse/history, Sections1--5/equations1--17 and freeze. |
| dependency | [C71 E1 selector](Yin_C_G0071_v1.md#statement) | Adopted all-weight E1 q^8 implication and signed-monomial alternative, applied to each independently constructed clean packet. |
| dependency | [Original coefficient estimate](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) | Full original nonzero norm, nonprimitive coefficients and exact S/rho/width/radial costs. |
| dependency | [Accepted angular modulus](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Exact c,h0,b,epsilon and monotonicity, with inherited source limits. |
| dependency | [Old rank-one mechanism](Yin_C_G0053_v1.md#statement) | Credited projection algebra and primitive particular-vector actual-order gate. |
| dependency | [Final actual covariance expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Direct generic full-original-root bound at true final width and weights, not reciprocal lifting existence. |
| support | [Old word criterion](../ledger/Yin_L_G0380_v1.md#finite-word-exact-interpolation-criterion) | Reuse boundary: rational factorization supplies neither intermediate legality nor short cumulative expense. |
| support | [Single positive-delay antecedent](Yin_C_G0072_v1.md#statement) | Motivation only, no pending premise; historical status in original body remains intact. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0297_v1.md#legal-delay-word-whole-independent-finding) | Entire actual21:48 proof only; no prospective wrapper review. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T14:11 |
| status | proved |
| reason | Adopt original whole R297 and separately inspected actual extraction R399. Fix the repeated-seed/either-sign local price, explicit legal finite-word threshold, both strict coordinate/length prices and true signed costs at their stated scope. Root is a proof/wrapper contributor, not either independent reviewer. Cumulative expense and every intermediate nonzero original-order value remain essential; unrestricted G0001 is unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, original domain, strict thresholds, local/word quantifiers, true costs and exclusions. |
| argument | [Entire original body](#argument) | ENTIRE21:48 D29 candidate/reuse/history, Sections1--5/equations1--17 and freeze. |
| dependency | [C71 E1 selector](Yin_C_G0071_v1.md#statement) | Adopted all-weight E1 q^8 implication and signed-monomial alternative, applied to each independently constructed clean packet. |
| dependency | [Original coefficient estimate](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) | Full original nonzero norm, nonprimitive coefficients and exact S/rho/width/radial costs. |
| dependency | [Accepted angular modulus](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Exact c,h0,b,epsilon and monotonicity, with inherited source limits. |
| dependency | [Old rank-one mechanism](Yin_C_G0053_v1.md#statement) | Credited projection algebra and primitive particular-vector actual-order gate. |
| dependency | [Final actual covariance expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Direct generic full-original-root bound at true final width and weights, not reciprocal lifting existence. |
| support | [Old word criterion](../ledger/Yin_L_G0380_v1.md#finite-word-exact-interpolation-criterion) | Reuse boundary: rational factorization supplies neither intermediate legality nor short cumulative expense. |
| support | [Single positive-delay antecedent](Yin_C_G0072_v1.md#statement) | Motivation only, no pending premise; historical status in original body remains intact. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0297_v1.md#legal-delay-word-whole-independent-finding) | Entire actual21:48 proof only; no prospective wrapper review. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0794_v2.md#c74-legal-delay-word-actual-extraction-finding) | ENTIRE actual A--D and retained original, all exact direct interfaces and preservation independently checked after registration; original R297 remains original-whole scope. |


### Decision sufficient-rational-delay-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:12 |
| status | proved |
| reason | Use the complete sufficient accepted home of the same exact prior rational factor/orbit/fixed-vector pole interface. Preserve the original domain and scope, all other tuples/fields, current review, old decisions and actual historical reading inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, original domain, strict thresholds, local/word quantifiers, true costs and exclusions. |
| argument | [Exact argument](#argument) | ENTIRE21:48 D29 candidate/reuse/history, Sections1--5/equations1--17 and freeze. |
| dependency | [Exact dependency](Yin_C_G0071_v1.md#statement) | Adopted all-weight E1 q^8 implication and signed-monomial alternative, applied to each independently constructed clean packet. |
| dependency | [Exact dependency](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Full original nonzero norm, nonprimitive coefficients and exact S/rho/width/radial costs. |
| dependency | [Exact dependency](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact c,h0,b,epsilon and monotonicity, with inherited source limits. |
| dependency | [Exact dependency](Yin_C_G0053_v1.md#statement) | Credited projection algebra and primitive particular-vector actual-order gate. |
| dependency | [Exact dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Direct generic full-original-root bound at true final width and weights, not reciprocal lifting existence. |
| support | [Exact support](Yin_C_G0441_v1.md#finite-word-exact-interpolation-criterion) | Reuse boundary: rational factorization supplies neither intermediate legality nor short cumulative expense. |
| support | [Exact support](Yin_C_G0072_v1.md#statement) | Motivation only, no pending premise; historical status in original body remains intact. |
| support | [Exact support](../audits/reviews/Yin_R_G0297_v1.md#legal-delay-word-whole-independent-finding) | Entire actual21:48 proof only; no prospective wrapper review. |
| review | [Exact review](../audits/reviews/Yin_R_G0794_v2.md#c74-legal-delay-word-actual-extraction-finding) | ENTIRE actual A--D and retained original, all exact direct interfaces and preservation independently checked after registration; original R297 remains original-whole scope. |


### Decision independent-current-whole-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:10 |
| status | proved |
| reason | Adopt the separately organized current fixed-target finding after complete statement and retained-argument inspection, including late extensions, actual costs, controls, necessary mathematical interfaces and source limits, while excluding credited comparison scopes first separately checked after old-review exposure. The initial mathematical conclusion was formed at 2026-10-22T22:46 UTC before old-target review comparison. The finding records the exact interface and later credited-comparison reading sequence. Preserve fixed mathematics, historical decisions, all non-review premises and their scopes; retain known sufficient independent findings in their original homes and original unknown findings at their actual checking scope. This selects current review evidence and supplies no new research, Task completion or execution resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement: statement](#statement) | Entire A--D, original domain, strict thresholds, local/word quantifiers, true costs and exclusions. |
| argument | [Argument: argument](#argument) | ENTIRE21:48 D29 candidate/reuse/history, Sections1--5/equations1--17 and freeze. |
| dependency | [Dependency: statement](Yin_C_G0071_v1.md#statement) | Adopted all-weight E1 q^8 implication and signed-monomial alternative, applied to each independently constructed clean packet. |
| dependency | [Dependency: actual-resultant-coefficient-energy-bound](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Full original nonzero norm, nonprimitive coefficients and exact S/rho/width/radial costs. |
| dependency | [Dependency: uniform-powered-angular-coherence](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact c,h0,b,epsilon and monotonicity, with inherited source limits. |
| dependency | [Dependency: statement](Yin_C_G0053_v1.md#statement) | Credited projection algebra and primitive particular-vector actual-order gate. |
| dependency | [Dependency: direct-exact-covariance-window-inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Direct generic full-original-root bound at true final width and weights, not reciprocal lifting existence. |
| support | [Support: finite-word-exact-interpolation-criterion](Yin_C_G0441_v1.md#finite-word-exact-interpolation-criterion) | Reuse boundary: rational factorization supplies neither intermediate legality nor short cumulative expense. |
| support | [Support: statement](Yin_C_G0072_v1.md#statement) | Motivation only, no pending premise; historical status in original body remains intact. |
| support | [Support: legal-delay-word-whole-independent-finding](../audits/reviews/Yin_R_G0297_v1.md#legal-delay-word-whole-independent-finding) | Entire actual21:48 proof only; no prospective wrapper review. |
| review | [Current isolated finding](../audits/reviews/Yin_R_G0794_v2.md#g74-current-independent) | Complete current mathematical statement and retained proof, including all late extensions, paid arithmetic, useful controls and accepted necessary interfaces at their exact scopes; exclude post-initial credited comparison scopes identified by the finding; initial conclusion 2026-10-22T22:46 UTC, then old-finding comparison; actual interface and credited-comparison reading limits are disclosed in the finding. |

## Registration and complete preservation

The [original D29 freeze](#legal-delay-word-entire-author-freeze) is the complete preservation target.
Its ENTIRE body follows, with duplicate front matter represented once, first title demoted one level, and line endings/terminal separating blank space normalized.
Every original argument, candidate, role, source and limitation remains.
Original relative claim/ledger links remain valid.
Historical C72 pending wording belongs to the21:41 allocation: C72 has since been independently extracted/adopted, and remains motivation-only.
Root is a proof/wrapper contributor and cannot independently review it.
A first attempted normal registration was safely refused because Current assessment incorrectly used a table; this corrected attempt uses the required explicit selected-decision link and preserves the actual mathematics.

## Argument

## Multiplicity prices for legal finite words of rational rank-one delays

Date: 2026-10-12T13:41.
Human author Yin.
New root AUTHOR inquiry under the continuing G0001 instruction.
Root selects and develops the proposed repeated-monomial and finite-word argument; a different noncontributor must independently review any result.
No native mathematical program, new source acquisition or execution allowance is proposed.
This is not a Claim adoption.

## Responsible question and bounded reuse

[C53](Yin_C_G0053_v1.md#statement) supplies the rational rank-one projection and exact particular-vector integrality mechanism.
The actual [C71 adopted all-weight E1 selector](Yin_C_G0071_v1.md#statement) supplies a necessary coefficient-denominator bound with no count or positive-weight lower bound.
[L229](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) supplies the complete primitive-or-nonprimitive original resultant coefficient norm estimate, at its explicit small total parameter.
[C72](Yin_C_G0072_v1.md#statement) currently registers, but has not yet adopted, the independently whole-reviewed distinct-monomial SINGLE positive-delay obstruction.
Its mechanism motivates this continuation; its pending extraction status is retained, and the new argument can use C71/L229/C53 directly.

A bounded G Claim/ledger search for intermediate monomials, repeated seed exponents, rank-one words and composite monomial mechanisms found C53, C65's universal-entry matrix theorem, C72's explicit exclusion of repeated seeds/negative delays/composites, and [L380's rational factorization and exact word criterion](../ledger/Yin_L_G0380_v1.md#finite-word-exact-interpolation-criterion).
The actual L380 Sections2--4 were read.
Its weighted rational factorization allows inverse factors and rational constant rotations but does NOT ensure actual intermediate integrality or bound the required word.
That different scope cannot supply the proposed legal-word restriction.
No matching multiplicity-controlled legal-word theorem was found in this bounded screen; no literature-wide novelty is asserted.
The accepted local interfaces suffice for the proposed direct algebra, with no new named theorem needed.

<a id="legal-delay-word-responsible-candidate"></a>
## Candidate before substantial proof

For ONE actual nontorsion integer unit, start with finitely many signed monomial values epsilon_i*alpha^(a_i), allowing repeated integer exponents.
Bound the maximum multiplicity of any exponent by an integer R>=1.
For a primitive integer direction v, s=sum v_i^2, and NONZERO integer delay k of EITHER sign, set V=sum v_i*epsilon_i*t^(a_i) and H=(t^k-1)V.
The proposed local energy bound is ||H||_2^2<=4Rs and effective support<=2s, whether or not V is primitive or zero as a polynomial.
The nonzero actual residual H(alpha)/s, when integral, should force an R-dependent positive Tm/d threshold uniformly for s>=5R.
For the remaining bounded s, apply actual C71 to the clean E1 output, requiring only actual q<=s rather than the false repeated-seed equality q=s.

The intended new question is whether ANY finite sequence of these factors, with all intermediate outputs nonzero actual O0 integers, can first leave the signed-monomial value class at small cumulative exponent expense while the preceding monomial state's exponent multiplicity remains bounded.
Cumulative span plus sum of absolute delays is a genuine extra budget; it must NOT be replaced by the potentially smaller final matrix/packet width after cancellations.
Original intermediate coefficient representatives may cease to be monomials even while their values remain monomial units; any clean-representative induction needs an explicit field-evaluation justification and full signed norm accounting.
Positive final surplus, unbounded multiplicity and merely final-integral words must remain carefully distinguished.

No result is asserted at allocation.
The entire proof, failures, cost conditions, source roles and exact finite-word quantifiers will be developed here before review.
No matrix or word enumeration is authorized or required by this candidate.


<a id="multiplicity-delay-explicit-threshold"></a>
## 1. Exact input, multiplicity and an explicit threshold

Fix an ACTUAL monic irreducible nontorsion integer-unit minimal polynomial P, ORIGINAL degree d>=2, alpha a root, K=Q(alpha), O0=Z[alpha], nu=Norm_K(alpha) in{+1,-1}, and total m=m(P)>0.
All norms retain the d original embeddings.
Fix N>=1 and a vector of actual SIGNED monomial values

    u_i=epsilon_i alpha^(a_i), epsilon_i in{+1,-1}, a_i in Z,
    R=max_a #{i:a_i=a}, A=max_i a_i-min_i a_i.                 (1)

The representation of each such value is UNIQUE: equality of two signed powers would give alpha^(a-b)=+/-1; nontorsion implies a=b and the same sign.
Thus the exponent multiplicity R is intrinsic to this signed-monomial value vector, not a favorable choice of representation.
Opposite signs at the same exponent still count separately.
Initially use the clean Laurent representatives f_i=epsilon_i t^(a_i), all indexed weights1/N, so E1 and FINAL M=N.

Retain c=log2/4,h0=c exp(-20), b and epsilon from the adopted C71/L229 interface.
For every integer R>=1 put

    K0=c/[2*36^8*5^64],
    eta_R=K0 R^(-64)=(c/2)[36(5R)^8]^(-8)>0.                (2)

Here K0 is a numerical constant, not the number field K.
These explicit constants satisfy

    eta_R<h0/2,
    exp(2eta_R)[4/5+8R epsilon(eta_R)+32R eta_R]<1,
    (5R)^8[epsilon(2eta_R)+12eta_R]<1.                       (3)

To verify these numerical margins directly, set y=u/c in(0,1].
The elementary maximum of x exp(-x/4) on x>=0 is4/e<2.
Hence (1/2)sqrt(y)log(1/y)<=y^(1/4), while cy<=y^(1/4).
Therefore b(u)<=y^(1/4) and

    epsilon(u)<=16(u/c)^(1/8), 0<u<=h0,                    (4)

because4c=log2<1.
This is only a convenient upper estimate for the EXISTING epsilon, not a new angular theorem.
Let D=36(5R)^8.
Since36^8>e^20 (use e<3 and2^16>3^4), eta_R<h0/2.
Also eta_R<1/20.
With z=(eta_R/c)^(1/8)=2^(-1/8)/D one has Rz<1/(36*5^8)<1/2000.
Consequently

    4/5+8R epsilon(eta_R)+32R eta_R
       <=4/5+136Rz<217/250,
    exp(2eta_R)<10/9,

where eta_R=c z^8<=c z and c<1/4 were used.
Their product is less than217/225<1.
Finally epsilon(2eta_R)+12eta_R<=18/D, so the last quantity in(3) is at most1/2.
The bound exp(x)<=1/(1-x) for0<=x<1 follows termwise from its nonnegative series.
Every strict margin in(3) is thereby established without a numerical experiment.

<a id="repeated-monomial-one-step-price"></a>
## 2. One step: repeated exponents and either delay sign

Let v in Z^N be nonzero and primitive, s=sum_i v_i^2, Pi=vv^T/s, and let k be ANY NONZERO integer.
Define

    U(t)=I-Pi+t^k Pi,
    V(t)=sum_i v_i epsilon_i t^(a_i),
    H(t)=(t^k-1)V(t),
    g_i(t)=epsilon_i t^(a_i)+v_i H(t)/s,
    B=A+|k|, u=B*m/d.                                     (5)

The parameter B is a SUPPLIED support expense, not necessarily actual width.
Laurent covariance is exactly sum_i g_i g_i*=N, so the clean outputs at weights1/N have E1.
Their actual common coefficient denominator q divides s; no equality q=s is asserted with repeated seed exponents.
Their actual common width T_g is at most B after one common shift.
Individual output nonvanishing is a separate requirement.

As in the primitive-vector Bezout argument of C53, every g_i(alpha) is in O0 if and only if H(alpha)/s is in O0.
This remains exact for repeated exponents, negative k, composite s, and zero H.
It is a field/order condition, not divisibility at a selected root or only at a squarefree reduction.

If V(alpha)!=0, then H(alpha)!=0 by nontorsion.
Under that integrality gate, z=H(alpha)/s is a NONZERO actual integer, so the full original norm floor is |Norm H(alpha)|>=s^d.
A common monomial makes H an integer polynomial and preserves this absolute floor, with its signed nu-power retained.

For the collected coefficients of V, Cauchy--Schwarz at each repeated exponent gives

    ||V||_2^2=sum_a (sum_(i:a_i=a) epsilon_i v_i)^2
                    <= R sum_i v_i^2=Rs.

The support of H has at most2r_v entries before collection, where r_v=#{i:v_i!=0}<=s.
Thus when H is nonzero as a polynomial,

    S=||H||_2^2<=4Rs,
    rho=||H||_1^2/S<=2r_v<=2s.                            (6)

Neither V nor H need be primitive; V can even be identically zero.
The nonzero-residual branch excludes that case before any logarithm or rho is taken.
For nonzero V, its product with t^k-1 has positive actual width w=width(V)+|k|<=B, because extreme product coefficients cannot cancel.
These statements handle both signs of k.

Apply the ACTUAL accepted L229 coefficient-energy bound at true w*m/d<=u.
When0<u<=h0, the norm floor and(6) imply

    1<=exp(2u)[4R/s+(8R-4R/s)epsilon(u)+32R*u].             (7)

Indeed log s<=log(sqrt(S))+u+(1/2)log[1+(rho-1)epsilon(u)+4rho*u]; exponentiating and substituting(6) gives(7).
All ORIGINAL norms and every numerator scalar are present even when content is nontrivial.
In particular when s>=5R and V(alpha)!=0,

    1<=exp(2u)[4/5+8R epsilon(u)+32R*u].                   (8)

By(3), this is impossible at u<=eta_R.
This is the repeated-seed, either-sign residual price.
It needs only the integrality gate and nonzero residual; an individual zero output does not undermine this necessary statement, although it prevents an admissible packet.

**Local transition theorem.**
Suppose EVERY clean output g_i(alpha) is a nonzero element of O0, and u<=eta_R.
Then every output value is again a signed monomial.
More precisely:

- At s1, v is a signed coordinate vector, so one coordinate exponent is shifted by k and all other values are unchanged.
- At s>=5R, necessarily V(alpha)=0, so ALL values are unchanged.
- At2<=s<5R, every CLEAN output POLYNOMIAL g_i is itself a signed monomial; its exponent lies in the expanded original interval from min a_i+min(0,k) to max a_i+max(0,k).

For the last case the actual q<=s<5R is enough.
If the clean E1 packet were nontrivial, C71 would give q^8[epsilon(2T_g*m/d)+12T_g*m/d]>=1.
Nontriviality itself forces T_g>0.
But T_g*m/d<=u<=eta_R, and the final inequality in(3), together with monotonicity, contradicts this.
If T_g0, the packet is trivially signed constants under actual integer-value membership and E1.
Thus C71's trivial alternative is the only possibility.
No lower bound on weights or upper bound on N is used.

In every branch, coordinates with v_i=0 are unchanged.
The large-s branch preserves all values and their multiplicities; in either of the other branches at most r_v<=s<5R coordinates change (for s1 use R>=1).
It follows that the new exponent multiplicity R' satisfies

    R'<=R+s<=6R in every changing branch,
    R'=R in the unchanged branch.                         (9)

This deliberately coarse inequality is uniform in the actual denominator and coefficient heights.
Opposite signs and arbitrary collisions are counted.
New signed monomial exponents have span at most B.
This is a statement about both actual values and their unique clean representatives; it is not a claim that an arbitrary previous polynomial representation becomes monomial.

<a id="legal-finite-word-exit-theorem"></a>
## 3. Finite words, clean representatives and the first departure

Fix a finite length L>=1, integer directions v^(j) primitive in Z^N, nonzero INTEGER delays k_j of either sign, and matrices U_j of(5),1<=j<=L.
Start from the clean signed-monomial vector F^(0).
Retain the TRUE Laurent polynomial vector at each stage

    F^(j)(t)=U_j(t) F^(j-1)(t).

Assume EVERY stage is LEGAL: all N actual values F_i^(j)(alpha) belong to O0 minus{0}, for j0,...,L.
This hypothesis is stronger than final integrality and expressly excludes restoration after illegal or zero intermediate coordinates.
The complete true covariance stays N and energy stays1 at every stage, regardless of repeated exponents or denominator growth.

Let A0 be the original seed span and R0 its actual exponent multiplicity.
Charge the entire available shift expense

    B_word=A0+sum_(j=1)^L |k_j|,
    U_word=B_word*m/d.                                    (10)

Actual final common width is at most B_word, but can be MUCH smaller by cancellations.
A small final width does not replace(10).
No constant rational orthogonal rotations, changing dimension, weighted metric or higher-rank factors are included.

**Finite-word theorem.** If

    U_word<=eta_(min{N,6^L R0}),                           (11)

then every intermediate actual value vector consists of signed monomials, and the final full norm income and surplus are zero.
In particular E1 positive income is impossible for ALL finite lengths at U_word<=eta_N.
For a given L the possibly stronger bound eta_(6^L R0) is also sufficient, without bounding N.

Here is the full induction, including the representation issue.
When the previous actual values are signed monomials, their unique clean representative vector C^(j-1)(t) has the same field evaluation as F^(j-1), whether or not the latter polynomials are monomials.
Evaluation is a ring homomorphism, so

    [U_j C^(j-1)](alpha)=[U_j F^(j-1)](alpha).              (12)

The clean output therefore inherits actual nonzero integrality from the TRUE legal stage.
It has its own exact E1 covariance since its clean inputs are signed monomials; this follows directly from paraunitarity, not from replacing polynomials inside an old covariance identity.
Thus the local transition theorem applies to this separately supplied clean construction whenever its expense is small.
This replacement is for the proof of the field-value class and costs; the TRUE vectors, final denominator and signed norms are still retained below.

Assume inductively the clean span is at most A0+sum_(ell<j)|k_ell| and multiplicity at most min{N,6^(j-1)R0}.
Its next local expense is at most B_word.
Since eta_R=K0 R^-64 decreases with R, (11) implies the local threshold at that actual multiplicity.
The local theorem shows the new ACTUAL values are signed monomials, their span grows by at most|k_j| and their multiplicity by at most6.
This proves the induction.
Independently, if only U_word<=eta_N is assumed, the same argument uses the automatic multiplicity bound N at every stage and works for ANY finite L, with no required6^L estimate.
These two observations prove(11).

Every final signed monomial has absolute original norm1; the actual E1 packet therefore has Lambda=0.
No inference about general actual units outside the signed-alpha-power subgroup is needed.
In particular a positive-income final packet must have a FIRST stage whose actual value vector leaves that subgroup.
The proof shows that before this first departure a bounded-multiplicity monomial state cannot be followed by a legal departing step at small paid expense.
Some individual departure could still be to a nonmonomial UNIT with norm of absolute value1; positive income implies a departure, not the converse.

<a id="legal-word-dimension-and-length-price"></a>
## 4. Explicit necessary coordinate and word-length prices

Taking the contrapositive of the two sufficient conditions just proved, ANY legal word with positive final income satisfies BOTH

    U_word>K0 N^(-64),
    U_word>K0 (6^L R0)^(-64).                             (13)

Equivalently,

    N>(K0/U_word)^(1/64),
    L>log[K0/(U_word R0^64)]/[64 log6].                    (14)

The latter is informative only when its right side is positive, but is a valid strict inequality in every case.
No optimality is claimed for the constants or exponents.

For any fixed C>0, on a HYPOTHETICAL sequence of actual nontorsion units with m_j->0 and legal positive-income words satisfying B_word,j<=C d_j, (13) implies

    N_j>(K0/(C*m_j))^(1/64) ->infinity.

If the INITIAL exponent multiplicities are uniformly bounded by a fixed Rbar, then also

    L_j>log[K0/(C*m_j*Rbar^64)]/[64 log6] ->infinity.        (15)

In particular initial DISTINCT monomials have R0=1.
These necessary growth statements allow all coefficient denominators and direction heights to grow without bound.
They do NOT prove that growing N,L is sufficient, that such a near-one sequence exists, or that every short final Laurent matrix admits a short-paid LEGAL factorization.
The cumulative absolute-delay budget is part of the theorem.
A factorization with many cancellations can have a small final window and a large(10), falling outside(15).

<a id="legal-word-complete-true-costs"></a>
## 5. Complete true polynomial costs and remaining ways outside the class

For the TRUE final vector F^(L), let q_L be its ACTUAL least common coefficient denominator after one common polynomial normalization.
The old finite rational factor algebra gives only

    q_L divides product_(j=1)^L s_j,

not equality.
Repeated exponents and cancellations may reduce it.
All indexed weights remain1/N, so FINAL M=N; every label has one copy.
Let D_i=Norm_K(F_i^(L)(alpha)) in Z minus{0}, after retaining the signed unit factor of any common normalization, and B_i=q_L F_i^(L) in Z[t].
Then

    Res(P,B_i)=q_L^d D_i,
    product_i Res(P,B_i)=q_L^(dN) product_i D_i,
    (1/N)sum_i||B_i||_2^2=q_L^2,
    Lambda=(1/(dN))sum_i log|D_i|,
    I_int=log q_L+Lambda,
    I_int-(1/2)log(q_L^2)=Lambda.                         (16)

Every content and every full original signed norm remains.
A common shift by t^b multiplies each norm by nu^b and the copied product by nu^(bN); it preserves absolute income and physical width.
Negative exponents are not fed to an ordinary polynomial resultant before that normalization.
The TRUE final coefficient window is measured from its actual support and is at most B_word.
C10's separate generic expense is Lambda<=(T_final/d)m, not(B_word/d)m declared equal to it.
The latter is only a weaker allowed-budget bound and the quantity used in the new local induction.

Under(11), if the final clean values are epsilon_i' alpha^(a_i'), their complete signed product is

    product_i D_i=(product_i (epsilon_i')^d)*nu^(sum_i a_i'),
    Lambda=0.                                            (17)

This is a conclusion about the TRUE norm values by(12), even if its coefficient representatives and denominator are complicated.
The proof does not replace q_L by a clean q, replace a true matrix factorization by a nonexistent one, or infer norm-product preservation from det(U_j)=t^(k_j).
Outside the stated threshold, actual coordinate norms can and do change under such matrices, as the separately fixed positive quartic control shows.

The exact ways outside this failure theorem remain: an unbounded coordinate count; enough factors to overcome the quantified multiplicity/length bound; a paid cumulative width not O(d) despite small final width; an intermediate nonintegral or zero coordinate before final restoration; a constant rational orthogonal mixing not among the specified factors; a changing weighted metric or dimension; a higher-rank step not supplied as a legal rank-one sequence; or a nonmonomial seed.
The theorem does not exclude these alternatives or assume they work.
Individual negative delays and repeated monomial exponents ARE covered here, unlike the earlier distinct-seed positive single-delay statement.

<a id="legal-delay-word-entire-author-freeze"></a>
## Entire author freeze and review obligations

2026-10-12T13:48.
Root authored all new repeated-seed estimates, the explicit eta_R calculation, clean-value induction, first-departure scope and coordinate/length consequences in this D.
C53/C71/L229/L380 are reused only at their actual stated interfaces; C72 is credited as the single-step motivating antecedent, not a missing premise of the new proof.
Root cannot independently review this material.
The complete original allocation/candidate/reuse history and Sections1--5/equations1--17 must be retained in any fixed extraction.
Every true/clean representation distinction, signed norm cost, cumulative rather than final width, intermediate legality and unproved outside class is part of the scope.
No native mathematical run, new source theorem, Claim adoption, formal verification, external human review or unrestricted G0001 result is asserted.
The next independent whole review should check particularly repeated-exponent Cauchy bounds, both signs of k, no primitivity of H, the strict explicit constants, actual q<=s rather than equality, clean evaluation(12), all changing branches in(9), eta monotonicity with min{N,6^L R0}, and the two separate contrapositives in(13)--(15).
