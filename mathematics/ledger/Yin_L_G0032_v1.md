---
author: Yin
---

# G0001: what a multi-place volume certificate must retain

Date: 2026-10-06.
Preserved proof and method-obstruction record supplied by the assigned AI ms25_source for Yin, with probabilistic separation input from the separate review_matrix_completion agent and the coordinator's trinomial control.
This supports the primary [algebraic-entropy strategy](../strategies/Yin_S_G0001.md) and its secondary [affine-growth route](../strategies/Yin_S_G0002.md).
It does not prove a Mahler gap.
The aim is to distinguish exact finite-alphabet entropy capture from stronger uniform geometric certificates that already fail on control families.

The complete reusable mathematical statements and proofs are owned by [C239](../claims/Yin_C_G0239_v1.md#argument); the original question, source comparison, method limits and fixed input remain here.

## Reuse and scope

Use [C212 radical theorem](../claims/Yin_C_G0212_v1.md#radical-collision-control) for the exact radical product decomposition and its irreducibility proof, [L G0007](Yin_L_G0007_v1.md#pisot-salem-attainment) for binary support attainment at a real one-expanding-conjugate unit, and [L G0030](Yin_L_G0030_v1.md#greedy-atom-bound) for the single-place maximum-atom bound.
The all-power-stable control below reuses [Smy08-U002's nonreciprocal gap](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number), the elementary trinomial reciprocal-factor check in [Smy08-U004](../audits/literature/Smy08/Yin_U004.md#smy08-u004), and the unique-largest-modulus fiber mechanism of [L G0017](Yin_L_G0017_v1.md#reciprocal-discriminant-family).
The established algebraic-entropy formula and support upper bound retain their existing source and review boundaries.
No new literature theorem, source acquisition, numerical computation, or novelty claim is used here.

The new geometric obstruction concerns a compact full-dimensional convex body whose width strictly increases in every direction under the specified block map.
It is not an obstruction for arbitrary compact sets, arbitrary finite alphabets, or arbitrary proofs of binary entropy growth.

<a id="same-event-house-obstruction"></a>
## Several embeddings do not supply independent collisions

Let lambda be algebraic, and let delta_j in {-1,0,1} be a fixed finite digit difference.
For every field embedding sigma,

    sum_j delta_j lambda^j=0  if and only if
    sum_j delta_j sigma(lambda)^j=0.

The equivalence follows from injectivity of sigma, since the sum belongs to Q(lambda).
For random digit differences these are therefore the same event on the same probability space.
Likewise, for any finite digit-sum random variable X and x in Q(lambda), the events X=x and sigma(X)=sigma(x) coincide.
Each single embedding and the joint embedding tuple preserve the full list of atom probabilities and every Renyi entropy.
Multiplying one-place collision or atom bounds as if the embedding events were independent is invalid.
This says nothing against a joint geometric argument that actually uses all places simultaneously.

There is a separate limitation of the particular strict largest-term test in L G0030.
Suppose e_0<...<e_k are selected exponents.
At a place of modulus rho>1, that test is

    rho^(e_k) > sum_(j<k) rho^(e_j),

or equivalently sum_(j<k) rho^(e_j-e_k)<1.
The expression on the left decreases strictly with rho when k>=1.
Thus if this test succeeds at any expanding place, it succeeds at the place of maximum modulus.
Allowing the place to change with the tested finite subset gives no improvement over using the house throughout.
This conclusion concerns this sufficient triangle-inequality test, not every argument that can prove a nonzero digit sum.

<a id="strict-width-block-obstruction"></a>
## A dimension obstruction for adapted-body covers

Let U be a real vector space of dimension r>=1, let A:U->U be invertible, and fix an integer N>=1.
For a compact full-dimensional convex body K and a nonzero real linear functional ell, define

    w_K(ell)=max_(x in K) ell(x)-min_(x in K) ell(x)>0.

Assume the strict-width property

    w_(A^N K)(ell)>w_K(ell) for every nonzero ell.       (1)

If D is a finite nonempty set and

    A^N K subset D+K,                                  (2)

then the affine span of D is all of U.
Indeed, if its affine span is proper, some nonzero ell is constant on D.
The width of D+K in that direction is then exactly w_K(ell).
Inclusion (2) contradicts (1).

In particular, for a vector v in U consider the length-N binary block digits

    D_N={sum_(j=0)^(N-1) b_j A^j v : b_j in {0,1}}.

Their affine span lies in span(v,Av,...,A^(N-1)v), which has dimension at most N.
A cover A^N K subset D_N+K under (1) therefore requires

    N>=r.                                              (3)

More generally, if an alphabet F has affine-difference span of dimension t, its N-step digit set has affine-difference span of dimension at most Nt.
Such a cover requires Nt>=r.
Without this dimension information one still obtains |D|>=r+1 from full affine span.

The hypothesis is natural for a usual expanding Minkowski body.
Decompose U into real one-dimensional and complex two-dimensional embedding blocks, on which A acts by multiplication by beta_sigma, all with |beta_sigma|>1.
Take K to be a product of centered intervals of positive radius in the real blocks and centered discs of positive radius in the complex blocks.
The width in a functional ell=(ell_sigma) is the sum of the block widths.
Applying A^N multiplies each nonzero block contribution by |beta_sigma|^N; complex rotation does not change the Euclidean dual norm.
Thus (1) holds for every N>=1.
The real dimension r counts complex blocks twice.
Its determinant is

    |det A|=product_sigma |beta_sigma|^(dim_R block_sigma).

Small total expanding determinant does not remove the necessary block length (3).
In particular, a binary one-step cover by this class of bodies cannot generalize the one-dimensional interval cover of L G0007 when r>=2.

The strict-width assumption is essential.
The proof does not assert (1) for an arbitrary body merely because all eigenvalues expand.
It also does not rule out a nonconvex invariant set, a body whose directional widths do not all increase, a degree-dependent block construction, or a method that uses arithmetic information beyond such a cover.

<a id="radical-full-place-control"></a>
## Fixed Mahler measure, growing expanding dimension, and a sharp block witness

Put phi=(1+sqrt(5))/2, r=2^k, lambda=phi^(1/r), and

    p_r(t)=t^(2r)-t^r-1.

L G0005 proves irreducibility by successive square roots: at each stage the monic minimal polynomial has even degree and constant term -1, so its chosen root has field norm -1 and cannot be a square in its own field.
Thus [Q(lambda):Q]=2r and [Q(lambda):Q(phi)]=r.
This is the existing proof, not an assumption about the degree of a substituted polynomial.

Exactly r conjugates satisfy beta^r=phi and have modulus rho=phi^(1/r)>1.
The other r satisfy beta^r=-1/phi and have modulus phi^(-1/r)<1.
Hence the expanding real Minkowski space U has dimension r, the house tends to 1, and

    M(p_r)=phi,    log M(p_r)=log phi

for every r.
These are nonreciprocal controls, already outside the unresolved reciprocal core; their purpose here is to test a proposed uniform certificate on the broader bounded-measure class, not to claim a new hard-case family.

Write A for multiplication by lambda on U, and v for the expanding embedding of 1.
Then A^r=phi I.
The vectors

    v, Av, ..., A^(r-1)v

form a real basis of U.
To see this, a real linear dependence would be a real polynomial of degree less than r vanishing at all r distinct expanding roots of t^r-phi, which is impossible.
Complex-coordinate conjugacy identifies these evaluations with the r-dimensional real Minkowski space.

Let V denote the isomorphism with those basis columns, and let R=1/(phi-1)>1.
Define the parallelotope

    K=V[0,R]^r,      D_r=V{0,1}^r.

Because phi R=R+1 and [0,R] union [1,R+1]=[0,R+1],

    A^r K=V[0,R+1]^r=D_r+K.                            (4)

This K has strictly increasing width under A^r=phi I, so (4) attains the necessary block length N>=r within the strict-width class.
For a given N<r, the preceding theorem excludes every cover satisfying (1); it does not claim (1) for this parallelotope under every smaller power.

In fact this same parallelotope admits a one-step cover outside the strict-width class.
In the V basis, multiplication is

    (x_0,...,x_(r-1)) -> (phi x_(r-1),x_0,...,x_(r-2)).

Consequently

    A K=V([0,R+1] x [0,R]^(r-1))=K union (K+v).        (4a)

For r>1 the widths in the latter r-1 coordinate directions are unchanged.
Thus (1) fails at N=1, exactly where the obstruction does not apply.
All eigenvalues of A expand, yet this full-dimensional convex body admits binary one-step covering.
This is an explicit counterexample to deleting the strict-width hypothesis.
The one-step identity also gives support lower bounds phi^n for every n directly by iteration and volume.

Iterating (4) gives A^(jr)K=T_(jr)(A,{0,v})+K.
Taking r-dimensional volume yields

    |T_(jr)(A,{0,v})| >= |det A|^(jr)=phi^(jr).

The projection of full algebraic digit sums to U cannot increase their cardinality, so this is also a lower bound for the full support at those lengths.
The full entropy equality also follows directly from the exact product decomposition below.
An increasing block length is necessary within the strict-width certificate class, even while total Mahler measure and the actual binary entropy rate stay fixed; it is not necessary for all convex-body covers.

<a id="all-renyi-radical-product"></a>
## Exact product splitting retains all entropy orders

More generally, let lambda!=0 be algebraic and r>=1 an integer, and suppose lambda^r=beta and [Q(lambda):Q(beta)]=r.
The basis 1,lambda,...,lambda^(r-1) over Q(beta) makes addition of the r residue-class digit sums injective.
For n=qr+s with 0<=s<r, the binary-sum law at lambda is therefore an injective image of s independent copies of the length-(q+1) law at beta and r-s copies of its length-q law.
Use X_0=0 and H_alpha(X_0)=0, including when n<r.

For every Renyi order alpha in [0,infinity], including Shannon at 1, support at 0, and maximum-atom entropy at infinity, independence and injectivity give exactly

    H_alpha(X_n(lambda))
       =s H_alpha(X_(q+1)(beta))+(r-s) H_alpha(X_q(beta)).       (5)

For finite positive orders other than 1, the power sum of product probabilities factors; Shannon entropy is additive; supports multiply; and maximum atom probabilities multiply.
Thus (5) includes the endpoints without a Shannon-to-Renyi comparison.
The rate existence argument is the subadditivity already recorded in L G0030.
Keeping r fixed while n tends to infinity gives

    h_alpha(lambda)=h_alpha(beta) for every alpha.              (6)

There is no factor 1/r, because the r independent residue classes compensate for their shorter lengths.
No varying-r/time limit interchange is made.

For the phi radical family, L G0007 gives h_0(phi)=log phi, so h_0(lambda)=log phi.
L G0030 supplies a positive lower bound for h_infinity(phi), and (6) preserves it at every r.
In contrast the single-house bound from L G0030 at lambda is

    log(2) (log phi/r)/log(1+phi^(1/r)),

which tends to zero.
This is a demonstrated loss of that certificate, not decay of the actual entropy.
Separate-place zero events and strict modulus domination cannot recover the compensation; the exact field-basis product splitting does.

The same transfer applies to a root of any polynomial p_beta from L G0030's one-expanding-conjugate scope whenever the stated relative degree is r.
The minimal polynomial of lambda is then p_beta(t^r): it vanishes at lambda and has degree r deg(beta), equal to [Q(lambda):Q].
Each root of p_beta contributes its r-th roots, so m(lambda)=m(beta).
Equations (5)--(6) transfer the exact quadratic comparison 0<=m-h_alpha<=m^2/(2 log2) to these radical lifts, despite their potentially many expanding places.
The required field-basis hypothesis is not available for an arbitrary unit.

<a id="power-stable-many-expanding-control"></a>
## The strict-width loss persists after all-power degree reduction

The coordinator supplied the following stronger control, whose argument is checked here.
For n>=3, put P_n(t)=t^n-t-1 and let alpha_n>1 be its positive real root.
The function t^n-t-1 is strictly increasing on [1,infinity), is negative at 1, and tends to infinity, so alpha_n exists and is unique there.
For any complex root z with |z|>1,

    |z|^n=|z+1|<=|z|+1

implies |z|<=alpha_n.
Equality of moduli forces equality in the triangle inequality, hence z is positive real and z=alpha_n.
Thus alpha_n is the unique root of largest modulus among all roots of P_n, including those in its actual monic minimal polynomial p_n.

The polynomial p_n is an integral unit polynomial: its monic integral cofactor in P_n has integer constant coefficient and their constant coefficients multiply to -1.
It is nonreciprocal.
Indeed

    P_n(t)+P_n^*(t)=-t-t^(n-1),

which does not vanish at alpha_n>1.
A reciprocal p_n would divide both P_n and P_n^*, giving a contradiction.
This is the elementary trinomial-factor mechanism already checked in Smy08-U004.
The accepted nonreciprocal theorem in Smy08-U002 therefore gives M(p_n)>=theta_0, where theta_0>1 is the real root of t^3-t-1.

There is also a uniform upper bound requiring no irreducibility theorem for P_n:

    M(p_n)<=M(P_n)<=sqrt(3).                            (7)

The first inequality uses multiplicativity and M>=1 for a monic integer cofactor.
For the second, Jensen's inequality for log applied to the circle integral of |P_n|^2 gives log M(P_n)<=log(||P_n||_2); Parseval gives ||P_n||_2=sqrt(3).
The logarithmic zeros are integrable, or the same calculation follows by positive regularization and a limit.
No cited sharper trinomial measure inequality is needed.

Since alpha_n^(n-1)=1+1/alpha_n<2, its house satisfies

    log house(p_n)=log alpha_n<log2/(n-1).

If r_n counts the expanding conjugates of p_n, with complex conjugates counted separately as real dimensions, then

    log theta_0 <= log M(p_n) <= r_n log alpha_n,

so

    r_n > (n-1) log theta_0/log2.                        (8)

Every positive power of alpha_n preserves its degree.
For a fixed power q, the embeddings of Q(alpha_n) over each embedding of Q(alpha_n^q) have the same fiber size [Q(alpha_n):Q(alpha_n^q)] in characteristic zero.
The fiber over alpha_n^q contains only alpha_n, since any conjugate with the same q-th power would have its uniquely maximal modulus.
Hence the common fiber size is one.

This supplies bounded-measure irreducible units with unbounded expanding dimension and with every positive power preserving degree.
The strict-width cover consequently requires unbounded binary block lengths N>=r_n even after the degree-reducing power mechanism of L G0014 has been exhausted.
Likewise the house-only rate in L G0030 tends to zero while log M(p_n)>=log theta_0.
No decay of the actual collision or maximum-atom rate is inferred.

These p_n are nonreciprocal and their measures stay above theta_0.
The control rules out the stronger certificate claim on the bounded-measure, all-power-preserving class; it does not settle the remaining small reciprocal core M<theta_0 and is not a Lehmer counterexample.
No Selmer irreducibility result, degree formula for p_n, or assertion that all P_n roots belong to p_n was used.

## Finite-alphabet capture and the remaining arithmetic question

For context, a parameter-dependent finite alphabet can capture every expanding place without a binary or uniform-block restriction.
Let B in GL_d(Z), Q=[0,1]^d, and

    F={floor(Bx):x in Q},

where floor is coordinatewise.
This is a finite subset of Z^d, and BQ subset F+Q.
Let pi_u be the real spectral projection onto the expanding generalized eigenspaces, commuting with B, and write B_u for the restriction.
If the expanding dimension is positive, K_u=pi_u Q is compact, convex, and has positive volume in that subspace.
Projection and iteration give

    B_u^n K_u subset pi_u T_n(B,F)+K_u.

Volume subadditivity therefore yields |T_n(B,F)|>=|det B_u|^n for every n>=1.
The accepted integral Yuzvinski formula supplies the matching asymptotic upper bound log|det B_u|, so this explicit F attains the algebraic entropy.
When there is no expanding space, the total entropy is zero and the volume argument is unnecessary.
This construction is a direct finite-dimensional control consistent with L G0002's accepted finite-set attainment, not a new solution of infinite finite-capture failure.

Neither the size of F nor its relation to one binary cyclic alphabet is uniform here.
For rational nonintegral B the same real-place reasoning would omit finite-place contributions; no adelic extension or full rational entropy formula is inferred from this construction.

The changed next action is precise: do not seek a parameter-uniform fixed block cover by an adapted expanding Minkowski body on the whole bounded-measure class tested here, and do not multiply embedding collision bounds.
The exhibited families do not establish the same obstruction on the small reciprocal core.
A continuing route must supply an actual product decomposition, a body outside the strict-width class, a justified degree-dependent block argument whose entropy normalization retains all places, or a new arithmetic obstruction to small Mahler measure.
The radical product is a control showing what successful compensation looks like; it is not asserted to exist for general reciprocal units.
None of these observations resolves G0001.

The complete original author/contributor/reviewer account is retained in [R518](../audits/reviews/Yin_R_G0518_v1.md#original-multiplace-contributor-finding), preserving every supplied proof part and the distinct noncontributed unknown scopes.
