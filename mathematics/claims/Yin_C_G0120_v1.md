---
author: Yin
---

# Paid stability of original Salem zero-coordinate Gram rigidity

Date: 2026-10-14T21:12.
Human author Yin.
The delegated strategy_critique AI authors this G0001 continuation.
Root supplied the research direction only, not a proof step.
Shared execution/task/strategy decisions and fixed adoption remain root-owned.

## Responsible question

Investigate whether the actual original-width real Salem zero-coordinate rigidity in C117 gives an explicit useful obstruction for REAL almost-PSD matrices with EXACT original circle symbol and fixed positive objective gain, or for sparse PSD correction matrices.
Retain every original degree, coefficient height, embedding and spectral parameter.
Do not use a rational denominator floor, fixed-input compactness alone, a restatement of C110/C113, or a silently uniform circle-factor stability estimate as the new result.

## Initial reuse and execution boundary

The author read the complete actual C110 v2 and has read C113 and C117's full original argument.
The intended reuse screen includes prior circle-factor stability and finite coefficient-Gram interfaces.
New reasoning will be retained incrementally here.
No mathematical native program or J is proposed; any such execution would require its own prior responsible declaration.
This draft initially asserted no theorem; the first substantive mechanism is retained below while its complete bounds are developed.

<a id="circle-visible-correction-working-mechanism"></a>
## First retained mechanism: a correction budget at actual circle roots

Use C117's actual irreducible Salem P, d=2h, N=d+1, t, C and coefficient multiplication matrix M (N by3).
Let q=d-2 and let V be the q-by-N evaluation matrix with rows(1,zeta,...,zeta^d), at ALL q circle roots zeta.
Its kernel is the coefficient space of multiples of C, so its rank is q; set s=the smallest positive singular value of V and kappa=||M^dagger||.
Both are actual positive finite input parameters, not uniform constants.
The conjugate-stable circle-root list makes the orthogonal projection Pi onto ker V real.

Let Q be any REAL symmetric exact-same-symbol matrix, let R be a REAL PSD correction with Q+R PSD, and put H0=sum p_j^2, T=H0+trace R, r=||R||, S=sum_zeta v_d(zeta)^*R v_d(zeta).
These quantities are nonnegative, T>0.
At each circle root, the exact symbol gives v^*Qv=0.
PSD spectral inequalities for B=Q+R and R give

    ||Qv|| <= (sqrt(T)+sqrt(r)) sqrt(v^*Rv).

Consequently, with

    tau=2(sqrt(T)+sqrt(r)) sqrt(S)/s,

one has ||Q-Pi Q Pi||<=tau.
The quotient S/s^2 is a PAID actual-circle evaluation expense, independent of rational denominators.
It does not infer that R must have a large rank.

The decisive qualitative case is S=0.
Then R and Q+R vanish on all circle evaluation vectors, so Q and R both have range in the original three-dimensional coefficient-multiplication subspace.
Q need not lie in the PSD face, because it may be indefinite.
If an original NONCENTRAL zero j has Qjj=Rjj=0, PSD gives (Q+R)e_j=Re_j=0.
Hence Qe_j=0.
C117's invertible three-by-three system, which uses only the exact affine fiber and this vector equation, forces Q=pp^T even though Q itself was not assumed PSD.
Thus a circle-invisible PSD correction for a nontrivial exact-symbol Q with its original zero diagonals unchanged MUST put positive mass at every noncentral missing coordinate.
The central zero is not covered by that invertibility argument.

There is an exact central control, not a conjectured extension.
Put W=C(1-z^2), let w be its coefficient vector, and for any a>0 define

    Q_a=pp^T+(a/2)(p w^T+w p^T),
    R_a=(a^2/4) w w^T.

On the circle, P/z^(h) is real and W/z^(h) is purely imaginary, so the cross term has zero real symbol.
Thus Q_a represents EXACTLY |P|^2, (Q_a)00=1+a, and

    Q_a+R_a=(p+(a/2)w)(p+(a/2)w)^T >=0.

R_a has rank1, is circle-invisible, and has trace/operator norm(a^2/4)||w||^2.
All original zero diagonals of Q_a stay zero.
By C117, w_j=c_j-c_(j-2) is nonzero at every noncentral interior index and w_h=0.
Therefore R_a pays EVERY noncentral original zero coordinate but keeps a central zero untouched.
This precisely prevents a false all-zero-coordinate extension to PSD corrections.
It is not a uniformly small correction, not a new Mahler gain, and not a rational-coefficient construction: w lies in the original trace field.

