---
author: Yin
---

# An iid central cocycle cannot have a stationary probability lift

Date: 2026-10-07.
Direct derivation by the coordinating AI for Yin, within the primary entropy route of G0001.
The goal is to test the missing central correction in the hyperbolic coding of L G0104--L G0106.
This is a precise obstruction for that construction, not a statement that all toral factors or finite-window encodings are impossible.

<a id="rotated-bernoulli-sums-not-tight"></a>
## A quantitative lack of tightness for rotated independent signs

Let E be a finite-dimensional real inner-product space, U an orthogonal linear map, and v a nonzero vector.
Let xi_0,xi_1,... be independent fair signs.
For every N>=1 put

    S_N=sum_(j=0)^(N-1) xi_j U^(N-1-j)v,
    a=||v||>0.

Writing v_j=U^(N-1-j)v, direct expansion gives

    E||S_N||^2=N a^2,
    E||S_N||^4=(sum_j ||v_j||^2)^2
                      +4 sum_(i<j) <v_i,v_j>^2
                <=(3N^2-2N)a^4<=3N^2 a^4.             (1)

Indeed ||S_N||^2=sum_j||v_j||^2+2sum_(i<j)xi_i xi_j <v_i,v_j>.
In its square the only nonzero expectations among the off-diagonal terms have the same unordered index pair.
Orthogonality gives ||v_j||=a and the last inequality follows from Cauchy--Schwarz.

For any nonnegative random variable Y of finite second moment and 0<lambda<1, split its expectation on Y<lambda E Y and the complement.
Cauchy--Schwarz then gives

    P(Y>=lambda E Y)>=(1-lambda)^2 (E Y)^2/E(Y^2).

Applying this elementary second-moment inequality to Y=||S_N||^2, lambda=1/2, proves

    P(||S_N||>=a sqrt(N/2))>=1/12.                      (2)

Consequently the laws of S_N are not uniformly tight.
For each fixed radius R, choose N with a sqrt(N/2)>R.
Their probability outside the radius-R ball is then at least 1/12.
This proof needs neither a limit theorem nor any arithmetic independence of the eigenvalues of U.

<a id="bernoulli-central-stationary-lift-obstruction"></a>
## No invariant probability lift, even with dependence on all digits

Let Omega={-1,1}^Z with its fair product law p, and let sigma be the left shift, (sigma omega)_j=omega_(j+1).
Consider the skew transformation

    F(omega,x)=(sigma omega, Ux+omega_0 v)              (3)

on Omega x E.
There is no F-invariant probability measure projecting to p.
In particular there is no measurable, finite-valued b:Omega->E satisfying b(sigma omega)=U b(omega)+omega_0 v almost everywhere.

Suppose a lift existed, and write X_0=x and X_N for its central coordinate after N iterations.
Algebraically,

    S_N=X_N-U^N X_0.                                   (4)

The signs in S_N have precisely the prescribed product law, regardless of any dependence between X_0 and the entire digit sequence.
Invariance makes X_N and X_0 identically distributed.
Since U is an isometry,

    P(||S_N||>2R)<=P(||X_N||>R)+P(||X_0||>R)
                       =2P(||X_0||>R).                 (5)

Every probability on finite-dimensional E has tails tending to zero.
Thus (5) would make the S_N laws uniformly tight, contradicting (2).
No moment assumption, independence of X_0, adaptedness, or continuity of a proposed transfer b is needed.
A measurable transfer would give the forbidden invariant graph measure, which proves that assertion too.

This also quantifies the finite-window boundary cost.
For any coupled endpoints obeying (4), if N>8R^2/a^2, then

    P(||X_0||>R)+P(||X_N||>R)>=1/12.                    (6)

At least one endpoint therefore has probability at least 1/24 outside the radius-R ball.
This does not require stationarity.
It says a uniformly tight family of both endpoints is impossible as N grows.
The scale is sqrt(N), not an asserted exponential or entropy-rate cost.

The same argument applies to a right shift and any fixed coordinate of the independent digit sequence.
Iteration still uses distinct, independent fair signs; their order does not affect (1)--(2).

<a id="missing-center-in-actual-toral-coding"></a>
## The exact missing correction in the algebraic-unit coding

