---
author: Yin
---
# Global small-Salem control and complementary zero-exit transport

Date: 2026-10-10.
Fixed retention under the coordinating AI for Yin's explicit adoption instruction after the complete separate D48 review and both complete separate D51 reviews.
This is restricted mathematical adoption, not C acceptance or Task completion.
G0001 remains active and unresolved.

<a id="global-control-fixed-scope"></a>
## Adopted conclusions and distinct proof inputs

For every Salem beta in(1,phi), phi=(1+sqrt5)/2, the [complete sparse-digit theorem](#small-salem-global-pointwise-control) proves original-digit strict PC at every real x in[1/2,1].
More strongly, for every nonzero neutral direction, strictly legal finite-word costs are unbounded below.
The fixed L176 interface therefore supplies a finite convex cover and compact neutral reduction for each such input.
Compact termination, actual-core equality, effective or degree-uniform costs and original-law gap estimates remain separate.

For every Salem beta in(1,2), the [zero-exit support criterion](#zero-exit-amplitude-support-criterion) exactly retains the cost of a prefix returning to zero, and the [coordinatewise unboundedness criterion](#coordinatewise-unbounded-exit-gate) identifies when this word family supplies arbitrarily negative costs in every direction.
The separate [Fen16-based norm argument](#height-one-spectrum-neutral-growth) proves at least one coordinate unbounded and controls all full-support directions.
With one neutral pair it proves [PC at every finite co-return point for every degree-four Salem beta in(1,2)](#quartic-co-return-point-control).
The exact prefix-family criterion and its higher-dimensional scope are preserved; the complementary theorem does not independently prove each coordinate unbounded for all beta in(1,2).

The global beta<phi proof uses no external spectrum theorem.
Fen16 Theorem1.2 is an accepted, statement-checked external input only to the complementary scalar-density/norm route; its source proof was not re-audited.
The complete proofs, original checking facts and dated restricted-retention account follow.
The retained D51 reviews and exact original author checks keep their actual scopes in R79.
Original pending/review-ready wording is historical and superseded only by the present adoption statement.
Only heading depth and navigation are relocated.

<a id="retained-zero-exit-control-argument"></a>
## Complete original D G0048 argument and review

## Zero-state exits, exact prefix transport and neutral amplitude growth

Date: 2026-10-10.
The coordinator supplied the observation that (1,-1) exits zero at beta-1, with nonzero neutral endpoints, and that leading zero digits rotate its displacement through a full joint phase orbit.
The further amplitude criteria and source deductions below belong to the drafting agent.
This working argument is not independently reviewed or fixed.

### Question

Does control at zero propagate through exact co-return prefixes after paying their neutral displacement?
Identify the precise stronger exit-amplitude condition.
A bounded primary-source screen of the unchanged height-one spectrum may inform the missing arithmetic step; real density alone must not be silently upgraded to simultaneous neutral growth.

<a id="zero-state-phase-control"></a>
### 1. The coordinator's zero-state control and its actual size

Use [L176's](Yin_L_G0176_v1.md#joint-neutral-pointwise-control) Salem beta in(1,2), degree2s+2, selected unit conjugates zeta_j, neutral rotation A and strict endpoint legality.
For a finite original-digit word v of length k, let E_v=T_v(0) and let z_v be its joint neutral embedding vector.
Then c_v=A^(-k)z_v.
Any number r>=0 of leading zero digits leaves the real endpoint E_v unchanged and gives

    c_(0^r v)=A^(-r-k)z_v.                           (1)

The coordinator supplied v=(1,-1): E_v=beta-1 lies in(0,1), and z_(v,j)=zeta_j-1 is nonzero at every coordinate.
Full joint phase density from L176 yields

    inf_(r>=0) u.c_(0^r v)=-sum_j |u_j| |zeta_j-1|
       <= -min_j |zeta_j-1| < 0                      (2)

for each real unit direction u.
Finite sphere selection gives PC at0 and on a common open real neighborhood.
This applies the same pointwise definition beyond the annulus solely to discuss subsequent transport.
The construction and(2) retain the coordinator's contribution explicitly.

This fixed exit supplies bounded displacement, with coordinate radii |zeta_j-1|.
Repetition of leading zeros varies phase only.
It does not establish arbitrarily large negative costs or free transport through another word.

<a id="zero-exit-amplitude-support-criterion"></a>
### 2. Exact transport criterion using all legal zero exits

Let E be the set of all field endpoints E_v of finite original-digit words starting at0 with |E_v|<1.
Include the zero endpoint, which is supplied by a nonempty zero word.
For a vector a=(a_1,...,a_s) with nonnegative real coordinates, define the extended nonnegative support quantity

    H(a)=sup_(E_v in E) sum_j a_j |z_(v,j)|.          (3)

Now fix any real x with an exact finite original-digit co-return prefix p: T_p(x)=0, of length l.
Necessarily x belongs to Q(beta); because beta is a unit it even belongs to Z[beta].
Let z_x be its neutral embedding vector.
The field cocycle gives c_p=-z_x, so

    c_(p 0^r v)=-z_x+A^(-l-r-k)z_v,
    inf_(v,r) u.c_(p 0^r v)=-u.z_x-H((|u_j|)_j).    (4)

The equality follows by first fixing v and using full joint phase density in r, then taking the infimum over v.
It remains valid with value minus infinity.
Every such complete word has strictly legal real endpoint E_v at x.
No cost of p has been discarded.

**Exact family criterion.** The family of words passing through this exact co-return prefix, then any zero wait and any legal zero exit, supplies strict negativity in every neutral direction if and only if

    H(a)>sum_j a_j |z_(x,j)|
      for every nonzero a in[0,infinity)^s.           (5)

For sufficiency, normalize any direction u and use -u.z_x<=sum_j|u_j||z_(x,j)| in(4).
The strict gap in(5) gives a finite actual exit and a finite wait with negative cost.
For necessity, if(5) fails at a, choose u_j of magnitude a_j opposite z_(x,j), with an arbitrary phase where that coordinate vanishes.
Then -u.z_x=sum_j a_j|z_(x,j)|; every complete word has nonnegative cost.
Normalizing u does not change the sign.
This equivalence concerns this complete prefix-through-zero family.
Failure of(5) does not rule out different words from x which do not first follow p.

When(5) holds, each direction has a strictly negative finite word.
Compactness selects finitely many; their strictly positive real endpoint margins give PC on an open neighborhood of x.
If their lengths are at most N and margins at least epsilon, radius epsilon beta^(-N) suffices.
No uniform length or radius is supplied by the criterion.

One exit with |z_(v,j)|>|z_(x,j)| for every j is sufficient, but not necessary.
Several exits can satisfy the weighted support inequalities without any one exit dominating all coordinates.
Thus simultaneous coordinatewise growth of a single exit is stronger than the mechanism actually needs.

<a id="coordinatewise-unbounded-exit-gate"></a>
### 3. The precise unboundedness gate

For each coordinate set

    M_j=sup_(E_v in E) |z_(v,j)|,
    J_b={j: M_j<infinity}.

If every M_j is infinite, then H(a)=infinity for every nonzero nonnegative a, because a has a positive coordinate.
Conversely, H(a)=infinity for every nonzero a implies M_j=infinity by taking a supported on j.
By(4), this is exactly the condition for arbitrarily negative cost in every direction for the zero-wait/exit family, either at0 or after any fixed exact co-return prefix.

Under this condition the displacements of finite original words legal at0 contain arbitrarily large centered balls in their finite convex hulls.
To justify the finite claim, fix R>0.
In every unit direction choose an exit and zero wait with cost below -R-1.
Negativity below -R persists on a neighborhood of that direction.
Compactness selects finitely many words, whose convex hull contains the ball of radius R by the finite separation argument already proved in L176.
Their real margins also give a common nonempty neighborhood.
Neither the selected words nor that neighborhood are uniform in R or beta.

In general, every direction with at least one nonzero coordinate outside J_b has H(|u|)=infinity and succeeds after every fixed prefix.
Any failure of(5) is therefore supported entirely on J_b.
This is a proper coordinate-face obstruction once at least one M_j is proved infinite.
If |z_(x,j)|>=M_j for a bounded coordinate, that one-coordinate test necessarily fails for this family.
Separate strict inequalities |z_(x,j)|<M_j at every bounded coordinate do not by themselves settle mixtures of coordinates; (5) remains the exact test.

<a id="height-one-spectrum-neutral-growth"></a>
### 4. What original-alphabet real density proves

The accepted input is [Fen16-U001](../audits/literature/Fen16/Yin_U001.md#fen16-u001), Theorem1.2 of De-Jun Feng's published JEMS paper, printed p.182/PDF p.2.
For q>1 and a positive integer m, the real spectrum of finite polynomials with coefficients{0,+/-1,...,+/-m} is dense exactly when q<m+1 and q is not Pisot.
The retained journal statement, definitions and applicability were checked; the source proof was not independently re-audited.
It is accepted at that explicit established-external-input scope.

A Salem beta in(1,2) is non-Pisot because it has a unit-circle conjugate, so m=1 applies to precisely the original alphabet.
Hence there are polynomials P with these coefficients and

    0<|P(beta)|<epsilon

for arbitrarily small epsilon>0.
Reading their coefficients in descending order realizes P(beta) as an actual endpoint from0.
For epsilon<1 these are legal exits in E.
Put S=beta/(beta-1).
The stable conjugate satisfies |P(beta^(-1))|<S.
The algebraic integer P(beta) is nonzero, so its field norm is a nonzero integer and

    1 <= |N(P(beta))|
       = |P(beta)| |P(beta^(-1))| product_j |P(zeta_j)|^2,
    product_j |P(zeta_j)|^2 > 1/(S |P(beta)|),
    max_j |P(zeta_j)| > (S |P(beta)|)^(-1/(2s)).       (6)

No conjugate value is zero, by irreducibility and P(beta)!=0.
Thus the maximum neutral exit amplitude is unbounded.
Finitely many coordinates imply that at least one M_j is infinite.
Moreover H(a)=infinity for every a with all coordinates strictly positive, since sum_j a_j|P(zeta_j)| is at least (min_j a_j) times that maximum.

This does not prove M_j=infinity for each prescribed j when s>1: the norm controls a product and a maximum, not every factor.
The source theorem is scalar real density and contains no such additional conclusion.
It follows that after any exact co-return prefix, all directions with all neutral coordinates nonzero admit arbitrarily negative costs.
A possible family failure lies on coordinate faces, more precisely on the coordinates in J_b.
This is a geometric restriction on the dual obstruction, not a proof that it is absent.

For example, purely as a statement about implications between amplitude bounds, vectors (n,1,...,1) have unbounded product and maximum but bounded last coordinates.
These are not claimed to be actual Salem exits; they show why inequality(6) alone cannot justify the missing inference.

<a id="quartic-co-return-point-control"></a>
### 5. Complete transport for degree-four Salem inputs

**Theorem.** Let beta in(1,2) be any degree-four Salem number.
Every real x admitting a finite exact original-digit co-return to0 satisfies PC and has a nonempty open PC neighborhood.
At0, legal original-word displacements have finite convex hulls containing centered balls of arbitrarily large radius.
These statements do not require a compact-termination theorem for beta.

There is only one unit-circle conjugate pair, so s=1.
Formula(6) proves M_1=infinity; equivalently, choose |P(beta)|<1/(S R^2) to obtain |P(zeta_1)|>R.
Sections2--3 now prove both conclusions, including every prefix cost.
The source density is not effective in word length, and no fixed quantitative radius, time or original-law probability estimate is asserted.

In particular all the exact limiting centers in [L178](Yin_L_G0178_v1.md#strict-boundary-failure-of-seed-limit) are controlled for every degree-four Salem input, because their prefix p followed by digit -1 sends them to0.
L178's specific periodic family still has the exact strict-boundary failure there; the new words use different zero-state exits of sufficiently large amplitude.
This repairs that family-specific gap at all its co-return centers in degree four, without proving that every real point is such a center or that their neighborhoods cover the annulus.

For higher degree the same theorem holds conditionally on the separate coordinatewise unboundedness M_j=infinity for every j.
It is not enough to know only that E is infinite or dense in its real projection, or that one neutral norm is unbounded.
Also a legal zero exit need not return to0; no actual-core conclusion follows from its existence alone.

### 6. Search, scope and remaining question

The initial reuse screen read the fixed L176/L178 control and cocycle interfaces.
A targeted registry/ledger search for Feng, Akiyama--Komornik and spectrum density found no retained exact input.
The bounded primary-source search located the stronger unchanged-alphabet density theorem, and the published artifact was acquired and validated under key Fen16.
The source account records exact acquisition, statement and proof-inspection boundaries.
A second narrow search did not provide an adopted per-coordinate neutral-growth theorem.
No search absence or novelty claim is asserted.

The next discriminating question is now precise: for a chosen unit-circle conjugate zeta of a Salem beta in(1,2), is |P(zeta)| unbounded over original height-one P with |P(beta)|<1?
A proof for each coordinate would remove every dual obstruction for all exact co-return points by(5).
Alternatively, one bounded coordinate would identify a genuine limitation of this prefix-through-zero mechanism.
Neither outcome is proved here in general degree.
Even complete transport on co-return points would still leave arbitrary real points, uniform finite-cover costs and compact termination separate.

The coordinator supplied only the zero-state exit and phase-control observation in Section1 for this round.
The drafting agent supplied the support criterion, unboundedness equivalence, norm adaptation, fourth-degree theorem and remaining-gate analysis.
These are exact written deductions, with no computation or J.
Author checking covered chronological powers, extended-real infima, failure directions including zero coordinates, strict endpoint margins, original digit order and the source hypotheses.
Complete independent review and fixed adoption remain pending; G0001 is active and unresolved.






<a id="retained-small-salem-global-control-argument"></a>
## Complete original D G0051 argument and both independent reviews

## Sparse prescribed digits give full joint control below the golden ratio

Date: 2026-10-10.
New coordinator-developed G0001 argument, continuing the exact [L176 pointwise-control interface](Yin_L_G0176_v1.md#joint-neutral-pointwise-control) and [L178 propagation boundary](Yin_L_G0178_v1.md#dense-open-salem-pointwise-control).
The question is whether spare binary expansion capacity can supply genuinely unbounded negative directional cost, rather than only rotate one bounded exit.
The complete direct proof is being developed here.
No computation or external spectrum theorem is an input.

<a id="small-salem-global-pointwise-control"></a>
### Statement and exact boundary

Let beta be any Salem number with1<beta<phi=(1+sqrt5)/2.
Use the original digits{-1,0,1}, every neutral conjugate pair, and strict endpoint legality |T_w(x)|<1 as in L176.
The proposed conclusion is full PC at every x in[1/2,1].
More strongly, for each fixed real direction and x, legal finite words have directional displacement cost unbounded below.
If the proof is accepted, L176 then gives a finite convex cover and neutral compact reduction for each such input.
Compact termination, actual-core equality, bounds under the original random law, degree-uniform constants and G0001 remain separate obligations.
Independent review is pending.

### 1. Directional coefficients and uniformly bounded sign gaps

Fix one root zeta_j from each of the s unit-circle pairs and a nonzero real direction u in C^s with its usual real inner product.
Put

    a_i=Re sum_(j=1)^s conjugate(u_j) zeta_j^(-i),
    A_u=sum_j |u_j|>0,
    B=1/(beta-1)>1.

For a chronological word w=(eta_1,...,eta_n), the neutral displacement cost is exactly

    u.c_w=sum_(i=1)^n eta_i a_i,
    T_w(x)=beta^n x+sum_(i=1)^n eta_i beta^(n-i).      (1)

L176 proves full product-torus density of the selected Salem phases, including each fixed positive power and arbitrarily late visits.
The same holds for inverse phases by inversion of the torus.
We need the following elementary strengthened consequence for this fixed u: there are epsilon>0 and an integer Q>=1 such that every block a_(n+1)...,a_(n+Q), n>=0, contains a value greater than epsilon and a value less than minus epsilon.

Indeed the real continuous function F(q)=Re sum_j conjugate(u_j)q_j on the product torus attains both A_u and -A_u.
Choose0<epsilon<A_u.
For the rotation R(q)=(zeta_j^(-1)q_j)_j, each orbit is dense, since it is a translate of the dense orbit of the identity.
Thus the inverse images R^(-i){F>epsilon}, i>=1, cover the compact torus.
A finite subcover gives a maximum index Q_+.
The same argument for {F<-epsilon} gives Q_-.
Set Q=max(Q_+,Q_-), and apply the two covers to R^n(1).
This proves the claim without an effective return-time bound.

Define the sign convention and discounted positive-position weight by

    chi_i=1 if a_i>=0, and chi_i=0 if a_i<0,
    P_n=sum_(j=1)^infinity chi_(n+j) beta^(-j).

Zeros are deliberately assigned to chi=1; their cost will be zero.
The sign-gap claim implies, with delta=beta^(-Q)>0,

    delta<=P_n<=B-delta for every n>=0.              (2)

Both signs are needed for this bound.
All constants here may depend on the fixed u and input beta.

### 2. A sparse prescribed-position binary expansion lemma

Because beta<phi,

    B-beta^(-1)=1/[beta(beta-1)]>1.

Choose an integer L>=2 large enough that

    B-beta^(-1)/(1-beta^(-L))>1.                     (3)

Let S be any set of positive integers whose distinct consecutive elements have gaps at least L.
For every free index i not in S, the total weight of later prescribed positions is at most

    sum_(s in S, s>i) beta^(-s)
        <=beta^(-i) beta^(-1)/(1-beta^(-L)).

Subtracting from the total later geometric weight beta^(-i)B and using(3) shows

    beta^(-i)<sum_(j>i, j not in S) beta^(-j).        (4)

Consequently the binary sums on free positions fill their entire possible interval:

    {sum_(i not in S) epsilon_i beta^(-i):
                        epsilon_i in{0,1}}
        =[0,B-sum_(s in S) beta^(-s)].               (5)

Here is a direct proof of the interval assertion.
List the free weights in decreasing order as w_1,w_2,..., and put t_j=sum_(r>j)w_r.
Equation(4) says w_j<=t_j.
The intervals[0,t_j] and[w_j,w_j+t_j] therefore cover[0,w_j+t_j].
Starting with any number in[0,sum w_j], choose at each stage the digit0 or1 whose corresponding interval contains the remainder.
The next remainder stays in[0,t_j], and the tails tend to zero.
The resulting convergent binary series represents the initial number.
Conversely every binary sum lies in the displayed interval.
Infinitely many free positions exist since L>=2.
No uniqueness of expansion is claimed or required.

This is the only place the golden-ratio restriction is used.
The argument does not assert the same sparse-hole interval statement for larger beta.

### 3. Unbounded negative cost inside a direction-dependent real interval

For the fixed u consider

    I_u=(P_0-B,P_0).

We prove that for every x in I_u and every real C there is a nonempty original word w such that |T_w(x)|<1 and u.c_w<C.

Set y=P_0-x, so0<y<B.
Choose an infinite subsequence S of positions where a_i>epsilon, with gaps at least L and with its first position sufficiently late that

    W_S=sum_(s in S) beta^(-s)<B-y.                  (6)

Such a subsequence exists by Section1's positive sign visits: after each selected position skip at least L places and then choose a later positive visit.
The geometric bound for a set with gaps L makes its total weight arbitrarily small by starting sufficiently late.

By(5)--(6), represent y as a binary sum with epsilon_s=0 at every prescribed position s in S.
On all positions put

    eta_i=epsilon_i-chi_i in{-1,0,1}.

If a_i>=0 then eta_i is either-1 or0, while if a_i<0 it is either0 or1.
Thus every cost eta_i a_i is nonpositive.
At s in S it is -a_s<-epsilon.
Therefore

    x=-sum_(i=1)^infinity eta_i beta^(-i),
    sum_(i=1)^n eta_i a_i -> -infinity.              (7)

This construction changes no digit probabilities: it selects legal finite words for a deterministic control argument, not a random-law estimate.

The real endpoint after the first n digits is the remaining tail:

    r_n=T_(eta_1,...,eta_n)(x)
       =-sum_(j=1)^infinity eta_(n+j) beta^(-j)
       =P_n-sum_(j=1)^infinity epsilon_(n+j) beta^(-j).

Equations(2) and0<=sum epsilon_(n+j)beta^(-j)<=B imply the uniform strict strip bound

    -B+delta<=r_n<=B-delta for every n.              (8)

Although this need not be the narrow interval(-1,1), it permits a bounded-length correction independent of n.
While |r|>=1, choose the next digit -sign(r).
Its new value has the same sign and magnitude beta|r|-1, because beta|r|-1>=beta-1>0.
The distance from the strip boundary consequently satisfies

    B-|beta r-sign(r)|=beta(B-|r|).

Choose an integer M>=1 with beta^M delta>B-1.
Starting from(8), the process must enter |r|<1 in at most M digits; otherwise the last displayed identity contradicts |r|>=1.
If the starting endpoint is already narrow, append no correction.
Each additional digit has absolute directional cost at most A_u, because |a_i|<=A_u at all indices.
Hence the full corrected word has cost at most

    sum_(i=1)^n eta_i a_i + M A_u,

which tends to minus infinity by(7).
Take n>=1 large enough to obtain the prescribed C.
This proves the claimed unbounded-cost statement, with a strictly legal endpoint.
It avoids any inference that a bounded phase orbit itself has unbounded amplitudes.

### 4. An exact finite prefix reaches that interval from the annulus

Let now x in[1/2,1] and keep any fixed nonzero direction u.
If x lies in I_u, Section3 applies directly.
Since P_0-B<0 and x>0, the only other possibility is x>=P_0.
We show that a finite prefix of digits all equal to-1 sends x into the relevant shifted-direction interval.

After n such digits put

    x_n=B+beta^n(x-B),
    d_n=x_n-P_n.

The sign weights satisfy P_n=beta P_(n-1)-chi_n, so

    d_n=beta d_(n-1)-(1-chi_n),
    beta^(-n)d_n
       =x-P_0-sum_(i=1)^n(1-chi_i) beta^(-i)
          ->x-P_0-(B-P_0)=x-B<0.                   (9)

Here B>1>=x, so the final inequality is strict.
Starting with d_0>=0, there is a first n>=1 with d_n<0.
At that step d_(n-1)>=0, and(9) forces1-chi_n=1 and

    -1<=d_n<0.

Since B>1, this gives

    P_n-B<x_n<P_n.                                  (10)

The suffix direction is u'=A^n u, where A=diag(zeta_j), because the exact concatenation law gives u.c_(pw)=u.c_p+(A^n u).c_w.
Its coefficients are a_i(u')=a_(n+i)(u), so its positive-position weight is exactly P_n.
Thus(10) puts the actual real prefix endpoint into I_(u').
Section3 supplies suffixes with strictly narrow endpoints and arbitrarily negative cost in direction u'.
Choose one whose cost is less than C-u.c_p.
The concatenated word is strictly legal at x and has full directional cost less than C.

The prefix cost has not been discarded or assumed favorable.
It is only finite, and Section3 supplies the genuinely unbounded negative suffix resource needed to absorb it.
No density of real seeds, order membership or eventual periodicity is assumed.
If desired its intermediate real values also stay narrow: the all-minus-one trajectory is decreasing while positive, before the first crossing x_j>=P_j>0, and at the crossing x_n>=P_n-1>-1.
The original endpoint convention alone already suffices.

### 5. Full PC and what follows from it

Sections3--4 prove the stronger asserted statement for every real unit direction and every x in[1/2,1].
Choosing C=0 proves the full strict PC condition of L176 for every Salem beta in(1,phi).
L176's independently reviewed compactness argument then selects finitely many actual finite words on each of finitely many closed real cells covering the annulus.
Their joint displacement convex hulls, equivalently the positively normalized hulls, contain zero in their interiors.
The source's squared-neutral-norm calculation gives compact reduction for actual narrow-domain states, with all intermediate real-strip and stable-coordinate conditions as already proved there.

The constants arise after fixing beta and the complete neutral system.
This proof gives no uniform Q, word length, cell width, convex margin or compact radius as the degree grows or beta tends to one.
The dimension-versus-width obstruction in L176 is not evaded: the finite cover chosen after the pointwise proof may require extremely long words and correspondingly small cells.
The conclusion also does not settle which compact residue states return to zero.
That compact termination, actual full-core identification and unchanged-law entropy estimates remain open obligations for the general input.

In particular, deterministic unbounded negative directional cost is not an averaged negative drift under the original probabilities.
The positive quadratic drift identity in L176 remains valid, and nothing here changes the digits' assigned probabilities or claims that chosen words occur at a uniform positive rate.
Neither a degree-independent entropy gap nor unrestricted G0001 follows from the control theorem alone.

### 6. Reuse, self-check and pending independent review

The coordinating AI for Yin developed every argument in this draft.
It read the fixed L176 PC, joint-phase-density and compact-reduction interfaces and L178's exact prefix/amplitude boundary.
The changed mechanism is the binary interval redundancy below phi, with infinitely many sparse forced negative contributions and a uniformly bounded real correction, not another rotation of a fixed-amplitude exit.
The root sent the mechanism to the two other agents for scheduling and scope separation; they supplied none of the derivations before this freeze.
No claim of external novelty is made.

The author checked the strict inequality in(3), the arbitrary-gap geometric sum, the recursive binary interval proof, the zero-sign convention, both uniform sign visits, the exact tail sign in(8), the bounded correction and its total chronological cost, and the all-minus-one prefix recurrence including equality at d_0=0.
All proof dependencies beyond elementary real algebra are the explicitly fixed project inputs.
No numerical experiment, external spectrum theorem or uninspected source proof is used.
Independent full review and fixed adoption are pending.
The unrestricted G0001 Task remains active and unresolved.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0079_v1.md#complete-separate-noncontributor-mathematical-review), with its original inspected scope and relationship.






The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0079_v1.md#small-salem-global-control-second-check), with its original inspected scope and relationship.

## Retention, contributions and source boundary

The structural drafting agent supplied D48's support criterion, amplitude analysis and source adaptations; the coordinator supplied its explicitly identified zero-state exit and phase-control observation.
On2026-10-10 the separately assigned resultant_research reviewer checked the complete frozen D48 Sections1--6/formulas(1)--(6), the degree-four theorem and all source/application limits, finding no mathematical defect or missing hypothesis.
Its exact mathematical input is the original body at [the retained D48 argument](#retained-zero-exit-control-argument).
It contributed none of D48 and had reviewed the fixed L176 interface.
It received the coordinator's checklist, Section1 contribution disclosure and shared project context, whose actual initial mathematical contents remain unestablished; that historical relationship is unknown.
It directly text-read the published Fen16 journal PDF pp1--2/printed181--182, including title, author, DOI, definition, Pisot convention and Theorem1.2.
It also read Fen16-U001 and its source account.
The accepted source scope is statement/application checking, without a proof or dependency audit.

The coordinator supplied the entire D51 sparse-digit proof.
The structural and orbit reviewers supplied none of those new derivations and checked the whole chain after receiving the target sparse mechanism.
Their complete findings are self-reviewed at the concrete original input arrangement recorded in [R79](../audits/reviews/Yin_R_G0079_v1.md#review-relationships), including the structural review's actual2026-10-09T17:50 time.
Both exact original author-check paragraphs remain there at their recorded scopes and day precision.
The original2026-10-10 fixed-retention instruction above followed these D48 and D51 checks; it was restricted mathematical adoption, not C acceptance or Task completion.
Mechanical retention by the structural agent implemented that instruction.

The Fen16 source unit retains the published-versus-locator edition and actual statement-reading boundaries, with original proof and dependency audits absent.
The original source screen adopted no prescribed-coordinate neutral-growth theorem and supplied no search-absence or novelty claim.
The [later R660 zero-exit finding](../audits/reviews/Yin_R_G0660_v1.md#isolated-zero-exit-whole-finding) is a new2026-10-22 inspection of C431v1, with the entire original D48 scope and historical source/context comparison recorded separately from the old adoption.
There is no numerical program or J for these rounds.
Earlier fixed L169/L170 actual-core examples and unrelated mathematical bodies are unchanged.
