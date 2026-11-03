---
author: Yin
---

# Integral cancellation obstruction for the degree-six realization

Current complete proof home: [C521](../claims/Yin_C_G0521_v1.md#stable-cancellation-fixed-scope), selected with [the actual complete current whole SELF](../audits/reviews/Yin_R_G0730_v1.md#current-integral-cancellation-whole-self-finding).
The [original R110 whole](../audits/reviews/Yin_R_G0110_v1.md#independent-review-stable-cancellation) remains UNKNOWN at its actual frozen input; its original independent wording/verdict and dates are preserved rather than retrospectively reclassified as SELF or asserted isolation.
The [complete original author checking/contribution account](../audits/reviews/Yin_R_G0730_v1.md#original-integral-cancellation-author-whole-self-finding) is separately SELF; current SELF does not close the old UNKNOWN or select/resume research Task/E.

Date: 2026-10-10.
The coordinating AI for Yin adopts this restricted result after complete separately organized noncontributor review under the continuing G0001 authorization.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="stable-cancellation-fixed-scope"></a>
## Current adopted scope

The complete argument identifies the primitive alternating-kernel restriction and its nonsingular modulo-prime discriminant square class as a congruence invariant.
It proves a norm-one splitting criterion, the exact leading-coefficient identity and an obstruction to every common identical integral stabilization of the actual rank-eight P6 realization to a rank-seven realization plus one.
The exact J46 controls and read-only independent replay are retained separately.
An independent high-energy rank-seven realization or a different stabilizing class remains open; original, absolute and signed-cover costs are all retained.

G0001 remains unresolved.

<a id="complete-retained-proof-and-review"></a>
## Complete retained author proof and independent review

## Cyclotomic cancellation and higher-energy integral realization

Date: 2026-10-10.
Starting question: Continue the prescribed P6 realization beyond the low-energy obstruction in L210.
Investigate higher-energy rank-seven presentations or rigorous integral cancellation/stabilization criteria, retaining complete polynomial, lattice and absolute-cover costs.
Do not repeat the excluded at-most12-unit-edge class.

The unrestricted Task remains unresolved.

### Reuse screen and changed question

The actual input is P(t)=t^6-t^5-t^3-t+1, with P(-1)=5 and Salem root beta in(3/2,151/100), as fixed in [L199](Yin_L_G0199_v1.md#degree-six-return-core-fixed-scope).
[L210](Yin_L_G0210_v1.md#signature-energy-fixed-scope) already gives an integral rank-eight V8 with full polynomial Phi2² P and energy7, by applying the earlier L191 Gram construction.
It also proves that any rank-seven realization of Phi2 P would have symmetric inertia(4,3) and energy at least13.
The excluded low-energy class is not searched again here.

The [L190 endpoint calculation](Yin_L_G0190_v1.md#nonzero-endpoint-stabilization-cost), [D9 exact congruences and signed cover](../claims/Yin_C_G0002_v1.md#signed-cover-identity), [D12 mutation scope](../claims/Yin_C_G0003_v1.md), and [L184 congruence boundary](Yin_L_G0184_v1.md#cycle-surgery-fixed-scope) were reread.
Their retained classical Pfaffian-square identity is reused, not newly attributed.
A targeted local screen of these inputs, L191, L196, L207 and L210 for the alternating-kernel restriction and its stabilized congruence invariant did not locate the argument below.
That bounded reuse screen is not an external novelty search or a claim that the invariant is historically new.
No new external theorem is needed or adopted.

The changed question is integral cancellation: can the known V8 be changed by integral bilinear congruences and common stabilizations into a rank-seven realization with one isolated[1] block?
An isolated[1] contributes exactly Phi2=t+1.
Polynomial divisibility by Phi2 does not itself split such an integral block.
The result below excludes this proposed cancellation route even after adding an arbitrary common integral matrix, while leaving an independently constructed rank-seven realization open.

<a id="alternating-kernel-splitting-criterion"></a>
### 1. The integral alternating kernel and exact one-block splitting

For an integral n by n matrix V define

    A_V=V^T-V,
    K(V)={x in Z^n:A_V x=0},
    b_V(x,y)=x^T V y for x,y in K(V).                        (1)

The group K(V) is a primitive free abelian sublattice: if a nonzero integer multiple of an integral vector lies in the kernel, so does that vector.
Integer row reduction therefore extends a Z-basis of K(V) to one of Z^n.
The restriction b_V is symmetric because x^T(V-V^T)y=0 on K(V), and is integral.
It need not be nondegenerate.
Neither the ambient V nor this definition requires definiteness.

If V'=Q^T V Q with Q in GL_n(Z), then Q maps K(V') bijectively to K(V) and preserves their restricted pairings.
This is a genuine lattice isometry, since Q and its inverse are integral.
Also

    K(V direct-sum W)=K(V) direct-sum K(W),
    b_(V direct-sum W)=b_V direct-sum b_W.                   (2)

Here and below the orthogonal sums in(2) refer to the restricted symmetric forms; the ambient matrices may be nonsymmetric.

**Splitting criterion.** There is an integral bilinear congruence from V to[1] direct-sum V' for some integral V' if and only if K(V) contains w with b_V(w,w)=1.

Necessity follows by transporting the first basis vector.
Conversely put ell(x)=w^T V x.
Since w lies in K(V), ell(x)=x^T V w and ell(w)=1.
Every x decomposes integrally as ell(x)w+[x-ell(x)w], so Z^n=Zw direct-sum ker ell.
The two summands are orthogonal for the ambient bilinear form in both orders.
A Z-basis of ker ell together with w gives a unimodular change of basis and the claimed block decomposition.
If det V=1, then det V'=1 as well.

This criterion is exact for integral bilinear splitting.
It does not assert that the complement has an upper-unitriangular basis, even if V initially has one.
That additional presentation requirement cannot be inferred from an integral matrix of determinant1.
The obstruction below uses only necessity, so it also obstructs the more restrictive upper-unitriangular cancellation.

<a id="minus-one-leading-coefficient-kernel"></a>
### 2. The first nonzero coefficient at minus one determines a kernel cost

Suppose now V is integral upper-unitriangular, and let r be the rank of K(V).
Choose an integral basis adapted to K(V).
Its change-of-basis matrix Q is unimodular, and in this basis

    Q^T V Q=[[G,X],[X^T,Y]],
    Q^T A_V Q=[[0,0],[0,A0]],   A0=Y^T-Y.                   (3)

The integer matrix G is a Gram matrix of b_V.
A0 is nonsingular alternating, so its size n-r is even.
Write d=Pf(A0), a nonzero integer; if that size is zero, use d=1.
The retained Pfaffian identity gives det A0=d².
Substituting t=-1+s yields

    Q^T(tV+V^T)Q=[[sG,sX],[sX^T,A0+sY]].                   (4)

The determinant is unchanged because det(Q)^2=1.
Expanding the determinant in s shows divisibility by s^r and gives

    coefficient of s^r in p_V(-1+s)=d² det G.               (5)

For example one can factor s from the first r rows in(4) and set s=0; the remaining block upper-triangular determinant is det G det A0.
This proves the coefficient even when G is singular.
It is nonzero precisely when the multiplicity of the root-1 equals r.
If G is singular the multiplicity is larger; there is no silent equality assumption.

Let P be an even-degree polynomial with P(-1)=N nonzero.
If p_Z=(t+1)P for an integral upper-unitriangular Z, then the kernel rank is1: it is positive and odd, since Z has odd size, and cannot exceed the simple-root multiplicity.
Its primitive generator w has some integral norm a, and(5) gives

    N=d_Z² a.                                               (6)

For the actual P, N=5, so d_Z=+1 or -1 and a=5.
This conclusion applies to every possible Z, without knowing its entries or imposing an energy bound.
Similarly any V with p_V=(t+1)²P has kernel rank2, since its size is even, its kernel rank is a positive even integer and its root multiplicity is2.
Its restricted Gram matrix obeys

    N=d_V² det G.                                           (7)

For N=5, every such G has determinant5.
The determinant alone need not identify its integral isometry class; that distinction is exactly what the next step uses.

<a id="kernel-mod-prime-stable-obstruction"></a>
### 3. A congruence invariant that survives every common stabilization

Fix an odd prime ell.
Reduce the integral restricted lattice(K(V),b_V) modulo ell.
Importantly, this means K(V)/ell K(V) with its reduced pairing, not the possibly larger kernel of A_V modulo ell.
Let R_V be the radical of that reduced symmetric form: the vectors pairing to zero with all vectors.
The quotient by R_V carries a nondegenerate symmetric form over F_ell.
Define

    delta_ell(V)=det(that quotient form) in F_ell^*/(F_ell^*)², (8)

with delta=1 for a zero-dimensional quotient.
Thus delta is always a nonzero square class, including when the original restriction is degenerate.

This definition is independent of every basis and complement choice.
The radical is intrinsic; the induced form on the quotient is well defined because the discarded vectors pair to zero with everything.
A change of quotient basis multiplies its determinant by the square of the basis determinant.
Choosing any complement to the radical realizes the same quotient form and hence gives the same class.
The integral isometry in Section1 descends to an isometry of these reduced quotients, so delta is invariant under integral bilinear congruence.

The radical of an orthogonal direct sum is the direct sum of its radicals.
Therefore the nondegenerate quotient is also an orthogonal direct sum and

    delta_ell(V direct-sum W)=delta_ell(V)delta_ell(W).        (9)

This proves actual cancellation of a common factor in the square-class group.
There is no invertibility assumption on b_W over Q or modulo ell: its nondegenerate quotient is the object in(8), and its determinant class is invertible by definition.
This also covers K(W)=0 and the case where the entire reduced restriction is radical.
No general lattice-classification or Witt-cancellation theorem is being imported.

**General obstruction.** Let P be an integral polynomial of even degree with N=P(-1) nonzero, and suppose the odd prime ell divides N exactly once.
Let V2 be integral upper-unitriangular with p_(V2)=(t+1)²P.
If delta_ell(V2) is not the square class1, then for every integral upper-unitriangular Z with p_Z=(t+1)P and every integral square matrix W, there is no integral unimodular congruence

    V2 direct-sum W  congruent to  Z direct-sum[1] direct-sum W. (10)

To prove this, (6) shows that ell does not divide d_Z and that the norm a of the primitive one-dimensional kernel is divisible by ell.
Its reduction is entirely radical, so delta_ell(Z)=1.
Also delta_ell([1])=1.
The right side of(10) has invariant delta_ell(W), while the left side has delta_ell(V2)delta_ell(W).
Equality would force delta_ell(V2)=1, a contradiction.
The case where no Z exists satisfies the conclusion without any existence assertion.
Equation(7) also shows that the rank-two Gram matrix of V2 has determinant divisible by ell exactly once; its reduction has rank1, since all its entries cannot be divisible by ell.
This gives a small exact way to compute the relevant invariant.

The common block W in(10) is entirely arbitrary, of any finite size, and can have additional alternating kernel or degenerate restricted form.
For neutral stabilization one may require it to be upper-unitriangular with cyclotomic p_W, but that is a smaller allowed class than the obstruction already covers.
The theorem does not exclude replacing W by a different block on the other side whose reduced kernel form changes the discriminant.
Such changed stabilization needs a fresh comparison, not an invocation of(10).

<a id="p6-stable-cyclotomic-cancellation-obstruction"></a>
### 4. The actual P6 matrix fails the cancellation criterion stably

Use the exact L210 matrix

    B=[[1,1,0],[1,0,1],[1,0,0],[0,1,0],[0,1,0]],
    V8=[[I5,-B],[0,I3]],
    p_(V8)=(t+1)²P.                                        (11)

Its alternating kernel is fully explicit.
Writing a vector as(x,y) with x in Z^5 and y in Z^3, the kernel equations are By=0 and B^T x=0.
The rows(1,0,0),(0,1,0) and(1,0,1) exhibit rank3, so By=0 forces y=0.
The remaining equations give

    x_2=0,    x_3=-x_1,    x_5=-x_1-x_4.

Thus the complete integer kernel, not a sublattice of finite index, has basis

    u=(1,0,-1,0,-1;0,0,0),
    v=(0,0,0,1,-1;0,0,0).

The first and fourth x-coordinates recover its two arbitrary integer coefficients.
Since y=0, the restricted pairing is the ordinary dot product on these x-vectors.
Its Gram matrix and norm are

    G=[[3,1],[1,2]],     det G=5,
    q(a,b)=3a²+2ab+2b².                                    (12)

It has no integral norm-one vector: q=2(b+a/2)²+(5/2)a², so a nonzero a gives q>=5/2, hence integer q>=3, whereas a=0 gives2b².
Its minimum on nonzero integral vectors is2.
Thus Section1 already rules out immediate removal of an orthogonal[1] block.

For the stronger stable obstruction reduce(12) modulo5.
Its matrix has rank1 and radical spanned by(1,2).
The class of the first basis vector is outside the radical and has norm3.
Therefore

    delta_5(V8)=class(3),                                  (13)

which is not1, since the nonzero squares modulo5 are1 and4.
Sections2--3 now prove(10) for this actual V8 and every possible rank-seven Z realizing(t+1)P, with every common integral W.
Equivalently, adjoining arbitrary common neutral blocks, applying an arbitrary integral unimodular bilinear congruence, and removing those same blocks cannot turn this V8 into Z direct-sum[1].
Adjacent Stokes mutations and diagonal sign changes are contained in the integral congruence class and therefore cannot evade this obstruction either.
There is no restriction here to nonincreasing energy paths or to bounded mutation length.

The exact endpoint derivative5 forces the unknown Z's primitive kernel norm to be5; adjoining[1] would have restricted form[5] direct-sum[1].
Its reduction modulo5 has square discriminant class1, unlike(13).
The failure is thus an integral form distinction between potential presentations of the same complete degree-eight polynomial.
It does not say that the degree-seven polynomial is unrealizable in a different bilinear class.

<a id="stable-cancellation-full-costs"></a>
### 5. Full factors, coefficient costs and boundaries

For(11), every diagonal entry is1, the largest strict-upper absolute entry is1 and E(V8)=7.
Its sole added factor is Phi2², of degree2, and m(p_(V8))=log beta.
It equals its all-negative absolute companion, so the canonical signed cover has rank16, energy14 and full polynomial Phi2^4 P², with measure2log beta.
These are the fixed L210/L191 costs, not new optimized claims.

If W is an r by r integral upper-unitriangular neutral block with cyclotomic C=p_W, put E_W=sum_(i<j)W_ij² and let W^- be its all-negative companion.
Entry height denotes the maximum absolute strict-upper entry, with value0 when that set is empty.
The left side of(10) then has exactly

    rank=8+r,    p=Phi2² P C,
    E=7+E_W,     entry height=max(1,height W),
    p_absolute=Phi2² P p_(W^-),
    p_doublecover=Phi2^4 P² C p_(W^-),
    m(p_doublecover)=2log beta+m(p_(W^-)).                   (14)

Its cover rank is16+2r and its cover energy is14+2E_W.
The entire neutral C, including all multiplicities, remains present; its degree is r.
A neutral original block need not have a neutral absolute companion, so that last measure term cannot be deleted.

For a hypothetical Z in(10), the right side would have the same full original polynomial Phi2² P C.
Its absolute companion has full polynomial Phi2 p_(Z^-) p_(W^-), and its double cover has the product of these two full polynomials, with measure

    log beta+m(p_(Z^-))+m(p_(W^-)).                          (15)

Its original energy is E(Z)+E_W>=13+E_W by L210, and its cover doubles that energy.
Its entry height is max(1,height Z,height W); no numerical bound on height Z or m(p_(Z^-)) is inferred.
Congruences can change both energy and absolute measure, so(14)--(15) are accounts of the actual two presentations, not a cost-invariance argument.
The impossibility of(10) rests solely on the restricted-lattice invariant.

This is not an obstruction under every different cyclotomic stabilization.
It excludes every common stabilizer in the precise integral congruence comparison, and gives a general necessary square-class criterion for inputs with a simple odd prime divisor of P(-1).
Changing the stabilizing form, constructing a new high-energy rank-seven matrix from another class, or using an operation outside integral bilinear congruence remains possible.
The criterion also does not supply a sufficient upper-unitriangular complement, universal reciprocal-input realization or a near-one absolute-cover estimate.

### 6. Verification and contribution scope

The finite control in [J46](../computations/programs/Yin_J_G0046/readme.md) checks the complete matrices, polynomials, integer kernel parameterization, restricted form, residue-field quotient and costs.
It was executed successfully using Python and SymPy.
Five neutral stabilizer controls include an empty kernel, a nonsquare quotient, an entirely radical nonzero reduced kernel, and a mixed quotient/radical case.
Their complete original polynomials are retained.
It contains no scan of the excluded low-energy class and no numerical claim about a rank-seven solution.
The all-matrix, all-common-stabilizer and general-input statements are proved above, not extrapolated from the finite control.

The coordinator assigned the broad post-L210 question, allocated D81 and permitted the small J46 verifier; it supplied none of the splitting criterion, leading-coefficient proof, modulo-prime quotient invariant or actual kernel calculation.
Its later request to check primitive-kernel and degenerate-stabilizer scope is addressed explicitly in Sections1--3.
The author developed and self-checked this full argument, reusing the retained Pfaffian identity and existing full determinants.
No external novelty claim is made for these elementary linear-algebra mechanisms.

The discriminating continuation is now to alter the bilinear class or the neutral block's restricted-kernel invariant, or to obtain a further necessary condition for an independently constructed high-energy Z.
Repeated common stabilization of this V8 cannot produce the desired cancellation.
This precise failure leaves the broader realization route open and G0001 unresolved.

The full author scope is frozen at 2026-10-09T20:47 for separately arranged complete noncontributor review: this draft and J46/{readme.md,verify.py,verification.json}.
Final self-check covered primitive-kernel completion, the integral splitting functional, singular-G coefficient behavior, kernel-rank versus root-multiplicity parity, exact prime divisibility, basis-independent quotient discriminant and cancellation for arbitrary degenerate common W, actual P6 parameterization, all full factors and cost boundaries.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0110_v1.md#independent-review-stable-cancellation), with its original inspected scope and relationship.
