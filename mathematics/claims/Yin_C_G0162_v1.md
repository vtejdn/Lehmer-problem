---
author: Yin
---
# Frobenius orbital valency, matching density and the complete ratio norm

Date: 2026-10-18T11:09.
Human author Yin.
Root proposed replacing the conservative centralizer count by an actual ordered-pair orbit and its compatible Frobenius edges, supplied the direct extra-depth norm alternative, and supplied the final C2-wreath group discriminator.
The entropy_attainment_bridge AI develops the complete pair-field, fiber, height, valuation, norm and comparison arguments.
Root and this agent are contributors and cannot independently review the whole result.
The complete argument was developed in the newly reused D43 under the 2026-10-18T11:09 assignment and is registered here for separate whole review.
The account is an author-checked proof candidate, with no numerical computation, actual Galois/unit realization, independent review or acceptance.

<a id="orbital-reuse"></a>
## Reuse and the actual added statement

[L397's accepted pair-orbit account](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) already proves the compositum degree, constant ratio fibers, nontorsion of every cross-exponent ratio and the full-coordinate height bound.
It also retains the failure of multiplying over all pairs, whose degree-weighted population is d^2.
These are reused mechanisms, not new claims here.
The inspected [C146v2 own-field argument](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) supplies the degree-D local value-group amplification; its [signed original return](Yin_C_G0146_v2.md#ratio-original-signed-norm-return) retains the norm tower and coefficient-order limits.
[C146v1](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) already uses extra p-powers and the elementary triangle bound to turn a supplied positive density into a direct measure bound.
The local source is the accepted [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001), with its original proof-reading limits.

The new question is the income from ONE actual ordered-pair orbit, with its own compositum valency s and actual Frobenius-edge density gamma, rather than a centralizer lower bound or full symmetrization.
[C147v5's accepted complete cyclic theorem](Yin_C_G0147_v5.md#decision-whole-reviewed-2026-10-18) supplies the current quantitative inverse threshold.
No angular C159 estimate is substituted for that full logarithmic norm.
The bounded source/comparison screen also read [L162](../ledger/Yin_L_G0162_v1.md#actual-inversion-matching-average), [L68](../ledger/Yin_L_G0068_v1.md#cyclic-norm-residue-density), [L205](../ledger/Yin_L_G0205_v1.md#bounded-residue-mass-near-one-escape), [AM16-U002](../audits/literature/AM16/Yin_U002.md#am16-u002), [AZ10-U001](../audits/literature/AZ10/Yin_U001.md#az10-u001) and the [Smyth nonreciprocal interface](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number).
Their actual prior coverage is separated below from the new two-parameter criterion.
No new external source, classification of primitive permutation groups or claim of globally novel arithmetic coverage is imported.

## Statement

Let alpha be a nontorsion algebraic integer unit of ORIGINAL degree d, with total logarithmic Mahler measure m>0.
Let L be its normal closure, G=Gal(L/Q), and X its d-element root set.
Choose any rational prime p, any prime of O_L above p and any lift sigma in its decomposition group of residue Frobenius.
No unramified or distinct-reduction hypothesis is imposed.
Put

    x=alpha, y=sigma(alpha), K=Q(x), H=G_x,
    Omega=G.(x,y),
    s=[G_x:G_x intersection G_y],
    M=|Omega|=s d,
    b=#{z in X:(z,sigma z) belongs to Omega},
    gamma=b/d.

Here 1<=s<=d, 1<=b<=d and 0<gamma<=1.
Let

    K''=Q(x,y), rho=x^p/y, E=Q(rho), D=[E:Q],
    a=ceil(log_p D), n=p^a.

Then rho is a nontorsion algebraic integer unit and

    [K'':Q]=s d, [K'':K]=s, 2<=D<=s d,
    h_abs(rho)<= (p+1)m/d,
    m_rho=D h_abs(rho)<=s(p+1)m,
    n<pD,
    log|Norm_(E/Q)(rho^n-1)|/D >=gamma log p/s.      (1)

Every own-field and original-field multiplicity is retained.
It is NOT assumed that sigma preserves K''; nontorsion is checked in the ambient finite Galois field L.

Use the exact C147v5 functions

    h_*=exp(-40),
    Phi_5(h)=86sqrt(h)[log(1/h)]^(5/2)
                    /[log log(1/h)]^(3/2), 0<h<=h_*.

For tau>0, H_5(tau)=h_* if tau/2>=Phi_5(h_*); otherwise H_5(tau) is the unique h in (0,h_*) with Phi_5(h)=tau/2.
The first resulting bound is

    m>H_5(gamma log p/s)/[p(p+1)s].                 (2)

It includes the large-height branch through the stated cap.
For every positive integer A satisfying A gamma log p/s>log2, the second, elementary bound is

    m>[A gamma log p/s-log2]/[p^A s(p+1)].          (3)

Both bounds are valid, so their maximum may be used at the same actual input.
For example p=2,s=2,gamma=1 and A=3 or A=4 give m>log2/96.
This numerical formula is conditional on ACTUAL supplied parameters, not a realized input or prime.

For either the exponent n in (1) or n_A=p^(a+A-1), let

    beta_N=x^(pN)-y^N, eta_N=Norm_(K''/K)(beta_N).

Then eta_N is a nonzero element of the full original O_K and

    Norm_(K/Q)(eta_N)
      =epsilon_N Norm_(E/Q)(rho^N-1)^(M/D),
    epsilon_N=Norm_(K''/Q)(y^N) in {1,-1},
    log|Norm_(K/Q)(eta_N)|/M
      =log|Norm_(E/Q)(rho^N-1)|/D.                  (4)

For n one has n<psd, pn<p^2sd and spn<p^2s^2d.
For n_A one has n_A<p^A sd, pn_A<p^(A+1)sd and spn_A<p^(A+1)s^2d.
The relative product has s factors and at most 2^s signed conjugate monomials before collection, with total conjugate exponent at most spN.
No cheap representative in Z[alpha] or bounded coefficient norm is asserted.

There is an exact comparison with C146.
Let C=C_G(sigma), kappa=[G:C], r_c=[H:H intersection C] and Gamma be sigma's conjugacy class.
Then

    gamma=|Gamma intersection H sigma H|/kappa,
    |H sigma H|=s|H|,
    s<=r_c<=kappa,
    gamma>=r_c/kappa,
    gamma/s>=1/kappa.                               (5)

Consequently the bound (2) is at least C146v5's actual supplied-class bound H_5(log p/kappa)/[p(p+1)kappa].
This is a comparison of proved functions, not a claimed strict gain in every input.
If |H| is bounded, a bounded s and positive lower bound for gamma already force bounded kappa through gamma<=s|H|/kappa.
A possible change of coverage therefore needs an unbounded point stabilizer or information outside that old class criterion.

A group-only discriminator below has s=2, gamma=1, unbounded class size, no bounded abelian subgroup index, no bounded cycle lengths or fixed-power class control, and no bounded relative degree over any abelian base in a hypothetical arithmetic realization.
Its root action permits a fixed-point-free G-equivariant involution and so does not itself exclude reciprocity.
Precisely, for every prime q and integer j>=3, take T=C_q times S_j, t=q j!, G=(C2)^T semidirect T on X=T times {0,1}, and sigma the pure translation by the central C_q generator.
Then d_model=2t, s=2, gamma=1, kappa=2^((q-1)j!), every sigma-cycle has length q, and N_G(G_x)/G_x is C2.
Every abelian subgroup A of G has [G:A]>=j!/3^(j/3).
In any hypothetical number-field realization of this root action, every finite abelian base F/Q satisfies [F(alpha):F]>=j!.
For each fixed f>=1 and q>f, sigma^f has the same conjugacy-class size as sigma.
No actual nontorsion unit, prime or residue-Frobenius realization of that model is supplied.
The original unrestricted arithmetic coverage remains unresolved.

<a id="argument"></a>
## 1. Pair-field and ratio fibers without a false field automorphism

The stabilizer of (x,y) is G_x intersection G_y, whose fixed field is exactly K''.
Orbit-stabilizer gives M=[K'':Q]=sd and [K'':K]=s.
The two coordinate projections Omega->X are equivariant and onto, and therefore each has constant fiber size s.
These are the accepted L397 identities, now used at one selected orbit.

The G-equivariant map

    (z,w) in Omega maps to z^p/w

has image the distinct conjugates of rho.
Each fiber has size M/D, since E is a subfield of K'' and every E-embedding extends to exactly M/D K''-embeddings.
Ratio coincidences therefore do not identify M ordered pairs with M distinct conjugates.

Both x and y are global integer units, so rho is an integer unit.
If rho^v=1 for some positive integer v, then x^(pv)=sigma(x)^v.
Apply powers of the ambient automorphism sigma in L; induction gives sigma^j(x)^v=x^(p^j v).
At its finite order j=q this would give x^((p^q-1)v)=1, contradicting nontorsion.
This argument never treats sigma as an automorphism of K''.
A rational integer unit would be 1 or -1, hence D>=2.

Since both coordinate fibers have size s, the complete sum over Omega gives

    sum_((z,w) in Omega) log^+|z^p/w|
      <=p s sum_(z in X)log^+|z|
         +s sum_(w in X)log^-|w|
      =s(p+1)m.

Dividing by M and canceling the constant ratio-fiber multiplicity proves the height bound in (1).
The bound for m_rho then uses D<=M.
No multiplicative independence, preserved powered degree or normality of the pair field is assumed.

## 2. Actual compatible values and ramification-safe amplification

For every one of the b counted pairs (z,sigma z), residue Frobenius gives z^p/sigma(z)=1 modulo the chosen prime of O_L.
Because both factors are units, this is a genuine positive valuation of the difference from 1.
The count refers to those b algebraic pairs, not all possible residue-compatible pairs.
At bad reductions additional pairs may contribute; they are not subtracted or called absent.

The constant fibers show that at least b/(M/D)=gamma D/s DISTINCT conjugates of rho are congruent to 1.
This can be a noninteger lower bound and means at least its ceiling.
Each such conjugate lies in its own degree-D copy of E.
The accepted local degree/value-group interface gives positive normalized valuation at least 1/e>=1/D, where v(p)=1 and e is the ramification index in THAT copy of E.
No bound for the ramification degree of L is substituted.

For v(z-1)>0, binomial expansion supplies

    v(z^p-1)>=min(p v(z-1),1+v(z-1)).

Thus after a=ceil(log_p D) steps each selected valuation is at least 1.
Indeed until that value is reached the lower bound is at least min(1,pv), and p^a>=D.
The strict inequality p^a<pD holds also when D is an exact power of p.
All other conjugates of rho^n-1 are integral and have nonnegative valuation.
The complete nonzero rational integer norm consequently has p-valuation at least gamma D/s, proving (1).

After A-1 further p-power steps, every selected valuation is at least A, since min(pv,1+v)>=v+1 when v>=1.
At the SAME exponent n_A=p^(a+A-1)<p^A D this gives

    log|Norm_(E/Q)(rho^(n_A)-1)|/D
       >=A gamma log p/s.                           (6)

This retains p=2, arbitrary ramification, all omitted nonnegative contributions and every original own-field conjugate.

## 3. The capped cyclic and direct elementary expenses

At exponent n, the actual height parameter for applying C147v5 to rho is

    u=n h_abs(rho)<p m_rho<=p(p+1)s m.

The norm density in (1) is at least tau=gamma log p/s>0.
C147v5's inverse implication gives u>H_5(tau), including u>h_* automatically.
Combining the strict inequalities proves (2).

For n_A, apply the elementary inequality |z^(n_A)-1|<=2max(1,|z|^(n_A)) to every actual conjugate of rho.
Then

    log|Norm_(E/Q)(rho^(n_A)-1)|/D
      <=log2+n_A h_abs(rho)
      <log2+p^A s(p+1)m.                            (7)

Equations (6)--(7), and the stipulated positive numerator, prove (3).
This is the C146v1 amplification/triangle architecture with the actual orbital fraction and smaller pair field, not a new elementary norm theorem.
The two alternatives need not dominate one another for all parameters.
The explicit p=2,s=2,gamma=1 check is direct substitution: A=3 gives numerator log2/2 and denominator 48, while A=4 gives numerator log2 and denominator 96.

For supplied bounds s<=S and gamma>=delta>0, (2) gives the class-wide positive bound H_5(delta log p/S)/[p(p+1)S].
Here H_5 is nondecreasing by its increasing-inverse and constant-cap definition.
The direct alternative can likewise use any A with A delta log p/S>log2 and denominator p^A S(p+1).
A bounded finite prime pool can be handled by the minimum of its applicable positive constants.
This does not provide any of those structural bounds automatically.

## 4. Complete signed return to the original field

For either retained exponent N, beta_N=y^N(rho^N-1) is a nonzero algebraic integer in K''.
Taking the full signed norm to Q gives (4), because E is a subfield of K'' and y is a global unit.
Taking the relative norm first gives eta_N in the full original O_K and the same signed norm by the tower identity.
No assumption that K''/K is Galois is used.

Concretely, with J=H intersection G_y, the relative product is

    eta_N=product_(hJ in H/J)[x^(pN)-h(y)^N].

The factors are well-defined on these left cosets because J fixes x and y.
There are s factors and at most 2^s monomials before collection.
Each selected summand has total root exponent at most pN, so the full product's exponent is at most spN.
The bounds in the statement follow from D<=sd and n<pD or n_A<p^A D.
Using original degree d rather than M=sd in the normalized norm would multiply BOTH income and expense by s.
No degree or coefficient saving is obtained by suppressing that factor.

<a id="orbital-centralizer-comparison"></a>
## 5. Exact double-coset law and domination of the old class parameters

Identify X with the left cosets G/H by gH maps to gx.
The neighbors of x in Omega are exactly H sigma H/H; their number is s.
For z=gx the condition (z,sigma z) in Omega is equivalent to

    g^(-1) sigma g in H sigma H.

Each root has |H| representatives g.
The conjugation map G->Gamma has constant fiber size |C|.
Consequently

    b|H|=|Gamma intersection H sigma H| |C|,

which is precisely the first identity of (5).
The double coset has s left H-cosets, so its size is s|H| and gamma<=s|H|/kappa.

Every h in H intersection C fixes y=sigma x, so H intersection C is contained in H intersection G_y.
Therefore s<=r_c, and r_c<=kappa is the usual index injection into G/C.
The entire C-orbit of x contributes compatible edges, because for c in C,

    c(x,y)=(cx,c sigma x)=(cx,sigma cx).

It has |C|/|C intersection H|=d r_c/kappa points.
Hence gamma>=r_c/kappa and gamma/s>=1/kappa.
Since H_5 is nondecreasing and s<=kappa, comparison of both numerator and denominator proves the stated domination of C146v5.

The distinction is substantive even though the ingredients are reused: the old field fixed by H intersection C can be strictly larger than Q(x,y), and its guaranteed centralizer subset can miss other compatible edges.
The new parameters record those two expenses separately.

There is no automatic bounded-valency selection from the partition into pair orbits.
Across all orbitals, their valencies sum to d and their matching counts sum to d.
Thus their densities sum to 1; this gives only a weighted ratio of order 1/d without further structure, consistent with L397's full-population obstruction.
For a 2-transitive action and sigma x!=x, the orbital is all unequal pairs, s=d-1 and b=d-|Fix_X(sigma)|.
The resulting criterion is degree-dependent.
If sigma x=x, it is the diagonal orbital and s=1 instead; the two cases must not be conflated.

<a id="orbital-prior-coverage"></a>
## 6. Prior-coverage tests and the useful failed group candidate

The diagonal orbital is old residue income.
Its b fixed roots satisfy z^(p-1)=1 in the residue field.
They contribute at least b original labels to the degree-one factor mass, including repeated reductions, so L205's bounded-residue theorem already excludes a positive density at bounded p near one.
L68 retains the earlier unramified good-reduction version.
The reciprocal inversion orbital similarly recovers L160/L162's already studied inverse matching rather than a new automatic class.

Bounded point stabilizer is also old coverage: (5) gives kappa<=s|H|/gamma.
Consequently bounded s, a fixed positive gamma and bounded |H| imply the supplied bounded-class hypothesis of C146.
A primitive bounded-subdegree classification is not invoked to produce such a stabilizer bound.

An initially considered block model used S3 wr C_q and the shift of q blocks.
It has bounded s and full matching density despite an unbounded class, but the fixed field of its base group is abelian and the original generator has relative degree at most 3 over that field.
AM16-U002 therefore already covers that field class.
More decisively, root identified the additional scope failure in the proposed S3 wr (C_q times S_j) variant: its natural point stabilizer is self-normalizing.
Indeed its coordinate at the distinguished block is a point stabilizer C2 in S3, which is self-normalizing; the other block coordinates are full S3, and a nontrivial regular block translation cannot preserve the distinguished block.
Thus N_G(H)=H.

In an actual normal-closure realization, Aut(Q(alpha)/Q)=N_G(H)/H.
A reciprocal irreducible nontorsion alpha would induce the nontrivial automorphism alpha maps to alpha^(-1), so such an S3-wreath natural action cannot belong to the reciprocal unresolved core.
Any actual integer-unit input in that action is nonreciprocal and already has the accepted Smyth gap.
This corrected failed candidate is retained rather than treated as newly uncovered arithmetic coverage.

<a id="reciprocity-compatible-group-model"></a>
## 7. A reciprocal-compatible group discriminator, not an arithmetic realization

Root proposed the corrected model with base C2.
Let q be a rational prime, j>=3 an integer, and put

    T=C_q times S_j, t=|T|=q j!,
    B=(C2)^T, G=B semidirect T,
    X=T times {0,1}, d_model=2t.

The group T acts regularly on blocks by left translation, and B flips the two points in each block.
Let z be the central generator of the C_q factor and let sigma be its pure block-translation lift.
Choose x=(1,0), so sigma x=(z,0).
The orbital consists exactly of ordered pairs from a block v to the block v z, with both choices of target bit.
Centrality of z makes this description G-invariant and gives

    s=2, b=d_model, gamma=1.                         (8)

The point stabilizer is the base subgroup H={b in B:b(1)=0}.
Because B is abelian it normalizes H; a block translation normalizes H only if it fixes the distinguished block, hence is the identity.
Therefore N_G(H)=B and N_G(H)/H is C2.
The all-one base vector is a central, fixed-point-free involution of X.
Thus the model permits the root-set involution required by reciprocity; this is a group-theoretic permission, not a reciprocal-polynomial realization.

A base vector commutes with sigma precisely when it is constant on each of sigma's block cycles.
There are t/q=j! such cycles, and every element of the top T commutes with z.
Consequently

    |C_G(sigma)|=2^(j!) t,
    kappa=2^((q-1)j!).                               (9)

Every sigma-cycle on X has length q.
For every fixed positive integer f, once q>f the element sigma^f has the same block cycles and conjugacy-class size (9).
Thus letting q and j grow separates (8) from bounded actual class, bounded fixed-power class and bounded Frobenius-cycle length.

For an abelian subgroup A of G, its image in T is abelian and its kernel has size at most 2^t.
Every abelian subgroup of S_j has order at most 3^(j/3).
To check the latter elementary estimate, its action on each orbit has a transitive abelian image, hence a regular image of size equal to that orbit size.
Faithfulness embeds the subgroup in the product of these images.
If the orbit sizes are n_i, its order is at most product n_i<=3^(sum n_i/3)=3^(j/3); the inequality n<=3^(n/3) for positive integers n follows at n=1,2,3 directly and from decreasing log(x)/x for x>=3 thereafter.
It follows that

    [G:A]>=j!/3^(j/3),                               (10)

which tends to infinity with j.
Thus the bounded-abelian-index specialization of AZ10 is not automatically supplied by this group model.

There is a stronger precise check for AM16's abelian-base relative-degree hypothesis.
The commutator subgroup G' contains the base augmentation subspace of even-weight vectors, because commutators of a coordinate flip with translations give flips at any pair of distinct blocks.
Such a vector can flip either bit of any given block, using another block for its second flip.
The top commutator is {1} times A_j: 3-cycles are commutators of transpositions and generate the even permutations.
Its regular orbit on blocks has size j!/2.
Thus every G'-orbit on X has size at least j!.

Suppose ONLY for this field-theoretic comparison that an actual number-field normal closure has this specified permutation action and alpha labels x.
For any finite abelian extension F/Q, the intersection L intersection F is abelian over Q, so Gal(L/(L intersection F)) contains G'.
Restriction identifies this group with Gal(LF/F).
Its orbit on alpha therefore gives

    [F(alpha):F]>=j!.                                (11)

Hence no finite abelian base supplies a relative degree bounded independently of j in that hypothetical realization.
This is more precise than merely noting that the obvious block quotient T is nonabelian.
It does not exclude every other classical height theorem or supply an arithmetic realization.

If an ACTUAL nontorsion integer-unit input and a residue-Frobenius lift at p=2 realized these orbital parameters, (3) would give m>log2/96.
No such input, prime or near-one family is constructed here.
At a good prime, cycle lengths q would also give no bounded-residue-degree mass as q grows, but no good-prime realization is inferred from abstract permutations.
The useful conclusion is that the orbital criterion is not reducible to the stated old group parameters solely by permutation theory, while its arithmetic supply remains unresolved.

## Author check and next use

The author checked actual pair stabilizers, constant ratio and coordinate fibers, the ambient rather than pair-field non-torsion iteration, ramification in each own degree-D field, every p=2 and exact-power endpoint, the distinct-compatible lower count, both cyclic and direct expenses, strictness and caps, and full original signed norms and exponent costs.
The double-coset orientation, centralizer-orbit lower bound, monotonic comparison with C146, prior residue and abelian-base cases, the corrected S3 reciprocity failure, and every C2-wreath count and field-intersection consequence were separately checked at author level.
Root supplied the orbital mechanism, double-coset comparison prompt, direct extra-depth estimate and the corrected group model; the agent supplied their complete implementation and comparison checks.
No independent review, numerical experiment or actual extra arithmetic coverage is asserted.

The two-parameter statement is reusable because it retains less field degree and more certified compatible mass than the conservative class construction, and includes a direct finite norm alternative.
The outstanding research input is still an actual bounded-prime, bounded-valency, positive-density orbital in the unrestricted near-one arithmetic domain, or another paid lower income.
Full symmetrization, an abstract permutation model, the existence of a local lift and an unrelated weak equidistribution statement do not supply it.


## Current assessment
[Selected decision](#decision-current-complete-residue-mass-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T11:15 |
| status | open |
| reason | Register the complete two-parameter Frobenius orbital criterion, own-ratio-field and full original norm costs, both capped cyclic and extra-depth elementary gaps, exact domination of the conservative class criterion, and the reciprocity-compatible group-only discriminator with its prior-coverage limits. Root and the drafting agent contributed; no independent acceptance or actual new unit/Frobenius realization is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete orbital statement](#statement) | Every actual original nontorsion integer unit and prime/ideal/lift; pair valency and matching density, distinct own-field norm floor, both gap functions, exact full original norm/time costs, class comparison and all quantified group-only scope assertions. |
| argument | [Complete proof](#argument) | Sections1--7 and author boundary: actual pair/ratio fibers, ambient non-torsion, arbitrary ramification, all amplification endpoints, inverse cap and direct norm strictness, full signed return, exact double cosets, prior domains and corrected C2-wreath group calculations. |
| dependency | [Accepted actual pair-orbit mechanism](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Compositum degree, equal coordinate and ratio fibers, cross-exponent unit/non-torsion mechanism and all-original-conjugate height bound; no full d^2 symmetrization is counted as new income. |
| dependency | [Accepted local degree and Frobenius interface](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Supplied residue-Frobenius lift at arbitrary ramification, normalized positive valuation at least reciprocal own-field ramification and e<=D; original selected-source inspection limits remain. |
| dependency | [Accepted complete cyclic inverse](Yin_C_G0147_v5.md#statement) | Actual rho unit and exponent n, Phi5 on its exact positive-height domain, complete capped H5 implication, full original powered multiplicities and monotonicity; not the angular C159 bound. |
| dependency | [Accepted conservative class criterion](Yin_C_G0146_v5.md#statement) | Only the exact g_ll(p,kappa) formula used in the comparison; its centralizer construction is not imposed on the smaller pair field. |
| dependency | [Existing bounded-residue mass exclusion](../ledger/Yin_L_G0205_v1.md#bounded-residue-mass-near-one-escape) | Section6 diagonal-orbital prior-coverage comparison, including repeated reductions and ramified primes; not a new automatic orbital-selection theorem. |
| dependency | [Existing abelian-base relative height](../audits/literature/AM16/Yin_U002.md#am16-u002) | Only the already-covered S3-wreath cyclic-block example with actual abelian base and relative degree at most3; its accepted external proof-inspection scope is unchanged. |
| dependency | [Existing nonreciprocal gap](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only Section1's accepted Smyth theorem in the corrected self-normalizing S3-wreath comparison: an actual integer-unit realization cannot be reciprocal and is already in that class. |
| support | [Original extra-depth norm mechanism](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Credited amplification and elementary triangle-norm architecture, fully specialized with actual orbital density in Sections2--3. |
| support | [Own-ratio and original-norm antecedent](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Credited degree-D valuation and collision accounting, with the signed original return retained at its linked subsection; no assumption sigma preserves the new pair field. |
| support | [Bounded-abelian-index prior coverage](../audits/literature/AZ10/Yin_U001.md#az10-u001) | Existing sufficient class contrasted with the explicit group index lower bound; no claim that every classical height theorem is thereby excluded. |

### Decision whole-reviewed-2026-10-18

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T11:22 |
| status | proved |
| reason | Adopt the complete orbital-valency and matching-density criterion after the actual whole noncontributor R387 review, including ramification-safe own-field amplification, both gap functions, original signed norm/time costs and exact prior-coverage/group boundaries. The abstract group model supplies no actual unit/Frobenius realization and automatic near-one coverage remains open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete orbital statement](#statement) | Every actual original nontorsion integer unit and prime/ideal/lift; pair valency and matching density, distinct own-field norm floor, both gap functions, exact full original norm/time costs, class comparison and all quantified group-only scope assertions. |
| argument | [Complete proof](#argument) | Sections1--7 and author boundary: actual pair/ratio fibers, ambient non-torsion, arbitrary ramification, all amplification endpoints, inverse cap and direct norm strictness, full signed return, exact double cosets, prior domains and corrected C2-wreath group calculations. |
| dependency | [Accepted actual pair-orbit mechanism](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Compositum degree, equal coordinate and ratio fibers, cross-exponent unit/non-torsion mechanism and all-original-conjugate height bound; no full d^2 symmetrization is counted as new income. |
| dependency | [Accepted local degree and Frobenius interface](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Supplied residue-Frobenius lift at arbitrary ramification, normalized positive valuation at least reciprocal own-field ramification and e<=D; original selected-source inspection limits remain. |
| dependency | [Accepted complete cyclic inverse](Yin_C_G0147_v5.md#statement) | Actual rho unit and exponent n, Phi5 on its exact positive-height domain, complete capped H5 implication, full original powered multiplicities and monotonicity; not the angular C159 bound. |
| dependency | [Accepted conservative class criterion](Yin_C_G0146_v5.md#statement) | Only the exact g_ll(p,kappa) formula used in the comparison; its centralizer construction is not imposed on the smaller pair field. |
| dependency | [Existing bounded-residue mass exclusion](../ledger/Yin_L_G0205_v1.md#bounded-residue-mass-near-one-escape) | Section6 diagonal-orbital prior-coverage comparison, including repeated reductions and ramified primes; not a new automatic orbital-selection theorem. |
| dependency | [Existing abelian-base relative height](../audits/literature/AM16/Yin_U002.md#am16-u002) | Only the already-covered S3-wreath cyclic-block example with actual abelian base and relative degree at most3; its accepted external proof-inspection scope is unchanged. |
| dependency | [Existing nonreciprocal gap](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only Section1's accepted Smyth theorem in the corrected self-normalizing S3-wreath comparison: an actual integer-unit realization cannot be reciprocal and is already in that class. |
| support | [Original extra-depth norm mechanism](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Credited amplification and elementary triangle-norm architecture, fully specialized with actual orbital density in Sections2--3. |
| support | [Own-ratio and original-norm antecedent](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Credited degree-D valuation and collision accounting, with the signed original return retained at its linked subsection; no assumption sigma preserves the new pair field. |
| support | [Bounded-abelian-index prior coverage](../audits/literature/AZ10/Yin_U001.md#az10-u001) | Existing sufficient class contrasted with the explicit group index lower bound; no claim that every classical height theorem is thereby excluded. |
| review | [Whole independent orbital finding](../audits/reviews/Yin_R_G0387_v1.md#orbital-ratio-whole-independent-finding) | Complete fixed statement/proof and every declared dependency/support scope, all pair/ratio fibers and local endpoints, H5 cap and direct-depth bounds, full original costs, exact comparison and corrected group-only discriminator. |


### Decision prior-coverage-assessed-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T11:54 |
| status | proved |
| reason | Retain the unchanged complete theorem and R387 whole independent acceptance. The later fixed author comparison applies the already accepted L205 bounded-residue-mass theorem to the actual own-ratio polynomial, covering the entire bounded-p/bounded-s/positive-gamma qualitative class for all nontorsion integer units. This result retains its sharper cyclic inverse, strict direct constants, orbital formulation and original-field transport, but is not a new qualitative gap domain. The comparison has its disclosed author-check scope and is not represented as an extension of R387. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete orbital statement](#statement) | Every actual original nontorsion integer unit and prime/ideal/lift; pair valency and matching density, distinct own-field norm floor, both gap functions, exact full original norm/time costs, class comparison and all quantified group-only scope assertions. |
| argument | [Complete proof](#argument) | Sections1--7 and author boundary: actual pair/ratio fibers, ambient non-torsion, arbitrary ramification, all amplification endpoints, inverse cap and direct norm strictness, full signed return, exact double cosets, prior domains and corrected C2-wreath group calculations. |
| dependency | [Accepted actual pair-orbit mechanism](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Compositum degree, equal coordinate and ratio fibers, cross-exponent unit/non-torsion mechanism and all-original-conjugate height bound; no full d^2 symmetrization is counted as new income. |
| dependency | [Accepted local degree and Frobenius interface](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Supplied residue-Frobenius lift at arbitrary ramification, normalized positive valuation at least reciprocal own-field ramification and e<=D; original selected-source inspection limits remain. |
| dependency | [Accepted complete cyclic inverse](Yin_C_G0147_v5.md#statement) | Actual rho unit and exponent n, Phi5 on its exact positive-height domain, complete capped H5 implication, full original powered multiplicities and monotonicity; not the angular C159 bound. |
| dependency | [Accepted conservative class criterion](Yin_C_G0146_v5.md#statement) | Only the exact g_ll(p,kappa) formula used in the comparison; its centralizer construction is not imposed on the smaller pair field. |
| dependency | [Existing bounded-residue mass exclusion](../ledger/Yin_L_G0205_v1.md#bounded-residue-mass-near-one-escape) | Section6 diagonal-orbital prior-coverage comparison, including repeated reductions and ramified primes; not a new automatic orbital-selection theorem. |
| dependency | [Existing abelian-base relative height](../audits/literature/AM16/Yin_U002.md#am16-u002) | Only the already-covered S3-wreath cyclic-block example with actual abelian base and relative degree at most3; its accepted external proof-inspection scope is unchanged. |
| dependency | [Existing nonreciprocal gap](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only Section1's accepted Smyth theorem in the corrected self-normalizing S3-wreath comparison: an actual integer-unit realization cannot be reciprocal and is already in that class. |
| support | [Original extra-depth norm mechanism](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Credited amplification and elementary triangle-norm architecture, fully specialized with actual orbital density in Sections2--3. |
| support | [Own-ratio and original-norm antecedent](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Credited degree-D valuation and collision accounting, with the signed original return retained at its linked subsection; no assumption sigma preserves the new pair field. |
| support | [Bounded-abelian-index prior coverage](../audits/literature/AZ10/Yin_U001.md#az10-u001) | Existing sufficient class contrasted with the explicit group index lower bound; no claim that every classical height theorem is thereby excluded. |
| review | [Whole orbital finding](../audits/reviews/Yin_R_G0387_v1.md#orbital-ratio-whole-independent-finding) | Complete fixed statement/proof and every declared dependency/support scope, all pair/ratio fibers and local endpoints, H5 cap and direct-depth bounds, full original costs, exact comparison and corrected group-only discriminator. |
| support | [All-unit own-ratio prior-coverage comparison](../ledger/Yin_L_G0398_v1.md#own-ratio-old-mass-proof) | Fixed author-checked composition of accepted L397 and L205 already covers every bounded-p/bounded-s/positive-gamma nontorsion-unit input. This is a coverage assessment, not a new premise or extension of R387. |
| support | [Rank-two Salem subdegree comparison](../audits/literature/AM16/Yin_U004.md#am16-u004) | Established fixed-rank theorem covers every low off-pair Salem subdegree without prime or matching hypotheses; its exact source and original-proof limits remain explicit. |


### Decision current-complete-pair-orbit-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:21 |
| status | proved |
| reason | Select the already complete C477 home for exactly the original L397 ordered-pair/ratio-fiber and full marginal-height mechanism used here. Every original collision, own-field degree, actual unit/non-torsion and fixed scope is present unchanged; only this same-object formal input locator changes. Preserve every other statement/argument/source/support/review relation, mathematical claim, scope and status. The original reviewer is not claimed to have read this later material or R835, and no target or antecedent independent-review obligation is discharged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every actual original nontorsion integer unit and prime/ideal/lift; pair valency and matching density, distinct own-field norm floor, both gap functions, exact full original norm/time costs, class comparison and all quantified group-only scope assertions. |
| argument | [Exact argument](#argument) | Sections1--7 and author boundary: actual pair/ratio fibers, ambient non-torsion, arbitrary ramification, all amplification endpoints, inverse cap and direct norm strictness, full signed return, exact double cosets, prior domains and corrected C2-wreath group calculations. |
| dependency | [Exact dependency](Yin_C_G0477_v1.md#full-ratio-orbits) | Compositum degree, equal coordinate and ratio fibers, cross-exponent unit/non-torsion mechanism and all-original-conjugate height bound; no full d^2 symmetrization is counted as new income. |
| dependency | [Exact dependency](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Supplied residue-Frobenius lift at arbitrary ramification, normalized positive valuation at least reciprocal own-field ramification and e<=D; original selected-source inspection limits remain. |
| dependency | [Exact dependency](Yin_C_G0147_v5.md#statement) | Actual rho unit and exponent n, Phi5 on its exact positive-height domain, complete capped H5 implication, full original powered multiplicities and monotonicity; not the angular C159 bound. |
| dependency | [Exact dependency](Yin_C_G0146_v5.md#statement) | Only the exact g_ll(p,kappa) formula used in the comparison; its centralizer construction is not imposed on the smaller pair field. |
| dependency | [Exact dependency](../ledger/Yin_L_G0205_v1.md#bounded-residue-mass-near-one-escape) | Section6 diagonal-orbital prior-coverage comparison, including repeated reductions and ramified primes; not a new automatic orbital-selection theorem. |
| dependency | [Exact dependency](../audits/literature/AM16/Yin_U002.md#am16-u002) | Only the already-covered S3-wreath cyclic-block example with actual abelian base and relative degree at most3; its accepted external proof-inspection scope is unchanged. |
| dependency | [Exact dependency](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only Section1's accepted Smyth theorem in the corrected self-normalizing S3-wreath comparison: an actual integer-unit realization cannot be reciprocal and is already in that class. |
| support | [Exact support](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Credited amplification and elementary triangle-norm architecture, fully specialized with actual orbital density in Sections2--3. |
| support | [Exact support](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Credited degree-D valuation and collision accounting, with the signed original return retained at its linked subsection; no assumption sigma preserves the new pair field. |
| support | [Exact support](../audits/literature/AZ10/Yin_U001.md#az10-u001) | Existing sufficient class contrasted with the explicit group index lower bound; no claim that every classical height theorem is thereby excluded. |
| review | [Exact review](../audits/reviews/Yin_R_G0387_v1.md#orbital-ratio-whole-independent-finding) | Complete fixed statement/proof and every declared dependency/support scope, all pair/ratio fibers and local endpoints, H5 cap and direct-depth bounds, full original costs, exact comparison and corrected group-only discriminator. |
| support | [Exact support](../ledger/Yin_L_G0398_v1.md#own-ratio-old-mass-proof) | Fixed author-checked composition of accepted L397 and L205 already covers every bounded-p/bounded-s/positive-gamma nontorsion-unit input. This is a coverage assessment, not a new premise or extension of R387. |
| support | [Exact support](../audits/literature/AM16/Yin_U004.md#am16-u004) | Established fixed-rank theorem covers every low off-pair Salem subdegree without prime or matching hypotheses; its exact source and original-proof limits remain explicit. |


### Decision current-complete-prior-coverage-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:39 |
| status | proved |
| reason | Select the complete C483 home for exactly the original L398 own-ratio bounded-residue prior-coverage comparison. The entire original argument, constants and torsion-dependent/descent limits are retained, while every other field, mathematical claim, dependency/support/review relation and scope remains unchanged. R387 is not extended to this later author-only composition or new R841; no new qualitative gap class, old isolation or source-proof audit is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every actual original nontorsion integer unit and prime/ideal/lift; pair valency and matching density, distinct own-field norm floor, both gap functions, exact full original norm/time costs, class comparison and all quantified group-only scope assertions. |
| argument | [Exact argument](#argument) | Sections1--7 and author boundary: actual pair/ratio fibers, ambient non-torsion, arbitrary ramification, all amplification endpoints, inverse cap and direct norm strictness, full signed return, exact double cosets, prior domains and corrected C2-wreath group calculations. |
| dependency | [Exact dependency](Yin_C_G0477_v1.md#full-ratio-orbits) | Compositum degree, equal coordinate and ratio fibers, cross-exponent unit/non-torsion mechanism and all-original-conjugate height bound; no full d^2 symmetrization is counted as new income. |
| dependency | [Exact dependency](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Supplied residue-Frobenius lift at arbitrary ramification, normalized positive valuation at least reciprocal own-field ramification and e<=D; original selected-source inspection limits remain. |
| dependency | [Exact dependency](Yin_C_G0147_v5.md#statement) | Actual rho unit and exponent n, Phi5 on its exact positive-height domain, complete capped H5 implication, full original powered multiplicities and monotonicity; not the angular C159 bound. |
| dependency | [Exact dependency](Yin_C_G0146_v5.md#statement) | Only the exact g_ll(p,kappa) formula used in the comparison; its centralizer construction is not imposed on the smaller pair field. |
| dependency | [Exact dependency](../ledger/Yin_L_G0205_v1.md#bounded-residue-mass-near-one-escape) | Section6 diagonal-orbital prior-coverage comparison, including repeated reductions and ramified primes; not a new automatic orbital-selection theorem. |
| dependency | [Exact dependency](../audits/literature/AM16/Yin_U002.md#am16-u002) | Only the already-covered S3-wreath cyclic-block example with actual abelian base and relative degree at most3; its accepted external proof-inspection scope is unchanged. |
| dependency | [Exact dependency](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only Section1's accepted Smyth theorem in the corrected self-normalizing S3-wreath comparison: an actual integer-unit realization cannot be reciprocal and is already in that class. |
| support | [Exact support](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Credited amplification and elementary triangle-norm architecture, fully specialized with actual orbital density in Sections2--3. |
| support | [Exact support](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Credited degree-D valuation and collision accounting, with the signed original return retained at its linked subsection; no assumption sigma preserves the new pair field. |
| support | [Exact support](../audits/literature/AZ10/Yin_U001.md#az10-u001) | Existing sufficient class contrasted with the explicit group index lower bound; no claim that every classical height theorem is thereby excluded. |
| review | [Exact review](../audits/reviews/Yin_R_G0387_v1.md#orbital-ratio-whole-independent-finding) | Complete fixed statement/proof and every declared dependency/support scope, all pair/ratio fibers and local endpoints, H5 cap and direct-depth bounds, full original costs, exact comparison and corrected group-only discriminator. |
| support | [Exact support](Yin_C_G0483_v1.md#own-ratio-old-mass-proof) | Fixed author-checked composition of accepted L397 and L205 already covers every bounded-p/bounded-s/positive-gamma nontorsion-unit input. This is a coverage assessment, not a new premise or extension of R387. |
| support | [Exact support](../audits/literature/AM16/Yin_U004.md#am16-u004) | Established fixed-rank theorem covers every low off-pair Salem subdegree without prime or matching hypotheses; its exact source and original-proof limits remain explicit. |


### Decision current-complete-residue-mass-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:42 |
| status | proved |
| reason | Maintain exactly the current original L205 dependency as the complete same-object C491 proof home after reading the full needed consumer scope and complete C491 Sections1--5/equations1--15. Its actual original-degree/all-input/repeated-reduction/no-index-or-ramification-hypothesis mass bound, full same-exponent and cost scope is unchanged. Every other field except this actual date/reason, all nonmatching relations and scopes, review tuples, Statement/Argument, original source/authority and old decisions remain unchanged. Existing review findings keep their actual old inputs; this maintenance does not assert that an old reviewer read C491, add whole independent coverage or select a research Task/E. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every actual original nontorsion integer unit and prime/ideal/lift; pair valency and matching density, distinct own-field norm floor, both gap functions, exact full original norm/time costs, class comparison and all quantified group-only scope assertions. |
| argument | [Exact argument](#argument) | Sections1--7 and author boundary: actual pair/ratio fibers, ambient non-torsion, arbitrary ramification, all amplification endpoints, inverse cap and direct norm strictness, full signed return, exact double cosets, prior domains and corrected C2-wreath group calculations. |
| dependency | [Exact dependency](Yin_C_G0477_v1.md#full-ratio-orbits) | Compositum degree, equal coordinate and ratio fibers, cross-exponent unit/non-torsion mechanism and all-original-conjugate height bound; no full d^2 symmetrization is counted as new income. |
| dependency | [Exact dependency](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Supplied residue-Frobenius lift at arbitrary ramification, normalized positive valuation at least reciprocal own-field ramification and e<=D; original selected-source inspection limits remain. |
| dependency | [Exact dependency](Yin_C_G0147_v5.md#statement) | Actual rho unit and exponent n, Phi5 on its exact positive-height domain, complete capped H5 implication, full original powered multiplicities and monotonicity; not the angular C159 bound. |
| dependency | [Exact dependency](Yin_C_G0146_v5.md#statement) | Only the exact g_ll(p,kappa) formula used in the comparison; its centralizer construction is not imposed on the smaller pair field. |
| dependency | [Exact dependency](Yin_C_G0491_v1.md#bounded-residue-mass-near-one-escape) | Section6 diagonal-orbital prior-coverage comparison, including repeated reductions and ramified primes; not a new automatic orbital-selection theorem. |
| dependency | [Exact dependency](../audits/literature/AM16/Yin_U002.md#am16-u002) | Only the already-covered S3-wreath cyclic-block example with actual abelian base and relative degree at most3; its accepted external proof-inspection scope is unchanged. |
| dependency | [Exact dependency](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only Section1's accepted Smyth theorem in the corrected self-normalizing S3-wreath comparison: an actual integer-unit realization cannot be reciprocal and is already in that class. |
| support | [Exact support](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Credited amplification and elementary triangle-norm architecture, fully specialized with actual orbital density in Sections2--3. |
| support | [Exact support](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Credited degree-D valuation and collision accounting, with the signed original return retained at its linked subsection; no assumption sigma preserves the new pair field. |
| support | [Exact support](../audits/literature/AZ10/Yin_U001.md#az10-u001) | Existing sufficient class contrasted with the explicit group index lower bound; no claim that every classical height theorem is thereby excluded. |
| review | [Exact review](../audits/reviews/Yin_R_G0387_v1.md#orbital-ratio-whole-independent-finding) | Complete fixed statement/proof and every declared dependency/support scope, all pair/ratio fibers and local endpoints, H5 cap and direct-depth bounds, full original costs, exact comparison and corrected group-only discriminator. |
| support | [Exact support](Yin_C_G0483_v1.md#own-ratio-old-mass-proof) | Fixed author-checked composition of accepted L397 and L205 already covers every bounded-p/bounded-s/positive-gamma nontorsion-unit input. This is a coverage assessment, not a new premise or extension of R387. |
| support | [Exact support](../audits/literature/AM16/Yin_U004.md#am16-u004) | Established fixed-rank theorem covers every low off-pair Salem subdegree without prime or matching hypotheses; its exact source and original-proof limits remain explicit. |

