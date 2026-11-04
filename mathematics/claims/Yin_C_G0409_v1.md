---
author: Yin
---

# Complete plastic-family mixed resultant and signed dyadic energy

The complete original D38 input/result and equations(1)--(15) are retained from [L174](../ledger/Yin_L_G0174_v1.md#retained-plastic-resultant-argument).
The arithmetic author rediscovered the first elimination identity already retained in the family proof, derived the second identity and full resultant/energy reduction, and supplied J35.
The initial absence claim was withdrawn after the old reviewer found the exact earlier identity; the original final review confirmed the corrected introduction and reuse paragraphs without changing the mathematical proof.
The coordinator's known contribution of the expected limiting expression and its complete collaborator check/rerun remain [self-reviewed at their actual scope](../audits/reviews/Yin_R_G0073_v1.md#plastic-resultant-original-collaborator-check-finding).
The separately assigned whole noncontributor finding remains [unknown under its initial-context boundary](../audits/reviews/Yin_R_G0073_v1.md#plastic-resultant-independent-review).
The accepted Dim16 unit is reused at its precise source-statement/direct-specialization depth.
No new source or native execution is used.

## Statement

Let f(z)=z^3-z-1, h(z)=1-z^2-z^3, theta the real root of f, and

    P_N(z)=z^N f(z)+h(z), N=9 mod120, N>=129,
    d_N=N+3, q=N-8.

P_N itself is the monic irreducible primitive Salem polynomial of actual degree d_N, with theta<tau_N<4/3 and m_N=log(tau_N) tending to log(theta)>0.
Let

    L(z)=z^10+z^9-z^7-z^6-z^5-z^4-z^3+z+1,

the original degree-ten Lehmer minimal polynomial, whose exterior root lambda lies in(117/100,118/100), with its reciprocal and eight unit-circle roots.
Put mu=log(lambda).
With every original powered conjugate retained, the exact resultants are positive and satisfy

    R_(1,2)(P_N)=2^(d_N) Res(L,z^q+1)>0.

The proof retains the two identities

    h^2 f(z^2)+f^2 h(z^2)=2zL,
    h-z^8 f=(1-z)L,

Res(f,h)=-1, Res(L,f)=1, and every resulting unit factor and sign.
The first identity is reused from the older complete family proof; its initial mistaken absence claim and original correction remain explicitly historical in L174/R73.

For this fixed L, write C_n=|Res(L,z^n-1)| and A_q=Res(L,z^q+1)=C_(2q)/C_q.
The accepted Dim16 all-index estimate at degree ten and0<mu<1 gives a fixed K_0 such that for every n>=1,

    n mu-K_0 log(2n)<=log C_n<=n mu+10log2.

Consequently

    log R_(1,2)(P_N)=d_N log2+q mu+O(log q).

The original complete Abel energy exists separately at each finite input, and

    E_Q(P_N)=kappa d_N+O(log N),
    kappa=log2+mu-3log(theta)=log(2lambda/(theta+1))>0,
    0.0119<kappa<0.012.

The rate tau_N-theta<=85 theta^(-N)/(27(3theta^2-1)) justifies the stated total error.
All source constants concern the fixed f,L and the accepted uncalibrated logarithmic-form constant; no degree-linear bound on the unbounded q is imposed.

Let K_N be the complete original pair-specific angular energy and gamma the complete fourth-delay theorem's exact positive coefficient.
Then

    [K_N+C_(4N)(P_N)/(4N)]/d_N
        ->kappa-gamma=-0.01002506582917568187...<-0.01.

This subtracts one proved positive contribution from the complete finite-input Abel quantity and then takes the limit.
It does not sum separate mode limits or interchange an infinite sum and N.
J35's exact finite controls at N=9,q=1 and N=129,q=121 give A_q=1 and62723699809; the all-index limit follows from the written proof/source interface, not finite extrapolation.
Any proposed bound E_Q<=C d m+o(d) covering this fixed family requires C>=kappa/log(theta), approximately0.04234028315108.
No uniform near-one bound, unrestricted Lehmer reduction, controlled auxiliary cofactor cost or Task completion is supplied.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:15 |
| status | open |
| reason | Retain the complete exact full-resultant/all-index energy and other-mode cancellation proof, including all signs/costs, actual source depth and corrected reuse history. Actual complete current whole self-check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete resultant and signed-energy theorem](#statement) | Entire original primitive plastic-family full resultant and complete signed-energy theorem, Input/result and equations(1)--(15): N=9mod120/N>=129/actual d=N+3/q=N-8/degree-ten fixed Lehmer root domain, both polynomial identities and all unit resultants/signs/substitution-versus-powered multiplicities, positive exact plus-cyclic quotient, accepted fixed-degree all-index Dim16 source with uncalibrated constant/exponent-one guard, exact q-to-d conversion and exponential tau rate/O(log N), finite-input Abel-before-N order, exact positivity and validated kappa/remaining-mode signs, actual N9/N129 finite controls distinguished from all-index proof, full quotient versus radial/energy income and fixed-positive-measure/near-one/uniformity limits. |
| argument | [Complete original mathematical proof](#argument) | Entire original primitive plastic-family full resultant and complete signed-energy theorem, Input/result and equations(1)--(15): N=9mod120/N>=129/actual d=N+3/q=N-8/degree-ten fixed Lehmer root domain, both polynomial identities and all unit resultants/signs/substitution-versus-powered multiplicities, positive exact plus-cyclic quotient, accepted fixed-degree all-index Dim16 source with uncalibrated constant/exponent-one guard, exact q-to-d conversion and exponential tau rate/O(log N), finite-input Abel-before-N order, exact positivity and validated kappa/remaining-mode signs, actual N9/N129 finite controls distinguished from all-index proof, full quotient versus radial/energy income and fixed-positive-measure/near-one/uniformity limits. |
| dependency | [Complete actual plastic-family classification](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Only the exact polynomial family/root configuration/theta<tau_N<4/3 for N>=16 and the older first identity h^2 f(z^2)+f^2 h(z^2)=2zL; no novelty claim for that identity. |
| dependency | [Complete no-padding progression](Yin_C_G0336_v1.md#a-progression-with-no-cyclotomic-padding) | Only N=9mod120/N>=9 itself irreducible Salem with actual degree N+3 and fixed-positive-measure family; N>=129 satisfies the separate upper-root hypothesis. |
| dependency | [Complete fixed Lehmer algebraic/root proof](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem) | Only the displayed original degree-ten monic irreducible reciprocal nontorsion polynomial, two positive real roots with117/100<lambda<118/100 and eight unit-circle roots; no core conclusion is used. |
| dependency | [Full powered-resultant convention](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Only all actual conjugates and full multiplicities, the distinction from polynomial substitution and existing nonvanishing/doubling floor; every sign/factor in this special reduction is proved here. |
| dependency | [Complete finite-input Salem energy and fourth mode](Yin_C_G0408_v1.md#statement) | Only the exact finite-input Abel identity/correction, primitive-family fixed-k moving-frequency theorem and exact gamma=-c4c8/4 certificate with its original retained J30 depth; no single-mode lower bound for a complete signed sum. |
| dependency | [Accepted fixed-polynomial all-index source interface](../audits/literature/Dim16/Yin_U001.md#dim16-u001) | Only its complete all-integer n>=1 cyclic-norm specialization on this fixed degree-ten nontorsion unit/0<mu<1, including exponent-one guard and reported Baker--Wustholz source-statement boundary/uncalibrated constant; no new source-proof audit or calibration. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:21 |
| status | proved |
| reason | Adopt after the actual entire current statement/proof and fixed-source/native-certificate self-check of every resultant factor/sign/multiplicity, all-index cyclic ratio and full finite-input-to-limit energy/cancellation step. Retain the original reuse-negative correction, exact source depth, fixed residual degree/error constants and fixed-positive-measure scope. The current whole finding is SELF and does not close the original whole UNKNOWN arrangement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire original primitive plastic-family full resultant and complete signed-energy theorem, Input/result and equations(1)--(15): N=9mod120/N>=129/actual d=N+3/q=N-8/degree-ten fixed Lehmer root domain, both polynomial identities and all unit resultants/signs/substitution-versus-powered multiplicities, positive exact plus-cyclic quotient, accepted fixed-degree all-index Dim16 source with uncalibrated constant/exponent-one guard, exact q-to-d conversion and exponential tau rate/O(log N), finite-input Abel-before-N order, exact positivity and validated kappa/remaining-mode signs, actual N9/N129 finite controls distinguished from all-index proof, full quotient versus radial/energy income and fixed-positive-measure/near-one/uniformity limits. |
| argument | [Exact retained argument](#argument) | Entire original primitive plastic-family full resultant and complete signed-energy theorem, Input/result and equations(1)--(15): N=9mod120/N>=129/actual d=N+3/q=N-8/degree-ten fixed Lehmer root domain, both polynomial identities and all unit resultants/signs/substitution-versus-powered multiplicities, positive exact plus-cyclic quotient, accepted fixed-degree all-index Dim16 source with uncalibrated constant/exponent-one guard, exact q-to-d conversion and exponential tau rate/O(log N), finite-input Abel-before-N order, exact positivity and validated kappa/remaining-mode signs, actual N9/N129 finite controls distinguished from all-index proof, full quotient versus radial/energy income and fixed-positive-measure/near-one/uniformity limits. |
| dependency | [Exact retained dependency](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Only the exact polynomial family/root configuration/theta<tau_N<4/3 for N>=16 and the older first identity h^2 f(z^2)+f^2 h(z^2)=2zL; no novelty claim for that identity. |
| dependency | [Exact retained dependency](Yin_C_G0336_v1.md#a-progression-with-no-cyclotomic-padding) | Only N=9mod120/N>=9 itself irreducible Salem with actual degree N+3 and fixed-positive-measure family; N>=129 satisfies the separate upper-root hypothesis. |
| dependency | [Exact retained dependency](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem) | Only the displayed original degree-ten monic irreducible reciprocal nontorsion polynomial, two positive real roots with117/100<lambda<118/100 and eight unit-circle roots; no core conclusion is used. |
| dependency | [Exact retained dependency](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Only all actual conjugates and full multiplicities, the distinction from polynomial substitution and existing nonvanishing/doubling floor; every sign/factor in this special reduction is proved here. |
| dependency | [Exact retained dependency](Yin_C_G0408_v1.md#statement) | Only the exact finite-input Abel identity/correction, primitive-family fixed-k moving-frequency theorem and exact gamma=-c4c8/4 certificate with its original retained J30 depth; no single-mode lower bound for a complete signed sum. |
| dependency | [Exact retained dependency](../audits/literature/Dim16/Yin_U001.md#dim16-u001) | Only its complete all-integer n>=1 cyclic-norm specialization on this fixed degree-ten nontorsion unit/0<mu<1, including exponent-one guard and reported Baker--Wustholz source-statement boundary/uncalibrated constant; no new source-proof audit or calibration. |
| review | [Complete actual current whole self finding](../audits/reviews/Yin_R_G0613_v1.md#current-plastic-complete-energy-finding) | Entire original primitive plastic-family full resultant and complete signed-energy theorem, Input/result and equations(1)--(15): N=9mod120/N>=129/actual d=N+3/q=N-8/degree-ten fixed Lehmer root domain, both polynomial identities and all unit resultants/signs/substitution-versus-powered multiplicities, positive exact plus-cyclic quotient, accepted fixed-degree all-index Dim16 source with uncalibrated constant/exponent-one guard, exact q-to-d conversion and exponential tau rate/O(log N), finite-input Abel-before-N order, exact positivity and validated kappa/remaining-mode signs, actual N9/N129 finite controls distinguished from all-index proof, full quotient versus radial/energy income and fixed-positive-measure/near-one/uniformity limits. Actual whole relationship is self-reviewed; all original complete noncontributor UNKNOWN and known collaborator/author SELF scopes remain separately retained. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:02 |
| status | proved |
| reason | Adopt the new isolated complete finding for every full resultant factor/sign/multiplicity, fixed-L all-index source specialization, finite-input-before-family-limit energy and cancellation, and exact original-parameter read-only J35 reproduction. Preserve accepted source depth, reuse-negative correction, original whole scopes and fixed-positive-measure/uniformity limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original primitive plastic-family full resultant and complete signed-energy theorem, Input/result and equations(1)--(15): N=9mod120/N>=129/actual d=N+3/q=N-8/degree-ten fixed Lehmer root domain, both polynomial identities and all unit resultants/signs/substitution-versus-powered multiplicities, positive exact plus-cyclic quotient, accepted fixed-degree all-index Dim16 source with uncalibrated constant/exponent-one guard, exact q-to-d conversion and exponential tau rate/O(log N), finite-input Abel-before-N order, exact positivity and validated kappa/remaining-mode signs, actual N9/N129 finite controls distinguished from all-index proof, full quotient versus radial/energy income and fixed-positive-measure/near-one/uniformity limits. |
| argument | [Complete selected argument](#argument) | Entire original primitive plastic-family full resultant and complete signed-energy theorem, Input/result and equations(1)--(15): N=9mod120/N>=129/actual d=N+3/q=N-8/degree-ten fixed Lehmer root domain, both polynomial identities and all unit resultants/signs/substitution-versus-powered multiplicities, positive exact plus-cyclic quotient, accepted fixed-degree all-index Dim16 source with uncalibrated constant/exponent-one guard, exact q-to-d conversion and exponential tau rate/O(log N), finite-input Abel-before-N order, exact positivity and validated kappa/remaining-mode signs, actual N9/N129 finite controls distinguished from all-index proof, full quotient versus radial/energy income and fixed-positive-measure/near-one/uniformity limits. |
| dependency | [Exact accepted input](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Only the exact polynomial family/root configuration/theta<tau_N<4/3 for N>=16 and the older first identity h^2 f(z^2)+f^2 h(z^2)=2zL; no novelty claim for that identity. |
| dependency | [Exact accepted input](Yin_C_G0336_v1.md#a-progression-with-no-cyclotomic-padding) | Only N=9mod120/N>=9 itself irreducible Salem with actual degree N+3 and fixed-positive-measure family; N>=129 satisfies the separate upper-root hypothesis. |
| dependency | [Exact accepted input](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem) | Only the displayed original degree-ten monic irreducible reciprocal nontorsion polynomial, two positive real roots with117/100<lambda<118/100 and eight unit-circle roots; no core conclusion is used. |
| dependency | [Exact accepted input](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Only all actual conjugates and full multiplicities, the distinction from polynomial substitution and existing nonvanishing/doubling floor; every sign/factor in this special reduction is proved here. |
| dependency | [Exact accepted input](Yin_C_G0408_v1.md#statement) | Only the exact finite-input Abel identity/correction, primitive-family fixed-k moving-frequency theorem and exact gamma=-c4c8/4 certificate with its original retained J30 depth; no single-mode lower bound for a complete signed sum. |
| dependency | [Exact accepted input](../audits/literature/Dim16/Yin_U001.md#dim16-u001) | Only its complete all-integer n>=1 cyclic-norm specialization on this fixed degree-ten nontorsion unit/0<mu<1, including exponent-one guard and reported Baker--Wustholz source-statement boundary/uncalibrated constant; no new source-proof audit or calibration. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0618_v1.md#isolated-plastic-energy-finding) | Entire original primitive plastic-family full resultant and complete signed-energy theorem, Input/result and equations(1)--(15): N=9mod120/N>=129/actual d=N+3/q=N-8/degree-ten fixed Lehmer root domain, both polynomial identities and all unit resultants/signs/substitution-versus-powered multiplicities, positive exact plus-cyclic quotient, accepted fixed-degree all-index Dim16 source with uncalibrated constant/exponent-one guard, exact q-to-d conversion and exponential tau rate/O(log N), finite-input Abel-before-N order, exact positivity and validated kappa/remaining-mode signs, actual N9/N129 finite controls distinguished from all-index proof, full quotient versus radial/energy income and fixed-positive-measure/near-one/uniformity limits. Entire current statement and argument are independently reviewed in the new finding; this includes the full current comparison at its explicitly stated domain where present. Original reviewer reruns remain distinct from the new bounded read-only reproductions, and old historical relationships are unchanged. |

## Complete retained argument

<a id="argument"></a>

<a id="retained-plastic-resultant-argument"></a>

### Input and result

Write

    f(z)=z^3-z-1,             h(z)=f*(z)=1-z^2-z^3,
    L(z)=z^10+z^9-z^7-z^6-z^5-z^4-z^3+z+1,
    P_N(z)=z^N f(z)+h(z),     d_N=N+3,
    N=9 mod120,              N>=129,
    q=N-8.

The actual primitive irreducible Salem-family input is the already fixed [complete family classification](Yin_C_G0248_v1.md#family-cyclotomic-factors), used in [complete no-padding progression](Yin_C_G0336_v1.md#a-progression-with-no-cyclotomic-padding).
Its exterior root tau_N satisfies theta<tau_N<4/3 and tends to the plastic root theta of f.
There is no removed cyclotomic factor.
The polynomial L is exactly the original degree-ten Lehmer minimal polynomial, with exterior root lambda in (117/100,118/100) and eight unit-circle roots, as retained in [complete fixed Lehmer root proof](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem).
Put mu=log(lambda).

Use all d_N conjugates in the powered resultant R_(1,2), as in [complete full-root resultant interface](Yin_C_G0231_v1.md#mixed-power-resultant-identities).
The complete exact reduction proved below is

    |R_(1,2)(P_N)|=2^(d_N) |Res(L,z^q+1)|.             (1)

In fact both sides before taking absolute values are positive in this domain.
Consequently the normalized Frobenius quotient is precisely a plus-cyclic norm of the fixed Lehmer unit; it is not an isolated Fourier mode or an estimate with omitted conjugates.

The already accepted [Dim16 all-index cyclic-norm bound](Yin_C_G0854_v1.md#dim16-cyclic-all-index) then gives

    log|R_(1,2)(P_N)|=d_N log2+q mu+O(log q).          (2)

For the exact original damped-polynomial energy E_Q of [complete exact positive-Salem identity](Yin_C_G0408_v1.md#salem-exact-damped-mixed-identity), the resulting complete limit is

    E_Q(P_N)/d_N -> kappa,
    kappa=log2+mu-3log(theta)
         =log(2lambda/(theta+1))>0.                  (3)

This is a fixed-positive-measure family: log M(P_N) tends to log(theta)>0.
The result gives a genuine linear normalized resultant quotient on this actual family, but supplies neither a near-one example nor a uniform estimate over variable Salem inputs.
The original development-time pending review statement remains historical in L174; this complete home has the explicit current assessment above.

<a id="plastic-lehmer-resultant-reduction"></a>
### 1. Exact elimination with every resultant factor retained

The first identity below is already retained in [the retained odd-order elimination row](Yin_C_G0248_v1.md#family-cyclotomic-factors).
It was independently rediscovered in this round.
Direct polynomial expansion checks it and the separately derived second identity in Z[z]:

    h(z)^2 f(z^2)+f(z)^2 h(z^2)=2z L(z),
    h(z)-z^8 f(z)=(1-z)L(z).                          (4)

There are no common zeros of f and h.
More precisely,

    Res(f,h)=-1,       Res(f,1-z)=f(1)=-1,
    Res(L,f)=Res(f,L)=1.                              (5)

Here is a direct check of the unit constants.
At a root u of f, h(u)=-u(u+1).
The products of the three roots u and of u+1 are respectively 1 and -f(-1)=1, so their h product is -1.
The second identity in (4), evaluated on those same roots, gives Res(f,h)=Res(f,1-z)Res(f,L), hence Res(f,L)=1.
Interchanging the degrees 3 and 10 introduces no sign.
Thus (5) does not rely on a numerical resultant computation.

Since d_N is even, resultant interchange between f and P_N has sign (-1)^(3d_N)=1.
Evaluation at the f roots therefore gives

    Res(P_N,f)=Res(f,P_N)=Res(f,h)=-1.                (6)

For each root alpha of P_N, f(alpha) is nonzero and alpha^N=-h(alpha)/f(alpha).
Thus

    P_N(alpha^2)
       =[h(alpha)^2 f(alpha^2)+f(alpha)^2 h(alpha^2)]/f(alpha)^2.

Taking products over all d_N roots, with multiplicities, and using (4)--(6) proves

    Res(P_N,P_N(z^2))=Res(P_N,2zL)/Res(P_N,f)^2
                    =2^(d_N) Res(P_N,L).             (7)

The factor Res(P_N,z) is one, because P_N has even degree, is monic and has constant coefficient one.
The denominator in (7) is also one; neither can carry an unrecorded exponential cost.
On the other hand

    Res(P_N,P_N(z^2))
      =product_(i,j)(alpha_i^2-alpha_j)
      =(-1)^(d_N^2) R_(1,2)(P_N)
      =R_(1,2)(P_N).                                 (8)

This explicitly distinguishes polynomial substitution from powering its complete root multiset and accounts for their sign here.

Interchange with L again has positive sign.
At a root z of L, the second identity in (4) gives h(z)=z^8 f(z), so

    P_N(z)=z^8 f(z)(z^q+1).

The factor Res(L,z^8) is one, since L is a monic even-degree unit polynomial, and Res(L,f)=1 by (5).
Consequently

    Res(P_N,L)=Res(L,P_N)=Res(L,z^q+1).               (9)

Equations (7)--(9) establish (1).
No degree loss or factor deletion is hidden in this calculation.
L has no root of unity, so its last resultant is nonzero.
Its two real-root factors lambda^q+1 and lambda^(-q)+1 are positive, and each complex pair contributes an absolute square.
Thus the resultant in (9) and R_(1,2) in (8) are actually positive.
The algebraic reduction also holds at N=9, q=1; the stricter N>=129 bound is used for the uniform root bounds and asymptotic family scope.

<a id="complete-plastic-mixed-energy-limit"></a>
### 2. Complete growth from an already accepted fixed-polynomial estimate

For this one fixed L put C_n=|Res(L,z^n-1)|.
Its irreducible degree is ten, it is a nontorsion unit, and 0<mu<1.
It therefore satisfies the full hypotheses of the retained Dim16-U001 specialization.
There is a fixed K_0 such that for every n>=1,

    n mu-K_0 log(2n) <= log C_n <= n mu+10log2.        (10)

The accepted source bound is the reported Baker--Wustholz interface at its existing statement/applicability scope.
Its transcendence proof and absolute numerical constant were not audited there and are not newly audited or calibrated here.
The guarded n=1 case in that unit remains valid; no uninspected multivariable convergence theorem is used.

Multiplicativity of resultants gives the exact plus-cyclic identity

    A_q:=|Res(L,z^q+1)|=C_(2q)/C_q.

Both C values are positive.
Equation (10) yields

    q mu-K_0 log(4q)-10log2 <= log A_q
                         <= q mu+K_0 log(2q)+10log2. (11)

The elementary bound |1+z^q|<=2 max(1,|z|)^q improves the right side to q mu+10log2 if desired.
Thus log A_q=q mu+O(log q), proving (2).
This is an all-q limit for a fixed degree-ten residual polynomial.
The exponent q tends to infinity; no claim q<=C deg(L), and no invocation of L168 under such a false condition, is made.
The growing original degree d_N and the fixed residual degree ten have different roles.

It remains to convert this resultant growth to the complete energy.
Define m_N=log(tau_N) and r_N=tau_N^(-1).
D29's exact per-input identity is

    E_Q(P_N)=log|R_(1,2)(P_N)|-(3d_N-2)m_N
                                +2log(1+r_N+r_N^2). (12)

The energy here is the Abel limit of the complete signed dyadic correlation of the original Q power sums.
D29 proved its existence from nonvanishing of the mixed resultant and the exact Salem correction.
We first use (12) for each fixed N, and only then let N tend to infinity.
No Fourier series is truncated, no sum of limiting mode coefficients is substituted, and no Abel/N limit exchange occurs.

Dividing (12) by d_N, using q/d_N=(N-8)/(N+3) tending to one, m_N tending to log(theta), and the bounded correction, proves (3).
There is also the fixed-input error statement

    E_Q(P_N)=kappa d_N+O(log N).                      (13)

For completeness the required rate of m_N follows directly from the family equation.
On theta<=tau_N<4/3, f'(t)>=3theta^2-1 and -h(t)<=85/27.
Since tau_N^N f(tau_N)=-h(tau_N),

    0<tau_N-theta
       <=[85/(27(3theta^2-1))] theta^(-N).

Thus m_N-log(theta)=O(theta^(-N)), and multiplying this error by d_N does not spoil (13).
All O constants in (10)--(13) concern the fixed f and L and may include the uncalibrated accepted logarithmic-form constant.

### 3. The sign, cancellation, and actual arithmetic content

The identity theta^3=theta+1 gives kappa=log(2lambda/(theta+1)).
The retained rational bounds lambda>117/100 and theta<4/3 already imply

    2lambda/(theta+1)>351/350>1.

So the complete normalized energy is strictly positive without a numerical approximation.
[J G0035](../computations/programs/Yin_J_G0035/readme.md) additionally certifies

    0.0119 < kappa < 0.012,
    kappa=0.0119060695987979093132786328095...,
    kappa/log(theta)=0.04234028315108191908....        (14)

The two strict decimal endpoints are exact rationals.
Exact polynomial identities and direct full powered-resultant controls at N=9 and N=129 both pass; their quotient values A_q are respectively 1 and 62723699809.
The former is an initial exact-floor instance, not a contradiction to eventual linear growth.
The intervals and finite controls do not prove the source-dependent all-index limit by extrapolation.

The quotient |R_(1,2)|/2^(d_N)=A_(N-8) has logarithm mu*d_N+O(log N), giving an actual linear arithmetic surplus for this family.
The original radial term is simultaneously about 3d_N log(theta).
The residual kappa is the full signed-energy balance after that radial contribution is subtracted, not the entire logarithmic resultant quotient.

In contrast, [complete fourth-delay theorem](Yin_C_G0408_v1.md#plastic-fourth-mode-certificate) has coefficient gamma=-c_4 c_8/4 approximately 0.0219311354.
Its positive contribution is larger than the complete constant kappa.
Let K_N denote the complete original pair-specific angular energy, so K_N=E_Q(P_N)-2log(1+r_N+r_N^2).
Removing just that fourth-delay term gives

    [K_N+C_(4N)(P_N)/(4N)]/d_N -> kappa-gamma
       =-0.01002506582917568187... < -0.01.           (15)

The expression on the left is exactly the per-input Abel sum of all the other original Fourier terms.
Thus they have a negative normalized net contribution even though the total limit is positive.
This statement uses the difference of two proved finite-input quantities and their separate limits, rather than summing termwise limits.
The bounded correction between E_Q and K_N does not affect their normalized limits.
J35's validated interval check certifies the strict rational upper bound in (15).

This calculation supplies a concrete benchmark for a proposed upper bound such as E_Q<=C*d*m+o(d): any such bound covering this family would need C>=kappa/log(theta).
It supplies no bound in the other direction, no evidence that a candidate inequality extends to m tending to zero, and no same-exponent coverage for arbitrary inputs.
In particular the original Lehmer polynomial's appearance as a residual algebraic factor is an exact identity for the plastic family, not a reduction of unrestricted Lehmer's problem to that fixed example.

## Original correction, contributions and exact limits

The entire original inaccurate absence claim, the reviewer's exact L38 discovery, withdrawal, corrected introduction/reuse reread and original complete final review remain in L174/R73.
That source-reuse correction changed no mathematical equation or proof.
The old collaborator and whole noncontributor findings keep their distinct actual contexts and computational depths.
The old whole noncontributor review read all J35 code and retained output and did not rerun it; the separately recorded coordinator rerun used disposable redirected output and matched every mathematical field.
J35's two direct full-powered resultants, exact unit identities, root brackets narrower than2^(-280),320-bit propagated constants and overlap-only consistency check remain finite evidence, distinct from the accepted all-index argument.

The first elimination identity is older retained mathematics; the z^8 identity and complete resultant/energy deduction have their actual disclosed contributions, without an exhaustive novelty claim.
The full quotient has logarithmic surplus mu*d_N+O(log N), while the original radial term is about3d_N log(theta).
Kappa is the residual complete signed-energy coefficient after that radial subtraction.
The actual family stays at fixed positive measure, so these identities supply no uniform small-measure or unrestricted-Lehmer conclusion.
No new source reading, native run, independent verifier or Task execution is supplied.
