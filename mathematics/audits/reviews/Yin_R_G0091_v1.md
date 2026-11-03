---
author: Yin
---

# Retained project review: Full original hitting bounds and the infinite excursion-conditioned stationary law

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0192_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="original-hitting-law-independent-review"></a>

### Complete separate noncontributor proof review

On 2026-10-10 the separately assigned orbit_research AI for Yin read and independently checked the complete frozen D58, including conventions, Sections1--6, equations(1)--(19), the infinite-chain argument and every conditional and uniformity boundary.
The pre-review file directly matched the recorded inspection fingerprint.
No mathematical defect, required correction or missing hypothesis affecting the conclusions was found.
The reviewer supplied none of D58's mathematics.
The coordinator's initial hitting bridge and the arithmetic author's subsequent derivations remain as disclosed.
The reviewer had contributed to earlier retained L172/L173 operator and collision arguments and to the fixed-input core work; those are already reviewed dependencies, not new contributions to this proof.
This is a separately organized noncontributor review of D58 and its input applicability, not a claim to re-review every upstream result independently of its authorship.
Shared context and the requested focus were available; this was not blind, human or formal inspection.

The reviewer directly reread L173's complete separated-digit proof, its explicit prefactor, actual-core conventions, maximum-atom argument and collision-radius interface; L189's entire linear-length proof, full finding and precise compact-termination hypothesis; and L154's actual first-return definitions, extended-value renewal identity and weighted-tail lower bound.
It also checked the retained reciprocal kernel conventions in L172 and L170's relevant actual narrow co-return and unbounded-narrow-state interfaces.
The accepted original source boundaries behind those fixed materials are retained, including the fixed-input support input used in the entropy comparison.
No external source theorem, source-proof audit, numerical test or new J is added by this review.

**Original law, domain and all-path bound.**
The actual core lies in the strict natural strip by the finite prefix/suffix bounds.
A core-killed n-step entry is bounded by its full-strip counterpart, so positivity or the same row/reciprocal-column Schur estimate transfers L173's operator bound.
The constants in(1) match that theorem exactly: gamma=log2 log(beta)/log(1+beta), C_beta=2M exp(gamma) and q=exp(-gamma).
The estimate is required only for n>=1.
A displacement from x to zero equals a shifted atom of the full difference law; its maximum atom is the zero displacement by the retained autocorrelation Cauchy--Schwarz argument.
This gives the ambient endpoint inequality for every x, not only for core states.

For nonzero x, every neutral field embedding is nonzero, so rho(x)>0 and n_x=ceil(rho/sqrt(s))>=1.
A zero-ending word has z_x+c_w=0, and each summand in c_w has norm at most sqrt(s); hence every hitting time is at least n_x.
Summing the endpoint upper bounds over all n>=max(N,n_x), with nonnegative terms and q<1, proves(2) for N>=1, including states with H=0.
No finite-horizon restriction or unproved reachability is used.

The real-boundary issue is consistent with the closed definition of N.
Forward stable estimates give <=S; backward estimation from zero gives a strict expanding bound <B at every point of a hitting word.
If a stable coordinate on that path equalled plus or minus S, reciprocal field substitution would make its expanding coordinate minus or plus B, respectively, a contradiction.
Indeed sigma(beta/(beta-1))=-1/(beta-1).
Thus such a hitting path also lies in the open natural strip; no boundary hit is discarded.
For x in the actual core, prefixing any fixed zero-to-x path makes every x-to-zero ambient path part of an actual closed word, which proves exact agreement with the core-killed hitting probabilities without identifying every strip point with D.

Under beta<phi and the full L189 compact-termination premise, that theorem applies to every actual order state of N, not merely states already known to return.
A zero-ending word of length at most A rho+B_0 has original path probability at least4^(-A rho-B_0), even if it first hits zero earlier.
This gives the lower bound in(3); enlarging positive constants safely handles small radius.
L170 supplies the premise for the original degree-ten input only.
Combining the bounds gives the stated fixed-input spatial scale on its unbounded narrow sequence, with the dimension factor and the potentially large chosen-control constants visible.

**Conditional law and its complete time tail.**
Division by the positive lower bound for H gives(4) for the full law conditional on hitting.
D_beta>1 and a,b nonnegative imply t_x>=1, so every application of the N>=1 bound at t_x+k is legitimate.
Its ceiling ensures D_beta exp(a rho+b-gamma t_x)<=1, yielding(5).
For the integer expectation, summing the terms through t_x by one and the later terms by q^k gives exactly t_x+q/(1-q), while the deterministic lower length remains true after conditioning.
This checks both offsets in(6), including the distinction between >=N and >N.
For Y=(tau-t_x)_+, the identity E exp(theta Y)=1+(exp(theta)-1)sum_(k>=0)exp(theta k)Pr(Y>k), together with Pr(Y>k)<=q^(k+1), proves(7) for 0<theta<gamma.
The discussion of an infinite unconditional extended mean when H<1 is correct and does not conflict with the conditional estimate.

