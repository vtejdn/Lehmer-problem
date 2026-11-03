---
author: Yin
---
# Exact boundary charge and scalar-certificate recovery for integer polynomial shears

Date: 2026-10-12T13:38.
Human author Yin.
Fixed extraction under the continuing G0001 authorization.
The original g0001_routes author supplied all new mathematics in the complete D28 at its actual 21:25 freeze; root supplied only the broad matrix/group-determinant question.
The fresh g0001_matrix_recovery collaborator authors this statement, initial assessment and preservation wrapper, and is therefore a contributor to this extraction, not an independent reviewer of it.
The separate original whole R295 finding inspected the original D28 body only.
A different noncontributor must actually review this allocated extraction before adoption.
All original allocation, reuse, candidate, proof, limitations, roles and freeze are retained below.

## Statement

Let P(t)=sum_(i=0)^d p_i t^i be an ACTUAL monic irreducible nontorsion algebraic-unit polynomial in Z[t], of degree d>=2.
Let alpha be a root, K=Q(alpha), O0=Z[alpha], and let beta_1,...,beta_d be ALL its original roots.
Put m(P)=sum_i log max(1,abs(beta_i)).
All logarithms are natural.
For every Q in Z[t] form the actual integer polynomial matrix

    A_Q(t)=[[1,Q(t)],[0,P(t)]]
          =diag(1,P(t)) U_Q(t),
    U_Q(t)=[[1,Q(t)],[0,1]].

The conclusions below keep this same scalar P, original field, order, full degree and roots, the group Z, and unnormalized matrix trace throughout.

**A. Full operator and exact open-convolution boundary identity.**
The shear U_Q is unimodular over Z[t], with inverse U_(-Q), and det A_Q=P exactly.
For the original Haar unitary U over Z and trace Tr_2 tensor Haar probability, both singular-value logarithms are integrable and

    log Delta(A_Q(U))=m(P).

The kernel has zero Haar dimension, so the unmodified and kernel-removed determinant conventions agree here.
Replacing Tr_2 by Tr_2/2 would give m(P)/2 and changes the normalization.

For each positive integer N let E_N be the polynomials of degree at most N-1 with their Euclidean coefficient norm.
Let F_R:E_N -> coefficient space be multiplication by R with ALL output coefficients retained, and let Pi_N project onto output positions 0,...,N-1.
Define

    G_N=F_P^*F_P, D_N=det G_N,
    T_Q=Pi_N F_Q, B_Q=(Id-Pi_N)F_Q.

Then G_N is positive definite and D_N is a positive integer.
The full Gram H_(N,Q) of the map (x,y)->(x+Qy,Py), with both inputs in E_N, is

    H_(N,Q)=[[Id_N,T_Q],
             [T_Q^*,F_Q^*F_Q+G_N]],
    det H_(N,Q)=det(G_N+B_Q^*B_Q)
               =D_N det(Id+B_Q G_N^-1 B_Q^*).

The last identity uses the actual finite tail rows of B_Q.
In particular the exact boundary charge is

    b_(N,Q)=log(det H_(N,Q)/D_N)
            =log det(Id+B_Q G_N^-1 B_Q^*)>=0.

It vanishes exactly when B_Q=0.
No truncated-output Gram substitutes for the full output in these identities.

**B. Exact arbitrary-polynomial rank, height growth and fixed-input bound.**
If Q is constant, including Q=0, then B_Q=0 and b_(N,Q)=0.
Otherwise let L=deg Q>=1.
Then

    rank B_Q=min(N,L).

For fixed P,N and nonconstant Q0 of degree L, put r=min(N,L) and let mu_1,...,mu_r be the positive eigenvalues of

    G_N^(-1/2) B_(Q0)^* B_(Q0) G_N^(-1/2).

For every positive integer H,

    b_(N,HQ0)=sum_(i=1)^r log(1+H^2 mu_i)
             =2r log H+sum_i log mu_i+o(1)

as H->infinity at these FIXED P,N,Q0.
The full determinant det H_(N,HQ0) is an integer polynomial in H^2 of exact degree r and positive integer leading coefficient.
Thus its amplification is unbounded even at fixed input and fixed matrix support width.

Let c be the number of original roots on the unit circle, with multiplicity, and define

    a_P=product_(abs(beta_i)!=1) abs(abs(beta_i)-1)>0,
    K_Q=sum_i abs(q_i),

using 1 for the empty product.
Then, for every N>=1 and y in E_N,

    ||Py||_2>=a_P (N+d)^(-c)||y||_2,
    lambda_min(G_N)>=a_P^2 (N+d)^(-2c),
    ||B_Q||<=K_Q.

For nonconstant Q,

    0<=b_(N,Q)
      <=min(N,L) log[1+K_Q^2 a_P^(-2) (N+d)^(2c)].

All expanding, contracting and circle roots remain in these estimates.
The constants can depend badly on P.
For FIXED P and FIXED Q this proves

    b_(N,Q)=O_(P,Q)(log(N+d)), b_(N,Q)/N->0.

Together with the accepted scalar Toeplitz theorem for abs(P)^2, including its circle zeros,

    log D_N/N->2m(P),
    log det H_(N,Q)/(2N)->m(P).

These are fixed-input limits only.
No degree-uniform conditioning estimate or uniform interchange of varying P,Q,N is asserted.

**C. Exact monomial control and all-height false gain.**
For Q=H t^L with nonzero integer H and L>=1,

    B_Q^*B_Q=H^2 E_(N,L),

