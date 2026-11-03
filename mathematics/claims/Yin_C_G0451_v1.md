---
author: Yin
---
# Complete trace-order norm symmetries, quartic optima and all root costs

The complete original L261 mathematical proof, equations1--16 and5a, and both fully charged controls are retained here.
L261 preserves substantive exploration, original formal-degree wording qualification, contribution/freeze/checking and fixed old review inputs.
No Task/E execution resumes.

## Statement

Let P be the ACTUAL monic irreducible reciprocal nontorsion unit polynomial of degree d=2s, P(0)=1, and P=t^s Q(t+t^-1).
For an original root alpha, tau=alpha+alpha^-1 has ACTUAL irreducible degree-s polynomial Q in Z[x]; use the actual trace order O=Z[tau] in K=Q(tau).
For EVERY nonzero V in Z[x] of degree<s set

    C_V=t^(s-1)(t^2-1)V(t+t^-1),
    c=cont(V)=cont(C_V)>0, E(V)=S_2(C_V)^2,
    Delta(V)=(1/d)log|Res(P,C_V/c)|-log S_2(C_V/c).

These are EXACTLY the integral polynomials anti-reciprocal at FORMAL degree d, with actual degree/monomial drops retained.
Every such nonzero C_V avoids EVERY original root, and

    Res(P,C_V)=P(1)P(-1)Res(Q,V)^2,
    E(V)=integral_(-2)^2(4-x^2)V(x)^2 dx/[pi sqrt(4-x^2)].

An ACTUAL field automorphism sigma of K preserving O as a SET acts by an integral unimodular coordinate map on V.
Its reduced degree-below-s representative V^sigma has the same content, same signed trace norm and same ENTIRE signed original resultant.
It need not preserve each LABELED original p-adic depth; no Galois or lift-to-Q(alpha) assumption is imposed.
For EVERY explicitly exhibited actual-order unit epsilon, the reduced representative V^epsilon of epsilon V(tau) also has the same content and ENTIRE signed original resultant; its trace norm changes only by Norm(epsilon)=+/-1.
This unit map preserves EACH original root's valuation at EVERY rational prime separately, as epsilon and its inverse are integral.
For either permitted transformation,

    Delta(V_new)-Delta(V)=(1/2)log[E(V)/E(V_new)].

All actual coefficients/degrees/support/leading and auxiliary-root costs are recomputed and retained.
Nontrivial automorphisms, small units, useful energy decrease, bounded transformation height and input-uniform near-one coverage are not automatic.

For EVERY actual irreducible reciprocal nontorsion quartic P=t^4-a t^3+b t^2-a t+1, a,b in Z, including complex trace fields, Q=x^2-a x+(b-2) and EVERY nonzero integer pair(u,v),

    C_V=u t^4+v t^3-v t-u, V=u x+v,
    E=2(u^2+v^2), Res(Q,V)=(b-2)u^2+a u v+v^2,
    Res(P,C_V)=[(b+2)^2-4a^2][(b-2)u^2+a u v+v^2]^2.

The order involution followed by overall sign sends(u,v) to(u,-a u-v), preserves content/full norm and has exact energy change2a u(a u+2v).
The u0 case is included: C_V=v(t^3-t) has actual degree3 but remains anti-reciprocal at FORMAL degree4.
Put

    D=(b-3)^2+a^2, rho=(|b-1|+sqrt(D))/2>0,
    W=|(b+2)^2-4a^2|>0.

Over ALL primitive integral auxiliaries in this FORMAL-degree4 class, the exact supremum is

    sup Delta=(1/4)log W+(1/2)log(rho/2).

It is attained by an actual primitive integer pair IF AND ONLY IF D is a square integer, including the scalar/equal-absolute-eigenvalue cases.
No coefficient-height bound is supplied for the approximating primitive sequence.
This class is not the union of anti-reciprocal classes defined at their separate actual degrees<=4.

For the actual fixed quartic P=t^4-t^3-t^2-t+1,Q=x^2-x-3, the genuine adjacent j4 primitive pair(8,-7), raw content32, is reflected to(8,-1):

    C_new=8t^4-t^3+t-8,
    Res(Q,8x-1)=-199, Res(P,C_new)=-118803=-3*199^2,
    E_old=226, E_new=130,
    Delta_new=(1/4)log(118803/16900)>0.

