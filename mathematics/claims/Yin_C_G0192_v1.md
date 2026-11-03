---
author: Yin
---
# Totally real integral unit residuals and the sharp protected coefficient

Date: 2026-10-20T11:57.
Human author Yin.
Root proposed and supplied the unit-residual existence route, the two-adic local construction, the direct adelic-set interface and the global capacity assembly.
The entropy_attainment_bridge agent supplied the full generic curve and boundary calculation and the nonzero odd-prime Hensel construction, after checking the initial root constructions.
The draft_inventory_later agent performed the primary-source follow-up and contributed to the finite-place, good-model and source-application checks.
All three are contributors; none independently reviews this whole existence theorem.
The draft_comparison_cleanup agent separately prechecked the earlier geometric and local author sections without contributing a construction; its whole review of this actual fixed theorem remains separate.
No new mathematical program, numerical root, parameter scan or explicit global point computation is a premise.

## Statement

For each s in{1,-1} there exist a totally real number field F and nonzero algebraic integers a,b,c in F such that

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5 belongs to O_F^times.               (1)

The field may be taken to be the actual generated field Q(a,b,c).
In particular, writing r=[F:Q] and

    e=b^2-a^3, f=2c^2-3a^5,
    Q_(s,lambda)=(e+s g)^2+f^2+lambda g^2,

one has, on the produced triple,

    abs(Norm_F(g))=1,
    Norm_F(Q_(s,1))=1<2^r,
    Norm_F(Q_(s,lambda))=lambda^r<2^r
                 for every rational0<lambda<2.    (2)

Consequently the proposed residual exponential floor abs(Norm_F(g))>=2^(r/2), and the unbuffered universal floor Norm_F(Q_(s,1))>=2^r, are false on their stated abstract totally real integral-triple domain.
Among positive rational constants lambda, the universal inequality Norm_F(Q_(s,lambda))>=2^[F:Q] for all nonzero totally real integral triples and both signs holds exactly for lambda>=2.
At lambda=2 the new triples attain equality, and the original three-square e^2+f^2+g^2 also has full norm exactly2^r on them.

This is an existence theorem without an explicit defining polynomial or a prescribed degree for F.
It does not assert that a,b,c are simultaneously the three actual trace quotients of one original reciprocal polynomial P.
It supplies no counterexample to the original G0001 Mahler contract and no failure of a lower bound restricted to a more constrained original-input class.

<a id="argument"></a>
## Complete proof

Fix s throughout.
All rational functions and curves below are defined over Q.
The proof constructs nonpolar integral local sets and proves their supercritical capacity before using the exact external global existence theorem.
It does not infer global solvability from separate local points.

<a id="unit-curve-and-boundary"></a>
### 1. The actual curve and all removed points

Put

    D(u)=108^3-2u^5, N(u)=216-u^2,
    s t^9 D(u)=N(u),
    a=6t^2, b=ut^3, c=108t^5,
    g=t^15D(u)=s t^6N(u), h=1/g.                 (3)

The polynomials D,N have simple roots and no common root.
A common root would imply216^5=(108^3/2)^2, but these numbers are respectively2^15*3^15 and2^10*3^18 and are unequal.
At a simple zero of N the degree-nine polynomial T^9-N/(sD) is Eisenstein over the corresponding discrete valuation ring of C(u).
It is therefore irreducible over C(u); the function field in(3) is geometrically integral and has degree9 over Q(u).
Let C/Q be its smooth projective curve.
Existence of the smooth projective model of a one-variable function field in characteristic zero is used here in its usual curve form: normalize a projective closure; a normal curve over the perfect field Q is smooth.

The displayed rational functions satisfy both equations in(1) identically.
Conversely, on their locus a!=0, t=c/(3a^2) and u=b/t^3 recover the same equation from the residual identities.
There is no reliance on an extra unrelated curve component.
For the existence argument it suffices to work with the one geometrically integral curve just constructed and its explicit coordinate functions.

The complete orders on C are as follows.

