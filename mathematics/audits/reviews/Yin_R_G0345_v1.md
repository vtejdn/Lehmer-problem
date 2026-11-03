---
author: Yin
---

# Whole review of nested divisor slices, rectangular means and arithmetic cancellation

Date: 2026-10-14T20:08.
Human record author Yin.
The separately assigned strategy_critique reviewer examined the ENTIRE ACTUAL fixed C108 v1, reported the auxiliary-cutoff domain defect below, and then read the ENTIRE ACTUAL corrected C108 v2, dated 04:04, together with its actual difference from v1.
Root authored the opening two-slice relaxation; g_bridge_audit authored the subsequent constructions and analytic proofs.
This reviewer did not supply those proofs or edit either target.
Shared research context, author summaries, the fixed arguments and root's response to the domain finding were available; this is a non-blind, separately organized whole review.

The reviewer identified and recommended explicitly integer H and H_j.
Root verified the integer integral comparison and implemented the correction in the new physical version, preserving v1.
This actual involvement is disclosed: the v2 finding is not represented as an untouched proof requiring no correction, nor as an independent discovery of the author's arguments.
Checking a proposed guard after reporting a defect did not supply a new theorem or replacement proof.
The two exact physical versions have separate findings and bindings below.
Root retains responsibility for acceptance and navigation.
The initial shared author-summary context is not specified sufficiently to establish the v1 reviewer's isolation, so the v1 domain finding has an unknown relationship.
For v2, the reviewer supplied the necessary integer-cutoff restriction absent from v1's explicitly unrestricted real-H assertion.
That contribution repairs the auxiliary mathematical domain even though A--C and the later real rectangular cutoffs remain unchanged; the v2 whole finding is therefore self-reviewed, rather than independent of its own repair.
The actual complete v2 rereading remains recorded, but an independent re-review of the repaired equation 8, integer H/H_j choices and the affected overshoot, r/y^2 and correlation/mass-limit chain remains due, with adequate coverage of the whole selected proof.
The original dates, two physical inputs, negative/pass distinction, mathematical checks and exact binding scopes remain unchanged, with no new review performed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original v1 domain finding](#nested-slice-v1-cutoff-domain-finding) | unknown |
| [Corrected v2 whole finding](#nested-slice-v2-whole-independent-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original v1 domain finding](#nested-slice-v1-cutoff-domain-finding) | [Exact v1 statement](../../claims/Yin_C_G0108_v1.md#nested-slice-continuation-statement) | Whole A--C statement examined; the auxiliary-domain error does not refute those conclusions. |
| [Original v1 domain finding](#nested-slice-v1-cutoff-domain-finding) | [Whole v1 argument](../../claims/Yin_C_G0108_v1.md#nested-slice-complete-argument) | Entire root and delegated argument, equations 1--21, all five sections, constructions, limit orders, constants, restrictions and source boundaries read; precise correction required in Section 1. |
| [Original v1 domain finding](#nested-slice-v1-cutoff-domain-finding) | [v1 affected construction](../../claims/Yin_C_G0108_v1.md#proper-divisor-cauchy-saturation) | Equation 8 integral tail estimate with unrestricted real H, propagated to H_j; explicit failure and sufficient integer-domain repair below. |
| [Original v1 domain finding](#nested-slice-v1-cutoff-domain-finding) | [C104 kernel and product argument](../../claims/Yin_C_G0104_v1.md#product-fractional-moment-argument) | Exact finite PSD lcm kernel, full-divisor squarefree factor, convergent sharp product constants and their product-profile scope. |
| [Original v1 domain finding](#nested-slice-v1-cutoff-domain-finding) | [L17 retained prime divergence](../../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Elementary reciprocal-prime divergence and its recorded attribution only; no use of the discriminant-family theorem. |
| [Corrected v2 whole finding](#nested-slice-v2-whole-independent-finding) | [Exact v2 statement](../../claims/Yin_C_G0108_v2.md#nested-slice-continuation-statement) | Complete A--C: mass-only stability obstruction, actual equal-constant local saturation, exact excluded-prime deficit cancellation and all nonclaims. |
| [Corrected v2 whole finding](#nested-slice-v2-whole-independent-finding) | [Whole v2 argument](../../claims/Yin_C_G0108_v2.md#nested-slice-complete-argument) | Entire actual corrected root and delegated argument, equations 1--21, all five sections, finite constructions, constants, limit interchanges, source and correction accounts. |
| [Corrected v2 whole finding](#nested-slice-v2-whole-independent-finding) | [Corrected finite nested construction](../../claims/Yin_C_G0108_v2.md#proper-divisor-cauchy-saturation) | Exact deletion identities, diagonal corrections, integer H/H_j, shortest prime-product overshoot, vanishing mass and energy imbalance. |
| [Corrected v2 whole finding](#nested-slice-v2-whole-independent-finding) | [Rectangular convolution](../../claims/Yin_C_G0108_v2.md#rectangular-fractional-convolution) | Finite triple expansion, absolute Euler majorant, independently diverging cutoffs, signed local factors, totient mass and positive R_s. |
| [Corrected v2 whole finding](#nested-slice-v2-whole-independent-finding) | [Prime-free coupled constants](../../claims/Yin_C_G0108_v2.md#prime-free-coupled-constants) | Fixed-p weighted multiples, both local factor removals, exact normalized slice constant and genuine finite ideal realization. |
| [Corrected v2 whole finding](#nested-slice-v2-whole-independent-finding) | [Deficit cancellation](../../claims/Yin_C_G0108_v2.md#excluded-prime-deficit-cancellation) | Both first-order terms and summable remainder, fixed-p-first limit and existence-only diagonal finite choices. |
| [Corrected v2 whole finding](#nested-slice-v2-whole-independent-finding) | [Strict half-moment comparison](../../claims/Yin_C_G0108_v2.md#interval-energy-not-global-extremum) | Strict local products, scalar factor, elementary zeta lower bound and precise separation from global extremality. |
| [Corrected v2 whole finding](#nested-slice-v2-whole-independent-finding) | [C104 kernel and product argument](../../claims/Yin_C_G0104_v1.md#product-fractional-moment-argument) | Actual finite Gram construction and Cauchy interface, exact squarefree full-capacity factors, convergent K_s and sharpness in the product class. |
| [Corrected v2 whole finding](#nested-slice-v2-whole-independent-finding) | [L17 retained prime divergence](../../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Existing elementary Euler-product/harmonic contradiction and attribution at the needed prime-divergence scope only. |

## Original domain objection and its exact effect

In v1, Section 1 states the tail estimate for any cutoff H>=2 without requiring an integer.
For a fixed 1<t<2, let H approach 3 from below.
On 2<H<3 the left side sum_(n>H) n^(-t) is the fixed sum from n=3.
Since x^(-t) is strictly decreasing,

    sum_(n>=3) n^(-t) > integral_3^infinity x^(-t) dx.

The claimed right side H^(1-t)/(t-1) tends to that smaller integral as H approaches 3.
Therefore the asserted comparison fails for some real H<3 arbitrarily close to 3.
This is a genuine quantifier/domain defect in the displayed auxiliary inequality, not merely a stylistic preference.

For an integer H, compare the summand n^(-t), n>=H+1, with the integral over [n-1,n].
Summing gives exactly the stated bound.
Every required construction can freely take such integers, and H_j may be the ceiling of the existing real lower threshold.
Thus the original statement A--C is not refuted.
The correction is to constrain these two auxiliary cutoff variables; it is unnecessary and incorrect to infer an integer restriction on the independent rectangular cutoffs X,Y later in the proof.

The actual v2 difference has precisely those two domain additions, the correction/provenance account, and corresponding organization/initial-assessment wording.
All other mathematical content and A--C are unchanged.
The complete v2 was nevertheless rechecked, rather than accepting a textual difference as whole-proof verification.

## Exact root relaxation and its scope

Write q=p-1.
The p-free condition gives phi(pa)=q phi(a), and the lcm acquires one factor p whenever at least one slice label is multiplied by p.
Consequently W=V0+qV1 and E=E0+2q p^(-s)E01+q^2 p^(-s)E1, with both ordered cross orientations and the complete diagonal.
C104's kernel is genuinely PSD: its finite one-prime vectors have positive telescoping weights d_k, and their tensor products give lcm(a,b)^(-s).
Its Cauchy inequality is therefore applicable to both slice arrays.

Substituting E_i<=C V_i^t and Cauchy gives the displayed F_(p,s)(x).
At x=p^-2 the cross term is 2/p-2/p^2 and the small-slice term is (1-1/p)^2 p^-t.
The denominator is (1+1/p-1/p^2)^t.
Thus p(F-1) tends to 2-t=s.
Elementary reciprocal-prime divergence makes the product of separate relaxed worst-case factors diverge.
This proves failure of that unrestricted scalar recursion alone.
It does not yet supply actual slice realization or refute a larger universal energy bound; the later construction pays its own slice constant.

## Proper-divisor ideals and the corrected cutoff

For full divisors of squarefree N, total weight is N, and the full row at maximal label N has potential N^(1-s).
Deleting its weight phi(N)=cN from one or both arguments gives E0/N^t=1+r, E01/N^t=y+r and E1/N^t=y^2+r, where y=1-c.
The cross term is not confused with deletion from both arguments.
Expanding the numerator of 1-rho^2 yields exactly r(1-y)^2, proving equation 7 with its positive denominator.

C104 supplies the exact squarefree product factor 1+(q^s-1)/q^2, so r>=0 and, for integer H, log(1+r)<=H^(1-t)/(t-1), uniformly in the finite number of chosen primes.
Reciprocal divergence also holds after removing every finite prime set.
It makes the shortest prime product with c<=1-x exist.
Its preceding product exceeds 1-x; multiplying by 1-1/q for q>H gives x<=y<x+(1-x)/H.
There is no distribution-rate premise.

For fixed x, integer H tending to infinity gives y to x and r to 0, hence rho to 1.
For x_j=1/j and integer H_j>=j^(4/(1-s)), the overshoot is o(1/j), log(1+r_j)=O_s(j^-4), and therefore r_j=O_s(j^-4).
This gives r_j/y_j^2 to 0 and equation 10.
The small slice has normalized energy asymptotic to y_j^s, so this family by itself does not match a positive common slice constant.
All finite arrays are full totient integer arrays on divisor ideals.

## Absolute rectangular limit and signed constants

The two identities in equation 11 follow prime by prime, with J_s positive.
After replacing lcm(a,b)^(-s) by gcd(a,b)^s/(ab)^s, expanding phi(a)/a and phi(b)/b yields exactly the finite triple sum 13 with exponent t-1=1-s in the two multiple sums.
For u=X/m, sum_(j<=u)j^(t-1)<=u^t, including u<1, so U_X(m)/X^t<=1/m.
The fixed-m limit is 1/(tm) by the ordinary integral bounds.
Both statements permit real positive X.

The absolute inner sum has a factor 1+q^-2 for q not dividing d, and a factor (1+1/q)/q^e for q^e exactly dividing d.
Hence it is (C_plus/d) times the displayed product.
Summing over all exponents e>=1 gives

    sum_(e>=1) J_s(q^e)/q^(2e)=(q^s-1)/(q^2-q^s).

Squaring the local inner factor yields precisely h_q, with h_q<=9/4.
The majorant's local excess is bounded by (9/4)q^-t/(1-2^-t), summable for t>1.
The nonnegative Euler expansions are monotone and bounded; no conditional rearrangement has entered this absolute-convergence proof.

For any error tolerance, a finite subset of triples leaves a small absolute tail uniformly in both cutoffs.
On this fixed finite subset, both U factors converge as soon as their respective cutoffs exceed a sufficiently large threshold.
The same majorant bounds the remaining terms.
This proves the independently growing rectangular limit without assuming X/Y stays bounded or replacing it with an iterated limit.

In the signed inner sum the prime factors become 1-q^-2 away from d and (1-1/q)/q^e on d.
Dividing by the missing outer factor gives (1+1/q)^(-1), as stated.
Absolute convergence licenses squaring and summing.
Thus M_s=A^2 product B_(q,s), with exactly the positive local B shown in equation 15.
The mass calculation uses mu(k)/k^2 and sum_(j<=u)j/u^2 to 1/2, with an absolutely summable majorant.
Consequently b=A/2 and R_s=(2^t/t^2)A^s product B.
These constants are finite and positive.
Applying the rectangular limit to the cross and both diagonal energies proves rho to 1 even along X=j^2,Y=j, while both normalized energies tend to R_s and their mass ratio tends to 0.

## Fixed-prime exclusion and cancellation

For p not dividing m, excluding multiples of p subtracts p^(t-1) times the sum through X/(mp), so U_X^(p)(m)/X^t tends to (1-1/p)/(tm).
If p divides m the restricted multiple sum vanishes.
It remains dominated by the previous multiple sum.
Therefore the same absolute triple proof applies with d,k,l all prime to p.

Removing p's local factor from M_s removes (1-p^-2)^2 B_(p,s); the two weighted-density factors contribute (1-1/p)^2.
The analogous mass factor is b/(1+1/p).
Dividing the energy by the t-th power of the mass constant gives exactly R_(s,p)=R_s/[(1+1/p)^s B_(p,s)], including the exponent s=2-t.
There is no missing local totient or density factor.

For each fixed p, the two p-free initial segments through T and T/p are nonempty nested divisor ideals once T>=p.
Their common finite prime pool excludes p; their union with p times the second slice is exactly the integers through T with v_p<=1.
Both cutoffs diverge with T, giving mass ratio p^-2, matched slice constants R_(s,p), and rho to 1.
Substitution into the exact two-slice identity proves actual local saturation at that constant, not at an asserted unknown global optimum.

B_(p,s)=1+O_s(p^-t); bounded Taylor remainders give R_(s,p)/R_s=1-s/p+O_s(p^-t).
The exact numerator and denominator of F give 1+s/p+O_s(p^-t).
Because 1<t<2, all p^-2 remainder terms fit within p^-t.
Their product is 1+O_s(p^-t), a summable local error.
These are fixed-s estimates.
The ideal limits occur first with p fixed; only afterward does p grow.
For each p, sufficiently large integer T(p) can make the finitely many displayed ratios AND the union energy as close as p^-3 to their limits.
This is an existence-only diagonal choice from the established fixed-p limits, with neither an effective rate nor an illicit uniform interchange.

## Strict half-moment comparison and dependencies

At s=1/2, C104 gives K_q=(1-q^-2)/(1-q^-3/2), and K_q-1=(q^s-1)/(q^2-q^s)>0.
Therefore B_q=1+(K_q-1)/(1+1/q)^2<K_q.
Both products converge; their strict comparison is already enforced by the factor at q=2.
The square of the remaining scalar (2^t/t^2)A^s is 128/[81 zeta(2)].
The strictly decreasing integral comparison gives zeta(2)>19/12>128/81, so this scalar is less than 1.
It follows that R_(1/2)<K_(1/2).
C104's finite full-capacity product profiles approach K, proving the exact asserted failure of global extremality within even that comparison class.

The complete needed C104 interfaces were inspected: finite Gram/Cauchy, exact squarefree factors, convergent product constant, and sharpness by first increasing finite exponent caps then prime pools.
No claim for arbitrary correlated ideals was imported.
L17's Euler-product/harmonic contradiction supplies the needed prime divergence and records its classical attribution; neither its discriminant-family claim nor a prime number theorem is needed.
The finite Euler expansions at exponent 2 also directly establish A=1/zeta(2), so C105's numerical witness and extremal theorem play no logical role.
Their historical mentions are not hidden dependencies.

## Source inspection and review limits

The reviewer directly read the primary journal PDF of Noboru Ushiroya, *Mean-Value Theorems for Multiplicative Arithmetic Functions of Several Variables*, INTEGERS 12 (2012), A33, at [Theorem 1 and its proof, printed pp. 3--4](https://math.colgate.edu/~integers/m33/m33.pdf).
It states the multivariable Wintner mean under absolute convergence of the divided convolution and uses finite divisor expansion plus a controlled tail.
This supports the recorded attribution of the METHOD.
The author's additional inspection of Theorem 4 on p. 5 remains the author's account; this reviewer does not claim independently reading that passage or the full paper.
No theorem from the contextual arXiv survey is used.
The actual weighted triple majorant, all local factors and every limit required here are supplied and checked locally, so no unverified source theorem fills a gap.
No source-original proof expansion, literature-wide novelty conclusion, source registration, native mathematical program or formal proof is claimed.

Historical future-tense and opening unresolved-obligation prose is explicitly reconciled by the later statement and continuation.
The whole artifact retains useful failed routes and does not silently turn a proposed mechanism into a general conclusion.
Neither a universal weak moment bound, nor an unbounded-energy family, fixed-positive-triple-density/no-capture example, actual Frobenius inventory or near-one Mahler sequence is proved.
In particular, neither local Cauchy saturation nor summable cancellation on this one family answers the remaining near-global-extremal inverse problem or completes G0001.

<a id="nested-slice-v1-cutoff-domain-finding"></a>

## Actual v1 whole-review finding: changes required in the auxiliary cutoff domain

CHANGES REQUIRED for the exact v1 auxiliary estimate quantified over unrestricted real H>=2, and the corresponding H_j choice.
The explicit H approaching 3 from below counterexample identifies the failed displayed implication.
Whole inspection found the other arguments consistent at their stated scope, and the main A--C conclusions are not refuted: all uses permit integer cutoffs.
This finding applies to the preserved physical v1 and is not erased by the corrected successor.

<a id="nested-slice-v2-whole-independent-finding"></a>

## Actual corrected v2 whole finding: pass

PASS for the ENTIRE ACTUAL C108 v2 statement, argument and selected input interfaces after the disclosed integer H/H_j correction.
The actual v2 was read in full and every substantive chain reconstructed above, including absolute triple convergence, independently growing rectangular cutoffs, signed local factors, fixed-p-first limits, finite realization, exact first-order cancellation and strict half-moment comparison.
The correction resolves the precise v1 domain objection without changing A--C or the real rectangular cutoffs.
This is bounded project review with the self-reviewed relationship and independent re-review obligation disclosed above, not source-wide certification, acceptance by itself, or completion of the unrestricted Task.
Root owns the adopting decision.
