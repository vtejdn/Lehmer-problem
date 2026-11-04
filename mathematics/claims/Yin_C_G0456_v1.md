---
author: Yin
---
# Complete exterior-square sextic realization, finite three-column and pivot boundaries, and all cover costs

The complete original proof and all unsuccessful-test boundaries are retained here; no research execution resumes.

## Statement

Let p be a monic reciprocal sextic in Z[t].
There exists an integral 6-by-6 bilinear matrix V with det V=1 and V+V^T equal to the specified wedge pairing G, whose only nonzero entries are G05=G50=1, G14=G41=-1 and G23=G32=1, and det(tV+V^T)=p, IF AND ONLY IF p(1)=-1 and p(-1) is an integer square.
The criterion is for this bilinear class with THAT symmetric form; it neither classifies all realizations up to congruence nor asserts an upper-unitriangular presentation.
The square is necessarily positive and odd.
For EVERY a in Z and k in Z_{>=0}, the entire polynomial and an explicit realizing matrix are

    p=t^6+a t^5+[k(k+1)-1]t^4
      -[2a+2k(k+1)+1]t^3+[k(k+1)-1]t^2+a t+1,
    q=x^4-(k+1)x^3-a x^2-k x+1,
    A=the integral companion of q, C=Lambda^2 A,
    V=G(I-C)^(-1)
      =[[0,-1,-k-1,0,-1,0],
        [1,0,a+1,1,0,1],
        [k+1,-a-1,0,k+1,-a-1,k],
        [0,-1,-k,0,-1,0],
        [1,-1,a+1,1,0,1],
        [1,-1,-k,0,-1,0]].

Here the exterior basis is(01,02,03,12,13,23), C^T G C=G, det(I-C)=-1, V+V^T=G and -V^(-1)V^T=C.
No irreducibility, simple-root or positivity hypothesis on q or p is required.
All six diagonal entries of V are zero.
A basis giving six positive unit pivots remains unproved.

Define B=-abs(V) using EVERY matrix entry, and define the 12-by-12 lift W with block x I2 for x=Vij<=0 and -x times the sheet swap for x>0 at EVERY ordered position, also below the diagonal.
The same sheet transform splits W and W^T simultaneously, so their COMPLETE polynomials satisfy p_W=p_V p_B.
Put u=abs(a+1), h=max(k+1,u), and

    L=(2k+1)u-3,
    M=-k(k+1)+(8k+4)u-3,
    R=-2k(k+1)+(12k+6)u-3.
    p_B=-t^6+L(t^5+t)+M(t^4+t^2)+R t^3-1.

The determinants are1,-1,-1, ranks/degrees6,6,12, and all entry heights equal h.
Their WHOLE squared-entry sums are E_all=6k^2+6k+17+4u^2 for V and B and2E_all for W.
These are nontriangular zero-diagonal matrices, so the proper diagonal-one cover theorem is not applied to them.
With all factors and leading coefficients retained,

    m(p_W)=m(p_V)+m(p_B),
    0<m(p_V)<=log720+6log(2h),
    0<=m(p_B)<=log720+6log(2h).

For the actual F=Phi6 P4 control(a,k)=(-2,1), h2, whole energy33 and lift energy66,

    p_B=-[t^6-7t^4-11t^3-7t^2+1].

Its full trace cubic z^3-10z-11 has one root in each(-3,-2),(-2,-1),(3,4), so the absolute factor has two exterior reciprocal pairs and one unit-circle pair.
Its ENTIRE measure is log R_-+log R_+, with1<R_-<(3+sqrt5)/2<R_+<2+sqrt3 and beta4<2, hence the relaxed complete cover costs STRICTLY MORE than2log beta4.
The achieved proper rank6/height1/energy5 Phi2^2 P4 control and its rank12/height1/energy10 Phi2^4 P4^2 cover remain cheaper.
For the actual S6=t^6-t^4-t^3-t^2+1 control(a,k)=(0,0), h1, whole energy21 and lift energy42,

    p_B=-[t^6+2t^5-t^4-3t^3-t^2+2t+1].

The full trace cubic z^3+2z^2-4z-7 has one root in each(-5/2,-12/5),(-2,-1),(1,2); exactly one exterior NEGATIVE reciprocal pair has modulus R, with12/5<R+R^(-1)<5/2 and1<R<2.
The original expanding trace is below9/4, so its relaxed complete cover again costs STRICTLY MORE than twice its original full measure.
No irreducibility of either absolute factor is assumed.

For the conference seed G0, ordered path basis Q0 and three actual norm-two replacements at i<j<k, the determinant of the full basis is EXACTLY the displayed ordered3-by-3 coordinate minor; the separate norm equations and a unit minor are necessary and sufficient in that architecture.
The complete reciprocal coefficients obey p=t6+a t5+b t4+(-3-2a-2b)t3+b t2+a t+1 and Pf(V-V^T)^2=5+4b.
Thus the ENTIRE F requires a=-2,Pf=+/-3, and the ENTIRE S6 requires a=0,Pf=+/-1.
No fixed-four-column all-integer congruence is assumed for the three-column domain.