| Points | Local orders and values | Rational closed orbit |
| --- | --- | --- |
| D(u)=0 | One point over each simple root u_0. The parameter1/t has order1, ord(u-u_0)=9, and the orders of a,b,c,g,h are -2,-3,-5,-6,6. | One degree5 orbit x_D, since u_0=18/v with v^5=3. Exactly one geometric point is real. |
| N(u)=0 | One point over each root u_0=±6sqrt6. The parameter t has order1, ord(u-u_0)=9, and the orders of a,b,c,g,h are2,3,5,15,-15. | One degree2 orbit x_N, with residue field Q(sqrt6), both geometric points real. |
| u=infinity | Three points, ord(t)=1, ord(u)=-3, b=ut^3 tends to beta with beta^3=s/2; a,c tend to0 and g tends to-2beta^5!=0. | One degree3 orbit, finite for all a,b,c,h. It is not removed. |

For the first two rows the derivative of the vanishing factor in u is nonzero and the other factor is a unit.
The implicit equation therefore gives exactly the stated parameters and residue fields, without a hidden residue extension in the index-nine ramification.
The degree5 assertion uses Eisenstein for v^5-3; the degree2 assertion uses X^2-6.
For the last row put v=1/u=t^3/b.
The equation becomes

    b^3(1-629856v^5)=(s/2)(1-216v^2).             (4)

At t=0 each root beta^3=s/2 has nonzero derivative3beta^2 after substituting v=t^3/b.
It determines a regular branch with parameter t and order3 for v.
The three branches account for all degree9 above u=infinity.
The reciprocal of beta has Eisenstein polynomial X^3-2s, establishing the stated residue orbit.
At every other point t,u and the displayed coordinates have no pole and g has no zero.
The pole sets of a,b,c,h are thus exactly the seven geometric points in the two closed orbits

    X={x_D,x_N}, U=C minus X.                    (5)

All four coordinate functions are regular on U and gh=1 there.
Each of the two removed rational closed points has a real smooth geometric branch.
The four nonreal geometric points in x_D are retained in the global pole set and capacity calculation.
They are not silently discarded to impose total reality.

<a id="finite-local-integral-points"></a>
### 2. Actual nonzero integral points at every finite prime

For an odd prime p, take a finite extension L/Q_p containing beta with beta^3=s/2.
This beta is a unit.
For a nonzero integral t of sufficiently large positive valuation consider

    P_t(B)=B^2-216t^6+s(108^3t^15-2B^5).

At t=0 the value at beta is0 and the derivative is-3beta!=0.
The coefficients are integral and, by choosing t sufficiently small,

    v(P_t(beta))>2v(3beta).

The exact complete-valued-field strong Hensel theorem in [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) supplies a root b with v(b-beta)>v(3beta)>=0.
Hence b is a unit, a=6t^2 and c=108t^5 are nonzero integral elements, both residual equations hold, and g=c^3-2b^5 and h are units.
This includes p=3: the derivative need not be a unit, which is precisely why the strong inequality was checked.

At p=2, take c=1 and a root a^5=2/3 in a finite extension.
Then a is integral with positive valuation.
In a finite splitting extension, normalized by v(2)=1, consider

    P(B)=B^2-2s B^5+s-a^3.

Its constant coefficient is a unit.
A root cannot have positive valuation, since the constant would then be the sole smallest term.
For a root with negative valuation w, the two nonconstant terms must tie, giving1+5w=2w and w=-1/3.
Vieta's product identity gives the sum of all five root valuations, counted with multiplicity, as-1.
Exactly three roots therefore have valuation-1/3 and two have valuation0.
Choose either unit root b.
Then a,b,c,h are integral, all a,b,c are nonzero, and g=1-2b^5 is a unit.
No assertion that this local splitting field is totally real is involved.

Each local point has t!=0 and D(u)!=0 because a,c,g are nonzero.
The derivative of s t^9D(u)-N(u) with respect to t is9s t^8D(u)!=0.
These are smooth points of the displayed generic curve and hence points of C in U.
Only a,b,c,h are required to be integral: at p=2 the recovered t has valuation-2/5, so imposing t-integrality would wrongly delete the constructed point.

<a id="finite-compatible-local-sets"></a>
### 3. One finite exceptional set and actual compatible finite-place sets

