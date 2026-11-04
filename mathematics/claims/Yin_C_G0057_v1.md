---
author: Yin
---
# Effective first-window energy deficit and height-independent indexed product windows

Date: 2026-10-12T10:33.
Human author Yin.
Internal fixed extraction under the unchanged G0001 continuation.
Root authored the complete original quantitative proof and dated tensor extension.
The present extracting AI independently whole-reviewed that original 18:27 extended D11 in R264 and NOW authors this new statement/wrapper; it is a contributor to this extraction and cannot independently review the new Claim.
The ENTIRE original author account follows, retaining its two freezes, extension, source resolution and original contribution history.
Initial status remains proof draft / under review pending a separate actual extraction review.

## Statement

Fix the ACTUAL monic irreducible minimal polynomial P in Z[t] of a nontorsion algebraic integer unit alpha, ORIGINAL degree d>=2, K=Q(alpha), ACTUAL O0=Z[alpha], original total logarithmic Mahler measure m(P)>0 and house H(P)=max_i|alpha_i|>1 over ALL original conjugates.
No reciprocity, coefficient-height bound, flatness, trace signature or unit-only residue inventory is imposed.

For every integer allowed window T>=0, let E_T^Q be the INFIMUM of weighted coefficient energy over finite rational-polynomial packets f_b in Q[t], deg f_b<=T, positive normalized RATIONAL weights omega_b, every actual value f_b(alpha) in O0 minus {0}, and EVERY aggregate lag sum omega_b sum_j f_(b,j)f_(b,j+l)=0 for 1<=l<=T.
The formal-real extension retains the SAME full integer remainder condition, rather than only a value at one embedding, and has the equal infimum E_T^R=E_T^Q=:E_T.
These are infima over actual finite packets, with no closure substitution or asserted optimizer.

Put the explicit constants

    Q=4d, N0=Q^d, rho_d=1/[16 Q^(2d)],
    B_d=ceil(2sqrt(d/rho_d)),
    N_d=(2B_d+1)^(d*d),
    delta_elem(d)=rho_d/(4d N_d)>0.

**A. Integer-floor conditioning and the exact first-window defect.**
For EVERY real positive-definite d-by-d matrix G with diagonal entries at most 1 and r^TGr>=1/2 for EVERY nonzero integer r, one has lambda_min(G)>rho_d.

In the ACTUAL first window T=d, let A=[a_0,...,a_d] be the full integer power-basis remainder matrix, with a_j=e_j for j<d, and let M be the actual integer companion for multiplication by alpha.
For each real symmetric POSITIVE DEFINITE Toeplitz (d+1)-by-(d+1) W with diagonal 1, put

    G=(A W^-1 A^T)^-1,
    mu=min_(0!=r in Z^d) r^T G r,
    epsilon=1-mu, K=W-A^TGA.

Then G>0, K>=0, 0<mu<=a_j^TGa_j<=1, diagG<=1 and every |K_ij|<=epsilon.
The SAME actual companion obeys

    (M^TGM-G)_ij=K_ij-K_(i+1,j+1), 0<=i,j<d,
    ||M^TGM-G||_op<=2d epsilon,
    M^TGM<=G+2d epsilon I.

When mu>=1/2, G>=rho_d I and for every integer n>=0,

    ||M^n||_2<=sqrt(d/rho_d)(1+2d epsilon/rho_d)^(n/2).

No eigenvector denominator bound, finite residue cutoff or coefficient-height factor is assumed.

**B. Elementary degree-only first-window deficit.**
Every rational W in the accepted C17 dual domain has mu(W)<1-delta_elem(d).
Its supremum therefore satisfies the WEAK bound

    E_d^Q=E_d^R<=1-delta_elem(d).

This is uniform over all coefficient heights at EACH fixed original degree d.
The explicit finite integer-matrix pigeonhole proof uses no house theorem or external geometry-of-numbers premise.
The bound is not asserted strict at the supremum and no rational maximizing W is asserted.

**C. Actual-house bound and separately optional accepted house sharpening.**
Define

    delta_H(P)=min{1/2, rho_d(H(P)^2-1)/(2d)}.

The actual-house argument, including complex eigenvectors and the separate mu<1/2 case, gives

    E_d<=1-delta_H(P),
    E_d<=1-max{delta_elem(d),delta_H(P)}.

The positivity H(P)>1 is locally justified by bounded integer companion powers and nontorsion.
This branch requires no new external lower-house theorem.

ONLY when invoking the additional already accepted Dim19 RETAINED 2019 v1 Theorem 1 statement at the precise Smy08-U001 interface, H(P)>=2^(1/(4d)) for noncyclotomic monic irreducible inputs of degree d>1, one also obtains

    delta_SZ(d)=rho_d log2/(4d*d)
               =log2/[64 d*d (4d)^(2d)],
    E_d<=1-delta_SZ(d).

Its acceptance is statement/applicability scope, not an independent review of Dimitrov's original proof, comparison with a later edition or fresh publication-status verification.
It is an OPTIONAL extra input and is not used for B.

**D. Actual finite midlevel packets and complete original arithmetic.**
For any positive deficit delta just proved above with E_d<=1-delta, there is an ACTUAL finite rational complementary packet with

    E<1-delta/2<1,
    allowed window [0,d], ACTUAL common union width exactly d.

