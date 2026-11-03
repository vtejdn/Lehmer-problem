---
author: Yin
---

# Retained project review: Complete polynomial return moments and the information cost of excursion conditioning

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0198_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="complete-return-moment-independent-review"></a>

### Complete separate noncontributor review

On 2026-10-10 the assigned resultant_research AI for Yin independently read and checked the entire present proof, Sections1-5 and equations(1)--(10), including all infinite sums, torsion/general-unit domains, actual core paths and probability-law distinctions.
The reviewer supplied none of D66's new higher-moment summation, general occupation proof, Green-entry extension, neutral moments or information-rate derivation.
It had previously authored the retained L192 excursion-conditioned construction and related hitting arguments, which are explicitly reused dependencies here; it does not claim a fresh independent re-audit of that earlier contribution.
Shared G0001 context and the assigned result were available.
This is a separately organized noncontributor review of the new complete D66 argument and applicability of its fixed interfaces, not a blind, human or formal review.
No mathematical defect or required correction was found.
The preceding author text was preserved unchanged when this finding was appended.

The reviewer read L154's exact first-return convention, degree-based zero segment, complete block Holder proof, central-binomial bound, renewal identity and actual weighted-tail family, as well as L173's autocorrelation maximum-atom interface and L192's earlier excursion law.
The L154 bound uses actual degree-d integral bases of Z[alpha] and therefore applies to torsion and nonreciprocal units as claimed.
Its reuse here does not substitute padded polynomial degree for field degree or introduce a Salem hypothesis.
No original source proof, program or old family classification is newly certified by this review.

For Section1, the absence of nontrivial first returns through time d removes every block with floor(n/d)=0.
Including n=d in the next block only enlarges the bound.
Each block has at most d terms, n^k<=d^k(q+1)^k, and q+1<=(3q+1)/2 for every q>=1.
Thus the full sum is bounded by 2^(-k)d^(k+1) sum_(q>=1)(3q+1)^(-d/2+k).
The sum-to-integral estimate is valid exactly when d/2-k>1.
Its first term and integral give 2^k d^(k+1)2^(-d)[1+8/(3(d-2k-2))], including the stated constants.
The complete k=0 sum is precisely the earlier T_d.
For fixed k its polynomial factor is dominated by2^d, but no estimate uniform in growing k follows.
The same block estimate for p_n makes U finite for d>2 after retaining all finitely many small n.
Nonnegative renewal then gives F<1 and U=1/(1-F), even for cyclotomic inputs.
At d>4, F' is finite and at least1/2.

For Section2, the actual core supplies both a zero-to-x path and a finite co-return for each x.
Prefixing the former to any ambient co-return ensures that all of its intermediate states belong to the core.
Consequently the killed-kernel first-step equations are the true H equations.
They normalize every nonzero Q row, while the zero row has the distinct factor F.
All positive core edges remain positive.
A first-return path has exactly one departure from zero before its terminal hit, so its H ratios telescope and its unique extra factor is1/F.
Its complete Q probability is therefore its original probability divided by F, including the length-one loop.
The full return distribution sums to one and has mean F'/F.
This proves recurrence and finite mean on the countable irreducible core, not merely on a finite approximation.

The occupation expression(4) includes the initial zero and excludes the terminal zero.
Its total mass is exactly F', and its zero numerator is F.
Passing from original returning excursions to Q excursions divides occupation by F and mean length by F, producing the same formula.
Stationarity follows by shifting visits from times0 through tau_+-1 to times1 through tau_+, whose endpoint contributions agree at zero.
Nonnegative sums and finite expected excursion length justify this transition-count argument.
It proves the general-unit formula without any reciprocity or operator-norm Green convergence.
Since F'>=1/2 and F'-F<=sum_(n>=2)n f_n, the stated nonzero stationary-mass estimate2B_(d,1) follows.

