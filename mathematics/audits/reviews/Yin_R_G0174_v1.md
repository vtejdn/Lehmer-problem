---
author: Yin
---

# Retained project review: Uniform full companion cost for every growing repeated-cell congruence

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0349_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="all-count-cost-complete-independent-review"></a>

### Complete separately organized noncontributor proof review

Reviewer: root AI for Yin.
Whole review completed2026-10-10T13:24 against the frozen20,574-byte author body, all Sections1--6 and equations(1)--(20).
Root supplied the broad growing-count assignment and asked that the exterior-to-Mahler conversion be checked explicitly; it supplied none of the new coefficient, angular integrability, dominance or limit arguments.
This is a nonblind noncontributor review of the ENTIRE new proof.
The full author prefix is retained unchanged.
There is no new native mathematical computation or numerical claim to review in D216.

#### Actual input and complete source interfaces

I reread the complete L346 subset-congruence and determinant identities, including the full proper basis, restored factors and whole-circle upper bound, and the L340 recurrence/cost interface.
The full original factor and positive measure log lambda_k in(log4,log5) retain the precise accepted L330 scope.
The actual companion is monic degree4k+1 and the cover has degree8k+2.
Nothing in the argument substitutes a scalar alteration for an integral congruence, or uses fixed-s coefficient bounds at growing depth.

I read the responsible Smy08-U001 height-normalization passage.
It explicitly gives the circular integral/full-root identity for nonzero complex polynomials, counts every root multiplicity and permits integrable circle zeros.
This is the exact inherited elementary source interface used in(8).
The new small-set bound, exterior-circle comparison and limiting deduction are proved in the responsible draft, rather than attributed to an uninspected theorem about root distributions.
The elementary polynomial factorization, isolated-zero/real-analytic uniqueness and Fatou/truncation facts are used in their standard stated roles.
No strong spectral theorem, equidistribution result, finite root approximation or new literature-dependent asymptotic is needed.

#### All-root negative logarithms and the radial charge

For a disk of radius u<r meeting the radius-r circle, the endpoint cosine formula gives the maximum half-angle arcsin(u/r), attained at center modulus sqrt(r²-u²).
The arc's normalized measure is therefore at most arcsin(u/r)/pi<=u/(2r), which is stronger than the deliberately loose2u in(4).
The case alpha=0 is empty, and the real boundary/tangency cases follow by continuity.
The restriction0<u<=1 and r>1 ensures u<r throughout the level-set application.

Layer-cake integration of the negative logarithm over an arbitrary measurable E uses the upper level measure min(delta,2exp(-v)).
Its integral is exactly delta[1+log(2/delta)], proving(5).
For the COMPLETE monic factorization, negative part of a sum is at most the sum of the negative parts; multiplicities and every root are therefore counted.
Dividing by k yields the exact factor4+1/k, safely bounded by5, in(6).
The estimate is independent of root location or size.
Large roots do not require a missing uniform house bound.

Taking E to be the whole circle bounds all negative-part integrals by5(1+log2).
Markov's inequality then bounds the measure of the set where the negative part exceeds M, and the same small-set estimate makes its integral uniformly vanish.
This proves the specific uniform integrability needed below, rather than a stronger unproved bound on the positive parts.

For the lower integral limit, max(f_k,-M)+M is nonnegative and converges almost everywhere to max(f,-M)+M.
Fatou gives the correct lower inequality for this truncation.
The only subtracted error is the uniformly small tail of f_k^-, already proved; the integrable limiting f allows M to increase.
Thus(7) is valid without domination or convergence of the positive parts.
In the actual application f is bounded for fixed r, so its integrability is explicit.

The radius-r circular integral of a monic polynomial is the sum of log max(r,|alpha|), as follows by applying the accepted linear-factor identity to p(rt).
Relative to m(p), each root contributes between0 and log r.
This gives precisely0<=J_r(p)-m(p)<=n log r, not an estimate from one large point.
The later deduction uses the FULL n=4k+1, and first fixes r before any k limit.
This closes the essential expense that the initial isolated-point idea lacked.

#### Exact recurrence coefficient and absence of bulk cancellation

At nonreal t with |t|=r>1, Im(t+t^-1)=(r-r^-1)sin theta is nonzero.
The scaled recurrence roots u and u^-1 therefore cannot have equal modulus: if equal they both have modulus1 and real sum.
The larger original root lambda has modulus strictly greater than2r, the other strictly less.
They are simple, and the unique modulus ordering supplies consistent local holomorphic choices across either connected upper/lower exterior domain.
Possible real discriminant zeros lie outside those open domains.
The recurrence initial values yield the exact difference-of-powers formula, including T_0 and T_-1.

I checked the endpoint identity dC_k-qtC_(k-1)=t^(k+2)+1 by direct cancellation of finite geometric sums.
Substituting this, F_k and the entire recurrence formula into B_k gives the lambda contribution with prefactor lambda^(k-2)/(lambda-nu).
Its leading t^(k+1)/(t-1) coefficient is exactly A lambda²-8t³(t-1)lambda+16t^4; the remaining constant bracket is the displayed D0.
The nu expression has the same denominator and opposite sign.
All three original B terms are present.

At fixed exterior t, both the constant bracket and the nu contribution have exponentially lower rate than the nonzero leading lambda bracket.
Thus B_k=b(t)(t lambda)^k(1+o(1)) with the exact b of(13).
The condition D(t,lambda)!=0 is justified on a full-measure angular set.
In either exterior half-plane, lambda=t²(1+o(1)) near infinity and the leading D term is t^8(1+o(1)), while the other terms are of lower order.
Hence the holomorphic function is not identically zero.
Isolated zeros meet either open semicircle in a discrete, at most countable set, of angular measure zero.
This is a complete noncancellation argument for the leading coefficient, not an inference from the earlier finite matrices.

