---
author: Yin
---
# A certified infinite original-digit return core for a quartic Salem unit

Date: 2026-10-09, Asia/Hong_Kong.
Fixed G0001 result adopted by the coordinating AI for Yin after the separately organized full-chain and corrected-consolidation reviews retained below.
The proof and complete review history are preserved from the retired working drafts identified in the retention account.
No unrestricted gap or Task completion is asserted.

<a id="quartic-infinite-core-theorem"></a>
## Theorem and precise scope

Let beta>1 be the expanding root of P(t)=t^4-t^3-t^2-t+1, zeta its upper unit-circle root, and S=beta/(beta-1).
For x in Z[beta], write x_+=x(beta), x_-=x(beta^(-1)), z=x(zeta).
Under the original operations x -> beta*x+eta, eta in {-1,0,1}:

1. Every state with |x_+|<=1 and |x_-|<=S has a finite continuation to zero.
2. The actual zero-to-zero return core contains every state with |x_+|<=1 and |x_-|<=beta, and is infinite.
3. The accepted L157 interface then implies unbounded nonzero state norms, infinitely many prime-ideal divisors across the core, and unbounded integer quotient heights H(q) with H(Pq)<=1.
4. For every x in Z[beta] with |x_+|<=1, |x_-|<=S and |z|<=R, where R>=10, there exists an original-digit continuation to zero of length at most L_R+25, with L_R defined below.
   Under the original independent digit law, the probability of hitting zero by that time is at least 4^(-(L_R+25)).
   This existence bound on continuation length is O(R^2 log R) for this fixed input; it is not a bound on every random trajectory.

This is a computer-assisted proof with exact rational interval and integer certificates, not formal verification.
It does not prove the corresponding assertions for the original Lehmer input, arbitrary Salem numbers or a near-one family, nor a uniform weighted-tail or entropy-gap estimate.

<a id="quartic-infinite-core-proof"></a>
<a id="quartic-neutral-descent"></a>

## Exact input and certified neutral descent

Let

    u=(1+sqrt(13))/2,
    beta=(u+sqrt(u^2-4))/2,
    Re(zeta)=(1-sqrt(13))/4, Im(zeta)>0, |zeta|=1.

These are roots of P.
Indeed t^(-2)P(t)=(t+t^(-1))^2-(t+t^(-1))-3.
Its two trace roots are u>2 and (1-sqrt(13))/2 in (-2,2).
The trace quadratic is irreducible.
Its discriminant for t, u^2-4, becomes negative in the latter real embedding and therefore is not a square in Q(sqrt(13)).
Thus P is irreducible, beta is a degree-four Salem unit, and Z[beta] embeds as a full lattice into R x R x C by the four real coordinates

    x -> (x_+,x_-,Re(z),Im(z))
       = (x(beta),x(beta^(-1)),Re(x(zeta)),Im(x(zeta))).

The bounds 17/10<beta<18/10 are verified in the exact computation.
Set

    B=1/(beta-1), S=1/(1-beta^(-1))=beta/(beta-1).

The original operation is x -> beta*x+eta, eta in {-1,0,1}.
No larger alphabet, quotient-ring relaxation, or reduction of the state modulo an ideal is used.

**Partial descent statement.** Every actual x in Z[beta] satisfying

    |x_+|<=1, |x_-|<=S, |z|>=10

admits a finite original-digit block ending at x' such that

    |x'_+|<1, |x'_-|<=S,
    |z'|^2 <= |z|^2-557/500.

All intermediate states have |x_+|<B and |x_-|<=S.
The block consists of an input-dependent number of zero digits followed by at most nine selected digits.
The radius-dependent bound for the zero prefixes is proved below.

This supplies descent on an unbounded neutral domain.
The compact termination and reachability arguments below are separate steps needed to identify actual returning states.

## Descent certificate and proof

[J G0018](../computations/programs/Yin_J_G0018/readme.md) retains fifty closed cells

    I_j=[j/100,(j+1)/100], j=50,...,99,

and three words w_(j,1),w_(j,2),w_(j,3) for every cell.
All words have length between one and nine.
For w=(eta_1,...,eta_k), define

    T_w(t)=beta^k*t + sum_(i=1)^k eta_i beta^(k-i),
    c_w=sum_(i=1)^k eta_i zeta^(-i).

The exact interval verifier establishes, for each cell:

1. Every one of its three words maps the entire cell strictly into (-1,1).
2. Their three complex c_w form an oriented triangle with zero strictly inside it.
3. If r_j is a certified lower bound for the distance from zero to every triangle edge, and m_j is a certified upper bound for max |c_w|^2, then 20*r_j-m_j>=557/500.

The saved decimal geometry is discovery output only.
The verifier recomputes all three conditions from the integer digits and rational cell endpoints with Fraction interval arithmetic.
Square-root enclosures are obtained from integer square roots at scale 10^35; no floating-point premise or optimizer result enters this check.

For any complex z, a triangle containing the disk of radius r_j centered at zero has a vertex c_w satisfying Re(conj(z)*c_w)<=-r_j*|z|.
Under its word the neutral coordinate becomes zeta^k(z+c_w), so if |z|>=10,

    |z'|^2 = |z+c_w|^2
             <= |z|^2-2*r_j*|z|+m_j
             <= |z|^2-557/500.

This proves the assertion for x_+ in [1/2,1].
A point at a shared endpoint may use either adjoining cell.
For x_+ in [-1,-1/2], apply the positive-cell result to -x and negate every selected digit; the squared neutral bound and both strip bounds are unchanged.

If 0<|x_+|<1/2, choose the first h>=1 with beta^h*|x_+|>=1/2.
Prepending h zero digits leaves the neutral magnitude unchanged and contracts |x_-|.
Its new expanding magnitude lies in [1/2,beta/2), hence in [1/2,1] because beta<2.
If x_+=0, injectivity of this field embedding forces x=0, which is outside |z|>=10; there is no missing nonzero zero cell.
Thus the operation covers every point of the stated actual algebraic domain.

The contracting bound is invariant under every digit individually:

    |beta^(-1)*x_-+eta| <= beta^(-1)*S+1 = S.

The narrow expanding strip need only hold at block endpoints.
To check every intermediate state, work backward from the final |x'_+|<1.
At r remaining digits its magnitude is at most

    beta^(-r) + (1-beta^(-r))/(beta-1) <= B,

and the inequality is strict because B>1 and the endpoint is strict.
Zero-prefix states have magnitude at most beta/2<1<B.
Hence the whole word stays within the ordinary necessary real strip for a returning state, while no actual return is asserted.


<a id="quartic-compact-reduction"></a>
## Reduction to a compact set

Iteration reaches K={x in Z[beta]: |x_+|<=1, |x_-|<=S, |z|<10} in finitely many blocks.
Each block outside K reduces a nonnegative squared neutral magnitude by at least 557/500, and every zero prefix is finite for a nonzero actual algebraic state.
The embedding is a full lattice: the distinct conjugates give an invertible Vandermonde embedding of the basis 1,beta,beta^2,beta^3, with the complex pair written in real coordinates.
Hence K is finite.
The following exact certificate proves that every point of K continues to zero.

<a id="quartic-compact-termination"></a>

## Complete compact termination certificate

Write x=a_0+a_1 beta+a_2 beta^2+a_3 beta^3.
Let M be the real matrix whose rows are beta^j, beta^(-j), Re(zeta^j), Im(zeta^j), for j=0,1,2,3.
It is invertible by the degree-four embedding result above.
If A=M^(-1), then every x in K satisfies

    |a_i| <= |A_(i,0)| + S |A_(i,1)|
                   + 10 sqrt(A_(i,2)^2+A_(i,3)^2).

The last term follows by Cauchy--Schwarz from |x(zeta)|<10.
Outward rational interval evaluation of the adjugate and determinant certifies that the integer coefficients must satisfy

    |a_0|<=5, |a_1|<=7, |a_2|<=7, |a_3|<=4.

The exact enumeration program in [J G0019](../computations/programs/Yin_J_G0019/readme.md) enumerates this whole box, first slicing a_0 by the expanding bound.
The slicing leaves 841 tuples to examine.
It uses integer-scaled outward embedding intervals to reject only tuples proved to violate |x_-|<=S or |x(zeta)|<10.
Its retained list contains 259 distinct states and is a finite superset of K.
No unclassified interval boundary is discarded, and equality at neutral radius ten may be discarded only when the lower bound is at least 100, consistently with K's strict neutral inequality.

Every one of the 259 retained states has an explicit saved continuation to zero of at most 25 original digits.
The exact checker uses

    (a_0,a_1,a_2,a_3) ->
       (-a_3+eta, a_0+a_3, a_1+a_3, a_2+a_3), eta in {-1,0,1},

