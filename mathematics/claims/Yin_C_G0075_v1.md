---
author: Yin
---
# Exact inverse-boundary comparison for general same-scalar Laurent matrices

Date: 2026-10-12T14:20.
Human author Yin.
The original D30 mathematics is by g0001_matrix_recovery; root supplied the broad question only.
g0001_review_recovery independently whole-reviewed that actual original in R298 and now AUTHORS this fixed extraction wrapper.
That changed role does not invalidate the completed original review, but the wrapper requires a separate actual noncontributor review.
Initial registration is a proof draft under review, with no adoption or original-draft retirement.
The complete original body, source account, candidate and historical freeze follow.

## Statement

Fix the ACTUAL monic irreducible minimal polynomial P of a nontorsion algebraic integer unit alpha, ORIGINAL degree d>=2, K=Q(alpha), O0=Z[alpha], ALL original roots beta_1,...,beta_d, and total m=m(P)>0.
All scalar norms below retain these d embeddings, including repetitions after powering.
Let r>=1 and let A(t) be ANY r-by-r integer Laurent matrix satisfying

    det A(t)=epsilon t^b P(t), epsilon in{+1,-1}, b in Z.

No integral Smith form or supplied unimodular factorization is required.
Every supplied integral unimodular left/right equivalent realization is included, but no classification of all such matrices is asserted.

**A. Actual normalization and full trace.**
Let a and a+w be the minimum and maximum exponents across ALL nonzero entries.
Then Ahat=t^(-a)A is a polynomial matrix supported in[0,w], ell=b-r*a>=0 and ell+d<=r*w, hence w>=1.
This common OUTPUT monomial shift preserves every full open convolution Gram.
It does not shift input columns independently.
Large r may allow w<d.
On canonical Haar probability for Z and UNNORMALIZED Tr_r, all singular-value logarithms are integrable and

    log Delta(A(U))=integral sum_(i=1)^r log s_i(A(z))=m(P).

The finite circle zero set has Haar measure zero and kernel dimension zero.
Normalizing the matrix trace by r would instead give m(P)/r and change this contract.
No finite-section or periodic limit is a premise of this identity.

**B. Exact no-wrap completion and original signed norm.**
For ANY integer N>=1 and ANY integer W>=max(w,d), put M=N+W and h=rW.
Let C_M be the cyclic shift on1,t,...,t^(M-1), B_A=Ahat(C_M), and G_A=B_A^T B_A.
Fix one component/exponent ordering; I contains every component at exponents0,...,N-1, and J its complement at exponentsN,...,M-1.
Thus |I|=rN and |J|=h.
The full open convolution Gram H_A,N satisfies

    H_A,N=G_A[I,I],
    R_M=abs(Norm_(K/Q)(alpha^M-1)) in Z_(>0),
    det B_A=epsilon^M (-1)^(ell(M-1)+Md)
                         Norm_(K/Q)(alpha^M-1),
    det G_A=R_M^2.

All outputs lie in0,...,N+w-1, so this completion omits no coefficient and introduces no wraparound.
P has no root of unity and B_A is invertible.
Neither M nor d is replaced by a smaller powered-field degree.
With group trace Tr_M/M and UNNORMALIZED Tr_r the periodic logarithmic determinant is log R_M/M; the compatible open rate is log det H_A,N/(2N), without another factor1/r.

**C. Exact same-size boundary comparison.**
Define Q_A,N=(G_A^-1)[J,J], a positive definite h-by-h matrix.
For the SAME r,N,W,M,I,J form A0=diag(I_(r-1),P), B0=A0(C_M), G0=B0^T B0 and Q0,N=(G0^-1)[J,J].
Write

    D_N=det Gram(P,tP,...,t^(N-1)P)>0,
    chi_A,N=log det Q_A,N,
    b_A,N=log det Q_A,N-log det Q0,N.

Then the exact identities are

    det H_A,N=R_M^2 det Q_A,N,
    D_N=R_M^2 det Q0,N,
    det H_A,N/D_N=det Q_A,N/det Q0,N,
    log det H_A,N=log D_N+b_A,N.

The requirement W>=d pays for the baseline's full output even when w<d.
The boundary dimension is the actual h=rW, with no smaller efficient computation promised.
The raw chi need not be nonnegative; at P=t^2-3t+1, A=P, r1,N1,W2,M3, one has D_1=11, signed Norm(alpha^3-1)=-16 and det Q_A,1=11/256<1.
That fixed positive-measure control has relative b=0.
No sign theorem for relative b over the entire matrix class is asserted.
C73's nonnegative relative shear charge remains a special case, not a sign rule for raw chi.