#### Entire cyclic term for every ratio and all exceptional angles

For an arbitrary sequence s_k, compactness permits a subsequence with s_k/k->tau.
At tau<1 the first term in E has leading factor qt/(t-1) times2^k t^(3k-s_k).
The second and third terms are bounded relative to it by constant multiples of r^(-2(k-s_k)+1), and the finite-geometric-sum error is exponentially small.
Since k-s_k grows linearly on this subsequence, the claimed whole-E asymptotic and rate in(14) follow.
No uncontrolled sum of equally large phases is dropped.

At tau=1 these relative errors need not vanish.
The proof correctly abandons a lower asymptotic for E and retains only the limsup of its COMPLETE three terms, at most log2+2log r.
The B rate log r+log|lambda| is strictly larger at every nonreal point.
Therefore B dominates regardless of cancellation inside E, also when k-s_k tends to infinity sublinearly.
This separately treats the all-selected endpoint rather than taking a nonuniform tau<1 estimate to its boundary.

At tau<1 the tie between B and E rates must also be controlled.
The larger-root modulus is real analytic on each open semicircle.
For1<r<2, approaching theta=0 gives scaled-root sum in(0,1/4), so both limiting scaled roots have modulus1 and |lambda| tends to2r.
At theta=pi the sum is less than-2, so the dominant limiting modulus is strictly greater than2r.
The real-analytic modulus function is consequently nonconstant on each semicircle; every fixed-level set is discrete there.
Thus the rate-tie angles have measure zero.
The two real points and coefficient zeros add only null sets.

Away from all these exceptions strict exponential dominance gives the whole-polynomial limit(16), including the factor q^(k-1) and both potential rates.
At tau=1 the same maximum formula is valid because its B entry wins strictly, even though E may vanish.
For fixed r, q is bounded away from zero and the dominant modulus has finite positive endpoint limits, so f_(r,tau) is bounded after harmless endpoint definitions.
The proof requires only almost-everywhere convergence for each fixed r; it does not claim one uniform error in theta, tau or r.

#### Uniform all-count conclusion, full expenses and limits

Every nonreal point gives log r+log|lambda|>log2+2log r, so the maximum in(16) is at least that common lower rate.
The complete q factor integrates to log r.
Applying the already proved lower Fatou bound therefore yields liminf J_r(P)/k>=log2+3log r.
Subtracting the full degree charge(4k+1)log r and taking k to infinity gives liminf m(P)/k>=log2-log r.
Letting the FIXED radius decrease to1 across these valid inequalities proves the lower constant log2; it does not exchange a k-dependent radius and the integral.

This reasoning works on every subsequence with convergent selected-count ratio.
If the minimum over the finite set of counts had a fixed deficit from log2 along infinitely many k, choose minimizing counts and extract a convergent-ratio subsequence; the preceding lower bound contradicts that deficit.
The uniform known upper bound yields the maximum limit.
This proves the exact quantifier statement(19), including ANY growing s(k), with no additional restriction on cell placement because the full scalar already depends only on s.

The original full scalar factor adds a bounded log lambda_k to every literal cover, so the same uniform leading limit follows for covers.
All q/e/other neutral multiplicities, all nonreal roots and the complete original positive factor remain present.
Rank, height, strict energy and full squared sum are the actual L346 values for the complete proper matrices and covers.
Normalizing by k to state a limit does not erase their increasing degree or coefficient cost.

The argument is not effective at a specified epsilon: no explicit K(epsilon), convergence speed or O(log k) lower remainder has been proved.
Its angular and radius limits do not justify such a rate.
It also gives no finite-k ordering and does not turn the14 earlier undecided full root products into computed finite values.
The old k3 saving, nonmonotonicity and k4 worsening remain consistent with this common leading asymptotic.

#### Complete finding

No mathematical defect or author repair is requested.
The entire new proof establishes a uniform leading full-cost obstruction for THIS explicit repeated-cell congruence family, including all-selected and every growing-count regime.
It does not bound the optimum over the whole integer congruence class, forbid different bulk-changing bases or neutral completions, or supply near-one inputs.
The original measure stays bounded between log4 and log5.
The useful rejected shortcuts and all source/contribution boundaries are accurately preserved.

There was no new mathematical executable, finite-domain extension, J output or numerical test in this proof-only round.
Review consisted of complete symbolic, analytic and quantifier checking of every equation and dependency above.
The entire20,574-byte frozen author prefix is preserved by this appended finding.
Fixed coordinator adoption and consumer updates remain separate; G0001 and all eight strategies remain active and unresolved.

The observed completion time is 2026-10-10T13:24.


## Review relationships

| Review | Relationship |
| --- | --- |
| [Original complete finding](#all-count-cost-complete-independent-review) | unknown |

The original account records a separate noncontributor whole inspection, but does not establish the complete initial conditions concerning substantive target-development context.
Broad assignments, fixed dependencies and upstream authorship alone establish neither shared development of this target nor its isolation.
The actual original date, full mathematical verdict and source, nonexecution and finite-input limitations remain unchanged.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original complete finding](#all-count-cost-complete-independent-review) | [Complete original input](../../ledger/Yin_L_G0349_v1.md#complete-retained-proof-and-review) | Entire original author statement and Sections1--6, all numbered equations, general and actual-input conclusions, necessary sources, useful failed implications and original cost/nonexecution limits. |
