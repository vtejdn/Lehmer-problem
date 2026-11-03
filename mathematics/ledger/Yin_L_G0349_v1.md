---
author: Yin
---

# Uniform full companion cost for every growing repeated-cell congruence

Date: 2026-10-10.
The coordinating AI for Yin adopts this restricted result after complete separately organized noncontributor review under the continuing G0001 authorization.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="all-count-cost-fixed-scope"></a>
## Current adopted scope

For the actual complete companion of every L346 selected-cell congruence, uniformly over all0<=s<=k and every subset placement, Mahler measure divided by k tends to log2.
The same is true of the entire literal cover.
The proof treats both exterior recurrence roots and all cycle terms, controls logarithmic negative parts for every root, pays the full(4k+1)log r radial expense and closes all subsequence/radius/count quantifiers.
It covers growing and all-selected counts without reusing fixed-depth coefficient bounds.
No effective convergence threshold, finite-k ordering, whole-class optimum or near-one gap is asserted.
Complete separately organized noncontributor review of the entire proof follows; no new numerical computation was used.

The complete D216 author proof and review follow without abridgment.
Historical pending-review, pending-adoption and stopped-execution handoff sentences are superseded only by this current adoption paragraph.
Heading depths and relative navigation are relocated; all statements, proofs, source boundaries, unsuccessful-test scope and review history are preserved.
G0001 remains active and unresolved.

<a id="complete-retained-proof-and-review"></a>
## Complete retained author proof and independent review

## Growing repeated-cell surgery and complete companion asymptotics

Date: 2026-10-10.
All eight routes remain active; the unrestricted Task is unresolved.

### Assigned question

Continue the open s=s(k) regime of D212, including all-selected s=k.
Seek a complete whole-root or whole-circle asymptotic for the actual complete companion and literal cover, or an exact structural simplification with all factors and costs.
The existing fixed-s coefficient argument cannot be applied with growing depth for free.
A useful quantitative obstruction or a changed actual cost mechanism is valid progress; maintain actual integral congruences and original positive-factor costs.
First reason directly from the complete formula and prior L330/L340/D212, without launching a new bounded search.
Any numerical extension requires a separately coordinated full domain before execution.
Root supplies only this open question.

Develop substantive work here; first inspect exact retained inputs and applicable reuse rules.
Reusable programs and outputs belong in a coordinated J with a declared finite domain before running.
Preserve unsuccessful implications, uncertainty, full original costs and source boundaries.
Freeze the complete author argument before whole separately organized noncontributor review.
Allocation asserts no result.

<a id="growing-surgery-reuse"></a>
### 1. Exact question, reused whole polynomial, and new conclusion

