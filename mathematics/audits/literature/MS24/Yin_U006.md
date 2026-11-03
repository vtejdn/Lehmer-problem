---
author: Yin
---

# MS24-U006: Complete finite-dimensional scaling interfaces for the determinant proof

## Source and inspection

[Source and edition notes](readme.md).

Source edition: MS24 arXiv:2406.15922v1, the registered 19-page source; retained Gur04 and full 68-page GGOW20 sources at their registered editions.

Passages: MS24 Propositions 2.7-2.10 and Sections3-4, pp.8-16; Gur04 Lemma4.5/Theorem4.7 pp.462-465 / PDF15-18; GGOW20 p.242/PDF20 and Lemmas3.6/3.10 pp.257-258/PDF35-36.

Inspection: 2026-09-12 primary passages read; MS24 p.8 and GGOW20 p.258 visually inspected; complete stated elementary source-interface reconstructions checked, with separate coordinating check at its disclosed scope.


<a id="ms24-u006"></a>
## Exact retained source scope

This complete source-interface reconstruction was retained from [L_F4](../../../ledger/Yin_L_F0004_v1.md#ms24-scaling-dependency-review) at 2026-10-21T01:19.
The actual original coordinating check is retained in the R_F0188 family; the source reader's reconstruction and that second finding are distinct accounts.
This maintenance does not reopen the sources or certify any additional original proof, arithmetic algorithm or project Claim.

## Retained scaling reconstruction

<a id="ms24-scaling-dependency-review"></a>

- Record: 2026-09-12, the scaling-dependency reviewer, independent source-interface review requested for MS24 as the principal research input.
- State: **Audited within scope** for the reconstructions below.
  This is a supplement to the existing source units, not a new project Claim or a certificate for every theorem in the cited papers.
- Primary artifacts: MS24, arXiv 2406.15922v1, especially Propositions 2.7-2.10 and Sections 3-4, printed/PDF pp. 8-16; Gur04, Lemma 4.5 and Theorem 4.7, printed pp. 462-465 / PDF pp. 15-18; GGOW20, the 68-page published article, capacity variational formula p. 242 / PDF p. 20, Lemmas 3.6 and 3.10, pp. 257-258 / PDF pp. 35-36.
  MS24's bibliography calls the last publication GGOW20; the repository retains GGOW20.
- Inspection: the specified primary passages were extracted and read directly, and the MS24 p. 8 and GGOW20 p. 258 formula pages were visually inspected.
  Earlier audit records were compared with these passages.
  The elementary proofs below were checked independently of their earlier reconstructions.

## What the Main Proof Actually Needs

The determinant formula in [MS24-U003](Yin_U003.md#ms24-u003) needs an exact scaling for the **strictly positive perturbations**, and approximate scaling for maps of positive capacity.
It does not need uniqueness of a general indecomposable minimizer.
The zero-capacity case can also be settled using the same determinant normalization argument employed in MS24's Section 4, without a free-field rank theorem.
The proofs below therefore give the entire finite-dimensional scaling input without an unresolved original-proof dependency on Gur04's earlier references or GGOW20's algorithm analysis.

| Input | Exact role in the reconstructed chain | Review disposition |
| --- | --- | --- |
| Capacity transformation and adjoint duality | Normalize a near minimizer and bound its second marginal | Direct proofs below, including singular cases |
| Strict positivity implies an attained positive minimum and exact doubly stochastic scaling | Apply the exact semicircular formula to the depolarizing perturbations in the lower bound | Coercivity and differentiation proof below; no uniqueness assumption |
| Near minimizer implies small marginal defect | Upper bound via the approximately semicircular hermitizations | Direct proof of the source's `6 delta` interface below |
| Rank non-decrease is equivalent to positive capacity | Source context and capacity dichotomy; available for subsequent uses | Independent qualitative proof below |
| Full homogeneous pencil is equivalent to no shrunk subspace | Identify the free-field input for the Haar model in Theorem 1.3 | Separate algebraic interface, not a consequence of the capacity calculus |
| Faithful affiliated realization at free Haar generators and the integral free-group determinant bound | Injectivity and the lower determinant estimate in Theorem 1.3 | Retained external inputs of [MS24-U004](Yin_U004.md#ms24-u004); outside this scaling review |

Neither main theorem uses the questioned rounding precisions, literal iteration constants, or complete quantitative capacity-continuity modulus in GGOW20.
Invariant-degree bounds, the invariant-ring generator theorem, the polynomial-time rank algorithm, and GGOW20's weaker integral capacity bound are also unnecessary premises of the MS24 chains.
The algebraic full-pencil/shrunk-subspace equivalence is a distinct dependency: omitting the invariant-theory route does not prove that algebraic theorem automatically.

## Conventions and Elementary Capacity Identities

Let \(T:M_m(\mathbb C)\to M_m(\mathbb C)\) be a positive complex-linear map.
Write \(\operatorname{Tr}\) for the unnormalized trace and \(\operatorname{tr}_m=\operatorname{Tr}/m\).
Both inner products define the same adjoint \(T^*\).
Put

\[
r_T(C)=\frac{\det T(C)}{\det C},\qquad
\operatorname{cap}(T)=\inf_{C>0}r_T(C).
\]

Here \(C>0\) means positive definite.
The ratio is unchanged by multiplying \(C\) by a positive scalar, so the infimum may be taken over \(\det C=1\).

For invertible \(A,B\), changing variables gives

\[
\operatorname{cap}\bigl(X\mapsto A T(B^*XB)A^*\bigr)
=|\det A|^2|\det B|^2\operatorname{cap}(T).
\]

No minimum or nonsingularity of all outputs is assumed in this identity.
Positive capacity, however, implies \(T(C)>0\) for every \(C>0\), since a singular such output would give a zero competitor.
More generally \(T(I)>0\) already implies this: \(C\geq\lambda_{\min}(C)I\).

The variational identity on GGOW20 p. 242 has the following determinant-one form:

\[
m\operatorname{cap}(T)^{1/m}
=\inf_{X,Y>0,\ \det X=\det Y=1}\operatorname{Tr}(T(X)Y)
=m\operatorname{cap}(T^*)^{1/m}.
\]

For a fixed positive definite \(D=T(X)\), arithmetic-geometric mean bounds \(\operatorname{Tr}(DY)\) below by \(m(\det D)^{1/m}\), attained at \(Y=(\det D)^{1/m}D^{-1}\).
If \(D\) is singular, take \(Y\) small on its support and large on its kernel, with determinant one; the infimum is zero.
Trace duality then exchanges \(X,Y\).
The source uses determinant constraints at least one; scaling each variable down shows its infimum equals the determinant-one version.
Thus

\[
\operatorname{cap}(T)=\operatorname{cap}(T^*)
\]

also at zero capacity.
No optimizer is needed for duality.

## Strictly Positive Maps: The Exact Scaling Needed in the Lower Bound

Assume precisely the strict positivity used in MS24 Definition 2.5(iii):

\[
T(X)\geq\alpha\operatorname{tr}_m(X)I
\quad(X\geq0),\qquad \alpha>0.
\]

For \(C>0\), \(\det C=1\), determinant monotonicity and arithmetic-geometric mean give

\[
\det T(C)\geq\alpha^m\operatorname{tr}_m(C)^m\geq\alpha^m>0.
\]

A sublevel bound on \(\det T(C)\) therefore bounds \(\operatorname{Tr}C\).
It bounds every eigenvalue above; the determinant-one condition then bounds every eigenvalue away from zero.
Sublevel sets are compact in the finite-dimensional space of Hermitian matrices.
A minimizing sequence consequently has a positive determinant-one limit \(C\), and continuity gives \(\det T(C)=\operatorname{cap}(T)>0\).

Differentiate \(\log\det T(C)\) on the smooth constraint \(\log\det C=0\).
The Lagrange multiplier equation is

\[
T^*(T(C)^{-1})=\lambda C^{-1}.
\]

Pairing with \(C\) under \(\operatorname{Tr}\) gives \(m=\lambda m\).
Hence

\[
Z(X)=T(C)^{-1/2}T(C^{1/2}XC^{1/2})T(C)^{-1/2}
\]

satisfies \(Z(I)=Z^*(I)=I\).
This is the positive-attainment part of Gur04 Theorem 4.7, with existence proved here at the smaller strictly positive scope actually used in the perturbation argument.
It is valid also for \(m=1\).
It does not require the general indecomposable uniqueness theorem or its mixed-discriminant estimates.

For the perturbed map \(\eta_t=\eta+t\beta\), \(\beta(X)=\operatorname{tr}_m(X)I\), one can take \(\alpha=t>0\).
Thus all exact scalings needed in the general lower bound meet the displayed hypotheses.
At an arbitrary positive \(C\), only \(Z(I)=I\) is automatic; the false general adjoint-normalization sentence on MS24 p. 8 is not used.

## Near Minimizers: A Direct Check of the GGOW20 Interface

Assume \(\operatorname{cap}(T)>0\), \(C>0\), \(0\leq\delta\leq1/6\), and

\[
\operatorname{cap}(T)\geq e^{-\delta}r_T(C).
\]

Define \(Z\) as above.
It is well-defined, \(Z(I)=I\), and the scaling identity and duality give

\[
\operatorname{cap}(Z^*)=\operatorname{cap}(Z)
=\frac{\operatorname{cap}(T)}{r_T(C)}\geq e^{-\delta}.
\]

Let \(x_1,\ldots,x_m>0\) be the eigenvalues of \(D=Z^*(I)\).
Positivity follows from positive capacity; trace duality gives \(\sum_jx_j=m\).
Since the identity matrix is a capacity competitor,

\[
\prod_jx_j=\det D\geq\operatorname{cap}(Z^*)\geq e^{-\delta}.
\]

Set \(f(x)=x-1-\log x\).
Then \(f\geq0\) and

\[
\sum_j f(x_j)=-\log\det D\leq\delta.
\]

Since \(f(2)=1-\log2>1/6\), and \(f\) is increasing for \(x\geq1\), every \(x_j<2\).
For \(1\leq x<2\),

\[
f(x)=\int_1^x\frac{t-1}{t}\,dt\geq\frac{(x-1)^2}{4},
\]

and for \(0<x\leq1\),

\[
f(x)=\int_x^1\frac{1-t}{t}\,dt\geq\frac{(x-1)^2}{2}.
\]

Consequently the required source estimate follows directly:

\[
\operatorname{ds}(Z)=\operatorname{Tr}((Z^*(I)-I)^2)
=\sum_j(x_j-1)^2\leq4\delta\leq6\delta.
\]

The intermediate constant four is only an elementary proof check supporting MS24 Proposition 2.10's stated constant six; no separate new result is designated here.
Complete positivity is supplied in MS24's application; this finite-dimensional calculation itself uses positivity only.

The Hermitian error matrix is

\[
E=C^{1/2}T^*(T(C)^{-1})C^{1/2}-I.
\]

It is similar to \(CT^*(T(C)^{-1})-I\), so cyclicity gives the squared trace printed in both papers.
That printed matrix is not generally Hermitian; its squared trace must not be replaced with its Hilbert-Schmidt norm squared without the conjugation above.

This proof avoids two shortcuts in the original GGOW20 proof: Lemma 3.10 weakens the available bound to \(1-\delta\), although the invoked Lemma 3.6 requires \(e^{-\delta}\); Lemma 3.6 invokes Lemma 5.1 without explicitly treating variance above one.
The earlier [GGOW20-U003](../GGOW20/Yin_U003.md#ggow20-u003) repairs those steps.
The direct estimate here independently verifies the exact MS24 input without using Lemma 5.1 or any algorithmic constants.
The assumption that \(T(C)>0\), implicit but essential in GGOW20's statement, is guaranteed by MS24's explicit positive-capacity hypothesis.

## Rank and Capacity: The Qualitative Gur04 Input

Gur04 Lemma 4.5 applies to **positive** maps, not only completely positive maps.
Its exact conclusion is

\[
\operatorname{cap}(T)>0
\quad\Longleftrightarrow\quad
\operatorname{rank}T(P)\geq\operatorname{rank}P\quad(P\geq0).
\]

The source uses a quantitative mixed-discriminant comparison from earlier references.
The qualitative conclusion can be checked without that comparison, as follows.

For an orthonormal basis \((u_i)\), let \(B_i=T(u_iu_i^*)\), and let \(d(U)\) be the coefficient of \(z_1\cdots z_m\) in \(\det(\sum_i z_iB_i)\).
Rank-one positive decompositions of the \(B_i\), followed by Cauchy-Binet, show that all coefficients are nonnegative and that \(d(U)>0\) exactly when independent vectors can be selected, one from each \(\operatorname{ran}B_i\).

The selection condition holds exactly when

\[
\dim\sum_{i\in J}\operatorname{ran}B_i\geq |J|
\quad(J\subseteq\{1,\ldots,m\}).
\]

Its sufficiency has a direct induction.
If a nonempty proper subset has equality, first select a basis for it and apply induction to the other subspaces modulo its sum; the inequalities descend by adjoining that subset.
Otherwise every proper nonempty subset has one extra dimension.
Choose a nonzero vector from the last subspace and quotient by its span; the remaining inequalities still hold.
The case of one subspace starts the induction.
This checks the needed finite-dimensional selection fact rather than importing an uninspected stronger bound.

Rank non-decrease applied to coordinate projections supplies these inequalities for every \(U\).
The coefficient \(d(U)\) is continuous and positive on the compact unitary group, so \(d_0=\min_U d(U)>0\).
For \(C=U\operatorname{diag}(\lambda_i)U^*>0\), \(\prod_i\lambda_i=1\), coefficient nonnegativity gives \(\det T(C)\geq d(U)\geq d_0\).
Thus capacity is positive.

Conversely, rank decrease can be tested on the support projection of a positive matrix: upper and lower positive scalar comparisons on its support show that the two images have the same support.
If \(P\) has rank \(k<m\) and \(T(P)\) rank \(r<k\), use the determinant-one matrices

\[
C_t=t^{m-k}P+t^{-k}(I-P),\qquad t\longrightarrow\infty.
\]

Then

\[
\det T(C_t)=t^{-km}\det(t^mT(P)+T(I-P))
=O(t^{m(r-k)})\longrightarrow0,
\]

because the polynomial determinant has degree at most \(r\) in \(t^m\).
If \(k=m\), the matrix \(T(I)\) is singular and positivity forces every \(T(C)\), \(C>0\), into its proper support.
Capacity is again zero.
This covers all matrix sizes and the zero map.

The source's stronger existence-and-uniqueness statement for general indecomposable maps is reviewed in [Gur04-U003](../Gur04/Yin_U003.md#gur04-u003).
This supplement does not independently repeat its uniqueness proof.
The scalar exception remains: indecomposability as defined by testing ranks strictly between zero and \(m\) is vacuous when \(m=1\); it does not make the zero map scalable.
Positive capacity or the strictly positive hypothesis above prevents that misuse.

## The Zero-Capacity Case of the Determinant Formula

This is a direct reuse of MS24 Section 4's determinant/second-moment normalization argument at the semicircular model.
Let \(S=\sum_i a_i\otimes s_i\in M_m(M)\), where the \(s_i\) are freely independent standard semicircular elements in a finite tracial von Neumann algebra \((M,\tau)\), and \(\eta(C)=\sum_i a_iCa_i^*\).
All Fuglede-Kadison determinants use \(\operatorname{tr}_m\otimes\tau\).

If \(\eta(I)\) is singular, a nonzero vector \(v\) in its kernel satisfies \(a_i^*v=0\) for all \(i\).
The projection onto \(\mathbb Cv\), tensored with \(1\), is contained in the kernel projection of \(S^*\).
It has positive trace, so \(\Delta(S^*)=\Delta(S)=0\).

If \(\eta(I)>0\), every \(\eta(C)\), \(C>0\), is positive definite.
Set

\[
S_C=(\eta(C)^{-1/2}\otimes1)S(C^{1/2}\otimes1).
\]

The standard second moments give

\[
(\operatorname{tr}_m\otimes\tau)(S_CS_C^*)
=\operatorname{tr}_m\!\left(\sum_i
\eta(C)^{-1/2}a_iCa_i^*\eta(C)^{-1/2}\right)=1.
\]

The ordinary determinant arithmetic-geometric mean bound and multiplicativity yield

\[
\Delta(S_C)^2=\Delta(S_CS_C^*)\leq1,
\qquad
\Delta(S)=r_\eta(C)^{1/(2m)}\Delta(S_C)
\leq r_\eta(C)^{1/(2m)}.
\]

Taking the infimum proves \(\Delta(S)\leq\operatorname{cap}(\eta)^{1/(2m)}\), and hence the required zero-capacity assertion.
This weaker general inequality is used only to settle the zero case; the sharper factor \(e^{-1/2}\) at positive capacity still requires the main semicircular argument.

Unlike MS24 Remark 3.1's original route, this check needs no free-field realization, rank/capacity equivalence, or prior injectivity theorem.
Multiplicativity of the ordinary determinant, including singular bounded factors, remains an explicit accepted foundation from [MS24-U005](Yin_U005.md#ms24-u005).
No determinant of an unbounded inverse is taken.

### The Additional Injectivity Equivalence

Zero determinant alone does not imply a kernel for a general bounded operator.
If the additional equivalence between positive capacity and affiliated invertibility is required, the independently checked Gur04 rank criterion gives an elementary kernel argument for this linear model.

If capacity is zero, there is a subspace \(V\subseteq\mathbb C^m\) with \(k=\dim V>r=\dim\sum_i a_iV\).
Let \(P,Q\in M_m(M)\) be the scalar projections onto these two subspaces, tensored with \(1\).
Then \(SP=QSP\).
The right support \(e\) of \(SP\) is at most \(P\); its left support is at most \(Q\).
Polar decomposition and the finite trace give

\[
(\operatorname{tr}_m\otimes\tau)(e)
\leq(\operatorname{tr}_m\otimes\tau)(Q)=r/m.
\]

The projection \(P-e\) lies in the kernel of \(S\), and its trace is at least \((k-r)/m>0\).
This argument uses only the coefficient-space rank obstruction and works for every represented tuple for which the displayed linear operator is defined and bounded.
Conversely, after the determinant formula has been proved, positive capacity gives positive ordinary determinant and hence injectivity; in a finite von Neumann algebra this is equivalent to an affiliated inverse.
Thus the extra equivalence, and the implication from injectivity needed in Corollary 1.4, can also be checked without the semicircular free-field realization theorem.
The Haar injectivity direction in Theorem 1.3 remains a separate dependency.

## Remaining Foundations and Limits

The finite-dimensional proofs retain spectral calculus, compactness, Cauchy-Binet, elementary determinant differentiation, and scalar integration/Jensen inequalities.
The zero-capacity operator argument additionally retains ordinary Fuglede-Kadison determinant multiplicativity and the standard semicircular second moments.
These are named foundations, not unresolved numerical conditions.

For Theorem 1.3, the identity \(\operatorname{ran}\eta(P)=\sum_i a_i\operatorname{ran}P\) identifies rank non-decrease with the absence of a shrunk subspace.
The next step, from this condition to fullness over the free field, is the separate algebraic theorem recorded in [GGOW20-U001](../GGOW20/Yin_U001.md#ggow20-u001) and [MSY23-U001](../MSY23/Yin_U001.md#msy23-u001).
Realization at free Haar unitaries and the integral free-group determinant property must then be verified at their own interfaces.
They cannot be replaced by positive capacity alone, and this supplement does not claim to audit their original proofs.

These inputs provide exact or approximate scaling and logarithmic determinant information.
They imply neither a bounded inverse nor a spectral gap for the represented operator.
No manuscript statement, project Claim, or unrelated numerical-algorithm assessment is changed by this supplement.