**D. Complete coefficient, boundary and condition costs.**
Put B_P=sum_j abs(p_j), and let K_A and K_adj be the sums of absolute values of ALL coefficients of all entries of Ahat and of its actual polynomial adjugate, respectively.
For r1 the adjugate is[1].
These quantities are positive integers.
Put delta_M=min_(zeta^M=1)abs(P(zeta))>0.
Then

    ||B_A||<=K_A, ||B_A^-1||<=K_adj/delta_M,
    -2h log K_A<=chi_A,N<=2h log(K_adj/delta_M),
    -2h log(K_A B_P/delta_M)<=b_A,N
                         <=2h log(K_adj B_P/delta_M).

The baseline estimates use ||B0||<=B_P and ||B0^-1||<=B_P/delta_M.
Moreover

    delta_M>=R_M/B_P^(M-1)>=B_P^(-(M-1)),
    -2h[log K_A+M log B_P]<=b_A,N
                         <=2h[log K_adj+M log B_P].

Every coefficient, h, M and the conditioning from original circle roots is retained.
These finite bounds assert no favorable sign, periodic convergence, uniform small boundary, or interchange of limits.

**E. Exact finite integer numerator and compulsory denominator.**
Let E_J be the rM-by-h standard coordinate selector and let

    Z_A=adj(B_A)^T E_J, Z_0=adj(B0)^T E_J.

These are integer matrices of full column rank, using the adjugate of the ENTIRE finite matrix, distinct from the polynomial adjugate in D.
One has

    Q_A,N=Z_A^T Z_A/R_M^2,
    det H_A,N=det(Z_A^T Z_A)/R_M^(2(h-1)),
    R_M^(2(h-1)) divides det(Z_A^T Z_A),
    det H_A,N/D_N=det(Z_A^T Z_A)/det(Z_0^T Z_0).

Here h>=2.
The divisibility follows from the exact positive integer open Gram, and is not extra arithmetic income.
These finite exact constructions make no efficient complexity assertion.
Their complementary columns are not asserted to be a packet of nonzero original-order scalar values at alpha.

**F. Full payment in the inherited scalar lower certificate.**
With Delta_P=abs(disc P)>0 and the ACTUAL original trajectory length N+d, L4 gives

    m(P)>=[log Delta_P+log D_N-d log(N+d)]/[2(N+d-1)]
         =[log Delta_P+log det H_A,N-b_A,N
                                -d log(N+d)]/[2(N+d-1)].

Thus every relative open-Gram gain in THIS exact use is offset by its signed boundary difference, for every supplied A above and the SAME P,N.
An independently valid UPPER bound on b may be subtracted with all of its costs, producing a valid potentially weaker certificate.
The identity alone cannot improve the scalar quantity D_N.
This closes uncharged open-Gram replacement at this interface, including C73's fixed-width unbounded-height example.
It does not classify matrices, reduce every possible matrix inequality to L4, exclude additional scalar arithmetic input or sharper justified boundary estimates, construct a near-one family, or settle unrestricted G0001.

The block determinant/inverse identity used in C is classical and is also proved completely in the retained original.
Actual BV04 AppendixA.5.5 printed650--651/PDF664--665 supports precisely the real positive definite Schur scope.
BV04's canonical U001 concerns separation and is NOT extended or used as a Schur dependency.
Den09 and Luc22 retain only their accepted Fourier, spectral and full-trace convention scopes; no new source theorem is imported.