The quantitative continuation below prices how small S and Rjj can be when a fixed positive objective is requested, and specializes to R=epsilon I for an explicit REAL almost-PSD error floor.
The initial observation above is preserved as the actual incremental development; the exact final statements and proof follow.

<a id="reuse-and-model-boundaries"></a>
## 1. Exact reuse screen and model boundaries

The complete [C110 v2](Yin_C_G0110_v2.md#statement) already proves a real regularization-corrected lower certificate and a rational all-root denominator floor.
Its elementary PSD estimate at a circle root is explicitly reused here, not claimed as new.
[C113](Yin_C_G0113_v1.md#localized-gram-correction) already allows a justified localized PSD correction and prices its whole symbol; its Sidon-support argument has a different independent-phase hypothesis.
[C117](Yin_C_G0117_v1.md#statement), now actually adopted after R349, supplies the exact original Salem coefficient identities, noncentral invertibility, central exception and complete height/norm bounds.
This author contributed C117 and is not independently reviewing that input.

The author also read [F110](../ledger/Yin_L_F0006_v1.md#coefficient-optimizer-degeneration) in full: its fixed-input root-regularization constants and compactness do not supply the estimates below.
The current complete home of that unchanged fixed-input comparison is [C_F7](Yin_C_F0007_v1.md#coefficient-optimizer-degeneration), with the same input-dependent constants and value-versus-derivative limits.
Bounded searches for circle-factor stability, approximate divisibility, coefficient-Gram Vandermonde control and near-face estimates found L61/L343 Vandermonde mechanisms in different arithmetic/dynamical settings, and the existing root estimates in C110/L361.
The used statements were checked at that limited scope; no prior whole-face quantitative theorem was silently imported.
No new external source theorem, source-proof expansion, novel general singular-value theorem, or historical novelty assertion is made.
The projection, triangular coefficient recovery and all required inequalities are proved locally.

The new point is an explicit original-input tradeoff between correction values at the ACTUAL circle roots and a missing coefficient coordinate, including a stronger obstruction for a missing whole row.
Diagonal absence and support absence must be distinguished for indefinite Q.
All coefficients of Q and R may be arbitrary reals.
No denominator lower bound or rational approximation is involved.
The correction can have rank1; rank alone will not control its cost.

## Statement

Retain the actual irreducible Salem P and all notation from the first mechanism, with original width d=2h>=4.
Thus P=(1-tz+z^2)C, C has degree q=d-2, c0=cq=1, M is coefficient multiplication by C, and V contains ALL q circle-root evaluations at width d.
Define

    H0=sum_(k=0)^d p_k^2, s=sigma_min(V)>0,
    kappa=||M^dagger||,
    alpha=2c1, beta=2c2+c1^2,
    K0=3+|alpha|(2+|alpha|)+|beta|,
    K1=2+|alpha|, K=K0+2K1+2, A=1+K0.          (1)

Here sigma_min(V) means the smallest of its q positive singular values, M^dagger is the Moore--Penrose inverse, and v_d(z)=(1,z,...,z^d)^T.
All norms are Euclidean/operator norms unless a Frobenius subscript is displayed.
Let Q,R be REAL symmetric N-by-N matrices satisfying

    v_d(z)^*Qv_d(z)=|P(z)|^2 on T,
    R>=0, Q+R>=0, Q00>=1+gamma, gamma>0.        (2)

Put

    r=||R||, T=H0+trace R,
    S=sum_(P(zeta)=0, |zeta|=1) v_d(zeta)^*R v_d(zeta),
    tau=2(sqrt(T)+sqrt(r)) sqrt(S)/s.            (3)

All q roots, both members of each complex conjugate pair, occur in S.
No normalized average replaces that sum.

**A. Noncentral coordinate and whole-row tradeoffs.**
Suppose p_j=0 and 1<=j<=d-1, j!=h.
Use C117's

    ell_j=(x,y,z)=(c_j,c_(j-1),c_(j-2)),
    Delta_j=(x-z)(y^2-xz)!=0,
    u_j=(y^2-xz+z^2,yz,y^2),
    U_j=||u_j||/|Delta_j|,
    L_j=A+U_j(kappa+K||ell_j||).                (4)

Then

    gamma <= U_j kappa ||Q e_j||+L_j tau.       (5)

If Qjj<=delta with a supplied delta>=0, writing r_j=Rjj gives the fully correction-based version

    gamma <= U_j kappa[sqrt(T(delta+r_j))+sqrt(r r_j)]
                         +L_j tau.             (6)

In particular Qjj=0 implies

    gamma <= (sqrt(T)+sqrt(r))
             [U_j kappa sqrt(r_j)+2L_j sqrt(S)/s]. (7)

If the WHOLE row/column Qe_j is zero, (5) gives the stronger necessary expense

    S >= s^2 gamma^2/[4 L_j^2(sqrt(T)+sqrt(r))^2]. (8)

Thus no nontrivial same-symbol Q with a missing noncentral original-zero row can be repaired by ANY PSD correction whose symbol vanishes at every original circle root.
This last no-gain statement holds for Q!=pp^T even without a positive objective, by the exact linear argument in the proof.

**B. Denominator-free REAL almost-PSD floor.**
Suppose Q has the exact original symbol, Qjj=0 at a noncentral original zero j, Q00>=1+gamma, and Q+epsilon I>=0 with epsilon>=0.
Set

    D_j=(sqrt(H0+1)+1)
          [U_j kappa+2L_j sqrt(qN)/s].          (9)

Then

    epsilon >= min{1/N, gamma^2/D_j^2}.         (10)

For the stronger condition Qe_j=0, the same bound holds with the smaller constant D_j^row=(sqrt(H0+1)+1)2L_j sqrt(qN)/s.
These are explicit original-input bounds, not a compactness argument.
Their constants are not asserted uniform in degree, height or circle-root geometry.

**C. Central coordinate, with its separate paid estimate.**
If p_h=0, put ell_h=(x,y,x) and D=x^2-y^2>0 from C117.
Suppose Qhh<=delta, delta>=0, and set

    J_h=1+K||ell_h||^2, e=kappa^2 r+K tau,
    F=T+A tau+e.

Then

    max(0,gamma-A tau)^2
        <= e(2+e)+F(delta+J_h tau)/D.           (11)

In particular for Qhh=0 and R=epsilon I define

    J=2(sqrt(H0+1)+1)sqrt(qN)/s,
    E=kappa^2+KJ, F0=H0+1+AJ+E,
    G=E(2+E)+F0 J_h J/D.

One has the explicit safe floor

    epsilon >= min{1/N, gamma^2/(4A^2J^2),
                              gamma^4/(16G^2)}. (12)

No optimality of this central exponent is claimed.

**D. Paid parameters and exact rank-one control.**
All parameters in A--C can either be retained as certified original spectral/algebraic data, or bounded using the explicit degree/height/measure substitutions in Section6 below.
No field embedding or denominator is silently discarded.
For every such P and every a>0, the Q_a,R_a pair retained above satisfies(2) with gamma=a, preserves every original zero DIAGONAL, and has R_a of rank1, S=0 and

    trace R_a=||R_a||=(a^2/4)||w||^2,
    (R_a)jj=(a^2/4)(c_j-c_(j-2))^2.           (13)

Q_a has exactly one positive and one negative eigenvalue, all remaining eigenvalues zero.
If W0=||w||^2, the magnitude of its negative eigenvalue is exactly

    epsilon_a=(sqrt(H0^2+a^2 H0 W0)-H0)/2.     (14)

For each FIXED original P, epsilon_a~a^2 W0/4 as a tends to0.
Thus no lower bound epsilon>=c_P gamma^b with c_P>0 and b<2 can hold for all sufficiently small positive gains at this diagonal-only scope when a noncentral original zero exists.
This does not establish a sharp constant, a whole-row example, or optimality of(12).
At a central original zero the whole Q_a row and the correction row both vanish; a central version of the qualitative no-repair claim in A would therefore be false.

The results retain original width, irreducible Salem input, exact symbol, real symmetry and every stated coordinate hypothesis.
No actual near-one sequence, uniform positive gain, arbitrary padding, general reciprocal reduction or Mahler-gap completion follows.

<a id="argument"></a>
## Complete argument

<a id="actual-circle-evaluation-leakage"></a>
### 2. Exact circle evaluations control leakage from the factor subspace

The q distinct circle roots of the original irreducible P make the first q columns of V an invertible Vandermonde matrix.
Hence V has full row rank and its kernel has dimension N-q=3.
A coefficient vector is in that kernel precisely when its polynomial vanishes at every circle root, equivalently is a multiple of C of degree at most d.
Thus ker V=range M after complexification.
Since C is real and the root list is closed under conjugation, its orthogonal projection Pi is a REAL symmetric matrix.
M has full column rank, and M M^dagger=Pi.

Let B=Q+R.
The constant Fourier coefficient in the exact symbol is trace Q=H0; therefore trace B=T.
For PSD matrices, B^2<=T B and R^2<=r R.
At a circle root zeta, put v=v_d(zeta) and b_zeta=v^*Rv.
The exact symbol gives v^*Bv=b_zeta, whence

    ||Qv|| <= ||Bv||+||Rv||
             <=(sqrt(T)+sqrt(r))sqrt(b_zeta).    (15)

This is C110's elementary root residual mechanism with the actual correction symbol retained instead of replacing it by an isotropic norm.
The columns of V^* are conjugate evaluation vectors.
The circle root list is closed under conjugation, and Q,R are real, so summing their squared estimates gives

    ||Q V^*||_F <=(sqrt(T)+sqrt(r))sqrt(S).

Using I-Pi=V^*(VV^*)^-1V and ||(VV^*)^-1V||=1/s yields

    ||Q(I-Pi)|| <=(sqrt(T)+sqrt(r))sqrt(S)/s.

Symmetry gives the same norm for (I-Pi)Q.
The identity Q-Pi Q Pi=Q(I-Pi)+(I-Pi)Q Pi then proves

    Q0:=Pi Q Pi,  ||Q-Q0||<=tau.                (16)

No estimate has replaced a vanishing symbol by PSD of Q.
Only B and R are PSD.
Because Q>=-R>=-rI, the exact quotient

    H=M^dagger Q0(M^dagger)^T,
    Q0=M H M^T

satisfies H>=-r kappa^2 I.
It need not be PSD.
Also ||Q||<=T: for unit vectors its quadratic value lies between -r and T, and r<=trace R<=T.

<a id="paid-three-lag-affine-recovery"></a>
### 3. Repairing the residual quadratic symbol at an explicit cost

For a real symmetric coefficient matrix X, write lag_k(X)=sum_i X_(i,i+k).
If ||X||<=tau, its highest three lag sums at width d have absolute values at most tau,2tau,3tau.
Let l2=H02, l1=H01+H12 and l0=trace H.
The top three coefficients of |C|^2 are 1,alpha,beta, because C is reciprocal with c0=cq=1:

    coefficient at lag q:       1,
    coefficient at lag q-1:     2c1=alpha,
    coefficient at lag q-2:     2c2+c1^2=beta.

This also holds at q=2, when the third coefficient is the constant coefficient of |C|^2.
Multiplication of Laurent symbols therefore gives

    lag_d(Q0)=l2,
    lag_(d-1)(Q0)=l1+alpha l2,
    lag_(d-2)(Q0)=l0+alpha l1+beta l2.           (17)

The desired residual symbol |1-tz+z^2|^2 has lag values (1,-2t,t^2+2).
Write e2,e1,e0 for the difference between these desired values and (l2,l1,l0).
Since the original Q has the exact symbol, (16)--(17) imply successively

    |e2|<=tau,
    |e1|<=K1 tau,
    |e0|<=K0 tau.                               (18)

The last bound pays 3tau+|alpha|K1 tau+|beta|tau, exactly K0 in(1).
Define the real symmetric 3-by-3 matrix E0 by putting e0 in entry00, e1 in entries01,10, e2 in entries02,20, and zero elsewhere.
Then

    ||E0||<=|e0|+2|e1|+2|e2|<=K tau.

Consequently Hbar=H+E0 has EXACTLY the desired residual symbol and

    Hbar>=-e I,  e=r kappa^2+K tau,
    |Hbar00-Q00|<=A tau.                        (19)

The second assertion uses Q0_00=H00, because the first row of M is(1,0,0).
This is a paid affine repair of an indefinite residual matrix, not a claim of a nearby PSD point.
No compactness theorem or unspecified inverse constant is used.

The full exact quadratic affine fiber, as in C117, is

    Hbar=r0 r0^T+D(a,b,c), r0=(1,-t,1)^T,
    D(a,b,c)=[[a,b,0],[b,c,-b],[0,-b,-a-c]],
    a=Hbar00-1 >=gamma-A tau.                   (20)

The correction-size scalar r from(3) does not enter the outer product r0 r0^T.
The residual symbol has lag1 equal to -2t, as required.

<a id="noncentral-correction-tradeoff-proof"></a>
### 4. Noncentral zero coordinate and the real precision floor

At a noncentral original zero j, C117 proves r0^T ell_j=0 and Delta_j!=0.
Its purely linear adjugate identity therefore applies to Hbar whether or not Hbar is PSD:

    a=(u_j dot Hbar ell_j)/Delta_j.             (21)

Since Q0 e_j=M H ell_j, applying M^dagger gives

    ||H ell_j||<=kappa ||Q0 e_j||
                 <=kappa(||Qe_j||+tau).

Combine this, (19)--(21) and ||E0||<=Ktau to get

    gamma<=A tau+|a|
      <=U_j kappa ||Qe_j||
          +[A+U_j(kappa+K||ell_j||)]tau,

which proves(5).
If Qjj<=delta, PSD of B and R gives

    ||Qe_j||<=sqrt(T Bjj)+sqrt(r Rjj)
              <=sqrt(T(delta+r_j))+sqrt(r r_j). (22)

All square-root arguments are nonnegative; Bjj>=0 and delta+r_j>=Bjj.
Substitution proves(6), and delta0 gives(7).
If Qe_j=0, (5) and(3) directly give(8).

For the objective-free qualitative assertion, S=0 implies tau0, so Q=Q0 lies exactly in the circle-factor subspace.
Its quotient H already has the exact quadratic symbol; if also Qe_j=0, then H ell_j=0.
The full invertible three-by-three system of C117 forces a=b=c=0, hence Q=pp^T.
This argument needs neither PSD of Q nor a specified positive objective.
Likewise if Qjj=Rjj=0, PSD of B and R forces Be_j=Re_j=0 and hence Qe_j=0.
It gives the diagonal/correction version stated in the initial mechanism.

For B take R=epsilon I.
Then r=epsilon, trace R=N epsilon, r_j=epsilon and S=qN epsilon.
If epsilon<=1/N, then T<=H0+1 and sqrt(epsilon)<=1, so(7) gives

    gamma <= (sqrt(H0+1)+1)sqrt(epsilon)
                  [U_j kappa+2L_j sqrt(qN)/s]
            =D_j sqrt(epsilon).

This includes epsilon0, which would contradict gamma>0.
If epsilon>1/N, the first branch of(10) already applies.
The two cases prove(10).
For Qe_j=0 use(5) directly, removing the U_j kappa term and giving D_j^row.
No q-denominator or integrality of Q has appeared; q throughout this draft is the number d-2 of circle roots.

<a id="central-correction-stability-proof"></a>
### 5. The center requires a separate quadratic inequality

Assume p_h=0.
C117 gives ell_h=(x,y,x), 2x=ty, D=x^2-y^2>0 and r0^T ell_h=0.
Direct substitution in(20) gives

    ell_h^T Hbar ell_h=-c D.

On the other hand (16),(18) imply

    ell_h^T Hbar ell_h
       <=Qhh+tau+K tau||ell_h||^2
       <=delta+J_h tau.                         (23)

The 0,2 principal minor of Hbar+e I is nonnegative by(19).
Its off-diagonal entry is1, so

    (1+a+e)(1-a-c+e)-1>=0,
    a^2<=e(2+e)-c(1+a+e).                      (24)

The factor 1+a+e=Hbar00+e is nonnegative.
It is at most T+A tau+e=F by(19) and ||Q||<=T.
Use(23) to bound -c by (delta+J_h tau)/D, which is nonnegative.
This gives a^2<=e(2+e)+F(delta+J_h tau)/D.
Since a>=gamma-A tau, its left side is at least max(0,gamma-A tau)^2 whenever that maximum is positive, and otherwise the stated lower bound0 is automatic.
This proves(11).

For the scalar floor, if epsilon<=1/N, set x0=sqrt(epsilon)<=1.
The definitions give tau<=J x0, e<=E x0, and F<=F0.
With delta0, (11) therefore gives

    max(0,gamma-AJ x0)^2<=G x0.                 (25)

If AJ x0>=gamma/2, then epsilon>=gamma^2/(4A^2J^2).
Otherwise the left side in(25) is greater than gamma^2/4, forcing epsilon>=gamma^4/(16G^2).
Including epsilon>1/N proves(12).
Every displayed constant is positive and finite.
The extra square-root loss comes from the projected affine correction, and no assertion of an optimal central exponent is made.

<a id="original-spectral-and-arithmetic-prices"></a>
### 6. Explicit original spectral, degree, height and field prices

The preceding formulas are already explicit in the ACTUAL s and kappa, not in an unspecified compactness modulus.
They can be bounded without treating either spectral parameter as uniform.
Let eta be the smallest distance between two distinct circle roots.
The Vandermonde minor V0 in the first q columns gives

    s>=sigma_min(V0)
      >=|det V0|/||V0||^(q-1)
      >=eta^(q(q-1)/2)/q^(q-1).                 (26)

Here ||V0||<=||V0||_F=q, and the product of its q singular values is |det V0|.
Thus the precise original circle-root separation is paid.
If a specified bound M(P)=lambda<=B is available, all d original roots have modulus at most B.
The COMPLETE original discriminant satisfies

    1<=sqrt(|disc P|)
       =product_(i<j)|alpha_i-alpha_j|
       <=eta (2B)^(d(d-1)/2-1).

Consequently one may use the conservative

    eta0=(2B)^(-(d(d-1)/2-1)),
    s0=eta0^(q(q-1)/2)/q^(q-1)<=s.             (27)

The discriminant uses every original root, including the two off-circle roots.
No selected-root product has been assigned an integer meaning.

The first three rows of M form the triangular matrix

    [[1,0,0],[c1,1,0],[c2,c1,1]],

with inverse [[1,0,0],[-c1,1,0],[c1^2-c2,-c1,1]].
This supplies a left inverse of M of norm at most

    kappa0=sqrt(3+2c1^2+(c1^2-c2)^2),

so kappa<=kappa0.
Indeed any left inverse has norm at least 1/sigma_min(M)=kappa.
There is no hidden conditioning assumption on multiplication by C.

For a bound purely in original integer coefficient size and a supplied B, reuse C117's already proved full-field estimates.
Put H1=sum|p_j|, L=hH1, L_B=L B^(h-1).
They give

    |c_k|<=L_B, ||ell_j||<=sqrt(3)L_B,
    U_j<=sqrt(11)L_B^2(4L^3)^(h-1)  (j!=h,p_j=0),
    D^-1<=4(4L^2)^(h-1)             (p_h=0).    (28)

The latter two estimates pay ALL h-1 other trace embeddings through the nonzero full field norms, as retained in C117.
In particular

    kappa<=sqrt(3+2L_B^2+(L_B^2+L_B)^2),
    K0<=3+6L_B+5L_B^2,
    K<=9+10L_B+5L_B^2,
    A<=4+6L_B+5L_B^2.                          (29)

Substituting(27)--(29) into the positive expressions(9),(12) supplies explicit, though large, bounds in d,H1,H0,B alone.
Every substitution enlarges the positive denominator constants and is therefore in the safe direction for the lower tolerance floors.
These constants retain original degree d=2h and the full trace-field degree h.
For arbitrary real Q,R no arithmetic denominator is presumed or bounded.
The rank-one construction below is over the actual trace field; requiring rational coefficients would be an additional problem, not a free descent.

<a id="rank-one-repair-and-central-countercontrol"></a>
### 7. Exact rank-one repair and the central exception

C is reciprocal of even degree d-2.
Therefore W=C(1-z^2) is anti-reciprocal of degree d, with coefficients w_j=c_j-c_(j-2), w0=1 and wd=-1.
On the unit circle, z^-h P(z) is real and z^-h W(z) is purely imaginary: write z^-(h-1)C(z), which is real, and multiply by z^-1-t+z or z^-1-z, respectively.
Hence Re(conjugate(P)W)=0.
This proves the exact same-symbol identity for Q_a, while expansion of the coefficient outer product proves Q_a+R_a=(p+(a/2)w)(p+(a/2)w)^T.
The root evaluations of W vanish at every circle root, so S=0.
The objective of Q_a is1+a, all its original zero diagonal entries are zero, and(13) follows from the norm of a rank-one PSD matrix.

Reciprocity of p and anti-reciprocity of w give p dot w=0, by pairing indices j,d-j; the central w_h is0.
Both vectors are nonzero, so on their orthonormal coefficient basis Q_a has matrix

    [[H0,(a/2)sqrt(H0 W0)],
     [(a/2)sqrt(H0 W0),0]].

Its determinant is -a^2 H0 W0/4<0.
This proves its exact inertia and the negative eigenvalue formula(14).
Rationalization gives

    epsilon_a=a^2 H0 W0/
       [2(sqrt(H0^2+a^2 H0 W0)+H0)],

and hence the stated fixed-input small-a equivalent.
C117 proves w_j!=0 at EVERY noncentral interior index; thus the correction activates every noncentral original zero.
However an indefinite Q_a with a zero diagonal at such j does NOT have zero row: Q_a e_j=(a/2)w_j p!=0.
It is therefore not a counterexample to the stronger whole-row bound(8).

At a central original zero, both p_h and w_h vanish, so Q_a e_h=R_a e_h=0.
This central phenomenon is nonvacuous.
As a bounded exact domain control, P=z^4-2z^3-2z+1 has trace polynomial X^2-2X-2, whose roots1+sqrt3>2 and1-sqrt3 in(-2,2) give exactly one real reciprocal outside/inside pair and one circle pair.
The shifted polynomial P(z+1)=z^4+2z^3-4z-2 is Eisenstein at2, so the original degree is4 and P is irreducible Salem; its central coefficient is0.
The general formulas above therefore give an actual central missing-row example.
This fixed control is included solely to verify the exception, not as the main result, a near-one family or a new low-measure construction.

<a id="stability-outcome-and-unresolved-gain"></a>
## 8. What changed and what remains unresolved

The new real stability result does not claim that a small negative eigenvalue implies exact PSD, and it does not transfer C110's rational resultant floor to arbitrary reals.
It gives an explicit original-input floor when a positive objective is combined with a missing original zero diagonal, and a stronger exact obstruction when an entire noncentral original-zero row is removed.
Correction symbol mass at the ACTUAL circle roots, rather than rank alone or an unpriced generic norm, is the measurable expense in(8).
C113's sufficient corrected Mahler inequality can use a justified correction independently; this draft supplies necessary structural prices for candidates.

The constants can deteriorate substantially with root separation, degree and height.
Section6 makes that dependence explicit rather than claiming input-uniform face stability.
If no original zero coefficient exists, no coordinate obstruction is supplied here.
Central and noncentral positions, diagonals and rows, raw objective and corrected determinant, original width and padding are all distinct hypotheses.
The rank-one pair shows why neither a low-rank repair nor a center-only support constraint by itself yields a gap.

No construction with a degree-independent positive gamma and a uniformly affordable corrected-symbol error is obtained.
The exact rank-one control has trace-field coefficients and pays its displayed original norm; its gain cannot be counted before the correction error is subtracted.
The unrestricted G0001 objective and actual near-one coverage remain open.
Root provided the question and progress reading only; all new derivations and the bounds here are by this author.
No native mathematical program, solver certification, independent review or global decision is asserted.

<a id="salem-real-stability-entire-author-freeze"></a>
## 9. Complete author check and freeze

2026-10-14T21:17.
The author freezes the ENTIRE actual account: original question and incremental first mechanism, exact reuse/contribution boundaries, Statement A--D, the complete argument Sections2--7, all29 numbered formulas and all outcome limitations.
The final reread checked complex evaluation/conjugation conventions and the real projector; both PSD matrices versus the possibly indefinite Q; the exact q-by-N rank and 1/s norm; two-sided leakage; every top-three-lag count including q2; the full affine repair and its remaining negative tolerance; C117's adjugate without a PSD premise; diagonal versus entire-row distinctions; epsilon0, epsilon=1/N and both scalar-floor branches; the central principal minor and signs when its quadratic value is negative; the full original discriminant and monotonic direction of every height/spectral substitution; the rank-one exact symbol, coefficient orthogonality, actual inertia and eigenvalue; and the nonvacuous central Eisenstein control.
The preliminary shorthand calling an indefinite matrix part of a PSD face was corrected to the coefficient-multiplication subspace before freeze; no formula or proved conclusion used that shorthand.
An unambiguous r0 r0^T notation replaced an initial typographic shorthand.
No remaining gap was found in this author check at the stated domain.
The structural material check passed; it is not mathematical review.
No native mathematical program was run, no independent-review claim is made, and root supplied no proof step.
The complete artifact is ready for separate actual fixed whole review.

## Fixed organization

The entire final author original is retained: the incremental mechanism, exact reuse and relationship account, Statement A--D, complete projection/affine-repair/coordinate proof, all explicit original-input parameters, rank-one and central controls, author-check history and unresolved gain.
Root supplied direction only and no proof step; a separate whole review of this actual fixed artifact is pending.

## Current assessment
[Selected decision](#decision-current-haar-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:19 |
| status | open |
| reason | Retain the complete real same-symbol correction tradeoffs and denominator-free almost-PSD bounds for whole independent review. Original degree, height, spectral and embedding prices remain explicit; there is no uniform gain or unrestricted Mahler-gap conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact real stability statement](#statement) | Full A--D, all original Salem/width/real/symbol/coordinate hypotheses, denominator-free floors, paid constants and exact rank-one exception. |
| argument | [Entire stability proof](#argument) | Complete Sections 2--7 and all 29 formulas, leakage, affine recovery, noncentral and central distinctions, spectral/arithmetic costs and actual control. |
| dependency | [Actual Salem coordinate identities](Yin_C_G0117_v1.md#statement) | Entire required original trace-field/coefficient identities, noncentral adjugate, central sign and all-field height bounds from the adopted input, whose selected R349 finding is self-reviewed. |
| dependency | [Actual Salem argument](Yin_C_G0117_v1.md#argument) | Exact derivations and every nonzero coefficient, determinant and full norm denominator used here. |
| support | [Prior real regularization](Yin_C_G0110_v2.md#statement) | Existing PSD root-residual mechanism; no rational denominator floor imported to the present real matrices. |
| support | [Localized correction](Yin_C_G0113_v1.md#localized-gram-correction) | Prior sufficient corrected-symbol Mahler inequality, distinguished from the new necessary correction costs. |
| support | [Prior fixed-input degeneration](../ledger/Yin_L_F0006_v1.md#coefficient-optimizer-degeneration) | Bounded reuse comparison; no unpriced stability or compactness theorem imported. |

### Decision whole-reviewed-2026-10-15

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:22 |
| status | proved |
| reason | Adopt complete noncontributor R350 review of the actual real same-symbol stability statement, all 29 formulas and direct inputs. Original-input correction costs and the noncentral whole-row obstruction are proved with the center treated separately. No uniform positive primal gain or unrestricted gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact real stability statement](#statement) | Full A--D, all original Salem/width/real/symbol/coordinate hypotheses, denominator-free floors, paid constants and exact rank-one exception. |
| argument | [Entire stability proof](#argument) | Complete Sections 2--7 and all 29 formulas, leakage, affine recovery, noncentral and central distinctions, spectral/arithmetic costs and actual control. |
| dependency | [Actual Salem coordinate identities](Yin_C_G0117_v1.md#statement) | Entire required original trace-field/coefficient identities, noncentral adjugate, central sign and all-field height bounds from the independently adopted input. |
| dependency | [Actual Salem argument](Yin_C_G0117_v1.md#argument) | Exact derivations and every nonzero coefficient, determinant and full norm denominator used here. |
| support | [Prior real regularization](Yin_C_G0110_v2.md#statement) | Existing PSD root-residual mechanism; no rational denominator floor imported to the present real matrices. |
| support | [Localized correction](Yin_C_G0113_v1.md#localized-gram-correction) | Prior sufficient corrected-symbol Mahler inequality, distinguished from the new necessary correction costs. |
| support | [Prior fixed-input degeneration](../ledger/Yin_L_F0006_v1.md#coefficient-optimizer-degeneration) | Bounded reuse comparison; no unpriced stability or compactness theorem imported. |
| review | [Complete actual independent finding](../audits/reviews/Yin_R_G0350_v1.md#real-salem-stability-whole-independent-finding) | Entire actual retained statement, proof and direct inputs, all hypotheses, quantitative costs, controls, contribution and source limits. |

### Decision current-haar-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:44 |
| status | proved |
| reason | Select the adopted complete C_F6/C_F7/C_F8 responsible homes, as applicable below, for the unchanged retained fixed-input coefficient degeneration comparison. The actual selected adoptions and complete needed interface sections were read and matched to the original fixed L_F5/L_F6/L_F7 text. Mathematical status, statement, full argument, selected findings and every relation scope remain unchanged; this is current proof-location maintenance with no new mathematical or independent review. Original dated decisions and all R bindings keep their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact real stability statement](#statement) | Full A--D, all original Salem/width/real/symbol/coordinate hypotheses, denominator-free floors, paid constants and exact rank-one exception. |
| argument | [Entire stability proof](#argument) | Complete Sections 2--7 and all 29 formulas, leakage, affine recovery, noncentral and central distinctions, spectral/arithmetic costs and actual control. |
| dependency | [Actual Salem coordinate identities](Yin_C_G0117_v1.md#statement) | Entire required original trace-field/coefficient identities, noncentral adjugate, central sign and all-field height bounds from the independently adopted input. |
| dependency | [Actual Salem argument](Yin_C_G0117_v1.md#argument) | Exact derivations and every nonzero coefficient, determinant and full norm denominator used here. |
| support | [Prior real regularization](Yin_C_G0110_v2.md#statement) | Existing PSD root-residual mechanism; no rational denominator floor imported to the present real matrices. |
| support | [Localized correction](Yin_C_G0113_v1.md#localized-gram-correction) | Prior sufficient corrected-symbol Mahler inequality, distinguished from the new necessary correction costs. |
| support | [Prior fixed-input degeneration](Yin_C_F0007_v1.md#coefficient-optimizer-degeneration) | Bounded reuse comparison; no unpriced stability or compactness theorem imported. |
| review | [Complete actual finding](../audits/reviews/Yin_R_G0350_v1.md#real-salem-stability-whole-independent-finding) | Entire actual retained statement, proof and direct inputs, all hypotheses, quantitative costs, controls, contribution and source limits. |