where E_(N,L) projects onto the LAST min(N,L) input coordinates.
In particular, if L>=N,

    det H_(N,Ht^L)=det(G_N+H^2 Id_N),
    (1/N)log det(G_N+H^2 Id_N)
      >=log[D_N^(1/N)+H^2]>=log(1+H^2).

Put gamma_(N,Q)=log det H_(N,Q)/(2N).
For N=L=d, the actual matrix union support width is exactly d and the maximum output exponent on degree<d inputs is 2d-1, yet gamma_(d,Ht^d) is unbounded as abs(H)->infinity.
With B_P=sum_i abs(p_i) and H=B_P+1,

    gamma_(d,Ht^d)>=log(1+H^2)/2>log B_P>=m(P).

Even H=1 gives gamma_(d,t^d)>=log(2)/2.
These are finite open-compression values, not scalar lower certificates.
The full circle determinant remains P; the exact excess over the scalar finite log determinant log D_N is b_(N,Q).
All these examples have coefficient denominator 1, matrix rank 2 over Q(t), actual matrix width max(d,L), and squared coefficient sum 1+H^2+sum_i p_i^2.
They require no near-one family, rational denominators, omitted companion or matrix-trace division.

**D. Periodic realization with original signed norm and full trace.**
Let C_N be the N-by-N cyclic permutation matrix, including C_1=[1].
Every P(C_N) is invertible because no original root of P is torsion.
Then

    det A_Q(C_N)=det P(C_N)
       =product_(zeta^N=1)P(zeta)
       =(-1)^(Nd) Norm_(K/Q)(alpha^N-1).

This is the full SIGNED ordinary determinant with all original d conjugates, not the smaller possible degree of alpha^N.
Its nonzero norm is an integer.
The full periodic Gram determinant is the square of this quantity and is independent of Q.
With the canonical finite cyclic group trace Tr_N/N and UNNORMALIZED matrix trace Tr_2, the logarithmic determinant is

    (1/N)log abs(Norm_(K/Q)(alpha^N-1)).

There is no extra division by 2 beyond taking the square root of the Gram determinant.
The periodic U_Q(C_N) is an integer unimodular matrix; it preserves the full periodic determinant.
By contrast, the polynomial U_Q does not generally preserve the finite open input space.
This is an exact finite comparison.
It supplies no proof of periodic convergence, fixed-input or uniform, in the presence of neutral conjugates.

**E. Exact payment returns to the inherited scalar certificate.**
Put Delta_P=abs(disc P)>0.
At the actual orbit trajectory length N+d, L4's full scalar certificate is

    m(P)>=[log Delta_P+log D_N-d log(N+d)]/[2(N+d-1)].

For every Q it becomes exactly

    m(P)>=[log Delta_P+log det H_(N,Q)
                 -b_(N,Q)-d log(N+d)]/[2(N+d-1)].

After the full charge b_(N,Q) is paid, this is IDENTICALLY the old certificate for the same P and N.
Varying Q within this triangular class cannot improve that certificate.
Omitting the charge adds exactly b_(N,Q)/[2(N+d-1)] to the alleged lower bound.
For fixed P,N and every nonconstant Q0 this omitted error is unbounded along Q=H Q0 as H->infinity, while the true m(P) stays fixed; the uncorrected substitution is therefore invalid within the stated original irreducible unit domain.

At t=alpha, A_Q(alpha) has determinant zero and contains the zero entry P(alpha), so it is not itself a packet of nonzero original-order scalar values.
A norm-floor argument requires an actual legal scalar packet with all its lags, weights, signed norms and width.
The finite matrix Gram alone supplies no missing same-exponent arithmetic income.

These conclusions close the proposed free replacement of D_N by this sheared full Gram, with its exact compensating boundary determinant.
They do not rule out other matrix constructions or bounds using additional arithmetic data, and they neither supply nor disprove a degree-uniform arithmetic surplus or an unrestricted G0001 solution.
The new finite algebra is proved locally.
The only asymptotic theorem used is the retained scalar Toeplitz input at its exact Den09-U002 scope; no new original source proof, general-group theorem or native computation is claimed.

