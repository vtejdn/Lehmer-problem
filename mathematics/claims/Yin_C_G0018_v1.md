---
author: Yin
---

# Exact integer-energy capacity and the scalar Fuglede--Kadison determinant

Date: 2026-10-11T18:49.
Human author: Yin.
Provenance: project deduction from the fixed integer-capacity duality and accepted classical lattice/Fourier interfaces.
Internal organization under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Root supplied the determinant/lattice and full-root scaling candidates; the responsible author derived the complete conditional argument.
Its original conditional history is retained in full below.
No main-theorem designation or objective change is made.

## Statement

Fix ONE actual monic irreducible minimal polynomial P in Z[t] of a nontorsion algebraic integer unit alpha, original degree d>=2.
Initially O_0=Z[alpha].
Let E_T be the exact energy INFIMUM over finite rational-coefficient packets in the allowed window[0,T], with positive normalized rational weights, every value a NONZERO ACTUAL O_0 integer, and ALL aggregate positive-lag correlations zero.
Equivalently their Laurent square sum is the constant energy E.
For T>=d-1 put N=T+1 and D_T=det(A_T A_T^T)>0, using the actual integer power-basis remainder matrix.
All logarithms are natural, m(P) is the TOTAL original logarithmic Mahler measure, and P,d are held fixed before T tends to infinity.

**A. Finite bounds and exact rate.** With C_d=4/kappa_d^(2/d), where kappa_d is the Euclidean unit-ball volume,

    exp(-2T m(P)/d)<=E_T<=min{1,C_d(T+1)/D_T^(1/d)}

for every T>=d-1.
Consequently

    m(P)=lim_(T->infinity) [-d/(2T)]log E_T,
    lim E_T^(1/T)=exp(-2m(P)/d),
    M(P)=lim E_T^(-d/(2T)).

Under the canonical scalar trace tau(I)=1 on N(Z), the last limit equals the Fuglede--Kadison determinant of the convolution operator r(P), equivalently P(U) for ONE Haar unitary with its canonical trace.
Circle zeros are allowed.
There is no matrix-trace division by d; d appears only in the capacity exponent.
The result concerns rational COEFFICIENTS and actual integer VALUES; integral-coefficient capacity is a different problem.

**B. Complete fixed-input determinant refinement.** Partition ALL distinct original roots into inside I, circle C and outside O, put c=|C|, Delta=|disc P|, and use ordinary determinants of the positive kernel matrices

    K_I=(1/(1-alpha_i conjugate(alpha_j)))_(i,j in I),
    K_O=(1/(1-(alpha_i conjugate(alpha_j))^-1))_(i,j in O).

With empty-block determinant1, C_P=det K_I det K_O/Delta>0 and

    D_T~C_P(T+1)^c exp(2T m(P)).

Thus E_T has the resulting lower/upper sandwich with polynomial upper factor (T+1)^(1-c/d) and input-dependent C_P; this is NOT a leading asymptotic equality for E_T.
The complete complex scaling/cross-block proof is retained and selected below.
The previously known fixed-input Gram/Szego rate is credited at its original source scope.

**C. Actual orders and complete arithmetic costs.** For every specified full overorder O containing alpha and alpha^-1, define E_T(O) by the same ACTUAL nonzero O-valued class.
It has the same fixed-input rate and scalar determinant limit.
Its own basis matrix satisfies D_T(O)=[O:O_0]^2 D_T(O_0), so the index is charged as a squared determinant factor, not an omitted norm or degree factor.
Every rational packet retains its actual coefficient denominator q, final weight denominator M_w, contents, signed full resultants q^d Norm_K(f_b(alpha)), complete copied multiplicities and possible signed monomial norm factors, as in the proof.
Formal-real capacity inherits the rate by its proved equality of infima; no field norm is applied to arbitrary irrational coefficients.

For each T a finite rational packet may be chosen with energy at most twice the positive upper bound in A.
Its weighted normalized log-norm income Lambda then satisfies Lambda<=[(d-c)/(2d)]log(T+1)+O_(P,d)(1).
This is a weighted bound, not an individual norm/ideal bound or unit-only selection.
No uniform q/M_w, height, packet-size, convergence window or energy deficit independent of input/degree is asserted.
A uniform finite-window deficit remains a separate sufficient Lehmer gate.