The first finite statement covers EXACTLY all729 root-cube vectors,114 norm-two roots,57 canonical signs and20*57^3=3703860 ORDERED triples in the FIXED column order, including dependent triples before filtering.
There are1759698 singular,1034514 nonzero nonunit and909648 unit minors;63116 old controls are discarded because an inserted root equals its OWN old column up to sign, leaving846532 genuine basis changes.
Neither complete target nor an even-a congruence escape occurs in that genuine finite class.
Its exact energy range is17--90 and its integer-height bound9 is coarse, not an attained-height assertion; all20 position counts, signed-Pfaffian/energy histograms and all six residue bins remain in J59.
The usual proper companions/covers for those unitriangular candidates retain full rank6/rank12 polynomials and energy doubling.
This finite statement excludes neither larger integer roots nor different orders, and proves no unbounded three-column congruence.

For the separate relaxed F form, the declared tree uses ONLY sign-normalized norm-one pivots in each current cube{-1,0,1}^n, the specified coordinate completion, support-size/lexicographic order and exact-form memoization, with caps20000 calls/120seconds.
It completed6670 calls,4500 duplicates and6669 pivot edges, with unique counts1,87,780,1213,89,0 in dimensions6,5,4,3,2,1,300 first-visited dead forms and maximum intermediate absolute entry86.
All20 saved dead paths are retained; no one-dimensional success or cap occurred.
Equality of whole remaining forms justifies merging only this declared graph.
It is not an all-integer-pivot, all-completion, all-order or all-bilinear-form obstruction.
No achieved proper target, optimized total cost, growing-degree/near-one coverage or unrestricted gap is asserted.
The source boundary remains the already recorded HPM22 conference attribution; no external spin/reflection/classification/triangularization theorem is a premise.

<a id="argument"></a>
## Complete argument

The complete original mathematical Sections1--6/equations1--14 follow, including both predeclared finite algorithms and their actual outcomes.
Their retained pending-review and test-intention sentences describe the original chronological declaration; current status is supplied only by the selected decision below.
Original family labels L254/L258/L246 identify their fixed inputs; their same-scope current proof hrefs use the already complete C429/C442 homes.
L262 itself retains the complete meaningful exploration, author and old review context and unsuccessful-basis gate.

For explicit seed closure use

    G0=[[2,1,1,1,1,1],
        [1,2,1,-1,-1,1],
        [1,1,2,1,-1,-1],
        [1,-1,1,2,1,-1],
        [1,-1,-1,1,2,1],
        [1,1,-1,-1,1,2]].