Fix a projective embedding of C over Q.
After excluding finitely many primes S_0, its projective closure model is smooth, the closures of X are finite etale with distinct geometric specializations, and a,b,c,h extend as regular functions on the complement of those closures.
Here the finite-exception assertion has its standard precise spreading-out content.
The smooth projective curve, the finite reduced divisor X, and the four regular sections on its open complement are all defined by finitely many equations, transition expressions and denominators over Q.
They spread to Z[1/M] for some nonzero integer M.
Smoothness of the projective closure and finite etaleness of the reduced divisor hold after enlarging M, since the generic fiber is smooth and the divisor is separable; their bad loci have closed image on this one-dimensional base by properness or finiteness and miss its generic point.
A finite affine cover of the open complement and the finitely many rational expressions for the four sections allow their remaining denominators to be cleared by one further enlargement of M.
Thus the same finite set works simultaneously for the curve, all seven geometric poles and all four coordinate functions.
No assertion of good reduction at every prime or integrality of the parameters t,u is needed.

For p outside S_0 take E_p to be the standard X-trivial Berkovich set: the inverse image of the reduction curve with the seven geometric specializations of X removed.
It is compact and disjoint from X, and is stable under all continuous automorphisms of C_p over Q_p.
It is nonpolar: over the algebraic residue field, the smooth reduction curve has points away from that finite set, and their tubes contain nonempty local analytic discs.
Every algebraic point of E_p has all four coordinate values in the local valuation ring.
Indeed properness extends it to the model over the valuation ring of its field of definition, its reduction lies in the open complement, and the four sections are regular there.
These are exactly the X-trivial sets in [Rum13-U001](../audits/literature/Rum13/Yin_U001.md#compatible-berkovich-adelic-set).

For each of the finitely many p in S_0 choose the local point from Section2 and a finite extension L/Q_p defining it.
All four functions are analytic near that smooth point and have integral values there.
Continuity gives a sufficiently small neighborhood on which each function differs from its center value by an element of absolute value strictly less than1; hence its own absolute value is at most1 throughout.
Shrink the neighborhood also to avoid X.
The precise small-ball parametrization in [Rum13-U001](../audits/literature/Rum13/Yin_U001.md#small-local-disc-interface) permits a positive-radius closed analytic disc inside this neighborhood, with radius in |Q_p^times|, strictly smaller than the parametrization radius.
It is a strict closed Berkovich affinoid, compact and nonpolar.
Use spherical balls for the fixed Q-projective embedding, so the disc is stable under every automorphism fixing its center, and take its finitely many local Galois conjugates.
Their union E_p is still compact, nonpolar, disjoint from X, and now stable under Aut_c(C_p/Q_p).
The rationality of a,b,c,h preserves their integral bounds on every conjugate disc.
The center may belong to a proper finite local extension; Theorem1.6(C1) requires invariance of the union, not Q_p-rationality of each center.

We now have a fixed family(E_p) at every finite prime.
Its only exceptional places form a finite set, its sets have the required strict-affinoid form there, and all its algebraic points have integral a,b,c,h.
No global normal arithmetic surface or extra normalization coordinates are required for this direct curve application.

<a id="real-arcs-and-supercritical-capacity"></a>
### 4. Two real arcs and the full global capacity

Choose one real geometric point A_D in x_D and one A_N in x_N.
At each take a real analytic coordinate z_i vanishing at A_i and a small positive real segment0<z_i<=delta_i which meets no other point of X.
Choose the two coordinate neighborhoods disjoint.
For epsilon_n decreasing to0 with0<epsilon_n<min(delta_D,delta_N), let K_(i,n) be the closed segment epsilon_n<=z_i<=delta_i, and put

    E_(infinity,n)=K_(D,n) union K_(N,n).

Each set is a compact union of two nondegenerate connected subsets of C(R), is pointwise fixed by complex conjugation, is nonpolar, and avoids all seven geometric points of X.
These sets increase with n.
Together with the fixed finite-place sets they give Q-rational compatible Berkovich adelic sets E_n meeting the exact local forms of Rumely's Theorem1.6.

We prove that their actual global Cantor capacities tend to infinity.
Use the fixed global-pole uniformizers and natural-log normalization specified in [Rum13-U001](../audits/literature/Rum13/Yin_U001.md#cantor-capacity-normalization), with all finite and archimedean place weights and the splitting-extension divisor intact.
The local canonical kernel at A_i is comparable, with fixed positive constants, to the inverted spherical metric

    rho_(A_i)(y,z)=||y,z||/(||y,A_i|| ||z,A_i||).

For the fixed endpoint B_i with z_i=delta_i and the moving endpoint Z_(i,n) with z_i=epsilon_n, this metric tends to infinity.
The checked arc-capacity bound in [QY26-U002](../audits/literature/QY26/Yin_U002.md#arc-capacity-and-exhaustion), with the precise canonical-distance comparison from Rumely, gives a constant c_i>0 independent of n such that

    cap_(A_i)(K_(i,n))
       >=c_i diam_(rho_(A_i))(K_(i,n)) -> infinity.

Equivalently its single-pole Robin constant tends to negative infinity.
By monotonicity the Robin constant of the larger E_(infinity,n), with the same pole A_i, also tends to negative infinity.
For every other geometric pole its Robin constant is bounded above by the value for the fixed initial nonpolar E_(infinity,1).
Every cross-Green entry is nonnegative and bounded above by its initial value, by the exact energy and Green monotonicity in [Rum13-U001](../audits/literature/Rum13/Yin_U001.md#single-pole-robin-and-green-monotonicity).
All the finite-place matrices remain fixed, with only finitely many nonzero local contributions in the fixed normalization.

Retain the entire global geometric-point matrix over a finite normal field splitting X, with the normalized sum over all its places.
Its Galois stability permits the two-block average indexed by the Q-closed points x_D,x_N, exactly as in [QY26-U002](../audits/literature/QY26/Yin_U002.md#closed-point-cantor-capacity).
The averaging includes positive degree weights for every geometric point, not only the chosen real branch.
In each diagonal block at least one real-branch Robin contribution tends to negative infinity, while every other diagonal or cross contribution in that block is bounded above.
Therefore, for the resulting two-by-two matrix Gamma_n=(c_(i,j,n)),

    c_(D,D,n)->-infinity, c_(N,N,n)->-infinity,
    0<=c_(D,N,n)<=c_(D,N,1)<infinity.             (6)

This block averaging preserves Cantor capacity.
One can also see the minimax invariance directly: average a row probability vector over the finite Galois group; concavity of its minimum against column strategies makes this no worse.
Against an invariant row vector, column probabilities may likewise be averaged without changing the payoff.
Thus both strategies reduce to total masses on the two geometric orbits and the payoffs are their block averages, with every original orbit multiplicity included.

For a matrix Gamma the convention is val(Gamma)=sup_s inf_r s^T Gamma r, with both vectors in the probability simplex.
Taking the particular column vector r=(1/2,1/2) gives

    val(Gamma_n)
      <=(1/2)max_i sum_j c_(i,j,n) ->-infinity.

Hence

    cap_X(E_n)=exp(-val(Gamma_n))->infinity.       (7)

Some finite n consequently has cap_X(E_n)>1.
This proof uses only the checked local arc estimate, monotonicity and global matrix definitions.
It reproduces the capacity-only part of QY26's Lemma7.7 without invoking that full lemma, its GVF hypothesis, its functional approximation, or its other global construction.

<a id="global-output-and-norm"></a>
### 5. The exact global theorem and the resulting original triple

Fix an n for which(7) is strictly greater than1 and let S consist of infinity and S_0.
The curve C is smooth, geometrically integral and projective over Q; X is the complete finite Galois-stable seven-point pole set.
Each E_v is compact, nonpolar, disjoint from X and locally Galois stable.
Outside S it is X-trivial.
At infinity it is a finite union of compact connected real arcs, and at the exceptional finite places it is a finite union of strict closed Berkovich affinoids.
All hypotheses of the actually inspected early-manuscript [Rumely Theorem1.6](../audits/literature/Rum13/Yin_U001.md#compact-set-fekete-szego-lrc) have now been verified.
That theorem supplies infinitely many algebraic points P of C whose entire global Q-conjugate orbit lies in E_v at every place v.
The theorem gives containment in the sets themselves; no complex neighborhood enlargement is substituted for the real constraint.
Choose one such P.

The point lies in U and the four coordinates a(P),b(P),c(P),h(P) satisfy the two residual equations and gh=1.
Every embedding of its field of definition into every local algebraic closure sends it to the prescribed E_p, so each of the four coordinates is integral at every finite place.
They are therefore algebraic integers.
Every complex embedding sends P to the real arcs; all four coordinate values under every embedding are real.
Their generated field, equivalently F=Q(a(P),b(P),c(P)) because h=1/g, is totally real.
Since both g and h are integral with gh=1, g is a unit and abs(Norm_F(g))=1.
This uses the complete original norm in the actual chosen field F, not one selected real embedding or a smaller own-field norm without its extension exponent.

The coordinates a,b,c are automatically nonzero.
If a=0 or c=0, the first relation gives both0; gh=1 then forces b!=0 and2s b^3=1, impossible for a global algebraic integer at a prime above2.
If b=0, then a,c are nonzero and a^3=s c^3.
At a prime above3, write A=v(a), C_0=v(c), e_3=v(3)>0.
These equations give A=C_0 and2C_0=e_3+5A, hence-3A=e_3, impossible for an integral a.
Thus(1) holds on the exact requested nonzero domain.
The construction applies to each of the two fixed signs s.

In this residual situation e=-s g and f=0, so Q_(s,lambda)=lambda g^2.
For rational lambda>0 its full norm is lambda^r Norm_F(g)^2=lambda^r.
This proves(2), as well as equality at lambda=2 and for e^2+f^2+g^2=2g^2.
No prescribed degree, explicit global polynomial or numerical norm computation is used.

<a id="protected-coefficient-sharpness"></a>
### 6. Sufficiency and sharpness of the coefficient2 on the entire abstract domain

For completeness, the upper direction uses exactly the accepted pairwise exclusions in [C153v2](Yin_C_G0153_v2.md#statement): over a totally real field, neither(e,g) nor(f,g) can vanish simultaneously for nonzero a,b,c.
Put x=e+s g.
If at least two of x,f,g are nonzero, choose two such integral elements once in F.
For lambda>=2 their coefficients in x^2+f^2+lambda g^2 are each at least1.
Every real embedding therefore gives a lower bound2|sigma(u)sigma(v)|, and multiplying all r inequalities gives a full norm at least2^r.
If only x were nonzero, f=g=0 would contradict C153v2; if only f were nonzero, x=g=0 would imply e=g=0 and the same contradiction.
All three zero is also excluded.
The only singleton possibility is g!=0 and x=f=0, when the norm is lambda^r Norm_F(g)^2>=2^r.
This proves sufficiency for every rational lambda>=2.
The unit triples already proved give failure for every rational0<lambda<2 and equality at2, completing the exact sharpness statement.

<a id="inputs-and-limits"></a>
## Inputs, original scope and actual review boundaries

The new global existence step is the established external Fekete–Szegö theorem at the actual early-manuscript statement/applicability scope recorded in Rum13-U001.
Its long patching proof was not independently re-audited, and no equivalence with the unavailable published 2013 version is claimed.
The local canonical-kernel, equilibrium and monotonicity inputs retain their recorded earlier-source limits.
QY26-U002 supplies the actually read arc-lemma proof and closed-point capacity conventions; the project supplies its own full finite-set and two-arc application above.
The complete QY26 GVF lemma or general integral-point theorem is not a premise.

| Input | Exact use |
| --- | --- |
| [Rum13-U001](../audits/literature/Rum13/Yin_U001.md#rum13-u001) | Actual 2012 early-manuscript Theorem1.6, compact compatible sets, all place/degree normalizations, local discs, canonical distance and Green/Robin monotonicity at the explicitly recorded inspection limits. |
| [QY26-U002](../audits/literature/QY26/Yin_U002.md#qy26-u002) | Complete displayed arc bound and the two closed-orbit minimax convention; the capacity subargument is reproduced here without invoking the full GVF lemma. |
| [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Strong Hensel theorem for each actual complete finite extension, including a nonunit derivative at3. |
| [C153v2](Yin_C_G0153_v2.md#statement) | Only its abstract pairwise radical exclusion, in the sufficiency direction for lambda>=2; not a construction of an original polynomial or a source for the new unit residual. |
| Standard curve and integral-model facts | Smooth projective model of a characteristic-zero one-variable function field, finite-presentation spreading outside finitely many primes, proper valuative extension, and algebraic integrality at all finite places. Their particular hypotheses and applications are specified in Sections1,3,5. No resolution of an arithmetic surface is used. |
| Elementary exact algebra | Eisenstein at the simple zero, implicit regular branches, valuations and Vieta with multiplicities, and the full number-field norm product. All identities and relevant exceptional cases are displayed. |

The actual field F need not be an originally proposed field, and no same-polynomial trace realization is supplied.
Even a separate theorem realizing a totally real field as a Salem trace field would not realize these three specified functions simultaneously as its divided self-composition remainders.
The accepted buffered norm floor survives and is sharp on this abstract domain.
A stronger bound for a restricted original-input class, or a transfer argument using additional original arithmetic information, remains a separate question.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T11:57 |
| status | open |
| reason | Register the complete geometric, local, capacity and global proof of actual totally real unit residuals and the exact protected-coefficient threshold for whole independent review. No original-polynomial realization or Mahler conclusion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Unit residual existence and sharp threshold](#statement) | Both signs, actual totally real integral nonzero triples, full unit norm, refutation of the abstract unbuffered floor and exact rational coefficient threshold. |
| argument | [Complete existence and sharpness proof](#argument) | All boundary points, finite-prime points and compact sets, finite good-model exceptions, complete averaged capacity, actual global output and full norm. |
| dependency | [Exact primary splitting and potential theory](../audits/literature/Rum13/Yin_U001.md#rum13-u001) | Actual early-manuscript theorem, local forms and normalizations at the stated external-proof inspection limits. |
| dependency | [Checked arc and closed-point mechanism](../audits/literature/QY26/Yin_U002.md#qy26-u002) | Arc bound and Galois orbit capacity; no use of the full GVF lemma after dropping a hypothesis. |
| dependency | [Strong complete-field Hensel theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Only the displayed nonzero odd-prime local root construction under its strict derivative inequality. |
| dependency | [Accepted pairwise exclusions](Yin_C_G0153_v2.md#statement) | Only the universal sufficiency of coefficient2 and larger, with the exact abstract nonzero totally real domain. |
| support | [Full input and authorship account](#inputs-and-limits) | Standard model facts with checked application hypotheses, exact inspected source versions, contributors, no computation and no original-P realization. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T12:05 |
| status | proved |
| authority | Internal adoption within Yin's selected residual singleton inquiry. |
| reason | Adopt the complete existence of totally real integral unit residuals for both signs through whole R466. This refutes the stated abstract unbuffered exponential floor and proves coefficient2 is the exact universal protected threshold. The complete source and all-place application limits remain explicit; no original-polynomial realization or Mahler counterexample is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Unit residual existence and sharp threshold](#statement) | Both signs, actual totally real integral nonzero triples, full unit norm, refutation of the abstract unbuffered floor and exact rational coefficient threshold. |
| argument | [Complete existence and sharpness proof](#argument) | All boundary points, finite-prime points and compact sets, finite good-model exceptions, complete averaged capacity, actual global output and full norm. |
| dependency | [Exact primary splitting and potential theory](../audits/literature/Rum13/Yin_U001.md#rum13-u001) | Actual early-manuscript theorem, local forms and normalizations at the stated external-proof inspection limits. |
| dependency | [Checked arc and closed-point mechanism](../audits/literature/QY26/Yin_U002.md#qy26-u002) | Arc bound and Galois orbit capacity; no use of the full GVF lemma after dropping a hypothesis. |
| dependency | [Strong complete-field Hensel theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Only the displayed nonzero odd-prime local root construction under its strict derivative inequality. |
| dependency | [Accepted pairwise exclusions](Yin_C_G0153_v2.md#statement) | Only the universal sufficiency of coefficient2 and larger, with the exact abstract nonzero totally real domain. |
| support | [Full input and authorship account](#inputs-and-limits) | Standard model facts with checked application hypotheses, exact inspected source versions, contributors, no computation and no original-P realization. |
| review | [Whole existence finding](../audits/reviews/Yin_R_G0466_v1.md#unit-residual-existence-whole-independent-finding) | Entire actual fixed proof, all geometry and local sets, complete capacity weights and source application, full original-field output and exact protected-coefficient threshold. |