## Current assessment
[Selected decision](#decision-independent-current-whole-review-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T14:20 |
| status | open |
| reason | Register the complete exact original-polynomial inverse-boundary comparison, signed cyclic determinant, full coefficient/condition and finite-adjugate prices, and paid scalar certificate. Whole R298 covers only the actual original D30; this new author wrapper requires separate actual independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, original input and all roots, arbitrary actual r,N,W, full signs, cost bounds, exact baseline, finite divisibility and limitations. |
| argument | [Entire original body](#argument) | COMPLETE22:09 D30 allocation/candidate/reuse/source account, Sections1--7/equations1--16 and historical author freeze. |
| dependency | [Original scalar Gram certificate](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate) | Actual monic squarefree original P, N shifts, full trajectory N+d, discriminant and denominator; no reciprocity needed. |
| dependency | [Accepted Fourier convention](../audits/literature/Den09/Yin_U001.md#den09-u001) | Only the one-Z Fourier/spectral determinant convention, full Gram half-log and integrable scalar log zeros; foundational inspection limits remain. |
| dependency | [Accepted full matrix trace](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Only canonical full matrix trace and kernel convention on this zero-kernel input; no approximation theorem or new matrix inequality. |
| support | [Prior triangular shear interface](Yin_C_G0073_v1.md#statement) | Credited special relative nonnegative tail charge and fixed-width height counterexample; not a premise of the new general finite block proof. |
| support | [Original independent whole finding](../audits/reviews/Yin_R_G0298_v1.md#general-matrix-boundary-whole-independent-finding) | Actual complete22:09 original only, with actual BV04 selected source reading; does not independently review the new wrapper authored by that reviewer. |


### Decision current-scalar-gram-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:32 |
| status | proved |
| reason | Select C209#gram-lower-certificate as the current responsible home of the identical retained L4 scalar Gram argument and full-dimension certificate. Its actual current statement and original saturated-kernel, dual-Gram and Vandermonde/Hadamard passages were read at this existing interface. Mathematical status, selected statement/argument/review and every scope are inherited unchanged; this is current locator maintenance, not a new proof or independent review. The older decision and the selected review retain their actual original L4 inputs and dates. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, original input and all roots, arbitrary actual r,N,W, full signs, cost bounds, exact baseline, finite divisibility and limitations. |
| argument | [Entire original body](#argument) | COMPLETE22:09 D30 allocation/candidate/reuse/source account, Sections1--7/equations1--16 and historical author freeze. |
| dependency | [Original scalar Gram certificate](Yin_C_G0209_v1.md#gram-lower-certificate) | Actual monic squarefree original P, N shifts, full trajectory N+d, discriminant and denominator; no reciprocity needed. |
| dependency | [Accepted Fourier convention](../audits/literature/Den09/Yin_U001.md#den09-u001) | Only the one-Z Fourier/spectral determinant convention, full Gram half-log and integrable scalar log zeros; foundational inspection limits remain. |
| dependency | [Accepted full matrix trace](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Only canonical full matrix trace and kernel convention on this zero-kernel input; no approximation theorem or new matrix inequality. |
| support | [Prior triangular shear interface](Yin_C_G0073_v1.md#statement) | Credited special relative nonnegative tail charge and fixed-width height counterexample; not a premise of the new general finite block proof. |
| support | [Original independent whole finding](../audits/reviews/Yin_R_G0298_v1.md#general-matrix-boundary-whole-independent-finding) | Actual complete22:09 original only, with actual BV04 selected source reading; does not independently review the new wrapper authored by that reviewer. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0794_v2.md#c75-general-matrix-actual-extraction-finding) | Complete ACTUAL registered statement, entire preserved original and all exact interfaces separately checked after allocation by a noncontributor; earlier whole review retains its original scope. Referenced finding relationship: unknown. |


### Decision independent-current-whole-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:10 |
| status | proved |
| reason | The current finding is SELF because its initial complete argument input included author-validation conclusions beyond the necessary derivation. Adopt the separately organized current fixed-target finding after complete statement and retained-argument inspection, including late extensions, actual costs, controls, necessary mathematical interfaces and source limits, while excluding credited comparison scopes first separately checked after old-review exposure. The initial mathematical conclusion was formed at 2026-10-22T22:46 UTC before old-target review comparison. The finding records the exact interface and later credited-comparison reading sequence. Preserve fixed mathematics, historical decisions, all non-review premises and their scopes; retain earlier findings in their original homes at their actual recorded relationships and checking scopes. This selects current review evidence and supplies no new research, Task completion or execution resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement: statement](#statement) | Entire A--F, original input and all roots, arbitrary actual r,N,W, full signs, cost bounds, exact baseline, finite divisibility and limitations. |
| argument | [Argument: argument](#argument) | COMPLETE22:09 D30 allocation/candidate/reuse/source account, Sections1--7/equations1--16 and historical author freeze. |
| dependency | [Dependency: gram-lower-certificate](Yin_C_G0209_v1.md#gram-lower-certificate) | Actual monic squarefree original P, N shifts, full trajectory N+d, discriminant and denominator; no reciprocity needed. |
| dependency | [Dependency: den09-u001](../audits/literature/Den09/Yin_U001.md#den09-u001) | Only the one-Z Fourier/spectral determinant convention, full Gram half-log and integrable scalar log zeros; foundational inspection limits remain. |
| dependency | [Dependency: luc22-u001](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Only canonical full matrix trace and kernel convention on this zero-kernel input; no approximation theorem or new matrix inequality. |
| support | [Support: statement](Yin_C_G0073_v1.md#statement) | Credited special relative nonnegative tail charge and fixed-width height counterexample; not a premise of the new general finite block proof. |
| support | [Support: general-matrix-boundary-whole-independent-finding](../audits/reviews/Yin_R_G0298_v1.md#general-matrix-boundary-whole-independent-finding) | Actual complete22:09 original only, with actual BV04 selected source reading; does not independently review the new wrapper authored by that reviewer. |
| review | [Current SELF finding](../audits/reviews/Yin_R_G0794_v2.md#g75-current-independent) | Complete current mathematical statement and retained proof, including all late extensions, paid arithmetic, useful controls and accepted necessary interfaces at their exact scopes; exclude post-initial credited comparison scopes identified by the finding; initial conclusion 2026-10-22T22:46 UTC, then old-finding comparison; actual interface and credited-comparison reading limits are disclosed in the finding. |

## Registration and complete preservation

The [original D30 freeze](#general-matrix-boundary-entire-author-freeze) is retained in full below, with duplicate front matter represented once, its first title demoted one level, and line endings/terminal separating blank space normalized.
No original paragraph, formula, candidate, source history, author limitation or freeze is omitted.
All original relative claim/ledger/audit/PDF links have the same valid resolution from this sibling directory and are preserved.
The original source attribution is an ordinary reading account, not a false canonical BV04-U001 extension.
No draft retirement or actual wrapper review is performed by this author.

## Argument

## Exact inverse-boundary charges for general same-scalar Laurent matrix realizations

Date: 2026-10-12T14:00.
Human author Yin.
New AUTHOR inquiry by g0001_matrix_recovery under the continuing G0001 instruction.
Root supplied only the broad request to test a genuinely different same-original-P matrix boundary mechanism; this author selects the finite cyclic completion and inverse-boundary construction.
This author earlier wrote the C73 wrapper and independently whole-reviewed D29; neither role supplies independent review of the present new argument.
No native mathematical run or new source acquisition is authorized here.

## Responsible question and bounded reuse

The author read the actual C18 fixed-input capacity/FK statement, C23's degree/height convergence modulus, and the complete C73 integer-shear argument, originally read and copied during its wrapper contribution.
Their fixed-input limits, triangular Schur defect, height counterexample, periodic sign and full trace conventions are prior results, not the new question.
The actual L4 scalar Gram certificate, L56 rational mixed-minor projection cancellation and L241 sharp joint auxiliary ratio were inspected; they do not yet give an explicit finite inverse-corner formula for an arbitrary square Laurent realization of the SAME scalar P.

The proposed new scope is EVERY actual square integer Laurent matrix A with det A(t)=epsilon t^b P(t), not only matrices supplied with a unimodular equivalence to diag(I,P).
Common output monomial normalization, its exact determinant sign, rank/width and all original roots must remain explicit.
The author will not assume a Smith form over Z[t,t^-1] or classify all equivalences.

<a id="general-matrix-boundary-candidate"></a>
## Candidate before substantial proof

For N finite input coefficient positions, normalize the union support of A to [0,w].
Choose a cyclic size M=N+W with W>=max(w,d), so every full output coefficient is retained without wraparound.
The open convolution Gram should then be exactly a principal submatrix of the full periodic Gram.
Block elimination should express its determinant as the squared ORIGINAL cyclic norm times a complementary principal determinant of the inverse periodic Gram, of size rW for rank r.
The same construction for diag(I,P) uses the same cyclic norm and gives an exact ratio of two inverse-boundary determinants.

The intended payoff is a computable finite boundary charge for all gains relative to the inherited scalar Gram, with explicit adjugate/coefficient/small-singular-value costs and exact cancellation when inserted into the old scalar lower certificate.
A scalar control should distinguish the possibly negative raw inverse-boundary logarithm from C73's nonnegative triangular charge.
No gain is inferred from a normalized rank, changed cyclic exponent or fixed-input limit.
This is a candidate, not an accepted result; the full derivation, source attribution check, controls, failures and review boundaries will remain in this responsible draft.

A bounded local search by unimodular Laurent equivalence, finite compression, boundary rank, inverse principal minor and Schur determinant found the above interfaces.
A possible classical identification with the complementary principal-minor/Jacobi identity needs a precise source-attribution check; the finite block algebra can be supplied locally, but a local proof does not settle that source question.
No novelty claim or unverified source theorem is made.


<a id="general-matrix-boundary-source-resolution"></a>
## 1. Source resolution and the actual new finite interface

The named complementary-principal-minor identity is classical, not a new determinant identity.
A bounded internet screen located that identification; its search snippets are not proof evidence.
An adequate ALREADY REGISTERED source is [BV04](../literature/pdf/BV04.pdf), with [its existing Appendix A.5.5 reading](../audits/literature/BV04/readme.md).
The author actually text-read printed650--651/PDF664--665 and visually inspected printed650/PDF664 of the retained corrected2009 printing.
For a real symmetric block matrix with invertible first diagonal block, printed650 explicitly gives det X=det A det S and the lower-right inverse block S^-1.
Printed651 supplies the positive-definite Schur equivalence.
The project matrices below are real positive definite, so this exact source scope suffices.
Both formulas are also derived locally below; the source supplies classical attribution, not an unresolved premise, whole-book audit or new acquisition.
No earliest-attribution claim is made.

The new project content is the no-wrap original-polynomial cyclic completion, its full signed determinant, the same-size two-boundary comparison for arbitrary determinant-P matrices, and complete finite arithmetic/conditioning prices.
[C73](Yin_C_G0073_v1.md#statement) supplies a distinct smaller positive tail determinant for its special shear.
[C226 retained projection identity](Yin_C_G0226_v1.md#projection-cost-identity) and [L241](../ledger/Yin_L_G0241_v1.md#sharp-joint-auxiliary-determinant) optimize different actual-root auxiliary ratios.
These comparisons do not replace the finite derivation below.

<a id="general-matrix-full-scalar-normalization"></a>
## 2. All square integer Laurent realizations and the original determinant

Fix the ACTUAL monic irreducible nontorsion integer-unit polynomial P of original degree d>=2, alpha a root, K=Q(alpha), O0=Z[alpha], and ALL original roots beta_1,...,beta_d.
Put m=m(P)>0 and nu=Norm_K(alpha) in{+1,-1}.
Let r>=1 and let A(t) be an r-by-r matrix over Z[t,t^-1] with

    det A(t)=epsilon t^b P(t), epsilon in{+1,-1}, b in Z.    (1)

This includes any supplied A=L diag(I_(r-1),P) R with L,R invertible over Z[t,t^-1], whose actual determinants are signed monomials.
No claim that every A admits such an integral factorization is made or needed.
The given integer matrix and scalar identity(1), rather than an inferred Smith form, are the input.

Let a be the minimum exponent and a+w the maximum exponent among ALL nonzero entries of A.
Normalize the entire OUTPUT by one monomial:

    Ahat(t)=t^(-a) A(t)=sum_(j=0)^w A_j t^j,
    ell=b-r*a,
    det Ahat(t)=epsilon t^ell P(t).                         (2)

The polynomial determinant shows ell>=0 and ell+d<=r w; hence w>=1.
This common output shift preserves the full coefficient norm on both-sided sequences, so the full open-input Grams of A and Ahat are identical.
It is not an independent input-column normalization.
Original degree d remains, even if large r allows w<d.

At almost every circle point, A(z) is invertible and its r singular values have product abs(P(z)).
All positive logarithmic parts are bounded by the fixed matrix norm; integrability of log abs(P) bounds each negative part by this integrable function plus the other bounded positive parts.
Thus for canonical Haar probability on Z and UNNORMALIZED Tr_r,

    log Delta(A(U))=integral sum_(i=1)^r log s_i(A(z))
                  =m(P).                                  (3)

The finite circle zero set has zero Haar measure.
Kernel dimension is zero and the Den09/Luc22 conventions agree on this input.
The [accepted Fourier convention](../audits/literature/Den09/Yin_U001.md#group-fourier-convention) and [full matrix trace](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant) keep their inspection limits.
Dividing Tr_r by r would give m/r and change the question.
No finite-determinant limit proves(3).

<a id="general-matrix-no-wrap-cyclic-completion"></a>
## 3. A finite cyclic completion with no omitted output

Fix ANY integer N>=1 and put

    W=max(w,d), M=N+W, h=rW.                               (4)

Every larger chosen integer W also works, with its actual h charged.
Let E_N^r consist of vector polynomials supported on0,...,N-1.
Multiplication by Ahat has output support in0,...,N+w-1, contained in0,...,M-1.
Identifying these outputs with the M-cycle therefore introduces NO aliasing or wraparound.
Let C_M be the cyclic shift t on the basis1,t,...,t^(M-1), and set

    B_A=Ahat(C_M), G_A=B_A^T B_A.

Order the rM input coordinates by component and exponent in one fixed order.
Let I contain EVERY component at exponents0,...,N-1, and J contain exponentsN,...,M-1.
Hence |I|=rN, |J|=h.
The full open convolution Gram is EXACTLY

    H_A,N=G_A[I,I].                                       (5)

This column restriction gives the full open Gram because M retains all its outputs.
It is not the generally invalid replacement of an N-input full convolution by A(C_N).

Fourier diagonalization gives det B_A=product_(zeta^M=1)det Ahat(zeta).
No root of the actual P is torsion, so B_A is invertible.
Define

    R_M=abs(Norm_(K/Q)(alpha^M-1)) in Z_(>0).

The full SIGNED ordinary determinant is

    det B_A=epsilon^M (-1)^(ell(M-1)+Md)
                    Norm_(K/Q)(alpha^M-1),
    det G_A=R_M^2.                                       (6)

Indeed product_zeta zeta=(-1)^(M-1), and EACH ORIGINAL root satisfies product_(zeta^M=1)(zeta-beta_i)=(-1)^M(beta_i^M-1).
Multiplication over all d gives(6).
No smaller degree of alpha^M replaces d; repeated powered conjugates remain.
Under finite group trace Tr_M/M and UNNORMALIZED Tr_r, the logarithmic determinant is log R_M/M, without another1/r.
The compatible open finite rate is log det H_A,N/(2N), not division by2rN.

<a id="general-matrix-exact-inverse-boundary"></a>
## 4. Exact inverse-boundary identity and the SAME scalar Gram

Define the h-by-h positive definite boundary matrix

    Q_A,N=(G_A^-1)[J,J].

Then

    det H_A,N=R_M^2 det Q_A,N.                            (7)

Reorder I before J and write G_A=[[H,C],[C^T,D]].
Positive definiteness gives H>0 and S=D-C^T H^-1 C>0.
Triangular block elimination gives det G_A=det H det S.
Solving G_A(x,y)=(0,v) gives y=S^-1 v, so its inverse J block is S^-1.
Taking determinants proves(7).
This is the classical BV04 finite Schur mechanism at the exact checked scope.

For the SAME r,N,W,M, set

    A0(t)=diag(I_(r-1),P(t)),
    B0=A0(C_M), G0=B0^T B0, Q0,N=(G0^-1)[J,J].

W>=d ensures the same no-wrap property.
Its open Gram determinant is

    D_N=det Gram(P,tP,...,t^(N-1)P)>0,

because the other(r-1)N coordinates contribute identity blocks.
The baseline has the same cyclic absolute R_M.
Therefore

    D_N=R_M^2 det Q0,N,
    det H_A,N/D_N=det Q_A,N/det Q0,N.                      (8)

The COMPLETE relative boundary charge is consequently

    b_A,N=log det Q_A,N-log det Q0,N,
    log det H_A,N=log D_N+b_A,N.                          (9)

This gives an actual rW-dimensional inverse-boundary formula computable without first knowing the two open determinants.
It applies to every(1), including any given integral unimodular left/right equivalence, without triangularity or an inverse Laurent factorization.
Rank r, W, original P and cyclic M remain.
If rW is large, no smaller practical computation is promised.

The individual RAW charge chi_A,N=log det Q_A,N need not be nonnegative.
This differs from C73's nonnegative RELATIVE shear charge.
At rank1, P=t^2-3t+1, A=P, N1,W2,M3, one has D_1=11.
Since alpha+alpha^-1=3, alpha^3+alpha^-3=18 and Norm(alpha^3-1)=2-18=-16.
Thus

    det Q_A,1=11/256<1, chi_A,1=log(11/256)<0.             (10)

P is irreducible by discriminant5, monic unit and nontorsion.
This is a FIXED positive-measure control, not a near-one family.
Because A=A0, its RELATIVE charge is0.
No sign theorem for b_A,N on the whole matrix class is asserted.


<a id="general-matrix-boundary-condition-price"></a>
## 5. Explicit complete coefficient and condition costs

Let B_P=sum_(j=0)^d abs(p_j)>=1 and define

    K_A=sum_(i,j,l) abs([t^l]Ahat_ij),
    K_adj=sum_(i,j,l) abs([t^l](adj Ahat)_ij),
    delta_M=min_(zeta^M=1) abs(P(zeta))>0.                 (11)

The adjugate is the ACTUAL polynomial adjugate of Ahat; at r1 it is[1].
Both coefficient sums are positive integers.
At every circle point, the operator norm is at most the full entrywise coefficient sum.
Cyclic Fourier diagonalization and the polynomial adjugate identity imply

    ||B_A||<=K_A, ||B_A^-1||<=K_adj/delta_M.

The signed monomial factor in det Ahat has modulus1.
G_A^-1 therefore has eigenvalues in[K_A^-2,(K_adj/delta_M)^2].
Restricting its quadratic form to J preserves these bounds.
Multiplication of its h positive eigenvalues yields

    -2h log K_A<=chi_A,N
                  <=2h log(K_adj/delta_M).                (12)

For the baseline, ||B0||<=B_P and ||B0^-1||<=B_P/delta_M, including r1.
Since delta_M<=B_P and B_P>=1, this covers both its identity coordinates and scalar inverse.
Subtracting the baseline bounds from(12) gives

    -2h log(K_A B_P/delta_M)<=b_A,N
                    <=2h log(K_adj B_P/delta_M).           (13)

Every matrix coefficient, condition delta_M and boundary dimension h=rW remains in this finite price.
Degree-linear N, fixed matrix rank or scalar determinant P alone does not make b_A,N small, give it a favorable sign, or turn H_A,N into a lower Mahler certificate.

A fully integer but coarse estimate is also available.
Every abs(P(zeta))<=B_P and their product is the nonzero integer R_M.
Hence

    delta_M>=R_M/B_P^(M-1)>=B_P^(-(M-1)).

It follows that

    -2h[log K_A+M log B_P]<=b_A,N
                       <=2h[log K_adj+M log B_P].          (14)

No root approximation, Baker estimate or numerical calculation is used.
Deterioration with M, height and h is retained.
The exact delta_M includes the conditioning from all original circle roots near roots of unity; none are discarded.
No periodic convergence or interchange of limits is inferred.

<a id="general-matrix-exact-integer-boundary-numerator"></a>
## 6. Exact integer numerator and forced determinant cancellation

Let E_J be the rM-by-h standard coordinate selector and form the ordinary integer adjugate of the ENTIRE finite matrix B_A:

    Z_A=adj(B_A)^T E_J in Z^(rM by h).

Since B_A^-T E_J=Z_A/det B_A, the boundary matrix is Q_A,N=Z_A^T Z_A/R_M^2.
Its h columns are independent and det(Z_A^T Z_A) is a positive integer.
Equations(7)--(8) now give

    det H_A,N=det(Z_A^T Z_A)/R_M^(2(h-1)),
    R_M^(2(h-1)) divides det(Z_A^T Z_A),
    det H_A,N/D_N=det(Z_A^T Z_A)/det(Z_0^T Z_0).            (15)

The divisibility follows from the exact identity and actual positive INTEGER open Gram determinant.
It is not an additional arithmetic-income source.
In this domain h=rW>=2, so no empty block or negative exponent is needed.
These are finite exact integer/rational constructions for supplied A,N, with no efficient complexity bound or native implementation asserted.

The large adjugate numerator cannot be retained as free income while deleting its exact R_M denominator.
The scalar baseline has the same denominator and comparison window.
Every complementary column, actual scalar cyclic norm and matrix size is present.
Z_A is not a packet of nonzero original-order scalar values at alpha, and(15) makes no such conversion.

<a id="general-matrix-paid-original-certificate"></a>
## 7. Complete paid recovery and the remaining quantitative question

The [L4 scalar relation/orbit certificate](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate), with Delta_P=abs(disc P)>0 and actual trajectory length N+d, is

    m(P)>=[log Delta_P+log D_N-d log(N+d)]/[2(N+d-1)].

Characteristic-zero irreducibility gives squarefreeness.
Substitution of(9) gives for EVERY matrix in(1)

    m(P)>=[log Delta_P+log det H_A,N-b_A,N
                         -d log(N+d)]/[2(N+d-1)].          (16)

This is IDENTICALLY the same certificate for the same P,N.
Every positive relative open-Gram gain in this exact use is offset by its explicit inverse-boundary difference.
The free-replacement proposal is thereby closed for ALL same-scalar integer Laurent matrices at this interface, beyond C73's triangular shears.
The already proved C73 fixed-width unbounded-height family is included and shows why uncharged replacement can fail arbitrarily badly; it remains credited prior mathematics.

This does not reduce every possible matrix bound to L4.
A genuinely different inequality or additional arithmetic control of the explicit boundary ratio remains a possible changed mechanism.
An UPPER bound on b_A,N can be subtracted in(16) only with its correct sign and all costs; (14) generally removes the apparent gain.
The exact identity alone cannot establish a better lower certificate than the existing scalar quantity D_N.

The next question is consequently a sharper, separately justified estimate coupling this actual boundary ratio to a genuine original scalar arithmetic input on a specified family.
Merely exhibiting a large open Gram, small displayed matrix, integer adjugate numerator or fixed-input determinant limit does not supply it.
No favorable delta_M bound, near-one family, new arithmetic-income theorem or unrestricted G0001 conclusion is asserted.


<a id="general-matrix-boundary-entire-author-freeze"></a>
## Entire author freeze and review obligations

2026-10-12T14:09.
Freeze the ENTIRE allocation/candidate/reuse account and Sections1--7/equations1--16.
The g0001_matrix_recovery author supplied the cyclic completion, exact inverse-boundary comparison, complete condition/adjugate prices and finite scalar-certificate interpretation.
Root supplied only the broad new-matrix question.
A different noncontributor must actually whole-review this complete body before a fixed extraction or adoption.
This author's earlier C73 wrapper and D29 independent review do not supply such evidence.

Author checking reconstructed the common OUTPUT monomial and ell>=0; all r singular logarithms and unnormalized trace; full no-wrap support at M=N+W with BOTH w and d charged; component/exponent selectors and their dimensions; epsilon^M and both cyclic sign exponents using ALL d roots; the exact positive block Schur inverse; SAME r,N,W,M baseline and D_N identity; the distinction between raw chi and relative b with the exact scalar11/256 control; polynomial-adjugate versus finite-adjugate roles; spectral bounds on the full inverse and its principal block; the nonzero integer resultant lower bound for delta_M; all powers of R_M in the boundary numerator and required divisibility; and the original N+d, discriminant and denominator in L4.
These are author checks, not independent acceptance.

The bounded structural command checked this draft with C73, L4, L56, L241 and the actual Den09/Luc22 convention units, with checked7.
The draft's authored text is ASCII; all sixteen displayed formula labels are present.
The BV04 selected original pages were actually text-read and one was visually checked as described in Section1; the creator's disposable render directory was removed.
No mathematical native program, new acquisition, Claim selection or draft retirement occurred.

No fixed-input limit, matrix rank normalization or finite scalar control is promoted to an unrestricted G0001 result.

## Historical assessments

<a id="decision-organized-reviewed"></a>

### Historical assessment organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T14:31 |
| status | proved |
| review-status | independently reviewed |
| reason | Adopt original whole R298 and separate actual extraction R403. The general same-original-scalar Laurent matrix inverse-boundary identity, full signed cyclic norm, actual conditioning/adjugate costs and paid scalar certificate are fixed. Every root, rank, width and source limit remains. No favorable boundary, new arithmetic income or unrestricted gap is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, original input and all roots, arbitrary actual r,N,W, full signs, cost bounds, exact baseline, finite divisibility and limitations. |
| argument | [Entire original body](#argument) | COMPLETE22:09 D30 allocation/candidate/reuse/source account, Sections1--7/equations1--16 and historical author freeze. |
| dependency | [Original scalar Gram certificate](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate) | Actual monic squarefree original P, N shifts, full trajectory N+d, discriminant and denominator; no reciprocity needed. |
| dependency | [Accepted Fourier convention](../audits/literature/Den09/Yin_U001.md#den09-u001) | Only the one-Z Fourier/spectral determinant convention, full Gram half-log and integrable scalar log zeros; foundational inspection limits remain. |
| dependency | [Accepted full matrix trace](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Only canonical full matrix trace and kernel convention on this zero-kernel input; no approximation theorem or new matrix inequality. |
| support | [Prior triangular shear interface](Yin_C_G0073_v1.md#statement) | Credited special relative nonnegative tail charge and fixed-width height counterexample; not a premise of the new general finite block proof. |
| support | [Original independent whole finding](../audits/reviews/Yin_R_G0298_v1.md#general-matrix-boundary-whole-independent-finding) | Actual complete22:09 original only, with actual BV04 selected source reading; does not independently review the new wrapper authored by that reviewer. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0794_v2.md#c75-general-matrix-actual-extraction-finding) | Complete ACTUAL registered statement, entire preserved original and all exact interfaces separately checked after allocation by a noncontributor; earlier whole review retains its original scope. Referenced finding relationship: unknown. |