No infimum attainer, explicit primal-coordinate algorithm, packet-size or height bound, or bound on the ACTUAL coefficient denominator q and FINAL indexed weight denominator M_w is supplied.
Write F_b=q f_b in Z[t], n_b=M_w omega_b in Z_(>0), sum_b n_b=M_w, and retain every FULL SIGNED original norm D_b=Norm_K(f_b(alpha)) in Z minus {0}.
Then

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(n_b)=q^(d M_w) product_b D_b^(n_b),
    sum_b omega_b ||F_b||_2^2=q^2 E,
    Lambda=(1/d)sum_b omega_b log|D_b|>=0,
    I=log q+Lambda,
    Lambda-(1/2)log E<=m(P).

Every original conjugate, numerator content, repeated label, positive copy and possible common monomial norm sign Norm_K(alpha)^ell is retained.
The same log q cancels only after both norm and energy costs are charged.
C17's lower bound and the new upper one give

    exp(-2m(P))<=E_d<=1-delta,
    m(P)>=-(1/2)log(1-delta)>=delta/2.

These remain degree/input-dependent statements.
The optional Dim19 premise already implies the stronger Mahler estimate m(P)>=log2/(4d); the present optional deduction concerns first-window CAPACITY and does not claim an improved number-theoretic Mahler bound.

**E. Exact full-indexed product construction.**
Take ANY actual finite rational complementary packet for this SAME alpha with 0<E<1, actual normalized common window [0,d] of width d, ACTUAL least coefficient denominator q, ACTUAL FINAL indexed weight denominator M, integer numerator polynomials F_i=q f_i, multiplicities m_i=M omega_i and full signed norms D_i.
For EVERY integer k>=1 keep ALL ordered tuples b=(b_1,...,b_k), without merging equal labels or values, and set

    f_b^(k)=product_(j=1)^k f_(b_j),
    omega_b^(k)=product_(j=1)^k omega_(b_j).

Every resulting value is a NONZERO integer in the SAME O0, and the exact finite Laurent identity is

    sum_b omega_b^(k) f_b^(k)(f_b^(k))*=E^k.

Every lag vanishes at ACTUAL common width EXACTLY kd.
The actual denominator and arithmetic identities are

    q_k=q^k, M_k=M^k,
    m_b^(k)=product_j m_(b_j),
    D_b^(k)=product_j D_(b_j),
    Lambda_k=k Lambda,
    F_b^(k)=product_j F_(b_j),
    Res(P,F_b^(k))=q^(k d) D_b^(k),
    product_b Res(P,F_b^(k))^(m_b^(k))
       =q^(k d M^k) [product_i D_i^(m_i)]^(k M^(k-1)),
    sum_b omega_b^(k)||F_b^(k)||_2^2=q^(2k) E^k,
    Lambda_k-(1/2)log(E^k)
       =k[Lambda-(1/2)log E]<=k m(P).

The field and norm degree are still the ORIGINAL d.
The exact denominator statements require this full indexed family; a representation with merged weights may have a different least weight denominator.
Different repeated labels may witness the left and right endpoints.
All contents, signs and q=M=1 or k=1 endpoints are retained; no assertion that product amplification improves surplus per unit window is made.

**F. Full finite-capacity transfer and a height-independent energy window.**
For all integers T,U>=0, on the SAME fixed input,

    E_(T+U)<=E_T E_U.

For EVERY integer T>=0 and ANY proved positive first-window deficit delta with E_d<=1-delta,

    E_T<=(1-delta)^floor(T/d).

At T<d this is the old exact value E_T=1.
These are infimum inequalities obtained from actual finite rational near-minimizers; no endpoint packet or optimizer is asserted.

For any rational 0<theta<1 choose the actual strict midlevel packet of D and set

    k=ceil(log(1/theta)/[-log(1-delta/2)])>=1.

Its actual indexed k-fold product has energy STRICTLY less than theta, actual width kd, exact q^k and M_w^k, and

    k<=ceil(2log(1/theta)/delta),
    T_actual<=d ceil(2log(1/theta)/delta).

