---
author: Yin
---

# G0001: dissociated colors, exact cyclic induction and embedding-cost boundaries

Date: 2026-10-07.
Direct proofs by assigned AI review_matrix_completion for Yin, within the coordinator's bounded multi-embedding moment investigation.
This note reuses L G0003's exact cyclic coordinates and L G0086's character calculation.
No new source or computation is used.
Its positive mechanism is preservation of colors under full cyclic induction; selection of one field factor is treated separately and has an explicit counterexample.
No common color bound on the small-Mahler class is asserted.

<a id="dissociated-colors-and-cost"></a>
## Exact color criterion and its entropy cost

For a sequence of nonzero elements v_j of an abelian group, call an index set I dissociated when every finitely supported relation sum_(j in I) epsilon_j v_j=0 with epsilon_j in {-1,0,1} has all coefficients zero.
Indices, rather than just distinct values, are retained: two equal orbit elements already give a forbidden signed relation.
Define chi_n as the least number of colors partitioning {0,...,n-1} into dissociated classes.
Singletons show chi_n<=n.
Write chi_infinity=sup_n chi_n.
If this supremum is a finite integer b, the whole infinite sequence admits a b-coloring.
To see this, take colorings of arbitrarily long prefixes, pass to an infinite subsequence with the same first color, then the same second color, and so on.
Every finite prefix of the resulting coloring occurs in an admissible finite coloring.
Every forbidden relation is finite, so none occurs.
This also proves the converse identification.

For independent fair binary digits, conditioning on every digit outside a dissociated set I gives 2^|I| distinct values with equal conditional probabilities.
Thus the maximum atom obeys

    p_n^*<=2^(-|I|),
    p_n^*<=2^(-ceil(n/chi_n)).                            (1)

On an algebraic-unit orbit v_j=alpha^j, the fixed-order entropy limits and the accepted total entropy bound imply

    chi_infinity<=b<infinity
       implies h_infinity>=log2/b and m(P)>=log2/b.        (2)

