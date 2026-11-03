---
author: Yin
---
# Simultaneous unit controls for the automatic dyadic-compositum gap

Human author Yin.
Root authored the combined radical-lifting and cyclotomic-product proof below on 2026-10-20T10:56.
The earlier C181 controls and C185 unit witness have different original inputs; this result proves all three comparison properties on the SAME new original unit.
It has its own whole independent-review obligation.
No field search, prime enumeration, numerical height calculation or parameter scan is performed.

## Statement

Fix a number field K, a finitely generated subgroup Gamma of the nonzero algebraic numbers, a positive real epsilon and an integer F>=1.
Put R=K(mu,Gamma^div), where mu contains all roots of unity and all division orders are allowed.
There exist an odd prime ell, a finite Galois2-power extension B/Q unramified at every odd finite prime, and an original nontorsion algebraic integer unit gamma in BQ(zeta_ell) such that

    gamma not in R,
    0<h_abs(gamma)<epsilon,
    every irreducible factor of P_gamma mod2 has degree>F.   (V1)

Here P_gamma is the actual monic irreducible polynomial over Q, and ALL reduction multiplicities are retained.
The entire class still satisfies

    m(gamma)>=log2/12,                                    (V2)

by the automatic central-Frobenius theorem.
Thus (V1) is not a construction with positive total measure tending to zero.
Every displayed finite field, unit and original polynomial in the proof is actual, not merely a prescribed group or a formal local pattern.
The fixed data K,Gamma,F,epsilon precede the witnesses.

More precisely choose the actual unit alpha supplied by C185, outside the fixed field R, in a finite dyadic Galois field B_0.
For any n>=0 set q=2^n and choose a q-th root beta of alpha; put d_n=[Q(beta):Q].
For every odd prime ell the actual product gamma=beta zeta_ell has

    [Q(gamma):Q]=d_n(ell-1),
    h_abs(gamma)=h_abs(alpha)/q,
    m(gamma)=(ell-1)m(beta),
    P_gamma mod2=(Phi_ell mod2)^d_n.                      (V3)

Each irreducible factor in(V3) has degree ord_ell(2).
No exact formula for d_n, binomial irreducibility or exact unit-radical minimal polynomial is assumed.

<a id="argument"></a>
## Complete proof

### Actual dyadic Galois field for every root

