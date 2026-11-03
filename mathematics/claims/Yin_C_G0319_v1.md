---
author: Yin
---

# Rotated iid cocycles have no stationary probability lift and no central coding repair

This retains the complete original 2026-10-07 [L118 mathematical argument](../ledger/Yin_L_G0118_v1.md).
The original coordinating agent derived the direct probabilistic and coding core for Yin; the source interface and fair-bit extension retain the exact contributions and limits in R34 and LS05-U001.
No current Task/E execution, source acquisition or mathematical program run is selected by this maintenance.

## Statement

For every finite-dimensional real inner-product space E, orthogonal U and nonzero v, the rotated fair-sign sums S_N have E norm(S_N)^2=N norm(v)^2, fourth moment at most 3N^2 norm(v)^4, and probability at least 1/12 of norm(S_N)>=norm(v)sqrt(N/2), for every N>=1.
Their laws are not uniformly tight.
Consequently the skew map (omega,x)->(sigma omega,Ux+omega_0 v) on two-sided fair-sign inputs has no invariant probability lift with that marginal, even with arbitrary dependence on all digits or auxiliary central randomness.
It admits no measurable finite-valued central transfer.
For any endpoints satisfying S_N=X_N-U^N X_0 and N>8R^2/norm(v)^2, their two exterior probabilities sum to at least 1/12.
For every positive-Mahler algebraic unit with central conjugates, every full order containing Z[alpha] and its trace-dual lattice, the exact hyperbolic coding seam requires this forbidden noncompact central correction.
The retained LS05 positive-time cocycle has exactly this rotated-sum normalization and fails the same necessary tightness for fair signs and fair bits; the hard source converse and full Salem entropy theorem remain unaudited accepted comparison statements with their actual restrictions.
No assertion excludes every compact toral factor, correlated digit law, alternate coding or finite-window construction; the sqrt(N) boundary scale gives no positive entropy-rate deficit or uniform Mahler gap.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:08 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(11), fair-bit extension and all scope controls: exact moment/probability bounds, arbitrary dependent stationary lift and nonstationary endpoints, lattice intersection and both coding shifts, precise source coordinate/application and restricted source inspection. |
| argument | [Complete argument](#argument) | Entire original (1)--(11), fair-bit extension and all scope controls: exact moment/probability bounds, arbitrary dependent stationary lift and nonstationary endpoints, lattice intersection and both coding shifts, precise source coordinate/application and restricted source inspection. |
| dependency | [Exact retained input](Yin_C_G0299_v1.md#trace-torus-dual-normalization) | Exact trace-dual lattice convention and integral trace matrix; only separability is used here, not hyperbolicity of the new input. |
| dependency | [Exact retained input](../audits/literature/LS05/Yin_U001.md#ls05-u001) | Sufficient retained v2 source coordinate, theorem hypotheses, topology and actual inspected passages; no new original-source inspection or proof of the hard converse is claimed. |
| dependency | [Exact retained input](Yin_C_G0316_v1.md#unit-circle-c0-integer-forcing) | Separate complete decaying-defect obstruction, used only to distinguish its scope from this stationary noncompact lift. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:12 |
| status | proved |
| reason | Adopt the exact complete original theorem and retained argument after actual whole self-review with resolved used inputs, retaining every fixed-input, source-inspection, cube, conditional and uniformity boundary. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(11), fair-bit extension and all scope controls: exact moment/probability bounds, arbitrary dependent stationary lift and nonstationary endpoints, lattice intersection and both coding shifts, precise source coordinate/application and restricted source inspection. |
| argument | [Complete argument](#argument) | Entire original (1)--(11), fair-bit extension and all scope controls: exact moment/probability bounds, arbitrary dependent stationary lift and nonstationary endpoints, lattice intersection and both coding shifts, precise source coordinate/application and restricted source inspection. |
| dependency | [Exact retained input](Yin_C_G0299_v1.md#trace-torus-dual-normalization) | Exact trace-dual lattice convention and integral trace matrix; only separability is used here, not hyperbolicity of the new input. |
| dependency | [Exact retained input](../audits/literature/LS05/Yin_U001.md#ls05-u001) | Sufficient retained v2 source coordinate, theorem hypotheses, topology and actual inspected passages; no new original-source inspection or proof of the hard converse is claimed. |
| dependency | [Exact retained input](Yin_C_G0316_v1.md#unit-circle-c0-integer-forcing) | Separate complete decaying-defect obstruction, used only to distinguish its scope from this stationary noncompact lift. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0550_v1.md#current-iid-lift-finding) | Exact current statement, complete original proof and directly used interfaces; self-reviewed, with actual old findings retained separately at their original inputs and precision. |

## Complete retained argument

<a id="argument"></a>
<a id="rotated-bernoulli-sums-not-tight"></a>
### A quantitative lack of tightness for rotated independent signs

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
### No invariant probability lift, even with dependence on all digits

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
### The exact missing correction in the algebraic-unit coding

Let alpha be an algebraic unit with irreducible polynomial P, log M(P)>0, and at least one unit-circle conjugate.
Let R be a full order in K=Q(alpha) containing Z[alpha], Lambda=R^vee its trace dual, and A multiplication by alpha on K_infinity.
Use the same real trace pairing and complex-coordinate conventions as [L G0104](Yin_C_G0299_v1.md#trace-torus-dual-normalization).
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
### The same obstruction in the retained nonexpansive coding source

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

### Scope for the Lehmer entropy route

This identifies a different obstruction from [L G0115](Yin_C_G0316_v1.md#unit-circle-c0-integer-forcing).
There the obstruction concerned every complete decaying rounded defect.
Here a merely measurable, potentially unbounded central correction fails for the actual iid digit law because its cocycle cannot be tight under a stationary lift.

No assertion excludes all measurable factors of a Bernoulli system onto the compact torus.
A different coding, a changed digit law, correlated digits, or a construction without this noncompact central lift is outside (3) and (9).
In particular a compact torus variable is not the noncompact vector variable used in the proof.

The quantitative finite-window cost in (6) does not prove a positive entropy loss.
A radius of order sqrt(N) in a fixed central dimension has only a logarithmic volume cost.
Thus a finite-window argument could still have sublinear boundary overhead.
Neither h_1<m, h_1=m, nor any positive Lehmer gap follows from this obstruction alone.
