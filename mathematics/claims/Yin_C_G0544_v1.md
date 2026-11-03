---
author: Yin
---

# Integral factor-retaining vertex couplings and complete absolute-cover costs

The one-vertex restriction and all-core quartic gate, followed by the classified two-vertex exception and arbitrary-rank pairing, share the actual integral-extension object with distinct quantifiers and operation classes.
Original full author inputs, declarations, checks and review acts remain fixed in [L287](../ledger/Yin_L_G0287_v1.md) and [L291](../ledger/Yin_L_G0291_v1.md); current mathematical proof responsibility is this C.

<a id="statement"></a>
## Complete statement

A proper matrix below is an actual integral upper-unitriangular matrix with diagonal one.
Put p_U(t)=det(tU+U^T), s=t+1, Q_v=t^2+(2-v)t+1 and E(U)=sum_(i<j)U_ij^2.
U^- has negative absolute strict-upper entries; the literal proper cover has full polynomial p_U p_(U^-), twice the rank and twice the strict-upper energy.
Absolute costs are not invariant under arbitrary integral bilinear congruence.

**One appended vertex.**
Let B be integral r-by-g of full column rank, r>=g+1, A=B^T B and P_A=t^g det((s^2/t)I-A).
Assume EVERY irreducible factor of the Q-minimal polynomial of A has a root in the OPEN interval(0,4), with repeated characteristic factors allowed.
For EVERY x in Z^r,y in Z^g and Z=[[I_r,-B,x],[0,I_g,y],[0,0,1]], full-multiplicity divisibility P_A|p_Z holds exactly when y=0 and B^T x=0.
Then N=||x||^2, p_Z=s^(r-g-1)P_A Q_N and the full companion is s^(r-g-1)t^(g+1)det((s^2/t)I-|[B,-x]|^T|[B,-x]|).
Rank is r+g+1, height max(1,max|B_ij|,max|x_i|), energy tr A+N and cover energy twice that.
The complete original/absolute measures are the spectral sums f(lambda), f=0 on[0,4], f(lambda)=arcosh((lambda-2)/2) above4, with multiplicities.
Under an actual integral core congruence, the criterion becomes c=Uw for w in ker_Z(U-U^T), with N=w^T Uw, and explicit cyclic reconstruction covers every insertion position.
It does not cover arbitrary unrelated core permutations or all forms with the same scalar polynomial.

For B with rows(1,1),(0,1),(0,1),(0,1), put P4=t^4-t^3-t^2-t+1 and let beta4>1 be its real expanding root.
All preserving columns have y=0,x=(0,a,b,-a-b), N=2(a^2+ab+b^2), a,b arbitrary integers.
The complete polynomial is Phi2 P4 Q_N, and only N=0 or2 give neutral Q_N; N=2 has precisely six solutions and gives Phi2 Phi4 P4.
Phi2 Phi6 P4 would require N=3 and is excluded throughout this congruence/insertion class.
For L=|a|+|b|+|a+b| and C_(N,L)=[[1,1,0],[1,4,L],[0,L,N]], H_(N,L)=t^3 det((s^2/t)I-C_(N,L)), the complete original/absolute/cover polynomials are Phi2 P4 Q_N, Phi2 H_(N,L), Phi2^2 P4 Q_N H_(N,L).
Their ranks are7/7/14, height max(1,|a|,|b|,|a+b|), energies5+N,5+N,10+2N and full spectral measures as above.
The six N=2 controls have complete cover measure greater than2log beta4.
A lambda=4 nonkernel boundary control has original measure zero and companion measure log(3+2sqrt2), so the OPEN-window condition cannot be discarded.

For EVERY proper rank6 U with p_U=Phi2^2 P4, irrespective of core congruence, any c in Z^6 preserves P4 exactly when c=Uw for w in its actual primitive alternating kernel.
Then p_Z=Phi2 P4 Q_N, N=w^T Uw; this rank-two restricted kernel has determinant3.
A full Phi2 Phi6 P4 extension exists exactly when this kernel represents3, equivalently1, equivalently U splits an integral orthogonal[1] block under bilinear congruence.
Neither a proper upper-unitriangular complement nor the existence of such a proper core is supplied.
For actual U,c, the full companion is (t+1)p_(U^-)-t|c|^T adj(tU^-+(U^-)^T)|c|, rank7/cover14, height max(height U,max|c_i|) and energy E(U)+||c||^2, doubled for the cover.
An arbitrary rank7 presentation need not have the required principal core; no universal rank7 exclusion follows.

**Two vertices and arbitrary simultaneous neutral pairs.**
For EVERY proper rank-n U, c in Z^n and a,b,k in Z, let Z=[[U,ac,bc],[0,1,k],[0,0,1]], delta=a^2+b^2-kab and M=tU+U^T.
Then p_Z=p_U Q_(k^2)-ts delta c^T adj(M)c.
For(a,b)!=(0,0), this coupling term vanishes for EVERY U,c exactly when |a|=|b|>0 and k=2sign(ab); the zero pair is separately disconnected.
Individual isotropic cancellations for a particular U,c are not excluded.
At the Gram cores satisfying the OPEN-window hypothesis and delta!=0, P_A retention again requires c=(x,0), B^T x=0, giving p_Z=s^(r-g)P_A Q_(k^2+delta||x||^2).
The complete companion uses |c| and delta_-=a^2+b^2+|kab| in the same adjugate formula.
Negative effective Q-parameters remain included.
Ranks are n+2/cover2n+4, height max(1,|U_ij|,|a c_i|,|b c_i|,|k|), energy E(U)+(a^2+b^2)||c||^2+k^2 and twice that for the cover.

For EVERY integral n-by-k C, k>=1, Z_C=[[U,C,C],[0,I_k,2I_k],[0,0,I_k]] satisfies p_(Z_C)=(t-1)^(2k)p_U without a rank restriction on C.
With D=|C| and M_-=tU^-+(U^-)^T, its full companion is

    A_C=(t-1)^(2k) det(M_- -4ts DD^T/(t-1)^2),
    p_cover=(t-1)^(2k)p_U A_C.

The rational display is the actual monic integral determinant; no cover factor is canceled.
Original/absolute rank is n+2k, cover2n+4k, height max(2,|U_ij|,|C_ij|), energy E(U)+2||C||_F^2+4k and doubled cover energy.
For r=rank_Q D, (t-1)^(2k-2r)|A_C and the remaining degree is at most n+2r<=3n, including C=0.
Fixed-core padding changes no original noncyclotomic factor and creates no unbounded companion irreducible degree.