The entropy interfaces are those retained in [L G0030](Yin_L_G0030_v1.md#renyi-rates) and [L G0002](Yin_L_G0002_v1.md#rational-primary-formula).
More generally any dissociated sets I_n in the first n indices satisfy

    limsup_n |I_n|/n<=h_infinity/log2<=m(P)/log2.          (3)

Consequently a common bounded-color theorem already supplies a gap by maximum-atom conditioning, without first passing through a high-moment estimate.

It also gives that estimate.
The convex-product proof of [L G0086](Yin_L_G0086_v1.md#elementary-house-moment-bound) uses only dissociation within each class, not an ordering of the exponents.
With b classes, its Holder and angular-average steps therefore give

    A_(n,r)<=(2e b r n)^r for all r>=1.                   (4)

For a particular partition with class sizes n_1,...,n_b>0, one may replace bn in the moment-generating bound by

    V=(sum_l sqrt(n_l))^2<=bn,
    A_(n,r)<=(2e r V)^r.                                 (5)

Indeed Holder with exponents p_l satisfying sum 1/p_l=1 gives variance proxy sum p_l n_l.
The choice p_l=(sum sqrt(n_j))/sqrt(n_l) minimizes it, as follows also from Cauchy--Schwarz.
Applying the same angular coefficient calculation proves (5).
This accounts for unequal class sizes; it is not an assumption of probabilistic independence between the classes.

<a id="exact-dissociation-under-cyclic-induction"></a>
## Full cyclic induction preserves the exact color number

Let psi be an automorphism of an abelian group B and v!=0.
On B^k let

    Phi(b_0,...,b_(k-1))=(psi b_(k-1),b_0,...,b_(k-2)),
    w=iota_0(v).

As in [L G0003](Yin_L_G0003_v1.md#g0001-cyclic-induction), Phi^(ak+s)w=iota_s(psi^a v).
If an index set I is split by its residues modulo k, a signed relation among its Phi-orbit elements is zero if and only if its separate signed sums in all k coordinates are zero.
Therefore I is dissociated if and only if every residue restriction, with indices divided by k, is dissociated in the corresponding base orbit.

Write n=ak+s with 0<=s<k, and set chi_0=0.
The k coordinate prefixes have lengths a or a+1.
Restriction of any coloring gives the lower bound by their maximum color number.
Conversely color each coordinate optimally and reuse the same color names across the different coordinates: a same-color union remains dissociated by the direct-sum criterion.
It follows exactly that

    chi_n(Phi,w)=chi_ceil(n/k)(psi,v),
    chi_infinity(Phi,w)=chi_infinity(psi,v).               (6)

In particular no factor k is paid in (4).
This is different from applying Holder to k arbitrary residue classes which are not known to be independent direct summands.

For a whole polynomial module, the residue decomposition

    Z[t]/(P(t^k))=direct-sum_(s=0)^(k-1)
                      t^s (Z[u]/(P(u))),    u=t^k,

provides precisely these coordinates, without an irreducibility hypothesis.
For a selected algebraic root alpha with alpha^k=beta, the same conclusion holds if

    [Q(alpha):Q(beta)]=k.                                 (7)

Indeed 1,alpha,...,alpha^(k-1) are then linearly independent over Q(beta); splitting an integer relation by residues is faithful.
On the monogenic orders the spanning decomposition is also exact.
Without (7), projecting the full module to a selected field can introduce signed relations between its former coordinates.

<a id="radical-colors-with-vanishing-house"></a>
## An irreducible radical control where the house cost is artificial

Let phi=(1+sqrt5)/2 and k=2^s, s>=0.
For the positive root alpha=phi^(1/k), the retained norm argument in [C212 radical proof](../claims/Yin_C_G0212_v1.md#radical-collision-control) proves irreducibility of t^(2k)-t^k-1 and relative degree k over Q(phi).
Briefly, each successive chosen root has even degree, monic minimal polynomial with constant term -1 and norm -1.
It cannot be a square in its own field, because the rational norm of a square is a square.
Each square-root step therefore doubles the degree.

The base powers of phi have exactly two colors: parity gives two dissociated classes because phi^2>2, while phi^2-phi-1=0 excludes one color.
More precisely its prefix color number is one for lengths 1 and 2, and two thereafter.
By (6)--(7),

    chi_n(alpha)=1 for n<=2k, and 2 for n>=2k+1,
    chi_infinity(alpha)=2,
    A_(n,r)(alpha)<=(4e r n)^r for every n,r>=1.           (8)

An explicit coloring is floor(j/k) modulo 2.
Its colors are reused across the k linearly independent residue coordinates.
The house of alpha is phi^(1/k), which tends to one, so the house-based color bound ceil(k log2/log phi) diverges.
In contrast (8) stays fixed.
The Mahler measure of every input is phi, consistent with (2).
These irreducible unit polynomials are nonreciprocal and have a degree-lowering kth power for k>1.
They do not solve the all-power-stable reciprocal core.

<a id="selected-factor-color-counterexample"></a>
## Selecting an irreducible factor can increase the color number

There is a reciprocal unit example already in the retained quartic Salem control.
Let lambda>1 be the real root of

    P(t)=t^4-t^3-t^2-t+1.

The irreducibility and root pattern are established in L G0003 and [L G0008](Yin_L_G0008_v1.md#salem-block-certificate).
Explicitly P(t)/t^2 gives z^2-z-3 for z=t+t^(-1).
Its two trace roots are (1+sqrt13)/2>2 and (1-sqrt13)/2 in (-2,2).
Modulo 2, P is the fifth cyclotomic polynomial, irreducible over F_2.
Thus the roots are lambda,lambda^(-1) and a pair on the unit circle.
The trace comparison gives phi<lambda<2, so lambda^2>2.

Parity again gives two dissociated classes for lambda.
Its own displayed polynomial is a nonzero {-1,0,1} relation, so

    chi_infinity(lambda)=2,
    chi_infinity(beta)=1 for beta=lambda^2.               (9)

The second assertion follows from beta>2 by highest-term domination.
Every positive power of lambda has degree four: in the common-size fibers of embeddings onto Q(lambda^n), the value lambda^n has only one preimage, because lambda is the unique conjugate of maximal modulus.
The field index is therefore one.
In particular Q(beta)=Q(lambda), and both lambda and beta are all-power degree stable.

Direct multiplication gives

    Q(t)=t^4-3t^3+t^2-3t+1,
    Q(t^2)=P(t)P(-t),                                    (10)

where Q is the minimal polynomial of beta.
The full cyclic induction defined by Q(t^2) has one dissociated color by (6), but selecting the P-factor yields (9)'s two colors.
Here [Q(lambda):Q(beta)]=1<2, exactly the missing hypothesis (7).
Reciprocity, integral units and all-power degree stability of each individual selected parameter do not repair that field-degree loss.
The example has Mahler measure lambda>phi; it is not in the remaining near-one window.

<a id="embedding-and-rank-color-boundaries"></a>
## What elementary embedding or rank relaxations can actually improve

For exponents e_0<...<e_s, a highest-term modulus certificate at an embedding of modulus rho has the form

    sum_(j<s) rho^(e_j-e_s)<1.                            (11)

Its left side is decreasing in rho>0.
Hence if any embedding passes this certificate, the embedding of largest modulus passes it.
Allowing the chosen expanding embedding to change with the prefix does not improve this absolute-value-only test.
A lowest-term certificate is the analogous test on alpha^(-1); on a reciprocal polynomial its best modulus is the same house.
No sum of expanding logarithms enters (11).
Phase cancellation or exact field-coordinate separation, as in (6), is information not present in that scalar relaxation.
The statement does not exclude other genuinely joint-embedding arguments.

Pure rational linear independence has a different limitation.
Any independent subset of a d-dimensional rational space has at most d elements.
A partition of n orbit vectors into such subsets therefore needs at least ceil(n/d) classes.
Inserting only this information into (4) loses a uniform asymptotic constant.
Integer dissociation is strictly weaker than rational linear independence: one dissociated class can be infinite even in rank one, for example the powers of 2 in Z.
Thus a finite-rank basis argument cannot substitute for the needed signed-relation control.

Finally, large support does not by itself give a linear-size class through the elementary maximal-set argument.
If D is an inclusion-maximal dissociated subset of a finite orbit set E, every element of E belongs to the {-1,0,1} span of D.
Otherwise adjoining it would preserve dissociation; in any new forbidden relation its coefficient must be +1 or -1.
For |E|=n this only gives

    n<=3^|D|,
    |T_n(alpha,{0,1})|<=(2n+1)^|D|.                      (12)

The second inequality uses that each binary sum has D-coordinates in [-n,n].
Consequently this route extracts at best the lower bound |D|>=log|T_n|/log(2n+1), rather than a positive density from a positive entropy value alone.
It is a limitation of these inequalities, not a counterexample to a stronger arithmetic extraction theorem.

The useful remaining question is therefore a uniform bound on signed-relation colors or large dissociated subsets for the actual all-power-stable core, using information beyond (11) and rank.
Full cyclic induction itself is already neutral for this cost, while selected-factor descent needs the exact guard.

## Current proof and retained checking scope

The complete current statement and every original mathematical argument are retained in [C279](../claims/Yin_C_G0279_v1.md#argument), with its actual selected assessment.
The [current entire finding](../audits/reviews/Yin_R_G0534_v1.md#current-dissociated-color-finding) is self-reviewed.
The [complete original checking account and exact findings](../audits/reviews/Yin_R_G0534_v1.md#historical-color-author-finding) retain their original2026-10-07 inputs, mathematical contributions, actual scopes and limitations.
Original independent or collaborator wording does not supply unrecorded initial context or transfer an old finding to this new C.