which follows from beta^4=-1+beta+beta^2+beta^3.
It verifies that the saved list covers all 259 states exactly once and that every path ends at the zero vector.
Therefore every x in K has a finite original-digit continuation to zero, of length at most 25.

The reverse graph used to discover these paths was restricted by floating-point embedding tests at neutral radius twelve.
Those tests are not proof premises: only the exact retained integer words and their complete coverage enter the conclusion.
No claim that the searched graph contains every possible path is needed.

## From descent to finite co-return

Combining the preceding certificate with the descent argument above yields:

    Every x in Z[beta] with |x_+|<=1 and |x_-|<=S
    admits a finite original-digit path to zero.

For |x(zeta)|<10 the compact certificate applies immediately.
Otherwise the descent argument above gives finitely many descent blocks reaching K and the final path above.
This statement concerns all actual algebraic states in the domain; it requires no prior reachability assumption.

The quantitative extension is also explicit.
If R>=10 and |x(zeta)|<=R, the L_R defined in the radius-dependent time section below gives a path to zero of length at most L_R+25.
Under the original independent difference-digit probabilities (1/4,1/2,1/4), at least one such word has probability at least 4^(-(L_R+25)).
Thus the probability of hitting zero by that time is bounded below by this radius-dependent quantity.
This remains a weak fixed-input existence bound, with no uniform full-law excursion-tail or entropy-gap assertion.


<a id="quartic-descent-time-bound"></a>

## A radius-dependent time and probability bound

Let R>=10 and start at an actual state in the narrow real domain with |z|<=R.
Put delta=557/500 and define

    N_R=floor((R^2-100)/delta)+1,
    K_R=min{k>=0:(17/10)^k >=17 R^2/14},
    L_R=N_R(K_R+9).

Then some original-digit word of length at most L_R reaches the compact set K in the compact-reduction argument.
In particular L_R=O(R^2 log R) for this one fixed quartic input.
For the original difference-digit probabilities (1/4,1/2,1/4), the probability of hitting K by time L_R is at least 4^(-L_R) from any such starting state.
This is a radius-dependent hitting bound, not an exponential return estimate uniform in a varying algebraic input.

Here is the arithmetic bound on the zero prefixes.
At any nonzero block endpoint before K is reached, x is an algebraic integer, so

    1<=|Norm(x)|=|x_+ x_-| |z|^2.

Since |x_-|<=S=beta/(beta-1)<17/7 and |z|<=R, it follows that

    |x_+|>7/(17 R^2).

Consequently K_R zero digits already make the expanding magnitude exceed 1/2, using beta>17/10.
The first crossing used in the block argument occurs after at most K_R digits and still lies below beta/2<1.
All subsequent block endpoints retain the same R bound because their neutral square decreases.
At most N_R descent blocks are needed: if that many were executed, the neutral square would be at most R^2-N_R delta<100.
Each uses at most K_R zero digits and nine chosen digits, proving the length estimate.
A starting point already in K uses the empty word.
The probability bound follows from this one actual finite digit word, whose product probability is at least 4 to the negative of its length; the event hits K by time L_R.
No continuation from K to zero is assumed.


<a id="compact-termination-infinite-core-bridge"></a>

## Reciprocal reachability and an infinite actual core

The exact compact certificate above supplies the premise of the following reciprocal bridge.
It provides reachability as well as co-return.

Let sigma be the field involution beta -> beta^(-1).
It exists because P is irreducible and reciprocal and beta^(-1) generates the same field.
Both sigma and multiplication by beta^(-1) preserve Z[beta].
Define

    T(x)=beta^(-1) sigma(x),       T(T(x))=x.

If a word eta_1,...,eta_n takes y to zero, then

    y=-sum_(i=1)^n eta_i beta^(-i),
    T(y)=-sum_(i=1)^n eta_i beta^(i-1).

The latter state is reached from zero by the reversed, negated word -eta_n,...,-eta_1.
This is the elementary reciprocal normalization behind the Mercat-type reachability mechanism; no source theorem about this new quartic is assumed.

Let D_narrow be the domain |x_+|<=1, |x_-|<=S, with no neutral bound.
The descent and compact certificate give a finite continuation to zero for every x in D_narrow.
Now take the smaller slab

    Omega={x in Z[beta]: |x_+|<=1, |x_-|<=beta}.