Here e_j is the j-th of the four left standard coordinates of the displayed canonical quartic core.
For that core with every column C=m e_2, k>=1,m!=0,L=km^2, the full polynomials are s^2 P4(t-1)^(2k), s^2(t-1)^(2k-2)H_L and their product, with H_L=t^3[v^3-(4L+3)v^2-v+8L+6], v=t+t^-1.
Its trace roots lie in(-2,-1),(1,2),(4L+2,4L+3), with one expanding pair and log(4L+1)<log alpha_L<log(4L+3).
Original measure stays log beta4 while the companion expense diverges; rank6+2k, height max(2,|m|), energy5+2L+4k and full cover expense remain.
For L=1 modulo3 the sextic is irreducible, of fixed degree6.
The separate nonbipartite rank8 Phi6 control has full original s^2 P4 Phi6, one companion pair greater than beta4, height1 and energies10/10/20.
The independent C=[e_1,e_2],k=2 control has companion s^2 H8 with H8=t^4[v^4-13v^3+33v^2+64v-44] irreducible of degree8, TWO expanding pairs of product greater than30, ranks10/10/20, height2 and energies17/17/34.
All exact additional factors and root costs in the argument remain part of the theorem.
Original J69/J72 controls corroborate the written all-integer proofs only at their declared finite domains.
No new execution, unrestricted gap, realization optimum or unbounded original irreducible complexity is asserted.

## Complete argument

<a id="argument"></a>

### Part I. One vertex and every proper quartic core

