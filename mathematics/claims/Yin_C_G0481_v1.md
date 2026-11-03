---
author: Yin
---

# Complete minimal Frobenius valuation, exact cyclic quotients and actual p-power lifts

The entire necessary original D69 proof is retained from [L202](../ledger/Yin_L_G0202_v1.md#retained-minimal-frobenius-proof), including all five sections, equations(1)--(17), both actual controls and every failed-coverage/cost boundary.
The assigned resultant_research AI developed its new deductions; the coordinator supplied a broad question and actually received interim findings.
The original `Yin_R_G0101_v1#minimal-frobenius-complete-independent-review` remains historically UNKNOWN because the actual prior interim/shared mathematical contents and initial reconstruction order are not established; [the later complete comparison](../audits/reviews/Yin_R_G0697_v1.md#l202-and-r101) preserves its complete original scope, date, inputs, verdict and limitations.
Earlier fixed L194/L200 contribution is disclosed reuse, not automatically target authorship or fresh independent re-proof.
The exact [original listed author checks](../audits/reviews/Yin_R_G0101_v1.md#minimal-frobenius-original-author-check-finding) remain separately SELF.
The fixed J10 facts retain their adequate C251/J10 mathematical/native homes without a new computation, source proof, program/J or research Task/E.

## Statement

Let P in Z[t] be the monic irreducible minimal polynomial of a nontorsion algebraic unit alpha, of actual degree d>=1, and let p be any rational prime.
Write K=Q(alpha),O=Z[alpha],P^[p] for the complete pth-powered polynomial retaining every conjugate multiplicity, and

    R_p=Res(P,P^[p]),C_n=|Norm_K(alpha^n-1)|,
    D_n=|Norm_K(Phi_n(alpha))|.

Assume exactly v_p(R_p)=d.
Other prime factors are allowed and reciprocity is unnecessary.
For every integer n>=1 prime to p, define the monic gcds

    g_n=gcd(Pbar,t^n-1),h_n=gcd(Pbar,Phi_n mod p)
    in F_p[t].

They are squarefree even if Pbar has repeated factors.
There are exact ring identifications

    (O/(alpha^n-1)O)_(p) = F_p[t]/g_n,
    (O/Phi_n(alpha)O)_(p) = F_p[t]/h_n,
    v_p(C_n)=deg g_n,v_p(D_n)=deg h_n,

where equalities of rings denote canonical isomorphisms and the subscript(p) denotes the entire finite p-primary ring, equivalently tensoring with Z_(p).
These rings are killed by p and are products of finite fields; gcd1 gives the zero ring.
For distinct irreducible factors phi of Pbar, with nonzero-root multiplicative order r_phi,

    v_p(C_n)=sum_(r_phi divides n)deg phi,
    v_p(D_n)=sum_(r_phi=n)deg phi, p not dividing n.

Original factor multiplicities do not occur at this first layer.
Other prime parts remain uncontrolled, and this does not assert global p/(alpha^n-1) in O.

The integral defect E_p=[P(t^p)-P(t)^p]/p satisfies gcd(Pbar,E_p mod p)=1.
Its determinant proof, explicit unique square-zero idempotent lift in (Z/p^2)[t]/(t^n-1) or Phi_n, Frobenius substitution automorphism and fixed idempotent, and full Smith-group passage prove the entire ring statements above, including p=2 and bad reduction.

The element alpha is not a pth power in K.
The proof uses the actual degree-d polynomial of a hypothetical integral unit gamma with gamma^p=alpha and a common reduced-root period n prime to p.
Writing r=deg rad(Pbar)>=1, the exact valuation r contradicts the two nonzero norm factors of gamma^n-1 and 1+gamma^n+...+gamma^((p-1)n), each with determinant valuation at least r.
The elementary prime-binomial product-of-roots argument therefore makes X^p-alpha irreducible over K.

For every positive integer q, without first assuming P(t^q) irreducible,

    Res(P(t^q),(P(t^q))^[p])=R_p^q,

with all fibers, multiplicities and orientation signs retained, including p dividing q.
No identity (P(t^q))^[p]=P^[p](t^q) is assumed when p divides q.
Consequently for every integer k>=0,

    F_k(t)=P(t^(p^k))

is actually irreducible of degree d p^k, is a nontorsion unit polynomial, and has M(F_k)=M(P)>1.
It is reciprocal if P is.
Its reduction is Pbar^(p^k), while for every n prime to p,

    v_p(C_n(F_k))=deg gcd(Pbar,t^n-1)<=r

independently of k.

For a monic polynomial F, define C_n(F) by the complete absolute product over every root with multiplicity; for irreducible F this is the actual field norm.
For every positive q,n,

    C_n(P(t^q))=C_(n/g)(P)^g,g=gcd(n,q).

Thus for n=p^j u,p not dividing u and0<=j<=k,

    v_p(C_(p^j u)(F_k))=p^j deg gcd(Pbar,t^u-1).

For any fixed eta>0, local income v_p(C_n(F_k))log p>=eta*d p^k at j<=k requires

    p^(k-j)<=r log p/(eta d).

A common reduced-root period u_0 realizes

    v_p(C_(p^k u_0)(F_k))=p^k r,
    (p^k u_0)/deg F_k=u_0/d.

These are genuine degree-linear local peaks on every fixed base, with no uniform varying-base bound on u_0/d or r/d.

For P6=t^6-t^5-t^3-t+1,p=2,R_2=2^6,Pbar=Phi_3^3, every F_k=P6(t^(2^k)) is actually irreducible of degree6*2^k.
At every odd n its dyadic valuation is2 if3 divides n and0 otherwise.
The complete norm is

    C_(3*2^k)(F_k)=4^(2^k),

so at n=deg F_k/2 the complete logarithm is(deg F_k)log2/3.
No bound on later odd-prime income is asserted.

For the original Lehmer polynomial, R_2=2^10 and its retained two distinct mod-two factors have degree5 and root order31.
Every dyadic lift is actually irreducible of degree10*2^k, and at odd n its dyadic valuation is10 if31 divides n and0 otherwise, while

    v_2(C_(31*2^k)(F_k))=10*2^k.

This last assertion is a local valuation, not a pure power-of-two complete norm.
Both families keep fixed positive total base measure; no Salem or near-one sequence is asserted.
The theorem does not cover all near-one inputs by its hypothesis, bound varying reduced-root periods/radical proportions, control inverse or full complementary auxiliary costs, or prove a Mahler gap.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:32 |
| status | open |
| reason | Retain the entire actual-order/all-prime minimal-Frobenius proof, complete prime-to-p cyclic and cyclotomic ring structure, same-field root exclusion, signed all-fiber resultant and actual p-power irreducibility, complete norm/delayed income formulas and two fixed-base controls with every source/native/near-one/cost limitation. Actual current whole SELF and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire minimal-Frobenius and radical-lift theorem](#statement) | Entire original D69 Sections1--5/equations(1)--(17), every monic actual-degree irreducible nontorsion unit/every rational prime p/exact v_p Res(P,P^[p])=d/other prime factors allowed/no reciprocity needed, actual O=Z[alpha]/every n>=1 prime to p/entire finite p-primary cyclic and cyclotomic rings/reduced squarefree gcds despite repeated Pbar/zero-ring case/exact valuations and root-order formulas/no global p-division or other-prime control, integral Frobenius defect/full determinant orientation/arbitrary-reduction gcd criterion/explicit square-zero idempotent lift including p2/sigma and its fixed lift/unit complementary component/full quotient modulo p2/entire Smith p-primary group, same-field pth-root exclusion/integrality/degree equality/common reduced-root period/two nonzero norm factors/both determinant nullities/prime-binomial proof including p2, every positive q complete signed resultant preservation with all fibers/multiplicities and p-divisible q/no false powered composition/all k>=0 actual irreducible p-power lifts/constant positive total Mahler measure/repeated reduction/all prime-to-p local income, complete all-q all-n cyclic norm fiber identity/every 0<=j<=k delayed valuation/necessary exponent inequality/common-period linear peaks/base-dependent cost, exact degree-six and original Lehmer dyadic control families/full P6 norm versus local Lehmer valuation/actual reduced factors and orders/no new native run, all original contribution/source/fixed-measure/near-one/inverse/cofactor/uncontrolled-other-prime boundaries. |
| argument | [Entire complete retained proof](#argument) | Entire original D69 Sections1--5/equations(1)--(17), every monic actual-degree irreducible nontorsion unit/every rational prime p/exact v_p Res(P,P^[p])=d/other prime factors allowed/no reciprocity needed, actual O=Z[alpha]/every n>=1 prime to p/entire finite p-primary cyclic and cyclotomic rings/reduced squarefree gcds despite repeated Pbar/zero-ring case/exact valuations and root-order formulas/no global p-division or other-prime control, integral Frobenius defect/full determinant orientation/arbitrary-reduction gcd criterion/explicit square-zero idempotent lift including p2/sigma and its fixed lift/unit complementary component/full quotient modulo p2/entire Smith p-primary group, same-field pth-root exclusion/integrality/degree equality/common reduced-root period/two nonzero norm factors/both determinant nullities/prime-binomial proof including p2, every positive q complete signed resultant preservation with all fibers/multiplicities and p-divisible q/no false powered composition/all k>=0 actual irreducible p-power lifts/constant positive total Mahler measure/repeated reduction/all prime-to-p local income, complete all-q all-n cyclic norm fiber identity/every 0<=j<=k delayed valuation/necessary exponent inequality/common-period linear peaks/base-dependent cost, exact degree-six and original Lehmer dyadic control families/full P6 norm versus local Lehmer valuation/actual reduced factors and orders/no new native run, all original contribution/source/fixed-measure/near-one/inverse/cofactor/uncontrolled-other-prime boundaries. |
| dependency | [Complete normalized Frobenius determinant and gcd criterion](Yin_C_G0237_v1.md#base-prime-power-extra-valuation) | Actual O=Z[alpha], full p^d normalization, arbitrary-reduction invertibility/gcd and first-lifting criterion. The new prime-to-p entire quotient is proved directly below. |
| support | [Complete original cyclotomic layer comparison](Yin_C_G0265_v1.md#old-layer-exception-threshold) | Comparison of distinct-factor initial depth with original-root multiplicities in later stable layers; no later-layer estimate is silently imported into the new initial quotient. |
| support | [Complete short cyclic saturation interface](Yin_C_G0473_v1.md#saturated-short-cyclic-fixed-scope) | Original short-return/odd-prime restrictions as comparison only; no all-input saturation or new uniform inverse/cofactor bound is assumed. |
| support | [Complete elementary prime-binomial proof](Yin_C_G0376_v2.md#irreducible-lehmer-radical-control) | Only the displayed elementary prime-binomial root-product argument, repeated directly below. Its separate degree-only external source bound and large-prime cutoff are not used. |
| dependency | [Complete degree-six actual saturation and norm control](Yin_C_G0478_v1.md#degree-six-principal-saturation-fixed-scope) | P6 actual polynomial/unit/nontorsion, R_2=64, repeated reduction Phi3 cubed and complete C3=4, used in the full dyadic fiber control. No fresh J39/J40 certificate review is claimed. |
| dependency | [Complete original Lehmer trace and resultant control](Yin_C_G0243_v1.md#reciprocal-trace-lehmer-control) | Original actual degree-ten Lehmer base with R_2=1024; not a uniform varying-base hypothesis. |
| dependency | [Complete retained J10 finite factor/order proof](Yin_C_G0251_v1.md#j10-complete-exponent-profile-proof) | Only original Lehmer two distinct degree-five mod-two factors with root order31, at the already retained original coefficient/factor/order native scope. Output was read without a new run or recertification of every original source/program. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:33 |
| status | proved |
| reason | Adopt after actual complete current whole SELF of the entire finite-ring/p-primary quotient proof, both Smith nullities and same-field root contradiction, elementary prime-binomial and all signed complete fibers, actual p-power irreducibility, full norm/delayed local-income consequences and both exact controls, with every actual-order/repeated-reduction/source/native/fixed-measure/near-one/cost boundary. No substantive defect or missing hypothesis was found. Current SELF does not close original R101 entire whole UNKNOWN or enlarge its exact listed author checks; fixed J10 outputs were read without a new run, source-proof audit or research execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire original D69 Sections1--5/equations(1)--(17), every monic actual-degree irreducible nontorsion unit/every rational prime p/exact v_p Res(P,P^[p])=d/other prime factors allowed/no reciprocity needed, actual O=Z[alpha]/every n>=1 prime to p/entire finite p-primary cyclic and cyclotomic rings/reduced squarefree gcds despite repeated Pbar/zero-ring case/exact valuations and root-order formulas/no global p-division or other-prime control, integral Frobenius defect/full determinant orientation/arbitrary-reduction gcd criterion/explicit square-zero idempotent lift including p2/sigma and its fixed lift/unit complementary component/full quotient modulo p2/entire Smith p-primary group, same-field pth-root exclusion/integrality/degree equality/common reduced-root period/two nonzero norm factors/both determinant nullities/prime-binomial proof including p2, every positive q complete signed resultant preservation with all fibers/multiplicities and p-divisible q/no false powered composition/all k>=0 actual irreducible p-power lifts/constant positive total Mahler measure/repeated reduction/all prime-to-p local income, complete all-q all-n cyclic norm fiber identity/every 0<=j<=k delayed valuation/necessary exponent inequality/common-period linear peaks/base-dependent cost, exact degree-six and original Lehmer dyadic control families/full P6 norm versus local Lehmer valuation/actual reduced factors and orders/no new native run, all original contribution/source/fixed-measure/near-one/inverse/cofactor/uncontrolled-other-prime boundaries. |
| argument | [Exact retained argument](#argument) | Entire original D69 Sections1--5/equations(1)--(17), every monic actual-degree irreducible nontorsion unit/every rational prime p/exact v_p Res(P,P^[p])=d/other prime factors allowed/no reciprocity needed, actual O=Z[alpha]/every n>=1 prime to p/entire finite p-primary cyclic and cyclotomic rings/reduced squarefree gcds despite repeated Pbar/zero-ring case/exact valuations and root-order formulas/no global p-division or other-prime control, integral Frobenius defect/full determinant orientation/arbitrary-reduction gcd criterion/explicit square-zero idempotent lift including p2/sigma and its fixed lift/unit complementary component/full quotient modulo p2/entire Smith p-primary group, same-field pth-root exclusion/integrality/degree equality/common reduced-root period/two nonzero norm factors/both determinant nullities/prime-binomial proof including p2, every positive q complete signed resultant preservation with all fibers/multiplicities and p-divisible q/no false powered composition/all k>=0 actual irreducible p-power lifts/constant positive total Mahler measure/repeated reduction/all prime-to-p local income, complete all-q all-n cyclic norm fiber identity/every 0<=j<=k delayed valuation/necessary exponent inequality/common-period linear peaks/base-dependent cost, exact degree-six and original Lehmer dyadic control families/full P6 norm versus local Lehmer valuation/actual reduced factors and orders/no new native run, all original contribution/source/fixed-measure/near-one/inverse/cofactor/uncontrolled-other-prime boundaries. |
| dependency | [Exact retained dependency](Yin_C_G0237_v1.md#base-prime-power-extra-valuation) | Actual O=Z[alpha], full p^d normalization, arbitrary-reduction invertibility/gcd and first-lifting criterion. The new prime-to-p entire quotient is proved directly below. |
| support | [Exact retained support](Yin_C_G0265_v1.md#old-layer-exception-threshold) | Comparison of distinct-factor initial depth with original-root multiplicities in later stable layers; no later-layer estimate is silently imported into the new initial quotient. |
| support | [Exact retained support](Yin_C_G0473_v1.md#saturated-short-cyclic-fixed-scope) | Original short-return/odd-prime restrictions as comparison only; no all-input saturation or new uniform inverse/cofactor bound is assumed. |
| support | [Exact retained support](Yin_C_G0376_v2.md#irreducible-lehmer-radical-control) | Only the displayed elementary prime-binomial root-product argument, repeated directly below. Its separate degree-only external source bound and large-prime cutoff are not used. |
| dependency | [Exact retained dependency](Yin_C_G0478_v1.md#degree-six-principal-saturation-fixed-scope) | P6 actual polynomial/unit/nontorsion, R_2=64, repeated reduction Phi3 cubed and complete C3=4, used in the full dyadic fiber control. No fresh J39/J40 certificate review is claimed. |
| dependency | [Exact retained dependency](Yin_C_G0243_v1.md#reciprocal-trace-lehmer-control) | Original actual degree-ten Lehmer base with R_2=1024; not a uniform varying-base hypothesis. |
| dependency | [Exact retained dependency](Yin_C_G0251_v1.md#j10-complete-exponent-profile-proof) | Only original Lehmer two distinct degree-five mod-two factors with root order31, at the already retained original coefficient/factor/order native scope. Output was read without a new run or recertification of every original source/program. |
| review | [Actual complete current whole SELF](../audits/reviews/Yin_R_G0692_v1.md#current-minimal-frobenius-whole-finding) | Entire original D69 Sections1--5/equations(1)--(17), every monic actual-degree irreducible nontorsion unit/every rational prime p/exact v_p Res(P,P^[p])=d/other prime factors allowed/no reciprocity needed, actual O=Z[alpha]/every n>=1 prime to p/entire finite p-primary cyclic and cyclotomic rings/reduced squarefree gcds despite repeated Pbar/zero-ring case/exact valuations and root-order formulas/no global p-division or other-prime control, integral Frobenius defect/full determinant orientation/arbitrary-reduction gcd criterion/explicit square-zero idempotent lift including p2/sigma and its fixed lift/unit complementary component/full quotient modulo p2/entire Smith p-primary group, same-field pth-root exclusion/integrality/degree equality/common reduced-root period/two nonzero norm factors/both determinant nullities/prime-binomial proof including p2, every positive q complete signed resultant preservation with all fibers/multiplicities and p-divisible q/no false powered composition/all k>=0 actual irreducible p-power lifts/constant positive total Mahler measure/repeated reduction/all prime-to-p local income, complete all-q all-n cyclic norm fiber identity/every 0<=j<=k delayed valuation/necessary exponent inequality/common-period linear peaks/base-dependent cost, exact degree-six and original Lehmer dyadic control families/full P6 norm versus local Lehmer valuation/actual reduced factors and orders/no new native run, all original contribution/source/fixed-measure/near-one/inverse/cofactor/uncontrolled-other-prime boundaries. Actual current whole relationship is self-reviewed; original entire whole UNKNOWN and exact listed author SELF remain separate. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:06 |
| status | proved |
| reason | Adopt the actual fresh whole independent finding after directly reading the entire R697, its exact fixed Statement/Argument coverage, real initial and post-comparison sequence, all source/native/negative limits and disclosed repeated-scope exposure. Preserve original whole UNKNOWN, original author SELF, prior current whole SELF and every actual date, accepted input and unrestricted boundary. No historical independence is backfilled and no Task/E resumes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original D69 Sections1--5/equations(1)--(17), every monic actual-degree irreducible nontorsion unit/every rational prime p/exact v_p Res(P,P^[p])=d/other prime factors allowed/no reciprocity needed, actual O=Z[alpha]/every n>=1 prime to p/entire finite p-primary cyclic and cyclotomic rings/reduced squarefree gcds despite repeated Pbar/zero-ring case/exact valuations and root-order formulas/no global p-division or other-prime control, integral Frobenius defect/full determinant orientation/arbitrary-reduction gcd criterion/explicit square-zero idempotent lift including p2/sigma and its fixed lift/unit complementary component/full quotient modulo p2/entire Smith p-primary group, same-field pth-root exclusion/integrality/degree equality/common reduced-root period/two nonzero norm factors/both determinant nullities/prime-binomial proof including p2, every positive q complete signed resultant preservation with all fibers/multiplicities and p-divisible q/no false powered composition/all k>=0 actual irreducible p-power lifts/constant positive total Mahler measure/repeated reduction/all prime-to-p local income, complete all-q all-n cyclic norm fiber identity/every 0<=j<=k delayed valuation/necessary exponent inequality/common-period linear peaks/base-dependent cost, exact degree-six and original Lehmer dyadic control families/full P6 norm versus local Lehmer valuation/actual reduced factors and orders/no new native run, all original contribution/source/fixed-measure/near-one/inverse/cofactor/uncontrolled-other-prime boundaries. |
| argument | [Exact argument](#argument) | Entire original D69 Sections1--5/equations(1)--(17), every monic actual-degree irreducible nontorsion unit/every rational prime p/exact v_p Res(P,P^[p])=d/other prime factors allowed/no reciprocity needed, actual O=Z[alpha]/every n>=1 prime to p/entire finite p-primary cyclic and cyclotomic rings/reduced squarefree gcds despite repeated Pbar/zero-ring case/exact valuations and root-order formulas/no global p-division or other-prime control, integral Frobenius defect/full determinant orientation/arbitrary-reduction gcd criterion/explicit square-zero idempotent lift including p2/sigma and its fixed lift/unit complementary component/full quotient modulo p2/entire Smith p-primary group, same-field pth-root exclusion/integrality/degree equality/common reduced-root period/two nonzero norm factors/both determinant nullities/prime-binomial proof including p2, every positive q complete signed resultant preservation with all fibers/multiplicities and p-divisible q/no false powered composition/all k>=0 actual irreducible p-power lifts/constant positive total Mahler measure/repeated reduction/all prime-to-p local income, complete all-q all-n cyclic norm fiber identity/every 0<=j<=k delayed valuation/necessary exponent inequality/common-period linear peaks/base-dependent cost, exact degree-six and original Lehmer dyadic control families/full P6 norm versus local Lehmer valuation/actual reduced factors and orders/no new native run, all original contribution/source/fixed-measure/near-one/inverse/cofactor/uncontrolled-other-prime boundaries. |
| dependency | [Exact dependency](Yin_C_G0237_v1.md#base-prime-power-extra-valuation) | Actual O=Z[alpha], full p^d normalization, arbitrary-reduction invertibility/gcd and first-lifting criterion. The new prime-to-p entire quotient is proved directly below. |
| support | [Exact support](Yin_C_G0265_v1.md#old-layer-exception-threshold) | Comparison of distinct-factor initial depth with original-root multiplicities in later stable layers; no later-layer estimate is silently imported into the new initial quotient. |
| support | [Exact support](Yin_C_G0473_v1.md#saturated-short-cyclic-fixed-scope) | Original short-return/odd-prime restrictions as comparison only; no all-input saturation or new uniform inverse/cofactor bound is assumed. |
| support | [Exact support](Yin_C_G0376_v2.md#irreducible-lehmer-radical-control) | Only the displayed elementary prime-binomial root-product argument, repeated directly below. Its separate degree-only external source bound and large-prime cutoff are not used. |
| dependency | [Exact dependency](Yin_C_G0478_v1.md#degree-six-principal-saturation-fixed-scope) | P6 actual polynomial/unit/nontorsion, R_2=64, repeated reduction Phi3 cubed and complete C3=4, used in the full dyadic fiber control. No fresh J39/J40 certificate review is claimed. |
| dependency | [Exact dependency](Yin_C_G0243_v1.md#reciprocal-trace-lehmer-control) | Original actual degree-ten Lehmer base with R_2=1024; not a uniform varying-base hypothesis. |
| dependency | [Exact dependency](Yin_C_G0251_v1.md#j10-complete-exponent-profile-proof) | Only original Lehmer two distinct degree-five mod-two factors with root order31, at the already retained original coefficient/factor/order native scope. Output was read without a new run or recertification of every original source/program. |
| review | [Exact review](../audits/reviews/Yin_R_G0697_v1.md#c485-whole-independent-finding) | Entire original D69 Sections1--5/equations(1)--(17), every monic actual-degree irreducible nontorsion unit/every rational prime p/exact v_p Res(P,P^[p])=d/other prime factors allowed/no reciprocity needed, actual O=Z[alpha]/every n>=1 prime to p/entire finite p-primary cyclic and cyclotomic rings/reduced squarefree gcds despite repeated Pbar/zero-ring case/exact valuations and root-order formulas/no global p-division or other-prime control, integral Frobenius defect/full determinant orientation/arbitrary-reduction gcd criterion/explicit square-zero idempotent lift including p2/sigma and its fixed lift/unit complementary component/full quotient modulo p2/entire Smith p-primary group, same-field pth-root exclusion/integrality/degree equality/common reduced-root period/two nonzero norm factors/both determinant nullities/prime-binomial proof including p2, every positive q complete signed resultant preservation with all fibers/multiplicities and p-divisible q/no false powered composition/all k>=0 actual irreducible p-power lifts/constant positive total Mahler measure/repeated reduction/all prime-to-p local income, complete all-q all-n cyclic norm fiber identity/every 0<=j<=k delayed valuation/necessary exponent inequality/common-period linear peaks/base-dependent cost, exact degree-six and original Lehmer dyadic control families/full P6 norm versus local Lehmer valuation/actual reduced factors and orders/no new native run, all original contribution/source/fixed-measure/near-one/inverse/cofactor/uncontrolled-other-prime boundaries. New current whole relationship is independently reviewed; original entire whole UNKNOWN and exact listed author SELF remain separate. |

## Complete retained argument

<a id="argument"></a>
<a id="retained-minimal-frobenius-proof"></a>
<a id="minimal-frobenius-fixed-scope"></a>

<a id="minimal-frobenius-cyclic-quotients"></a>
### 1. A local condition and its complete prime-to-p consequences

Let P in Z[t] be the monic irreducible polynomial of a nontorsion algebraic unit alpha, of actual degree d.
Let p be any rational prime.
Retain all conjugate multiplicities in P^[p], and write

    R_p=Res(P,P^[p]),
    C_n=|Norm(alpha^n-1)|,
    D_n=|Norm(Phi_n(alpha))|.

Assume exactly

    v_p(R_p)=d.                                              (1)

Thus the p-part of the full Frobenius resultant is minimal; surplus at other primes is allowed.
In particular the entire saturated doubling class of L194 satisfies(1) with p=2.
Reciprocity is not needed for Sections1-5.
No theorem asserts(1), or full saturation, for every sufficiently near-one input.

For every n>=1 with p not dividing n, put

    g_n=gcd(P mod p,t^n-1) in F_p[t],
    h_n=gcd(P mod p,Phi_n mod p).

Both gcds are monic and squarefree, regardless of multiplicities in P mod p.
The new claim is the exact ring structure

    (O/(alpha^n-1)O)_(p) isomorphic to F_p[t]/g_n,
    (O/Phi_n(alpha)O)_(p) isomorphic to F_p[t]/h_n,            (2)
    v_p(C_n)=deg g_n,          v_p(D_n)=deg h_n,

where O=Z[alpha] and the subscript(p) means its finite p-primary ring, equivalently tensoring the finite quotient with Z_(p).
These p-primary groups are killed by p and are products of finite fields.
A gcd equal to1 gives the zero ring.
The other prime parts of the complete quotient and norm remain present and uncontrolled; (2) does not say that the full quotient is killed by p, or that p/(alpha^n-1) belongs to O globally.

#### Reuse and exact algebraic input

The local screen read [C237's complete normalized Frobenius quotient and first-lifting criterion](Yin_C_G0237_v1.md#base-prime-power-extra-valuation), [C265's complete local cyclotomic layers](Yin_C_G0265_v1.md#old-layer-exception-threshold), [C473's complete short-return and odd-prime restrictions](Yin_C_G0473_v1.md#saturated-short-cyclic-fixed-scope), and the actual controls in L200 and J10.
The prime-binomial root-product argument below is reused from [C376's complete elementary prime-binomial argument](Yin_C_G0376_v2.md#irreducible-lehmer-radical-control); its earlier accepted degree-only source bound is not used here.
The construction below proves its finite-ring lifting step directly and adopts no new p-adic or external source theorem.
A bounded local screen found no matching all-prime-to-p quotient or p-power radical conclusion; no literature-priority claim is made.

Define the integral Frobenius defect

    E_p(t)=[P(t^p)-P(t)^p]/p.                                (3)

Coefficientwise Frobenius proves integrality.
At alpha, E_p(alpha)=P(alpha^p)/p.
The complete powered polynomial gives

    Norm(P(alpha^p))=Res(P^[p],P)=(-1)^(d^2) R_p.

Consequently multiplication by E_p(alpha) in the actual monic power basis of O has determinant with p-valuation zero under(1).
Its reduction is invertible on F_p[t]/Pbar, so

    gcd(Pbar,E_p mod p)=1.                                  (4)

This uses only a unit modulo p, not a unit of O at every prime.
Equation(4) is the normalized Frobenius criterion already present in L63; the new use is on prime-to-p cyclic quotients.

### 2. Elementary proof of the entire quotient, including bad reduction

First take N(t)=t^n-1, p not dividing n, and work in the finite free ring

    A=(Z/p^2 Z)[t]/N(t).

The substitution sigma:t -> t^p is an automorphism: choose an inverse exponent modulo n.
Reduction modulo p is the ordinary Frobenius automorphism on

    Abar=F_p[t]/N,

a product of finite fields because N'=n t^(n-1) is coprime to N.
Let ebar be its idempotent equal to1 precisely on the factors where Pbar vanishes, and zero on all other factors.
Its component ring ebar Abar is F_p[t]/g_n.

Every idempotent of Abar has a unique idempotent lift e to A.
Here is the elementary square-zero argument.
Lift ebar arbitrarily to e_0.
Correct it by p u.
The idempotence equation modulo p^2 is

    (e_0^2-e_0)/p+(2 e_0-1)u=0 modulo p.

The coefficient 2 ebar-1 has square1 and is invertible.
This determines u uniquely modulo p and gives the required lift.
The ring A is free over Z/p^2, so the division of the known multiple of p and the correction modulo p are well defined.
Since sigma reduces to Frobenius and fixes every idempotent of Abar, uniqueness gives sigma(e)=e.

On eA, one has eP in p eA, so eP^p=(eP)^p=0 modulo p^2.
The identity(3) in A therefore gives

    e sigma(P)=p e E_p,
    eP=p sigma^(-1)(e E_p).                                (5)

By(4), e E_p is a unit of eA modulo p, hence a unit of eA: an inverse modulo p lifts by the finite geometric correction for the square-zero ideal p eA.
Equation(5) shows that the ideal generated by eP is exactly p eA.
On (1-e)A, P is already a unit modulo p and thus is a unit in that component.
It follows that

    A/(P) isomorphic to eA/p eA
                      isomorphic to F_p[t]/g_n.             (6)

Now let C=Z[t]/(P,N), which is finite because P is nontorsion.
Its reduction C/p^2 C is exactly(6).
If its finite p-primary additive group had a Smith factor divisible by p^2, then C/p^2 C would have an element of additive order p^2.
Equation(6) rules this out.
Thus the p-primary part of C is killed by p, and reduction modulo p identifies it, as a ring, with C/pC=F_p[t]/g_n.
This proves the first statement of(2), not just a lower bound from mod-p nullity.

For the second statement use N=Phi_n.
It remains a squarefree divisor of t^n-1 modulo p, and t -> t^p is an automorphism of Z[t]/Phi_n when p is coprime to n, with the inverse exponent modulo n.
The same proof applies verbatim, giving the second ring and valuation formulas.
No squarefree reduction of P, discriminant restriction, maximal-order assertion or preservation of degree under alpha -> alpha^p is used.

Equivalently, factor the reduction into distinct irreducibles as

    Pbar=product_phi phi^(e_phi),

and let r_phi be the multiplicative order of a root of phi.
The unit constant coefficient ensures r_phi is defined and prime to p.
The exact formulas become

    v_p(C_n)=sum_(r_phi divides n) deg phi,
    v_p(D_n)=sum_(r_phi=n) deg phi,       p not dividing n.    (7)

The exponents e_phi do not appear.
This is actual initial local depth, including repeated reduction, rather than the original-root multiplicity count used for later stable layers in L78.

<a id="minimal-frobenius-p-power-irreducibility"></a>
### 3. Minimal Frobenius valuation excludes a pth root in the same field

Under(1), alpha is not a pth power in K=Q(alpha).
Suppose instead alpha=gamma^p with gamma in K.
Both gamma and its inverse are integral by the monic equations over the algebraic integers, so gamma is a nontorsion algebraic unit.
Also Q(gamma)=K.
If G is its actual monic minimal polynomial, deg G=d and its complete pth-powered polynomial is P.
Thus

    G mod p=P mod p,

by coefficientwise Frobenius on the elementary symmetric functions of the conjugates.

Choose n prime to p divisible by every reduced root order r_phi, and put

    r=deg rad(Pbar)>=1.

By(2), v_p(C_n(alpha))=r.
On the other hand

    alpha^n-1=(gamma^n-1) S_p(gamma^n),
    S_p(y)=1+y+...+y^(p-1).

Both factors are nonzero.
For any integral multiplication matrix, the p-valuation of its nonzero determinant is at least its nullity modulo p, as follows directly from integer Smith normal form.
Multiplication by a polynomial h in F_p[t]/Gbar has nullity deg gcd(Gbar,h): writing Gbar=g G_1 and h=g h_1 with coprime G_1,h_1 proves this even with repeated factors.

For h=t^n-1 that degree is exactly r.
For h=S_p(t^n), use

    S_p(t^n)=(t^n-1)^(p-1) modulo p,

whose gcd with Gbar has degree at least r.
Norm multiplicativity consequently gives

    v_p(C_n(alpha))
       =v_p(Norm(gamma^n-1))+v_p(Norm(S_p(gamma^n)))
       >=2r,

contradicting the exact value r.
This rules out the pth root without any external lower bound for Mahler measure or any good-reduction assumption.

The elementary prime-binomial argument now proves X^p-alpha irreducible over K.
A proper monic factor of degree1<=a<p would give the product c of its selected roots in K with c^p=alpha^a.
Choosing integers u,v with au+pv=1 would give (c^u alpha^v)^p=alpha, contrary to the preceding result.
If beta^p=alpha, the tower K subset Q(beta) therefore has degree p, and

    P(t^p) is irreducible of degree dp.                      (8)

### 4. All p-power lifts are actual inputs with the same total measure

For any positive integer q, put F(t)=P(t^q).
Even when F has not yet been proved irreducible, full root-fiber evaluation gives

    Res(F,F^[p])=R_p^q,                                     (9)

where F^[p] denotes the complete pth-powered polynomial of F, with every multiplicity.
To avoid assuming a false composition formula when p divides q, compute first the norm product

    product_(beta^q=alpha_i, all i) P((beta^p)^q)
       =[product_i P(alpha_i^p)]^q.

Each factor is repeated q times.
Converting each side from Res(F^[p],F) to Res(F,F^[p]) has total sign exponent d^2(q^2+q), which is even.
This proves the signed identity(9).
It does not assert F^[p]=P^[p](t^q) when p divides q.

In particular its p-valuation is dq under(1).
Combining this preservation with(8) inductively proves

    F_k(t)=P(t^(p^k)) is irreducible of degree d p^k
    for every integer k>=0.                                (10)

It remains a nontorsion algebraic unit; if the base is reciprocal so is each F_k.
Root-fiber grouping also proves M(F_k)=M(P).
The total positive logarithmic measure is fixed along this family, while its p-power reduction is

    F_k mod p=Pbar^(p^k).

Thus (7) gives, simultaneously for every n prime to p,

    v_p(C_n(F_k))=deg gcd(Pbar,t^n-1)<=r,                    (11)

independently of k, even as the actual degree d p^k grows.
This is an exact all-prime-to-p income limitation.
It is distinct from L194's already retained fixed-base odd-lift bounded primitive auxiliary/cofactor cost; no new assertion about that cost is made here.

<a id="p-power-delayed-cyclic-income"></a>
### 5. Exact movement of local income into p-divisible exponents

For a monic polynomial F, write C_n(F) for the absolute product of beta^n-1 over all roots beta of F with multiplicity.
This agrees with the actual field norm when F is irreducible.
For any radical polynomial F(t)=P(t^q), the same full fiber argument gives

    C_n(F)=C_(n/g)(P)^g,             g=gcd(n,q).              (12)

Indeed the nth powers in one qth-root fiber consist of the q/g roots of t^(q/g)-alpha_i^(n/g), each repeated g times.
Evaluating their product against1 gives the claimed absolute norm after multiplying all original fibers.
This proof retains repeated powered roots and needs no within-level degree preservation.

For q=p^k and n=p^j u with p not dividing u, (12) implies, throughout0<=j<=k,

    v_p(C_(p^j u)(F_k))
       =p^j deg gcd(Pbar,t^u-1).                            (13)

Consequently linear p-income A_p(n)=v_p(C_n)log p of at least eta*d p^k, at an exponent with j<=k, requires

    p^(k-j)<=r log p/(eta d).                               (14)

A fixed eta>0 therefore forces v_p(n) to be within a bounded distance of k, or larger than k.
Prime-to-p exponents cannot supply that income along these actual families.
This identifies where the mass is delayed; it does not say that no affordable p-divisible exponent exists.

In fact choose u_0 to be a common reduced-root period.
Then

    v_p(C_(p^k u_0)(F_k))=p^k r,
    (p^k u_0)/(deg F_k)=u_0/d.                              (15)

This is a genuine same-exponent linear local income along each fixed base, with a base-dependent exponent cost.
The order u_0 and the ratio r/d are not controlled uniformly over varying near-one bases.
Neither(15) nor the root-order formula supplies the missing unrestricted L168 coverage.

#### Two actual controls with different repeated reductions

For the [C478 degree-six input](Yin_C_G0478_v1.md#degree-six-principal-saturation-fixed-scope), p=2, P=t^6-t^5-t^3-t+1 and R_2=2^6.
Its reduction is Phi_3^3.
Equations(10)--(13) give actual irreducibility and saturation of every P(t^(2^k)), degree6*2^k, and

    v_2(C_n)=2 if3 divides n, and0 otherwise, for every odd n;
    C_(3*2^k)(P(t^(2^k)))=4^(2^k).                         (16)

The second equality is the complete norm, since L200 gives C_3(P)=4 and(12) gives the whole product.
At that exponent n=(deg F_k)/2 its logarithm is(deg F_k)log2/3.
At all odd exponents the dyadic income is at most2 log2; possible odd-prime income at larger odd exponents is not bounded here.
These statements include highly repeated reduction and actual irreducibility, not cyclotomic padding.

For the original Lehmer base, L66 gives R_2=2^10.
The retained exact [C251 complete retained J10 factor/order proof](Yin_C_G0251_v1.md#j10-complete-exponent-profile-proof) has two distinct degree-five factors modulo2, both with root order31.
The new theorem, reusing those already verified finite facts without a new run, gives irreducibility of every dyadic lift, degree10*2^k, and

    v_2(C_n)=10 if31 divides n, and0 otherwise, for odd n;
    v_2(C_(31*2^k))=10*2^k.                                 (17)

This reaches local income(deg F_k)log2 at exponent31/10 times the degree on this fixed base.
It does not need L159's degree-only source bound or a large-prime cutoff.
Both control families keep their fixed positive base measure; the dyadic lifts generally have many expanding roots and are not asserted Salem or near-one sequences.

## Original contribution, author checks and remaining arithmetic obligation

The assigned resultant_research AI developed the new Sections1--5 deductions, with the exact original1152-character contribution/fixed-reuse/listed-check/then-pending account retained as SELF in R101.
The coordinator supplied a broad question and actually received interim findings; the prior mathematical contents and initial reconstruction order remain unestablished, so the original entire R101 whole remains UNKNOWN.
Its earlier L194/L200 contributions remain fixed dependency history, not automatically authorship of this target.
The original7249-character81-line whole review, day precision, verdict, unchanged-author-text assertion, actual input reading and all source/native limits remain fixed.
The original J10 readme and exact coefficient/factor/order outputs were read; no native program is rerun and no new source-proof equivalence is asserted.
Current authored whole SELF does not close the old whole UNKNOWN or invent an additional historical whole author review.

The changed arithmetic result is that minimal Frobenius valuation determines every prime-to-p initial cyclic and cyclotomic layer exactly, including bad reduction, and forces all p-power radical lifts to be genuine irreducible inputs.
The actual lift controls show how growing repeated reduction suppresses all prime-to-p local income while allowing a precisely located linear peak at p-divisible exponents.
They disprove neither a near-one gap nor a uniform estimate essentially using total m tending to zero.
The next useful arithmetic step must control reduced-root periods and radical degree, or the later p-power layers, uniformly as both degree and total measure vary.
The full inverse and complementary auxiliary cost are still uncontrolled on that varying-input domain, and no result puts all near-one inputs under(1).

These original arithmetic limitations remain current.
Historical active-Task/pending-review prose stays at L202 as chronology and selects no research execution here.
No new source/PDF inspection, acquisition, program/J, numerical/native run or research Task/E occurs.
