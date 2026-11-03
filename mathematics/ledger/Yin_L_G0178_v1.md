---
author: Yin
---
# Dense open joint control and the exact strict-boundary obstruction

Date: 2026-10-10.
Fixed retention under the coordinating AI for Yin's explicit adoption instruction after its complete separately organized noncontributor review.
This records the restricted result below; G0001 remains active and unresolved, with no C acceptance or Task-completion decision.

<a id="dense-open-control-fixed-scope"></a>
## Adopted scope and preserved account

For every Salem beta in(1,2), the real points satisfying the original strict joint-neutral PC condition form a relatively open dense subset of[1/2,1].
The complete [prefix-amplitude criterion](#periodic-prefix-amplitude-criterion), [algebraic phase selection](#nonexceptional-prefix-phase-selection) and [dense-open proof](#dense-open-salem-pointwise-control) are retained below.
The [exact boundary calculation](#strict-boundary-failure-of-seed-limit) explains why this same family does not control its own limiting centers.
The residual failure set is relatively closed and nowhere dense; it is not proved empty, null or countable.
There is no general compact termination or uniform gap conclusion.

The complete original D G0047 account follows, including all proofs, limitations and the full independent finding.
Historical pending-review/fixed-adoption wording is superseded only by this current adoption statement.
Retention changes heading depth and navigation, not the inspected mathematics or review history.

<a id="retained-dense-open-control-argument"></a>
## Complete original proof and independent review

## Propagating joint control: exact prefix costs and endpoint-amplitude gates

Date: 2026-10-10.
The input is the fixed [L176](Yin_L_G0176_v1.md#joint-control-fixed-scope).
The coordinator supplied the research question only; the derivations below are the drafting agent's.
This is a working argument, not an independently reviewed or fixed result.

### Question and reuse boundary

Can the locally controlled periodic seeds be propagated through real prefixes to cover the annulus?
The exact concatenation cost and strict real margin must be retained.
Repeating a loop before one fixed exit has bounded neutral displacement, so an assertion of arbitrarily large negative suffix cost needs a new mechanism.
We seek a precise sufficient propagation theorem or a concrete obstruction, without inferring coverage from density.

<a id="prefix-control-cost-and-margin"></a>
### 1. Exact prefix propagation and the bounded-suffix obstruction

Use the Salem beta, selected unit conjugates zeta_j, neutral rotation A, endpoint legality and chronological original-digit words of [L176](Yin_L_G0176_v1.md#joint-neutral-pointwise-control).
A prefix p of length l has real offset b_p and neutral displacement c_p.
For a suffix w of length k,

    T_(pw)(x)=T_w(T_p(x)),
    c_(pw)=c_p+A^(-l)c_w,
    u.c_(pw)=u.c_p+(A^l u).c_w.                       (1)

The rotation is orthogonal on the complete real neutral space.
A finite suffix family legal at y=T_p(x), with convex hull containing a centered ball of radius r, therefore gives control at x if r>||c_p||.
More exactly, one must check

    min_w (A^l u).c_w < -u.c_p for every unit u.       (2)

If those finitely many complete words have lengths at most N and endpoint margins at least epsilon>0 at x, they remain strictly legal for |x'-x|<epsilon beta^(-N).
This is the actual continuity cost; a suffix legal only at one real point does not automatically remain legal after a long approximate prefix or many loops.

Repeating an exact periodic loop before a single fixed exit supplies no unbounded negative resource.
Indeed [L176's cocycle](Yin_L_G0176_v1.md#periodic-loop-exit-control), at a field seed with neutral vector z and loop length k, reads

    c_(W^r V)=A^(-rk)h-z,   h=z+c_V,
    ||c_(W^r V)|| <= ||h||+||z|| for every r>=0.       (3)

Consequently every directional cost in that family is bounded below.
Increasing r changes phase, not the available amplitudes.
If a proposed prefix has u.c_p>||h||+||z|| in some unit direction, no member of this suffix family can give negative total cost in that direction.
This is a mechanism-specific obstruction, not an assertion that arbitrary legal suffixes have bounded cost.

The same issue can be resolved without arbitrarily large suffix negativity when the endpoint amplitudes are tailored to the prefix.
The rest of this argument does that exactly and yields genuine additional real coverage.

<a id="periodic-prefix-amplitude-criterion"></a>
### 2. An exact amplitude criterion for a prefixed periodic family

For k>=2 use the same seed, loop and exit as L176:

    x_k=beta^(k-1)/(beta^k-1),
    W_k=(-1,0,...,0),  V_k=(-1,0,...,0,-1),
    T_(W_k)(x_k)=x_k,  T_(V_k)(x_k)=x_k-1.

Choose k large enough that 1/2<x_k<1.
Write the prefix as p=(eta_1,...,eta_l), and put

    f(t)=sum_(i=1)^l eta_i t^(l-i),
    a_k=beta^(-l)(x_k-f(beta)),
    z_j=zeta_j^(k-1)/(zeta_j^k-1),
    z_(a,j)=zeta_j^(-l)(z_j-f(zeta_j)).               (4)

Thus T_p(a_k)=x_k.
The numbers a_k and x_k lie in Q(beta); no order membership or actual-core status is assumed by the real pointwise-control criterion.
Every word p W_k^r V_k has the same strictly legal real endpoint x_k-1 at a_k.
Its neutral displacement is exactly

    c_(p W_k^r V_k)=A^(-l-(r+1)k)(z-1)-z_a.         (5)

This follows either by substituting(1) or by applying the field cocycle to the complete word.
In particular the prefix displacement has not been dropped.

**Exact family criterion.** This family has a strictly negative displacement in every unit direction if and only if

    |z_j-1| > |z_j-f(zeta_j)| for every j.            (6)

To prove it, the positive-power joint density already completely proved in [L176](Yin_L_G0176_v1.md#salem-joint-phase-density) applies to A^k.
The fixed factor A^(-l-k) does not alter coordinate moduli.
Therefore for each real unit u the exact infimum over r>=0 is

    inf_r u.c_(p W_k^r V_k)
       =-sum_j |u_j| |z_j-1| - u.z_a.                (7)

If all gaps in(6) are positive, this is at most minus their minimum, because sum_j|u_j|>=1 and |z_(a,j)|=|z_j-f(zeta_j)|.
The strictly negative infimum gives an actual finite r in each direction; the finite sphere argument selects finitely many such words and a strict common real neighborhood.
Conversely, if |z_j-1|<=|z_(a,j)| for one coordinate with z_(a,j)!=0, take u supported there, equal to -z_(a,j)/|z_(a,j)|.
Every cost is nonnegative.
If z_(a,j)=0 and that failed inequality holds, both moduli vanish and the costs in every direction supported there are zero.
Thus the family fails the required strict condition.
This also explains the exact product-of-disks convex-hull geometry without assuming a finite orbit.

<a id="nonexceptional-prefix-phase-selection"></a>
### 3. The algebraic exception and independent phase selection

The prefix is called nonexceptional here precisely when the integral Laurent polynomial

    H_f(t)=t(f(t)-1)-t^(-1)(f(t^(-1))-1)              (8)

does not vanish at beta.
This is an algebraic condition on the actual polynomial value, not merely a formal nonzero coefficient test.

At a unit conjugate, H_f(zeta_j)=2i Im[zeta_j(f(zeta_j)-1)].
If H_f vanishes at any conjugate of beta, multiplying by a sufficiently large power of t gives a rational polynomial divisible by beta's irreducible minimal polynomial.
It then vanishes at all its conjugates.
Consequently a nonexceptional prefix satisfies

    Im[zeta_j(f(zeta_j)-1)] != 0 for every j.          (9)

The converse also follows by the same argument.
All embeddings are nonzero, so multiplication by that power introduces no issue.

For a variable phase q on the unit circle other than1,

    z=zeta_j^(-1) q/(q-1)
     =zeta_j^(-1)(1/2+i t_j),   t_j in R.

As q varies, t_j runs through every real value.
With f_j=f(zeta_j), the squared gap in(6) is

    |z-1|^2-|z-f_j|^2
      =1-|f_j|^2+Re[zeta_j(f_j-1)]
           +2 t_j Im[zeta_j(f_j-1)].                (10)

By(9), choose a finite real t_j making this gap strictly positive, independently for each j.
The corresponding target phases q_j are different from1.
Continuity gives one open joint phase neighborhood, away from all zero denominators, where all gaps remain positive.
Joint density gives arbitrarily large k with (zeta_1^k,...,zeta_s^k) in that neighborhood.
The real seed condition holds for all sufficiently large such k.
Hence the exact family criterion proves PC at each corresponding a_k.
Their limits are

    a_infinity=beta^(-l)(beta^(-1)-f(beta)),
    a_k-a_infinity=beta^(-l-k) x_k > 0.              (11)

If a_infinity belongs to(1/2,1), then every sufficiently large selected a_k also belongs to that annulus.
These are distinct controlled real points, each with a nonempty open controlled neighborhood.
The argument proves no common size for these neighborhoods.

The nonexceptional requirement is easy to arrange without losing the prefix alphabet.
Fix its first l-1 digits and write their shifted polynomial as t g(t).
The two choices eta_l=0 or1 give f_0=t g and f_1=t g+1, with

    H_(f_1)(t)-H_(f_0)(t)=t-t^(-1).                 (12)

Since beta>1, the two Laurent polynomials cannot both vanish at beta.
At least one of these final-digit choices is nonexceptional.
This is a single global choice valid simultaneously for every neutral pair, not a separate digit choice at each embedding.

<a id="dense-open-salem-pointwise-control"></a>
### 4. Open dense pointwise control for every Salem beta in(1,2)

**Theorem.** For every Salem beta in(1,2), the set of real x in[1/2,1] satisfying the original strict PC condition is relatively open and dense.
Its relatively closed failure set is nowhere dense.
No assertion that the failure set is empty, null, countable or quantitatively small is made.

Openness is the finite sphere selection and common strict real margin proved in L176.
It suffices to show that every open subinterval of(1/2,1) contains one of the controlled points from Section3.

Put B=1/(beta-1)>1.
Every x in[-B,B] has a signed beta expansion

    x=sum_(i=1)^infinity a_i beta^(-i),
    a_i in {-1,0,1}.

For completeness, beta[-B,B]=[-B-1,B+1].
The three intervals [-B,B]+a for a=-1,0,1 cover this interval because B>1.
Given a remainder r in[-B,B], choose a with beta r-a in[-B,B] and iterate.
After n steps the error is beta^(-n) r_n, bounded by B beta^(-n) and tending to zero.
This proves the asserted expansion without a source theorem or an eventual-periodicity assumption.

Fix any x in(1/2,1) and use the first l-1 expansion digits to set eta_i=-a_i.
Choose eta_l in{0,1} by(12), giving a nonexceptional prefix.
The associated limiting center obeys

    a_infinity=sum_(i=1)^(l-1) a_i beta^(-i)
                  -eta_l beta^(-l)+beta^(-l-1),
    |a_infinity-x|
       <= beta^(-l)(beta B+1+beta^(-1)).             (13)

Thus these nonexceptional centers are dense in the open annulus: for a prescribed interval first choose x in its interior and then l sufficiently large that the bound puts a_infinity strictly inside the interval.
Section3 supplies arbitrarily large selected k for which a_k lies in the same interval and satisfies PC.
Therefore controlled points are dense.
Combining density with openness gives the theorem, including relative density at the two endpoints of the closed annulus.
Their own PC status is not asserted.

All successful controls use finite words p W_k^r V_k in the unchanged original alphabet.
They are legal at the specific real point by their exact endpoint x_k-1, and a finite family is legal on a common open neighborhood.
The backward real-strip estimate of L176 applies to these words; intermediate real legality has not been silently replaced by a different alphabet.
This is a statement on real PC, not membership of these fractional field points in the actual algebraic order or return core.

<a id="strict-boundary-failure-of-seed-limit"></a>
### 5. Why this still does not cover the limiting centers

There is an exact obstruction to passing this construction to the center a_infinity of(11).
For every r>=0, evaluate the same word at that center instead of a_k.
Its affine slope and(11) give

    T_(p W_k^r V_k)(a_infinity)
       =(x_k-1)-beta^(l+(r+1)k)(a_k-a_infinity)
       =-1-x_k(beta^(rk)-1).                         (14)

For r=0 this is exactly -1, and for r>=1 it is strictly smaller than -1.
Thus none of these words is strictly legal at its own limiting center, for any selected k.
This is stronger than merely having no known uniform neighborhood size.
It identifies the exact boundary equality responsible for the failed limiting inference.

At a_k the endpoint margin is x_k, so if a selected finite family has largest repetition r_max, its immediate common neighborhood radius may be taken as

    epsilon_k=(x_k/2) beta^(-l-(r_max+1)k).           (15)

For even r_max=0 this is only half the center distance in(11); larger repetitions shrink it further.
Other control words or other prefix families may control that center.
Indeed T_p(a_infinity)=beta^(-1), and one more digit -1 sends it exactly to0.
This co-return observation by itself supplies no negative neutral directional cost, and does not repair the failed strict legality of(14).

An open dense controlled set permits an arbitrary relatively closed nowhere-dense failure set at the present proof scope; such sets need not have measure zero.
Compactness does not produce a finite cover of the whole annulus unless PC is proved at every remaining point.
Thus neither global PC nor general compact termination nor the unrestricted G0001 conclusion follows here.

### 6. Remaining gate and checking boundary

The useful next question is whether a second, genuinely different exit or a recurrent controlled real region can control the residual points, including the exact boundary centers in(14).
Equation(2) states the necessary prefix accounting.
Unbounded directional negativity could be sufficient when correctly aligned and legal, but(3) proves that mere repetition of one loop before one fixed exit cannot supply it.
The dense-open theorem instead succeeds by selecting amplitudes jointly with the prefix, through the exact nonexceptional algebraic test(8).

This round reused the full fixed L176 PC interface, joint-density proof, chronological cocycle and strict-neighborhood compactness argument.
A targeted local reuse check found no existing prefixed amplitude criterion or dense-open PC statement in the retained G materials.
No external theorem, new literature artifact, numerical experiment or program is a premise.
The signed-expansion, exceptional-prefix and margin arguments are all proved above.
The coordinator supplied the research question and received the preliminary phase-selection discovery; it did not supply these derivations.

The drafting agent checked word order, the signs in(1),(5),(10), the irreducible-polynomial argument for simultaneous nonzero slopes, the single global last-digit choice, the actual density quantifiers, the exact boundary value and the source/domain limits.
This is author checking only.
A complete separate review and fixed adoption remain pending.
The full gap Task remains active and unresolved.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0077_v1.md#dense-open-control-independent-review), with its original inspected scope and relationship.

## Retention and contribution boundaries

The drafting agent supplied the complete argument.
The coordinating AI assigned the question but supplied none of these derivations and completed the separately organized, nonblind noncontributor review preserved above.
Its earlier contribution to a fixed L176 exit construction remains disclosed there.
The new zero-state suggestion belongs to the subsequent research round, not to this inspected proof.
Mechanical retention by the author implements the coordinator's adoption and does not substitute for the independent finding.

The retired identity D G0047 is preserved in full at [its original account](#retained-dense-open-control-argument), including [all six mathematical sections](#prefix-control-cost-and-margin) and the [complete review](../audits/reviews/Yin_R_G0077_v1.md#dense-open-control-independent-review).
No program or J exists for this proof-only round, and no fixed prior mathematical input is changed.