Inputs are [C458v2 Gram identities](Yin_C_G0458_v2.md#statement), [C521 full kernel identities](Yin_C_G0521_v1.md#statement), [C429 cyclic reconstruction](Yin_C_G0429_v1.md#ordering-exact-reduction), [C520v2 bipartite comparison](Yin_C_G0520_v2.md#statement) and [C2 literal cover](Yin_C_G0002_v1.md#signed-cover-identity).
McM02/Hir06 were screened only at their retained scopes; no classification/plumbing/tree-order theorem is used.
The direct block/spectral proof uses no new source intake or novelty claim.
Equations1--24 in Part I and1--15 in Part II keep their local numbering.

<a id="factor-retaining-one-vertex-rigidity"></a>
### 2. A general factor-retention criterion for all integer couplings

Let B be an integral r-by-g matrix of full column rank, with r>=g+1, and set

    U_B=[[I_r,-B],[0,I_g]], A=B^T B,
    s=t+1, u=s^2/t=t+t^(-1)+2,
    P_A(t)=t^g det(u I_g-A), p_(U_B)=s^(r-g) P_A.       (1)

Assume that EVERY irreducible factor over Q of the minimal polynomial of A has at least one root in the OPEN interval(0,4).
Multiplicities in the characteristic polynomial are permitted; A is real symmetric positive definite and its minimal polynomial has distinct roots.
This hypothesis is checked on the actual A, not on a chosen dominant eigenvalue alone.

For arbitrary integer x in Z^r and y in Z^g form the actual upper-unitriangular extension

    Z(x,y)=[[I_r,-B,x],[0,I_g,y],[0,0,1]].              (2)

**Theorem.**
The following are equivalent:

    P_A divides p_(Z(x,y)) in Z[t];
    y=0 and B^T x=0.                                  (3)

When they hold, put N=x^T x.
The COMPLETE polynomial is

    p_Z=s^(r-g-1) P_A Q_N,
    Q_N=t^2+(2-N)t+1.                                 (4)

No bound on x,y, entry height or energy is imposed.
Divisibility means retaining P_A with its full multiplicities.
The conclusion is stronger than an unchanged Mahler measure or retained single eigenvalue.

The generic theorem also retains every absolute and proper-cover expense.
In the canonical coordinates satisfying(3), put B_plus=[B,-x], C_abs=|B_plus|^T|B_plus| and k=r-g-1.
Then

    p_absolute=Phi2^k t^(g+1) det((t+t^(-1)+2)I-C_abs),
    p_proper_cover=Phi2^(2k) P_A Q_N
                         t^(g+1) det((t+t^(-1)+2)I-C_abs). (4a)

Original/absolute rank is r+g+1, proper-cover rank twice that, height max(1,max|B_ij|,max|x_i|), original/absolute energy tr A+N and cover energy twice that.
The full original measure is sum_(lambda in spec A) f(lambda)+f(N), the full companion measure is sum_(mu in spec C_abs) f(mu), and the cover is their sum, with the exact L191 spectral function f stated below(16).
These are actual Gram spectra with multiplicity; zero eigenvalues and all Phi2 factors are retained in the polynomials.
Costs under a different integral congruence must be recomputed from that actual matrix, as(23) does, not transported as invariants.

**Proof.**
Write v=B^T x and M=t U_B+U_B^T.
The one-row block determinant gives

    p_Z=p_(U_B)[s-t R(t)], R(t)=(x,y)^T M^(-1)(x,y).    (5)

This is initially over Q(t), then a polynomial identity after multiplication.
Invert the two core blocks with D=s^2 I_g-t A.
Direct substitution yields

    s R(t)=||x||^2+v^T(uI-A)^(-1)v
                    +u v^T(uI-A)^(-1)y
                    +u y^T(uI-A)^(-1)y.               (6)

In particular the coefficient of the cross term is u, not 2u: the two unequal off-diagonal inverse blocks contain factors t and 1, whose sum is s.

For each distinct eigenvalue lambda of A let E_lambda be its orthogonal spectral projection.
The residue at u=lambda of the rational expression in(6) is

    ||E_lambda v||^2+lambda (E_lambda v).(E_lambda y)
                         +lambda ||E_lambda y||^2.     (7)

If 0<lambda<4, this equals

    ||E_lambda v+(lambda/2)E_lambda y||^2
           +lambda(1-lambda/4)||E_lambda y||^2,

so it vanishes only when both projections vanish.

Suppose P_A divides p_Z.
From(1),(5), s-t R=p_Z/p_(U_B) can have finite poles only at t=-1.
For an eigenvalue lambda in(0,4), the two solutions of u(t)=lambda are nonzero, different from -1, and simple for the u map: du/dt=1-t^(-2) is nonzero there, since lambda is neither0 nor4.
Thus a nonzero residue(7) would produce a forbidden pole of R, and(7) must vanish.
This argument remains valid for repeated eigenvalues, because the resolvent has only simple poles and full divisibility retains their entire characteristic multiplicities.

The projection E_lambda is a matrix with entries in Q(lambda).
For example if m is the squarefree minimal polynomial, then

    E_lambda=[m(A)/(A-lambda I)]/m'(lambda),            (8)

where the bracket means evaluate the polynomial m(z)/(z-lambda) at A, not divide zero matrices.
Any field embedding sending lambda to another root mu of the same irreducible factor sends E_lambda to E_mu; A,v,y are rational.
Hence E_lambda v=E_lambda y=0 propagates to every conjugate root.
By the hypothesis this covers every eigenvalue, and summing all projections gives v=y=0.
Conversely, if v=y=0, (6) gives R=N/s and(5) gives exactly(4).
Since P_A is monic, rational divisibility of integer polynomials here is also integral divisibility.
This proves the theorem.

The criterion transports through arbitrary integral bilinear congruence, not only through a finite mutation sequence.
Let U=Q^T U_B Q be proper upper-unitriangular with Q in GL_(r+g)(Z), and append any integer column c.
Applying diag(Q,1) to a core extension shows that(3) is equivalent to

    c=U w for some w in K(U)=ker_Z(U-U^T),
    N=w^T U w,                                        (9)

with the same full polynomial(4).
Indeed K(U_B) consists exactly of(x,0) with B^T x=0, and U_B fixes those vectors; transport uses w=Q^(-1)(x,0) and c=Q^T(x,0)=U w.
Conversely Q is integral unimodular, so every transported vector is an actual integer column.
No absolute-companion invariance under this congruence is claimed.

The no-target consequence also covers inserting the new vertex anywhere in the ordered core, with arbitrary integer connections on each side.
Here is the needed integral cyclic identity.
For any proper upper-unitriangular V=[[1,a],[0,W]], take basis columns e_j-a_j e_1 for j>1, followed by -e_1.
Their determinant is+1 or-1, and the exact new Gram is

    [[W,a^T],[0,1]].                                   (10)

This is the cyclic reconstruction of the same symmetric entries.
Repeatedly apply(10) to the WHOLE extension until the added vertex is last.
The retained core is a cyclic reconstruction of the original U, which is itself integrally bilinearly congruent to U by the same formula.
Then(9) applies.
This statement covers all insertion positions, not arbitrary permutations of an unrelated core or every form with the same scalar polynomial.

<a id="quartic-core-complete-extension-classification"></a>
### 3. The actual quartic core and complete neutral replacements

Use the already achieved L191 matrix with

    B=[[1,1],[0,1],[0,1],[0,1]],
    A=[[1,1],[1,4]],
    P4=t^4-t^3-t^2-t+1,
    p_(U_B)=Phi2^2 P4.                                (11)

The minimal polynomial lambda^2-5lambda+3 is irreducible since its discriminant13 is not a rational square.
It has one root in(0,1) and another in(4,5), by endpoint signs.
Thus Section2 applies without a source theorem about arbitrary Salem inputs.
The complete integral kernel is

    y=0, x=(0,a,b,-a-b), a,b in Z,
    N=2(a^2+ab+b^2).                                  (12)

Consequently every factor-retaining extension of this core has exactly

    p_Z=Phi2 P4 Q_N, N=2(a^2+ab+b^2).                  (13)

This also holds as a necessary-and-sufficient append criterion for every proper core in its integral bilinear congruence class, and gives the same necessary scalar possibilities at every insertion position.
In particular Phi2 Phi6 P4 would require N=3 and is IMPOSSIBLE throughout this unbounded class.
This is not an exclusion of all non-bipartite rank7 forms with that polynomial; a candidate whose core is not in the stated congruence class remains open.

All roots of Q_N have modulus1 exactly when 0<=N<=4: its trace is N-2.
This is an elementary quadratic fact, including the repeated endpoints.
The even form in(12) rules out1 and3; also a^2+ab+b^2 is0 or1 modulo3, so N=4 is impossible.
N=0 forces a=b=0.
N=2 has exactly six solutions, namely (1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1).
To see completeness, 4(a^2+ab+b^2)=(2a+b)^2+3b^2=4 bounds |b|<=1 and determines a.
Therefore the only cyclotomic quadratic replacements in this ENTIRE extension class are Q_0=Phi2^2 and Q_2=Phi4.
No list of small couplings is substituted for this all-integer proof.

For the displayed canonical core, all factor-retaining extensions have y=0, so they regroup as a genuine bipartite matrix with r=4 and g=3, and new rectangular block [B,-x].
Put

    L=|a|+|b|+|a+b|,
    C_(N,L)=[[1,1,0],[1,4,L],[0,L,N]],
    chi_(N,L)(z)=(z-N)(z^2-5z+3)-L^2(z-1),
    H_(N,L)(t)=t^3 chi_(N,L)(t+t^(-1)+2).              (14)

The matrix C is exactly |[B,-x]|^T |[B,-x]| and hence positive semidefinite.
Original, absolute and proper-cover polynomials are, in FULL,

    Phi2 P4 Q_N,
    Phi2 H_(N,L),
    Phi2^2 P4 Q_N H_(N,L).                            (15)

The actual ranks are7,7,14; entry height is max(1,|a|,|b|,|a+b|); original/absolute strict-upper energy is5+N and cover energy10+2N.
The L191 spectral function f(z)=0 for0<=z<=4 and arcosh((z-2)/2) for z>4 gives exact complete costs

    m_original=log beta4+f(N),
    m_absolute=sum_(lambda in spec C_(N,L)) f(lambda),
    m_cover=m_original+m_absolute,                    (16)

with multiplicities.
None is replaced by energy, entry height or one selected eigenvalue.

The six N=2 solutions all have L=2.
They give an actual changed rank7 target Phi2 Phi4 P4, with original measure log beta4, height1, energy7 and proper-cover energy14.
Its full absolute factor is Phi2 H_(2,2), where

    H_(2,2)=t^3[(t+t^(-1))^3-(t+t^(-1))^2
                               -7(t+t^(-1))-4].        (17)

The cubic has three roots in(-2,-1),(-1,0),(3,4), since its values at-2,-1,0,3,4 are-2,1,-4,-7,16.
Thus H_(2,2) has exactly one expanding reciprocal pair with root alpha>(3+sqrt5)/2>2>beta4, and complete cover measure log beta4+log alpha>2log beta4.
This is a successful alternative neutral replacement, not the excluded Phi6 target or an improvement over L191's proper rank6 Phi2^2 P4 / rank12 Phi2^4 P4^2 double-cost control.
The zero solution simply adds an isolated vertex, giving Phi2^3 P4 and identical companion.
Equations(14)--(16) retain costs for all unbounded parameters, whose additional positive factor has degree at most2; no increasing positive irreducible complexity is created by retaining P4 this way.

<a id="open-spectral-window-boundary-control"></a>
### 4. Why the open spectral hypothesis matters

The theorem is sufficient, not claimed necessary for every matrix A.
Its OPEN interval cannot be replaced indiscriminately by the closed interval.
Take r=2,g=1, B=(2,0)^T, A=(4), and append x=(-1,0)^T,y=1.
Then v=B^T x=-2 is nonzero, but the residue at lambda=4 is(v+2y)^2=0 and(6) gives R=0.
The actual integer matrix and full costs are

    Z=[[1,0,-2,-1],[0,1,0,0],[0,0,1,1],[0,0,0,1]],
    p_Z=Phi2^2 (t-1)^2,
    p_(Z^-)=Phi2^2 (t^2-6t+1),
    p_cover=Phi2^4 (t-1)^2 (t^2-6t+1).                 (18)

Its original non-Phi2 factor is retained by a genuinely nonkernel coupling.
The original measure is0, the entire companion/cover measure is log(3+2sqrt2), ranks4/4/8, height2, original/absolute energy6 and cover energy12.
This exact boundary control prevents treating factor retention alone as a universal no-coupling theorem.
It is not a positive-small-measure counterexample.

<a id="all-core-quartic-factor-retention"></a>
### 6. A criterion for EVERY proper core with the same full quartic polynomial

There is a stronger analytic statement that does not require the core to be bipartite or congruent to(11).
Let U be ANY proper integral rank6 upper-unitriangular matrix with

    p_U=Phi2^2 P4,
    Z_c=[[U,c],[0,1]], c in Z^6.                       (19)

Then

    P4 divides p_(Z_c)
      if and only if c=U w with w in K(U),
    p_(Z_c)=Phi2 P4 Q_N, N=w^T U w.                   (20)

The real number N in the last formula is an integer and need not be nonnegative before examining its restricted lattice.
The complete kernel lattice is determined from the actual U, not assumed equal to the canonical kernel(12).

**Proof.**
The retained L191 quartic argument gives irreducibility of P4 over Q and a nonreal unit-circle root zeta, which is simple and different from+1,-1.
Write M(t)=tU+U^T.
By the same scalar block determinant as(5), P4 divides p_(Z_c) exactly when it divides c^T adj(M)c.
Choose theta with zeta=e^(i theta).
The matrix

    H=e^(-i theta/2) M(zeta)
      =e^(i theta/2)U+e^(-i theta/2)U^T

is Hermitian.
It has rank5: a lower rank would give determinant vanishing to order at least2 in this linear pencil, contradicting the simple root of p_U.
Its adjugate is therefore a nonzero REAL scalar times v v^* for a nonzero complex kernel vector v.
Since c is real, c^T adj(H)c=0 implies v^* c=0, and hence adj(H)c=0.
Multiplying by the scalar phase gives adj(M(zeta))c=0.
Every entry of adj(M(t))c is a rational polynomial.
Irreducibility of P4 therefore forces P4 to divide every such entry.
The vector M(t)^(-1)c can have finite poles only at t=-1.

The alternating matrix U^T-U has positive even kernel dimension, bounded above by the multiplicity2 of -1; hence its primitive integer kernel has rank2.
Read the full [C521 adapted-block coefficient identity](Yin_C_G0521_v1.md#minus-one-leading-coefficient-kernel): for an integral kernel basis with restricted symmetric matrix G and nonsingular alternating complement A0, the leading coefficient at -1 is Pf(A0)^2 det G.
Here this is P4(-1)=3, so

    Pf(A0)=+1 or -1, det G=3.                         (21)

In the adapted basis M(-1+s)=[[sG,sX],[sX^T,A0+sY]].
Since both G and A0 are invertible, its block inverse has at most a SIMPLE pole at s=0: the upper Schur block is s[G-sX(A0+sY)^(-1)X^T], with invertible bracket at0.
There is no assumption that root multiplicity always equals alternating nullity for arbitrary inputs; it is proved here for this full polynomial.

At infinity M(t)^(-1)c=(1/t)U^(-1)c+O(t^(-2)).
A rational vector with no finite pole except a simple pole at -1 and this decay equals w/(t+1), with w=U^(-1)c.
Because U is integral unimodular, w is integral.
Comparing M(t)w=(t+1)c gives Uw=U^T w=c, so w lies in K(U).
Conversely such w gives M(t)^(-1)c=w/(t+1), c^T w=w^T U w, and the full determinant(20).
This proves both directions for every actual core U in(19).

**Exact changed-core discriminator.**
A core U as in(19) admits an integer one-vertex extension with full Phi2 Phi6 P4 if and only if its primitive restricted kernel represents1, equivalently if U splits an integral orthogonal [1] block under bilinear congruence:

    there is c with p_(Z_c)=Phi2 Phi6 P4
      iff there is w in K(U) with w^T U w=3
      iff there is z in K(U) with z^T U z=1.           (22)

The last equivalence needs no binary-form classification theorem.
If z has norm1, the integral splitting functional on the rank2 kernel gives a basis with Gram diag(1,3), by(21), and its second vector has norm3.
Conversely, a norm3 vector w is primitive, since any nontrivial integral multiple would make a square greater than1 divide3.
Complete it to a kernel basis with Gram [[3,b],[b,c0]].
Its determinant3 gives 3c0-b^2=3, hence b=3k and c0=1+3k^2.
The second basis vector minus k w has norm1.
L214's exact norm-one splitting criterion now proves the stated ambient bilinear splitting equivalence.
The complementary rank5 integral form need NOT have a proper positive upper-unitriangular basis.
No such basis or existence of an eligible U is inferred from the splitting statement.

Thus the canonical even kernel(12), and every integral bilinear congruence of that core, is excluded; changing couplings or insertion positions cannot repair it.
A genuinely different core with polynomial(19) and a norm-one alternating-kernel vector would give the desired rank7 extension explicitly by c=Uw for the constructed norm3 vector.
This is a necessary-and-sufficient constructor criterion, not an assertion that such a proper core has been found.
An arbitrary rank7 target presentation need not have a principal deletion with polynomial(19), so it is also not a universal rank7 nonexistence theorem.
Formula(10) transfers the same statement to each insertion position when the ordered old core is fixed.

For ANY supplied U,c the absolute and cover expenses have their actual complete formulas.
With U^- denoting its diagonal-one negative absolute companion and d=|c|, put

    A_c(t)=(t+1)p_(U^-)(t)
                -t d^T adj(tU^-+(U^-)^T)d.
    p_(Z_c^-)=A_c,
    p_proper_cover=p_(Z_c) A_c.                       (23)

These are monic integral full polynomials of degrees7 and14.
The original/absolute energy is E(U)+||c||^2, the proper-cover energy twice that number, height max(height U,max_i |c_i|), and ranks7/7/14.
For a target satisfying(22), complete measure is log beta4+m(A_c); there is no favorable assigned companion cost until the actual U,c are supplied.
The explicit canonical controls instead have the fully resolved costs(15)--(18).
This separates the new all-core gate from both a realized optimum and the restricted bipartite theorem in L283.

<a id="factor-retention-execution-and-self-check"></a>
### 7. Executed evidence, complete cost boundary and contribution

The declared [J69 exact verifier](../computations/programs/Yin_J_G0069/verify.py) first completed at 2026-10-10T04:49 using Python3.12.14 and SymPy1.14.0, in1.017 seconds against the declared120-second aggregate cap.
Its complete native output (`mathematics/computations/outputs/Yin_J_G0069/result.json`) verifies the symbolic six-variable adjugate identity, the unrestricted two-parameter specialization, all six norm2 solutions and zero, the lambda4 boundary matrix, and236 exact integer pencil evaluations.
It independently constructs each of the eight literal proper covers in vertex-then-sheet order and verifies its whole degree14 or8 determinant against the product.
The separate characteristic-polynomial and pencil-evaluation methods are author self-checks, not noncontributor review.

The36 transported-core controls have252 whole-extension cyclic/insertion cases.
Within each cyclic group BOTH full original and absolute polynomials and the rank/height/energy are preserved.
Changing the core by an arbitrary congruence is NOT asserted to preserve the absolute factor.
Indeed the native output contains two different companion polynomials across the36 core groups:28 have the canonical Phi2 H_(2,2) and energy7;8 have energy8 and

    p_absolute=Phi2 H_extra,
    H_extra=t^3[(t+t^(-1))^3-5(t+t^(-1))^2
                                -15(t+t^(-1))-8].      (24)

All their original polynomials are Phi2 Phi4 P4; all heights are1, and every complete cover polynomial is retained.
The cubic in(24) takes values-6,1,-8,-15,64 at-2,-1,0,7,8, respectively.
It has exactly one expanding reciprocal pair and its entire measure is log alpha_extra, with alpha_extra>(7+sqrt45)/2.
Thus these transported controls also cost MORE than2log beta4 in full cover measure; their energies8 and cover energies16 are not confused with the canonical7/14 control.
These actual non-bipartite presentations show why retaining original factors under core congruence does not retain favorable absolute costs.

There was no failed assertion, cap exit, search expansion, rejected candidate concealed as success, or numerical root approximation in this author execution.
The finite test is exactly the declared symbolic/control scope, not all possible U or all couplings.
The unrestricted coupling, repeated-eigenvalue, every-core and splitting claims are written proofs in Sections2 and6.
Section6 is an analytic strengthening developed after the finite control, with no additional discovery run or computed classification claim.


### Part II. Exceptional pair and arbitrary simultaneous coupling

The proper-cover and absolute conventions are those of Part I.
L46's directed quotient and L207's pendant-tail screen supplied no theorem about this operation and no absence claim.
The original derivations in both parts were by orbit_research for Yin; the original coordinator supplied broad questions and administration rather than derivations.

<a id="rank-one-two-vertex-factor-retention"></a>
### 2. Complete rank-one two-vertex identity and the exceptional neutral pair

Let U be any proper rank-n matrix, c in Z^n, and a,b,k in Z.
Define

    Z=[[U, a c, b c],[0,1,k],[0,0,1]],
    Q_v=t^2+(2-v)t+1,
    delta=a^2+b^2-kab, M=tU+U^T.

The COMPLETE identity is

    p_Z=p_U Q_(k^2)-t s delta c^T adj(M)c.              (1)

Indeed eliminating M gives the two-by-two matrix

    [[s,tk],[k,s]]-t(c^T M^(-1)c) [[a^2,ab],[ab,b^2]].

Its determinant is Q_(k^2)-t(c^T M^(-1)c)s delta: the quadratic correction vanishes because the perturbation has rank one.
This proves(1) over Q(t), and hence as an integral polynomial.
Singular values of t do not restrict the resulting identity.

For a nonzero pair(a,b), the coupling term in(1) vanishes IDENTICALLY for every proper U and every c exactly when

    |a|=|b|>0 and k=2 sign(ab).                        (2)

For sufficiency substitute delta=0.
For necessity, U=[1], c=[1] shows that universal disappearance forces delta=0.
Divide a,b by their positive gcd.
Neither can be zero.
The equation a^2+b^2=kab implies that each of the two coprime integers divides the other's square, so both have absolute value one.
Rescaling gives exactly(2).
Thus, up to a sign change of the second new basis vector and absorption of a common integer into c, the unique nonzero rank-one universal cancellation is a=b=1,k=2.
This is a claim about the ENTIRE stated universal operation, not about all possible individual cancellations: a particular core can have c^T adj(M)c=0 for another reason, as the [open-window boundary control](#open-spectral-window-boundary-control) already shows.

There is also a complete P_A-retention classification in the L287 core class.
In this paragraph keep(a,b)!=(0,0); the omitted pair is disconnected and always has p_Z=p_U Q_(k^2) directly by(1).
Let U_B=[[I_r,-B],[0,I_g]], r>=g+1, B have full column rank, and assume every irreducible minimal-polynomial factor of A=B^T B has a root in(0,4), exactly as in [Part I](#factor-retaining-one-vertex-rigidity).
Set P_A=t^g det((t+t^(-1)+2)I-A) and h=r-g.
For delta!=0, (1), coprimality of P_A with t(t+1), and the [one-vertex theorem](#factor-retaining-one-vertex-rigidity) give

    P_A divides p_Z  iff  c=(x,0), B^T x=0.
    In that case p_Z=s^h P_A Q_(k^2+delta N), N=||x||^2. (3)

The full multiplicities of P_A are retained in this reasoning: divisibility of the second term in(1) is exactly the one-vertex divisibility condition.
The exclusion of a zero Gram eigenvalue is why P_A(-1) is nonzero.
If delta=0, every integer c retains P_A, and in fact the entire p_U, with complete multiplier(t-1)^2 by(2).
Thus the two-vertex exception is real, not a finite failure to detect the one-vertex kernel condition.
The transport through integral core congruence has precisely L287's c=Uw, w in ker_Z(U-U^T) interpretation when delta!=0; no invariance of absolute costs is asserted.

The full costs for(1) are explicit even outside the cancellation class.
Put d=|c|, M_-=tU^-+(U^-)^T and delta_-=a^2+b^2+|kab|.
Then

    p_(Z^-)=p_(U^-) Q_(k^2)-t s delta_- d^T adj(M_-)d,
    p_cover=p_Z p_(Z^-).                              (4)

Original and absolute ranks are n+2, cover rank2n+4.
Their strict-upper energies are E(U)+(a^2+b^2)||c||^2+k^2, and twice that for the cover.
Height is max(1,max|U_ij|,|a|max|c_i|,|b|max|c_i|,|k|).
The complete measures are m(p_Z), m(p_(Z^-)) and their sum, with every factor in(1),(4) retained.
Under(3), m_original=m(P_A)+g(k^2+delta N), where g(v)=0 for0<=v<=4 and g(v)=arcosh(|v-2|/2) otherwise.
Negative values of the effective v are not silently discarded.

<a id="arbitrary-rank-neutral-pair-coupling"></a>
### 3. Arbitrary simultaneous coupling and its full companion cost

For an arbitrary integral n-by-k matrix C, k>=1, form

    Z_C=[[U,C,C],[0,I_k,2I_k],[0,0,I_k]].

There is an exact universal factor-preserving theorem

    p_(Z_C)=(t-1)^(2k) p_U.                           (5)

The new vertices interact with the core through arbitrary columns, including linearly independent ones.
Thus this is not limited to rank-one attachment.
To prove it eliminate the bottom2k block

    T=[[sI_k,2tI_k],[2I_k,sI_k]], det T=(t-1)^(2k).

The coupling correction to M is t C [I,I] T^(-1) [I;I] C^T.
Direct multiplication gives [I,I] T^(-1) [I;I]=0, since its numerator is(2s-2t-2)I.
Thus the Schur complement is exactly M.
Polynomial continuation gives(5) at t=1 too; no division there is a mathematical hypothesis.

Let D=|C|, p_-=p_(U^-), M_-=tU^-+(U^-)^T.
Changing EVERY upper sign to negative changes that same numerator to4sI.
Consequently the COMPLETE absolute polynomial is

    A_C(t)=(t-1)^(2k) det(M_- -4t s D D^T/(t-1)^2),
    p_proper_cover=(t-1)^(2k) p_U A_C(t).              (6)

The rational display is an integral monic polynomial of degree n+2k because it is the actual determinant of Z_C^-; factors are not to be canceled from the proper cover.
Original/absolute rank is n+2k and cover rank2n+4k, height max(2,max|U_ij|,max|C_ij|), energy E(U)+2||C||_F^2+4k and twice that for the cover.
Exact complete measures are

    m_original=m(p_U), m_absolute=m(A_C),
    m_cover=m(p_U)+m(A_C).                            (7)

This proves preservation of original positive measure for arbitrary coupling, not cheapness of that operation on the companion side.

There is a useful degree boundary to the mechanism.
Let r=rank_Q D.
Multilinearity shows det(M_- -z D D^T) has degree at most r in z: any term using more than r columns from D D^T vanishes.
After substituting z=4ts/(t-1)^2, each term in(6) contains at least(t-1)^(2k-2r).
Therefore

    (t-1)^(2k-2r) divides A_C,
    deg[A_C/(t-1)^(2k-2r)]<=n+2r<=3n.                (8)

The exponent is nonnegative since r<=k.
This is a complete scalar degree statement, not a claim that the quotient is irreducible or cyclotomic.
In particular adding arbitrarily many such pairs to a fixed core cannot create unbounded positive irreducible degree in its companion, and it never changes the original noncyclotomic factors at all.
Changed input complexity would have to enter through a changing core or a different operation.

<a id="quartic-neutral-pair-companion-penalty"></a>
### 4. Actual quartic family with exact unbounded companion expense

Take the exact proper rank6 L191/L287 core with B rows(1,1),(0,1),(0,1),(0,1), A=[[1,1],[1,4]], and p_U=s^2 P4, P4=t^4-t^3-t^2-t+1.
It already has U^-=U and complete original measure log beta4.
Let e_2 denote the SECOND of the four left coordinates (index1 if indexing from zero).
For k>=1 take every column of C equal to m e_2, with a nonzero integer m, and put L=k m^2>=1.
Then(5)--(6) simplify to

    p_original=s^2 P4 (t-1)^(2k),
    p_absolute=s^2 (t-1)^(2k-2) H_L,
    p_cover=s^4 P4 (t-1)^(4k-2) H_L,
    H_L=t^3 f_L(t+t^(-1)),
    f_L(v)=v^3-(4L+3)v^2-v+8L+6.                    (9)

For verification of the specialization, the core resolvent gives

    s e_2^T adj(M)e_2=s^2(t^4+1).

Indeed at u=t+t^(-1)+2 the relevant numerator is u^2-4u+2, and t^2(u^2-4u+2)=t^4+1.
The repeated columns give D D^T=L e_2 e_2^T.
Inserting this into(6) yields the complete factor in(9), not only its dominant root.

The cubic f_L has exactly one root in each interval

    (-2,-1), (1,2), (4L+2,4L+3).                     (10)

At -2,-1,1,2 its values are -8L-12,4L+3,4L+3,-8L, respectively.
At4L+2 and4L+3 they are -16L^2-12L and4L+3.
Three disjoint sign-changing intervals exhaust its degree.
Let lambda_L be its last root and alpha_L=(lambda_L+sqrt(lambda_L^2-4))/2.
The other two reciprocal pairs lie on the unit circle.
Consequently the FULL costs are

    m_original=log beta4,
    m_absolute=log alpha_L,
    m_cover=log beta4+log alpha_L,
    log(4L+1)<log alpha_L<log(4L+3).                  (11)

Here lambda-1<alpha<lambda for lambda>2.
Thus already at L=1 the complete companion exceeds beta4, and the cover costs more than twice the original.
As |m| or k increases, the whole original measure remains fixed positive, while the companion expense diverges like log L.
The actual rank is6+2k, height max(2,|m|), original/absolute energy5+2L+4k and cover energy10+4L+8k.
The neutral degrees displayed in(9) are paid explicitly.
The smaller-target rank6 L191 control still achieves exact doubled measure and lower dimension.

For L congruent1 modulo3, H_L is actually irreducible of degree6.
The trace polynomial reduces to v^3-v^2-v+2 modulo3, with no root in F3; hence it is irreducible over Q.
The trace field is totally real by(10).
If v^2-4 were a square in that field, all of its real conjugates would be nonnegative; the root in(-2,-1) contradicts this.
Thus adjoining a root of t^2-vt+1 doubles the trace degree to6.
This proves irreducibility directly.
It supplies genuine companion sextics, not increasing irreducible complexity: their degree stays6 as the neutral padding grows, consistently with(8).

<a id="changed-nonbipartite-phi6-control"></a>
### 5. A different proper rank8 Phi6 control, with its full higher cost

The nonexceptional branch(3) also has a concrete two-vertex control outside the rectangular bipartite architecture.
In the same core choose

    c=(0,1,-1,0,0,0)^T, a=b=k=1.

Then c lies in the actual alternating kernel, N=2 and delta=1.
The complete original polynomial is

    p_Z=s^2 P4 Phi6.                                  (12)

The graph has triangles: both added vertices meet the same core coordinates and have a nonzero internal edge.
Its full absolute polynomial and proper cover are

    p_(Z^-)=s^2 J, p_cover=s^4 P4 Phi6 J,
    J=t^3[(t+t^(-1))^3-6(t+t^(-1))^2
                                  -10(t+t^(-1))+3].  (13)

To check this, d=|c| has norm squared2 and B^T d=(0,2)^T.
The same inverse-block calculation gives s d^T adj(M)d=2s^2[s^4-3ts^2+t^2].
In(4), delta_-=3 and Q_(k^2)=Phi3.
Their substitution gives exactly(13).
Its trace cubic has roots in(-2,-1),(0,1),(7,8), from values -9,6,3,-12,-18,51 at -2,-1,0,1,7,8.
Thus its WHOLE measure is log alpha_J for the unique expanding reciprocal pair, alpha_J>(7+sqrt45)/2>beta4.
Original/absolute rank8 and proper-cover rank16 are literal; height1, energies10/10/20.
The complete cover cost is log beta4+log alpha_J>2log beta4.

This is a genuine non-bipartite realization of the paid target already realizable at rank8 by L283, not a new minimum dimension or a cost improvement.
L283's bipartite companion trace root is in(3,4), so this control is strictly more expensive.
The target without the two Phi2 factors remains absent here.
Its purpose is to verify that the second branch of the exact two-vertex classification produces actual scalar targets and to keep the changed architecture and its cost distinct from an exclusion of all rank7 forms.

<a id="independent-pair-full-two-root-cost"></a>
### 7. Independent columns produce an actual irreducible octic companion

The fourth fixed control has C=[e_1,e_2], two linearly independent left columns, and k=2.
Its full original factor is still s^2 P4(t-1)^4.
Formula(6) gives

    p_absolute=s^2 H8,
    H8=t^4 g(t+t^(-1)),
    g(v)=v^4-13v^3+33v^2+64v-44,
    p_cover=s^4 P4(t-1)^4 H8.                         (14)

Here is a direct two-dimensional check of that specialization.
Put chi(u)=u^2-5u+3.
The selected submatrix of s M^(-1) on e_1,e_2 is

    I_2 + [1,1;0,1](uI-A)^(-1)[1,0;1,1].

Its trace is (2u^2-7u+2)/chi(u), and its determinant is (u^2-2u)/chi(u).
The latter follows either by the two-by-two determinant or by replacing A with A-[1,0;1,1][1,1;0,1]=diag(0,2).
Set z=4t/(t-1)^2.
The determinant correction in(6) is therefore

    1-z(2u^2-7u+2)/chi(u)+z^2(u^2-2u)/chi(u).

Multiplying by (t-1)^4 s^2 t^2 chi(u), substituting u=t+t^(-1)+2 and collecting proves(14).
This also supplies a transparent derivation independently of the saved coefficient arrays.

The values of g at -2,-1,0,1,6,7,8 are80,-61,-44,41,16,-37,20.
Thus it has exactly four real roots in(-2,-1),(0,1),(6,7),(7,8).
The latter two roots lambda_3,lambda_4 each give an expanding reciprocal pair.
Define alpha_i=(lambda_i+sqrt(lambda_i^2-4))/2.
The COMPLETE costs of this actual control are

    m_original=log beta4,
    m_absolute=log alpha_3+log alpha_4,
    m_cover=log beta4+log alpha_3+log alpha_4.           (15)

In particular alpha_3>5 and alpha_4>6, so the companion cost exceeds log30.
Its ranks are10/10/20, height2, original/absolute energy17 and cover energy34.
An estimate based on only its Perron root would omit a strictly positive second contribution.
Both neutral factors and that second pair remain in(14)--(15).

This is also an ACTUAL irreducible degree-eight companion.
Modulo3, g=v^4-v^3+v+1 has values1,2,2 at the three field elements.
The three monic irreducible quadratics are v^2+1, v^2+v+2, v^2+2v+2; division leaves respective remainders2v+2,2v+1,2v+2.
Thus g has neither a linear nor an irreducible quadratic factor and is irreducible over F3, hence over Q.
Its trace field is totally real by the four intervals.
A conjugate in(-2,-1) makes v^2-4 negative, so that element is not a square in the totally real field.
The reciprocal quadratic extension has degree two and H8 is irreducible of degree8.
This changed companion complexity is finite and expensive; the unchanged original positive factor is still P4.
It is not a bounded-companion-cost family of increasing original irreducible degree.

<a id="coupled-neutral-pairs-scope-and-self-check"></a>
### 8. Executed evidence, boundaries and author self-check

[J72](../computations/programs/Yin_J_G0072/readme.md) executed exactly the declared five matrices, with no discovery search.
The first successful run was2026-10-10T05:19, taking0.4162429 seconds.
The already declared fourth control produced two expanding pairs; the cost-completion checks of Section7 were then stated in the responsible J before a same-domain rerun.
That final run succeeded at 2026-10-10T05:21 in0.4068650 seconds.
Combined author runtime was0.8231079 seconds, below the original aggregate120-second cap.
No failed assertion, timeout, hidden matrix extension or numerical root scan occurred.
The extra fifth control had been justified and approved BEFORE the first execution.
Its purpose and the initial four-control allocation remain accurately recorded in J72.

The native Python3.12.14/SymPy1.14.0 program verifies the full symbolic rank-one identity, both k=1,2 paired contractions and their absolute counterparts, the displayed cofactor specializations, all-L sextic coefficients and endpoint identities, and the exact mod3 arithmetic.
It computes all fifteen complete original/absolute/literal-cover polynomials by exact characteristic-polynomial arithmetic and independently checks191 integer full-pencil values, with at least degree-plus-one points for each polynomial.
Forty additional scalar Schur values verify(6) on the four paired controls.
It retains every actual matrix, all integer coefficient arrays, ranks, heights, energies, trace factors, and the extra Section7 irreducibility/sign checks.
These are author computations, with some ordinary helper patterns reused from the author's earlier J69 verification; they are not a separate independent verification.
No old program or output was changed.
The all-k, all-C and all-L claims have complete written proofs and are not inferred from these finite checks.

The resulting mechanism is exact: simultaneous neutral pairs can preserve a full scalar polynomial under arbitrary integer couplings even where a single preserving vertex must lie in the alternating kernel.
The exceptional rank-one operation is classified in full.
The absolute matrix does not enjoy that cancellation.
The fixed quartic examples retain constant positive original measure while the complete companion expense grows, and an independent-column example has an irreducible octic with TWO positive measure contributions.
These presentation costs are compatible with D9's older warning about uncontrolled signed covers; the new contribution here is the explicit universal coupled-pair formula, its rank/degree boundary and the complete actual controls, not a new general discovery that presentations can be expensive.

No stated construction removes the original Phi2 factors, realizes rank7 Phi2 Phi6 P4, lowers the complete positive seed measure, or produces unbounded original irreducible complexity from a fixed core.
The non-bipartite paid rank8 Phi6 control has higher cost than the existing L283 bipartite presentation.
Even the neutral-pair family is worse than L191's lower-rank doubled-cost control for the smaller complete quartic target.
A meaningful next question is whether a different internal multi-vertex block can retain a desired noncyclotomic factor while reducing unwanted neutral factors, or whether a changing core with controlled whole measure can use such cancellations without an increasing companion penalty.
Neither is a theorem here, and no further search is part of this round.


## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:25 |
| status | open |
| reason | Register both complete integral-extension proof chains at their explicit distinct operation classes; current whole internal inspection follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Every matrix, operation class, hypothesis, neutral factor, actual degree and full original/absolute/cover expense. |
| argument | [Entire two-part argument](#argument) | Full open-window/every-core proofs, universal rank-one exception, arbitrary-rank cancellation, companion degree bounds, exact controls and source/native limits. |
| dependency | [C458v2 Gram identity](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Actual integral Gram determinant, quartic and complete spectral costs. |
| dependency | [C521 alternating-kernel theorem](Yin_C_G0521_v1.md#statement) | Primitive adapted kernel, minus-one coefficient and norm-one bilinear splitting. |
| dependency | [C2 literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) | Full original/negative-absolute product and actual two-sheet construction. |
| support | [Original one-vertex input](../ledger/Yin_L_G0287_v1.md#factor-retention-reuse) | Complete original Sections1--7/equations1--24 including4a and original author/native/source/failure/frozen-review history. |
| support | [Original paired-coupling input](../ledger/Yin_L_G0291_v1.md#coupled-neutral-pairs-reuse) | Complete original Sections1--8/equations1--15 and distinct original author executions. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:39 |
| status | proved |
| reason | Adopt the full unchanged mathematical statement and complete argument after the actual current whole SELF, preserving every operation/class/input/cost/negative/source/native limit; original UNKNOWN or SELF findings are not upgraded to independence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Every matrix, operation class, hypothesis, neutral factor, actual degree and full original/absolute/cover expense. |
| argument | [Entire two-part argument](#argument) | Full open-window/every-core proofs, universal rank-one exception, arbitrary-rank cancellation, companion degree bounds, exact controls and source/native limits. |
| dependency | [C458v2 Gram identity](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Actual integral Gram determinant, quartic and complete spectral costs. |
| dependency | [C521 alternating-kernel theorem](Yin_C_G0521_v1.md#statement) | Primitive adapted kernel, minus-one coefficient and norm-one bilinear splitting. |
| dependency | [C2 literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) | Full original/negative-absolute product and actual two-sheet construction. |
| support | [Original one-vertex input](../ledger/Yin_L_G0287_v1.md#factor-retention-reuse) | Complete original Sections1--7/equations1--24 including4a and original author/native/source/failure/frozen-review history. |
| support | [Original paired-coupling input](../ledger/Yin_L_G0291_v1.md#coupled-neutral-pairs-reuse) | Complete original Sections1--8/equations1--15 and distinct original author executions. |
| review | [Actual current whole SELF](../audits/reviews/Yin_R_G0739_v1.md#current-integral-couplings-whole-self-finding) | Entire selected statement and complete argument, including both original proof chains where this C combines them; exact scope and current SELF relationship are declared in R739. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:42 |
| status | proved |
| reason | Adopt the unchanged complete statement and written argument through the separately arranged isolated whole inspection completed at 2026-10-22T20:32; old findings keep their actual original inputs, relationships, dates and source/native limits. This decision performs no proof repair, native run or research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Every matrix, operation class, hypothesis, neutral factor, actual degree and full original/absolute/cover expense. |
| argument | [Entire two-part argument](#argument) | Full open-window/every-core proofs, universal rank-one exception, arbitrary-rank cancellation, companion degree bounds, exact controls and source/native limits. |
| dependency | [C458v2 Gram identity](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Actual integral Gram determinant, quartic and complete spectral costs. |
| dependency | [C521 alternating-kernel theorem](Yin_C_G0521_v1.md#statement) | Primitive adapted kernel, minus-one coefficient and norm-one bilinear splitting. |
| dependency | [C2 literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) | Full original/negative-absolute product and actual two-sheet construction. |
| support | [Original one-vertex input](../ledger/Yin_L_G0287_v1.md#factor-retention-reuse) | Complete original Sections1--7/equations1--24 including4a and original author/native/source/failure/frozen-review history. |
| support | [Original paired-coupling input](../ledger/Yin_L_G0291_v1.md#coupled-neutral-pairs-reuse) | Complete original Sections1--8/equations1--15 and distinct original author executions. |
| review | [Actual isolated whole written finding](../audits/reviews/Yin_R_G0770_v1.md#whole-current-independent-finding) | Entire exact current statement and complete argument, including every actual class, fixed-input interface, original-law/degree/cost control and stated negative or unresolved boundary; no new native execution or original source-proof audit. |

