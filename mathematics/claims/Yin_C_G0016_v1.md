---
author: Yin
---

# Exact integer residue moments and Toeplitz certificates for complementary energy

Date: 2026-10-11T18:18.
Human author: Yin.
Provenance: project deduction, with classical terminology attributed at its checked source scope.
Internal reusable-result organization under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Root supplied the conceptual integer-moment/Gram and complete weighted-Toeplitz quotient candidate; the responsible author supplied the realization, density and sharp control.
Complete contribution and review boundaries follow below.
No manuscript main-theorem designation or objective change is made.

## Statement

Let P be the ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, degree d>=2.
Fix the ALLOWED common coefficient window [0,T], N=T+1, initially O_0=Z[alpha].
Let A be the integer d-by-N power-basis remainder matrix.
Admissible rational coordinates f have ACTUAL NONZERO integral residues Af in Z^d minus{0}.
For a finite positive normalized rational-weight packet put X=sum_b omega_b f_b f_b^T.
Exact constant Laurent covariance additionally requires L_h(X)=sum_(j=0)^(T-h)X_(j,j+h)=0 for every1<=h<=T, and its energy is E=Tr X>0.
Let

    C_Z=conv{r r^T: r in Z^d minus{0}},

where conv is the FINITE convex hull, with no closure or zero atom.

**A. Exact finite-moment realization.** A RATIONAL symmetric X is the coefficient second-moment matrix of a finite rational weighted packet with every residue nonzero and integral if and only if X>=0 and A X A^T belongs to C_Z.
This equivalence concerns weighted packets BEFORE imposing lag cancellation.
To realize a complementary packet, impose ALL equations L_h(X)=0 as well.
The construction remains within the original allowed window; it does not assert that every realization has minimal support width exactly T.
The same statement holds with real X/coefficients/weights and the same formal integer residue condition.
PSD and a residue-trace lower bound alone do not replace membership in C_Z.

**B. Rational and formal-real energy infima.** Define E_T^Q as the infimum of Tr X over the rational feasible matrices in A WITH all lag equations, and E_T^R using real matrices/coefficients/weights but STILL requiring Af_b in Z^d minus{0} formally in the extended quotient, not only a value at one real embedding.
Then 0<E_T^Q=E_T^R<=1.
In O_0 and T<d both equal1 and are attained.
In general neither an optimizer, rational optimizer, closed-hull substitution nor a finite residue cutoff is asserted.

**C. Whole-lattice Toeplitz lower certificates.** If T>=d-1 and W is any rational symmetric POSITIVE DEFINITE Toeplitz N-by-N matrix with diagonal1, put

    G_W=(A W^-1 A^T)^-1,
    mu(W)=min_(0!=r in Z^d)r^T G_W r.

Then E>=mu(W)>0 for every allowed exact complementary packet, regardless of the chosen representative in each residue fiber.
Thus Gamma_T=sup_W mu(W)<=E_T^Q=E_T^R.
Equality at a specified W forces every residue to be a shortest lattice vector and every coordinate to be its W-least-norm representative, plus the exact lag conditions.
No general equality Gamma_T=E_T or maximizing W is asserted.
The kernel error is paid, rather than silently replacing representatives by Euclidean projections.

**D. Exact input control and all equality bundles.** For P=t^2-4t+1, O_0=Z[alpha], T=2, the displayed rational W gives

    f^T W f=[m^2+(n+2m)^2]/5+(4/5)y^2,
    (m,n)=(x-z,y+4z), f=x+y t+z t^2.

Consequently Gamma_2=E_2^Q=E_2^R=1/5, attained by f_1=(1+t^2)/4 and f_2=(1-t^2)/2 at weights4/5,1/5.
ALL minimizers in this allowed window consist of signed copies of these two coordinates with those total masses, allowing positive splits.
The COMPLETE Euclidean residue-lattice minimum is only1/9, and its shortest representatives have strictly positive lag-two correlation.
The two-label attainer has actual q4,M5, contents1,2, full numerator resultants+16,-48, integer energy16/5 and copied signed product4^10*(-3); splitting may increase the least weight denominator, while q and weighted energy/income remain as stated.

**E. Actual overorders and full costs.** A--C extend to a specified full order O containing alpha and alpha^-1 by using an actual integral basis and the actual integer coordinate matrix A_O; use its real/rational range at short windows and full row rank when T>=d-1.
The short-window value1 is specific to O_0 and is not asserted for arbitrary overorders.
In every rational realization the full signed resultants, scalar and final-weight denominators, contents, original-degree monomial norm factors and coefficient window charges are exactly those in the retained proof.
In particular the moment hull alone does NOT determine the nonlinear norm income: the same second moment can have different residue norm products.
No input-uniform Lehmer bound or general strong-duality theorem follows.