In the reciprocal specialization, the field map sigma and T=alpha^(-1)sigma form the asserted additive involution of the actual order.
Reversing an edge replaces its digit by its negative, which has the same original weight; reversing a closed word also preserves D.
This gives K(Ty,Tx)=K(x,y) in the correct transpose orientation.
The full displacement autocorrelation bounds every shifted endpoint atom by p_n, so all Green entries are finite and bounded by U even though no summability in operator norm is assumed.
The first-hit and reversal formulas yield G(x,0)=H(x)U and G(0,x)=UH(Tx).

For the last-zero decomposition, every finite zero-to-x path with x!=0 has a unique last visit to zero.
Its prefix contributes the corresponding return probability and its nonempty suffix avoids zero; Tonelli gives G(0,x)=U V(0,x).
This suffix definition correctly allows paths whose future never returns.
At any such pre-return visit to x, the Markov property multiplies its visit probability by H(x) when one also requires an eventual positive return to zero.
Thus the original returning-excursion occupation is H(x)V(0,x)=H(x)H(Tx), proving(6).
Normalization comes from the already proved finite occupation formula, so no unproved product of critical Green operators is used.
The torsion extension and the absence of a new exponential radial tail are correctly stated.

For Section3, every selected neutral embedding rotates under multiplication by alpha and each digit contributes norm at most sqrt(s).
Propagating the complete closed word forward and backward gives the two bounds sqrt(s)j and sqrt(s)(n-j).
There are n occupation times before the terminal return, so the pathwise kth radius sum is at most (sqrt(s)/2)^k n^(k+1).
The one-step loop contributes zero.
Dividing by F'>=1/2 and using (1) at order k+1 yields exactly(7) with threshold d>2k+4.
Since s<=d/2, the additional dimension factor is only polynomial at each fixed k and the asserted uniform high-degree limit follows.
No separation assumption for nonzero projected lattice radii is needed.

