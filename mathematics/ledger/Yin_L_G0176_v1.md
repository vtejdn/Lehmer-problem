---
author: Yin
---
# Joint neutral control: finite-cover equivalence, obstructions and periodic seeds

Date: 2026-10-10.
Fixed retention under the coordinating AI for Yin's explicit adoption instruction following both complete separately organized reviews.
This is a restricted mathematical adoption, not a C acceptance or Task-completion decision.
G0001 remains active and unresolved.

<a id="joint-control-fixed-scope"></a>
## Current adopted scope

For every Salem beta in(1,2), the [pointwise criterion](#joint-neutral-pointwise-control) is equivalent to a finite strict original-digit convex cover of the real annulus.
Under that criterion, the complete argument reduces neutral descent to a compact residue; compact termination remains a separate premise.
The [rank/width obstruction](#finite-cell-neutral-rank-barrier), exact fixed-cell counterexample and [positive original-law quadratic drift](#original-law-quadratic-drift-obstruction) retain their specified limitations.

The [loop separation and cocycle](#periodic-loop-dual-cocycle), complete [joint phase-density proof](#salem-joint-phase-density) and [loop-and-exit criterion](#periodic-loop-exit-control) prove pointwise control on nonempty neighborhoods of [infinitely many explicit periodic seeds](#general-salem-periodic-control-seeds) for every such Salem beta.
Those distinct seeds converge to beta^(-1); their neighborhoods need not cover that limit or the annulus.
The exact [two-step examples](#period-two-neutral-exit-test) distinguish immediate projected escape, energy increase and eventual phase-assisted control.
There is no general compact-termination or unrestricted gap conclusion.

The complete original D G0026 and D G0043 accounts follow, including every proof, limitation, source boundary and review finding.
Date-specific pending-review/adoption wording is historical and superseded only by this current adoption statement.
Retention changes section depth and navigation, not mathematical statements or historical findings.

<a id="retained-pointwise-control-argument"></a>
## Complete original D G0026 argument and review

## Analytic joint-neutral controllability and the finite-cell barrier

Date: 2026-10-10.

Earlier original-Lehmer certificates remain frozen.

### Question

Characterize when original {-1,0,1}-digit words legal on a whole expanding interval have joint neutral displacement hull containing zero in its interior.
Separate feasibility from the normalized geometric cost, and test whether dense reciprocal neutral rotations alone suffice.
The output sought is a proved conditional theorem and a concrete counterexample or next discriminating test, without a universal Salem or gap claim.

### Reuse boundary

Reuse the explicit normalized identity and full-coordinate contracts in [D G0020](Yin_L_G0170_v1.md#normalized-lehmer-radius-eight), the original-Lehmer field checks in [D G0017](Yin_L_G0170_v1.md#lehmer-joint-neutral-descent), and the quartic control in [fixed L G0169](Yin_L_G0169_v1.md#quartic-neutral-descent).
The current question is conceptual dependence on interval width, neutral dimension and real legality, rather than another input-by-input enumeration.

<a id="joint-neutral-pointwise-control"></a>
### 1. A pointwise criterion equivalent to a finite convex-cover certificate

Let beta in (1,2) be a degree d=2s+2 Salem number.
Let zeta_1,...,zeta_s be one root from each unit-circle conjugate pair, and identify C^s with R^(2s) using its usual real inner product.
The alphabet stays {-1,0,1}.
For a nonempty word w=(eta_1,...,eta_k), put

    b_w=sum_(i=1)^k eta_i beta^(-i),
    c_w=(sum_(i=1)^k eta_i zeta_j^(-i))_(j=1)^s,
    T_w(x)=beta^k(x+b_w).

The word is strictly legal at x if |T_w(x)|<1.
It is strictly legal on a closed interval if this inequality holds throughout that interval.
All statements below use this endpoint legality, with the usual full intermediate real-strip bound recovered afterward.

Consider the following pointwise condition:

    (PC) For every x in [1/2,1] and every real unit direction u in C^s,
         there is a nonempty original-digit word w with
         |T_w(x)|<1 and u.c_w<0.

**Finite-cover theorem.** Condition (PC) is equivalent to the existence of finitely many closed intervals covering [1/2,1], each equipped with finitely many words strictly legal on its whole interval, such that zero lies in the interior of the joint convex hull of its c_w.
Equivalently, one may use the normalized nonzero vectors c_w/||c_w||^2 in this conclusion.

Here is a proof, including the finiteness step.
For any finite set F of vectors, zero lies in the interior of conv(F) exactly when every unit direction u has min_(v in F) u.v<0.
Necessity follows by testing a small point opposite u in the contained ball.
For sufficiency, the minimum is continuous in u, so strict negativity on the unit sphere gives a uniform negative bound.
The corresponding positive support bound in every direction implies that a ball is contained in conv(F): otherwise a nearest point of the compact convex hull to an omitted point of that ball gives a separating supporting direction contradicting the bound.
Thus no nonzero linear functional is nonnegative on the entire set.
Multiplying each vector by its own positive scalar leaves this sign condition unchanged.
This proves the normalized equivalence and shows that zero vectors can be discarded.

Fix x and assume (PC).
For each unit u choose one successful word.
Its negative inner product persists in an open neighborhood of u, so compactness of the unit sphere selects finitely many words whose directions cover it.
Their displacement hull contains zero in its interior.
Each of those finitely many words has a strict real-image margin at x, so all remain legal on one common open neighborhood of x.
These neighborhoods cover the compact interval [1/2,1]; take a finite subcover and a finite closed subdivision subordinate to it.
Assign to every subinterval one of the already chosen word families.
This proves the forward implication.
Conversely, a convex-cover family supplies a negative vertex in every direction at every covered x, proving (PC).

The condition is a concrete constrained signed-sum problem.
If

    a_i(u)=Re(sum_j conj(u_j) zeta_j^(-i)),

then it asks for some finite original-digit sequence simultaneously satisfying

    -x-beta^(-k) < sum_i eta_i beta^(-i) < -x+beta^(-k),
    sum_i eta_i a_i(u)<0.

Frequency recurrence alone does not impose this simultaneous real-discounted balance and neutral sign condition.

### 2. What this criterion proves conditionally for Salem inputs

Under (PC), take the finite normalized convex cover above.
Let r>0 be a common contained-ball radius and m>0 a common lower bound for every retained nonzero ||c_w||^2.
Choose R>1/(2r) and put delta=m(2rR-1)>0.
The normalized identity from D G0020 gives, for every joint neutral state of norm at least R, a legal word lowering its squared norm by at least delta.
The longest chosen word has a finite length L.

The real-coordinate proof extends without changing the alphabet: signs cover negative x_+, zeros bring any nonzero |x_+|<1/2 to the annulus, the first crossing stays below beta/2<1, and an actual algebraic state with x_+=0 is zero.
With S=beta/(beta-1), every digit preserves |x_-|<=S.
Backward estimation from the final narrow endpoint gives |x_+|<1/(beta-1) at intermediate states.
Repeated descent therefore reduces every actual point of the narrow real domain to the finite compact residue rho<R.

This is an analytic conditional theorem for any such Salem input.
To conclude full narrow-domain co-return one still needs finite continuations from the compact residue.
If that additional condition holds, the reciprocal transformation beta^(-1) sigma(x), sigma(beta)=beta^(-1), supplies reachability on the smaller slab |x_+|<=1, |x_-|<=beta, and the degree-d coefficient-box count gives infinitely many actual returning states.
The proof is the same explicit reciprocal sign/order and pigeonhole argument already recorded for the quartic and original Lehmer inputs, with (N+1)^d/O(N^2) growing like N^(d-2).
Compact reduction by itself is not compact termination.

Finite certificates with strict margins are also stable under small changes of the real base and neutral angles, at fixed s: finitely many real-image inequalities remain strict, and the strictly positive directional margin of the finite normalized hull persists by continuity.
This supplies local parameter robustness of the geometric certificate.
It does not by itself produce an infinite family of algebraic-integer Salem bases or handle unbounded degree.
A fixed-dimensional parameter neighborhood must not be identified with the unrestricted G0001 class.

<a id="finite-cell-neutral-rank-barrier"></a>
### 3. A dimension-versus-interval obstruction

Let I=[a,b] have positive width h and let a length-k word be strictly legal on I.
Its affine real image has width beta^k h, so necessarily

    beta^k h<2.                                      (1)

Thus a fixed positive-width cell admits only finitely many lengths, regardless of an unrestricted search cap.
Arbitrarily long dense rotations cannot be inserted while preserving whole-cell legality.

There is a sharper obstruction near the upper real endpoint.
Define the first 2s joint neutral power vectors

    v_i=(zeta_1^(-i)...,zeta_s^(-i)), i=1,...,2s.

They are a real basis of C^s.
Indeed a real dependence would give a polynomial sum_(i=1)^(2s) a_i t^i vanishing at all 2s distinct unit roots and also at zero.
Its degree is at most 2s, so it must be identically zero.

Consequently there is a real linear functional ell with

    ell(v_i)=beta^(-i), i=1,...,2s.

Every word of length k<=2s then obeys ell(c_w)=b_w.
If its cell has right endpoint b>=beta^(-1), strict legality at b gives

    ell(c_w)=b_w<beta^(-k)-b<=0.                     (2)

All such words lie strictly on one side of the same hyperplane.
Their convex hull cannot contain zero, even before normalization.
Any positive norm weighting or invertible coordinate change preserves this separating obstruction.

Therefore a successful full-dimensional convex certificate on such a cell must include at least one word with

    k>=2s+1=d-1,
    h<2 beta^(-(d-1)).                              (3)

These are necessary conditions, not sufficient ones.
In particular, if a finite interval cover of [1/2,1] has a successful certificate on every cell, the cells intersecting (beta^(-1),1] must satisfy the width bound.
Their number is at least

    (1-beta^(-1))/(2 beta^(-(d-1)))
       =(beta-1) beta^(d-2)/2,

with the obvious integer rounding.
This bound describes a possible geometric cost when degree grows; it is not an obstruction to adaptive refinement.

### 4. A dense-rotation counterexample to the fixed-cell shortcut

Use the rigorously established quartic input P=t^4-t^3-t^2-t+1 from [L G0169](Yin_L_G0169_v1.md#quartic-neutral-descent), with 17/10<beta<18/10 and one unit-circle pair zeta,conj(zeta).
On the single cell I=[1/2,1], (1) requires beta^k<4.
Since beta^3>(17/10)^3>4, every legal word has k<=2=d-2.
Its right endpoint is one, so (2) strictly separates every legal joint displacement from zero.
The complete available word set on this cell cannot give a joint neighborhood of zero, no matter which convex weights or positive quadratic norm are chosen.

Nevertheless the neutral rotation is dense on the circle.
The root zeta is not a root of unity, since irreducibility would otherwise make beta a root of unity.
The compact-group closure argument already proved in [L G0102](Yin_L_G0102_v1.md#unit-circle-trace-witness-decay) makes the closure of its nonnegative powers a closed subgroup.
An infinite closed subgroup of the circle is the whole circle: arbitrarily close distinct points supply nonzero subgroup angles tending to zero, and integer multiples of those angles approximate every circle point.
Thus this is a genuine dense neutral rotation in an actual Salem example, whose infinite actual core is independently established in L G0169.

The exact counterexample refutes the claim that dense neutral rotations suffice for joint control on a prescribed whole cell.
It does not refute (PC), adaptive finite covers, or the possibility of a broader Salem theorem.
The quartic's finer successful table is fully compatible with this obstruction.

<a id="original-law-quadratic-drift-obstruction"></a>
### 5. Deterministic descent does not give original-law quadratic contraction

For the original independent difference digits, P(eta=-1)=P(eta=1)=1/4 and P(eta=0)=1/2.
Hence E eta=0 and E eta^2=1/2.
Let

    V(z)=sum_(j=1)^s w_j |z_j|^2, w_j>0.

One digit acts as z'_j=zeta_j z_j+eta.
Direct expansion gives the exact identity

    E[V(z') | z] = V(z)+(1/2)sum_j w_j.              (4)

The drift is strictly positive at every state.
More generally, if A is the real joint neutral rotation, e is the real digit vector, and Q is positive definite with A^T Q A=Q, then

    E[(Az+eta e)^T Q(Az+eta e) | z]
        =z^TQz+(1/2)e^TQe.

Thus no positive quadratic norm compatible with the neutral rotations has strictly negative one-step drift under the unchanged original law.
Choosing a legal word in the favorable direction is a controlled path statement; averaging the original random digit is a different operation.
Equation (4) proves this distinction without relying on a failed numerical estimate.

This does not exclude estimates for a killed process, a law conditioned on returning through the real strip, a nonquadratic quantity, or a multistep expression retaining arithmetic probabilities.
Such changes must keep their probability normalization and loss explicit.
It supplies no reason to pause those alternatives.
It rules out only the direct inference from the deterministic convex descent table to an averaged negative quadratic drift for the full original process.

### 6. Discriminating next tests and review boundary

The sharper conceptual target is to prove or disprove (PC) for a specified Salem class by analyzing the coupled discounted-balance and neutral-sign inequalities, rather than invoking dense rotations alone.
The finite-cell barrier gives a concrete minimum horizon d-1 near x_+=1 and a necessary interval width; it should be imposed before constructing a table.
A possible broad conjecture is that (PC) holds for every Salem beta in (1,2) admitting a nontrivial original height-one relation.
It is unproved here, and even its proof would leave compact termination and the original-law entropy gate separate.

For the probability route, the next useful test is a precisely normalized killed/conditioned kernel or a nonquadratic observable that escapes (4).
A successful estimate must be stated under its actual law; the fixed-input chosen-path probability lower bounds do not by themselves yield a uniform G0001 gap.

The local reuse screen read the existing joint descent, normalization, compact/reciprocal, L155 norm-weight obstruction and L102 compact-rotation interfaces.
A bounded primary search rediscovered the already registered Mercat work and located elementary rotation notes.
No additional work was adopted as an input or retained comparison, because L102 plus the elementary closed-subgroup argument above supplies the needed density fact.
No new source registration or numerical program was required for this proof-only round.

All arguments above were self-checked by the drafting agent.
The exact quartic counterexample uses only already certified algebraic bounds and the stated dimension argument; no optimizer failure is a premise.
Independent review, fixed promotion and any universal Salem or Lehmer-gap assertion remain absent.




The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0075_v1.md#separate-complete-local-review), with its original inspected scope and relationship.



<a id="retained-periodic-control-argument"></a>
## Complete original D G0043 argument and independent review

## Periodic-loop separation and an exact outward-excursion test for joint control

Date: 2026-10-10.
The question is the pointwise joint-neutral condition of [D26](#joint-neutral-pointwise-control), not another fixed-input enumeration.
The drafting agent derived the cocycle obstruction, loop-and-exit phase mechanism and the two-step tests below.
After receiving those findings, the coordinator suggested the general single-digit exit from a longer periodic seed; its contribution to Section5 is explicitly retained.
This is author-developed mathematics pending separate review, not an independently reviewed or fixed result.

### Result and exact remaining gate

For every Salem beta in(1,2), the pointwise condition (PC) holds at infinitely many explicit-form periodic real seeds in(1/2,1), converging to beta^(-1), and on a nonempty open neighborhood of each such seed.
A strictly legal finite family exists at each seed.
The argument does not cover every point of[1/2,1], give uniform word lengths or intervals, or prove compact termination.
No new actual-core equality or Mahler gap follows.

The mechanism requires both a periodic loop and a genuine exit.
All exact loops at one nonzero periodic seed are separated from zero by a fixed real functional, even with unbounded lengths.
One legal exit that strictly increases every neutral coordinate modulus removes that barrier after suitable loop repetitions.
A phase choice constructs such exits for arbitrarily large periods at every Salem input.
This is different from invoking dense rotations for words constrained on one prescribed interval; the finite interval is chosen only after finitely many successful pointwise words are selected.

<a id="periodic-loop-dual-cocycle"></a>
### 1. The endpoint cocycle and an exact loop obstruction

Use D26's original digits, strict endpoint legality and complete neutral coordinates.
Let beta have degree2s+2, let zeta_1,...,zeta_s be one root from each unit-circle pair, put A=diag(zeta_1,...,zeta_s), and use the real inner product on C^s.
For a word w=(eta_1,...,eta_l), set

    c_w=sum_(i=1)^l eta_i A^(-i)e,  e=(1,...,1),
    T_w(x)=beta^l x+sum_(i=1)^l eta_i beta^(l-i).

If x belongs to Q(beta), let z=(sigma_j(x)) be its neutral embeddings, and let y=T_w(x), with neutral vector z_y.
Applying each field embedding gives the exact cocycle

    z_y=A^l(z+c_w),
    c_w=A^(-l)z_y-z,
    u.c_w=(A^l u).z_y-u.z.                            (1)

No integrality of x is needed here.
In fact every real periodic seed automatically lies in Q(beta), since T_w(x)=x solves a linear equation with nonzero coefficient beta^l-1.
The pointwise condition in D26 quantifies over real x, so such fractional field points are legitimate tests; they are not asserted to be actual order states.

Suppose x!=0 and a nonempty word returns exactly to x.
Then z_y=z.
For any weights a_j>=0, not all zero, take the unnormalized real direction u_j=-a_j z_j.
Every z_j is nonzero by injectivity of a field embedding, and no zeta_j is a root of unity, since irreducibility would then make beta a root of unity.
Thus

    u.c_w=sum_j a_j |z_j|^2(1-Re(zeta_j^l))>0.           (2)

Dividing u by its positive norm supplies a unit direction without changing signs.
Equation(2) separates all nonempty exact returning words at this same seed, with no restriction on their lengths or on the number of different loops used.
At x=0 all exact returning words instead have c_w=0.
Consequently neither case supplies a full-dimensional displacement hull around zero using exact loops alone.

For a general strictly legal endpoint y, put V_a(z)=sum_j a_j|z_j|^2.
In the direction u=-diag(a_j)z, a negative cost implies

    V_a(z_y)=V_a(z)+2 Re sum_j a_j conj(z_j)c_(w,j)
                         +sum_j a_j|c_(w,j)|^2
               > V_a(z).                              (3)

The converse need not hold, because the rotation in(1) matters.
More precisely, failure of the negative-cost condition in this direction is equivalent to

    Re sum_j a_j conj(z_j)zeta_j^(-l)z_(y,j)<=V_a(z)

for every strictly legal word and its length l.
If all such endpoints satisfy V_a(z_y)<=V_a(z), weighted Cauchy--Schwarz proves this failure.
This is a concrete sufficient obstruction criterion, not an assertion that an actual Salem seed with that property has been found.

<a id="salem-joint-phase-density"></a>
### 2. Joint neutral phases, with the elementary proof exposed

The classical independence of the selected Salem conjugate arguments is not claimed as new.
[Dub23](../literature/pdf/Dub23.pdf), Section2, printed p.863 / PDF p.2, the paragraph preceding Lemma5, attributes it to Salem's 1963 book p.32, with the argument credited to Pisot; that original book is cited here only through Dub23.
The [scoped source reading](../audits/literature/Dub23/readme.md) distinguishes the joint statement from the weaker individual irrationality in Lemma5.
The exact property needed here has a short direct proof: if integers n_j satisfy product_j zeta_j^(n_j)=1, choose an automorphism of the splitting field sending any fixed zeta_i to beta.
Its inverse conjugate is the unique preimage of beta^(-1), so no other selected zeta_j can map to either real conjugate.
All other images have modulus1.
Taking absolute values of the transformed relation gives beta^(n_i)=1 and hence n_i=0.
This holds for every i.
The same argument, or raising a root-of-unity right-hand side to its order, excludes every nontrivial torsion-valued product.

It follows that for every positive integer k, the nonnegative powers of (zeta_1^k,...,zeta_s^k) are dense in the full product of s circles.
To keep the precise density input self-contained, here is an elementary finite-polynomial verification.
For every nonzero integer vector n, the average of

    product_j zeta_j^(k r n_j),  r=0,...,N-1,

tends to zero by the finite geometric-sum formula.
Fix a target q=(q_j) on the torus and a neighborhood requiring Re(conj(q_j)v_j)>1-delta for every j, with0<delta<1.
The nonnegative trigonometric polynomial

    F_m(v)=product_j(1+Re(conj(q_j)v_j))^m / b_m^s,
    b_m=2^(-m) binomial(2m,m)

has constant Fourier coefficient1.
Its average along the orbit therefore tends to1, since it has only finitely many Fourier terms and every nonconstant term has limiting average zero.
The binomial expansion proves the displayed b_m; maximality of the central binomial coefficient and the sum of the2m+1 coefficients give b_m>=2^m/(2m+1).

If the orbit avoided that neighborhood, at least one factor would be at most(2-delta)^m and all other factors at most2^m.
Hence on the orbit

    F_m <= (2m+1)^s(1-delta/2)^m.

For sufficiently large m the right side is strictly below1, contradicting the limiting average1.
This proves density.
The same finite geometric averages hold after removal of any initial orbit segment, so every such neighborhood is visited at arbitrarily large times.
The argument asserts no effective first-visit bound or uniformity in beta, k or s.

<a id="periodic-loop-exit-control"></a>
### 3. A single simultaneous outward exit gives all directions at a seed

Let x in(1/2,1) have an exact original-digit loop W of length k>=1, and let V be any nonempty word strictly legal at x, of length l, ending at y.
Denote h=z+c_V=A^(-l)z_y.
Concatenate r copies of W followed by V.
Using(1), or telescoping the loop geometric sum, gives

    c_(W^r V)=A^(-r k)h-z.                             (4)

Every such word is strictly legal at x, since its real endpoint is the same y.
This assertion uses the exact loop, rather than an approximate periodic orbit: a small real error would expand during repetitions and is not discarded.

Assume the single exit increases every neutral modulus:

    |z_(y,j)|>|z_j| for all j.                         (5)

The joint phase density of Section2 shows that, for any real unit direction u,

    inf_(r>=0) u.c_(W^r V)
       =-sum_j |u_j| |z_(y,j)|-u.z
       <=-sum_j |u_j|(|z_(y,j)|-|z_j|)
       <=-min_j(|z_(y,j)|-|z_j|)<0.                    (6)

The last inequality uses sum_j|u_j|>=||u||_2=1.
The minimum on the torus is achieved by choosing each phase opposite the corresponding u_j; dense orbit values approach that minimum.
Thus some finite r gives a strictly negative cost in each direction, proving PC at x.
Compactness of the unit sphere selects finitely many of these words.
Their strict common real endpoint margin then supplies a neighborhood of x on which every selected word stays strictly legal, so D26's finite-hull argument gives PC throughout that neighborhood.

Equivalently, the convex hull of the complete phase orbit of h is the product of disks of radii |z_(y,j)|.
It contains z in its interior under(5).
Exact loops alone have h=z and leave z on that boundary, consistent with(2).
A larger Euclidean norm alone is weaker than(5) and need not put z inside that product of disks.
No prescribed positive cell width is retained while r is allowed to grow.

<a id="period-two-neutral-exit-test"></a>
### 4. An exact short-horizon test and two actual controls

Suppose first that phi=(1+sqrt(5))/2<beta<2.
Define

    x_2=beta/(beta^2-1),
    W=(-1,0),   V=(-1,-1).

Then1/2<x_2<1, W returns x_2 exactly to itself, and V ends at y=x_2-1 in(-1/2,0).
The inequalities use beta^2-beta-1>0 and beta^2-2beta-1<0.
At each neutral place

    z_j=zeta_j/(zeta_j^2-1)=1/(zeta_j-zeta_j^(-1)),
    Re(z_j)=0,
    |z_j-1|^2=|z_j|^2+1.                              (7)

Consequently Section3 proves PC at x_2 for every Salem beta in(phi,2), with a finite neighborhood.
The exit may need loop repetitions to achieve a particular direction.

For the radial dual direction u=-z, the raw two-step exit has an exact trace test.
Write zeta_j=exp(i theta_j),0<theta_j<pi.
Then z_j=-i/(2sin theta_j), c_V,j=-zeta_j^(-1)-zeta_j^(-2), and

    u.c_V=sum_j(1+2cos(theta_j))/2
          =(s+Tr(beta)-beta-beta^(-1))/2.              (8)

Here Tr(beta) is the integral field trace.
Because beta+beta^(-1) lies strictly between sqrt(5) and5/2, the cost is negative exactly when s+Tr(beta)<=2.

These are the only possibilities through horizon two.
At length one only eta=-1 is strictly legal, and its dual cost is s/2>0.
At length two, the endpoint is beta+x_2+beta eta_1+eta_2.
If eta_1=-1 this is x_2+eta_2, legal exactly for eta_2=-1 or0.
If eta_1>=0, its minimum is beta+x_2-1>1: beta^3-2beta^2+2 is positive at phi and increasing for beta>phi, since its derivative is beta(3beta-4)>0.
Thus only W and V are legal; W has strictly positive cost by(2).
Hence(8) is an exact necessary and sufficient test for a negative witness of length at most two in this one direction, not for full PC.

For the fixed quartic of [L169](Yin_L_G0169_v1.md#quartic-neutral-descent), s=1, Tr(beta)=1 and beta+beta^(-1)=(1+sqrt(13))/2.
Formula(8) gives

    u.c_V=(3-sqrt(13))/4<0.

This is an exact successful exit, not a numerical optimizer result.
The known bound beta>17/10>phi places the seed in the stated interval.

For a contrasting actual degree-six input, set

    P_6(t)=t^6-t^5-t^4-t^3-t^2-t+1,
    Q(v)=v^3-v^2-4v+1,
    t^(-3)P_6(t)=Q(t+t^(-1)).

The cubic Q is irreducible over Q, since its only possible rational roots are +/-1 and neither is a root.
It has distinct roots in(-2,-1),(0,1),(sqrt(5),5/2): the first two follow by signs at their integer endpoints, while Q(sqrt(5))=sqrt(5)-4<0 and Q(5/2)=3/8>0.
These three disjoint intervals exhaust its roots.
At an embedding taking the last trace root to either inner root, v^2-4 is negative; it is therefore not a square in the totally real cubic field.
Adjoining a root of t^2-vt+1 gives degree six.
Thus P_6 is irreducible and has a Salem root beta_6 in(phi,2), with two unit pairs and trace1.

For beta_6, (8) is(3-beta_6-beta_6^(-1))/2>1/4.
Every strictly legal word through horizon two has positive dual cost, even though V increases the total neutral square norm by2.
Nevertheless(7) and the phase-prefix theorem prove that some longer word W^r V succeeds, and that all directions can be controlled at this seed.
This discriminates an immediate projected escape from mere outward energy growth and from eventual phase-assisted control.
No least successful r or numerical search is asserted.

<a id="general-salem-periodic-control-seeds"></a>
### 5. Controlled periodic seeds for every Salem beta in(1,2)

For k>=2 set

    x_k=beta^(k-1)/(beta^k-1)=beta^(-1)/(1-beta^(-k)),
    W_k=(-1,0,...,0),
    V_k=(-1,0,...,0,-1),                               (9)

where both words have length k and the last digit of W_k is changed for V_k.
For sufficiently large k,1/2<x_k<1, since x_k decreases strictly to beta^(-1) in(1/2,1).
Direct substitution gives

    T_(W_k)(x_k)=x_k,
    T_(V_k)(x_k)=x_k-1 in(-1/2,0).                    (10)

The loop's intermediate real values after its first digit are1/(beta^k-1), beta/(beta^k-1)...,x_k; they are positive and at most x_k.
Thus it is an actual narrow real periodic orbit.
The endpoint condition alone suffices for V_k and its prefixed-loop words; D26's backward real estimate supplies the usual larger intermediate strip if required.

The coordinator suggested the general single-zero-to-minus-one exit after the drafting agent's two-period calculation.
Equations(9)--(10) use its last-position case.
The phase selection and its control consequence below are the drafting agent's further deduction.

The neutral seed coordinates are

    z_(k,j)=zeta_j^(k-1)/(zeta_j^k-1).

By Section2, there are arbitrarily large k for which all zeta_j^k lie in a sufficiently small neighborhood of-1.
At the target phase-1 the displayed expression is zeta_j^(-1)/2, whose real part is strictly below1/2 because zeta_j!=1.
Finitely many coordinates and continuity away from the denominator zero give one joint neighborhood on which

    Re(z_(k,j))<1/2 for every j,
    |z_(k,j)-1|^2-|z_(k,j)|^2=1-2Re(z_(k,j))>0.        (11)

Choose k in those arbitrarily late visits, also large enough for the real bounds.
The loop W_k and strictly legal exit V_k satisfy Section3's simultaneous modulus increase.
Thus PC holds at every selected x_k, and on a nonempty open neighborhood of each.
The seeds are distinct and converge to beta^(-1).
All words are finite and retain the original alphabet.
No auxiliary alphabet, alteration of the real base or formal continuous control is used.

The neighborhoods may shrink with k and the longest selected loop repetition.
Accumulation at beta^(-1) does not imply that the limit point or the rest of the annulus is covered.
This is a local controllability theorem with one family of certified-form seeds, not a finite cover of[1/2,1].

### 6. Remaining gate, sources and checking boundary

The unresolved global question is still D26's PC at every real x in[1/2,1].
One possible next mechanism is to transport the new local controlled regions to arbitrary x while retaining real legality and the prefix's neutral displacement cost.
A merely dense family of real seeds or approximate periodicity is insufficient: expansion magnifies errors during long loop repetitions.
Even full PC would only give compact reduction; compact termination and the unchanged original-law probability estimates remain separate requirements.

The qualification in D26's suggested conjecture that beta admit a nontrivial original height-one relation is automatic in this Salem interval: [L91](Yin_L_G0091_v1.md#effective-first-height-one-relation) supplies such a relation whenever m=log(beta)<log2.
This is reuse of an existing result, not a new assumption or a proof of PC.

The initial reuse screen read D26 in full, the L169/L170 neutral and real-coordinate interfaces and L102's compact-rotation argument.
A targeted G-ledger/draft search found no retained version of the loop separation or loop-and-exit mechanism.
A subsequent bounded source screen checked the classical joint-angle independence attribution, first against the existing Smy15 distribution context and then the precise Dub23 passage.
The Dub23 publisher artifact was acquired, registered and text-checked; the source readme records its exact scope and the original-monograph inspection boundary.
The full elementary Galois and finite-polynomial density proofs are included above, so no uninspected source proof supplies a missing step.
No broad novelty claim is made.

The drafting agent self-checked the signs and word order in(1)--(11), strict endpoints, fractional versus actual-order domains, conjugate multiplicities, finite sphere selection, and the complete degree-six algebraic control.
The examples are exact symbolic proof checks, not an executed enumeration.
No program or J is required or claimed.
This complete draft is now frozen for the separately assigned noncontributor review.
Independent review and fixed adoption remain pending; the coordinator's Section5 contribution prevents its later contributor check from constituting independent review of that full extension.
The two previously fixed actual-core theorems and the unrestricted G0001 contract remain unchanged.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0075_v1.md#periodic-loop-control-independent-review), with its original inspected scope and relationship.

## Retention and contribution boundaries

The original drafting accounts and their distinct reviews are preserved above.
The coordinating AI assigned the D G0026 question and supplied none of its mathematical derivations; its complete nonblind noncontributor review is retained.
For D G0043, the coordinating AI contributed the general single-zero-to-minus-one exit identified in original Section5.
The separately assigned resultant_research AI supplied none of that argument and independently checked its entire frozen proof and source scope.
Its full finding identifies the inspected argument and its historical review scope.
The author's mechanical retention implements the coordinating adoption decision and is not another independent review.
No human inspection or formal verification is asserted.

Dub23 is retained for the exact classical attribution and hypothesis comparison stated in the original account.
The needed Galois and phase-density arguments are proved locally and were completely reviewed.
The original Salem monograph was not inspected, and Dub23's main theorems were not adopted.
Earlier L169/L170 actual-core results and L91's height-one relation are reused only at their explicit interfaces.

| Retired working identity | Complete fixed home |
| --- | --- |
| D G0026 | [Entire original account](#retained-pointwise-control-argument), [criterion](#joint-neutral-pointwise-control), [barrier](#finite-cell-neutral-rank-barrier), [drift](#original-law-quadratic-drift-obstruction) and [complete independent local review](../audits/reviews/Yin_R_G0075_v1.md#joint-neutral-control-local-review) |
| D G0043 | [Entire original account](#retained-periodic-control-argument), [loop/cocycle](#periodic-loop-dual-cocycle), [phase density](#salem-joint-phase-density), [exit criterion](#periodic-loop-exit-control), [two-step tests](#period-two-neutral-exit-test), [general seeds](#general-salem-periodic-control-seeds) and [complete independent review](../audits/reviews/Yin_R_G0075_v1.md#periodic-loop-control-independent-review) |

There is no new program or J: both rounds are written proofs.
Actual incoming links were relocated.
The fixed L172 change is navigation only; its mathematical body is unchanged.
