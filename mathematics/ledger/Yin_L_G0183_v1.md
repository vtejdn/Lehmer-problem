---
author: Yin
---
# Compact termination certificates, full-path traps and arithmetic-domain controls

Date: 2026-10-10.
Fixed retention under the coordinating AI for Yin's explicit adoption after its complete separately organized noncontributor review.
This is a restricted mathematical adoption, not C acceptance or Task completion.
G0001 remains active and unresolved.

<a id="compact-termination-controls-fixed-scope"></a>
## Current adopted scope

The [finite-certificate equivalence](#compact-termination-certificate-interface) states exactly what remains after fixed-input compact reduction.
The [unbounded-excursion theorem](#unbounded-legal-excursions-no-finite-trap) rules out finite sets closed under all admissible original paths, while leaving infinite possible nonreturn basins unresolved.
[Finite ideal quotients](#original-digit-finite-quotient-connectivity) are algebraically strongly connected, without a real-legality conclusion.
The [actual Lehmer two-cycle](#actual-lehmer-compact-cycle-control) demonstrates a cycling policy at states which do return through other words.
The [index-five fractional-module control](#fractional-module-five-class-obstruction) exhibits a genuine obstruction outside the actual order.
None of these deductions proves universal actual-order termination.

The complete original D G0052 argument and review follow.
Historical pending-review wording is superseded only by this adoption statement.
The retention changes headings and navigation, preserving all proofs, scope boundaries and review facts.

<a id="retained-compact-termination-controls"></a>
## Complete original argument and independent review

## Compact termination: finite certificates, unavoidable excursions and exact cycle controls

Date: 2026-10-10.
The coordinator assigned the compact-termination question after [L180's global small-Salem control](Yin_L_G0180_v1.md#small-salem-global-pointwise-control).
The drafting agent develops the deductions below.
This is a working argument pending independent review, not a universal termination theorem.

### Question and reuse boundary

Global PC gives compact reduction, not exact co-return.
Determine what a finite sufficient certificate must cover, whether a compact cycle can be mistaken for a true obstruction, and whether a proper ideal can separate an actual state from zero.
Use the original alphabet, the actual order Z[beta], and every embedding.
Avoid inferring termination from finite trajectories or from controllability alone.

<a id="compact-termination-certificate-interface"></a>
### 1. The exact finite certificate left after global PC

Fix a Salem beta in(1,phi), O=Z[beta], B=1/(beta-1), S=beta/(beta-1), and the joint neutral norm rho from the fixed control interface.
Put

    N={x in O: |x_+|<=1, |x_-|<=S},
    Omega={x in O: |x_+|<B, |x_-|<=S}.

The [L180 theorem](Yin_L_G0180_v1.md#small-salem-global-pointwise-control) and the [L176 descent interface](Yin_L_G0176_v1.md#joint-neutral-pointwise-control) give some finite R such that each x in N has a finite original-digit continuation into

    K_R={x in N: rho(x)<=R}.                          (1)

Enlarge R if needed; the proven reduction to a strict smaller radius then still lands in K_R.
The full embedding map is an invertible real linear map on the coefficient space of O, so its image is a full lattice.
The bounded real, stable and neutral coordinates in(1) imply that K_R is finite.
This argument requires all embeddings, not only a real projection.

**Finite certificate criterion.** Every x in N co-returns to0 if and only if every k in K_R has a finite original-digit word ending exactly at0.
The forward implication restricts the asserted property to K_R; the reverse implication concatenates the known compact-reduction path with the supplied finite continuation.
A certificate can list one exact continuation for each nonzero k.
Equivalently, assign a nonnegative integer rank h to K_R, with h(0)=0 and h(k)>0 otherwise, and for every k!=0 give a nonempty original word ending at a member of K_R of strictly smaller rank.
Repeated strict rank decrease proves termination.
Conversely, direct zero continuations give the rank-one certificate.
Empty words at0 are harmless.

An executable certificate must prove that its state list or exact superset covers every actual K_R point, using complete coefficient bounds and embedding inequalities; visiting many states does not prove exhaustion.
Each word can then be checked by exact arithmetic modulo beta's minimal polynomial.
A certified superset is sufficient if every listed actual state has a zero continuation, or every excess candidate is exactly excluded.
If a selected word ends at a smaller-ranked state, its entire digit order and algebraic endpoint must be checked.
Its intermediate stable coordinate stays within S; backward estimation from the final narrow endpoint places every preceding real value strictly inside(-B,B).
There is no need to require all intermediate states to stay in the compact residue.

For a fixed fully specified finite K_R, breadth-first word enumeration is a semidecision for this positive certificate: it eventually finds a continuation for every state if all exist.
Failure at a finite search horizon is not a no-return proof.
This paragraph does not provide a computed R, a general termination algorithm with a stopping bound, or a universal certificate.
L169/L170 supply completed examples; no new input-by-input enumeration is performed here.

<a id="unbounded-legal-excursions-no-finite-trap"></a>
### 2. Global unbounded cost rules out finite fully closed traps

The stronger L180 proof yields more than a finite descent cover.
For every x in N and every H>0, there is an original-digit word whose endpoint y is again in N and satisfies rho(y)>H.
Here is the precise extension from its stated annulus.

For 0<|x_+|<1/2, zero digits bring the magnitude into[1/2,beta/2), so into the annulus, without a neutral prefix displacement.
Negative values are handled by negating the word and the direction.
At x_+=0, injectivity of the real embedding gives x=0.
The preserved original D51 Section3 proof applies directly at real zero: for every direction its interval I_u=(P_0-B,P_0) contains0 by the two strict sign bounds.
It therefore supplies arbitrarily negative legal costs at0 as well.
This uses an explicit proved part of that argument, not a new assumption that annulus control automatically transfers to zero.

For a general fixed x, choose a real unit direction u and a strictly legal word w with

    u.c_w < -(H+rho(x)).

If w has length n, its neutral endpoint satisfies the field cocycle

    z_y=A^n(z_x+c_w),
    rho(y)=||z_x+c_w|| >= ||c_w||-rho(x)>H.           (2)

For the zero/sign preliminary prefixes, the exact concatenation cost is retained; the unbounded suffix absorbs any finite cost.
The endpoint is narrow.
Every original digit preserves the stable bound, and backward real estimation from that narrow endpoint keeps the whole word in Omega.
Thus this is an actual legal excursion, not just a formal large neutral vector.

Consequently no nonempty finite subset of N can be closed under every original word staying in Omega and ending in N.
In particular a finite set of compact states cannot be a complete closed obstruction merely because one chosen policy cycles inside it.
More generally no nonempty finite subset of Omega can be closed under all one-step original transitions which remain in Omega: from any of its states, the usual opposite-sign correction reaches N in finitely many steps, since its distance from the real boundary B grows by beta until it is narrow.
Then(2) contradicts finite closure.
Stable bounds remain invariant throughout.

This still does not prove exact co-return.
If some x in N has no continuation to0, every state reachable from x also lacks a continuation to0, by concatenation.
Formula(2) makes that no-return reachable basin infinite and neutral-unbounded.
Compact descent maps those endpoints back into the finite set of no-return members of K_R.
Thus the possible obstruction is an infinite excursion basin with a finite compact residue, not a finite set closed under all full transitions.

One can make this last distinction exact.
If the no-return part of K_R is nonempty, fix any H>R.
From each of its states choose an excursion beyond H using(2), then a compact reduction back to a no-return member of K_R.
These choices define a map on a finite nonempty set, hence some cycle of compact vertices.
Each edge is an actual finite word with an intermediate neutral norm exceeding H.
Such arbitrarily large excursion-return cycles would be necessary for a failed universal termination statement.
The argument neither constructs such a no-return basin nor excludes it; actual returning basins can also have large excursions.

<a id="original-digit-finite-quotient-connectivity"></a>
### 3. Finite ideals cannot provide an algebraic digit obstruction

**Theorem.** For any algebraic unit beta, O=Z[beta], and any nonzero proper ideal I of O, the finite quotient O/I is strongly connected under x -> beta*x+eta with eta in{-1,0,1}.
In fact the digits0 and1 already suffice at a single common word length depending on the quotient.
This theorem concerns the quotient graph alone, without real-coordinate legality.

The quotient is finite: choose nonzero a in I.
Multiplication by a on the rank-d free abelian group O has nonzero determinant N(a), so O/aO is finite, and O/I is its quotient.
Let q be the positive additive characteristic of O/I and let h be the finite multiplicative order of the unit beta modulo I.
Choose

    N=q h.

Every residue t in O/I is an integral combination of powers of beta.
Reducing exponents modulo h and coefficients modulo q writes it as

    t=sum_(r=0)^(h-1) c_r beta^r,  0<=c_r<q.

Place a coefficient1 at each exponent r+kh for0<=k<c_r and coefficient0 at every remaining exponent from0 to N-1.
These positions are distinct and less than N, and beta^h=1 in the quotient.
Thus the resulting original-digit polynomial F has F(beta)=t modulo I.
Since beta^N=1 modulo I, reading its coefficients in descending chronological order sends any residue x to x+t.
Choosing t=y-x realizes any desired ordered pair x,y.
This proves the assertion with the complete original digit constraint.

A finite family of ideal congruences gives no stronger algebraic obstruction: its intersection is again a finite-index nonzero ideal, and the same construction applies simultaneously.
Nor is there a proper digit-generated ideal here, since digit1 is a unit.
However the constructed quotient word may leave the real strip; no bounded-length legal real continuation has been proved by this quotient argument.
A possible actual obstruction must retain more than finitely many ideal residues or impose additional analytic/path constraints.
Solving every finite congruence does not imply solving the exact equation in O.

<a id="actual-lehmer-compact-cycle-control"></a>
### 4. An actual compact two-cycle that nevertheless returns

Use the original Lehmer Salem unit from [L170](Yin_L_G0170_v1.md#lehmer-infinite-core-theorem), whose certified beta lies in(117/100,118/100), hence below phi.
Its minimal polynomial satisfies the exact identity

    P(t)=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1
        =(t+1)(t^9-t^6-t^4-t^2+t)+1.

Therefore the actual order element

    a=1/(beta+1)=-beta^9+beta^6+beta^4+beta^2-beta    (3)

has the original-digit two-cycle

    a --(-1)--> -a --(+1)--> a.

Indeed beta a-1=-a.
Its real magnitude is less than1/2, its stable magnitude is beta/(beta+1)<1, and all neutral magnitudes1/|zeta_j+1| are finite because no unit conjugate is-1.
Both states lie in a bounded full-coordinate compact set inside N.
Choosing a compact reduction radius large enough includes them in K_R, without invalidating the original reduction theorem.

Nevertheless L170's complete narrow-domain co-return theorem applies to both actual states.
Its exact open-strip theorem also places them in the actual return core: their real and stable values are strictly inside the required bounds.
Thus the displayed two-cycle is a fully legitimate possible trajectory in the original alphabet, but it is not a nonreturn trap.
A test which follows only the digit opposite the current sign at these states loops forever and misses their other finite zero continuation.
Detecting this policy cycle cannot replace exhaustive coverage or a ranked certificate.
No new return word or numerical experiment is claimed here; the existence of another continuation is reused from the already fixed full theorem.

<a id="fractional-module-five-class-obstruction"></a>
### 5. Why the actual digit-generated module is essential

For a separate exact control, consider

    P_6(t)=t^6-t^5-t^3-t+1,
    t^(-3)P_6(t)=Q(t+t^(-1)),
    Q(v)=v^3-v^2-3v+1.                              (4)

The signs Q(-2)=-5, Q(-1)=2, Q(0)=1, Q(1)=-2 and Q(2)=-1, Q(sqrt5)=2sqrt5-4>0 put its three roots in(-2,-1),(0,1),(2,sqrt5).
These intervals exhaust its degree.
The only possible rational roots are+/-1, neither a root, so Q is irreducible.
It defines a totally real cubic field.
The discriminant v^2-4 of t^2-vt+1 is negative at an inner real embedding and hence cannot be a square in that field.
The quadratic extension has degree six, proving P_6 irreducible.
Its outer trace root yields a Salem beta with1<beta<phi, since phi+phi^(-1)=sqrt5.
Thus the global PC theorem applies to this actual base.

But P_6(-1)=5.
The fractional point a=1/(beta+1) has absolute field norm1/5, so it is not an algebraic integer and is not in O.
It lies in the larger lattice module

    M=(beta+1)^(-1)O,
    [M:O]=5.

The index follows from the determinant of multiplication by beta+1.
This module is invariant under multiplication by the unit beta and under addition of the original digits.
Modulo O its nonzero class obeys beta a=-a.
Hence any original word of length n starting at a has class (-1)^n a+O, never zero.
There is no finite co-return to0 from a or-a.

The same two-cycle +/-a is strictly narrow, has stable magnitude beta/(beta+1)<1 and finite neutral coordinates.
PC still applies to its real coordinates, and the compact-reduction argument works in the full lattice M just as a norm reduction.
It must leave a nonzero compact residue because of the invariant nonzero fractional class.
Thus global control, a discrete full embedding lattice and finite compact reduction do not logically imply termination without the exact arithmetic-domain condition.
This is an explicit control in a larger module, not a counterexample to actual compact termination in O.
The obstruction also does not contradict Section3: it is a nonzero coset of M/O containing no actual O state, not a separation between two states of O modulo an ideal of O.

### 6. Remaining gate and checking boundary

For actual O states, the unresolved step remains a finite exact continuation certificate for every residual state, or a general theorem furnishing those continuations.
Sections2--3 restrict simplistic obstruction models: a failed basin must have unbounded legal excursions, and no finite ideal congruence alone can block original algebraic words.
Section4 shows that a cycling policy can coexist with actual co-return; Section5 shows why enlarging the state module can manufacture a genuine obstruction which does not answer the actual question.

The local reuse screen read L176/L180's complete reduction and unbounded-cost interfaces, L170's actual Lehmer and open-strip theorem, and the L157 golden-ratio cycle discussion.
The latter is a different nonreciprocal input and convention-transfer example; it does not supply the new actual Lehmer identity or the module obstruction here.
A targeted retained-G search found no existing finite-quotient construction or this exact cubic control.
All new algebra and graph arguments are displayed directly.
No additional source theorem, source intake, numerical enumeration or J is needed or claimed.

The drafting agent checked every domain, the cocycle norm inequality, preservation of the two real bounds, the quotient word's exponent order, the polynomial identity(3), all cubic signs and the fractional index.
These are author checks only.
Complete independent review and fixed adoption remain pending.
There is no universal compact-termination assertion or unrestricted G0001 conclusion.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0082_v1.md#compact-termination-controls-independent-review), with its original inspected scope and relationship.

## Retention and contribution boundary

The drafting structural agent supplied the new deductions.
The coordinator assigned the question and received progress explanations but supplied none of those arguments.
It authored an underlying fixed L180 theorem, whose independent review is retained there; its new D52 review is noncontributing at the exact scope disclosed in the full finding above.
Author retention implements coordinating adoption and is not a substitute independent review.

The retired working identity D G0052 is preserved in full at [the original account](#retained-compact-termination-controls), with all six sections and [complete independent finding](../audits/reviews/Yin_R_G0082_v1.md#compact-termination-controls-independent-review).
The complete review identifies the original argument and its inspected scope.
Actual incoming references were relocated.
No computation or J was introduced, and no earlier fixed mathematical body was changed.