For Section4, the transformed row has at most three positive digit probabilities and each original probability is at least1/4.
Relative entropy is nonnegative and at most log4.
The complete-excursion likelihood ratio is1/F, with all original digit weights retained.
Absolute integrability is justified before changing summation order: sum_eta q|log(q/p)| is at most -sum q log q-sum q log p<=log3+log4 at every row.
Finite Q mean return length then bounds the expected sum of absolute transition log likelihoods.
Excursion occupation converts its expected signed sum -log F into mean length times I, proving I=-(F/F')log F.
The estimate(9) follows by writing log2-I=(1-pi(0))log2+pi(0)log(2F), using(5), F=1/2+a and log(1+2a)<=2a.
In particular I tends to log2, not zero; this relative-entropy rate is not the original collision entropy or Mahler measure.

Finally, Section5 uses precisely L154's actual irreducible family with N=9 modulo120, N>=129 and degree N+3, with theta<M(P_N)<4/3 and fixed positive limiting measure theta.
Its complete original weighted tail at4/3 is at least1/3.
All fixed polynomial return moments and fixed neutral stationary moments nevertheless tend to zero by the independently checked preceding bounds, while pi(0) tends to one and I tends to log2.
These are simultaneous properties of the same actual inputs; each moment order is fixed before degree tends to infinity.
They do not assert that all polynomial moments are finite at one fixed degree, interchange degree and time limits, or infer a near-one sequence from this fixed-positive-limit family.
They establish the stated obstruction to extracting that exponential weighted-tail control from the displayed unweighted moments and conditioned concentration alone, while leaving a smaller universal weight or an additional near-one arithmetic theorem open.

This complete proof-only review used no new source acquisition, numerical run, finite scan, material fingerprint or J.
It supports the full polynomial-moment estimates, the general-unit infinite conditioned-chain and occupation formulas, their reciprocal specialization, all fixed neutral-moment bounds, the exact information identity and the actual-family comparison.
It does not establish original-law recurrence, an infinite critical transform, a uniform positive collision rate, a common weighted-return inequality or completion of G0001.
Fixed retention remains a separate coordinator action.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original whole return-moment and information finding](#complete-return-moment-independent-review) | unknown |
| [Original complete listed author checks](#return-moment-original-author-check-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original whole return-moment and information finding](#complete-return-moment-independent-review) | [Entire original frozen return-moment proof](../../ledger/Yin_L_G0198_v1.md#retained-complete-return-moment-proof) | Actual original2026-10-10day-precision whole: Entire original D66 starting interfaces/Sections1--5/equations(1)--(10): every actual degree-d algebraic unit including torsion and nonreciprocal units with the original iid(1/4,1/2,1/4) law, every integer k>=0 with d>2k+2 and complete infinite B_(d,k) bound/first-return zero segment/full renewal and transience, every d>4 actual possibly infinite core/ambient versus killed co-return/positive H/stochastic zero-row-F excursion transform/exact f_n/F/finite mean/general original returning-excursion occupation and stationarity, reciprocal degree/involution/maximum-atom finite entry Green/first-hit and last-zero proof/full stationary normalization without l2 operator-norm summability, every selected neutral conjugate pair/every fixed k>=1 with d>2k+4/entire closed-word forward-backward radius and stationary moment limit, original-digit relative entropy/absolute-integrability-before-reordering/exact I=-(F/Fprime)logF/uniform high-degree log2 limit and pi0 limit, the same actual irreducible Salem progression/full nonvanishing original4/3 weighted tail/fixed-positive-limit and order-of-limits counterexample, all original-versus-conditioned/source/contribution/noncritical/nonuniform-growing-k/near-one/smaller-weight/Task limits. The earlier L192 contribution is fixed reuse whose original proof is not freshly independently re-audited by this finding. |
| [Original complete listed author checks](#return-moment-original-author-check-finding) | [Original proof and exact author checking account](../../ledger/Yin_L_G0198_v1.md#retained-complete-return-moment-proof) | Actual original2026-10-10day-precision listed self-check: degree restrictions/complete summation/last-zero decomposition/torsion/core paths/original and conditioned laws/reciprocal orientation/moment factors/likelihood telescoping/limit order, with exact contribution/reuse/then-pending account. No extra historical whole author-review event is invented. |

## Exact retained initial-arrangement boundary

All original100lines of the complete whole review, its original day-precision date, verdict, author-text-retention assertion, all inspected scopes and source/nonexecution boundaries remain fixed.
The reviewer supplied none of this target's new derivations and explicitly disclosed its earlier authorship of the fixed L192 excursion-conditioned construction and related hitting arguments.
That dependency contribution is not automatically contribution to the new higher-moment/general-occupation/Green-entry/neutral-moment/information argument.
The recorded shared G0001 context and availability of the assigned result do not retain their actual prior mathematical contents or the complete initial reconstruction sequence.
They establish neither new-target SELF nor initial isolation.
The entire original whole relationship therefore remains UNKNOWN for independent-review purposes.
Its original applicability check and explicit absence of a fresh independent re-audit of L192 remain part of that full scope.
The exact original listed author checks remain separately SELF below.
A current authored whole SELF cannot close the old entire UNKNOWN or create another historical whole author review.
No source-proof audit, source acquisition, numerical/native run, program/J or research Task/E is added.

<a id="return-moment-original-author-check-finding"></a>
## Original complete listed return-moment author checks

Date: 2026-10-10.
The exact original contribution, reuse, listed author-check and then-pending account follows.

The coordinator supplied the higher-moment summation, general-unit excursion/occupation extension, reciprocal formula without operator-norm summability, all neutral moments, exact information-rate identity with its absolute-integrability justification, and the combined actual-family comparison.
L154's rank bound, first-return gap and weighted example and L173's maximum-atom argument are explicit fixed reuse.
L192 supplies the earlier Salem construction and interpretation; no new external theorem, program or finite scan is needed.
Self-check covered degree restrictions, complete summation, last-zero decomposition, torsion cases, actual core paths, original versus conditioned probabilities, reciprocal orientation, moment factors, likelihood telescoping and limit order.
Full separate noncontributor review is pending; G0001 remains active and unresolved.