## Current assessment
[Selected decision](#decision-current-complete-isolated-adoption)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-11T18:49 |
| status | open |
| reason | Assemble the complete formerly conditional author argument with the now actually adopted fixed C17 duality. The new unconditional statement and exact fixed dependency interface await separate current whole/extraction review; no original conditional history or old C16 weak scope is rewritten. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A--C for fixed original polynomial/degree and exact nonzero integer-value capacity, all original roots and canonical scalar normalization; no uniform-gap assertion. |
| argument | [Argument](#argument) | Actual C17 assembly below plus complete preserved author Sections1--7/equations1--21, selecting the local full-root determinant proof as sufficient for the rate. |
| dependency | [Adopted complete integer-capacity duality](Yin_C_G0017_v1.md#statement) | Exactly Gamma_T^Q=E_T^Q=E_T^R for this full actual-residue class, every T>=d-1 and each specified order. This resolves the original author's sole pending SD input; the separate first-window theorem is not needed. |
| dependency | [Exact capacity and quotient domain](Yin_C_G0016_v1.md#statement) | Finite nonzero integer moment hull, all lag constraints, positive fixed-window infimum, weighted quotient form and rational/formal-real conventions. |
| dependency | [Direct generic-monic full-root inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Actual common allowed window, positive final weights and nonzero full original resultants; supplies the charged integer norm lower energy bound without reciprocity. |
| dependency | [Classical arithmetic-minimum upper bound](../audits/literature/Sch09/Yin_U002.md#sch09-u002) | Exact real positive-definite form on the entire integer lattice, with DIMENSION-DEPENDENT C_d and the retained source proof-inspection limits. |
| dependency | [Scalar Fourier/FK and Jensen conventions](../audits/literature/Den09/Yin_U001.md#den09-u001) | Precisely its group-fourier-convention and scalar Mahler/Jensen interface: canonical trace1, right-translation/Fourier convention and finite polynomial circle zeros; no finite-quotient determinant approximation. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-11T18:55 |
| status | proved |
| reason | Adopt the completed separate noncontributor finding for this exact registered scope and selected fixed argument. Complete original histories, current repairs, source inspection limits and all costs remain; no uniform efficiency, unrestricted gap or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A--C for fixed original polynomial/degree and exact nonzero integer-value capacity, all original roots and canonical scalar normalization; no uniform-gap assertion. |
| argument | [Argument](#argument) | Actual C17 assembly below plus complete preserved author Sections1--7/equations1--21, selecting the local full-root determinant proof as sufficient for the rate. |
| dependency | [Dependency](Yin_C_G0017_v1.md#statement) | Exactly Gamma_T^Q=E_T^Q=E_T^R for this full actual-residue class, every T>=d-1 and each specified order. This resolves the original author's sole pending SD input; the separate first-window theorem is not needed. |
| dependency | [Dependency](Yin_C_G0016_v1.md#statement) | Finite nonzero integer moment hull, all lag constraints, positive fixed-window infimum, weighted quotient form and rational/formal-real conventions. |
| dependency | [Dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Actual common allowed window, positive final weights and nonzero full original resultants; supplies the charged integer norm lower energy bound without reciprocity. |
| dependency | [Dependency](../audits/literature/Sch09/Yin_U002.md#sch09-u002) | Exact real positive-definite form on the entire integer lattice, with DIMENSION-DEPENDENT C_d and the retained source proof-inspection limits. |
| dependency | [Dependency](../audits/literature/Den09/Yin_U001.md#den09-u001) | Precisely its group-fourier-convention and scalar Mahler/Jensen interface: canonical trace1, right-translation/Fourier convention and finite polynomial circle zeros; no finite-quotient determinant approximation. |
| review | [Current finding](../audits/reviews/Yin_R_G0746_v1.md#c18-integer-capacity-asymptotic-extraction-finding) | Exact registered statement, selected complete argument, changed interfaces and dependencies in this physical version; preserved original reviews are not silently expanded. |


### Decision current-complete-isolated-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:16 |
| status | proved |
| reason | Adopt the exact complete current statement and selected full argument with R746's separately assigned isolated whole finding at this specific target. All actual-order/domain, finite/rational/formal-real, window, equality, original norm/denominator and unresolved-uniformity boundaries remain. The original UNKNOWN findings retain their actual dates, fixed inputs, source/checker/preservation facts and relationships; the new finding does not backfill their contexts or adopt any stronger conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | A--C for fixed original polynomial/degree and exact nonzero integer-value capacity, all original roots and canonical scalar normalization; no uniform-gap assertion. |
| argument | [Exact retained argument](#argument) | Actual C17 assembly below plus complete preserved author Sections1--7/equations1--21, selecting the local full-root determinant proof as sufficient for the rate. |
| dependency | [Exact retained dependency](Yin_C_G0017_v1.md#statement) | Exactly Gamma_T^Q=E_T^Q=E_T^R for this full actual-residue class, every T>=d-1 and each specified order. This resolves the original author's sole pending SD input; the separate first-window theorem is not needed. |
| dependency | [Exact retained dependency](Yin_C_G0016_v1.md#statement) | Finite nonzero integer moment hull, all lag constraints, positive fixed-window infimum, weighted quotient form and rational/formal-real conventions. |
| dependency | [Exact retained dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Actual common allowed window, positive final weights and nonzero full original resultants; supplies the charged integer norm lower energy bound without reciprocity. |
| dependency | [Exact retained dependency](../audits/literature/Sch09/Yin_U002.md#sch09-u002) | Exact real positive-definite form on the entire integer lattice, with DIMENSION-DEPENDENT C_d and the retained source proof-inspection limits. |
| dependency | [Exact retained dependency](../audits/literature/Den09/Yin_U001.md#den09-u001) | Precisely its group-fourier-convention and scalar Mahler/Jensen interface: canonical trace1, right-translation/Fourier convention and finite polynomial circle zeros; no finite-quotient determinant approximation. |
| review | [Complete current isolated finding](../audits/reviews/Yin_R_G0746_v1.md#current-c18-complete-isolated-independent-finding) | Entire exact current Statement, complete selected Argument and all necessary interfaces, with actual complete initial judgment2026-10-22T19:11 preceding complete old-finding comparison2026-10-22T19:12; no proof repair, expanded source-proof scope or new native run. |

## Argument

### Resolution of the exact pending SD input

The original author account below correctly left its upper-capacity implication conditional on the developing D12 statement.
That historical judgment is preserved.
The current assembly instead selects [C17 v1's actual organized-reviewed decision](Yin_C_G0017_v1.md#decision-organized-reviewed), supported by the separate [R746 exact extraction finding](../audits/reviews/Yin_R_G0746_v1.md#c17-toeplitz-completeness-extraction-finding).
C17 proves the same Gamma_T=E_T equality for all actual orders and T>=d-1, using precisely the rational positive-definite Toeplitz class, finite nonzero integer residues and exact lags required in author equation(SD).
All application hypotheses are the common initial domain above.
Thus every occurrence of SD in the preserved proof is now resolved by this selected fixed C input, without enlarging C16 or retroactively changing the original author's conditional inspection.

The full upper/lower chain, all norm and scalar factors, and the squeeze then give A.
For the determinant rate, the entire local root-block proof of author equations(13)--(16) is physically retained and selected: all three blocks and every cross-block limit are checked without an additional unowned L argument.
The old Gram/relation/Szego derivation and Den09-U002 remain separately credited classical context, not necessary missing proof behind an L redirect.
The current actual C17 input also covers overorders, and the retained inclusion/index argument gives C.
The exact fixed original statement is a new assembly to be checked by the separate reviewer; this registration is not acceptance.

### Complete original conditional author account

## Fixed-input asymptotic of exact integer complementary-energy capacity

Date: 2026-10-12.
Human author: Yin.
Root supplied the substantive determinant/lattice-minimum candidate and the proposed full-evaluation scaling argument.
The internal author is responsible for this draft's derivation and self-check; separate whole review is pending.

## Current question and starting scope

For the actual fixed monic irreducible nontorsion algebraic integer unit P and the exact integer-valued complementary-energy infimum E_T in C_G0016_v1, determine whether the fixed-input limit -d log(E_T)/(2T) equals m(P).
Retain actual nonzero order membership, finite rational positive weights, all lag equations and the full allowed coefficient window.
This is a fixed-input asymptotic question, with no input-uniform positive gap or rate claimed.

Starting established inputs were the exact C16 moment/weak-duality setup and the generic-monic norm lower bound in C_G0010_v2.
The parallel D12 investigation of strong duality Gamma_T=E_T remains a CANDIDATE until separately fixed and adopted.
At allocation the root-owned source check of the dimension-dependent Hermite/Minkowski upper bound was pending; Section1 now records the supplied canonical Sch09-U002 acceptance.
Existing L4/L241 fixed-input Gram/Szego identities are reused at their actual scope, not presented as new mathematics.
No native mathematical program, numerical scan or new J is authorized by this assignment.

<a id="integer-capacity-asymptotic-reuse"></a>
## 1. Reuse, actual inputs and review limits

The author read the complete current [C16 statement and argument](Yin_C_G0016_v1.md#statement), including exact rational/formal-real energy infima, the FINITE nonzero integer moment hull and the weighted quotient certificate.
The selected [C10 v2 direct exact-covariance inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) explicitly supplies its generic monic argument and does not impose its other reciprocal lifting hypotheses on that inequality.
These are established inputs at their selected scope.

[L4 Sections2--4](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate) already identify the actual power-orbit Gram determinant with the saturated polynomial-relation Gram determinant, and already retain its FIXED-INPUT Szego exponential rate.
[L241 Sections1,4--5](../ledger/Yin_L_G0241_v1.md#sharp-joint-auxiliary-determinant) already show that a full joint auxiliary determinant optimizes to that same old quantity, including its discriminant and window costs.
Those results, their limits and their checked source interfaces were read and are reused.
Their classical determinant asymptotic is not the new question.
A bounded G-series Claim/ledger search additionally screened Gram-asymptotic, circle-root, Hermite and Minkowski formulations; it supplies no priority assertion.

[Den09-U002, finite-section determinant](../audits/literature/Den09/Yin_U002.md#finite-section-determinant) accepts the classical Toeplitz limit for a bounded nonnegative symbol positive on a set of positive Haar measure, including unit-circle polynomial zeros; the cited original Szego proof is uninspected at that retained scope.
[Den09-U001](../audits/literature/Den09/Yin_U001.md#group-fourier-convention) supplies the scalar group-trace/Fuglede--Kadison normalization and the Jensen root formula.
No general noninvertible finite-quotient determinant-approximation theorem is used.

The new [Sch09-U002](../audits/literature/Sch09/Yin_U002.md#sch09-u002), read in its canonical form after this draft was allocated, accepts precisely

    min_(0!=r in Z^d) r^T Q r <= C_d (det Q)^(1/d),
    C_d=4/kappa_d^(2/d),                               (1)

for every real symmetric positive-definite Q, with kappa_d the volume of the Euclidean unit ball.
Root checked the selected source equation(8), its density/volume conversion and exact domain.
The foundational Minkowski proof and sharp Hermite tables are not newly audited.
C_d DEPENDS ON d.
U001 remains at its earlier definition-only scope.

The parallel [D12 dual-completeness candidate](Yin_C_G0017_v1.md#toeplitz-completeness-statement) has been read only as the proposed interface

    Gamma_T = E_T,  T>=d-1.                            (SD)

As of this authored revision, (SD) has no adopted fixed support supplied to this draft.
Every assertion below that needs it is explicitly CONDITIONAL ON (SD), separately from the completed local algebra.
No fixed C argument may later select this mutable D12 link as a resolved dependency; adoption must name the exact fixed successor and its actual checked scope.
This author did not contribute to D12 and does not claim to have performed its whole proof review.
Its first-window theorem is not needed here.

Root supplied the substantive determinant/lattice-minimum connection and the full-root scaling candidate.
The author supplied the complete matrix-order proof, all root-block/cross-block limits, positive leading constant, the exact capacity normalization and arithmetic-cost consequences below.
These are disclosed mathematical contributions.
The author self-check is not independent review; root owns subsequent fixed organization, separate whole review and adoption.
No source intake or native mathematical computation is performed by this author.

<a id="integer-capacity-asymptotic-domain"></a>
## 2. Exact capacity and the proposed conclusion

Fix throughout ONE actual monic irreducible minimal polynomial P in Z[t] of a nontorsion algebraic integer unit alpha, of degree d>=2.
Let K=Q(alpha), O_0=Z[alpha], and let alpha_1,...,alpha_d be ALL its distinct complex roots.
Write

    m=m(P)=sum_(i=1)^d log max(1,|alpha_i|),
    Delta=|disc P|>0.

All logarithms are natural.
No reciprocity, total-reality or unique exterior pair is imposed.
The polynomial, degree and order stay fixed as T tends to infinity.

For integer T>=0, put N=T+1 and let A=A_T be the d-by-N INTEGER power-basis remainder matrix: its column j is the coordinate of alpha^j in 1,alpha,...,alpha^(d-1).
In particular its first d columns are I_d when N>=d.
A rational admissible packet consists of finitely many f_b in Q^N, positive rational weights omega_b summing to1, and

    A f_b in Z^d minus{0} for EVERY b,
    sum_b omega_b sum_(j=0)^(T-h) f_(b,j) f_(b,j+h)=0
                     for EVERY 1<=h<=T.               (2)

Thus f_b(alpha) is an ACTUAL nonzero O_0 integer, not a merely formal nonzero vector at one embedding.
Its coefficient energy E=sum_b omega_b||f_b||_2^2 is the exact constant in sum_b omega_b f_b(t)f_b(t^-1)=E.
Define E_T=E_T^Q as the INFIMUM of these energies in the allowed common window [0,T].
C16 proves E_T^Q=E_T^R when the real version retains the formal entire residue constraint, and proves 0<E_T<=1.
No minimum, rational optimizer or bound on packet size is asserted.
Extending every vector by a zero coordinate gives E_(T+1)<=E_T; this does not assert an attained minimizing packet.

For T>=d-1 put

    D_T=det(A_T A_T^T)>0,
    G_W=(A_T W^-1 A_T^T)^-1,
    mu(W)=min_(0!=r in Z^d) r^T G_W r,
    Gamma_T=sup_W mu(W),                              (3)

where W ranges over precisely the RATIONAL symmetric positive-definite Toeplitz N-by-N matrices with diagonal1 from C16.
Its weak inequality Gamma_T<=E_T is established.
The equality (SD) remains the explicit candidate dependency above.

**Theorem, conditional capacity connection.** Assuming (SD) at every T>=d-1 for this exact input and entire admissible class, one has the finite bounds

    exp(-2Tm/d) <= E_T
       <= min{1, C_d N / D_T^(1/d)}.                 (4)

Consequently

    lim_(T->infinity) [-d/(2T)] log E_T = m(P),
    lim_(T->infinity) E_T^(1/T) = exp(-2m(P)/d).      (5)

The lower bound in(4), the upper bound for Gamma_T in place of E_T, and the determinant statements in Section4 are UNCONDITIONAL deductions from the stated established inputs.
Passing the upper bound from Gamma_T to E_T, and hence(5), is conditional on (SD).

In the canonical group von Neumann algebra N(Z), write r(P) for the bounded convolution operator of P, with the canonical trace tau(I)=1 and the Den09 right-translation convention.
Then the equivalent form of(5) is

    Delta_(N(Z))(r(P))=M(P)
       =lim_(T->infinity) E_T^(-d/(2T)).              (6)

The d in this exponent is the ORIGINAL field degree; it is not a normalized matrix trace or a powered/trace-subfield degree.
Unit-circle roots are allowed.
This is a fixed-input asymptotic formula for the exact INTEGER-VALUE capacity.
The coefficients and weights of the admissible packets are rational; imposing integral COEFFICIENTS instead would give energy at least1 and a different problem.

<a id="integer-capacity-finite-determinant-bound"></a>
## 3. Complete finite upper bound and norm lower bound

Let W be any matrix in(3).
Since W>0 and trace W=N, each eigenvalue is positive and no larger than N.
Therefore W<=N I_N.
Diagonalizing the real symmetric W gives W^-1>=(1/N)I_N.
Congruence by the full-row-rank A gives

    A W^-1 A^T >= (1/N) A A^T >0.

Inversion reverses this order: if H>=K>0, then K^-1/2 H K^-1/2>=I, whose inverse is <=I, and congruence gives H^-1<=K^-1.
Hence

    0<G_W<=N(A A^T)^-1.                              (7)

For positive-definite H<=K, all eigenvalues of K^-1/2 H K^-1/2 are in(0,1], so det H<=det K.
Applied to(7),

    det G_W <= N^d / D_T.

The EXACT hypothesis of Sch09-U002 holds for this real positive-definite d-by-d form on the FULL lattice Z^d.
Substitution into(1) yields

    mu(W)<=C_d(det G_W)^(1/d)
          <=C_d N / D_T^(1/d).

The last expression does not depend on W, so

    Gamma_T <= C_d N / D_T^(1/d).                    (8)

No rational maximizing W, compactness of the open Toeplitz cone or swap of infimum and supremum is used.
C16 weak duality alone DOES NOT turn(8) into an upper bound for E_T; precisely (SD) makes that step.
Together with the constant packet f=1 this gives the upper half of(4), conditionally.

For its lower half take ANY rational packet(2), choose its actual common positive coefficient denominator q, and put F_b=q f_b in Z[t].
The normalized residues a_b=f_b(alpha) are nonzero O_0 integers.
Monicity and ALL original conjugates give

    Res(P,F_b)=q^d Norm_(K/Q)(a_b)!=0,
    |Norm_(K/Q)(a_b)|>=1.                            (9)

Its constant integer-numerator covariance is S=q^2 E.
The direct generic-monic C10 inequality, applied to these actual polynomials in the common allowed window, is

    log q+(1/d)sum_b omega_b log|Norm(a_b)|
          <=(1/2)log(q^2 E)+(T/d)m.

Cancel the SAME log q on both sides only after retaining the full resultants in(9).
With

    Lambda=(1/d)sum_b omega_b log|Norm(a_b)|>=0,

one obtains

    E >= exp(2Lambda-2Tm/d) >= exp(-2Tm/d).          (10)

Taking the infimum gives the lower half of(4) without any strong-duality assumption.
If an individual packet has smaller actual support width, C10 gives the correspondingly stronger bound; using the allowed T in(10) is still valid.
C16's equality of rational and formal-real infima transfers this capacity bound to E_T^R; the original-field norm in(9) is NOT silently applied to arbitrary irrational coefficient vectors.

<a id="integer-capacity-gram-rate-and-conditioning"></a>
## 4. The existing Gram rate and an explicit fixed-input conditioning constant

The needed exponential rate is already the L4/Den09 input.
Its exact finite interface is repeated concisely to fix N,T and the relation size.
Let k=N-d>=0.
The integer kernel of A_T is precisely the coefficient vectors of P,tP,...,t^(k-1)P: monic division gives an integral quotient with exactly this degree range.
Let K_k be their N-by-k column matrix.
For k=0 use the empty Gram determinant1.
The bottom k-by-k block of K_k is triangular with diagonal1.
If A=[I_d B], the standard kernel basis is [-B;I_k]; the actual shift basis differs by a triangular integer matrix of determinant1.
Thus

    D_T=det(I_d+B B^T)
       =det(I_k+B^T B)=det(K_k^T K_k).               (11)

The middle equality follows, for example, by computing the two Schur complements of the block matrix [I_d B;-B^T I_k].
The relation Gram in(11) is exactly the k-by-k Toeplitz matrix of the circle symbol |P(e^(i theta))|^2.
This symbol is bounded, nonnegative and positive outside finitely many points; its logarithmic integral is 2m.
Therefore the retained Den09 Theorem2 interface gives

    lim_(k->infinity) det(K_k^T K_k)^(1/k)=exp(2m).

Since k/T=(T+1-d)/T tends to1 at this FIXED degree,

    lim_(T->infinity) (1/T) log D_T=2m.              (12)

This is the old fixed-input Gram/Szego rate, not a new asymptotic contribution.
Its hypotheses include circle zeros through Theorem2; Theorem4's bounded-invertible case alone would be insufficient there.

For the actual input dependence in the new capacity upper bound one can additionally retain the following fully local refinement of(12).
It supplies a definite leading constant by finite geometric sums, without importing an uninspected strong-asymptotic or Fisher--Hartwig theorem.
The classical first-order rate has the source attribution just given; no historical novelty for the following determinant calculation is asserted.

Partition ALL roots into I={i:|alpha_i|<1}, C={i:|alpha_i|=1}, and O={i:|alpha_i|>1}, and put c=|C|.
Define the positive-definite kernel matrices

    K_I=(1/(1-alpha_i conjugate(alpha_j)))_(i,j in I),
    K_O=(1/(1-(alpha_i conjugate(alpha_j))^-1))_(i,j in O),
    C_P=det K_I det K_O / Delta>0,                  (13)

with the determinant of an empty block equal to1.
Then

    D_T = C_P N^c exp(2Tm) (1+o_P(1)).              (14)

**Proof of the refinement.** Let V=(alpha_i^j)_(1<=i<=d,0<=j<d) be the square original-root Vandermonde matrix, and H_T=V A A^T V*.
Remainder evaluation gives the EXACT entries

    (H_T)_(i,j)=sum_(ell=0)^T
                      alpha_i^ell conjugate(alpha_j)^ell,
    det H_T=|det V|^2 D_T=Delta D_T.                (15)

Use the diagonal COMPLEX row scaling R_T with entries1 on I, N^-1/2 on C and alpha_i^-T on O, and consider R_T H_T R_T*.
The I-by-I block converges to K_I by geometric sums.
The O-by-O block has exact entries

    sum_(ell=0)^T (alpha_i conjugate(alpha_j))^-ell,

after the reindexing ell=T-old_index, so converges to K_O.
On C the diagonal entries are1.
Distinct circle roots give alpha_i conjugate(alpha_j)!=1 when i!=j; their off-diagonal geometric sums are bounded independently of T and divided by N, hence tend to0.
The circle block therefore tends to I_c, with no unremoved phase factor.

All cross blocks vanish.
For I against C, the finite geometric sum is bounded because the product of the moduli is less than1, and the scaling divides it by sqrt N.
For O against C write a=|alpha_i|>1; the absolute value is at most

    N^-1/2 a^-T sum_(ell=0)^T a^ell
                 <=[a/(a-1)] N^-1/2 ->0.

For O against I write a>1 and b=|alpha_j|<1.
Each absolute summand after scaling is a^-T(ab)^ell.
Its maximum over 0<=ell<=T is max(a^-T,b^T), regardless of phases, so the entire entry is bounded by

    N max(a^-T,b^T) ->0.

The transposed cross blocks are their Hermitian adjoints.
These estimates cover also alpha_i conjugate(alpha_j)=1 across the exterior/interior partition, where a direct division by 1-alpha_i conjugate(alpha_j) would have been invalid.

Both limiting kernel blocks are strictly positive definite.
For K_I the quadratic form is

    sum_(ell=0)^infinity
        |sum_(i in I) conjugate(z_i) alpha_i^ell|^2.

If it vanishes, its first |I| terms vanish, and the Vandermonde matrix of the distinct alpha_i is invertible, forcing z=0.
For K_O the same argument uses the distinct numbers alpha_i^-1 inside the disk.
Hence

    R_T H_T R_T* -> diag(K_I,I_c,K_O)>0,
    det(R_T H_T R_T*) -> det K_I det K_O>0.          (16)

Finally |det R_T|^2=N^-c exp(-2Tm).
Taking determinants in(15)--(16) gives exactly(14).
Every original conjugate and the entire Delta denominator remain.
The constants and convergence rates depend on the fixed root locations, radial distances and phase separations.
This proves the refinement locally; it gives no input-uniform remainder estimate.

<a id="integer-capacity-limit-and-fk"></a>
## 5. Capacity squeeze and scalar Fuglede--Kadison normalization

For T>=d-1 with T>0, assuming (SD), equations(4) imply

    max{0,[log D_T-d log(C_d N)]/(2T)}
        <=[-d/(2T)] log E_T <=m.                    (17)

Using the already retained rate(12), the left side tends to m.
This proves both limits in(5).
The optional refinement(14) makes the fixed-input error explicit:

    exp(-2Tm/d) <= E_T
       <= C_d C_P^(-1/d) N^(1-c/d)
                         exp(-2Tm/d)(1+o_P(1)),     (18)

and, equivalently, the normalized logarithm differs from m by at most O_(P,d)(log(T+1)/T).
Formula(18) is a SANDWICH, not an asymptotic equivalence for E_T or an identified polynomial prefactor of E_T.
No packet or dual form is claimed to attain either side.

Under Fourier transform on ell^2(Z), r(P) acts as multiplication by P on the circle, up to the inversion convention recorded in Den09-U001.
Haar inversion preserves the logarithmic integral.
The canonical trace has mass1, and that unit's accepted formula gives

    log Delta_(N(Z))(r(P))
       =integral_(circle) log|P(z)| dmu(z)=m(P).

The finitely many circle zeros have Haar measure zero and integrable logarithmic singularities.
They do not require omitting a spectral kernel or changing the determinant.
Exponentiating(5) yields(6).
This is a scalar operator in N(Z), not a dimension-normalized amplification of an arbitrary matrix, and no nonabelian determinant-to-polynomial transfer is inferred.

For any specified full order O containing alpha and alpha^-1, O_0 is contained in O, so the exact rational admissible class enlarges and E_T^O<=E_T^(O_0).
Every nonzero O element still has a nonzero integer field norm, giving the SAME lower bound exp(-2Tm/d) by(9)--(10).
Thus the same fixed-input limit holds for E_T^O as a corollary of the monogenic (SD) and(5), even without separately invoking an O version of strong duality.
If an actual integral basis of O has power-basis inclusion matrix B, then A_O=B A_T and |det B|=[O:O_0], so

    det(A_O A_O^T)=[O:O_0]^2 D_T.                  (19)

Any direct determinant upper bound using dual completeness for O must retain precisely that actual index factor.
The argument has not identified the chosen order with the maximal order or assumed that short-window energy1 extends to arbitrary overorders.

<a id="integer-capacity-full-arithmetic-costs"></a>
## 6. Original norms, denominators and support costs

For a rational packet let q be its ACTUAL least common positive coefficient denominator, F_b=q f_b, M_w its ACTUAL least positive final weight denominator and p_b=M_w omega_b>0 integers with sum p_b=M_w.
Its normalized nonzero actual residues are a_b=f_b(alpha).
Retaining signs and original degree, the full formulas are

    Res(P,F_b)=q^d Norm(a_b),
    product_b Res(P,F_b)^p_b
          =q^(d M_w) product_b Norm(a_b)^p_b,
    sum_b omega_b||F_b||_2^2=q^2 E,
    sum_b p_b||F_b||_2^2=M_w q^2 E.                 (20)

If the packet started with Laurent coordinates g_b in a common support [L,U], then f_b=t^(-L)g_b and T=U-L.
The actual residue is a_b=alpha^(-L)g_b(alpha), so Norm(a_b)=Norm(alpha)^(-L)Norm(g_b(alpha)), with Norm(alpha)=+1 or-1.
This original-degree MONOMIAL SIGN factor remains in each full signed resultant and copied product; its absolute value is1 and only therefore disappears from the logarithmic inequalities.
No assumption Norm(alpha)=1 is introduced in the generic unit case.

Every F_b is a nonzero integral coefficient polynomial, so ||F_b||_2^2>=1.
Consequently q^2 E>=1 and the total copied integer energy is at least M_w.
Along any sequence of rational packets with E tending to0, their q must tend to infinity.
Contents are retained in F_b: dividing one F_b by its content changes its residue, full resultant, all its lag contributions and energy.
Such a division is not an innocuous way to preserve the same feasible packet.
Increasing M_w by splitting labels also supplies no free normalized-energy gain.

The stronger packet inequality(10) retains the weighted full-norm income Lambda.
The capacity lower bound merely uses Lambda>=0; it does not claim that near-optimal packets consist of units, preserve a fixed norm inventory, or have predetermined ideals.
Conditional on(4), for every T one may choose a finite rational packet with energy at most twice the positive upper bound C_d N/D_T^(1/d), by the definition of infimum.
Any such chosen packet obeys

    0<=Lambda<=(1/2)log(2C_d N/D_T^(1/d))+(T/d)m
            =[(d-c)/(2d)]log N+O_(P,d)(1)            (21)

using(14).
This is a bound on its weighted log norms, not their individual sizes or a unit-selection theorem.
The proof supplies no upper bounds on q, M_w, label count, numerator heights or near-optimal W denominators.
The full coefficient/window and denominator costs remain even though they cancel algebraically in the normalized rate.

The limits hold with P and d fixed FIRST.
They provide neither a convergence window T<=C d uniform in P nor an energy deficit bounded away from zero at T=d.
A sufficient new uniform result would be fixed C,epsilon>0 and, for every input, some allowed window T<=C d with E_T<=1-epsilon; then(10) would give m>=log(1/(1-epsilon))/(2C).
Neither(12), (14) nor the input-dependent upper constant supplies that uniform statement.
Thus this capacity formula reorganizes the fixed-input determinant/energy relationship; it does not resolve the unrestricted Lehmer gap, a unit-only capacity, or the fixed seed-inventory questions of other Claims.

<a id="integer-capacity-asymptotic-author-self-check"></a>
## 7. Complete author self-check and outstanding adoption

The author checked Sections1--6 as a complete CONDITIONAL argument, with (SD) its sole new unresolved project dependency.
The check covers the precise rational packet/finite-hull/whole-residue class from C16; rank at T=d-1; eigenvalue, inversion and determinant directions in(7)--(8); the exact Sch09 form/domain and dimension-dependent constant; the need for strong duality at the upper-capacity step; infimum/supremum versus attainment; generic monic C10 applicability and every original nonzero integer norm in(9)--(10); k=T+1-d and the empty determinant endpoint; saturated integer relation basis and symbol |P|^2; the exact retained Szego scope at circle zeros and the fixed-degree passage to(12).

For the local conditioning refinement the check covers all distinct roots, complex row scalings and their conjugates, exterior reindexing with the ORIGINAL terminal exponent T, the identity circle diagonal, distinct-phase off-diagonal sums, all three cross-block types including exterior/interior product1, positive-definite limiting kernels via Vandermonde, the full Delta denominator and N^c factor, empty root blocks and the absence of an input-uniform remainder.
No root was selected or lost through a real/complex-pair convention.

The check also covers both directions of the squeeze in(17), the distinction between the capacity sandwich and a leading-term equality, scalar trace1 and the original degree in(6), formal-real capacity through C16 rather than irrational field norms, overorder inclusion and the actual squared index in(19), common Laurent support and signed unit monomial norms, every q^d/q^2/M_w factor and retained content in(20), existence of a finite twice-upper-bound packet without a minimum, the weighted-norm rather than individual-norm conclusion in(21), and the failure to obtain the uniform finite window/deficit required for G0001.

This is author self-review with disclosed root contribution, not a separate whole noncontributor review.
Before unconditional fixed adoption, root must supply an adopted fixed exact (SD) statement/argument covering this entire residue class and every T>=d-1, and arrange separate whole review of this capacity connection and any included refinement.
Sch09-U002 and the retained Den09 inputs are resolved only at their stated source-inspection scope; no original source-proof audit or priority claim is added.
No native mathematical program, numerical scan, solver or J was used.
G0001 remains active and unrestrictedly unresolved.

<a id="integer-capacity-asymptotic-entire-author-freeze"></a>
The complete authored revision through Section7 is ready for separate whole review.
Preserve all statements, complete proofs, actual inputs, conditional-dependency boundaries, arithmetic costs and self-check when fixing this account; a short theorem extraction alone does not retain this author's full work.
Later resolution of (SD) must cite its exact fixed support and actual adoption, without retroactively expanding C16 v1's weak-duality statement or this author-check's scope.


## Registration and preservation operation

2026-10-11T18:49: retain the COMPLETE original D13 author account, its self-check and conditional freeze, with only first-title depth and final whitespace normalization.
Its original freeze supplies a date/section scope, not a precise frozen minute; none is invented here.
The separate current assembly supplies the actually adopted fixed SD proof.
The independent reviewer must bind this unconditional C statement/argument and fixed-input interface after actual inspection.
Original working addresses are retired only after full-body comparison and locator maintenance.
No native mathematical program, new allowance or Task completion accompanies registration.

## Retained conditional-account locator maintenance

2026-10-11T19:03: the historical D12 candidate link in the original conditional account now reaches the SAME preserved author statement in fixed C17 before the D address is retired.
Its old as-of-revision conditional prose is unchanged; current unconditional reliance remains solely the explicit adopted C17 assembly/decision above.
This navigation repair creates no retrospective author acceptance or review coverage.