Since 1<beta<2, beta<S.
For x in Omega, both x and T(x) lie in D_narrow: T(x)_+=x_-/beta and T(x)_-=beta x_+, so their required bounds follow directly.
Thus x continues to zero, and the continuation from T(x) yields a path from zero to T(T(x))=x.
Every point of Omega is an actual returning state.

Finally Omega contains infinitely many distinct elements.
For N>=1 take the (N+1)^4 elements sum_(j=0)^3 a_j beta^j, 0<=a_j<=N.
Their two real embeddings lie in a rectangle of side lengths O(N), with constants depending only on beta.
Partition it into O(N^2) half-open rectangles of respective widths 1 and beta.
One cell contains at least c N^2 distinct elements for a fixed c>0 and all sufficiently large N.
Subtract one element of this cell from all its other elements.
The resulting distinct differences belong to Omega, since their real coordinate differences have magnitudes below 1 and beta.
Their number tends to infinity.
Hence the full actual core is infinite, and the retained [L157 equivalence](Yin_L_G0157_v1.md#global-prime-support-finite-core-equivalence) then gives unbounded state norms and quotient heights and no single finite prime-support cover at this input.


## Sources, computation and contributions

The geometric descent method is adapted from the scoped [Mer13 source inspection](../audits/literature/Mer13/Yin_U001.md#mer13-u001).
Its published theorem treats a different quartic and is not transferred to this input.
The present proof uses the newly constructed finite certificates.
No novelty claim is made.
L157 is an accepted project dependency only for the final norm, prime-support and quotient-height consequences; its existing ESS input retains its recorded statement-and-applicability scope.

The orbit_research AI constructed the 150-word table and its actual-domain descent proof, the complete compact enumeration and 259 continuations, and the co-return implication.
The coordinating AI contributed the norm-based timing bound and the reciprocal/pigeonhole bridge, which orbit_research cross-checked.
The complete component review is [preserved full-chain review](../audits/reviews/Yin_R_G0068_v1.md#quartic-full-chain-review), by the structural_research AI who contributed none of this mathematics.
Shared task context, progress explanations and prior local checks were available, so the review is not blind.

[J21](../computations/programs/Yin_J_G0021/readme.md) independently reimplements the arithmetic checks without author helpers: all 150 words, interval Gaussian inversion, all 22,275 coefficient tuples, agreement of the 841 expanding-strip tuple count, equality of the 259 retained-state sets, and whole-polynomial division for all 259 paths of length at most 25.
The intermediate 841-tuple set is not retained by the author program and was not compared as a set.
J21 also reruns the author's exact checkers with output redirected into the review group.
Library dependencies and the absence of formal verification remain explicit.
The full original source proofs and numerical discovery programs were not rerun as part of that independent review.

The complete final consolidation review and its resolved initial findings are retained below.
G0001 remains active and unresolved.

<a id="quartic-fixed-retention"></a>
## Fixed retention and coordinator adoption

On 2026-10-09, after the 2026-10-09T15:48 corrected-consolidation review, the coordinating AI for Yin accepted this exact fixed-quartic result and delegated its mechanical fixed retention to the independently assigned reviewer.
This section implements that coordinating adoption decision; it is not a new proof contribution or a personal human proof inspection.
No C acceptance decision or Task-completion decision is created here.
G0001 remains active and unresolved.

The complete proof above is the corrected former D G0018 consolidation of former D G0013 Sections 1--7 and former D G0014 Sections 1--4.
The complete D G0016 review history below preserves its original dated inspections, initial consolidation objections and resolved disposition.
Those identities are retired working-material locators, not additional current proof dependencies.
Their link destinations now point to the corresponding retained proof/review sections; references to their original section numbers describe the historical inspections.
Headings are nested for this fixed home, and status/navigation metadata is current; mathematical formulas, hypotheses and historical findings are unchanged.

| Retired working identity | Retained content |
| --- | --- |
| `Yin_D_G0013` | [Neutral descent](#quartic-neutral-descent), [compact reduction](#quartic-compact-reduction), [timing](#quartic-descent-time-bound), [reciprocal bridge](#compact-termination-infinite-core-bridge), and the dated local/contributor review accounts below |
| `Yin_D_G0014` | [Complete compact certificate](#quartic-compact-termination), the co-return implication and its disclosed contributor checks |
| `Yin_D_G0016` | [Complete independent chain review](../audits/reviews/Yin_R_G0068_v1.md#quartic-full-chain-review) and [initial/corrected consolidation findings](../audits/reviews/Yin_R_G0068_v1.md#quartic-consolidation-review), retained in full |
| `Yin_D_G0018` | [Corrected complete theorem](#quartic-infinite-core-theorem) and [complete proof](#quartic-infinite-core-proof) above |

The retained review text includes historical pending or rolling-status wording.
It records what was true at each original inspection; the final corrected disposition and this adoption are the current selection.
The original timestamps and review relationships are not rewritten by promotion.
J G0018, J G0019 and J G0021 retain their programs, inputs, exact certificates and executed results.
The remaining live method consumer D G0017 receives only updated navigation to this fixed proof.

<a id="quartic-preserved-local-reviews"></a>
## Preserved earlier local and contributor review accounts

These accounts precede the full-chain review.
Their pending statements are historical, and their inspection scope is not enlarged by this fixed retention.
The following original paragraphs preserve the actual dates, contributions and boundaries.

### D G0013 local partial-descent review, 2026-10-09T15:25

At 2026-10-09T15:25 the coordinating AI for Yin separately reviewed Sections 1--4 and all of J G0018's interval verifier.
It checked the degree-four field and embedding domain, triangle-to-descent implication, every interval operation including square-root enclosures, full closed-cell coverage, conjugate rotation, negative/zero cells, both strip bounds and finite compact reduction.
It reran all 150 block checks successfully, recovering the exact 557/500 lower bound.
The reviewer had assigned the broad exploration and requested explicit domain/compact-residue boundaries; it had not derived the block construction or supplied the certificate.
It received author progress explanations.
No mathematical defect was found in the stated partial theorem.
This review did not rerun discovery, reconstruct the Mercat source proof, enumerate K or prove reachability.
It is a local exploratory check, not fixed acceptance evidence.
The coordinator's subsequent new derivation in Section 6 is a separate contribution and is not covered by this independent relationship.

### D G0013 timing contributor cross-check, 2026-10-09T15:28

The coordinator self-checked this corollary.
At 2026-10-09T15:28 the orbit_research AI for Yin separately read and checked this exact Section 6 argument: norm integrality and nonvanishing, S<17/7, the rational threshold defining K_R, the strict first-crossing bound, N_R at the R=10 endpoint, and the single-word original-law probability implication.
No gap was found within the stated radius-dependent scope.
Before reading this text, that checker had received the coordinator's norm idea and supplied an equivalent beta-logarithm formula for the zero-prefix bound.
This is therefore a cross-check of a discussed contribution, not a claimed independent derivation or an independent review relationship for the corollary.
The earlier separate review of Sections 1--4 remains limited to those sections.

### D G0013 conditional bridge contribution, 2026-10-09T15:29

The coordinating AI added this conditional interface on 2026-10-09T15:29.
Assume that every point of the finite K in Section 3 has an original-digit continuation to zero.
Then the actual returning core for this quartic is infinite.
The compact hypothesis remains unproved here; the following argument isolates why proving it would also supply reachability, rather than only co-return.

This establishes only the conditional bridge.
It supplies no compact enumeration, no path for an unchecked residual state, no near-one family and no uniform entropy estimate.
The coordinator self-checked the involution, word order, slab inclusion and counting argument; separate review of this added interface is pending.


### D G0014 contributor and computation checks

The retained reachability/counting proof is the coordinator's Section 7, linked above.
While the coordinator wrote it, the orbit researcher separately developed a similar narrower symmetric-slab argument; this draft uses the coordinator's single explicit bridge to avoid duplicate proof narratives.
The orbit researcher then read and cross-checked the retained involution, reversed/negated word order, both strip inclusions and pigeonhole count.
That contributor cross-check is not the full independent review of the combined result, which remains pending.

The author ran exact enumeration, numerical path discovery and a separate integer path checker; all 259 candidate paths passed.
The interval enumeration reuses J G0018's reviewed elementary root interval functions, and the path checker uses neither floating-point embeddings nor the reverse search helper.
This distinguishes numerical discovery, exact completeness/path evidence, and mathematical conversion.
Independent review of this new round is pending.
The earlier review of D G0013 does not extend automatically to D G0014.
No fixed L or Claim promotion is asserted.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0068_v1.md#1-algebraic-domain-and-exact-interval-arithmetic), with its original inspected scope and relationship.
