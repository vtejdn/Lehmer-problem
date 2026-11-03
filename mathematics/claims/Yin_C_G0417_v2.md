---
author: Yin
---

# Complete periodic-loop separation, phase exits and local Salem control seeds

The complete original D43 proof is retained from [L176](../ledger/Yin_L_G0176_v1.md#retained-periodic-control-argument).
The drafting agent supplied the cocycle, loop obstruction, density/phase mechanism, exact examples and further seed deduction.
After those findings the coordinator suggested the general last-digit exit in Section5.
The original author checking account preserves its exact listed mathematical obligations and that contribution, as retained in [R75](../audits/reviews/Yin_R_G0075_v1.md#periodic-control-original-author-check-finding).
The separately assigned [whole noncontributor account](../audits/reviews/Yin_R_G0075_v1.md#periodic-loop-control-independent-review) records additional communications without their actual initial mathematical contents, so its independent-review relationship remains unknown.
The full classical Galois and finite-polynomial density proofs remain local.
[Dub23-U001](../audits/literature/Dub23/Yin_U001.md#dub23-u001) owns only the original exact attribution/statement comparison and actual passage-reading depth.
No new source/PDF read, computation or research execution is used.

## Statement

Let beta in(1,2) be a Salem number of degree2s+2>=4, and select one neutral conjugate zeta_j from each inverse pair.
Use A=diag(zeta_j), e=(1,...,1), the real inner product on C^s and chronological original digits{-1,0,1}.
For a nonempty word w of length l define

    c_w=sum_(i=1)^l eta_i A^(-i)e,
    T_w(x)=beta^l x+sum_(i=1)^l eta_i beta^(l-i).

For every field point x in Q(beta), with full neutral vector z and y=T_w(x),

    z_y=A^l(z+c_w),
    c_w=A^(-l)z_y-z,
    u.c_w=(A^l u).z_y-u.z.

Field points need not belong to Z[beta].
Every exact real periodic seed lies in Q(beta).
At any nonzero seed, every nonempty exact loop has strictly positive cost in each nonzero direction u_j=-a_j z_j with a_j>=0:

    u.c_w=sum_j a_j|z_j|^2(1-Re(zeta_j^l))>0.

At zero all exact-loop displacements vanish.
Thus exact loops alone never give an interior joint displacement hull at that same seed.
A negative cost in the displayed weighted radial direction forces larger weighted endpoint square norm; the converse is not asserted.

The selected neutral roots have no nontrivial root-of-unity-valued multiplicative relation.
The full local Galois/modulus proof of this independence uses only the genuine Salem root configuration and beta>1.
For every positive integer k the nonnegative powers of(zeta_1^k,...,zeta_s^k) are dense in the full s-torus and visit every neighborhood arbitrarily late.
The explicit finite-polynomial proof supplies no effective first-visit bound.

Suppose x in(1/2,1) has an exact loop W of length k and a nonempty strictly legal exit V ending at y, with |z_(y,j)|>|z_j| for every neutral coordinate.
Then some loop-prefix word W^r V has negative displacement cost in each prescribed real unit direction.
Indeed its displacement is A^(-rk)(z+c_V)-z and the exact directional infimum is at most

    -min_j(|z_(y,j)|-|z_j|)<0.

Compactness selects finitely many actual finite words with a strict joint hull, and their real endpoint margins give a nonempty open neighborhood of x satisfying PC.
The neighborhood is selected after finitely many words, without retaining a prescribed positive width during unbounded repetitions.

For phi=(1+sqrt5)/2<beta<2,

    x_2=beta/(beta^2-1), W=(-1,0), V=(-1,-1)

satisfy T_W(x_2)=x_2,T_V(x_2)=x_2-1 and |z_j-1|^2=|z_j|^2+1.
Thus x_2 has PC, although for the raw unnormalized radial direction u=-z the immediate exit cost is

    (s+Tr(beta)-beta-beta^(-1))/2,

negative exactly when s+Tr(beta)<=2.
The one- and two-digit possibilities are exhaustively proved below.
The fixed quartic gives cost(3-sqrt13)/4<0.
The exact irreducible degree-six Salem polynomial t^6-t^5-t^4-t^3-t^2-t+1 gives raw exit cost greater than1/4 for V, and every strictly legal word through horizon two has positive raw dual cost, despite total neutral square-norm increase2 for V.
Longer phase-assisted words nevertheless give PC at that seed.

For every beta in(1,2), at arbitrarily large selected integers k>=2 put

    x_k=beta^(k-1)/(beta^k-1),
    W_k=(-1,0,...,0), V_k=(-1,0,...,0,-1),

with both words of length k.
The exact loop/exit endpoints are x_k and x_k-1.
Joint phase visits near(-1,...,-1) give Re(z_(k,j))<1/2 simultaneously, so the exit increases every coordinate modulus.
These are infinitely many distinct seeds in(1/2,1), decreasing to beta^(-1), each with PC on a nonempty open neighborhood.
Their neighborhoods may shrink and do not establish PC at the limit or throughout[1/2,1].
They are fractional field points and are not asserted actual order/core states.
No compact termination, degree-uniform word length, unchanged-law entropy estimate, actual-core equality or unrestricted Mahler gap follows.
The earlier height-one-relation qualification is automatic by C281 at m=log(beta)<log2, without a further PC consequence.

## Current assessment

[Selected decision](#decision-explicit-raw-direction-normalization)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:47 |
| status | open |
| reason | Retain the complete loop/cocycle/full-phase-density/exit and explicit local periodic-seed proof, exhaustive symbolic controls, exact source attribution and all global/compact/probability limits. Actual complete current whole self-check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete periodic-control theorem and boundaries](#statement) | Entire original D43 Sections1--5/formulas(1)--(11) plus exact source/remaining gate: chronological full-neutral cocycle and field-versus-order domain, all nonzero exact-loop separation with arbitrary nonnegative weights and weighted-energy obstruction, complete torsion-valued Salem Galois independence and finite-trigonometric full-product density for every positive power/arbitrarily late visits, exact loop repetitions plus coordinatewise-outward legal exit/strict finite real neighborhoods, exhaustive horizon-two radial-direction test and quartic/degree-six symbolic controls, explicit infinitely many distinct x_k seeds converging to beta^-1 for every Salem beta in(1,2), no global/limit-point cover or compact termination/word-length uniformity, exact C281 height-one reuse and Dub23 attribution-only original-source depth. |
| argument | [Entire original proof and explicit remaining gate](#argument) | Entire original D43 Sections1--5/formulas(1)--(11) plus exact source/remaining gate: chronological full-neutral cocycle and field-versus-order domain, all nonzero exact-loop separation with arbitrary nonnegative weights and weighted-energy obstruction, complete torsion-valued Salem Galois independence and finite-trigonometric full-product density for every positive power/arbitrarily late visits, exact loop repetitions plus coordinatewise-outward legal exit/strict finite real neighborhoods, exhaustive horizon-two radial-direction test and quartic/degree-six symbolic controls, explicit infinitely many distinct x_k seeds converging to beta^-1 for every Salem beta in(1,2), no global/limit-point cover or compact termination/word-length uniformity, exact C281 height-one reuse and Dub23 attribution-only original-source depth. |
| dependency | [Complete pointwise/finite-hull and real-strip interface](Yin_C_G0416_v1.md#joint-neutral-pointwise-control) | Only the exact local strict-direction/finite convex-hull equivalence, normalization after discarding zero vectors, strict finite real neighborhoods and backward original-digit strip estimate. Global PC/compact termination are not assumed or imported. |
| dependency | [Complete fixed quartic algebraic control](Yin_C_G0396_v1.md#quartic-neutral-descent) | Only actual quartic irreducibility/Salem configuration,17/10<beta<18/10, field trace1 and beta+beta^-1=(1+sqrt13)/2 used in the exact horizon-two example; no extension of its fixed actual-core theorem to all Salem inputs. |
| dependency | [Complete first height-one relation](Yin_C_G0281_v1.md#effective-first-height-one-relation) | Only its original nontrivial {-1,0,1} relation existence when m=log(beta)<log2, with exact original cost/overhead limits; this removes an unnecessary conjectural qualification and supplies no PC or compact-termination implication. |
| support | [Exact classical attribution/statement comparison](../audits/literature/Dub23/Yin_U001.md#dub23-u001) | Only the originally inspected Section2 printed863/PDF2 paragraph before Lemma5, joint rational independence versus weaker individual irrationality, attribution to Salem1963 p32/Pisot and original-monograph/main-source-theorem exclusions. All needed independence/density mathematics is proved locally; no new source-proof audit. |

### Decision explicit-raw-direction-normalization

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:48 |
| status | open |
| reason | State the horizon-two numerical costs in the actual raw unnormalized direction u=-z and preserve the original separate exit-cost-greater-than1/4 versus all-legal-costs-positive conclusions. The complete mathematical argument and every phase/control/domain/source interface are unchanged; this open physical revision makes the statement normalization explicit before the whole current self-check. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire original D43 Sections1--5/formulas(1)--(11) plus exact source/remaining gate: chronological full-neutral cocycle and field-versus-order domain, all nonzero exact-loop separation with arbitrary nonnegative weights and weighted-energy obstruction, complete torsion-valued Salem Galois independence and finite-trigonometric full-product density for every positive power/arbitrarily late visits, exact loop repetitions plus coordinatewise-outward legal exit/strict finite real neighborhoods, exhaustive horizon-two radial-direction test and quartic/degree-six symbolic controls, explicit infinitely many distinct x_k seeds converging to beta^-1 for every Salem beta in(1,2), no global/limit-point cover or compact termination/word-length uniformity, exact C281 height-one reuse and Dub23 attribution-only original-source depth. Horizon-two numerical values refer to raw u=-z, before any unit-direction normalization. |
| argument | [Exact retained argument](#argument) | Entire original D43 Sections1--5/formulas(1)--(11) plus exact source/remaining gate: chronological full-neutral cocycle and field-versus-order domain, all nonzero exact-loop separation with arbitrary nonnegative weights and weighted-energy obstruction, complete torsion-valued Salem Galois independence and finite-trigonometric full-product density for every positive power/arbitrarily late visits, exact loop repetitions plus coordinatewise-outward legal exit/strict finite real neighborhoods, exhaustive horizon-two radial-direction test and quartic/degree-six symbolic controls, explicit infinitely many distinct x_k seeds converging to beta^-1 for every Salem beta in(1,2), no global/limit-point cover or compact termination/word-length uniformity, exact C281 height-one reuse and Dub23 attribution-only original-source depth. Horizon-two numerical values refer to raw u=-z, before any unit-direction normalization. |
| dependency | [Exact retained dependency](Yin_C_G0416_v1.md#joint-neutral-pointwise-control) | Only the exact local strict-direction/finite convex-hull equivalence, normalization after discarding zero vectors, strict finite real neighborhoods and backward original-digit strip estimate. Global PC/compact termination are not assumed or imported. |
| dependency | [Exact retained dependency](Yin_C_G0396_v1.md#quartic-neutral-descent) | Only actual quartic irreducibility/Salem configuration,17/10<beta<18/10, field trace1 and beta+beta^-1=(1+sqrt13)/2 used in the exact horizon-two example; no extension of its fixed actual-core theorem to all Salem inputs. |
| dependency | [Exact retained dependency](Yin_C_G0281_v1.md#effective-first-height-one-relation) | Only its original nontrivial {-1,0,1} relation existence when m=log(beta)<log2, with exact original cost/overhead limits; this removes an unnecessary conjectural qualification and supplies no PC or compact-termination implication. |
| support | [Exact retained support](../audits/literature/Dub23/Yin_U001.md#dub23-u001) | Only the originally inspected Section2 printed863/PDF2 paragraph before Lemma5, joint rational independence versus weaker individual irrationality, attribution to Salem1963 p32/Pisot and original-monograph/main-source-theorem exclusions. All needed independence/density mathematics is proved locally; no new source-proof audit. |

## Complete retained argument

<a id="argument"></a>
<a id="retained-periodic-control-argument"></a>

<a id="periodic-loop-dual-cocycle"></a>
### 1. The endpoint cocycle and an exact loop obstruction

Use C416's original digits, strict endpoint legality and complete neutral coordinates.
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
The pointwise condition in C416 quantifies over real x, so such fractional field points are legitimate tests; they are not asserted to be actual order states.

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
The [exact retained source-reading unit](../audits/literature/Dub23/Yin_U001.md#dub23-u001) distinguishes the joint statement from the weaker individual irrationality in Lemma5.
The exact property needed here has a short direct proof: if integers n_j satisfy product_j zeta_j^(n_j)=1, choose an automorphism of the splitting field sending any fixed zeta_i to beta.
Its inverse conjugate is the unique preimage of beta^(-1), so no other selected zeta_j can map to either real conjugate.
All other images have modulus1.
Taking absolute values of the transformed relation gives beta^(n_i)=1 and hence n_i=0.
This holds for every i.
The same argument, or raising a root-of-unity right-hand side to its order, excludes every nontrivial torsion-valued product.
The Galois/modulus argument in this paragraph uses only the genuine Salem conjugate configuration and beta>1, so its independence interface also applies without beta<2; all control conclusions below keep beta in(1,2).

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
Their strict common real endpoint margin then supplies a neighborhood of x on which every selected word stays strictly legal, so C416's finite-hull argument gives PC throughout that neighborhood.

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

For the fixed quartic of [complete fixed quartic theorem](Yin_C_G0396_v1.md#quartic-neutral-descent), s=1, Tr(beta)=1 and beta+beta^(-1)=(1+sqrt(13))/2.
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
The endpoint condition alone suffices for V_k and its prefixed-loop words; C416's backward real estimate supplies the usual larger intermediate strip if required.

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

## Exact remaining gate and inherited existence interface

The unresolved global question is still C416's PC at every real x in[1/2,1].
A dense family or approximate periodicity does not fill this gate, since expansion magnifies errors during long loop repetitions.
Even full PC only gives compact reduction; compact termination and unchanged original-law probability estimates remain separate.
The earlier suggested height-one-relation qualification is automatic in this interval: the complete [effective first relation theorem](Yin_C_G0281_v1.md#effective-first-height-one-relation) supplies a nontrivial original {-1,0,1} relation whenever m=log(beta)<log2.
This reuses its exact existence/cost scope and supplies no additional PC implication.

## Original source and checking boundary

The original source screen read the exact Dub23 passage and retained its classical attribution only.
The original project reviewer also directly text-read that passage; its full account keeps that source depth and unestablished initial proof context separately.
No original Salem monograph proof or Dub23 main theorem is adopted.
The full Galois and density arguments above have no missing source-supplied proof step.

The original author check, coordinator exit contribution, whole noncontributor inspection, frozen versions and then-pending/fixed-retention history remain at their exact L176/R75 homes.
The current complete finding must check the entire proof, interfaces, exact examples and remaining gate rather than only home-location differences.
The independence mechanism is also the unchanged source interface used by C165's own real-pair/all-beta>1 extension; this proof does not consume that later theorem or create a reverse dependency.
No new native run, numerical word search, source reading, actual-order membership claim, global PC, compact termination or Task execution follows.