The author is structural_research AI for Yin.
Root supplied the open growing-count question, not a derivation.
I read the complete repeated-cell congruence and polynomial in the then-live D212, now retained with its complete separate review in [L346](Yin_L_G0346_v1.md#repeated-cell-fixed-scope), the original full scalar and actual matrices in [L330](Yin_L_G0330_v1.md#positive-sparse-cost-fixed-scope), and the whole-circle bound and old fixed-depth limitation in [L340](Yin_L_G0340_v1.md#all-parameter-cost-fixed-scope).
The needed new step is a full-root lower bound uniform over ALL selected counts, not another fixed-depth coefficient.
A local search for circular logarithmic integrability and Jensen interfaces led to [Smy08-U001](../audits/literature/Smy08/Yin_U001.md), whose initial definitions explicitly include circle zeros and the factorwise Mahler integral.
That already accepted elementary identity is the only source-level analytic input below.
The logarithmic small-set estimate and limiting comparison needed here are proved in full, with no external zero-distribution theorem.

For k>=3 and ANY subset S of the k cells, write s=|S|.
Retain the complete proper matrix X_(k,S)=Q_S^T V_k Q_S and its negative absolute companion from L346, including every attachment.
Define

    P_(k,s)(t)=det(t X_(k,S)^-+(X_(k,S)^-)^T)
              =(t+1)^(k-1) G_(k,s)(t).

It is monic of degree n_k=4k+1.
With q=t+1, d=t^2+1, e=(t-1)^2 and C_j=sum_(h=0)^j t^h,

    T_(-1)=0, T_0=1, T_1=e,
    T_j=e T_(j-1)-4t^2 T_(j-2),
    A=t^4-4t^3-2t^2+1, A*=t^4-2t^2-4t+1,
    F_k=(t^(k+1)A-A*)/(t-1),
    B_k=F_k T_(k-1)-8t^2(d C_k-q t C_(k-1))T_(k-2)
                                    +16t^4 C_k T_(k-3),
    G_(k,s)=B_k-E_(k,s),
    E_(k,s)=2^k q[t^(2k-s)(C_k+1)+t^(s+1)C_k+t^(k+s+1)]. (1)

These are ENTIRE polynomial identities, including t=1 by polynomial continuation; no denominator roots or neutral factors are discarded.
The known upper bound, uniform for every integer 0<=s<=k, is

    0<=m(P_(k,s))<=k log2+log(20k^2+4k).              (2)

The new result is the complementary UNIFORM leading lower bound:

    lim_(k->infinity) min_(0<=s<=k) m(P_(k,s))/k=log2,
    lim_(k->infinity) max_(0<=s<=k) m(P_(k,s))/k=log2. (3)

Consequently EVERY choice s=s(k), including s=k or k-o(k), and every placement of those selected cells, has complete companion cost k log2+o(k), uniformly in the choice.
The complete literal cover has the same limit after division by k, since its extra original measure is log lambda_k in(log4,log5).
The proof below handles the nonreal roots left unpriced in the old finite experiment; it does not compute their individual locations, finite measures or a convergence rate.

<a id="circle-negative-log-control"></a>
### 2. Whole-circle conversion with every degree charged

Here is the analytic step that an isolated exterior evaluation would not supply.
All angular integrals use normalized Lebesgue measure dtheta/(2pi).
Fix r>1.
For any complex alpha and 0<u<=1,

    measure{theta: |r exp(i theta)-alpha|<u}<=2u.     (4)

For a direct geometric proof, an intersecting disk of radius u<r cuts an arc whose angular width is at most 2 arcsin(u/r).
Indeed if alpha has modulus a, the endpoint equation has cos(theta)=(r^2+a^2-u^2)/(2ra); its minimum over a>0 is sqrt(1-u^2/r^2), at a=sqrt(r^2-u^2).
This gives the stated maximal width; alpha=0 has empty intersection for u<r.
Since arcsin v<=pi v/2 on[0,1], the normalized measure is at most u/(2r), and the weaker bound(4) suffices, also at limiting endpoints.

For any measurable angular set E of normalized measure delta in(0,1], integration over levels gives

    integral_E log^-|r exp(i theta)-alpha|
       <= integral_0^infinity min(delta,2 exp(-v)) dv
       =delta[1+log(2/delta)].                       (5)

The convention log^-x=max(0,-log x) includes logarithmic infinities on null sets.
Now let p_k be any MONIC polynomial of degree at most 4k+1 and put f_k(theta)=k^-1 log|p_k(r exp(i theta))|.
By complete factorization, including multiplicities,

    integral_E f_k^- <=(4+1/k) delta[1+log(2/delta)]
                       <=5 delta[1+log(2/delta)].    (6)

This is uniform in the locations and sizes of ALL roots.
No bound on the largest root is assumed: some of the present companions have exponentially large roots.
In particular the negative parts are uniformly integrable.
Explicitly their total integrals are at most 5(1+log2); hence the set f_k^- >M has measure at most 5(1+log2)/M, and(6) makes its negative integral tend uniformly to zero as M tends to infinity.

It follows that, if f_k converges almost everywhere to a finite integrable f, then

    liminf_k integral f_k >= integral f.              (7)

To see this without assuming domination of the positive parts, first truncate only below: f_k^M=max(f_k,-M).
Apply the nonnegative integral liminf inequality to f_k^M+M.
Subtract the uniformly vanishing integral of (f_k^- -M)_+, and finally let M increase.
For the integrable limit f the lower truncations converge in integral.
Thus possible very large positive values cannot invalidate the lower bound.
This is the usual elementary Fatou/truncation argument, not an asserted new integration theorem.

Finally the factorwise circular Mahler identity, with all n roots counted, says

    J_r(p):=integral log|p(r exp(i theta))|
           =sum_alpha log max(r,|alpha|),
    m(p)<=J_r(p)<=m(p)+n log r.                       (8)

The equality follows by applying the same accepted linear-factor circle integral to p(r t); monicity is used explicitly.
Thus an exterior CIRCLE lower bound pays at most n log r when transferred to the unit-circle full measure.
A single exterior point has no such implication and is not used in the theorem.
All subsequent limits first hold at a fixed r, then take r down to1; no k-dependent radius or unproved exchange is used.

<a id="complete-transfer-dominance"></a>
### 3. The common matching term outside the circle

Fix 1<r<2 and a nonreal t=r exp(i theta).
The roots lambda,nu of

    z^2-e z+4t^2=0                                   (9)

are distinct and have different moduli.
Indeed u=z/(2t) obeys

    u+u^-1=(t+t^-1-2)/2.

The right side has nonzero imaginary part, since Im(t+t^-1)=(r-r^-1) sin theta.
Two roots of equal modulus would both have modulus1 in the u variable, and then their sum would be real.
Label the larger root lambda.
Their product gives

    |lambda|>2r>|nu|, lambda nu=4t^2,
    T_j=(lambda^(j+1)-nu^(j+1))/(lambda-nu), j>=0.   (10)

The last identity also gives T_(-1)=0.
The dominant root is holomorphic on the upper exterior half-plane {Im t>0,|t|>1}, and separately on its conjugate: simple roots give local holomorphic branches, while the unique larger modulus makes their labels agree on overlaps.
There is no branch point in these domains.

A useful exact simplification of the endpoint coefficient is

    d C_k-q t C_(k-1)=t^(k+2)+1.                    (11)

Substitute C_k=(t^(k+1)-1)/(t-1), F_k from(1), and(10) into B_k.
The lambda contribution is

    lambda^(k-2)/(lambda-nu)
       *[ t^(k+1)/(t-1) D(t,lambda)+D0(t,lambda) ],
    D(t,z)=A(t) z^2-8t^3(t-1)z+16t^4,
    D0(t,z)=-A*(t)z^2/(t-1)-8t^2 z-16t^4/(t-1),    (12)

and the nu contribution is the same expression with lambda and nu exchanged and a minus sign, using the SAME denominator lambda-nu.
As r>1 and |nu|<|lambda|, whenever D(t,lambda) is nonzero this proves

    B_k(t)=b(t)(t lambda)^k(1+o(1)),
    b(t)=t D(t,lambda)/[(t-1)(lambda-nu)lambda^2]
          !=0.                                     (13)

The error is pointwise at the fixed t; no uniform near-endpoint error is asserted.
Both the subleading constant-in-k bracket in(12) and the entire nu contribution are exponentially smaller at this fixed t.

The nonzero condition excludes only a null set on each circle.
The holomorphic function D(t,lambda(t)) is not identically zero in either exterior half-plane.
As t tends to infinity there, the dominant root is lambda=t^2(1+o(1)), so A lambda^2=t^8(1+o(1)), while the other terms of D have degrees at most6 and4.
Thus D is nonzero near infinity.
Its zeros are isolated.
Each open semicircle is inside the domain; its possible zeros form a countable discrete set and have angular measure zero.
This argument proves noncancellation of the leading matching coefficient; it is not inferred from sampled matrix values.

<a id="all-count-exterior-competition"></a>
### 4. Every growing selected count and the possible exponential tie

Take ANY sequence of integers s_k in[0,k].
Pass to a subsequence along which s_k/k tends to tau in[0,1].
All statements in this section refer to this subsequence; no coefficient depth is being held fixed.

If tau<1, the FIRST term in E_(k,s_k) dominates the other two, and C_k+1 has its usual exterior leading term.
Precisely,

    E_(k,s_k)(t)
       =[q t/(t-1)] 2^k t^(3k-s_k)(1+o(1)),
    lim k^-1 log|E_(k,s_k)(t)|
       =log2+(3-tau)log r.                          (14)

To check the full expenses, the second and third terms divided by the leading first one are bounded, for fixed t, by a constant times r^(-2(k-s_k)+1); this tends to zero exponentially when tau<1.
The errors from the constant part of C_k+1 are bounded by a constant times r^-k.
The prefactor q t/(t-1) is nonzero since r>1.
There is no hidden sign or phase cancellation in(14).

If tau=1, these two other terms cannot simply be discarded.
Instead the whole displayed sum in(1) satisfies

    limsup k^-1 log|E_(k,s_k)(t)|<=log2+2log r.       (15)

This follows directly from the three upper exponential rates log2+(3-tau)log r and log2+(1+tau)log r.
If the sum happens to vanish, its logarithm is minus infinity, which still satisfies(15).
But(10),(13) give the STRICTLY larger rate log r+log|lambda|>log2+2log r for B_k.
Thus the entire E term is negligible in this case, even when k-s_k grows unboundedly but sublinearly.

For tau<1 a tie between the two rates is the only further exception.
For fixed r the function theta ->log|lambda(r exp(i theta))| is real analytic on either open semicircle.
It is not constant.
As theta decreases to0, (r+r^-1-2)/2 belongs to(0,1/4), so both boundary roots in the u variable have modulus1 and the limit |lambda| is2r.
As theta increases to pi, (-r-r^-1-2)/2<-2, so the limiting dominant u root has modulus greater than1 and |lambda|>2r.
Therefore a fixed level, in particular

    log|lambda|=log2+(2-tau)log r,

can occur only on a discrete subset of either open semicircle, hence a null set.
This excludes an identical-rate open arc, rather than presuming unequal phase oscillations cannot cancel.
Together with the isolated coefficient zeros and the two real points, all exceptions have measure zero.

It follows from(13)--(15) and strict exponential dominance that the WHOLE normalized polynomial has the almost-everywhere limit

    k^-1 log|P_(k,s_k)(r exp(i theta))|
       -> f_(r,tau)(theta)
       :=log|q|+max{
             log r+log|lambda|,
             log2+(3-tau)log r}.                    (16)

For tau=1 the first entry strictly wins at every nonreal point, so the same formula remains valid without relying on any asymptotic lower bound for E.
The function f is bounded on the circle after harmless endpoint definitions: q is bounded away from zero for fixed r>1, and the dominant modulus has finite positive one-sided endpoint limits.
In particular it is integrable.
This derives an actual complete-polynomial limiting rate, not a maximum-modulus estimate or a maximum-root approximation.

<a id="uniform-repeated-cost-theorem"></a>
### 5. Uniform complete Mahler cost and its exact limitations

Apply(7) to the monic degree4k+1 polynomials and their limit(16).
Every nonreal point satisfies |lambda|>2r; both entries in the maximum are at least log2+2log r, with strictness for the first.
The elementary one-factor circle integral gives integral log|r exp(i theta)+1|=log r.
Hence

    liminf k^-1 J_r(P_(k,s_k))
       >=integral f_(r,tau)
       >=log2+3log r.                               (17)

Now use the FULL degree expense in(8):

    liminf k^-1 m(P_(k,s_k))
       >=log2+3log r-4log r
       =log2-log r.                                 (18)

This holds for EVERY fixed r in(1,2) on the same subsequence with s_k/k->tau.
Let r decrease to1 in this family of inequalities.
The conclusion is liminf m(P_(k,s_k))/k>=log2.
In combination with the uniform upper bound(2), this proves a limit log2 along every convergent-ratio subsequence.

For explicit quantifier closure, suppose the minimum in(3) had liminf below log2.
Choose indices k tending to infinity and integer minimizing s_k with values bounded below log2 by a fixed epsilon.
Compactness of[0,1] gives a further subsequence s_k/k->tau; the just-proved bound contradicts that epsilon deficit.
The upper bound(2) controls every maximum.
This proves BOTH limits in(3), equivalently

    for every epsilon>0 there is K(epsilon) such that
    k>=K(epsilon), 0<=s<=k implies
    |m(P_(k,s))/k-log2|<epsilon.                      (19)

This proof establishes existence of K(epsilon), not an explicit computed threshold, convergence speed or an O(log k) lower error.
The exponential separation in the exterior proof deteriorates near its crossing angles, and the final r down to1 step is not uniform at a prescribed finite k.
No such missing uniform rate is silently charged as zero.
The old finite exact comparisons remain valid: actual savings and increases occur at k3 and k4, and nothing here orders the choices at a given k.
What is now ruled out is an o(k) full companion cost, or any leading constant below log2, for ANY sequence of these specific repeated-cell congruences.

The entire literal cover still contains the original factor, so

    m(p_(W(X_(k,S))))=log lambda_k+m(P_(k,s)),
    sup_(S subset{0,...,k-1})
      |k^-1 m(p_(W(X_(k,S))))-log2| ->0.             (20)

The full original p_X=q^(k-1)(t-1)^(2k-2)F_k, every additional neutral factor in F_k or G_(k,s), and every nonreal root all remain counted.
The actual integer Q_S is exactly the block diagonal L346 witness, with Q3=[[0,0,1],[1,0,1],[0,1,1]] on selected cells, I3 elsewhere and I_(k+1) at the end.
It has determinant1 and includes every selected-to-selected and endpoint attachment.
Rank4k+1, height1, strict energy5k+2 and full squared sum9k+3 remain unchanged; the proper cover has rank8k+2, height1, energy10k+4 and full squared sum18k+6.
Those increasing degree/energy costs are not normalized away when asserting the scalar expense.

This is a construction-specific obstruction, not a class-wide minimum.
Other integral bases, moves that change B_k rather than just the cycle exponents, neutral stabilization or a different positive family remain open.
The original total measure stays in(log4,log5); this family supplies no near-one input or unrestricted Lehmer gap.
The changed next structural question is an actual unimodular move that changes the bulk recurrence itself, or an independently paid neutral-factor reduction, since this entire selected-subset family now has the same leading full cost.

<a id="growing-surgery-self-check"></a>
### 6. Self-check, useful failed implications, sources and contributions

The exploratory isolated-point idea was insufficient: a large value at t=i r alone does not lower-bound Mahler measure with a vanishing radial charge.
The completed proof uses an ENTIRE exterior circle, the all-root negative-log estimate(6), and the exact degree(4k+1)log r charge(8).
A second tempting simplification, a uniform bound on every root for all s, is false in the old s=0 regime and is unnecessary;(5)--(7) work for arbitrary root locations.
The proof likewise does not apply the old fixed-s onset or binomial coefficient with growing depth.
These are retained failures of possible shortcuts, not premises.

Author self-check covered: the actual L346 whole polynomial and all restored q factors; exact simplification(11); both recurrence roots and their analytic labeling in each exterior half-plane; lambda leading coefficient(12), its nonvanishing near infinity and isolated exceptional zeros; all three cyclic terms for tau<1 and tau=1; the boundary real-point limits, real-analytic level-set exclusion and noncancellation; all angular log singularities, multiplicities, monicity, uniform negative-part integrability and the precise lower Fatou direction; the full degree4k+1 radial expense and the order of all subsequence/r/k limits; uniform-in-count closure and the lack of an effective onset; original, companion and cover costs and fixed-input versus near-one scope.

No mathematical program, numerical extension, new J, root scan or finite experiment was executed.
The earlier complete J82 evidence is reused only at its retained L346 scope; none of its undecided finite root products is relabeled solved by this asymptotic theorem.
The local search initially used a PowerShell-incompatible rg wildcard path and then succeeded with rg's own glob option; that operational search retry produced no mathematical evidence or changed computation domain.

Source attribution is deliberately bounded.
The circular Mahler/Jensen identity is classical and already explicitly accepted in Smy08-U001, including integrable circle zeros; that exact passage was reread.
The new exterior-circle argument is an elementary application of the L346 recurrence and that identity, with the additional logarithmic small-set and truncation estimates proved here.
Standard factorization, analytic isolated-zero/real-analytic uniqueness facts and the elementary nonnegative integral liminf rule are used at their usual basic scope; no external transfer-matrix zero-locus, equidistribution, root-convergence, potential-theoretic compactness or Mahler-limit theorem is imported or claimed newly proved.
No new external source acquisition was needed.
L330's complete original positive-root statement retains its existing Hir06 attribution and prior inspection boundary.

Root supplied the broad growing-count question and explicitly requested checking the exterior-to-Mahler conversion; it supplied no step of the proof above.
This author developed the recurrence coefficient, all-ratio dominance, full angular integrability and uniform-cost deduction independently.
No current sibling proof is used.
The entire proof is author-self-checked and will be held for separately organized complete noncontributor review.
G0001 and all routes remain active and unresolved.


#### Entire author freeze

2026-10-10T13:21.
Complete Sections1--6, equations(1)--(20), all-count and all-placement full companion/cover asymptotics, the complete exterior-circle and negative-log conversion, all costs, source and failed-shortcut boundaries.
No program or new computation.
The entire author body is now held for separately organized complete noncontributor review.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0174_v1.md#complete-separately-organized-noncontributor-proof-review), with its original inspected scope and relationship.