Energy130 is the GLOBAL integer minimum for that fixed FULL original norm in the ENTIRE primitive formal-degree4 class, including actual degree drops.
The improvement is exactly(1/2)log(226/130), and effective support decreases from450/113 to162/65.
Both full auxiliaries have all four roots on the circle and leading coefficient8, hence full Mahler cost log8.
The overall all-norm supremum is unattained because D17 is not square and exceeds this fixed-norm minimum's margin by

    (1/2)log[65rho/199]
      =(1/2)log[1+1/{398(65sqrt17+268)}]>0,
    17*65^2-268^2=1.

All original prime/root depths are retained: at199 the selected simple trace root changes from7/8 to1/8, so exactly the two inverse original-root labels with depth1 exchange with the two depth0 labels.
At3 the same original pair retains depth1/2 and the other pair depth0; every other primitive prime depth is0.
The unchanged raw content32 contributes dyadic depth5 at EVERY original root and is removed entirely by primitive normalization.
Norm preservation is not mislabeled as depth preservation for this automorphism step.

The ACTUAL order unit epsilon=tau+1 has inverse tau-2 and norm-1.
Its matrix and integral inverse are

    T=[[2,1],[3,1]], T^-1=[[-1,1],[3,-2]].

For the different genuine adjacent j3 control, raw content6, it sends(3,-17) to(-11,-8), then overall sign gives(11,8):

    C_old=(t^2-1)(3t^2-17t+3),
    C_new=(t^2-1)(11t^2+8t+11),
    Res(Q,3x-17)=211, Res(Q,11x+8)=-211,
    Res(P,C_old)=Res(P,C_new)=-133563=-3*211^2,
    E_old=596, E_new=370.

EVERY labeled local depth is preserved by the actual p-adic unit multiplier, and content6 remains before primitive division.
The old exterior reciprocal auxiliary pair has full Mahler cost log[(17+sqrt253)/2]; the new all-circle auxiliary has full leading cost log11, strictly smaller.
Despite the energy/root improvement, Delta_new=(1/4)log(133563/136900)<0 remains negative.
No minimum370, full unit-orbit optimization or positive-margin success is asserted.

For actual centered windows j,j+h with j>=d-1 and integer h>=1, the separated identity1 is integral/anti-reciprocal at formal degree d+2h-2.
Its full additional2h-2 degree is charged; when that exceeds d it has no automatic nonzero/nonvanishing guarantee.
Along ANY hypothetical total-m(P)->0 sequence of actual inputs, the ENTIRE original-degree time-two cyclic cost tends to0.
An automorphism fixes primitive constant trace V, and unit multiplication can make it nonconstant but leaves absolute trace norm1 and coefficient energy>=2.
Thus these operations alone still give margin at most-(1/2)log2+o(1), and cannot manufacture missing arithmetic income from the forced cyclic factor.
No uniform existence of useful symmetries/units, least joint-conjugate expense, near-one family or unrestricted gap is proved.
L237's separately established universal scalar margin remains established and is not treated as a missing premise.

<a id="argument"></a>
## Complete argument

### Adequate actual trace, finite-control and cyclic-cost inputs

The complete original final mathematical Sections1--6/equations1--16 and5a follow without abridgment.
The original Section7 review-prompted formal-versus-actual-degree qualification and author self-check remain in L261 and its formal review account; they are not relabeled as a new repair or isolated present review.
Their2026-10-10 Task-active/pre-adoption language is chronology, not execution authority.

