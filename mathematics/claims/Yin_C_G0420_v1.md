---
author: Yin
---

# Complete prefixed amplitude criterion, dense open control and exact limiting boundary

The complete necessary original D47 proof is retained from [L178](../ledger/Yin_L_G0178_v1.md#retained-dense-open-control-argument).
Its drafting agent supplied the prefix, algebraic phase-selection, signed-expansion and boundary derivations.
The coordinator supplied the question and explicitly received this target's preliminary phase-selection discovery during development.
The [original complete finding](../audits/reviews/Yin_R_G0077_v1.md#dense-open-control-independent-review) therefore has known substantive target context and is self-reviewed at its original whole scope.
Its earlier contribution to the fixed L176 exit input does not constitute contribution to this new proof or determine that relationship.
The [original listed author checks](../audits/reviews/Yin_R_G0077_v1.md#prefix-control-original-author-check-finding) retain exactly their named obligations and date precision.
Every necessary prefix/amplitude/dense-open/boundary argument remains here; the full reused pointwise and joint-phase proofs have adequate C homes.
No source/PDF reading, external proof audit, numerical search, J or Task/E execution is added.

## Statement

Let beta in(1,2) be any Salem number of degree2s+2>=4.
Choose one neutral conjugate zeta_j from each unit-circle pair, put A=diag(zeta_j), and use the full real inner product on C^s and chronological original digits{-1,0,1}.
For a nonempty word w of length n write

    c_w=(sum_(i=1)^n eta_i zeta_j^(-i))_j,
    T_w(x)=beta^n x+sum_(i=1)^n eta_i beta^(n-i).

Strict legality means |T_w(x)|<1.
The original PC condition at x in[1/2,1] is: for every real unit direction u some nonempty strictly legal word has u.c_w<0.

For every finite prefix p of length l and suffix w,

    T_(pw)(x)=T_w(T_p(x)),
    c_(pw)=c_p+A^(-l)c_w,
    u.c_(pw)=u.c_p+(A^l u).c_w.

A legal finite suffix hull containing a centered ball of radius r>||c_p|| is sufficient for prefix control.
The exact condition is its directional minimum less than-u.c_p in every unit direction.
For finitely many complete words of lengths at most N and endpoint margins at least epsilon>0, all remain strictly legal for |x'-x|<epsilon beta^(-N).
One fixed periodic loop/exit family has uniformly bounded displacement norm, so repeating it does not supply arbitrarily negative suffix cost for an arbitrary prefix.

For k>=2 sufficiently large, use

    x_k=beta^(k-1)/(beta^k-1) in(1/2,1),
    W_k=(-1,0,...,0), V_k=(-1,0,...,0,-1)

of length k.
For a prefix polynomial f(t)=sum_(i=1)^l eta_i t^(l-i), put

    a_k=beta^(-l)(x_k-f(beta)),
    z_j=zeta_j^(k-1)/(zeta_j^k-1),
    z_(a,j)=zeta_j^(-l)(z_j-f(zeta_j)).

Every word p W_k^r V_k, r>=0, has real endpoint x_k-1 at a_k and displacement

    c_(p W_k^r V_k)=A^(-l-(r+1)k)(z-1)-z_a.

This precise family has a strictly negative cost in every prescribed real unit direction, with a finite r depending on that direction, if and only if

    |z_j-1|>|z_j-f(zeta_j)| for every j.

Its exact directional infimum is-sum_j |u_j||z_j-1|-u.z_a.
A failed coordinate gives a supported direction with all costs nonnegative, including the zero-coordinate case.
When all gaps are positive, finite sphere selection supplies a finite strictly legal full joint hull and a common real neighborhood.
For PC these real points are taken inside the annulus; field membership Q(beta) does not imply order/core membership.

Define the integral Laurent polynomial

    H_f(t)=t(f(t)-1)-t^(-1)(f(t^(-1))-1).

The prefix is nonexceptional exactly when H_f(beta)!=0 as an actual algebraic value.
Then Im[zeta_j(f(zeta_j)-1)]!=0 for every j, by clearing the Laurent denominator and irreducibility.
Writing a variable phase seed as zeta_j^(-1)(1/2+i t_j) gives squared amplitude gap

    1-|f(zeta_j)|^2+Re[zeta_j(f(zeta_j)-1)]
       +2t_j Im[zeta_j(f(zeta_j)-1)].

Choose finite t_j independently to make every gap positive.
Joint density gives arbitrarily large actual k in a common phase neighborhood away from denominator zero.
The corresponding controlled a_k are distinct and converge from above to

    a_infinity=beta^(-l)(beta^(-1)-f(beta)),
    a_k-a_infinity=beta^(-l-k)x_k>0.

For each fixed first l-1 digits, the last choices eta_l=0 and1 have H-value difference beta-beta^(-1)!=0, so at least one single global digit choice is nonexceptional simultaneously at all embeddings.

Every x in[-B,B], B=1/(beta-1)>1, has a signed original-digit beta expansion, proved by the covering remainder intervals.
Truncating the first l-1 digits and making the one global final-digit choice produces nonexceptional centers with

    |a_infinity-x|<=beta^(-l)(beta B+1+beta^(-1)).

Thus every open subinterval of(1/2,1) contains a controlled a_k.
The set of original PC points in[1/2,1] is relatively open and dense.
Its failure set is relatively closed and nowhere dense, without a claim that it is empty, null, countable or quantitatively small.
Relative density near either annulus endpoint does not assert PC at that endpoint.

For the very same words at their own limiting center, the exact endpoint is

    T_(p W_k^r V_k)(a_infinity)
       =-1-x_k(beta^(rk)-1).

It is-1 when r=0 and less than-1 for every r>=1, so none is strictly legal there.
A finite family's immediate common neighborhood radius can be taken as

    (x_k/2) beta^(-l-(r_max+1)k),

which is at most half the center distance.
A prefix followed by digit-1 sends a_infinity to zero, but that co-return supplies no negative neutral directional inequality.
Other words or families may still control such centers.
No limiting-center conclusion, full annulus cover, actual-order membership, general compact termination, uniform word length or unrestricted gap follows from this dense-open theorem.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:07 |
| status | open |
| reason | Retain the entire exact prefixed amplitude equivalence, algebraic phase-selection/single-digit/signed-expansion dense-open proof and limiting-center obstruction, with full chronological costs, strict margins, every domain and residual-set limitation. Actual whole current self-check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete prefix/dense-open/boundary theorem](#statement) | Entire original D47 Sections1--5/formulas(1)--(15) and exact checking/source/domain limits: chronological prefix cost and total-length strict margins, bounded fixed-loop/exit suffix resource, necessary-and-sufficient coordinate amplitude criterion and every supported-direction/zero-coordinate exception, actual algebraic Laurent nonexceptionality and simultaneous embedding slopes, independent finite phase targets/arbitrarily late k, one global original last digit, signed-expansion approximation/dense centers, relatively open dense PC with endpoints and residual-set limits, exact limiting-center endpoint/boundary failure and shrinking neighborhoods, fractional field versus actual order, no global PC/compact termination/uniformity/gap claim. |
| argument | [Entire original proof and exact limits](#argument) | Entire original D47 Sections1--5/formulas(1)--(15) and exact checking/source/domain limits: chronological prefix cost and total-length strict margins, bounded fixed-loop/exit suffix resource, necessary-and-sufficient coordinate amplitude criterion and every supported-direction/zero-coordinate exception, actual algebraic Laurent nonexceptionality and simultaneous embedding slopes, independent finite phase targets/arbitrarily late k, one global original last digit, signed-expansion approximation/dense centers, relatively open dense PC with endpoints and residual-set limits, exact limiting-center endpoint/boundary failure and shrinking neighborhoods, fractional field versus actual order, no global PC/compact termination/uniformity/gap claim. |
| dependency | [Complete original pointwise/finite-hull and strict-strip interface](Yin_C_G0416_v1.md#joint-neutral-pointwise-control) | Only exact pointwise negative-direction/finite convex-hull equivalence, individual positive normalization, finite sphere selection, common strict endpoint margins and original-digit backward expanding strip. Neither global PC nor compact termination is assumed. |
| dependency | [Complete loop/exit cocycle and joint-phase proof](Yin_C_G0417_v3.md#periodic-loop-exit-control) | Only the exact chronological field cocycle, fixed-periodic-loop bounded phase orbit and complete full-product density for every positive power/arbitrarily late visits, with local Galois/finite-polynomial proof and no quantitative first visit. Actual fractional seeds and original alphabet are retained; no global cover/order/core assertion is imported. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:08 |
| status | proved |
| reason | Adopt after actual whole current self-check of all chronological prefix costs/strict margins, fixed-loop bounded-amplitude obstruction, both directions and all exceptions of the exact coordinate-amplitude criterion, algebraic Laurent simultaneous slopes/global digit/finite phase targets, signed-expansion dense-open proof and exact limiting-center boundary failure. The entire proof and necessary complete C416/C417v3 interfaces were checked, not inferred from an old PASS or density alone. No substantive mathematical defect or missing hypothesis was found. Current and original whole findings are self-reviewed at their actual scopes; no global PC, measure-full control, actual-order membership, compact termination or unrestricted gap follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire original D47 Sections1--5/formulas(1)--(15) and exact checking/source/domain limits: chronological prefix cost and total-length strict margins, bounded fixed-loop/exit suffix resource, necessary-and-sufficient coordinate amplitude criterion and every supported-direction/zero-coordinate exception, actual algebraic Laurent nonexceptionality and simultaneous embedding slopes, independent finite phase targets/arbitrarily late k, one global original last digit, signed-expansion approximation/dense centers, relatively open dense PC with endpoints and residual-set limits, exact limiting-center endpoint/boundary failure and shrinking neighborhoods, fractional field versus actual order, no global PC/compact termination/uniformity/gap claim. |
| argument | [Exact retained argument](#argument) | Entire original D47 Sections1--5/formulas(1)--(15) and exact checking/source/domain limits: chronological prefix cost and total-length strict margins, bounded fixed-loop/exit suffix resource, necessary-and-sufficient coordinate amplitude criterion and every supported-direction/zero-coordinate exception, actual algebraic Laurent nonexceptionality and simultaneous embedding slopes, independent finite phase targets/arbitrarily late k, one global original last digit, signed-expansion approximation/dense centers, relatively open dense PC with endpoints and residual-set limits, exact limiting-center endpoint/boundary failure and shrinking neighborhoods, fractional field versus actual order, no global PC/compact termination/uniformity/gap claim. |
| dependency | [Exact retained dependency](Yin_C_G0416_v1.md#joint-neutral-pointwise-control) | Only exact pointwise negative-direction/finite convex-hull equivalence, individual positive normalization, finite sphere selection, common strict endpoint margins and original-digit backward expanding strip. Neither global PC nor compact termination is assumed. |
| dependency | [Exact retained dependency](Yin_C_G0417_v3.md#periodic-loop-exit-control) | Only the exact chronological field cocycle, fixed-periodic-loop bounded phase orbit and complete full-product density for every positive power/arbitrarily late visits, with local Galois/finite-polynomial proof and no quantitative first visit. Actual fractional seeds and original alphabet are retained; no global cover/order/core assertion is imported. |
| review | [Complete actual current whole self finding](../audits/reviews/Yin_R_G0622_v1.md#current-prefixed-control-whole-finding) | Entire original D47 Sections1--5/formulas(1)--(15) and exact checking/source/domain limits: chronological prefix cost and total-length strict margins, bounded fixed-loop/exit suffix resource, necessary-and-sufficient coordinate amplitude criterion and every supported-direction/zero-coordinate exception, actual algebraic Laurent nonexceptionality and simultaneous embedding slopes, independent finite phase targets/arbitrarily late k, one global original last digit, signed-expansion approximation/dense centers, relatively open dense PC with endpoints and residual-set limits, exact limiting-center endpoint/boundary failure and shrinking neighborhoods, fractional field versus actual order, no global PC/compact termination/uniformity/gap claim. Actual current whole relationship is self-reviewed; the original whole SELF and precisely listed original author SELF remain separate. |

## Complete retained argument

<a id="argument"></a>
<a id="retained-dense-open-control-argument"></a>
<a id="dense-open-control-fixed-scope"></a>

<a id="prefix-control-cost-and-margin"></a>
### 1. Exact prefix propagation and the bounded-suffix obstruction

Use the Salem beta, selected unit conjugates zeta_j, neutral rotation A, endpoint legality and chronological original-digit words of [complete pointwise/finite-hull theorem](Yin_C_G0416_v1.md#joint-neutral-pointwise-control).
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
Indeed [complete loop/exit cocycle](Yin_C_G0417_v3.md#periodic-loop-exit-control), at a field seed with neutral vector z and loop length k, reads

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

For k>=2 use the same seed, loop and exit as C417:

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

To prove it, the positive-power joint density already completely proved in [complete joint-phase proof](Yin_C_G0417_v3.md#salem-joint-phase-density) applies to A^k.
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

Openness is the finite sphere selection and common strict real margin proved in C416.
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
The backward real-strip estimate of C416 applies to these words; intermediate real legality has not been silently replaced by a different alphabet.
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

## Original checking and exact remaining gate

All prefix, amplitude, Laurent, expansion, strict-margin and boundary mathematics needed for the theorem is explicit above.
The original author check and coordinator's receipt of the preliminary phase-selection discovery are retained at their actual L178/R77 homes.
The existing frozen L176 exit contribution and subsequent zero-state suggestion are kept at their distinct actual scopes.
Neither supplies a new independent finding of this theorem.

The dense-open conclusion leaves a relatively closed nowhere-dense possible failure set.
It provides no assertion of full measure, emptiness, countability, control at every limiting center or a compact cover of the full annulus.
Even a later global PC theorem would leave compact termination and unchanged original-law quantitative estimates separate.
Original exploration, frozen/pending/fixed-retention wording, date precision and Task history remain historical at L178.
The current whole finding must check every implication and negative boundary, not only the proof-location change.