Let alpha be an algebraic unit with irreducible polynomial P, log M(P)>0, and at least one unit-circle conjugate.
Let R be a full order in K=Q(alpha) containing Z[alpha], Lambda=R^vee its trace dual, and A multiplication by alpha on K_infinity.
Use the same real trace pairing and complex-coordinate conventions as [L G0104](Yin_L_G0104_v1.md#trace-torus-dual-normalization).
That section's trace-matrix argument, which needs only separability, gives a full lattice Lambda contained in K and R contained in Lambda.
This elementary dual-lattice statement does not use hyperbolicity.

Write E_s,E_u,E_c for the stable, expanding and central embedding spaces, and e_s,e_u,e_c for the corresponding projections.
Both E_s and E_u are nonzero, by positive measure and the unit norm.
On E_c, A_c=A|E_c is orthogonal for the usual real/complex Euclidean norm.
The vector v=e_c 1 is nonzero.
Moreover

    E_c intersect Lambda={0}.                          (7)

In fact an element of Lambda comes from K; membership in E_c makes its stable embedding zero, and an injective field embedding can vanish only on zero.
No lattice in the center is silently introduced.

For a two-sided sign sequence retain the summable hyperbolic part

    r_j=A^j e_s 1          (j>=0),
    r_j=-A^j e_u 1         (j<0),
    x(omega)=sum_(j in Z) omega_j r_j.

This series converges uniformly, but the seam now obeys

    A r_(-1)-r_0=-1+v.

For the right shift (tau omega)_j=omega_(j-1), the exact identity is

    A x(omega)-x(tau omega)=omega_(-1)(-1+v).           (8)

Suppose one tries to repair this specific coding by an arbitrary measurable central term b(omega) in E_c, so that

    kappa(omega)=[x(omega)+b(omega)] in K_infinity/Lambda

intertwines tau with multiplication by alpha almost surely.
From (8), the discrepancy modulo Lambda is omega_(-1)v+A_c b(omega)-b(tau omega), because the term -omega_(-1)1 already lies in Lambda.
This remaining discrepancy lies in E_c, so (7) forces the exact equation

    b(tau omega)=A_c b(omega)+omega_(-1)v.              (9)

The previous theorem, in its right-shift version, rules out (9).
It even rules out replacing the graph of b by a stationary probability extension carrying an additional random central coordinate.
Thus the hyperbolic iid coding cannot be extended by this central correction.

<a id="ls05-central-cocycle-iid-interface"></a>
## The same obstruction in the retained nonexpansive coding source

The retained v2 of Lindenstrauss--Schmidt, *Symbolic representations of nonexpansive group automorphisms*, supplies a directly relevant coding model; its actual inspected source interface is recorded in [LS05-U001](../audits/literature/LS05/Yin_U001.md#ls05-u001).
The coordinator and assigned source agent inspected the retained printed/PDF pp.7,12,15--16, including the formula normalization below.
The hard converse tightness-to-coboundary theorem is not needed in this local iid obstruction.

For f=P, source (2.15)--(2.17), p.7, give the central mode basis (beta^l)_(l in Z) and the central sequence

    w^(Delta0)_l=sum_(|beta|=1) beta^(l-1)/P'(beta).

The displayed partial-fraction normalization has b_beta/f_d=1/P'(beta).
By (4.8), p.12, the coefficient of the beta-mode in d(N,omega) is

    [d(N,omega)]_beta
       =beta^(N-1)/P'(beta)
                         sum_(j=0)^(N-1) omega_j beta^(-j). (10)

Indeed the source shift on the central basis multiplies it by beta, and d(N,omega)=sum_(j=0)^(N-1) omega_j S^(N-j)w^(Delta0).
There is no unrecorded bounded remainder or coboundary in (10).

Identify the real central space with the conjugation-symmetric tuples (c_beta) over all unit-circle roots, use norm squared sum_beta|c_beta|^2, let U multiply the beta-coordinate by beta, and put v_beta=1/P'(beta).
Then (10) is precisely S_N in (1), with

    a^2=sum_(|beta|=1)|P'(beta)|^(-2)>0.               (11)

Thus this source's central cocycle is not uniformly tight under fair iid signs.
Theorem 4.13, pp.15--16, lists invariant probability lift, uniform tightness of d(k,.) in the finite-dimensional central space, and measurable central coboundary as equivalent conditions; Definition 4.14 calls such laws weakly d-bounded.
The iid law fails that condition.
The necessary lift-to-tightness implication is proved in the source on p.16 and is also independently proved here by (4)--(5).
No use is made of the source's harder converse or its external reference [18].

The usual fair {0,1} digits have the same obstruction, not merely the same algebraic-sum entropy.
Write B_j=(1+xi_j)/2.
Their central cocycle is one half of the fair-sign cocycle plus (1/2)sum_(j=0)^(N-1) U^j v.
No central beta equals one, since P is irreducible and noncyclotomic.
In each coordinate the geometric sum is therefore uniformly bounded in N; there are finitely many coordinates.
A uniformly bounded deterministic translation cannot turn a family which is not tight into a tight one.
Thus the {0,1} law also fails the necessary condition.

The source's Salem entropy-preserving statement, Theorem 6.3 on p.25, assumes both weak d-boundedness and support on the two-sided beta-shift.
It therefore does not supply an entropy-preserving representation for the unrestricted fair iid algebraic-sum law used in G0001.
In addition to any digit-support issue, (10)--(11) directly disprove the necessary tightness for that law.
This is a source applicability check, not a claim to have re-audited all of Theorem 6.3 or the whole article.

## Scope for the Lehmer entropy route

This identifies a different obstruction from [L G0115](Yin_L_G0115_v1.md#unit-circle-c0-integer-forcing).
There the obstruction concerned every complete decaying rounded defect.
Here a merely measurable, potentially unbounded central correction fails for the actual iid digit law because its cocycle cannot be tight under a stationary lift.

No assertion excludes all measurable factors of a Bernoulli system onto the compact torus.
A different coding, a changed digit law, correlated digits, or a construction without this noncompact central lift is outside (3) and (9).
In particular a compact torus variable is not the noncompact vector variable used in the proof.

The quantitative finite-window cost in (6) does not prove a positive entropy loss.
A radius of order sqrt(N) in a fixed central dimension has only a logarithmic volume cost.
Thus a finite-window argument could still have sublinear boundary overhead.
Neither h_1<m, h_1=m, nor any positive Lehmer gap follows from this obstruction alone.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0034_v1.md#contribution-and-review-scope), with its original inspected scope and relationship.