The complete integral anti-reciprocal trace parametrization, both-way content equality, signed full resultant with BOTH roots above each trace, exact weighted energy and primitive normalization are sufficiently proved in [C438](Yin_C_G0438_v1.md#argument).
Its actual adjacent-window edges/scales and all degree/cancellation/nonvanishing hypotheses are the exact inputs to the separated identity below.
The original full J57 payload's quartic j3 and j4 rows (`mathematics/computations/outputs/Yin_J_G0057/verification.json`) supply only the inherited primitive pairs(3,-17),(8,-7), contents6/32 and complete original norms/energies.
Both complete rows were statically read; all new transformed values follow from the displayed integer maps/products/comparisons.
No author program, new window, machine scan or new J57 replay is performed here.

The exact [C391 original-degree cyclic-cost proof](Yin_C_G0391_v1.md#bounded-power-degree-escape) is sufficient at n2<=2d, including norm towers and powered-degree drops.
For even d the literal product P(1)P(-1)=product_i(alpha_i^2-1) is the FULL original-field time-two norm, so its normalized logarithm tends to0 along the stated hypothetical sequence.
This uses only the already accepted Pri11 statement scope inside that complete proof, without a source-proof audit or finite enumeration.
No new source theorem or mathematical program is required.

<a id="trace-norm-symmetry-reuse"></a>
### 1. Changed question, reuse and actual scope

Date:2026-10-10.
This argument is authored by the resultant-research agent for Yin.
The current Task, S4/S8 and relevant repository rules are retained from the preceding coordinated round and checked against this assignment.
Root supplies the question and coordination, not a proof step; its simultaneous Blaschke coefficient-moment argument is neither a premise nor a contribution here.
No new execution allowance is created.

The direct inputs are [L257's complete anti-reciprocal trace norm, energy and primitive normalization](../ledger/Yin_L_G0257_v1.md#adjacent-edge-trace-factor-cost), its [quartic actual coupled control](../ledger/Yin_L_G0257_v1.md#adjacent-edge-quartic-positive-control), and [L237's already established universal scalar margin](../ledger/Yin_L_G0237_v1.md#monomial-projection-uniform-margin).
The latter is not an unsolved existence question.
A bounded local G-ledger and registry search for separated windows, anti-reciprocal auxiliaries, trace energy, trace-field symmetry and coefficient-norm optimization found the stated L257 interface but no retained optimization of its single trace norm under integral trace symmetries.
The L56/L241 full-matrix determinant optimization and L245 full-space quadratic-root bound concern different objects; their earlier reuse correction remains in force.
The following norm identities, integral changes and two-variable quadratic optimization are direct calculations using these adequate inputs.
No new external theorem, source artifact or literature-novelty claim is adopted.

For orientation, separating centers j and j+h, h>=1, directly gives

    [A_(j+h) B_j-t^(2h)A_j B_(j+h)]/P
       =F_(j+h) B_j-t^(2h)F_j B_(j+h),
    degree <=d+2h-2.                                (1)

It is integral and anti-reciprocal at formal degree d+2h-2, but it need not be nonzero or avoid original roots when its degree exceeds d.
Thus separation alone is not free: it adds2h-2 degrees and loses L257's degree-d automatic nonvanishing argument.
The substantive changed test here instead keeps degree at most d and the COMPLETE actual norm fixed while changing the trace-coefficient energy.
It can be applied after a coupled window produces an auxiliary, without a new window or enlargement of its degree bound.

Throughout, P is the actual monic irreducible reciprocal nontorsion unit polynomial of degree d=2s, P(0)=1, and

    P(t)=t^s Q(t+t^(-1)),   Q in Z[x] monic, deg Q=s.

For an original root alpha, tau=alpha+alpha^(-1) has minimal polynomial Q: its degree is at most s by this equation and at least s because alpha has degree2s and solves t^2-tau t+1 over Q(tau).
Thus Q is irreducible.
Every trace root corresponds to exactly two inverse original roots, including every embedding and all nonarchimedean multiplicities.
There are no original roots at+/-1.

<a id="integral-trace-symmetry-full-norm"></a>
### 2. Norm-preserving integral changes in the actual trace order

For V in Z[x], 0<=deg V<s, define

    C_V(t)=t^(s-1)(t^2-1)V(t+t^(-1)).                (2)

The zero polynomial is excluded.
By L257, these are exactly the integral anti-reciprocal polynomials at formal degree d.
Actual monomial and degree drops are allowed: if deg V=r, the first and last nonzero exponents of C_V are s-1-r and s+1+r.
Since V is nonzero of degree below that of the irreducible Q, C_V avoids every original root.
Its content is exactly cont(V), and its COMPLETE norm and coefficient energy are

    Res(P,C_V)=P(1)P(-1)Res(Q,V)^2,
    E(V):=S_2(C_V)^2
       =integral_(−2)^2 (4-x^2)V(x)^2 dnu(x),
    dnu(x)=dx/[pi sqrt(4-x^2)].                      (3)

These are the retained identities, not another project proof of them.

Let K=Q(tau), and let sigma be a field automorphism of K that preserves the ACTUAL trace order O=Z[tau] as a set.
This is a stated condition, not a property imposed on every input.
In the integral basis1,tau,...,tau^(s-1), sigma has an integral matrix T; sigma^(-1) preserving the same order gives an integral inverse.
Thus T is unimodular.
Write V^sigma for the unique polynomial of degree below s representing sigma(V(tau)) in that basis.
Then

    cont(V^sigma)=cont(V),
    Res(Q,V^sigma)=Res(Q,V),
    Res(P,C_(V^sigma))=Res(P,C_V).                   (4)

For content, an integer divides every coordinate before the transformation if and only if it divides every coordinate after it, using both integral matrices.
For the norm, composition with sigma permutes the s embeddings of K into an algebraic closure; the product of V(tau) over these embeddings is unchanged.
This proves(4) without assuming K is Galois or sigma lifts to an automorphism of Q(alpha).
All d original roots still occur in the last product in(3).
At each rational prime, every original valuation remains finite and nonnegative after primitive normalization.
The total valuation of the full norm is preserved; its distribution among labeled original roots need not be preserved, because the factor alpha^2-1 remains attached to the original trace while the V value is permuted.
No independently cheap prime certificates are merged.

If c=cont(V) and Delta(V) denotes the normalized resultant-minus-coefficient margin of C_V/c, then

    Delta(V^sigma)-Delta(V)
                    =(1/2)log[E(V)/E(V^sigma)].     (5)

Thus any energy reduction is a genuine improvement at exactly the same full signed norm and the same degree upper bound.
Primitive normalization cancels from both sides.
The leading coefficient, actual degree drop, effective support and exceptional roots may change and remain part of the actual new polynomial; none is held fixed by(4).
Taking the identity transformation is always available, so a finite inspected set of such symmetries can improve energy or leave it unchanged.
Nontrivial symmetry, a useful reduction, a height bound for T and uniform near-one improvement are not automatic.
In particular many irreducible trace fields have no such nontrivial automorphism; no coverage theorem is hidden here.

The same exact margin comparison has a useful larger domain.
If epsilon is any exhibited unit of O, multiplication by epsilon on O has an integral inverse and hence is another unimodular change of the coefficient vector.
Its field norm is+/-1.
For the unique reduced polynomial V^epsilon of degree<s representing epsilon V(tau), content is unchanged and Res(Q,V^epsilon)=Norm(epsilon)Res(Q,V), so the COMPLETE signed original resultant in(3) is still unchanged.
Equation(5) applies with V^epsilon in place of V^sigma.
Furthermore every original nonarchimedean root depth is individually preserved under this multiplication: at that trace embedding, epsilon and its inverse are algebraic integers, so both have nonnegative valuation and v_p(epsilon)=0.
Therefore

    v_p(C_(V^epsilon)(alpha_i)/cont(V))
                    =v_p(C_V(alpha_i)/cont(V))     (5a)

for every rational prime and EVERY original root.
All original roots and their inverse partners are retained.
Unlike the automorphism case, no root-label permutation is needed.
Reducing epsilon V modulo the monic Q keeps the representative integral and its degree below s; one does not keep an uncharged high-degree product.
The auxiliary's full coefficient energy, leading coefficient and complex root locations can nevertheless change.
Only an explicitly exhibited actual-order unit is used: no Dirichlet-unit theorem, uniform small fundamental unit or access to all unit orbits is assumed here.

<a id="quartic-trace-reflection-and-optimum"></a>
### 3. Complete quartic formula and a reversible energy reduction

Now let the ACTUAL input be any irreducible reciprocal nontorsion quartic

    P=t^4-a t^3+b t^2-a t+1,
    Q=x^2-a x+(b-2),      a,b in Z.                 (6)

This includes the allowed complex trace case; no Salem root distribution is assumed.
The quadratic trace involution tau maps to a-tau preserves Z[tau].
For V=u x+v, (u,v) in Z^2\{(0,0)}, combine that involution with multiplication of V by-1 to obtain

    (u,v) maps to (u,-a u-v).                       (7)

The map is an integral involution of determinant-1.
The extra sign does not alter the quadratic trace norm or the full original resultant, and preserves content.
Equations(2)--(3) specialize to

    C_V=u t^4+v t^3-v t-u,
    S_2(C_V)^2=2(u^2+v^2),
    Res(Q,V)=(b-2)u^2+a u v+v^2,
    Res(P,C_V)=[(b+2)^2-4a^2]
                    [(b-2)u^2+a u v+v^2]^2.        (8)

The formula includes u=0: then C_V=v(t^3-t), so its actual degree is3 and its monomial factor is retained.
All nonzero integer pairs yield nonzero resultants, by irreducibility of Q.
The scalar [(b+2)^2-4a^2]=P(1)P(-1) is nonzero, with its sign kept.
The energy change in(7) is exactly

    E(new)-E(old)=2a u(a u+2v).                     (9)

This provides a direct strict-improvement criterion, rather than an unquantified choice of another basis.
It does not alter an auxiliary matrix determinant while ignoring a full Gram cost: it changes one actual polynomial and preserves its scalar field norm for the arithmetic reason in(4).

There is also a complete optimal upper bound for ALL primitive integral anti-reciprocal polynomials of formal degree4 on this input, not just the pairs generated by adjacent windows.
Put

    B=[[b-2,a/2],[a/2,1]],
    D=(b-3)^2+a^2,
    rho=(|b-1|+sqrt(D))/2>0,
    W=|(b+2)^2-4a^2|.                               (10)

Then their net margins have the exact supremum

    sup Delta(V)=(1/4)log W+(1/2)log(rho/2).         (11)

Indeed the quadratic norm in(8) is z^T B z for z=(u,v).
The two real eigenvalues, found by the degree-two characteristic equation, are (b-1+/-sqrt(D))/2, with largest absolute value rho.
Orthogonal diagonalization, or completing the corresponding real squares, gives |z^T B z|<=rho||z||^2, and equality at an eigenvector of eigenvalue with absolute value rho.
Substitution in the complete margin from(8) proves the upper bound in(11).
Rational directions approximate an optimizing real eigenvector; after clearing denominators and dividing the coefficient gcd they give primitive integer pairs with the same homogeneous ratio and converging margins.
Thus it is the supremum over actual primitive integral auxiliaries, with no coefficient-height bound claimed for the approximating sequence.

The supremum is attained by such a pair if and only if D is a square integer.
If D is square, the optimizing eigenvalue and a corresponding nonzero eigenvector can be chosen rational; this includes scalar B when D=0.
If D is not square, then a!=0 (otherwise D=(b-3)^2), and a rational nonzero optimizing vector would force its eigenvalue rational from either nonzero coordinate of Bz=lambda z, contrary to the displayed eigenvalues.
When both eigenvalues have equal absolute value, equality in the absolute quadratic bound still requires one of their eigenspaces, unless B is scalar, which has already been covered.
This proves both directions without mistaking a real optimum for attained integral data.
The proof supplies a full parametrized quartic conclusion; it is not an unrestricted-degree or near-one theorem.


<a id="quartic-fixed-norm-energy-minimum"></a>
### 4. The coupled quartic positive norm has an exact integer energy minimum

Take the retained actual quartic P=t^4-t^3-t^2-t+1, so a=1,b=-1,Q=x^2-x-3.
L257's genuine adjacent j=4 output has primitive trace pair(u,v)=(8,-7), content32 before normalization, full signed original norm-118803=-3*199^2, and energy226.
Applying(7) yields(u,v)=(8,-1), hence the ACTUAL primitive auxiliary

    C_new=8t^4-t^3+t-8=(t^2-1)(8t^2-t+8),
    Res(Q,8x-1)=-199,
    Res(P,C_new)=-118803,
    S_2(C_new)^2=130,
    Delta_new=(1/4)log(118803/16900)>0.              (12)

Its improvement over the retained coupled output is exactly(1/2)log(226/130).
The full resultant is identical, not a newly added prime contribution.
The effective support S_1^2/S_2^2 decreases from450/113 to162/65.
Both auxiliaries have all four roots on the circle and leading coefficient8, so their actual Mahler measure remains log8; the energy improvement is not justified by deleting that leading cost.

This particular improvement is globally optimal for its fixed norm inside the ENTIRE primitive integral class satisfying anti-reciprocity at FORMAL degree4, namely t^4 C(1/t)=-C(t); its actual degree may drop.
This is not the union of ordinary anti-reciprocal classes defined at each actual degree at most4.
In the stated formal-degree4 class (8) shows that original resultant-118803 requires

    |-3u^2+u v+v^2|=199.

Here rho=(2+sqrt17)/2.
If the positive integer u^2+v^2 were at most64, the absolute quadratic form would be at most64rho=64+32sqrt17<199: the last strict inequality follows from17<(135/32)^2.
Therefore u^2+v^2>=65, and(8) forces energy at least130.
The primitive pair(8,-1) attains equality.
This proves an integer minimum over all such polynomials with the specified FULL original norm, not only over the two reflection choices or the old windows.

The overall unrestricted-height supremum(11), in contrast, is NOT attained on this quartic because D=17 is not square.
There is no conflict: optimizing one exact norm and optimizing over all norms are distinct problems.
Its supremum exceeds(12) by the exact positive amount

    (1/2)log[65rho/199]
      =(1/2)log[1+1/{398(65sqrt17+268)}].            (13)

Indeed17*65^2-268^2=1.
This identity is only an exact comparison of the two optimization domains, not a claim of optimality among all integer auxiliaries without the anti-reciprocal degree restriction.

All rootwise costs can be retained without an additional computation.
The new trace factor8x-1 vanishes modulo199 at the trace root1/8, whereas the old factor8x-7 selected the trace root7/8.
Since Q has discriminant13, these are distinct simple roots modulo199; Q(1/8)=Q(7/8)=-199/64.
Thus precisely the other pair of original roots acquires depth1 at199, with the first pair now at depth0.
The factor t^2-1 remains a199-adic unit at all original roots.
At3, both linear trace factors are units at both trace roots0,1, so the original pair over trace1 still has depth1/2 from t+1, and the other pair has depth0.
Every other prime has total norm valuation zero and hence all four depths zero.
The transformation of the raw content32 output retains content32, so raw dyadic depth5 is again removed entirely by primitive normalization.
This accounts for every original root and prime, while explicitly distinguishing preserved norm from unchanged labeled depth in an automorphism step.
The input has fixed positive total measure and degree four; it is not a near-one sequence.

<a id="actual-trace-unit-removes-auxiliary-exterior-pair"></a>
### 5. A trace unit changes the roots and every coefficient cost without changing local income

On the same actual trace order, tau^2=tau+3.
The element epsilon=tau+1 is a unit with inverse tau-2, since (tau+1)(tau-2)=1.
Its norm is-1.
Multiplication by epsilon sends

    (u,v) to (2u+v,3u+v),
    T=[[2,1],[3,1]],    T^(-1)=[[-1,1],[3,-2]].     (14)

This is an exhibited actual-order unit, so the entire statement(5a) applies.
Take the other retained coupled output, j=3 in L257, whose primitive trace pair is(3,-17), content6 before normalization and full signed resultant-133563=-3*211^2.
Applying(14), and then the harmless overall sign-1, gives the primitive pair(11,8):

    C_old=(t^2-1)(3t^2-17t+3),
    C_new=(t^2-1)(11t^2+8t+11),
    Res(Q,3x-17)=211,
    Res(Q,11x+8)=-211,
    Res(P,C_old)=Res(P,C_new)=-133563,
    E_old=596,       E_new=370.                     (15)

No local income is moved between original roots: at every p and every alpha_i the multiplier is the p-adic unit-epsilon at its actual trace embedding.
Both polynomials have content one, and applying the same map before primitive division retains content6.
All real and nonarchimedean factors in(15) are charged.

The old quadratic auxiliary factor has an exterior reciprocal pair with trace17/3>2.
Its full Mahler measure is log[(17+sqrt253)/2].
The new factor has trace-8/11 in(-2,2), so all its roots, together with+/-1, are on the circle and its full Mahler measure is log11.
This is a genuine decrease, since sqrt253>5.
It is attained by changing the actual polynomial in the same norm/depth class, not by dropping its original exterior roots from an estimate.
Despite both the improved energy and removed exterior pair, the new net margin is STILL negative:

    Delta_new=(1/4)log(133563/136900)<0,
    136900=370^2.                                   (16)

The improvement relative to the old margin is(1/2)log(596/370).
No assertion is made that (14), one step, or370 is minimal over the full unit orbit for this different norm.
This control is deliberately retained as a failed positive-margin attempt with exact useful improvement, rather than enlarged into a search until a favorable result appears.

<a id="trace-norm-symmetry-unresolved-near-one-scope"></a>
### 6. Actual consequence and unresolved unrestricted cost

The changed result is a norm-preserving transformation principle in the actual trace order, a parametrized exact quartic optimum including its integral attainment boundary, and two fully charged consequences for genuine coupled outputs.
One gives the global integer energy minimum130 at a specified complete norm within the formal-degree4 anti-reciprocal class, including its actual degree drops.
The other preserves every labeled nonarchimedean depth while removing an exterior auxiliary pair, yet still fails to obtain positive net income.
No new J was required: the only inherited numerical inputs are the exact L257/J57 coupled coefficients, and every new value is reproduced by the displayed two-by-two integer maps, products and integer comparisons.
This is direct proof, not an unrecorded larger enumeration.

The construction provides no uniform availability of nontrivial trace automorphisms, of small units, or of energy reduction on the general reciprocal near-one core.
It also does not show that minimizing energy within such an orbit controls the full joint original-conjugate estimate.
A unit can have large coefficients and may initially increase energy; that expense is carried by its actual reduced representative.
The full original norm in(3), its forced time-two factor and every remaining trace cofactor remain present.

In particular constant V is fixed by every field automorphism, so automorphism reduction cannot repair L257's constant-trace cyclic collapse.
Multiplication by a unit can make V nonconstant, but its absolute trace norm remains1.
Since a nonzero primitive integral anti-reciprocal polynomial has energy at least2, L168/L257 then still give net margin at most-(1/2)log2+o(1) along a hypothetical total-m(P)->0 sequence.
Thus neither operation can manufacture arithmetic norm income from the short cyclic factor on that near-one domain.
A useful improvement must begin with a genuinely sufficient complete trace norm and change its actual joint expense, or use a different construction with all costs proved.

L237's separate universal scalar-margin theorem remains established.
This draft does not count that existence as missing, claim a new general small-Mahler family, replace total measure by height per degree, or discard the cost2h-2 in separated-window formula(1).
Actual nonconstant trace factors, separated windows, other nonlinear edge operations and their full arithmetic/archimedean correlations remain active parallel questions.
G0001 is unresolved.



### Actual checking and retained qualification

The entire original L261/R160 were read, including the final09:28 qualification and the whole09:29 corrected-scope review.
All original mathematical Sections1--6/equations1--16 and5a are retained with href relocation only.
The old qualification explicitly restricts anti-reciprocity to FORMAL degree4; actual degree drops remain included and the union of smaller own-degree classes is not claimed.
Every order/inverse/content/norm/valuation, real-supremum/rational-attainment, exact fixed-norm minimum, leading/root cost and near-one step was checked against the actual C438/C391 mechanisms and two inherited full native rows.
No program/native/PDF/source-proof operation or Task/E execution occurred.
R160's original mathematical pass and review-prompted clarification remain unchanged; the exact content and initial timing of its reportedly available progress summaries are not established.
Its whole relationship remains historical UNKNOWN, and this maintaining-agent SELF check does not supply fresh isolation or discharge any distinct post-qualification review obligation.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:56 |
| status | open |
| reason | Retain the complete original trace-order/unit/full-norm/root-depth theorem, every quartic parameter/supremum/attainment/formal-degree case and both exact signed-norm/energy/root/leading/negative controls, with complete actual trace and original-degree cyclic inputs. The original formal-degree qualification and whole corrected review remain; no producer/source/Task expansion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete theorem](#statement) | Every actual reciprocal nontorsion input/reduced trace/order-preserving automorphism/exhibited unit/original prime-root label, all actual quartic parameters/primitive directions/formal-degree drops, exact two controls/signed norms/energy/leading/root costs and full near-one/coverage limits. |
| argument | [Entire proof](#argument) | Complete final Sections1--6/equations1--16 and5a, all content/integral inverse/full-norm/valuation/spectral/rational-attainment/fixed-norm/prime/root/degree/time-two arguments and retained qualification/source/nonexecution scope. |
| dependency | [Complete actual trace/coupled input](Yin_C_G0438_v1.md#argument) | Actual centered edges/scales, formal anti-reciprocal parametrization/degree/zero/nonvanishing, both-way content, full signed trace norm and weighted energy, original quartic j3/j4 data; no new adjacent-window execution. |
| dependency | [Full original-degree cyclic-cost decay](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Entire original-field n2 norm with powered-degree drops and fixed-input degree escape, accepted Pri11 statement scope only; no new source-proof audit/income/finite enumeration. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0057/readme.md#recorded-runs) | Only actual quartic j3/j4 complete fields, primitive pairs(3,-17)/(8,-7), raw contents6/32, signed norms-133563/-118803 and energies596/226; static read, no new producer or reviewer replay. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0057/verification.json`; this target locates its run account. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:59 |
| status | proved |
| reason | Adopt after the actual whole C451/R656 SELF check of every actual order/trace-degree/nonzero/formal-degree/integral-inverse/content/full-signed-norm/original-root-depth case, complete all-quartic spectral supremum/rational attainment, fixed-norm global integer minimum and both fully charged leading/root/energy/prime/negative controls. The entire original mathematical1--6/1--16 and5a proof, final formal-degree qualification and needed C438/C391/J57 static inputs are retained and checked; no source-proof/producer/search/Task expansion. Original R160 whole UNKNOWN and preliminary qualification/complete corrected rereview remain historical; this SELF adoption supplies no fresh isolation or post-qualification independent coverage. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete theorem](#statement) | Every actual reciprocal nontorsion input/reduced trace/order-preserving automorphism/exhibited unit/original prime-root label, all actual quartic parameters/primitive directions/formal-degree drops, exact two controls/signed norms/energy/leading/root costs and full near-one/coverage limits. |
| argument | [Entire proof](#argument) | Complete final Sections1--6/equations1--16 and5a, all content/integral inverse/full-norm/valuation/spectral/rational-attainment/fixed-norm/prime/root/degree/time-two arguments and retained qualification/source/nonexecution scope. |
| dependency | [Complete actual trace/coupled input](Yin_C_G0438_v1.md#argument) | Actual centered edges/scales, formal anti-reciprocal parametrization/degree/zero/nonvanishing, both-way content, full signed trace norm and weighted energy, original quartic j3/j4 data; no new adjacent-window execution. |
| dependency | [Full original-degree cyclic-cost decay](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Entire original-field n2 norm with powered-degree drops and fixed-input degree escape, accepted Pri11 statement scope only; no new source-proof audit/income/finite enumeration. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0057/readme.md#recorded-runs) | Only actual quartic j3/j4 complete fields, primitive pairs(3,-17)/(8,-7), raw contents6/32, signed norms-133563/-118803 and energies596/226; static read, no new producer or reviewer replay. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0057/verification.json`; this target locates its run account. |
| review | [Actual whole SELF finding](../audits/reviews/Yin_R_G0656_v1.md#trace-order-whole-self-finding) | Complete exact statement/argument/all direct inputs, every trace/order/unit/full norm/labeled depth/quartic/formal-degree/supremum/attainment/fixed-norm/prime/leading/root/near-one/source/negative boundary; original R160 whole UNKNOWN and its qualification remain. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:54 |
| status | proved |
| reason | Adopt R669 after complete coordinator reading of the new isolated whole C451 finding, covering the final formal-degree qualification and entire affected actual-order/content/norm/root-depth/quartic-spectrum/full-control/time-two chain. Preserve R160 whole UNKNOWN, original qualification/whole rereview and author/current SELF, all leading-cost/negative/source/native limits; no unit-orbit or near-one conclusion is added. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every actual reciprocal nontorsion input/reduced trace/order-preserving automorphism/exhibited unit/original prime-root label, all actual quartic parameters/primitive directions/formal-degree drops, exact two controls/signed norms/energy/leading/root costs and full near-one/coverage limits. |
| argument | [Exact argument](#argument) | Complete final Sections1--6/equations1--16 and5a, all content/integral inverse/full-norm/valuation/spectral/rational-attainment/fixed-norm/prime/root/degree/time-two arguments and retained qualification/source/nonexecution scope. |
| dependency | [Exact dependency](Yin_C_G0438_v1.md#argument) | Actual centered edges/scales, formal anti-reciprocal parametrization/degree/zero/nonvanishing, both-way content, full signed trace norm and weighted energy, original quartic j3/j4 data; no new adjacent-window execution. |
| dependency | [Exact dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Entire original-field n2 norm with powered-degree drops and fixed-input degree escape, accepted Pri11 statement scope only; no new source-proof audit/income/finite enumeration. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0057/readme.md#recorded-runs) | Only actual quartic j3/j4 complete fields, primitive pairs(3,-17)/(8,-7), raw contents6/32, signed norms-133563/-118803 and energies596/226; static read, no new producer or reviewer replay. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0057/verification.json`; this target locates its run account. |
| review | [Exact review](../audits/reviews/Yin_R_G0669_v1.md#trace-order-whole-independent-finding) | Complete exact C451v1 Statement and Argument, equations1--16/5a and final formal-degree qualification, all actual-order/root/norm/spectral/full-control/cost/source limits. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0057](../computations/programs/Yin_J_G0057/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