Using delta_elem(d) supplies an entirely elementary degree-only energy-window bound independent of coefficient height.
Using delta_SZ(d) supplies its separate accepted-house-input sharpening.
Both window multipliers may grow rapidly with d; they do not supply an absolute constant times d, a degree-uniform deficit, uniformly bounded q/M, or unrestricted G0001 completion.
C18's fixed-input exponential rate and C23's different degree/height modulus remain unchanged.
For a specified overorder the same monogenic packets remain admissible, but its first possible window may be smaller; the exact first-window assertion belongs to O0.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T10:33 |
| status | open |
| reason | Register the precise elementary/actual-house/optional-house first-window statements and full indexed product/capacity/window extension while retaining the ENTIRE original 18:27 extended D11. R264 independently covers that original author body only. This new statement, complete-preservation operation and selected interfaces await another noncontributor review; the R264 reviewer now authors this wrapper and cannot supply its independent review. No optimizer, bounded primal denominator, degree-uniform gap or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | A--F above: actual original unit/order/degree, generic integer-floor estimate, rational-dual endpoint, three separately scoped deficit choices, actual finite midlevel packets, exact indexed products and full arithmetic/window limits. |
| argument | [Entire retained author account](#argument) | COMPLETE original D11 allocation/reuse/roles, unchanged 18:18 Sections 1--7/Lemma 1/Theorem 2/equations (1)--(15), original freeze, 18:24 Section 8/equations (16)--(21), 18:27 source resolution and extended freeze. |
| dependency | [C17 exact dual and first-window interface](Yin_C_G0017_v1.md#statement) | Exact rational Toeplitz supremum equals finite rational/formal-real energy infima, whole nonzero-integer domain, monogenic short-width boundary and lower original-root energy bound; no optimizer or finite cutoff. |
| dependency | [C17 actual companion interface](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) | Actual power-basis columns, companion multiplication, weighted quotient residual and width-d versus shorter monogenic boundary. |
| dependency | [C10 complete original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only actual complementary finite rational packets with nonzero full signed integer norms/resultants, same final weights/copies and physical common width; no reciprocal-only construction premise. |
| dependency | [Optional accepted house source unit](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | ONLY the unit's smy08-house subsection for delta_SZ and conclusions invoking it: retained 2019 v1 Dim19 Theorem 1, original d>1 noncyclotomic monic irreducible domain, statement/applicability acceptance without original proof or later-edition review. |
| support | [Original entire-author review](../audits/reviews/Yin_R_G0264_v1.md#effective-first-window-whole-finding) | Exact original 18:27 extended D11 body, including its original 18:18 proof, dated tensor extension and narrow source resolution. It does not inspect this new statement/wrapper or constitute current Claim adoption. Finding relationship: self-reviewed. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T10:47 |
| status | proved |
| reason | Adopt the independently performed whole extended-author finding and separate actual extraction/interface finding at their precise scopes. The entire original proof, tensor extension and source/contribution history remain. This supplies a height-independent but degree-dependent existence window, without a bounded primal dictionary or an unrestricted uniform gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | A--F above: actual original unit/order/degree, generic integer-floor estimate, rational-dual endpoint, three separately scoped deficit choices, actual finite midlevel packets, exact indexed products and full arithmetic/window limits. |
| argument | [Entire retained author account](#argument) | COMPLETE original D11 allocation/reuse/roles, unchanged 18:18 Sections 1--7/Lemma 1/Theorem 2/equations (1)--(15), original freeze, 18:24 Section 8/equations (16)--(21), 18:27 source resolution and extended freeze. |
| dependency | [C17 exact dual and first-window interface](Yin_C_G0017_v1.md#statement) | Exact rational Toeplitz supremum equals finite rational/formal-real energy infima, whole nonzero-integer domain, monogenic short-width boundary and lower original-root energy bound; no optimizer or finite cutoff. |
| dependency | [C17 actual companion interface](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) | Actual power-basis columns, companion multiplication, weighted quotient residual and width-d versus shorter monogenic boundary. |
| dependency | [C10 complete original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only actual complementary finite rational packets with nonzero full signed integer norms/resultants, same final weights/copies and physical common width; no reciprocal-only construction premise. |
| dependency | [Optional accepted house source unit](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | ONLY the unit's smy08-house subsection for delta_SZ and conclusions invoking it: retained 2019 v1 Dim19 Theorem 1, original d>1 noncyclotomic monic irreducible domain, statement/applicability acceptance without original proof or later-edition review. |
| support | [Original entire-author review](../audits/reviews/Yin_R_G0264_v1.md#effective-first-window-whole-finding) | Exact original 18:27 extended D11 body, including its original 18:18 proof, dated tensor extension and narrow source resolution. It does not inspect this new statement/wrapper or constitute current Claim adoption. Finding relationship: self-reviewed. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0266_v1.md#c57-effective-first-window-actual-extraction-finding) | Complete actual A--F, retained argument/preservation and exact current direct interfaces; checked by a noncontributor at the actual SELF relationship. |

## Registration and complete preservation

The complete source body follows.
Only the repeated author front matter is supplied once and the original first title is demoted one heading level.
All substantive prose, formulas, anchors, original role disclosures, historical statuses, author checks, source-access history, original 18:18 freeze and 18:27 extended freeze remain.
Existing relative links remain valid from this Claim directory and are retained.
A direct full-body comparison accompanies this extraction; no mere section summary substitutes for retained proof.

The [EPF26 ordinary attribution account](../audits/literature/EPF26/readme.md#dirichlet-simultaneous-selected-attribution) identifies the classical simultaneous Dirichlet method only.
It is not made a canonical project Review target or a new proof premise.
The optional Dim19 theorem remains the separately named accepted source statement.
The extractor's previous whole review of D11 does not independently review the wrapper written here.
The original D11 is left in place pending preservation, consumer maintenance and actual extraction review; this operation performs no retirement or adoption.

## Argument


## Effective first-window capacity deficit from approximate companion isometry

Date: 2026-10-12T10:14.
Human author Yin.
Root AUTHOR inquiry on the unrestricted G0001 mathematical objective.
Root supplies the substantive quantitative companion/conditioning candidate and cannot independently review it.
No native mathematical program or new external source is planned.
A new working address is allocated normally and inherits no earlier serial mathematics.

## Question and bounded reuse

The adopted [C17](Yin_C_G0017_v1.md#statement) proves exact dual completeness and E_d<1 for each actual original non-torsion integer unit, but leaves the first-window deficit nonquantitative.
Its entire first-window proof was read.
[C23](Yin_C_G0023_v1.md#statement) gives a different degree/height-dependent asymptotic capacity modulus at potentially enormous windows; its statement/relevant conditioning proof and a bounded current-Claim screen found no explicit first-window degree-only defect at the present interface.
No exhaustive novelty claim follows.

For T=d and each rational positive Toeplitz W with diagonal1, put G=(A W^-1 A^T)^-1, K=W-A^TGA, mu=min_nonzero_integer r^TGr and epsilon=1-mu.
C17 supplies these ACTUAL original-order interfaces, K>=0 and every monomial's quotient value between mu and1.
Candidate: every K entry has magnitude<=epsilon, so the companion defect M^TGM-G has operator norm<=2d epsilon.
A finite grid argument may quantify G's smallest eigenvalue whenever mu>=1/2 and diagG<=1.
Combine this with either the ACTUAL house or a finite integer-power pigeonhole argument to bound epsilon explicitly.
This supplies a degree-dependent first-window energy deficit, not a degree-uniform gap or an algorithm for the rational primal packet.

Test the safe constants Q=4d, rho_d=1/[16Q^(2d)], B_d=ceil(2sqrt(d/rho_d)), N_d=(2B_d+1)^(d*d), delta_d=rho_d/(4dN_d).
Integer-floor conditioning might give lambda_min(G)>rho_d; if epsilon<=delta_d, powers M^n for0<=n<=N_d remain bounded entrywise by B_d, hence two integer matrices coincide and non-torsion fails.
Separately the actual house H(P)>1 would force epsilon>=rho_d(H(P)^2-1)/(2d) in the mu>=1/2 branch.
All limits, strictness, nonreciprocal/signed unit cases, true lattice dimension and denominator/weight/full-norm costs require complete proof.
A sharper optional accepted house theorem will be considered only at its actual source scope and is not needed for the elementary route.

## Status

Developing author candidate; no theorem adoption, independent review or native run.
All substantive argument continues below in this responsible D.
Original q, FINAL M, physical support and nonzero actual integer residues are mandatory.
Fixed-degree quantitative loss tending to zero with unbounded d does not resolve the Task's uniform bottleneck.


<a id="effective-first-window-domain"></a>
## 1. Actual original order, complete dual and the proposed quantitative object

Fix the ACTUAL monic irreducible minimal polynomial P in Z[t] of a nontorsion algebraic integer unit alpha, original degree d>=2, and use O0=Z[alpha] with ordinary power basis1,...,alpha^(d-1).
Let A=[a_0,...,a_d] be the integer d-by-(d+1) matrix for1,...,alpha^d, so a_j=e_j for0<=j<d.
Every a_j is nonzero.
Let M be multiplication by alpha in this actual basis, so M is an invertible INTEGER companion matrix and M a_j=a_(j+1) for0<=j<d.
Denote the ACTUAL house by H(P)=max_i|alpha_i| and total original Mahler measure by m(P)>0.
Reciprocity, flat coefficients, a height bound, trace signature, unit-only targets and a chosen norm inventory are NOT assumed.

Use exactly C17's first-window finite-packet infimum E_d^Q=E_d^R and rational positive-Toeplitz supremum.
For each real symmetric POSITIVE DEFINITE Toeplitz (d+1)-by-(d+1) matrix W with diagonal1 define

    G=(A W^-1 A^T)^-1,
    mu=min_(0!=r in Z^d) r^T G r,
    K=W-A^T G A.                                     (1)

The algebra below works for real W as well; the transfer to primal packets uses only the actually accepted equality over RATIONAL W.
The weighted quotient identity gives G>0,K>=0, and every coordinate monomial is an allowed representative of its actual nonzero integer residue.
Therefore

    0<mu<=a_j^T G a_j<=1, 0<=j<=d,
    G_ii<=1, traceG<=d,
    epsilon=1-mu in[0,1).                           (2)

The lattice minimum exists because G>0; no finite shortlist is assumed.
The input W can be arbitrarily close to singular and need not maximize the supremum.
C17's selected proof/source acceptance is reused only at these exact interfaces.
Its original nonquantitative contradiction and C23's different large-window degree/height modulus remain unchanged.

<a id="effective-integer-floor-conditioning"></a>
## 2. A finite-grid quantitative integer-floor lemma

**Lemma1.**
Let G be a real positive-definite d-by-d matrix with each diagonal<=1 and r^TGr>=1/2 for EVERY nonzero r in Z^d.
Put

    Q=4d, N0=Q^d, rho_d=1/[16 Q^(2d)].               (3)

Then the smallest eigenvalue lambda_min(G)>rho_d.

*Proof.*
Since traceG<=d, lambda_max(G)<=d.
Suppose lambda_min(G)<=rho_d and choose a real Euclidean unit eigenvector v for that eigenvalue.
Consider the N0+1 fractional vectors of jv, j=0,...,N0, in[0,1)^d, divided into Q^d=N0 half-open cubes of side1/Q.
Two distinct points have fractional parts in the same cube.
Subtracting their integer and fractional parts gives some integer1<=k<=N0 and z in Z^d with

    ||kv-z||_infinity<1/Q,
    ||kv-z||_2<sqrt(d)/Q.

The vector z is nonzero: otherwise k=||kv||_2<sqrt(d)/Q<1.
The G-norm is a genuine norm, so its triangle inequality gives

    sqrt(z^TGz)
      <=k sqrt(lambda_min(G))
        +sqrt(lambda_max(G)) ||z-kv||_2
      <N0 sqrt(rho_d)+d/Q
       =1/4+1/4=1/2.

Thus z^TGz<1/4, contradicting the integer floor1/2.
This finite pigeonhole proof requires neither Minkowski's theorem, determinant estimates, an eigenvector denominator bound nor an algorithm for finding the lattice minimum.
Q,N0 and rho_d are explicit in d alone.
Strictness is harmless; every subsequent use may weaken it to G>=rho_d I.
This proves Lemma1.

The integer condition on ALL nonzero r is essential.
Positive definiteness and unit diagonal alone would allow arbitrarily poor conditioning.
In(1)--(2), Lemma1 applies whenever mu>=1/2, without choosing a bounded set of possible minimizers.

<a id="approximate-companion-isometry-defect"></a>
## 3. Exact companion defect from the same Toeplitz quotient

The diagonal entries of K satisfy0<=K_jj=1-a_j^TGa_j<=epsilon.
Because K>=0, its two-by-two minors give

    |K_ij|<=sqrt(K_ii K_jj)<=epsilon.               (4)

For0<=i,j<d, actual companion multiplication and the exact Toeplitz shift imply

    (M^TGM-G)_ij
       =a_(i+1)^TG a_(j+1)-a_i^TG a_j
       =K_ij-K_(i+1,j+1).

Consequently every entry of the real symmetric defect has magnitude<=2epsilon and its Euclidean operator norm is at most2d epsilon.
In particular,

    M^T G M <=G+2d epsilon I.                       (5)

One direct proof of the norm bound is |x^TDefect x|<=2epsilon (sum_i|x_i|)^2<=2d epsilon ||x||_2^2.
No coefficient-height factor is needed: the companion can have large entries, but the actual quotient/Toeplitz identity already accounts for them.

If mu>=1/2, Lemma1 gives G>=rho_d I.
Set

    t=2d epsilon/rho_d>=0.

Then (5) yields

    M^T G M <=(1+t)G,
    (M^n)^T G M^n <=(1+t)^n G,
    ||M^n||_2 <=sqrt(d/rho_d)(1+t)^(n/2)          (6)

for every integer n>=0.
Induction gives the middle inequality, and rho_d I<=G<=d I gives the last.
This is the SAME actual input and G as(1), not a changed form or selected embedding.

<a id="elementary-degree-only-capacity-deficit"></a>
## 4. Elementary degree-only first-window deficit

Define the explicit positive integers and rational constant

    B_d=ceil(2sqrt(d/rho_d)),
    N_d=(2B_d+1)^(d*d),
    delta_elem(d)=rho_d/(4d N_d).                    (7)

They depend ONLY on the ORIGINAL degree d.
In particular0<delta_elem<1/2.

**Theorem2 (elementary bound).** For every actual nontorsion integer-unit input of degree d,

    E_d^Q=E_d^R<=1-delta_elem(d).                    (8)

For every such input an ACTUAL finite rational complementary packet exists with every value nonzero in O0, positive normalized rational weights, every lag zero, ACTUAL common union width exactly d, and energy

    E<1-delta_elem(d)/2<1.                          (9)

No optimizer, explicit primal coordinates or bounds on their q, FINAL M or norms are asserted.

*Proof.*
For each rational W in C17's dual domain suppose epsilon<=delta_elem.
Then mu=1-epsilon>1/2, so(6) applies and Nt<=1/2 for N=N_d.
For any integer0<=n<=N,

    (1+t)^n<=sum_(k=0)^infinity (nt)^k
             =1/(1-nt)<=2.

Here binomial(n,k)<=n^k for0<=k<=n justifies the finite-to-geometric comparison; n0 is immediate.
Thus all matrix entries of M^n are bounded in absolute value by sqrt(2d/rho_d)<2sqrt(d/rho_d)<=B_d.
There are at most(2B_d+1)^(d*d)=N possible integer d-by-d matrices with that entry bound.
The N+1 matrices I,M,...,M^N therefore include a repetition M^a=M^b for0<=a<b<=N.
Since M is invertible over Q (indeed integral unit), M^(b-a)=I.
Applying to the actual coordinate of1 implies alpha^(b-a)=1, a contradiction.

Hence EVERY rational dual W has mu(W)<1-delta_elem.
Its supremum is at most1-delta_elem, not necessarily strictly below that endpoint.
C17's ACTUAL equality of the supremum with the finite rational and formal-real infima proves(8).
Since the right side is strictly below1-delta_elem/2, the definition of the RATIONAL finite-packet infimum supplies an actual packet with(9).
No closure point is declared realizable.
Its allowed window is[0,d]; C14/C17's original monogenic short-width theorem forces its actual union span to be exactly d.
The proof nowhere gives a finite enumeration of integer residues or a procedure for selecting that packet.
This proves Theorem2.

This explicit deficit is extremely small and tends to0 with d.
Its significance here is a quantitative first-window capacity statement uniform over coefficient heights at EACH degree.
It is not an input-uniform positive gap over unbounded degree, and its induced degree-dependent Mahler lower bound is not claimed to improve known number-theoretic bounds.

<a id="actual-house-capacity-deficit"></a>
## 5. Actual-house refinement and separately accepted house input

For an actual input define

    delta_H(P)=min{1/2, rho_d(H(P)^2-1)/(2d)}.         (10)

Here H(P)>1.
For completeness, if all original conjugate moduli were<=1, the unit norm would force all to equal1.
Characteristic-zero irreducibility makes them distinct, so the actual companion is diagonalizable over C with all eigenvalues on the circle.
Its powers are then bounded in Euclidean norm by the fixed diagonalization condition.
The finite integer-matrix argument gives a repeated power and torsion, a contradiction.
This is a local use of the same familiar integer-power mechanism, not a newly invoked external Kronecker variant.

For mu>=1/2, (5) applied to a complex eigenvector of M with eigenvalue of modulus H(P) gives

    H(P)^2<=1+2d epsilon/rho_d,
    epsilon>=rho_d(H(P)^2-1)/(2d).                  (11)

The real quadratic-form inequality extends to its Hermitian form by applying it to real and imaginary parts.
No real-eigenvalue assumption is made.
If mu<1/2 then epsilon>1/2.
Thus in EVERY case epsilon>=delta_H(P), so C17 again gives

    E_d<=1-delta_H(P),
    E_d<=1-max{delta_elem(d),delta_H(P)}.            (12)

The same finite rational midlevel argument as(9) applies with either positive delta.
This is an exact actual-house bound, with no current asymptotic/source theorem as a premise.

**Optional accepted house sharpening.**
The already adopted [Smy08-U001 house interface](../audits/literature/Smy08/Yin_U001.md#smy08-house) records Dim19's RETAINED2019v1 Theorem1 at statement/applicability scope:

    H(P)>=2^(1/(4d)), d>1,

for actual noncyclotomic monic irreducible integer polynomials.
Our actual nontorsion unit minimal P satisfies precisely that scope.
This draft neither re-proves Dimitrov's theorem, upgrades its proof-review depth, compares a later accepted edition nor makes a fresh publication-status assertion.
The existing accepted statement is an explicit extra input ONLY to this optional paragraph.

Using exp(x)>=1+x in(10)--(11) gives the positive degree-only constant

    delta_SZ(d)=rho_d log2/(4d*d)
               =log2/[64 d*d (4d)^(2d)]<1/2,
    E_d<=1-delta_SZ(d).                             (13)

Indeed H(P)^2-1>=log2/(2d), and both arguments of the minimum in(10) are at least delta_SZ.
This transfers the accepted house theorem into a quantitative CAPACITY upper bound.
It is much stronger than the elementary constant(7), but still decays with d and supplies no rational packet algorithm or q/M estimate.
A finite actual packet with E<1-delta_SZ/2 exists by the same infimum argument.
Its mathematical use is separate from Theorem2's entirely local proof.

<a id="effective-first-window-full-costs"></a>
## 6. Complete finite arithmetic and logical limits of the energy estimate

For EACH actual finite packet selected in(9) or its(12)/(13) analogues, let q be the ACTUAL least coefficient denominator and M_w the ACTUAL least denominator of its FINAL positive normalized weights omega_b.
Let m_b=M_w omega_b be the positive integer copies, F_b=q f_b integer numerators in the original allowed[0,d] window, and D_b=Norm_(Q(alpha)/Q)(f_b(alpha)) the complete SIGNED original-degree norms.
They are all nonzero integers.
Retain every content and repeated label.
If a different Laurent representation is first normalized by a common monomial, retain its actual original unit norm sign Norm(alpha)^ell in D_b; no sign is silently replaced by+1 in the general nonreciprocal domain.

At the exact constant covariance and ACTUAL width T=d,

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(m_b)=q^(dM_w) product_b D_b^(m_b),
    sum_b omega_b ||F_b||_2^2=q^2E,
    I=log q+Lambda, Lambda=(1/d)sum_b omega_b log|D_b|>=0,
    Lambda-(1/2)log E<=m(P).                        (14)

These are the exact accepted C10/C17 original-root costs; selecting a packet by the energy infimum has not removed its unknown norms, contents, copies or denominators.
There is no prespecified unit-only norm inventory, and neither q nor M_w is uniformly controlled.
Large q and M_w are compatible with the necessary C50/C28 conclusions in their respective exact domains; there is no uncancelled extra log q cost.

The lower infimum bound in C17 and the new upper bounds give

    exp(-2m(P))<=E_d<=1-delta,                       (15)

where delta may be delta_elem, delta_H or delta_SZ when its added premise is used.
Thus m(P)>=-(1/2)log(1-delta)>=delta/2.
This corollary is a degree/input-dependent bound.
The optional Dim19 premise itself already gives m(P)>=log2/(4d), which is far stronger as a Mahler bound than this particular delta_SZ/2; no new best degree-dependent number-theoretic estimate is claimed.
The new information is a positive explicit DEFICIT for the complete finite-packet energy at the FIRST window, not an improved external Mahler theorem.

For actual fixed d, (8) is height-independent.
Along any HYPOTHETICAL sequence m(P_j)->0, the original degree must grow and the constants in(7)/(13) can tend to0, consistently with E_(d_j)->1.
No hypothetical sequence has been produced.
Extending the existence to any specified overorder is immediate by using the SAME monogenic packet, but the exact first possible window need not remain d there; the stated equality of actual width concerns O0 only.

An inverse-bound mistake would be to treat(5) as making every positive Toeplitz form uniformly conditioned without the INTEGER minimum floor; Lemma1 uses that floor essentially.
Another would be to turn the strict pointwise dual inequality into an attained rational optimum; the proof only uses supremum/infimum and a strictly higher finite-packet energy level.
The present argument repairs neither of those nonexistent implications and claims neither of them.

<a id="effective-first-window-selfcheck-and-scope"></a>
## 7. Author self-check, source scope and outcome

The author checked every step on the actual d-dimensional power basis: all nonzero monomial residues including alpha^d; G>0 and quotient K>=0; mu<=1 and the real versus rational Toeplitz domains; integer-floor hypothesis, Q^d+1 grid points, nonzero approximating integer vector, norm constants and strict eigenvalue conclusion; EVERY K entry and exact Toeplitz shift indices0,...,d; the companion defect as K_ij-K_(i+1,j+1) with correct sign; real/Hermitian quadratic forms; finite iteration bound and n0; the N+1 versus N integer matrix pigeonhole, invertibility and actual torsion consequence; strict dual versus weak supremum bound; actual rational finite packet chosen above the infimum, not at its endpoint; true monogenic width and overorder exception.

The actual-house branch has its own exact positive input and a separately elementary justification H>1.
The optional Dim19 statement is explicitly named, uses the ORIGINAL minimal degree and retains its previously accepted statement-only proof depth and unchanged artifact edition.
No current source-status claim, new external theorem, approximation, finite numerical check, solver or native mathematical program occurs.
The C17 antecedent discloses root contributions and has its separate adopted independent review; this draft is a new author quantitative continuation, not a self-supplied independent audit of that antecedent or of itself.

Every finite denominator, FINAL weight, content, signed norm and actual support remains in(14).
The bound adds a degree-dependent quantitative first-window defect; it is still nonconstructive for primal coordinates and arbitrarily small across unbounded degrees.
C23's large-window coefficient-height construction remains a different interface, and no full-profile, scalar-width or original-law finite calculation is silently substituted.
No unresolved step was found in this author check.
A noncontributor must review the ENTIRE argument before adoption, and any actual fixed extraction needs its own review.


<a id="effective-first-window-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T10:18.
Freeze the complete initial question/reuse/source/contribution record, Sections1--7, Lemma1, Theorem2 and equations(1)--(15), all original-order/finite/strictness/optional-source/cost boundaries and author self-check for separate independent whole review.
Every substantive derivation was written directly in this responsible D and hand checked.
No native mathematical execution, new source intake, fixed Claim or self-supplied independent review is claimed.


<a id="first-window-tensor-capacity-transfer"></a>
## 8. Dated extension: actual indexed products and height-independent energy windows

Date: 2026-10-12T10:24.
The original18:18 Sections1--7 and their author freeze remain unchanged.
This additional local argument is a NEW extension requiring actual review together with that original proof; an earlier whole finding would not automatically cover it.
A bounded check of C16/C18/C23 found their finite-packet/rate definitions and input-dependent large-window bounds, but no registered version of this exact first-window degree-only consequence.
Finite multiplication of square identities is elementary; no novelty is claimed for that algebraic operation.

First take ANY actually supplied rational complementary packet for this SAME alpha, with finite indexed labels f_b, positive normalized rational weights omega_b, every field value a nonzero O0 integer, constant energy0<E<1 and common support normalized to[0,d] of ACTUAL width d.
Let its ACTUAL common coefficient denominator be q, its FINAL indexed weight denominator be M, its integer numerator polynomials F_b=qf_b, positive copies m_b=M omega_b and complete signed field norms D_b.
No labels are merged.
For each positive integer k and every ordered index tuple b=(b_1,...,b_k), define

    f_b^(k)(t)=product_(j=1)^k f_(b_j)(t),
    omega_b^(k)=product_(j=1)^k omega_(b_j).

These are finitely many labels with positive rational weights summing1.
Each evaluated value is a NONZERO integer in O0.
Multiplying the exact finite Laurent identities gives

    sum_b omega_b^(k) f_b^(k)(f_b^(k))*=E^k.           (16)

Thus EVERY lag cancels at the full common window, not just a selection of lags.
Some original label has nonzero constant coefficient and some has degree d, since the whole normalized union attains both endpoints.
Their k-fold repeated labels retain respectively nonzero constant coefficient and nonzero degree-kd leading coefficient; products have no endpoint cancellation.
All labels lie in[0,kd], so the ACTUAL common union width is EXACTLY kd.
This argument does not require one original coordinate to attain both endpoints.

For this FULL indexed tensor family, the ACTUAL denominator identities are stronger than safe divisibility bounds:

    q_k=q^k, M_k=M^k,
    m_b^(k)=product_j m_(b_j),
    D_b^(k)=product_j D_(b_j),
    Lambda_k=k Lambda,                              (17)

where Lambda=(1/d)sum_b omega_b log|D_b|.
To prove q_k=q^k, for each prime p dividing q the least-denominator property supplies an original F_b nonzero as a polynomial modulo p.
Its k-th power is nonzero in the integral domain F_p[t].
Hence some coefficient of this numerator is not divisible by p, so that label needs the full p-adic denominator exponent k*v_p(q).
Since every coefficient denominator divides q^k, equality follows prime by prime.
The case q1 is immediate.
Likewise, for every prime p|M, leastness of the indexed weight denominator gives an original m_b not divisible by p.
Its repeated tuple has numerator m_b^k coprime to p and requires the full exponent in M^k.
This proves the exact second equality, also at M1.
Merging identical labels could lower a different representation's weight denominator; it is explicitly NOT the present indexed construction.

All signed copies and contents are retained.
With Q_k=q^k and the actual integer numerator product F_b^(k)=product_jF_(b_j), one has

    Res(P,F_b^(k))=Q_k^d D_b^(k),
    product_b Res(P,F_b^(k))^(m_b^(k))
        =q^(k d M^k) [product_i D_i^(m_i)]^(k M^(k-1)),
    sum_b omega_b^(k)||F_b^(k)||_2^2=q^(2k)E^k,
    Lambda_k-(1/2)log(E^k)
        =k[Lambda-(1/2)log E]<=k m(P).              (18)

For the copied signed product, fix a position and index i.
Summing other tuple multiplicities contributes M^(k-1), so that D_i occurs to exponent k m_i M^(k-1).
This includes every sign even when the resulting total exponent happens to be even.
Coefficient content is never removed.
A pre-normalization monomial's actual unit norm sign propagates through these same products.
There is no claim that tensor amplification improves surplus per unit of window: equation(18) shows it preserves that normalized rate exactly.

For arbitrary finite allowed windows T,U the same two-packet argument gives the capacity inequality

    E_(T+U)<=E_T E_U.                               (19)

Indeed choose actual finite rational packets with energies arbitrarily close ABOVE the two infima, form their product family in allowed window[0,T+U], and pass through the real energy inequality.
Nonzero integral products stay nonzero integral.
No optimizer or closure-point realization is required.
Repeating with T=d, and using capacity monotonicity under adding unused allowed coefficients, gives for EVERY integer T>=0 and ANY proved positive first-window deficit delta with E_d<=1-delta,

    E_T<=(1-delta)^floor(T/d).                      (20)

When T<d, the exponent is0 and the old exact value1 applies.
The nontrivial bound is an infimum statement; it is not a claim that the endpoint energy is attained.
It uses the same fixed input and same O0 at every product, not independent fields, a powered minimal polynomial or a degree substitution.

To state an ACTUAL constant-energy window with no endpoint issue, take the actual packet from(9) (or its house/optional variants) with E<1-delta/2.
For any desired rational0<theta<1 put

    k=ceil(log(1/theta)/[-log(1-delta/2)]).

This is a positive finite integer.
The actual k-fold packet has E^k<=(1-delta/2)^k<=theta, in fact strict because the base E is strict, and ACTUAL width kd.
An explicitly coarser cap is

    k<=ceil(2log(1/theta)/delta),
    T_actual<=d ceil(2log(1/theta)/delta).            (21)

The inequality uses-log(1-delta/2)>=delta/2 and monotonicity of ceil.
Choosing delta_elem(d) gives a completely elementary degree-only energy window uniform over coefficient heights; choosing the accepted-input delta_SZ(d) gives a far smaller but still rapidly growing degree-only window.
For theta=3/4 this supplies a uniform constant ENERGY target at a width whose coefficient is a large function of d, not the required absolute C*d.
The actual q^k, M^k, label count and norm products can grow and are not bounded by this argument without the missing original-packet data.

The extension therefore improves the explicit height dependence of an existence window while preserving the true uniform bottleneck.
It does not replace C18's sharp fixed-input exponential rate or C23's different actual-input/height bounds, and it does not turn any hypothetical m->0 sequence into a contradiction at unbounded d.
Author check covered every indexed label, endpoint, prime denominator exponent, copy exponent, all-lag identity, infimum passage, k1 and q/M1 cases, actual support and the signed full norm charge.
This extension remains author work until independently inspected.


<a id="effective-first-window-dirichlet-attribution"></a>
## 9. Dated classical-method attribution resolution

2026-10-12T10:27.
The whole reviewer recognized Section2's box argument as the classical simultaneous Dirichlet pigeonhole method, already named in the project's [L133](../ledger/Yin_L_G0133_v1.md) at its old different phase-return use.
A bounded bibliography/source-unit screen did not find an exact registered attribution.
Root therefore checked primary teaching sources: the Claremont metadata for a2006 Fukshansky lecture was accessible but its linked PDF returned404, so no theorem from that inaccessible document is consumed.
The official EPFL DISOPT Lecture10 PDF was then acquired and its typed simultaneous Dirichlet statement on PDFpage8 was text-read and visually verified.
See [EPF26's exact selected account](../audits/literature/EPF26/readme.md#dirichlet-simultaneous-selected-attribution).
Institutional attribution and unknown individual author/date are explicit; its2026 key is an inspection-year convention.

The source is attribution only: it identifies the familiar common-denominator approximation statement.
Section2 already proves the exact finite INTEGER-Q box result locally, including strict residual, nonzero vector and all quantitative constants.
No source lattice/Minkowski theorem, proof-completeness assertion or algorithm is used, and none of Sections1--8 changes mathematically because of this source note.
The18:18 no-intake statements remain true for their original frozen time; this later intake and the18:24 tensor extension are now explicitly additional author scope.

<a id="effective-first-window-extended-author-freeze"></a>
## Complete extended author freeze

2026-10-12T10:27.
Freeze the ENTIRE actual D11: original allocation, unchanged18:18 Sections1--7/Lemma1/Theorem2/equations1--15 and original freeze,18:24 Section8/equations16--21 with complete indexed product/capacity/window/cost proof, and this exact source-resolution account.
Root remains the substantive author of all new mathematics and cannot independently review it.
The separately assigned whole reviewer must inspect the actual extension/source interfaces before publishing a finding for this extended scope; no earlier draft reading automatically includes it.
No native mathematical program or numerical experiment was run.