## Current assessment
[Selected decision](#decision-current-complete-isolated-adoption)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-11T18:18 |
| status | open |
| reason | Retain the exact finite-moment, rational-infimum, whole-lattice certificate and sharp-control statements with their complete frozen author argument. Separate whole and actual C extraction/interface review remains pending; fixed retention and author checking do not themselves adopt the result. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only A--E, with finite nonzero integer atoms, lag equations separately imposed, specified allowed window, and no generic attainment or dual-completeness claim. |
| argument | [Argument](#argument) | Complete frozen Sections1--9, Theorem1, Propositions2--3, equations1--19, exact singular/noise/density proofs, control/equality/norm accounting and all limits. |
| dependency | [Short-window actual integer coordinates](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | Unique monogenic integer coordinates and the exact short-window endpoint; no inference that a norm floor replaces actual order membership. |
| dependency | [Direct generic-monic window inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Full finite Poisson/reversal/log proof with all original nonzero resultants and the actual common window; this subsection does not impose reciprocity on the present generic monic input. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-11T18:25 |
| status | proved |
| reason | Adopt the completed separate noncontributor finding for this exact registered scope and selected fixed argument. Complete original histories, current repairs, source inspection limits and all costs remain; no uniform efficiency, unrestricted gap or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only A--E, with finite nonzero integer atoms, lag equations separately imposed, specified allowed window, and no generic attainment or dual-completeness claim. |
| argument | [Argument](#argument) | Complete frozen Sections1--9, Theorem1, Propositions2--3, equations1--19, exact singular/noise/density proofs, control/equality/norm accounting and all limits. |
| dependency | [Dependency](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | Unique monogenic integer coordinates and the exact short-window endpoint; no inference that a norm floor replaces actual order membership. |
| dependency | [Dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Full finite Poisson/reversal/log proof with all original nonzero resultants and the actual common window; this subsection does not impose reciprocity on the present generic monic input. |
| review | [Original R741 finding retained](../audits/reviews/Yin_R_G0741_v1.md#c16-integer-moment-extraction-finding) | Exact registered statement, selected complete argument, changed interfaces and dependencies in this physical version; preserved original reviews are not silently expanded. |


### Decision current-complete-isolated-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:51 |
| status | proved |
| reason | Adopt the exact complete current Statement and Argument with R741's actual separately assigned isolated whole finding. The new review covers every domain, proof step, selected interface, equality/control and original arithmetic cost, with no theorem repair or expanded source/native scope. The earlier R301 UNKNOWN and current R883 SELF remain at their actual dates and relationships; no original context or coverage is backfilled, and no general dual-completeness, optimizer or uniform-gap conclusion is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Only A--E, with finite nonzero integer atoms, lag equations separately imposed, specified allowed window, and no generic attainment or dual-completeness claim. |
| argument | [Exact retained argument](#argument) | Complete frozen Sections1--9, Theorem1, Propositions2--3, equations1--19, exact singular/noise/density proofs, control/equality/norm accounting and all limits. |
| dependency | [Exact retained dependency](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | Unique monogenic integer coordinates and the exact short-window endpoint; no inference that a norm floor replaces actual order membership. |
| dependency | [Exact retained dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Full finite Poisson/reversal/log proof with all original nonzero resultants and the actual common window; this subsection does not impose reciprocity on the present generic monic input. |
| review | [Complete current isolated finding](../audits/reviews/Yin_R_G0741_v1.md#current-c16-complete-isolated-independent-finding) | Entire current Statement A--E and complete Argument Sections1--9, Theorem1/Propositions2--3/equations1--19, all directly used C14/C10 interfaces, singular realization/density/full-lattice/control/overorder/norm costs and every unresolved boundary; initial complete judgment precedes old R301/R883 comparison at actual2026-10-22T18:40. |

## Argument

The whole frozen D11 account follows unchanged apart from first-title depth and final whitespace.
Its Theorem1 uses weighted packets before cancellation; its consequent equation(5) imposes all lag equations for complementary energy.
The construction preserves the allowed window, with no claim that minimal actual union width is always T.
Every actual proof step is retained here, including rational singular range inversion and nonzero-residue noise; historical L references remain ancestry/comparisons rather than missing current proof homes.
The exact selected C inputs above supply reused current interfaces.

Classical arithmetic-minimum/trace/threshold language is separately attributed in [Sch09-U001](../audits/literature/Sch09/Yin_U001.md#sch09-u001).
Root acquired and checked the exact v1 PDF after the author's earlier HTML-only inspection and failed fetch.
No source theorem on local finiteness, perfect forms, minimax, closure or general dual completeness is a premise of this proof.

## Integer residue moments and exact finite-window complementary energy

Date: 2026-10-12.
Authored by the paraunitary researcher AI for Yin under root-coordinated continuing G0001 authorization.
This distinct draft was allocated before substantive derivation.
Root supplied the conceptual Gram/residue-moment suggestion and then the complete positive Toeplitz weighted-quotient certificate; both are substantive contributions.
The author derived the exact finite-moment realization, rational/formal-real infimum comparison, explicit sharp quadratic control and its equality classification.
No native mathematical program, scan, solver or new J was run.
The author is not this work's independent reviewer.

<a id="integer-moment-reuse-and-source"></a>
## 1. Exact reuse and the changed problem

The complete relevant [L237 projection and norm account](../ledger/Yin_L_G0237_v1.md#monomial-projection-uniform-margin), [L318 exact complementary inequality](Yin_C_G0600_v1.md#weighted-integral-bundle-bound), [L345 integral coordinate interface](../ledger/Yin_L_G0345_v1.md#signed-power-classification-proof) and [L355 finite norm-one comparison](../ledger/Yin_L_G0355_v1.md#unit-capped-exact-normalization) were read.
L355 already proves weak duality over all REAL weights on each selected finite family, with its exact rational certificates and unsuccessful last certificate distinguished.
It does not optimize over all residue vectors or all representatives.

Most directly, [L341](../ledger/Yin_L_G0341_v1.md#all-lattice-old-dual-criterion) ALREADY pulls the old fixed residual-direction dual back to a quadratic form on every nonzero integer residue, and identifies a complete lattice-minimum obligation.
Its whole residue basis, rational Schur witness and positive-definite-versus-lattice-minimum distinction are reused.
Merely naming an integer quadratic-form certificate would repeat that mechanism.
Here EVERY rational representative in every nonzero residue fiber is admissible, and the aggregate autocorrelations must vanish EXACTLY.
Replacing all representatives by their Euclidean least-norm projections can destroy that condition.

The selected [L241 determinant optimization](../ledger/Yin_L_G0241_v1.md#sharp-joint-auxiliary-determinant) already proves that the entire optimized joint root-evaluation determinant is the old orbit Gram quantity.
[L288 capacity](../ledger/Yin_L_G0288_v1.md#whole-capacity-fiber-working) concerns a homogeneous anti-reciprocal norm/energy supremum with rational approximation, not this discrete residue-moment constraint.
The actual normalizer/cokernel distinctions in [L300](../ledger/Yin_L_G0300_v1.md#primitive-column-cokernel-order) and [L363](../ledger/Yin_L_G0363_v1.md#cokernel-denominator-identity) were read: a particular denominator is not the whole determinant or group cardinality.
None of those costs disappears here.

Current C9--C14 statements were screened.
Their field-profile existence, structural lifting, cyclic restriction and fixed inventories give no fixed-window minimum over this entire integral-value class.
The exact [C14 v2](Yin_C_G0014_v2.md#statement), including nonzero values and its one-way content condition, supplies the short-window and minimum-integer-energy boundaries.
Its q=2,S=2 classification does not minimize normalized E when q varies.

A bounded primary-source check recognizes the classical lattice-form language: Achill Schuermann, [Enumerating perfect forms, arXiv:0901.1587v1](https://arxiv.org/html/0901.1587v1), Sections 1--3, especially arithmetic minimum (2) and the rank-one halfspace description (9)--(10).
The primary full HTML was read; the PDF fetch failed.
This is attribution for the lattice minimum/Ryshkov formulation.
No local-finiteness, perfect-form enumeration, minimax, closure or strong-duality theorem is imported.
The source is not asserted to prove the interpolation result below.
All required algebra is reconstructed locally.
This author performs no source intake or novelty claim.

An initial Windows wildcard-path search failed and yielded no mathematical evidence; corrected directory/glob searches supplied the bounded reuse screen.
The screen is not exhaustive priority research.

<a id="integer-moment-domain-and-energy"></a>
## 2. Actual residue coordinates, energy infima and exact moments

Let P in Z[t] be the ACTUAL monic irreducible minimal polynomial of a nontorsion integer unit alpha, degree d>=2, constant coefficient +/-1.
Put K=Q(alpha) and initially O_0=Z[alpha].
Fix one common coefficient window [0,T], N=T+1, T>=0.
A common Laurent shift into that window preserves O_0 and nonzero values because alpha and alpha^-1 belong to O_0.
Reciprocity is not required.

Let A=A_T be the d-by-N INTEGER matrix whose column j is the coefficient vector of t^j mod P in 1,alpha,...,alpha^(d-1).
Monicity gives the integer remainders; minimality gives uniqueness.
Its first min(d,N) columns are the corresponding coordinate columns.
Hence its rank is min(d,N), and it has full row rank when T>=d-1.
For rational coefficients f in Q^N,

    r=A f in Z^d minus{0}
      iff f(alpha) is a nonzero actual O_0 element.       (1)

The coefficient polynomial f and its column use the same notation.
Its finite positive-lag autocorrelations are

    a_h(f)=sum_(j=0)^(T-h) f_j f_(j+h), 1<=h<=T.

A rational admissible bundle is a finite list of such f_b and positive rational weights omega_b with sum omega_b=1, satisfying sum omega_b a_h(f_b)=0 for EVERY h.
These conditions are precisely the Laurent identity sum omega_b f_b f_b*=E, where

    X=sum_b omega_b f_b f_b^T,
    L_h(X)=sum_(j=0)^(T-h) X_(j,j+h)=0,
    E=trace X=sum_b omega_b ||f_b||^2>0.                 (2)

Define E_T^Q as the INFIMUM of these E; no general minimum or attainment is presumed.
Define E_T^R by allowing real coefficients and real weights but RETAINING the exact formal residue requirement A f_b in Z^d minus{0}.
For real coefficients this is a requirement in the scalar extension of the power-basis quotient, not mere membership of the value at one chosen real embedding.
Irrational coefficients cannot be moved through the original field embeddings silently.

Let

    C_Z=conv{r r^T : r in Z^d minus{0}},                (3)

where conv means FINITE real convex combinations, without closure.
Each combination can be written with positive weights after zero weights are omitted.
No zero residue atom is allowed.
The rational analogue uses rational positive weights.
If a RATIONAL matrix Y belongs to C_Z, it has a finite rational convex representation: take any finite positive representation, solve its rational linear equations including sum lambda=1 by Gaussian elimination, and approximate the real free parameters by rationals within the strictly positive region.
Thus C_Z intersect Sym_d(Q) is exactly the rational finite convex hull.

In particular Y in C_Z implies Y>=0 and trace Y>=1, but those two inequalities are not sufficient.
For d>=2, let v=(1,1,0,...,0) and Y=v v^T/2.
It is rational positive semidefinite with trace 1.
In any finite positive rank-one representation, every integer atom would lie on the line of v: a vector orthogonal to v gives a sum of nonnegative squares equal to zero.
Nonzero integer atoms on that line are integer multiples of the primitive v, with squared norm at least 2.
Their normalized average cannot have trace 1.
This disproves the free-PSD/trace relaxation as an exact description.
Including the forbidden zero atom would erase this obstruction.

<a id="exact-rational-integer-moment-realization"></a>
## 3. Exact finite-moment characterization, including sufficiency

**Theorem 1.** A rational symmetric N-by-N matrix X is the coefficient second-moment matrix of a finite rational bundle with nonzero actual O_0-valued residues if and only if

    X>=0 and Y=A X A^T belongs to C_Z.                (4)

Consequently the exact optimization description is

    E_T^Q=inf{trace X:
        X in Sym_N(Q), X>=0,
        L_h(X)=0 for every 1<=h<=T,
        A X A^T in C_Z}.                              (5)

With real X and the same FINITE convex hull, the analogous formula gives E_T^R.
The moments in this theorem are second moments, not centered covariances; no mean-zero hypothesis on residue atoms is imposed.

Necessity follows directly from (1)--(2): Y=sum omega_b r_b r_b^T.
For sufficiency, write Y=sum_j lambda_j r_j r_j^T with r_j nonzero integers, lambda_j>0 rational and sum lambda_j=1, using the rational finite-representation fact above.
In particular Y is nonzero.
Every r_j lies in range Y, because each vector in ker Y has zero scalar product with every r_j.

Use the symmetric inverse Y^+ on range Y and zero on its orthogonal complement.
It is rational: choose a rational basis U of range Y and write Y=U C U^T with rational C positive definite; then

    Y^+=U(U^T U)^-1 C^-1(U^T U)^-1 U^T.

Define

    B=X A^T Y^+,
    K_0=X-B Y B^T.                                  (6)

Then A B is the orthogonal projection onto range Y.
Also K_0>=0 and A K_0=0.
Here is the needed complete square argument.
If h in ker Y, then (A^T h)^T X(A^T h)=0.
For a positive-semidefinite X this implies X A^T h=0: otherwise the quadratic polynomial in a scalar perturbation by a suitable vector would take a negative value.
Therefore A X z lies in range Y for every z.
With c=A X z,

    (z-A^T Y^+c)^T X(z-A^T Y^+c)
        =z^T Xz-c^T Y^+c=z^T K_0 z>=0.

The same range identity gives A K_0=A X-Y Y^+ A X=0.
No invertibility of X or Y and no full-row-rank assumption on A is needed.

A rational positive-semidefinite K_0 has a decomposition

    K_0=sum_(l=1)^k d_l v_l v_l^T,
    d_l>0 rational, v_l in Q^N intersect ker A,       (7)

with k=rank K_0; take a rational basis of its range and perform rational square completion on the induced positive-definite matrix.
Its range is contained in ker A.
A zero residual uses the empty list.
This is elementary rational LDL, not an assertion of rational square roots.

Choose a positive integer L with sum_l d_l/L^2<=1.
Define a finite rational noise distribution with values +L v_l and -L v_l, each of probability d_l/(2L^2), and value zero of probability 1-sum_l d_l/L^2; omit a zero-probability outcome.
Its mean is zero and second moment K_0.
For k=0 use only zero with probability 1.

Independently pair that noise with the residue distribution lambda_j and set

    f_(j,ell)=B r_j+eta_ell.                         (8)

Every coefficient is rational.
Moreover A f_(j,ell)=r_j, since AB r_j=r_j and A eta_ell=0.
Thus EVERY resulting coordinate has a nonzero actual residue; the construction introduces no separate zero-valued polynomial.
Averaging gives second moment B Y B^T+K_0=X because the cross terms have zero noise mean.
Weights are positive rational after omitting zero outcomes and sum to 1.
The construction remains in the ORIGINAL N positions.
This proves sufficiency and (5).
The real version follows by the same range/square argument with finite real noise, without a rationality claim.

This is an exact constraint characterization, not an ordinary semidefinite program: finite membership in C_Z retains all nonzero integer residue atoms.
It uses every residue fiber and its kernel noise, rather than only the least Euclidean representative selected in the old residual lattice.

<a id="rational-real-infima-and-attainment-boundary"></a>
## 4. Rational and formal-real infima agree; attainment is separate

**Proposition 2.** For this fixed input and window,

    0<E_T^Q=E_T^R<=1.                               (9)

For T<d, both infima are attained and equal 1 in the monogenic order.
In general no optimizer, finite residue cutoff, rational optimal matrix, closure of C_Z or strong-duality equality is asserted here.

The upper bound is the constant polynomial 1.
The short case follows from the unique degree-below-d coordinates: A f integer forces f integer for N<=d, also in the defined formal-real domain.
Every nonzero coordinate has energy at least 1 and 1 attains it.

For the equality of infima, start from ANY real feasible X and one finite positive representation Y=sum lambda_j r_j r_j^T.
The rational matrix X_*=I_N/N is positive definite and feasible: it is the second moment of the N monomials t^j with equal weights, each having the nonzero integer residue A e_j.
Its lag sums vanish and trace is 1.

For a small rational delta>0, mix (X,lambda) with this monomial packet.
The new matrix X_delta is positive definite and all the weights on the finite union of the two indexed residue lists are positive.
The equations

    A X_delta A^T=sum lambda_j r_j r_j^T,
    sum lambda_j=1, L_h(X_delta)=0

are linear equations with rational coefficients and rational right sides in the matrix entries and the weights.
Gaussian elimination supplies a rational parametrization of their real affine solution set.
Rational free parameters are dense.
Approximate the mixed point within that affine set while keeping positive definiteness and all weights strictly positive, which are open conditions.
The resulting rational X' is feasible by Theorem 1 and trace X' can be arbitrarily close to trace X_delta.
Let delta and the approximation error tend to zero.
Hence E_T^Q<=E_T^R; the reverse inclusion is immediate.
This proves equality of INFIMA, not exact rational realization of every real feasible energy.

For T>=d-1 the positive lower bound follows from Proposition 3 below with W=I; the remaining short windows already have value 1.
Thus no fixed finite window has infimum zero.

Bounded average energy does not bound the individual residue labels.
Already at T=0 the constants L and 1, at weights 1/L^2 and 1-1/L^2 for integers L>=2, form exact bundles with E=2-1/L^2 while one residue tends to infinity.
Small weights must remain visible.
Compactness of a trace-bounded PSD matrix set therefore does not by itself prove compactness/closedness of the finite-atom realization or attainment in (5).
The proof above does not replace finite C_Z by its closure.

<a id="weighted-quotient-lattice-certificate"></a>
## 5. Toeplitz weighted quotient certificates for all representatives

**Proposition 3, root's supplied certificate with complete verification.** Assume T>=d-1.
Choose any rational symmetric positive-definite Toeplitz matrix W of size N with diagonal 1.
If w_h is its h-th off-diagonal value, then

    f^T W f=||f||^2+2sum_(h=1)^T w_h a_h(f).

For every exact complementary bundle, all aggregate a_h vanish, so averaging gives sum omega_b f_b^T W f_b=E.
Define

    G_W=(A W^-1 A^T)^-1,
    f_W(r)=W^-1 A^T G_W r,
    mu(W)=min_(0!=r in Z^d) r^T G_W r.              (10)

Full row rank of A and W>0 make A W^-1 A^T and G_W positive definite.
Also A f_W(r)=r.
Every representative f of r has f=f_W(r)+k with A k=0, and f_W(r)^T W k=r^T G_W A k=0.
Thus

    f^T W f=r^T G_W r+k^T W k,
    E>=sum_b omega_b r_b^T G_W r_b>=mu(W)>0.        (11)

All minimizing representatives are rational for rational r,W,A.
Positive definiteness makes the lattice minimum positive and attained: any fixed lattice vector gives an upper cutoff, and coercivity bounds the Euclidean length of every vector below that cutoff, leaving finitely many integer vectors.
This is a finite-existence argument, not a claimed enumeration algorithm or uniform cutoff.

Let Gamma_T be the supremum of mu(W) over the stated rational positive-definite Toeplitz matrices with diagonal 1.
Then

    Gamma_T<=E_T^Q=E_T^R.                           (12)

Equation (12) is the proved weak lower-certificate statement.
This draft does NOT claim equality for every input or a maximizing W.
Neither perfect-form theory nor a general minimax theorem has been checked/applied to this nonlinear weighted-quotient family, the finite convex hull, its possible limiting atoms, or the open positive-definite domain.
Resolving general dual completeness would require additional work.
The exact control below has a matching certificate and bundle, so equality there is proved directly without general strong duality.

If a bundle attains mu(W), positivity of every weight in (11) forces EVERY residue to be a shortest vector of G_W and EVERY coefficient vector to be its W-least-norm representative.
Those two equality conditions, plus the exact lags, give a finite structural test at a specified W.
A certificate for a selected finite list or positive definiteness of G_W alone cannot replace the nonzero integer minimum.

At W=I, formula (10) is exactly the Euclidean quotient form already implicit in L237/L341.
In general its least representatives cannot be substituted into an existing bundle while assuming the same lag equations.
The new weighted certificate tests all representatives through an inequality and pays their nonnegative kernel error; it does not perform that invalid projection.

<a id="sharp-quadratic-window-minimum"></a>
## 6. Exact original control: E_2=1/5, strictly above the Euclidean lattice floor

Take the original P=t^2-4t+1 and alpha=2+sqrt3, O_0=Z[alpha]=Z[sqrt3].
Its two distinct irrational reciprocal roots are 2+/-sqrt3, so it is the actual irreducible degree-two nontorsion unit input.
Its total m(P)=log(2+sqrt3) stays positive.
Use T=2, N=3.
For f=x+y t+z t^2, the relation alpha^2=4alpha-1 gives

    A=[[1,0,-1],[0,1,4]],
    (m,n)=A f=(x-z,y+4z).                            (13)

Actual admissibility is exactly (m,n) in Z^2 minus{0}.
Choose

    W=[[1,2/5,3/5],[2/5,1,2/5],[3/5,2/5,1]].

It is Toeplitz with diagonal 1.
Direct expansion gives the complete identity

    f^T W f=[m^2+(n+2m)^2]/5+(4/5)y^2.             (14)

It also proves W positive definite: all three squares zero force y=m=n=0 and then x=z=0.
The integer change (m,n)->(m,n+2m) is unimodular.
Thus the nonzero residue minimum is at least 1/5, and equality requires y=0 and (m,n+2m) in {(1,0),(-1,0),(0,1),(0,-1)}.
Averaging the exact lag constraints proves E>=1/5 even for the formal-real version of the class.

The rational pair

    f_1=(1+t^2)/4, f_2=(1-t^2)/2,
    omega_1=4/5, omega_2=1/5                        (15)

attains it.
Its values are alpha and 1-2alpha, both nonzero actual O_0 elements.
The lag-two terms are (4/5)(1/16)+(1/5)(-1/4)=0; the lag-one terms are zero.
Its energy is (4/5)(1/8)+(1/5)(1/2)=1/5.
Hence

    Gamma_2=E_2^Q=E_2^R=1/5,

with an actual rational minimum.
Every equality coordinate in (14) is a signed copy of f_1 or f_2.
If p is the total weight on signed copies of f_1, lag two gives p/16-(1-p)/4=0, so p=4/5.
Thus (15), arbitrary repetitions and signs, and positive splits inside these two total masses describe ALL minimizing bundles in this fixed window.
No bounded coefficient or denominator assumption is used in the lower proof.

The Euclidean quotient form is

    r^T(AA^T)^-1 r
       =(17m^2+8mn+2n^2)/18
       =m^2/2+(n+2m)^2/9.                          (16)

Its complete nonzero integer minimum is 1/9: m!=0 gives at least 1/2, and m=0,n=+/-1 attains 1/9.
Those two Euclidean shortest representatives are +/- (2+t+2t^2)/9; each has lag-two autocorrelation 4/81>0.
No positive normalized mixture of only them is complementary.
This exposes the exact failure of replacing the problem by its shortest quotient representatives or a trace-only residue test.

The weighted certificate therefore improves the COMPLETE Euclidean residue minimum, not just a sampled list.
C14's earlier q=2,S=2 pair at the same input/window has E=1/2 and serves its different minimum-integer-energy classification.
Here variable coefficient denominators permit E=1/5 and the integer energy S is larger.
There is no contradiction between the two sharp assertions.

<a id="integer-moment-norms-and-costs"></a>
## 7. Every original norm, denominator and construction cost

For any rational admissible bundle in (5), let q be its ACTUAL least common coefficient denominator and M its ACTUAL least common positive weight denominator; let m_b=M omega_b.
Integer F_b=q f_b has the original signed full resultant

    Res(P,F_b)=q^d D(r_b),
    D(r)=Norm_(K/Q)(sum_(j<d) r_j alpha^j) in Z minus{0},
    I=log q+(1/d)sum_b omega_b log|D(r_b)|,
    product_b Res(P,F_b)^(m_b)
       =q^(dM) product_b D(r_b)^(m_b).              (17)

Every nonzero degree-below-d integral residue has nonzero full norm by irreducibility.
No original embedding or factor is discarded.
For an initially Laurent family shifted by one common t^a, multiply each pre-shift norm by Norm(alpha)^a, possibly -1 in the general domain; equivalently use the actual shifted residue throughout (17).

The final constant integer covariance is S=q^2 E>=1.
Each F_b is nonzero integral and has coefficient energy at least 1.
If its integer content is c_b, then c_b^d divides q^d D(r_b).
Unit residue norm is SUFFICIENT for c_b|q, not necessary; nonunit labels can have that divisibility too.
No primitive rescaling occurs while keeping old data.

The exact original-root inequality in [C10 v2](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality), whose selected finite-polynomial proof does not use reciprocity, gives

    (1/d)sum_b omega_b log|D(r_b)|-(1/2)log E
       <=(T/d)m(P).                                (18)

The residue-moment hull forgets norm income unless the actual atoms and weights are retained; two decompositions of a second moment need not have the same norm product.
For example, the single constant 2 and the constants 1,3 with weights 5/8,3/8 have the SAME coefficient second moment X=4 in window T=0.
Their normalized original norm incomes are log2 and (3/8)log3, respectively.
All residues are nonzero actual integers and q=1.
Thus (5) is an energy characterization, not an optimization of the full nonlinear arithmetic surplus.
It supplies no free bound on D(r_b).

The sufficiency construction keeps T exactly, but if the supplied finite residue representation has J atoms and rank K_0=k it may create up to J(2k+1) labels before zero probabilities and duplicates are removed.
Its coefficient denominator depends on B, the rational range inverse, noise vectors and L; its weight denominator depends on the initial lambda_j, d_l and L^2.
Those are the final q and M to be recomputed, not inherited denominators of an earlier packet.
No bound on residue sizes, those arithmetic denominators or bit costs uniform in P,T,E is supplied.
The rational-density proof similarly gives no approximation rate or denominator bound and proves no rational optimizer.

For (15), q=4, M=5, F_1=1+t^2 and F_2=2-2t^2 have contents 1 and 2 and energies 2 and 8.
The original residue norms are +1 and -3: Norm(alpha)=1 and Norm(1-2alpha)=1-2(4)+4=-3.
Thus the full numerator resultants are +16 and -48.
The actual copied signed product is

    16^4*(-48)=4^10*(-3),
    S=16/5,
    I=log4+(log3)/10,
    I-(1/2)log S=(log5)/2+(log3)/10.                (19)

Every factor is original degree 2.
Its width expense is Tm/d=log(2+sqrt3).
The second content 2 is retained.
Its sign and nonunit norm are part of the income, not discarded as if both target norms were 1.
The equality classification forces q=4 and total weights 4/5,1/5 for every rational minimizing bundle, so its least weight denominator is divisible by 5; arbitrary positive splitting can increase that denominator.
The energy and weighted income in (19) stay the same under those splits and overall signs.
This is one fixed positive-measure input, not a near-one family.

<a id="actual-overorder-moment-extension"></a>
## 8. Specified overorders and the remaining dual question

The moment theorem extends to a specified full order O containing alpha and alpha^-1 by choosing an ACTUAL Z-basis of O and using the integer coordinate matrix A_O of 1,alpha,...,alpha^T in that basis.
For T>=d-1 it has full row rank, though its first d columns need not be an integral identity and its integer column lattice can have nontrivial index.
Rational representatives are permitted, so A_O Q^N=Q^d in that range; actual admissibility remains A_O f in Z^d minus{0}.
The proof of (4)--(8) is unchanged.
For shorter windows, the same finite-moment condition automatically keeps all atoms in range A_O; no nonexistent representative is inserted.
The real-infimum comparison still uses the actual monomial residues A_O e_j and the rational positive matrix I_N/N.

The dual formula (10)--(12) applies at full row rank with A_O.
In original monogenic coordinates this is equivalently the ACTUAL overorder residue lattice, not a replacement by the maximal order or by real vectors.
In (17) replace the power-basis expression by sum r_j beta_j for the chosen actual order basis beta_j; its norm is still the complete original degree-d field norm.
No order index becomes an omitted income factor.
The short-window conclusion E_T=1 is specific to O_0 and is not extended to an overorder; C14's e=2 control explicitly prevents that extension.

A tempting stronger statement would identify E_T with the optimized positive Toeplitz lattice bound for EVERY P,T.
The present proof establishes the exact finite-moment primal and the weak bound, and proves equality for the explicit control; it does not settle that general assertion.
The required convex-closure, limiting-atom and dual-boundary analysis has not been supplied by a cited theorem or assumed from the word SDP.
Neither rational-real equality of INFIMA nor positive definiteness of a candidate lattice form proves attainment or dual completeness.

The input-uniform objective remains beyond this fixed-window description.
To obtain a uniform Mahler consequence one would need a bound or construction uniform over actual near-one original inputs, with the exact lattice minima, norm products and T/d all controlled.
The degree-two fixed-positive-measure optimum supplies no such coverage.
The new useful discriminator is exact: a proposed low-energy finite-window bundle can be excluded by any proved weighted whole-lattice minimum, while its exact feasibility additionally requires the full integer moment hull, not just a free covariance or least-representative energy.

<a id="integer-moment-author-self-check"></a>
## 9. Author self-check and review boundary

The complete self-check covers the actual monic power-basis residue map, nonzero-value equivalence, generic nonreciprocal scope and common Laurent shift; every coefficient and lag sum; finite rather than closed hull, rational finite-representation argument, and the explicit PSD/trace counterexample; singular Y range inversion, rationality, both square-completion identities, K_0 positivity and kernel range, rational finite noise with total probability 1 and zero mean, all nonzero residues and unchanged support; both directions of the moment characterization; strict positive rational affine approximation after mixing with all monomials, infimum versus optimizer and all short-window branches; every weighted quotient inverse, cross term, finite lattice-minimum and equality condition; the complete quadratic control, unimodular integer square certificate, all equality bundles, strict 1/9 versus 1/5 distinction and exact lag failure of Euclidean minimizers; actual q/M/content/norm signs and copied product, no automatic norm-income optimization, the overorder basis/index qualification and every unresolved uniform/duality/attainment claim.

Root's full conceptual and weighted-Toeplitz contributions are disclosed.
The primary source check concerns only classical arithmetic-minimum terminology and the infinite halfspace formulation; no new external theorem is a hidden proof premise.
This is author self-review, not separate independent evidence.
No mathematical native program, scan, solver, J or source-intake write occurred.
G0001 remains active and unrestrictedly unresolved.
Separate whole noncontributor review and root adoption remain pending.

<a id="integer-moment-entire-author-freeze"></a>
The complete Sections 1--9, Theorem 1, Propositions 2--3, equations (1)--(19), both directions of the finite-moment characterization, all real/rational and nonattainment boundaries, the sharp original quadratic control and its full equality/norm accounting are author-frozen at 2026-10-11T18:10 for a separately organized whole noncontributor review.
Scoped material validation passed before this freeze and is repeated afterward; it checks structure and locators, not mathematics.
Author work on this frozen input now stops pending review.



## Registration and preservation operation

2026-10-11T18:18: retain the entire 2026-10-11T18:10 D11 author freeze directly as this Claim argument.
The separate whole reviewer checked the complete mathematical account and identified two extraction precision guards: weighted-packet realization alone does not impose zero lags, and keeping the allowed window does not assert minimal width exactly T.
Both are explicit in this registered statement and proof selection.
New C-specific bindings require actual review of this exact statement and dependencies.
The original D is retired only after full-body comparison and incoming-link maintenance.
No native mathematical program, new allowance or Task completion accompanies registration.