On the set where H is positive, first-step decomposition with H(0)=1 gives the stated absorbing hit transform.
A positive successor of a finite positive hitting potential is well defined, and zero-potential successors have zero transformed weight.
First-hit word products telescope to their original weights divided by H(x); the complete sum is one.
Thus this is event conditioning, with no omitted spectral factor or original-law recurrence assertion.
The time-zero convention at zero is kept separate from positive first returns in the later sections.

**Green potential and reciprocal orientation.**
The operator series for G converges in norm because the complete n>=1 norms are exponentially summable; the identity operator supplies its n=0 term.
Its entries therefore equal the nonnegative path sums.
Every zero-to-zero path is in D, so U=G(0,0)=sum p_n.
Since f_n<=p_n and f_1=1/2, both F and F' converge, F'>=1/2, and the complete renewal identity implies F<1 and U=1/(1-F).
The exponential bound gives a neighborhood of z=1 in which both generating functions converge; differentiation there is legitimate.

First-hit decomposition from x in D gives G(x,0)=H(x)U, including x=0 under the stated H(0)=1 convention.
Hence h=G delta_0/U is in l2, positive on the actual core and satisfies(I-K)h=delta_0/U.
This yields harmonicity away from zero and Kh(0)=1-1/U=F.
The reciprocal map T is an additive involution of the order, and reversing a complete closed word proves preservation of D itself.
On each selected neutral embedding it acts by multiplication by zeta_j^(-1) after complex conjugation, so it preserves rho.
The equal digit weights give K(Ty,Tx)=K(x,y), whence G(0,x)=G(Tx,0)=U h(Tx).
This is transpose-through-involution symmetry, not ordinary kernel reversibility.
All row/column orientations used in(9)--(11) are correct.

**The actual infinite excursion-conditioned chain.**
In(12), harmonicity normalizes each nonzero row and the separately divided zero row has sum Kh(0)/F=1.
Every core edge of positive weight remains positive.
The actual core is irreducible through zero because its definition supplies both reachability and co-return paths, so the new chain is irreducible as well, including the possible singleton case.
A first-return excursion contains exactly one initial zero-row factor1/F; all h ratios cancel.
Its complete first-return distribution is therefore f_n/F, including the length-one zero loop, with total one and finite mean F'/F.
This proves the asserted return conditioning and positive recurrence on the countable infinite core; no limiting finite-core normalization is needed.

The explicit stationary calculation also closes normalization directly.
Since h is in l2 and T is a permutation, sum h(x)h(Tx) is finite by Cauchy--Schwarz.
The nonnegative matrix-entry convolution and the norm-convergent operator series give(G^2)(0,0)=sum_(n>=0)(n+1)p_n.
Substitution of the Green columns and U'=F'U^2 gives precisely sum h hT=1-F+F'.
Removing the x=0 term, which is one, proves F+sum_(x!=0)h(x)h(Tx)=F'.
Thus(14) is a probability, with pi(0)=F/F' as independently required by the mean excursion length.
Applying the T permutation to(I-K)h gives K^T(h o T)=h o T-delta_0/U.
When checking stationarity, the exceptional zero-row factor F cancels its numerator pi(0); all remaining terms combine into h(y)K^T(h o T)(y)/F'.
At y!=0 this is pi(y), and at y=0 it is(1-1/U)/F'=F/F'.
Nonnegative summation and the proved finite normalization justify these infinite sums.

For R>0, n_R>=1 and the zero state does not belong to the radial set.
Finite neutral propagation annihilates every projected K^n delta_0 term with n<n_R.
Projecting the Green expansion before applying the triangle inequality therefore gives exactly(D_beta/U)q^n_R as the l2 tail bound.
The radial set is T-invariant, so Cauchy--Schwarz bounds its stationary mass by the square of that l2 norm divided by F'.
Using U>=1 and F'>=1/2 yields(16), with exponent2gamma/sqrt(s).
The bound needs no lattice-point count or truncation of D.
Nonnegative tail integration gives all stated smaller exponential radial moments.
These statements concern the explicitly changed excursion-conditioned chain and do not create an eigenvector or a normalized transform at the full critical radius.

**Weighted first-hit and return gate.**
Multiplying every first-hit mass by exp(c n) and summing the complete endpoint bounds gives(17) exactly for 0<=c<gamma.
It permits zero at states without a co-return.
At a finite positive H_c state, first-step decomposition gives H_c(x)=exp(c)sum_eta p_eta H_c(beta x+eta); any positive-probability successor with infinite potential would contradict finiteness.
The stated absorbing transform is therefore well defined and its full first-hit distribution is normalized by the complete weighted mass.
It is a changed law, with no claim at the critical boundary.