Fix alpha and B_0 from [C185](Yin_C_G0185_v1.md#statement).
The element alpha is nontorsion and an algebraic integer unit, and alpha is not in the same fixed R.
For q=2^n let C=B_0(mu_q).
The cyclotomic field Q(mu_q) is Galois of2-power degree and unramified at every odd finite prime: for q>=2 its cyclotomic degree divides q and its local splitting is unramified at odd primes by simple-root lifting of X^q-1; q=1 gives Q.
The exact unramified-compositum and lifting interfaces are those accepted in [C181](Yin_C_G0181_v1.md#unramified-lifting-source-interface), including Con26e's complete-valued-field specialization.
Thus C/Q is finite Galois of2-power degree and unramified at odd finite primes.

Let alpha_1,...,alpha_d be the distinct Q-conjugates of alpha, all in B_0 since B_0/Q is Galois.
Adjoin to C one q-th root of each alpha_j and call the resulting field B_n.
Each root may be adjoined by n successive quadratic radical steps, so [B_n:C] is a power of2.
Because mu_q is already present, B_n contains ALL roots of every X^q-alpha_j.
Every Q-embedding permutes B_0, mu_q and these full root sets, hence preserves B_n.
In characteristic zero the extension is separable, so B_n/Q is finite Galois of2-power degree.
This argument does not assume independence of the radicals or that their extension has the maximum possible degree.

At every odd prime of C each alpha_j is a unit and q is invertible in the residue field.
The polynomial X^q-alpha_j has nonzero roots and unit derivative qX^(q-1) in its splitting residue field.
All such residue roots for all j lie in one finite residue-field extension.
In the corresponding finite unramified complete local extension the simple-root Hensel theorem lifts them to the complete collection of roots of the original polynomials.
Their local splitting field is therefore a subextension of this unramified extension.
The accepted unramified subextension/compositum interface, together with the unramified C/Q completion, proves B_n is unramified at each odd rational prime.
Thus B_n is an actual member of C181's B class.
In particular2 is totally ramified in B_n with residue field F_2.

The chosen beta belongs to B_n.
It is integral because beta^q=alpha and alpha is integral, and its inverse is integral by the same argument applied to alpha^(-1).
It is therefore an original algebraic integer unit.
It is nontorsion, since any torsion beta would make alpha torsion.
It remains outside R, since beta in R would imply alpha=beta^q in R.

### Exact original product degree and reduction

Let ell be any odd prime and A=Q(zeta_ell).
It is abelian and unramified at2 by the same simple-root argument for X^ell-1.
The accepted C181 global disjointness and product theorem gives

    A intersect B_n=Q,
    Gal(AB_n/Q)=Gal(A/Q) times Gal(B_n/Q).

Write beta_1,...,beta_(d_n) for the distinct original Q-conjugates of beta, all in B_n.
Every pair beta_i zeta_ell^a with1<=a<=ell-1 occurs as a Q-image of gamma=beta zeta_ell, by this actual product group.
If beta_i zeta_ell^a=beta_j zeta_ell^b, then

    beta_i/beta_j=zeta_ell^(b-a) in A intersect B_n=Q.

The only rational ell-th root of unity for odd ell is1.
Thus a=b modulo ell and beta_i=beta_j, proving all d_n(ell-1) products distinct and the exact original degree in(V3).
No lower bound on the individual conjugate moduli or irreducibility of X^q-alpha is used in this distinctness argument.

At the unique prime of B_n over2, every beta_i is a unit and therefore reduces to1 in F_2.
The ell-th roots of unity reduce to distinct roots: their reduction polynomial X^ell-1 is separable, and the local simple-root correspondence preserves the full root set.
The nonidentity roots remain primitive because ell is prime; equivalently Phi_ell(1)=ell is odd.
Reducing the full original product over these distinct conjugates gives exactly

    P_gamma mod2=(Phi_ell mod2)^d_n.

The full exponent d_n is retained; taking a squarefree part would change the original reduction mass.
The irreducible degree of each primitive ell-th root over F_2 is its Frobenius orbit length ord_ell(2).
This proves every reduction claim in(V3).

### Heights, same-target exclusion and choice of witnesses

Every original conjugate of alpha occurs equally often among the q-th powers of the original beta conjugates, since embeddings over each conjugate extend equally in the finite separable extension Q(beta)/Q(alpha).
For units the absolute logarithmic height is the original-degree average of log^+ of the archimedean conjugates.
The identity log^+|beta_i^q|=q log^+|beta_i|, with those complete equal fibers, therefore gives h_abs(beta)=h_abs(alpha)/q.
Multiplication by each zeta_ell^a leaves the modulus unchanged, and the complete product degree just proved yields

    m(gamma)=(ell-1)m(beta),
    h_abs(gamma)=h_abs(beta)=h_abs(alpha)/q.

Because mu is contained in the fixed R, the implication gamma in R would give beta=gamma/zeta_ell in R and then alpha in R, a contradiction.
Thus the SAME gamma is outside R and has the exact height in(V3).
It is nontorsion because gamma^ell=beta^ell and beta is nontorsion.

For every fixed F, the odd primes with ord_ell(2)<=F divide the nonzero integer product_(j=1)^F(2^j-1), and so form a finite set.
Infinitely many odd primes exist, so choose one ell with ord_ell(2)>F.
Next choose n sufficiently large that h_abs(alpha)/2^n<epsilon.
The positive height follows from nontorsion and nonzeroness of the original integral unit alpha and the accepted [Kronecker height-zero characterization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), at printed322/PDF1 with its explicit zero exception.
The resulting B_n,ell,gamma satisfy ALL of(V1) simultaneously, with each fixed datum unchanged.
Finally gamma is a nontorsion integer unit in B_n A, so C181 supplies(V2) with its original degree, uniformly over n,ell and the initial witness alpha.
There is no conflict: d_n and the total product degree can grow while absolute height decreases.

<a id="comparison-boundaries"></a>
## Exact simultaneous comparison and retained limits

This proof strengthens the earlier separate controls to one actual original-unit input.
For every fixed radical-field domain and every fixed original residue-degree threshold at2 there are inputs outside that domain whose bounded-degree reduction mass at2 is zero and whose absolute height is arbitrarily small.
Consequently the whole C181 class has neither automatic containment in one such fixed radical domain, nor automatic positive bounded-degree original reduction mass at2, nor a uniform positive absolute-height floor.
Each assertion concerns its stated fixed parameters.
It does not refute the older theorems, the auxiliary-ratio criterion, original residue tests at other primes, or every possible infinite-base hypothesis in CDPT26.
The accepted total-measure conclusion is obtained from that old auxiliary-ratio criterion after the actual automatic central lift is supplied.
No field-wide novelty or optimal constant is asserted.

The original unit theorem C185 is reused with its actual [R457](../audits/reviews/Yin_R_G0457_v1.md#dyadic-unit-noncontainment-whole-finding); that review does not cover this new root/product construction.
The C181 local field theorem and its [R454](../audits/reviews/Yin_R_G0454_v1.md#dyadic-composita-whole-independent-finding) and [source readback](../audits/reviews/Yin_R_G0454_v1.md#dyadic-source-declaration-readback) are accepted upstream interfaces, not newly independently re-reviewed here by their contributor.
All finite-local and height applications in this proof are stated explicitly.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:56 |
| status | open |
| reason | Register the complete same-unit radical-field exclusion, arbitrarily small absolute height and unbounded original residue degree, with the automatic positive total bound retained. Independent whole review of the new radical and original-product construction remains required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Simultaneous original-unit controls](#statement) | Every fixed K,Gamma,F,epsilon, actual finite fields and original unit, all three properties on one input, exact V3 and the inherited total bound V2. |
| argument | [Complete construction and proof](#argument) | All-conjugate radical Galois closure, exact2-power and odd-unramified properties, true unit integrality, same-target exclusion, original pair distinctness, full reductions and original-degree height fibers. |
| dependency | [Accepted actual unit witness](Yin_C_G0185_v1.md#statement) | Nonzero nontorsion integral alpha in an actual dyadic Galois B_0 outside the same pre-fixed all-order radical field. |
| dependency | [Automatic dyadic field and measure theorem](Yin_C_G0181_v1.md#statement) | Actual total ramification, disjointness/product with A unramified at2, central lift and original total bound. |
| dependency | [Exact simple-root and unramified interfaces](Yin_C_G0181_v1.md#unramified-lifting-source-interface) | Complete local fields, all distinct unit roots and derivative, finite unramified splitting extensions, subextensions and composita at odd primes. |
| dependency | [Exact height-zero characterization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted Kronecker statement for a nonzero algebraic integer unit: height zero implies a root of unity; the zero exception is excluded. |
| support | [Actual upstream witness review](../audits/reviews/Yin_R_G0457_v1.md#dyadic-unit-noncontainment-whole-finding) | Earlier C185 scope only, not this new proof. |
| support | [Exact simultaneous comparison limits](#comparison-boundaries) | Distinct old theorem premises tested on the same unit, no all-literature or other-prime exclusion and no zero total-gap conclusion. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T11:03 |
| status | proved |
| authority | Internal adoption within Yin's selected automatic-supply inquiry. |
| reason | Adopt the complete simultaneous original-unit controls through noncontributor whole R458, including the exact height-zero source clarification. For every fixed K,Gamma,F,epsilon, one actual unit has all three comparison properties while retaining the uniform total bound. This closes the scoped comparison without claiming a near-one family, exclusion of every older theorem or unrestricted G0001 completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Simultaneous original-unit controls](#statement) | Every fixed K,Gamma,F,epsilon, actual finite fields and original unit, all three properties on one input, exact V3 and the inherited total bound V2. |
| argument | [Complete construction and proof](#argument) | All-conjugate radical Galois closure, exact2-power and odd-unramified properties, true unit integrality, same-target exclusion, original pair distinctness, full reductions and original-degree height fibers. |
| dependency | [Accepted actual unit witness](Yin_C_G0185_v1.md#statement) | Nonzero nontorsion integral alpha in an actual dyadic Galois B_0 outside the same pre-fixed all-order radical field. |
| dependency | [Automatic dyadic field and measure theorem](Yin_C_G0181_v1.md#statement) | Actual total ramification, disjointness/product with A unramified at2, central lift and original total bound. |
| dependency | [Exact simple-root and unramified interfaces](Yin_C_G0181_v1.md#unramified-lifting-source-interface) | Complete local fields, all distinct unit roots and derivative, finite unramified splitting extensions, subextensions and composita at odd primes. |
| dependency | [Exact height-zero characterization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted Kronecker statement for a nonzero algebraic integer unit: height zero implies a root of unity; the zero exception is excluded. |
| support | [Actual upstream witness review](../audits/reviews/Yin_R_G0457_v1.md#dyadic-unit-noncontainment-whole-finding) | Earlier C185 scope only, not this new proof. |
| support | [Exact simultaneous comparison limits](#comparison-boundaries) | Distinct old theorem premises tested on the same unit, no all-literature or other-prime exclusion and no zero total-gap conclusion. |
| review | [Whole simultaneous-unit finding](../audits/reviews/Yin_R_G0458_v1.md#simultaneous-dyadic-unit-whole-finding) | Entire final V1--V3 and construction, q=1, all conjugate radical fields, odd-prime lifting, exact original degrees and reductions, same-target exclusion, height fibers and all declared inputs. |