For C0=G0-2I, direct multiplication gives C0^2=5I and trace C0=0, hence the eigenvalues of G0 are2+sqrt5 and2-sqrt5, each three times.
Thus det G0=-1, signature(3,3), and the even integral lattice is unimodular.
The ordered path columns Q0=(e0,e1-e0,...,e5-e4) have determinant1 and each norm2; H=Q0^T G0 Q0 has diagonal2.
These are precisely the complete seed/endpoint conventions in [C429](Yin_C_G0429_v1.md#argument).

<a id="three-column-construction-and-reuse"></a>
### 1. Reuse and the changed exact construction

[L254](Yin_C_G0429_v1.md#argument) supplies the exact two-column/ordering identities and the locally justified secondary scalar target; [L258](Yin_C_G0442_v1.md#argument) supplies the now-excluded fixed-four-column domain and its exact first-root congruence class.
The seed and its precise HPM22 attribution remain those of [L246](Yin_C_G0429_v1.md#argument).
The [L210 signature interface](../ledger/Yin_L_G0210_v1.md#determinant-two-signature-constraint) was screened as a possible guide but does not itself exclude the determinant-minus-one rank-six target.
A bounded local search for Arf/Brown/stronger coefficient-congruence conclusions did not locate a usable broader theorem; no literature-wide absence or named theorem is claimed.
The following construction uses elementary integer minors, the already proved reciprocal endpoint identity and finite exact arithmetic, so the existing inputs suffice without a new source theorem.

Keep the actual conference Gram G0=2I+C with C^2=5I from L246 and its ordered path basis Q0=(e0,e1-e0,...,e5-e4).
Write H=Q0^T G0 Q0.
For three distinct positions i<j<k choose actual norm-two roots r,s,u in standard coordinates and put c=Q0^(-1)r,d=Q0^(-1)s,f=Q0^(-1)u.
Replace those three columns of Q0 and keep the other three columns fixed, in the same displayed order.
Expansion on the unchanged columns gives

    det Q=det [[c_i,d_i,f_i],
               [c_j,d_j,f_j],
               [c_k,d_k,f_k]].                        (1)

The new columns form an actual standard integral basis exactly when this3-by-3 minor is+1 or-1.
Each replacement must separately satisfy r^T G0 r=s^T G0 s=u^T G0 u=2.
Repeated or dependent inserted roots are therefore automatically rejected by(1); there is no rational-basis relaxation.
Reconstruct V by giving it diagonal one and upper entries equal to the new Gram's upper entries.
Then V+V^T=Q^T G0 Q and det(V+V^T)=-1.

For the full reciprocal polynomial write

    p_V=t^6+a t^5+b t^4+(-3-2a-2b)t^3+b t^2+a t+1,
    5+4b=Pf(V-V^T)^2.                                (2)

These are the reused L254 endpoint identities.
Consequently the COMPLETE target F=Phi6 P4 is equivalent to a=-2 and Pf=+/-3, while S6=t^6-t^4-t^3-t^2+1 is equivalent to a=0 and Pf=+/-1.
The original norm and basis equations remain necessary.
L258's restriction a even implies a+b=1 modulo4 is known only for its stated fixed-four-column family.
It will be monitored as a candidate discriminator here, not assumed for three changed columns.

<a id="three-column-declared-finite-domain"></a>
### 2. Declared finite scope before execution

The first exact test uses precisely the norm-two roots r in{-1,0,1}^6, recomputing all729 vectors and the114-root count previously used in L254.
Normalize each root's sign by requiring its first nonzero coordinate to be positive; this gives57 representatives.
Independent column signs conjugate V by a diagonal sign matrix and leave V^- unchanged, so this normalization loses neither complete original nor complete companion polynomials, determinant admissibility or norm constraints.

For each of20 position triples i<j<k, test every ORDERED triple of these57 roots, including dependent triples before the minor filter.
The exact cap is20*57^3=3703860 triples and120 seconds.
Retain counts for singular minors, other nonunit minors, old controls and genuinely changed triples.
A triple is genuine only if every inserted root differs from its own old column up to sign; otherwise it is a discarded control, not new three-column evidence.
The previous fixed-order one-/two-column conclusions are not silently applied to arbitrary controls or other orderings.

For each genuine integral basis compute the signed Pfaffian and first coefficient, retain all F and S6 hits, and separately record whether an even a ever violates the L258 residue a+b=1 modulo4.
A hit or a congruence-escape control must receive the full determinant expansion and its complete absolute-companion/literal-cover accounting before any mathematical conclusion.
This is a fixed-order finite short-root test; no unchanged order extension, larger root cube, all-integer completeness claim or new modulus is authorized by this declaration.
A cap exit will be reported as incomplete, with no complete negative theorem.

The preceding declaration was recorded before execution; its completed outcome follows.
Independent review remains pending.

The declared experiment completed below its120-second cap.
All3703860 triples were considered:1759698 had zero minor,1034514 a nonzero nonunit minor, and909648 a unit minor.
Of the latter,63116 were discarded old controls and846532 were genuine three-column changes.
Neither target occurred, and no genuine candidate with even a violated a+b=1 modulo4.
This is finite evidence only; it does not yet prove an all-three-column congruence or exclude a different basis.

<a id="exterior-square-changed-constructor"></a>
### 3. Changed algebraic constructor before any basis test

The finite outcome motivates a different realization interface.
Let A be the actual4-by-4 integral companion matrix of q(x)=x^4-2x^3+2x^2-x+1, so det A=1.
On the six-dimensional integral exterior-square lattice use the ordered basis(01,02,03,12,13,23), put C=Lambda^2 A, and let G be the symmetric pairing determined by wedge product into e0 wedge e1 wedge e2 wedge e3.
Its only nonzero paired entries are G_(01,23)=1,G_(02,13)=-1,G_(03,12)=1 and their symmetric partners.
Thus G is even unimodular with determinant-1 and signature(3,3), all shown by its three explicit hyperbolic pairs.
Exterior functoriality gives C^T G C=G directly from det A=1; this identity will also be checked entry by entry.

For a4-by-4 determinant-one matrix with characteristic polynomial x^4-s1 x^3+s2 x^2-s3 x+1, expansion of the six pairwise eigenvalue products gives

    det(tI-Lambda^2 A)
       =t^6-s2 t^5+(s1 s3-1)t^4
          -(s1^2+s3^2-2s2)t^3
          +(s1 s3-1)t^2-s2 t+1.                    (3)

This is a polynomial identity: diagonal matrices give it by elementary symmetric expansion, and polynomial continuation proves it for every matrix, including repeated roots.
For s1=2,s2=2,s3=1 it equals the COMPLETE target F.
In particular det(I-C)=F(1)=-1, so

    V0=G(I-C)^(-1)                                  (4)

is an actual integral bilinear matrix with determinant one.
The C-isometry identity gives

    V0+V0^T=G,  -V0^(-1)V0^T=C,
    det(tV0+V0^T)=F.                                (5)

For the first equation use (I-C^(-1))^(-1)=I-(I-C)^(-1); transposition of(4) gives its G times left-hand term.
The other equations then follow, with det V0=det G/det(I-C)=1.
These statements do NOT yet provide an upper-unitriangular presentation: V0 is generally not triangular and all its diagonal entries in this isotropic wedge basis are zero.
They isolate an actual integer-basis condition instead of introducing an artificial root list or deleting Phi6.

The next bounded test, declared before execution, will compute(3)--(5) exactly and attempt a nonsymmetric integer Gram--Schmidt construction.
For an integral bilinear form V and a primitive vector v with v^T V v=1, choose a unimodular basis beginning with v.
Subtract from each other basis vector its pairing V(w,v) times v, making the first column(1,0,...,0)^T; the complementary form is again integral and determinant one.
Repeat on that complementary form.
A branch succeeds only if all six resulting diagonal pivots are+1 and the total integer basis has determinant+/-1.
A branch can fail because the tested roots miss a permissible pivot; that is not an all-basis obstruction.
The initial declared pivot vectors at each remaining dimension n are all v in{-1,0,1}^n with v^T V v=1, with sign normalized, and the total recursive-node cap is20000 with a120-second runtime cap.
Both the successful full integer basis or the actual capped failure will be retained.
This test changes the underlying bilinear form and basis construction; it is not a new radius in the previous root-cube enumeration.
Any achieved triangular matrix requires complete original, absolute and cover factor/cost verification.

This second test also completed:6670 recursive calls, with4500 repeated forms merged, exhaust the declared finite pivot tree.
No triangular basis was found.
The dimensional call counts were1,87,1362,3638,1582 at remaining dimensions6,5,4,3,2; no one-dimensional success was reached.
There were300 first-visited forms with no norm-one pivot in their current small cube.
This does not prove that those forms lack larger integer norm-one vectors.
No original, absolute or cover target is claimed as upper-unitriangular, and no wider basis search is undertaken this round.

<a id="sextic-integral-bilinear-realization"></a>
### 4. A general exact sufficiency statement in the relaxed integral class

The exterior-square construction has a useful complete parameter scope.
Let p be ANY monic reciprocal sextic with p(1)=-1 and p(-1) an integer square.
Necessarily p(-1) is an odd square by the coefficient identity(2).
Choose its positive odd square root u and put k=(u-1)/2.
Writing a for its t^5 coefficient, every coefficient of p is then forced to be

    p=t^6+a t^5+[k(k+1)-1]t^4
          -[2a+2k(k+1)+1]t^3
          +[k(k+1)-1]t^2+a t+1.                    (6)

Conversely every a in Z and k>=0 in Z gives these endpoints.
Set

    q_(a,k)(x)=x^4-(k+1)x^3-a x^2-kx+1,

take its integral companion A, and apply(3)--(5) with the same explicit wedge pairing G.
Then V_(a,k)=G(I-Lambda^2 A)^(-1) is integral, det V_(a,k)=1, V_(a,k)+V_(a,k)^T=G, and

    det(t V_(a,k)+V_(a,k)^T)=p.                       (7)

This is a necessary-and-sufficient endpoint criterion for an integral determinant-one BILINEAR realization whose symmetric form has the specified G: necessity follows from reciprocity, det V=1, det G=-1, and the Pfaffian square at-1; sufficiency is the displayed construction.
No irreducibility or absence of repeated roots is needed for q or p.
The claim does not say that EVERY realization is congruent to this one, or that every reciprocal sextic satisfies those endpoints.
In particular it is not an equivalence between upper-unitriangular realization and the two endpoint conditions.

For a proof of the exterior coefficient identity not relying on an uninspected representation theorem, diagonalize a generic complex matrix with four distinct nonzero eigenvalues of product one.
The six exterior eigenvalues are their pairwise products.
Expanding the first three elementary symmetric functions gives s2, s1 s3-1, and s1^2+s3^2-2s2; reciprocal pairing supplies the remaining coefficients.
These polynomial identities extend to all determinant-one matrices by density (equivalently, by the elementary symmetric polynomial identity with determinant variable specialized to one).
Direct symbolic identities for the actual two-parameter companion are retained in J59.
The isometry C^T G C=G is simply the four-fold wedge product formula, with an explicit integer entry check.
Thus neither a spin-group identification nor an assertion of integral reflection generation is a hidden premise.

The relaxed result explains why replacing root lists by a companion matrix alone cannot close the requested realization gate: integral unimodularity and the exact determinant already hold, but the additional actual ordered integer basis with six positive unit pivots has not been supplied.
The earlier L258 obstruction concerns one root-basis architecture, while(7) supplies an actual bilinear form directly from the prescribed polynomial.
The new unresolved condition is concrete integral triangularization, not scalar divisibility or a missing cofactor calculation.

For full explicitness the matrix in(7) is

    V_(a,k)=[
      [0, -1, -k-1, 0, -1, 0],
      [1, 0, a+1, 1, 0, 1],
      [k+1, -a-1, 0, k+1, -a-1, k],
      [0, -1, -k, 0, -1, 0],
      [1, -1, a+1, 1, 0, 1],
      [1, -1, -k, 0, -1, 0]].                       (8)

Its pairwise entry sums give exactly G; multiplication by I-C gives G entry by entry.
This verifies the inverse formula and its integrality without a bound on the parameters or an existence theorem.
All six diagonal entries remain zero.
The construction by itself does not supply a positive unit pivot sequence, even over all integer vectors, and the completed finite tree cannot rule out larger pivots.

<a id="relaxed-bilinear-complete-absolute-cost"></a>
### 5. Full original, absolute and covering expenses

The two sorts of matrices in this round must remain distinct.
Every admitted three-column candidate is an actual rank6 upper-unitriangular integer V; its standard absolute companion has diagonal one and strict upper entries-|V_ij|, and its rank12 literal cover has the entire product of their determinant polynomials, exactly at the reused D9/L254 scope.
No target was achieved in that finite class.
J59 retains the complete energy histogram, whose minimum and maximum are17 and90.
Thus every strict upper entry has absolute value at most9, giving a coarse uniform height bound without claiming an attained maximum height.
Energy is not used as a Mahler estimate or an optimum.

The new V_(a,k) is instead a nontriangular integer bilinear matrix with diagonal zero.
For it explicitly define the FULL-entry absolute matrix B=-|V_(a,k)|, with zero diagonal, and the following full-entry twelve-dimensional integer lift W.
For EVERY ordered matrix entry x=V_ij, its2-by-2 block is x I2 if x<=0 and -x times the sheet-swap matrix if x>0.
This definition applies also below the diagonal.
The symmetric-sheet subspace carries B and the antisymmetric-sheet subspace carries V.
The same fixed real orthogonal sheet transform splits both W and W^T, proving

    det(tW+W^T)=det(tV+V^T) det(tB+B^T).              (9)

This is a directly verified full-matrix identity.
It is NOT an invocation of the upper-unitriangular cover theorem outside its hypotheses.
W has zero diagonal and is not upper-unitriangular, nor is B a diagonal-one companion.
These remain relaxed controls and supply no accepted upper-unitriangular solution.

Let u=|a+1|, h=max(k+1,u), and

    L=(2k+1)u-3,
    M=-k(k+1)+(8k+4)u-3,
    R=-2k(k+1)+(12k+6)u-3.

Direct expansion of(8)'s full-entry B gives the COMPLETE factor

    p_B=-t^6+L(t^5+t)+M(t^4+t^2)+R t^3-1.           (10)

In particular det B=-1, so both B and W are nonsingular integral matrices, det W=-1, and their polynomial degrees are6 and12.
There is no lost leading coefficient or undefined zero polynomial.
Formula(10) is proved by finite polynomial expansion (also checked symbolically in J59); taking absolute values is legitimate with the explicitly retained u and k>=0.

The actual ranks are6,6,12, and all three entry heights are h.
For the NONTRIANGULAR matrices use the whole squared-entry sum, not the upper-entry energy convention:

    sum_(i,j) V_ij^2=sum_(i,j) B_ij^2
       =6k^2+6k+17+4u^2=:E_all,
    sum_(i,j) W_ij^2=2E_all.                         (11)

Since p_V(1)=-1, p_V has a real root above1 and positive total logarithmic Mahler measure.
The leading magnitude of p_B is1.
With all factors retained, (9) gives

    m(p_W)=m(p_V)+m(p_B),
    0<m(p_V)<=log720+6log(2h),
    0<=m(p_B)<=log720+6log(2h).                       (12)

For the upper bounds, every entry of tV+V^T or tB+B^T on the circle has modulus at most2h; expand into6! terms and integrate the logarithm.
The logarithms of these nonzero polynomials are integrable even at circle roots.
This is a complete, coarse, unnormalized bound, not a near-one theorem.
Repeated or neutral factors are never removed.

For the actual F control take a=-2,k=1, hence h=2,E_all=33 and covering sum66.
The complete factors are

    p_V=Phi6 P4,
    p_B=-[t^6-7t^4-11t^3-7t^2+1].                   (13)

The second factor divided by -t^3 has trace polynomial q_B(z)=z^3-10z-11.
Its values at -3,-2,-1,3,4 are -8,1,-2,-14,13, so its three distinct roots lie in(-3,-2),(-2,-1),(3,4).
Thus it has two exterior reciprocal pairs, one negative and one positive, and one nonreal unit-circle pair.
Let R_- and R_+ be the moduli of the two expanding roots.
Its ENTIRE measure is log R_-+log R_+, where1<R_-<(3+sqrt5)/2 and(3+sqrt5)/2<R_+<2+sqrt3.
Since beta4<2<(3+sqrt5)/2, this absolute cost exceeds log beta4.
Consequently the complete relaxed cover has measure GREATER than2log beta4, retaining the full degree-two Phi6 and the full other sextic.
Even this relaxed control does not improve the achieved L191 upper-unitriangular Phi2^2 P4 cover of measure2log beta4.

For the actual S6 control take a=0,k=0, giving h=1,E_all=21 and covering sum42.
The complete factors are

    p_V=S6=t^6-t^4-t^3-t^2+1,
    p_B=-[t^6+2t^5-t^4-3t^3-t^2+2t+1].             (14)

Its trace polynomial is q_B(z)=z^3+2z^2-4z-7.
At -5/2,-12/5,-2,-1,1,2 its values are -1/8,37/125,1,-2,-8,1.
Hence exactly one trace root is in(-5/2,-12/5), another in(-2,-1), and the last in(1,2).
There is exactly one expanding reciprocal pair, both negative, with modulus R satisfying12/5<R+R^(-1)<5/2 and hence1<R<2.
The full absolute measure is log R.
L254 gives the original expanding trace below9/4<12/5, so R exceeds the original expanding root of S6.
Its complete relaxed cover again has measure greater than twice the original measure.
There is no claimed optimality or new smaller upper-unitriangular seed.
No irreducibility assertion for the absolute controls is needed for these complete root-count and measure statements.

The full degree12 products, all matrices, determinant signs and squared-entry costs in(13)--(14) are retained in J59.
Thirteen separate integer evaluations of each literal covering determinant verify its full product, because its degree is at most12.
The exact orthogonal sheet splitting supplies the all-parameter proof of(9); the26 evaluations are additional author checks of the two displayed controls, not a substitute for that proof.

<a id="three-column-and-exterior-execution-scope"></a>
### 6. Execution, self-check and the remaining realization condition

The actual code and native outputs are in [J59](../computations/programs/Yin_J_G0059/readme.md).
search.py recomputes every root and the complete3-by-3 minor, then uses exact Pfaffians and triangular inversion for the complete reciprocal coefficients.
All3703860 declared triples were visited.
The six coefficient-residue bins for(a mod4,b mod4) were(0,1):75339,(1,1):174281,(1,3):178537,(2,3):68129,(3,1):174483,(3,3):175763.
They total846532 genuine candidates.
Their continuing a+b restriction is finite evidence; the modular theorem of L258 is not extended to them by observation.

exterior.py verifies the exact companion, six-by-six exterior matrix, G-isometry, integral V0, and FULL target polynomial before any basis attempt.
Its deterministic pivot ordering first minimizes the number of nonzero entries and then uses lexicographic order.
A normalized cube vector has a coordinate+1, so the specified completion by the other coordinate vectors is unimodular.
Subtracting V(w,v)v from each other column clears the lower first column and leaves the first diagonal1.
The recursive lower block has determinant1.
If it had reached all six positive pivots, composition would have produced a checked unimodular basis and exact upper-unitriangular target.
Repeated exact forms are merged; identical remaining forms have identical subsequent finite pivot trees, so this memoization does not remove a possible success in the declared tree.
No node/runtime cap was reached.
Absence in this particular finite sequence of small coordinate pivots is not absence of a different completion or of larger vectors at any level.

costs.py verifies the whole two-parameter exterior characteristic identity, det(I-C)=-1, G-isometry, the explicit integer matrix(8), both equations linking it to G and C, and the complete absolute polynomial(10).
It then specializes both actual targets and checks the full matrices, signs, factors and26 integer cover determinants.
The program was rerun at the same control scope after adding the symbolic general absolute factor; the displayed original control polynomials and costs stayed unchanged.
All arithmetic affecting conclusions is exact.
No failed or capped mathematical run occurred.

### Explicit exterior coefficient and finite-certificate closure

The elementary expansion in3 is fully determined before specialization: for four eigenvalues with elementary sums s1,s2,s3,s4, the six pairwise products have first sums s2 and s1*s3-s4.
For the third sum, the four triangles contribute s3^2-2s2*s4, the four stars s4*(s1^2-2s2), and the twelve paths2s2*s4.
Their total is s3^2+s4*s1^2-2s2*s4, and complementary edges supply reciprocity when s4=1.
This is a polynomial identity, hence includes repeated eigenvalues and every determinant-one companion without a diagonalizability assumption.
Transposition of V=G(I-C)^(-1) gives V^T=G(I-C^(-1))^(-1)=G-V=-VC, proving all signs, the full symmetric form and determinant pencil.
Necessity of the endpoints uses det V=1, det G=-1 and the skew Pfaffian square; p(-1)=5+4b cannot be an even or zero square.

The two full lift polynomials, in ASCENDING coefficient order, are

    F control: [-1,2,6,-2,-9,-8,1,-8,-9,-2,6,2,-1],
    S6 control: [-1,-2,2,6,3,-4,-7,-4,3,6,2,-2,-1].

They retain every original, cyclotomic, reciprocal and absolute factor, including leading sign-1 and actual degree12.
The full generic sheet proof9 proves their product identity; the26 exact scalar evaluations are additional fixed controls.
The rational signs in13--14 give three disjoint sign intervals for each cubic and exhaust its degree, proving simplicity and all remaining unit-circle pairs without an irreducibility premise.

For each pivot, r=Vv and l=v^T V give the remaining matrix by deleting the pivot coordinate from V-r*l.
This independently agrees with the declared unimodular completion and lower-column clearing, whose remaining determinant is1.
The unique-state graph, all6669 edges, both declared cap boundaries and all20 terminal paths are therefore a finite exact certificate, not a substitute for the missing unrestricted basis theorem.
The original current input matrices and all20 position tables, every energy/Pfaffian/residue histogram, both full A/G/C/V/B/W controls and all26 determinant values remain in the four [J59 native records](../computations/programs/Yin_J_G0059/readme.md).


### Actual checking and retained limits

The maintaining agent read all original L262/R161, all four J59 programs/readme and all four native JSON records, and compared the complete C429/C442/C2 and achieved L191 interfaces at their actual scopes.
It checked the whole integer-minor/norm/sign/endpoint construction, every integer parameter and repeated-root case, all integral inverse/symmetric/isometry signs, the full-entry splitting and every determinant/rank/degree/height/whole-energy/trace/leading/measure cost.
Only the original reviewer was replayed: its original20*57^3 domain,<=20000 pivot-call bound, two symbolic/finite controls and240-second cap were unchanged.
The sole report write was intercepted in memory; the whole old report matched in1.827seconds and all9 program/native files stayed unchanged.
The replay included all3703860 triples/846532 genuine cases, all20 tables/histograms, the complete6670-call/6669-edge graph, all20 saved dead paths, both full degree12 controls and26 determinant values.
No author producer, larger root cube, alternative completion, new source passage/PDF, experiment or Task/E execution was run.
The author's original whole self-check is retained at its recorded2026-10-10 date, without inventing an absent check/freeze minute.
R161's known assignment/progress descriptions do not establish the exact initial proof-relevant context and ordering, while its D9 authorship/upstream reviews alone do not establish contribution to this proof; its full original scope remains UNKNOWN.
This maintaining-agent whole SELF is not fresh isolation and closes no historical independent-review obligation.

## Current assessment
[Selected decision](#decision-complete-quartic-home-maintenance)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:11 |
| status | open |
| reason | Retain the complete original integral bilinear endpoint theorem, every integer parameter/repeated-root/sign/inverse/full absolute/lift factor and all root/leading/rank/whole-energy costs, together with both exact finite negative scopes. Existing C429/C442/C2 and fixed L191 inputs are used only at their complete actual scopes; no triangularization, universal congruence, optimized cost, source-proof intake or research run is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact whole theorem](#statement) | Every endpoint-compatible integral reciprocal sextic, all integer a/nonnegative k/repeated roots, actual specified G and zero-diagonal bilinear class; both original finite domains, all full factors/ranks/degrees/heights/whole energies/roots/measure/negative limits. |
| argument | [Entire proof](#argument) | Complete mathematical Sections1--6/equations1--14, explicit G0/minor/sign/endpoint/exterior/symmetric-inverse proof, all-parameter V/B/W identities, exact scalar comparisons and full fixed finite certificates. |
| dependency | [Complete seed/endpoint/secondary scalar proof](Yin_C_G0429_v1.md#argument) | Exact conference G0/path basis/norm/determinant conventions, full reciprocal endpoint targets and complete local S6 trace/root proof; no unstated order extension. |
| dependency | [Proper signed-cover proof](Yin_C_G0002_v1.md#signed-cover-identity) | Only proper upper-unitriangular candidates; complete original/absolute factor and rank/energy doubling. The relaxed V/B/W identity is proved separately here. |
| support | [Different unbounded fixed-four-column theorem](Yin_C_G0442_v1.md#argument) | Exact earlier architecture/comparison boundary only; its parity conclusion is not presumed for three changed columns. |
| support | [Achieved proper quartic control](../ledger/Yin_L_G0191_v1.md#irreducible-quartic-gram-family) | Actual k4 rank6/height1/energy5 Phi2^2 P4 and full rank12/height1/energy10 Phi2^4 P4^2, measure2log beta4; fixed original input until its adequate current home exists. |
| support | [All original native evidence](../computations/programs/Yin_J_G0059/readme.md) | Full static four-program/four-native inspection and stdout-only fixed reviewer replay of the original complete scope; no author execution/new experiment or expanded domain. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:13 |
| status | proved |
| reason | Adopt after the actual C456/R662 whole SELF check of the complete original Sections1--6/equations1--14, all integer endpoint-compatible parameters/repeated roots, explicit minors/norms/signs/integer inverses/G-isometry, full-entry original/absolute/lift factors, every rank/degree/leading/root/height/whole-energy/measure cost and both exact finite negative domains. The original fixed reviewer reproduced the entire native report without file writes or expanded input; author producers/source proof/PDF/Task execution were not run. R161 remains UNKNOWN on its original entire mathematical/native scope, with prior roles/algorithmic separation not treated as proof of isolation; new SELF supplies no fresh isolation or universal triangularization/congruence/cost/gap conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact whole theorem](#statement) | Every endpoint-compatible integral reciprocal sextic, all integer a/nonnegative k/repeated roots, actual specified G and zero-diagonal bilinear class; both original finite domains, all full factors/ranks/degrees/heights/whole energies/roots/measure/negative limits. |
| argument | [Entire proof](#argument) | Complete mathematical Sections1--6/equations1--14, explicit G0/minor/sign/endpoint/exterior/symmetric-inverse proof, all-parameter V/B/W identities, exact scalar comparisons and full fixed finite certificates. |
| dependency | [Complete seed/endpoint/secondary scalar proof](Yin_C_G0429_v1.md#argument) | Exact conference G0/path basis/norm/determinant conventions, full reciprocal endpoint targets and complete local S6 trace/root proof; no unstated order extension. |
| dependency | [Proper signed-cover proof](Yin_C_G0002_v1.md#signed-cover-identity) | Only proper upper-unitriangular candidates; complete original/absolute factor and rank/energy doubling. The relaxed V/B/W identity is proved separately here. |
| support | [Different unbounded fixed-four-column theorem](Yin_C_G0442_v1.md#argument) | Exact earlier architecture/comparison boundary only; its parity conclusion is not presumed for three changed columns. |
| support | [Achieved proper quartic control](../ledger/Yin_L_G0191_v1.md#irreducible-quartic-gram-family) | Actual k4 rank6/height1/energy5 Phi2^2 P4 and full rank12/height1/energy10 Phi2^4 P4^2, measure2log beta4; fixed original input until its adequate current home exists. |
| support | [All original native evidence](../computations/programs/Yin_J_G0059/readme.md) | Full static four-program/four-native inspection and stdout-only fixed reviewer replay of the original complete scope; no author execution/new experiment or expanded domain. |
| review | [Actual whole SELF finding](../audits/reviews/Yin_R_G0662_v1.md#exterior-sextic-whole-self-finding) | ENTIRE exact statement/argument and all actual direct inputs, every parameter/repeated-root/sign/minor/norm/exterior/inverse/sheet factor and full root/leading/rank/degree/height/whole-energy/measure cost, both finite certificates and all original/source/unresolved-basis boundaries; original R161 whole UNKNOWN remains. |


### Decision complete-quartic-home-maintenance

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:26 |
| status | proved |
| reason | Select the actual complete current C458v2 k4 integer-Gram/Schur/full-sheet mechanism for the same already proved proper quartic comparison after full statement/argument/decision/R665 reading and actual same-object input check. The entire C456 statement and proof, all other inputs/reviews and every finite/bilinear/root/full-factor/cost/negative scope remain unchanged. Existing original L191/R161/R662 inputs and dates remain actual; this administrative home maintenance is SELF and supplies no new mathematical repair, isolation, source/native run or Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact whole theorem](#statement) | Every endpoint-compatible integral reciprocal sextic, all integer a/nonnegative k/repeated roots, actual specified G and zero-diagonal bilinear class; both original finite domains, all full factors/ranks/degrees/heights/whole energies/roots/measure/negative limits. |
| argument | [Entire proof](#argument) | Complete mathematical Sections1--6/equations1--14, explicit G0/minor/sign/endpoint/exterior/symmetric-inverse proof, all-parameter V/B/W identities, exact scalar comparisons and full fixed finite certificates. |
| dependency | [Complete seed/endpoint/secondary scalar proof](Yin_C_G0429_v1.md#argument) | Exact conference G0/path basis/norm/determinant conventions, full reciprocal endpoint targets and complete local S6 trace/root proof; no unstated order extension. |
| dependency | [Proper signed-cover proof](Yin_C_G0002_v1.md#signed-cover-identity) | Only proper upper-unitriangular candidates; complete original/absolute factor and rank/energy doubling. The relaxed V/B/W identity is proved separately here. |
| support | [Different unbounded fixed-four-column theorem](Yin_C_G0442_v1.md#argument) | Exact earlier architecture/comparison boundary only; its parity conclusion is not presumed for three changed columns. |
| support | [Complete achieved proper quartic mechanism](Yin_C_G0458_v2.md#quartic-six-to-twelve-cover-costs) | Same actual k4 integer Gram rows and Schur/two-sheet proof, rank6/height1/energy5 Phi2^2 P4 and ENTIRE rank12/height1/energy10 Phi2^4 P4^2/measure2log beta4; original L191/R161/R662 fixed inputs and original decisions remain unchanged. |
| support | [All original native evidence](../computations/programs/Yin_J_G0059/readme.md) | Full static four-program/four-native inspection and stdout-only fixed reviewer replay of the original complete scope; no author execution/new experiment or expanded domain. |
| review | [Actual whole SELF finding](../audits/reviews/Yin_R_G0662_v1.md#exterior-sextic-whole-self-finding) | ENTIRE exact statement/argument and all actual direct inputs, every parameter/repeated-root/sign/minor/norm/exterior/inverse/sheet factor and full root/leading/rank/degree/height/whole-energy/measure cost, both finite certificates and all original/source/unresolved-basis boundaries; original R161 whole UNKNOWN remains. |
| review | [Actual current-home SELF finding](../audits/reviews/Yin_R_G0662_v1.md#exterior-sextic-quartic-home-finding) | Entire unchanged current C456 statement/argument and exact same-object k4 full proof/cost interface at C458v2, with earlier whole SELF reused and original old-input findings/whole R161 UNKNOWN preserved. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0059](../computations/programs/Yin_J_G0059/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