At zero the first digit either gives an immediate return of weight exp(c)/2 or enters1 or-1 with weights exp(c)/4.
Sign symmetry identifies their complete first-hit potentials.
This proves(18) as an extended nonnegative sum for every c>=0, regardless of whether1 is known to belong to D: if it has a co-return it is in D because it is reached by one original digit, and otherwise its contribution is zero.
For a common positive c<log2, algebraic rearrangement gives exactly(19), with a positive right-hand side.
Finite H_c or normalization of its transform alone is not that strict inequality.
For c<gamma, complete exponential summability makes U(exp c) finite, and L154's renewal sum then forces F(exp c)<1.
The retained spectral comparison gives gamma<=h2<=log beta, with gamma/log beta tending to one as beta tends to one.
For c>log beta and exp c<2, L154's full weighted-tail lower bound instead gives F(exp c)>=1.
The shrinking fixed-input range, all late excursions, and the missing common positive c are retained without exchanging input, degree or time limits.

This complete written review supports all-path original hitting upper bounds, the conditional linear time scale under its stated termination premise, the exact infinite excursion-conditioned process and stationary law/tail, and the explicit complete weighted-return boundary.
It does not prove universal compact termination, original-law positive recurrence or finite unconditional hitting means, an infinite critical normalization, input-uniform constants or a Lehmer gap.
No proof correction, source acquisition, program execution or new J was required.
The author bytes remain unchanged as the file prefix; substantive later revisions require corresponding review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original whole hitting-law and stationary-chain finding](#original-hitting-law-independent-review) | unknown |
| [Original listed hitting-law author checks](#original-hitting-law-author-check-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original whole hitting-law and stationary-chain finding](#original-hitting-law-independent-review) | [Entire original frozen hitting/Green/stationary proof](../../ledger/Yin_L_G0192_v1.md#retained-original-hitting-law-proof) | Actual original2026-10-10day-precision whole D58 conventions/Sections1--6/equations(1)--(19): all fixed Salem beta in(1,2)/degree/order/original digit law/actual core versus ambient strip, every nonzero/time-zero and strict-boundary convention, exact fixed exponential constants and maximum atom/neutral finite propagation/all original hitting paths, conditional compact-termination and original-Lehmer spatial comparison, full conditional tail/mean/centered moment and absorbing transforms, norm-convergent complete Green sums/first-hit renewal/reciprocal T orientation, exceptional zero row and exact f_n/F excursions, countable-core positive recurrence/full stationary normalization/invariance/projected radial tail, complete weighted first-hit identity/strict common-c gate/shrinking-rate and full weighted-tail obstruction, actual contribution/check/reuse and every nonuniformity/noncritical/original-law limitation. The entire original whole scope is preserved. |
| [Original listed hitting-law author checks](#original-hitting-law-author-check-finding) | [Original complete argument and listed author account](../../ledger/Yin_L_G0192_v1.md#retained-original-hitting-law-proof) | Actual original2026-10-10day-precision listed author checks: ambient versus actual core/nonzero-time-zero/complete infinite sums/neutral propagation/floors and tail offsets/conditional mean and moment/T norm and Green transpose/exceptional zero row/derivative identity/projected l2 tail/conditional termination and weighted gate ranges. No additional original whole author-review event is invented. |

## Exact retained initial-arrangement boundary

All original135lines of the whole written review, its original day-precision date, pre-review inspection-fingerprint assertion, verdict, full scope, actual contributions and source/nonexecution boundaries remain fixed.
The separately assigned reviewer supplied none of D58's mathematics, while it had contributed to already fixed L172/L173 and fixed-input core work.
Reading or authoring those fixed upstream inputs does not by itself establish contribution to this new hitting/Green/stationary proof.
Shared context and the requested focus were available, but their actual mathematical contents and the complete initial target-review arrangement are not retained.
Consequently initial isolation is not established and the original entire whole finding remains UNKNOWN for independent-review purposes.
The old independently/noncontributor title and verdict do not determine that relationship.

The coordinator actually proposed combining the deterministic minimum length, maximum-atom bound and exponential summation into the eventual-hitting bridge, together with its comparison with L189's selected-path lower bound.
The arithmetic author checked that bridge and developed the complete conditional, Green, stationary and weighted-return derivations.
Those are disclosed target mathematical contributions.
The conditional sentence that a coordinator check alone would not be noncontributor review does not record an additional completed coordinator whole-review event.
The precise original listed author checks follow as SELF.
A current authored whole check neither supplies missing original isolation nor closes the original entire UNKNOWN obligation.
No new external source/PDF inspection, fingerprint computation, program/J, native run or research Task/E is supplied.

<a id="original-hitting-law-author-check-finding"></a>
## Original listed hitting-law author checks

Date: 2026-10-10.
The exact original listed author-check and then-pending account follows.

Self-check covered the original ambient versus actual-core path sets, nonzero/time-zero conventions, complete rather than truncated infinite sums, neutral finite propagation, every floor and tail offset, the conditional expectation and exponential-moment identities, preservation of rho under T, Green entry/transpose orientation, the exceptional zero-row normalization, the derivative identity(15), l2 tail projection before operator-norm summation, all conditional termination assumptions, and the direction and range of the weighted-return criterion.
The source inputs are precisely fixed L173/L189/L154 interfaces; no new external source, numerical test or J is needed.
Complete separate noncontributor review is pending.
