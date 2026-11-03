---
author: Yin
---

# Interlaced integral realizations with nonreal reciprocal traces

The complete current mathematical home is [C470](../claims/Yin_C_G0470_v1.md#statement), whose current decision adopts the [new R682 whole finding](../audits/reviews/Yin_R_G0682_v1.md#interlaced-quartic-isolated-whole) at2026-10-21T22:48.
The original [listed author SELF](../audits/reviews/Yin_R_G0095_v1.md#interlaced-original-author-check-finding) and the [precise original whole-review facts](../audits/reviews/Yin_R_G0682_v1.md#l196-and-r95) remain at their actual scopes and dates.

Date: 2026-10-10.
The coordinating AI for Yin adopts the complete D G0065 proof and full separate noncontributor review.
The orbit_research AI supplied all new mathematics; the coordinator independently reviewed it.
No new computation or external theorem is used.

<a id="interlaced-realization-fixed-scope"></a>
## Adopted scope

The explicit interlaced weighted four-cycle matrices below realize an infinite family of actual irreducible reciprocal unit quartics with nonreal trace roots, with neutral multiplier exactly one.
Such a polynomial cannot divide any real block-Gram determinant, even after cyclotomic multiplication.
The construction therefore leaves that restricted trace class while retaining integer entries and every diagonal one.

The same support in block order has a different explicitly computed polynomial.
The entire original measure, absolute presentation, rank-eight signed cover and all entry/energy costs are retained, including the change between one and two expanding absolute trace branches.
Both measures grow asymptotically as2log(n(n+1)); no near-one or optimized universal cost assertion is adopted.
The proof gives actual coverage outside one restricted class, not coverage of every reciprocal input.
G0001 remains active and unresolved.
Historical pending-review wording records chronology; only heading depth and relative navigation are transformed.

<a id="retained-interlaced-realization-proof"></a>
## Integral reciprocal realization beyond the Gram trace subclass

Date: 2026-10-10.
Author inquiry by orbit_research for Yin.
Starting question: Develop a concrete integer upper-unitriangular realization mechanism beyond L191 diagonal-dominant Gram trace matrices, or prove a surviving invariant with an actual unrestricted-domain control.
Preserve full determinant, unit diagonal, cyclotomic factors and complete extra measure; merely reproducing the L175 nonreal-trace exclusion is insufficient.
The coordinator assigned the question but supplied no derivation.
G0001 remains active and unresolved.

### Reuse and changed mechanism

Read the fixed [L191 Gram construction](Yin_L_G0191_v1.md#integral-gram-realization-fixed-scope), the [L175 block-bipartite trace restriction](Yin_L_G0175_v1.md#sparse-trinomial-auxiliary), the [L184 cycle-order calculation](Yin_L_G0184_v1.md#cycle-order-polynomial), and the signed cover in [D9](../claims/Yin_C_G0002_v1.md#signed-cover-identity).
The matching/full-cycle determinant expansion and the sensitivity to ordering are established inputs here.
The present construction uses weighted four-cycles with an interlaced vertex order to obtain irreducible quartics with nonreal trace roots.
It does not merely rename the Gram variables or re-state their exclusion.

The underlying four-cycle graph is bipartite.
What is different is the order used to build its upper-unitriangular matrix: the two bipartition classes are interlaced, so the matrix is not the block form [[I,B],[0,I]] used in L175/L191.
An explicit comparison below computes the changed polynomial when the same signed edge weights are instead put in bipartition order.
No permutation congruence preserving the original determinant is inferred from that reorientation.

The new family has no neutral multiplier at all.
Its complete signed and absolute polynomials, all root contributions to measure, matrix size and coefficient costs are proved below.
The examples have growing measure at fixed degree; they do not provide unrestricted coverage or a near-one family.
The argument is self-contained from the retained determinant conventions, requires no new source theorem or computational scan, and makes no historical novelty claim.

<a id="interlaced-four-cycle-determinant"></a>
### 1. An exact weighted four-cycle identity

For arbitrary integers a,b,c,d, let

    V(a,b,c,d)=[[1,a,0,d],
                [0,1,b,0],
                [0,0,1,c],
                [0,0,0,1]],
    E=a^2+b^2+c^2+d^2,      s=t+1.

The full determinant is

    det(tV+V^T)
      =s^4-E t s^2+(a^2 c^2+b^2 d^2)t^2-abcd(t^3+t)
      =t^4+(4-E-abcd)t^3
           +(6-2E+a^2 c^2+b^2 d^2)t^2
           +(4-E-abcd)t+1.                                  (1)

Indeed a nonzero determinant permutation is either the identity, one edge transposition, two disjoint edge transpositions, or one of the two oriented full four-cycles.
The identity gives s^4.
A transposition at an edge of weight w gives -tw^2 and leaves two fixed vertices, yielding the second term.
The two perfect matchings give t^2 a^2 c^2 and t^2 b^2 d^2.
Each full cycle has permutation sign minus; the two numbers of upper-triangular entries are three and one, giving -abcd(t^3+t).
These exhaust all nonzero terms, since there is no triangle.
This proves the complete polynomial identity including all signs and multiplicities.

For the all-negative absolute presentation V^-, the energy and matching terms are unchanged, but the full-cycle product is |abcd|.
Therefore

    p_(V^-)=t^4+(4-E-|abcd|)t^3
                    +(6-2E+a^2 c^2+b^2 d^2)t^2
                    +(4-E-|abcd|)t+1.                       (2)

This is the actual polynomial of the absolute matrix, not a spectral estimate.

<a id="nonreal-trace-integral-quartic-realization"></a>
### 2. An infinite irreducible family beyond the real-trace class

For every integer n>=2 put q=n(n+1), and choose

    V_n=[[1,2,0,-n],
         [0,1,n+1,0],
         [0,0,1,2],
         [0,0,0,1]].

This is integral upper-unitriangular of rank four.
Its strict-upper squared-entry sum is E=2q+9, its maximum entry magnitude is n+1, and its cycle product is -4q.
Equation(1) gives

    P_n(t):=det(tV_n+V_n^T)
       =t^4+(2q-5)t^3+(q-2)^2 t^2+(2q-5)t+1.              (3)

Thus the neutral multiplier C is exactly1, of degree zero.
No eigenvalue selection, deleted factor or scalar normalization occurs.
The reciprocal trace form is

    P_n(t)=t^2 Q_q(t+t^(-1)),
    Q_q(u)=u^2+(2q-5)u+(q-2)^2-2,
    disc(Q_q)=17-4q<0.                                    (4)

In particular none of the four roots of P_n is real or on the unit circle, since either property would make t+t^(-1) real.
There are exactly two expanding complex-conjugate roots and their two contracting reciprocals.
This is a nontorsion reciprocal unit family, not a Salem family.

Every P_n is irreducible over Q.
By monicity and Gauss's lemma, any proper rational factorization can be made monic integral.
A linear factor would have root1 or-1, but

    P_n(1)=q^2-4>0,
    P_n(-1)=(q-4)^2>0.                                    (5)

The remaining possible factorization is into two monic integer quadratics.
Their constant terms must either both be1 or both be-1.
In the first case they are(t^2+r t+1)(t^2+s t+1), forcing r+s=2q-5 and rs=(q-2)^2-2.
The discriminant of this real quadratic pair is17-4q<0, impossible for integers r,s.
In the second case(t^2+r t-1)(t^2+s t-1) has opposite t^3 and t coefficients.
They cannot both equal2q-5, which is nonzero.
This proves irreducibility and covers every rational factorization case.

The construction genuinely leaves the whole real block-Gram determinant class.
For any real rectangular B, the fixed L175 calculation says every root other than-1 of the block-bipartite determinant has real trace t+t^(-1)=sigma_j(B)^2-2.
The roots in(4) cannot occur in such a polynomial.
Thus P_n cannot even divide one of those block determinants, including after multiplication by any cyclotomic product.
Nevertheless(3) realizes it directly in the required upper-unitriangular class.
The new fact is this exact realized family, not the previously known necessary real-trace condition.

For the first example n=2,q=6,

    V_2=[[1,2,0,-2],[0,1,3,0],[0,0,1,2],[0,0,0,1]],
    P_2=t^4+7t^3+16t^2+7t+1,
    Q_6=u^2+7u+14,       disc(Q_6)=-7.

It is an explicit irreducible reciprocal test input outside the L191 trace subclass, with no stabilization.
Its endpoint square P_2(-1)=4 is necessary but is not used as a sufficiency argument; the displayed matrix supplies the realization.

<a id="same-support-ordering-polynomial-change"></a>
### 3. Bipartite support is not the block-order hypothesis

The two graph classes of the four-cycle are{1,3} and{2,4}.
If the same signed weights are placed in the order1,3,2,4 and then reoriented to upper-triangular form, the corresponding block matrix is

    W_n=[[I_2,B_n],[0,I_2]],
    B_n=[[2,-n],[n+1,2]].

This is another legitimate integral upper-unitriangular matrix, but it is not asserted to be a permutation congruence of V_n.
Its Gram matrix has

    tr(B_n^T B_n)=2q+9,
    det(B_n^T B_n)=(q+4)^2,
    (B_n^T B_n)_(12)=2.

The retained block determinant formula consequently gives

    det(tW_n+W_n^T)
       =t^4-(2q+5)t^3+(q+2)^2 t^2-(2q+5)t+1.              (6)

Its trace polynomial has discriminant4q+17>0, unlike(4).
Equations(3) and(6) differ already in their t^3 coefficient, so no integral congruence preserving the full determinant has been performed by this reorientation.
Merely knowing that the support graph is bipartite does not put an arbitrary ordered upper-unitriangular presentation into L175's block class.
This is an exact all-parameter distinction, not a numerical comparison of a few eigenvalues.

<a id="interlaced-quartic-total-mahler-cost"></a>
### 4. The complete original and absolute-cover measures

The original measure can be written exactly.
Let R>1 be the modulus of an expanding root of P_n, and write that root R exp(i theta).
The root set is

    R exp(i theta), R exp(-i theta),
    R^(-1) exp(i theta), R^(-1) exp(-i theta).

Put a=2q-5, b=(q-2)^2 and X=R^2+R^(-2)>2.
Multiplication of the two real quadratic factors gives

    a=-2 cos(theta)(R+R^(-1)),
    b=R^2+R^(-2)+4 cos(theta)^2.

Eliminating cos(theta) yields

    X^2+(2-b)X+a^2-2b=0.

At X=2 this quadratic is17-4q<0, so its two real roots straddle2 and the actual X is the larger one.
Its discriminant is

    (b+2)^2-4a^2=P_n(1)P_n(-1)=(q^2-4)(q-4)^2.

Consequently

    X_q=[(q-2)^2-2+(q-4)sqrt(q^2-4)]/2,
    m(P_n)=2 log R=arcosh(X_q/2).                           (7)

This accounts for both expanding roots, not only the modulus of one.
All roots are off the unit circle by(4), and no leading coefficient term is missing because P_n is monic.

Equation(2) gives the complete absolute factor

    R_n(t):=p_(V_n^-)(t)
       =t^4-(6q+5)t^3+(q-2)^2 t^2-(6q+5)t+1.              (8)

Its real trace roots are

    u_plus=[6q+5+sqrt(32q^2+76q+17)]/2,
    u_minus=[6q+5-sqrt(32q^2+76q+17)]/2.                   (9)

Both are positive: their sum is6q+5 and product q^2-4q+2>0.
The trace polynomial at2 is q^2-16q-4.
For n=2,3 the values q=6,12 make this negative, so0<u_minus<2<u_plus.
For n>=4, q>=20 makes it positive; since2 lies below the vertex(6q+5)/2, one has2<u_minus<u_plus.
Therefore the whole added measure is exactly

    m(R_n)=arcosh(u_plus/2)                       if n=2,3;
    m(R_n)=arcosh(u_plus/2)+arcosh(u_minus/2)      if n>=4.  (10)

The first case retains the two unit-circle roots and the second retains both positive expanding roots.
No trace branch at2 or-2 has been discarded: none occurs for these integer parameters.
The formula is consistent with L185's positive-cost necessity and supplies the full value rather than merely that theorem's lower bound.

D9's explicit signed double cover gives an all-negative integral upper-unitriangular matrix of rank eight whose full polynomial is P_n R_n.
Thus its total logarithmic measure is exactly the sum of(7) and(10); the extra cost is(10).
Its maximum strict-upper entry is still n+1 and its squared-entry sum is2E=4q+18, since each original edge is lifted to two equal-magnitude edges.
The realization of P_n itself uses no added cyclotomic factor, while this cover adds the explicitly noncyclotomic factor R_n with its accounted positive measure.

For quantitative scope, X_q/q^2 tends to one, and u_plus/q,u_minus/q tend to3+2sqrt(2),3-2sqrt(2), respectively.
Hence

    m(P_n)=2 log q+o(1),
    m(R_n)=2 log q+o(1),
    m(R_n)/m(P_n) -> 1.

This gives a controlled asymptotic cost in the displayed growing-measure family, not an optimized global cost theorem.
In particular m(P_n) tends to infinity, approximately4 log n.
Fixed degree, integral entries and a favorable asymptotic ratio here do not address the unrestricted near-one regime.

### 5. Checks, contribution and remaining coverage

The coordinator supplied only the broad question.
This agent derived the weighted four-cycle specialization, irreducibility, interlaced/block-order comparison and complete measure formulas.
The matching expansion, real block determinant restriction and signed double-cover construction are explicitly reused at their retained scopes.
No new external theorem or historical novelty assertion is needed.

Author checking included every nonzero determinant-permutation type in(1), the absolute-cycle sign, both endpoint evaluations, the complete integral quartic factorization alternatives, the trace-root obstruction and root multiplicities, the actual block reorientation and Gram entries, elimination of the expanding modulus with its correct larger root, both regimes in(10), full cover dimension/energy and all asymptotic branches.
These are direct exact identities and inequalities; no numerical roots, finite sample extrapolation or continuing program is used, and no J is required.
Complete noncontributor review remains pending.

The result gives an actual infinite reciprocal irreducible family beyond L191 even though its support graph is a four-cycle.
It does not supply a procedure for an arbitrary reciprocal polynomial, a near-one target family or a universal controlled cover.
The next constructive discriminator would have to extend interlaced signed cycles to independently prescribed higher-degree coefficients or identify what arithmetic restrictions remain under such ordered integral constructions and neutral stabilization.
The demonstrated ordering freedom removes one restricted-class barrier; it does not remove the full unrestricted coverage obligation.
G0001 remains active and unresolved.



The original `Yin_R_G0095_v1#interlaced-quartic-independent-review` checked this complete proof on2026-10-10; its exact whole scope, original arrangement and contribution/source/nonexecution limits remain in [R682's mathematical comparison](../audits/reviews/Yin_R_G0682_v1.md#l196-and-r95).

## Retention and review bindings

The original day-precision review covered the entire [retained proof](#retained-interlaced-realization-proof), including the full determinant, irreducibility cases, nonreal-trace restriction, actual ordering change, complete measures and all costs.
The reviewer assigned the question but supplied none of the derivations.
The [new R682 whole finding](../audits/reviews/Yin_R_G0682_v1.md#interlaced-quartic-isolated-whole) supplies current independently checked coverage of the exact C470 proof and all original root/cost branches.

The complete D G0065 argument and necessary original review facts retain their actual scopes and SELF/UNKNOWN boundaries.
This is proof retention, not Task completion.