## Current assessment
[Selected decision](#decision-independent-current-whole-review-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T13:38 |
| status | open |
| reason | Register the exact original-scalar integer-shear boundary identity, rank and complete height/root/window costs, monomial false-gain family, signed periodic norm and full-trace convention, and exact paid recovery of L4. The entire original 21:25 D28 is retained. R295 supplies original whole review support only. The fresh wrapper contributor is not an independent reviewer; actual separate extraction review and an adoption decision remain pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E with all original-input hypotheses, full finite maps, rank/height/root costs, trace and sign conventions, fixed-input limits and failure boundaries. |
| argument | [Entire retained author body](#argument) | Complete D28 allocation/reuse/candidate, Sections 1--7 and equations 1--17, source limits, author roles, checking and actual 21:25 freeze. |
| dependency | [Original scalar Gram certificate](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate) | Monic squarefree full-root relation/orbit Gram at trajectory length N+d, discriminant, dimension cost and denominator 2(N+d-1); no computation or degree-uniform claim. |
| dependency | [Scalar logarithmic determinant and Fourier convention](../audits/literature/Den09/Yin_U001.md#den09-u001) | Exact fk-determinant and group-fourier-convention subsections: finite trace and spectral logarithm, Gram square-root factor, Haar probability on the single original Z, scalar log-polynomial with circle zeros and inversion convention. Foundational proof-inspection limits retained. |
| dependency | [Scalar finite-section theorem](../audits/literature/Den09/Yin_U002.md#den09-u002) | Exact finite-section-determinant subsection, Theorem 2 for scalar bounded nonnegative abs(P)^2 with finite circle zeros. Fixed P only; original Sim05 proof remains uninspected, and no general noninvertible matrix approximation theorem is used. |
| dependency | [Full matrix trace and kernel convention](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Exact luc22-kernel-removed-determinant subsection: unnormalized matrix trace, kernel-removed agreement for these injective maps, finite group normalization abs(det)^(1/N) without rank division. |
| support | [Commutative scalar-return distinction](../audits/literature/Luc22/Yin_U002.md#luc22-u002) | Exact luc22-ore-determinant-interface subsection: same-ring commutative determinant versus quotient of scalar determinants; no general Ore theorem is required for the direct triangular calculation. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0295_v1.md#integer-shear-whole-independent-finding) | Actual complete 21:25 D28 and its direct interfaces only. This historical whole finding does not inspect the new statement/wrapper or adopt this extraction. |


### Decision current-scalar-gram-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:32 |
| status | proved |
| reason | Select C209#gram-lower-certificate as the current responsible home of the identical retained L4 scalar Gram argument and full-dimension certificate. Its actual current statement and original saturated-kernel, dual-Gram and Vandermonde/Hadamard passages were read at this existing interface. Mathematical status, selected statement/argument/review and every scope are inherited unchanged; this is current locator maintenance, not a new proof or independent review. The older decision and the selected review retain their actual original L4 inputs and dates. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E with all original-input hypotheses, full finite maps, rank/height/root costs, trace and sign conventions, fixed-input limits and failure boundaries. |
| argument | [Entire retained author body](#argument) | Complete D28 allocation/reuse/candidate, Sections 1--7 and equations 1--17, source limits, author roles, checking and actual 21:25 freeze. |
| dependency | [Original scalar Gram certificate](Yin_C_G0209_v1.md#gram-lower-certificate) | Monic squarefree full-root relation/orbit Gram at trajectory length N+d, discriminant, dimension cost and denominator 2(N+d-1); no computation or degree-uniform claim. |
| dependency | [Scalar logarithmic determinant and Fourier convention](../audits/literature/Den09/Yin_U001.md#den09-u001) | Exact fk-determinant and group-fourier-convention subsections: finite trace and spectral logarithm, Gram square-root factor, Haar probability on the single original Z, scalar log-polynomial with circle zeros and inversion convention. Foundational proof-inspection limits retained. |
| dependency | [Scalar finite-section theorem](../audits/literature/Den09/Yin_U002.md#den09-u002) | Exact finite-section-determinant subsection, Theorem 2 for scalar bounded nonnegative abs(P)^2 with finite circle zeros. Fixed P only; original Sim05 proof remains uninspected, and no general noninvertible matrix approximation theorem is used. |
| dependency | [Full matrix trace and kernel convention](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Exact luc22-kernel-removed-determinant subsection: unnormalized matrix trace, kernel-removed agreement for these injective maps, finite group normalization abs(det)^(1/N) without rank division. |
| support | [Commutative scalar-return distinction](../audits/literature/Luc22/Yin_U002.md#luc22-u002) | Exact luc22-ore-determinant-interface subsection: same-ring commutative determinant versus quotient of scalar determinants; no general Ore theorem is required for the direct triangular calculation. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0295_v1.md#integer-shear-whole-independent-finding) | Actual complete 21:25 D28 and its direct interfaces only. This historical whole finding does not inspect the new statement/wrapper or adopt this extraction. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0794_v2.md#c73-integer-shear-actual-extraction-finding) | Complete actual statement, ENTIRE original preservation and all exact direct/assembly interfaces inspected after allocation by a noncontributor. Original whole finding remains at its original scope. |


### Decision independent-current-whole-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:10 |
| status | proved |
| reason | Adopt the separately organized current fixed-target finding after complete statement and retained-argument inspection, including late extensions, actual costs, controls, necessary mathematical interfaces and source limits, while excluding credited comparison scopes first separately checked after old-review exposure. The initial mathematical conclusion was formed at 2026-10-22T22:46 UTC before old-target review comparison. The finding records the exact interface and later credited-comparison reading sequence. Preserve fixed mathematics, historical decisions, all non-review premises and their scopes; retain known sufficient independent findings in their original homes and original unknown findings at their actual checking scope. This selects current review evidence and supplies no new research, Task completion or execution resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement: statement](#statement) | Entire A--E with all original-input hypotheses, full finite maps, rank/height/root costs, trace and sign conventions, fixed-input limits and failure boundaries. |
| argument | [Argument: argument](#argument) | Complete D28 allocation/reuse/candidate, Sections 1--7 and equations 1--17, source limits, author roles, checking and actual 21:25 freeze. |
| dependency | [Dependency: gram-lower-certificate](Yin_C_G0209_v1.md#gram-lower-certificate) | Monic squarefree full-root relation/orbit Gram at trajectory length N+d, discriminant, dimension cost and denominator 2(N+d-1); no computation or degree-uniform claim. |
| dependency | [Dependency: den09-u001](../audits/literature/Den09/Yin_U001.md#den09-u001) | Exact fk-determinant and group-fourier-convention subsections: finite trace and spectral logarithm, Gram square-root factor, Haar probability on the single original Z, scalar log-polynomial with circle zeros and inversion convention. Foundational proof-inspection limits retained. |
| dependency | [Dependency: den09-u002](../audits/literature/Den09/Yin_U002.md#den09-u002) | Exact finite-section-determinant subsection, Theorem 2 for scalar bounded nonnegative abs(P)^2 with finite circle zeros. Fixed P only; original Sim05 proof remains uninspected, and no general noninvertible matrix approximation theorem is used. |
| dependency | [Dependency: luc22-u001](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Exact luc22-kernel-removed-determinant subsection: unnormalized matrix trace, kernel-removed agreement for these injective maps, finite group normalization abs(det)^(1/N) without rank division. |
| support | [Support: luc22-u002](../audits/literature/Luc22/Yin_U002.md#luc22-u002) | Exact luc22-ore-determinant-interface subsection: same-ring commutative determinant versus quotient of scalar determinants; no general Ore theorem is required for the direct triangular calculation. |
| support | [Support: integer-shear-whole-independent-finding](../audits/reviews/Yin_R_G0295_v1.md#integer-shear-whole-independent-finding) | Actual complete 21:25 D28 and its direct interfaces only. This historical whole finding does not inspect the new statement/wrapper or adopt this extraction. |
| review | [Current isolated finding](../audits/reviews/Yin_R_G0794_v2.md#g73-current-independent) | Complete current mathematical statement and retained proof, including all late extensions, paid arithmetic, useful controls and accepted necessary interfaces at their exact scopes; exclude post-initial credited comparison scopes identified by the finding; initial conclusion 2026-10-22T22:46 UTC, then old-finding comparison; actual interface and credited-comparison reading limits are disclosed in the finding. |

## Registration and complete preservation

The [original complete D28 freeze](#integer-shear-entire-author-freeze) is extraction ancestry, not a new proof dependency.
The ENTIRE original body follows after removal of its duplicate author/framework front matter, demotion of its first title by one hash, and normalization of line endings and terminal/separating blank lines.
Every original paragraph, formula, explicit anchor, candidate declaration, reuse history, author/self-checking role, limitation and freeze is retained.
All original ../ledger/, ../claims/ and ../audits/ locators are valid from this Claim directory and need no rebasing.
No summary replaces any part of the proof.

The current wrapper and initial decision are authored by the fresh recovery collaborator under human Yin.
The original proof and freeze belong to g0001_routes, root's original contribution was the broad question, and R295 records the separate noncontributor whole review at its own exact input.
Their roles are not reassigned.
The original body's prospective review language is preserved as history; the selected initial assessment above states this new extraction's actual pending review.
Literal preservation and structural checking supply no independent mathematical acceptance.
No D retirement or adoption accompanies this registration.

## Argument

## Exact boundary cost of determinant-preserving integer polynomial shears

Date: 2026-10-12T13:19.
Human author Yin.
AUTHOR inquiry by g0001_routes under the continuing G0001 instruction.
Root supplied only the broad distinct matrix/group-determinant question, not this matrix, formulas or argument.
This author chooses the construction and owns its mathematical development.
No native mathematical program, new J or source acquisition is planned.

## Bounded reuse and precise changed mechanism

The actual S5 Fourier and S6 integral-presentation routes retain their full original-input and complete companion costs.
The more directly relevant S3 determinant route requires the SAME scalar P and unnormalized matrix trace.
[L1](../ledger/Yin_L_G0001_v1.md#lehmer-route-assessment) already excludes inference from small determinants in changed finite groups and normalized matrices.
[L4](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate) supplies the original orbit/relation Gram with its discriminant and full degree penalty; [L241](../ledger/Yin_L_G0241_v1.md#sharp-joint-auxiliary-determinant) already optimizes its joint auxiliary ratio.
These facts are not reproved as new results.

[Den09-U001](../audits/literature/Den09/Yin_U001.md#fk-determinant) and [its Fourier convention](../audits/literature/Den09/Yin_U001.md#group-fourier-convention) identify the scalar logarithmic determinant.
[Luc22-U001](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant) retains the unnormalized matrix trace and the kernel convention; [Luc22-U002](../audits/literature/Luc22/Yin_U002.md#luc22-ore-determinant-interface) distinguishes a scalar quotient from an integral scalar and the commutative determinant return.
Their actual local scope was read.
No general-group theorem or original foundational source proof is newly adopted.
[C18](Yin_C_G0018_v1.md#statement) already has the exact fixed-input capacity/FK rate, and [C36](Yin_C_G0036_v1.md#statement) has the rational-denominator price.
Neither is the new question here.
L380's rational Laurent pole obstruction is likewise a different mechanism.

A targeted screen of actual G Claims, ledgers and drafts for polynomial shears, finite compression, boundary/Hankel defects and triangular Toeplitz comparison found the above old certificates and general warnings, but no exact theorem for the complete construction below.
This is bounded reuse, not historical novelty.
One initial Windows wildcard-path search was rejected before returning evidence and was repeated correctly with rg filename globs.
No mathematical run is hidden in this screen.

<a id="integer-shear-responsible-candidate"></a>
## Candidate, exact construction and next obligations

Keep an ACTUAL monic irreducible nontorsion algebraic-unit polynomial P in Z[t], original degree d>=2, field K=Q(alpha), order O0=Z[alpha], all original roots and total m(P).
For ANY Q in Z[t], choose the actual2-by-2 integer polynomial matrix

    A_Q(t)=[[1,Q(t)],[0,P(t)]].

Its full determinant is EXACTLY P, with no scalar factor, degree division or changed group.
The intended comparison is between the Gram of its full convolution applied to finitely supported input vectors and its actual periodic finite cyclic realization.
A proposed Schur calculation should expose an explicit positive boundary matrix from the part of Q times an input that leaves the retained coefficient interval.
The actual finite determinant may grow even while det A_Q and the scalar field remain fixed; that term must be paid before returning to a scalar lower certificate.

The author will derive the exact finite formula, both coefficient/physical-width costs and a fully symbolic monomial-shear control, then compare its full periodic determinant with the actual original cyclic norm.
All statements, any failed strengthening and the precise entropy/arithmetic direction will be retained here.
This allocation is a candidate, not a result or an independent finding.
No new native program or source theorem is needed for the intended elementary convolution, Schur and finite determinant calculation.


<a id="integer-shear-full-operator"></a>
## 1. Exact same-scalar matrix and full group normalization

Keep P,alpha,K,O0,d and all original conjugates beta_1,...,beta_d as above.
Put

    A_Q(t)=[[1,Q(t)],[0,P(t)]]
          =diag(1,P(t)) U_Q(t),
    U_Q(t)=[[1,Q(t)],[0,1]], U_Q^-1=[[1,-Q(t)],[0,1]].     (1)

For EVERY integer polynomial Q this is a unimodular change of polynomial presentation over Z[t], with det A_Q=P EXACTLY.
No neutral scalar factor, positive companion factor or field extension has been introduced.
For z on the circle away from the finitely many roots of P, the matrix is invertible.
Its two singular values s_1(z),s_2(z)>0 satisfy s_1*s_2=|P(z)|.
Its entries are bounded, so log-positive parts are bounded; integrability of log|P| and that identity also give integrability of the log-negative parts of BOTH singular values.
It follows directly, with the UNNORMALIZED trace Tr_2 tensor circle Haar probability, that

    log Delta(A_Q(U))=integral(log s_1+log s_2)=m(P).       (2)

Here U is ONE original Haar unitary over Z, not two free variables or a changed group.
The kernel has zero Haar dimension, so the Den09 unmodified and Luc22 kernel-removed conventions agree here.
Normalizing Tr_2 by1/2 instead gives m(P)/2 and is not the original scalar normalization.
The equality(2) is the elementary commutative determinant identity under the already accepted Fourier conventions, not a new FK gap theorem.

## 2. Full convolution on a finite input window and the exact boundary determinant

Fix any positive INTEGER N.
Identify E_N with coefficient vectors of polynomials of degree at most N-1, with the ordinary Euclidean coefficient norm.
Work in the full one-sided coefficient space, allowing ALL output coefficients.
Let F_R:E_N -> coefficients denote multiplication by a polynomial R, and let Pi_N project outputs to coefficients0,...,N-1.
Define

    G_N=F_P^* F_P, D_N=det G_N,
    T_Q=Pi_N F_Q, B_Q=(Id-Pi_N)F_Q.                      (3)

G_N is positive definite: multiplication by a nonzero polynomial is injective.
Its entries are integers, so D_N is a positive integer, in particular D_N>=1.
It is precisely the scalar Toeplitz Gram of N shifts of P.
B_Q is the ACTUAL omitted-output tail of multiplication by Q; its finitely many nonzero rows are retained in every determinant below.
No output truncation is substituted for the full Gram.

Apply A_Q to two input polynomials x,y in E_N.
The output is(x+Qy,Py).
Its full coefficient Gram H_(N,Q), of size2N, is

    H_(N,Q)=[[Id_N,T_Q],
             [T_Q^*,F_Q^*F_Q+G_N]].

Since F_Q^*F_Q=T_Q^*T_Q+B_Q^*B_Q, elimination using the identity first block gives the EXACT formula

    det H_(N,Q)=det(G_N+B_Q^*B_Q)
               =D_N det(Id+B_Q G_N^-1 B_Q^*).            (4)

The second determinant has the actual number of tail rows.
To verify that equality without a determinant lemma assumption, compute the determinant of the block matrix [[G_N,-B_Q^*],[B_Q,Id]] by the two Schur complements.
Both needed diagonal blocks are invertible.
All finite matrices before G_N^-1 are literal integer coefficient matrices.

Write the full boundary charge

    b_(N,Q)=log[det H_(N,Q)/D_N]
            =log det(Id+B_Q G_N^-1 B_Q^*)>=0.            (5)

Equality holds exactly when B_Q=0, since G_N is positive definite and every nonzero positive-semidefinite eigenvalue contributes a strictly positive logarithm.
Thus the full matrix's finite input compression is NOT invariant under this unimodular polynomial shear, although its entire circle determinant is unchanged.

<a id="integer-shear-exact-rank"></a>
## 3. Exact boundary rank and complete height control

If Q is constant, including Q=0, then B_Q=0.
Otherwise write Q=sum_(i=0)^L q_i t^i with ACTUAL degree L>=1 and q_L!=0.
Its only possible tail rows are N,...,N+L-1.
Their entry in input column k is q_(j-k), with coefficients outside0,...,L zero.
Consequently

    rank B_Q=min(N,L).                                  (6)

For N>=L, restrict to rows N+j and columns N-L+k,0<=j,k<L.
The entry is q_(L+j-k), zero below the diagonal j>k and q_L on the diagonal.
This L-by-L triangular minor is nonzero.
For N<L, use rows L+j and columns k,0<=j,k<N; all selected rows are in the tail and the same triangular calculation gives a nonzero N-by-N minor.
The upper bound follows from the row and column counts.
This proves the rank for arbitrary integer lower coefficients, not merely monomial Q.

In particular, for a fixed nonconstant integer Q_0 of degree L and Q=H Q_0, H a positive INTEGER, let mu_1,...,mu_r be the positive eigenvalues of G_N^-1/2 B_(Q_0)^*B_(Q_0)G_N^-1/2, r=min(N,L).
Then(4) gives

    b_(N,HQ_0)=sum_(i=1)^r log(1+H^2 mu_i)
              =2r log H+sum_i log mu_i+o(1)              (7)

as H->infinity at FIXED P,N,Q_0.
All mu_i are positive real numbers belonging to these exact rational finite matrices; they are not required to be field conjugates or integers.
The left determinant det H_(N,HQ_0) itself is an integer polynomial in H^2 with positive leading coefficient and degree r.
This follows either from(4) and its nonzero eigenvalues, or from the direct integer determinant expansion; multiplying D_N by the nonzero leading product gives the same positive integer coefficient.
Therefore the boundary amplification is unbounded even for fixed P,N and fixed matrix support width.

A useful fixed-input upper cost can also be proved directly.
Let c be the number of original roots on the unit circle, counted with multiplicity, and set

    a_P=product_(|beta_i|!=1) abs(abs(beta_i)-1)>0,
    K_Q=sum_i |q_i|.

The empty product is1.
If y has at most M consecutive coefficient positions, then for |beta|!=1,

    ||(t-beta)y||_2 >= abs(abs(beta)-1)||y||_2,

by the reverse triangle inequality and invariance of coefficient norm under multiplication by t.
For |beta|=1, write g=(t-beta)y.
The recurrence y_j=beta^-1 y_(j-1)-beta^-1 g_j, starting y_(-1)=0, gives |y_j|<=sum_(k<=j)|g_k|.
Cauchy--Schwarz and summation give ||y||_2<=M||g||_2.
Apply these bounds successively to the COMPLETE factorization P=product_i(t-beta_i), whose intermediate input lengths are at most N+d.
Thus

    ||P y||_2 >= a_P (N+d)^(-c)||y||_2,
    lambda_min(G_N)>=a_P^2 (N+d)^(-2c).                 (8)

No expanding, contracting or neutral root is discarded; a_P may depend badly on the original input.
Also ||B_Q||<=||F_Q||<=K_Q by the triangle inequality for shifts.
Together with the exact rank,

    0<=b_(N,Q)
      <=min(N,L) log[1+K_Q^2 a_P^-2 (N+d)^(2c)]          (9)

for L>=1, with b=0 for constant Q.
This is a fully specified boundary upper cost, not a degree-uniform condition estimate.

For FIXED P and FIXED Q, (9) gives b_(N,Q)=O_(P,Q)(log(N+d)) and b_(N,Q)/N->0.
Combining only this estimate with the OLD scalar Toeplitz limit for D_N yields

    lim_(N->infinity) log det H_(N,Q)/(2N)=m(P).          (10)

The accepted scalar limit is [Den09-U002's finite-section theorem](../audits/literature/Den09/Yin_U002.md#finite-section-determinant), also retained by L4.
This is not a new proof of the capacity/FK rate in C18, and no uniform interchange of Q,P or N is made.
Rather(9) identifies the presentation-specific extra cost which vanishes in this fixed-input limit but need not be small at a degree-linear window.

<a id="integer-shear-monomial-control"></a>
## 4. Fully symbolic monomial shear and degree-linear artificial excess

For Q=H t^L, H a nonzero INTEGER and L>=1, the actual tail satisfies

    B_Q^*B_Q=H^2 E_(N,L),

where E_(N,L) is the diagonal projection onto the LAST min(N,L) input positions.
In particular L>=N gives

    det H_(N,Ht^L)=det(G_N+H^2 Id_N).                    (11)

This is an exact symbolic formula with no root approximation or native calculation.
If lambda_i>0 are G_N's eigenvalues, convexity of f(x)=log(exp(x)+H^2), whose second derivative is H^2 exp(x)/(exp(x)+H^2)^2>0, gives

    (1/N)log det(G_N+H^2 Id)
        >=log[D_N^(1/N)+H^2]>=log(1+H^2).               (12)

The first inequality is Jensen at x_i=log lambda_i; the second uses the actual positive integer D_N>=1.
Define the unnormalized-matrix finite rate gamma_(N,Q)=log det H_(N,Q)/(2N).
Then gamma_(N,Ht^L)>=log(1+H^2)/2 whenever L>=N.

Take specifically N=L=d.
The original scalar P is unchanged, the matrix's ACTUAL union support width is exactly d, and the finite input-to-output maximum width is2d-1.
Yet(7) makes gamma unbounded as the integer HEIGHT |H| grows.
More concretely, let B_P=sum_i |p_i| and choose H=B_P+1.
The circle pointwise bound and Jensen give m(P)<=log B_P, whereas

    gamma_(d,Ht^d)>=log(1+H^2)/2>log B_P>=m(P).          (13)

Thus a strict excess over the true full scalar logarithmic determinant occurs at a literal degree-linear input/output window for EVERY stated input, solely from a legal integer shear.
This is not a positive arithmetic-income construction: the exact excess is the charged boundary expression(5), and the underlying complete determinant remains P.
No small-Mahler input family is assumed.

Even H=1 gives the universal finite value gamma>=log2/2 at N=L=d.
This does NOT imply a universal Mahler gap; it is a finite compression value with a generally nonnegligible boundary charge.
No hypothesis that this value is a lower certificate is made.
The example exposes precisely why that inference would be false, rather than advertising a spurious scalar counterexample.

The construction has coefficient denominator q=1 throughout, matrix rank2 over Q(t), actual width max(d,L), and sum of squared polynomial coefficients1+H^2+sum_i p_i^2 in the monomial control.
All these costs are actual and recorded.
The discrepancy exists without rational denominators, high matrix rank, dropped companion factors or normalized matrix trace.

<a id="integer-shear-periodic-comparison"></a>
## 5. Periodic finite cyclic realization removes exactly this shear dependence

Let C_N be the actual N-by-N cyclic permutation matrix, including C_1=[1].
Substitute it into the SAME integer polynomial matrix:

    A_Q(C_N)=[[Id_N,Q(C_N)],[0,P(C_N)]].

Every root of P is nontorsion, so P(zeta)!=0 for every N-th root of unity zeta.
Thus P(C_N), and hence the entire2N-by-2N matrix, is invertible.
Its full SIGNED ordinary determinant is

    det A_Q(C_N)=det P(C_N)
       =product_(zeta^N=1) P(zeta)
       =(-1)^(Nd) Norm_(K/Q)(alpha^N-1).                (14)

To check the sign, for each original beta_i use product_(zeta^N=1)(zeta-beta_i)=(-1)^N(beta_i^N-1), then multiply over all d ORIGINAL roots.
There is no substitution of the smaller degree of alpha^N.
The exact nonzero integer Norm(alpha^N-1), all original conjugates, actual order O0 and full sign are retained.
The scalar coefficient denominator of alpha^N-1's representative is1; no packet weight denominator is being defined by a matrix trace.

The Gram determinant of this full periodic matrix is therefore the SQUARE of(14), completely independent of Q.
With the canonical finite cyclic group trace (1/N)Tr_N and the UNNORMALIZED matrix trace Tr_2, its logarithmic determinant is

    (1/N)log abs(Norm_(K/Q)(alpha^N-1)).                 (15)

There is no additional factor1/2 from matrix rank: the square root in the Gram determinant has already been taken.
This is an EXACT finite comparison, not a claim that cyclic determinants converge uniformly, or even a newly supplied proof of their fixed-input convergence in the presence of neutral conjugates.
Such asymptotic arithmetic needs its own actual input.

The periodic shear U_Q(C_N) is an integer unimodular matrix and preserves the full finite determinant; in contrast, U_Q does not preserve the truncated polynomial INPUT space because Qy can leave it.
Formula(4) is the exact resulting difference for the open input compression.
This explains the boundary source without discarding any original root or comparing normalized determinants from different groups as classical counterexamples.

<a id="integer-shear-original-scalar-certificate"></a>
## 6. Exact correction returns to the old scalar arithmetic certificate

L4's original full orbit/relation identity uses D_N as the Gram of N shifts of P and the actual trajectory window N+d.
Its proved scalar lower certificate is

    m(P)>=[log Delta_P+log D_N-d log(N+d)]
                      /[2(N+d-1)],                    (16)

where Delta_P=abs(disc P)>0.
The present irreducible characteristic-zero P is squarefree, so that interface applies.
Monicity, the entire degree and every original conjugate remain exactly as in L4.

Substituting the complete identity(5), the SAME valid certificate in the sheared variables becomes

    m(P)>=[log Delta_P+log det H_(N,Q)
                 -b_(N,Q)-d log(N+d)]/[2(N+d-1)].       (17)

After paying b_(N,Q), it is IDENTICALLY(16), for EVERY polynomial Q of this class.
Thus varying this complete integer shear cannot improve that inherited scalar certificate at a fixed actual input/window.
Omitting b adds exactly b/[2(N+d-1)] to the alleged lower bound.
For fixed P,N and any nonconstant Q_0, this omitted term is unbounded as Q=H Q_0 with H->infinity, by(7), while the actual m(P) stays fixed.
Hence the uncorrected replacement is conclusively invalid within the stated original irreducible unit domain.
This is stronger than observing that finite Toeplitz values usually approach a limit: it supplies the exact compensating determinant and a whole unbounded integer-presentation class.

This does not prove that every matrix mechanism is reducible to L4 or that all possible lower bounds built from H are useless.
It closes ONLY the proposed use of its full finite determinant as a free replacement for D_N under the exact triangular shear(1).
Other nontriangular constructions, additional arithmetic data and estimates not using this scalar certificate require separate analysis.

At t=alpha the matrix A_Q(alpha) is singular, with determinant P(alpha)=0.
It is therefore not itself a packet of nonzero scalar O0 values with a positive full copied norm.
Its entries 1,Q(alpha),P(alpha) include the zero P(alpha); the known nonzero entry1 has norm1 and Q(alpha) may or may not vanish.
No C10/C18 norm-floor argument can be assigned to all its entries or minors without first constructing a genuinely legal scalar packet and paying its actual lags, weights, signed norms and width.
This explicit arithmetic interface prevents confusing an integer finite matrix Gram determinant with the missing same-exponent arithmetic income.

## 7. Outcome, source boundary and author checking

This inquiry supplies the exact finite identity(4), arbitrary-polynomial boundary rank(6), complete height amplification and fixed-input upper cost(7)--(9), the symbolic degree-linear control(11)--(13), fully signed original periodic norm(14)--(15), and exact cancellation in the scalar certificate(17).
It is a concrete failure closure for determinant-preserving triangular integer shears, leaving the SAME P, original field, actual group Z and full trace fixed.
It is distinct from C18's old capacity asymptotic, C36's rational-denominator price, L241's all-auxiliary Gram optimization and the old topological/group-return cautions.

All new finite identities were derived directly from the actual coefficient maps, finite elimination and elementary norm/eigenvalue inequalities.
The only limiting input is the already accepted scalar Toeplitz theorem at its precise Den09-U002 scope; its classical original proof has not been newly reviewed.
The full-operator interpretation uses only the established Fourier/trace conventions.
There is no new primary-source theorem, group-transfer theorem, integer spectral gap, native program, scan or new J.
No statement here produces or disproves the original degree-uniform positive arithmetic surplus, near-one input family or unrestricted G0001.

Author checking includes the order A=diag(1,P)U_Q, original det and both matrix-trace normalizations; full output Gram rather than output truncation, both Schur eliminations and positivity/equality; actual triangular tail minors in BOTH N>=L and N<L cases, Q0/constant endpoints, full original-root lower singular bound including every neutral factor, fixed-input versus changing-input limits; monomial last-coordinate projection, convex logarithmic inequality, actual positive integer D_N, explicit H=B_P+1 control with width and height; cyclic sign(-1)^(Nd), original degree versus power degree, integer invertibility and complete norm; L4's N+d trajectory length, discriminant and full denominator, exact charge cancellation and the singular value at the original algebraic root.
This is AUTHOR checking and requires separately organized whole noncontributor review before any fixed extraction or adoption.

<a id="integer-shear-entire-author-freeze"></a>
## Entire author freeze

Freeze the ENTIRE allocation/candidate/reuse account and Sections1--7/equations1--17 at 2026-10-12T13:25, including every matrix, root, trace, coefficient/window/height cost, direct argument, fixed-input/source boundary and failed inference.
The author supplied all new construction and proof steps; root gave only the broad question.
Whole noncontributor review of this actual body is required before fixed extraction or adoption.
Scoped validation of this draft and its five actual L4/Den09/Luc22 inputs passed with checked6; that is structural evidence only.
The actual Den09 Theorem2 passage was reread at its scalar nonnegative-symbol scope, including circle zeros and the uninspected original Szego proof, before this freeze.
No matrix noninvertible approximation theorem is imported in its place.

No native mathematical run, J or source acquisition occurred.
The complete body is now frozen for root-organized independent review.

## Historical assessments

<a id="decision-organized-reviewed"></a>

### Historical assessment organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T13:50 |
| status | proved |
| review-status | independently reviewed |
| reason | Adopt original whole R295 and separate actual extraction R397. The same-scalar integer shear has its exact complete boundary determinant cost, true rank and fixed-input limit, explicit height-amplified false gain, signed periodic original norm and exact recovery of the fully paid L4 certificate. Canonical scalar/group trace and unnormalized matrix amplification remain separate. This is not a new arithmetic-income or unrestricted gap theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E with all original-input hypotheses, full finite maps, rank/height/root costs, trace and sign conventions, fixed-input limits and failure boundaries. |
| argument | [Entire retained author body](#argument) | Complete D28 allocation/reuse/candidate, Sections 1--7 and equations 1--17, source limits, author roles, checking and actual 21:25 freeze. |
| dependency | [Original scalar Gram certificate](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate) | Monic squarefree full-root relation/orbit Gram at trajectory length N+d, discriminant, dimension cost and denominator 2(N+d-1); no computation or degree-uniform claim. |
| dependency | [Scalar logarithmic determinant and Fourier convention](../audits/literature/Den09/Yin_U001.md#den09-u001) | Exact fk-determinant and group-fourier-convention subsections: finite trace and spectral logarithm, Gram square-root factor, Haar probability on the single original Z, scalar log-polynomial with circle zeros and inversion convention. Foundational proof-inspection limits retained. |
| dependency | [Scalar finite-section theorem](../audits/literature/Den09/Yin_U002.md#den09-u002) | Exact finite-section-determinant subsection, Theorem 2 for scalar bounded nonnegative abs(P)^2 with finite circle zeros. Fixed P only; original Sim05 proof remains uninspected, and no general noninvertible matrix approximation theorem is used. |
| dependency | [Full matrix trace and kernel convention](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Exact luc22-kernel-removed-determinant subsection: unnormalized matrix trace, kernel-removed agreement for these injective maps, finite group normalization abs(det)^(1/N) without rank division. |
| support | [Commutative scalar-return distinction](../audits/literature/Luc22/Yin_U002.md#luc22-u002) | Exact luc22-ore-determinant-interface subsection: same-ring commutative determinant versus quotient of scalar determinants; no general Ore theorem is required for the direct triangular calculation. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0295_v1.md#integer-shear-whole-independent-finding) | Actual complete 21:25 D28 and its direct interfaces only. This historical whole finding does not inspect the new statement/wrapper or adopt this extraction. |
| review | [Actual independent extraction](../audits/reviews/Yin_R_G0794_v2.md#c73-integer-shear-actual-extraction-finding) | Complete actual statement, ENTIRE original preservation and all exact direct/assembly interfaces inspected after allocation by a noncontributor. Original whole finding remains at its original scope. |
