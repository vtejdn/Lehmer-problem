---
author: Yin
---

# Affiliated Operators and Free-Field Realization

## MSY23-U004

- Source: [MSY23, user-supplied published MSY23.pdf](../../../literature/pdf/MSY23.pdf), JFA 285 (2023), article 110016; canonical work key MSY23.
- Locators: Section 5.1, printed/PDF pp. 28-34, through Remark 5.11.
All pages were read; pp. 29 and 32-34 were also checked as rendered pages.
Corollary 5.12 and the beginning of Corollary 5.13 on p. 34 were read for the handoff to the next unit.
- Record: 2026-09-08, the main unit authoring agent; proof audit for [MSY23 free-field and Atiyah source audit](readme.md#msy23-free-field-and-atiyah-source-audit).
Independent review of the main pp. 28-34 unit by the main unit reviewing agent is recorded below; the later p. 36 supplement has a separate review boundary.
- Result: Lemmas 5.1-5.5, Theorem 5.6, Lemma 5.9, and Remarks 5.7-5.11 are accepted within the declared affiliated-operator and free-field foundations.
A range statement in the proof is made precise below using closures.
This unit does not establish bounded scalar descent.

### Ambient Algebra, Domains, and Foundational Inputs

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, in a faithful Hilbert-space representation.
Write \(U=U(M)\) for the algebra of closed densely defined affiliated operators.
Sums and products in \(U\) mean the closures of the natural densely defined operations.
Matrix amplification identifies \(M_N(U)\) with the affiliated algebra of \(M_N(M)\).

The source recalls the affiliated \(*\)-algebra and polar-decomposition theory from reference [47].
These basic operator-algebra facts are retained foundational inputs, consistent with the affiliated and finite-algebra interfaces already recorded in [Miy26-U008](../Miy26/Yin_U008.md#miy26-u008).
This audit does not reconstruct the general existence/associativity proof for closures of affiliated sums and products.
The required specific consequences are proved below.
The algebraic free-field foundations and all Section 4 interfaces are separated in [MSY23-U003](Yin_U003.md#msy23-u003).

No selfadjointness, normality, freeness, or generation condition on \(X\in M^n\) is required in Theorem 5.6 itself.
Later results connect its equivalent conditions with \(\Delta(X)=n\) and dual systems; those implications belong to the neighboring units.

### Lemmas 5.1-5.5: Finite Trace, Invertibility, and Stable Finiteness

For \(T\in U\), polar decomposition is \(T=V|T|\), where \(V\in M\) is a partial isometry.
Its initial and final projections are

\[
V^*V=1-p_{\ker T},\qquad VV^*=p_{\overline{\operatorname{im}T}}.
\]

The trace of these two equivalent projections agrees, so

\[
\tau(p_{\ker T})+\tau(p_{\overline{\operatorname{im}T}})=1.
\]

This proves Lemma 5.2 from Lemma 5.1.
If \(T\) is injective, its range is dense by faithfulness of the trace.
The inverse on that range is closed, densely defined, and affiliated (equivalently use the spectral inverse of \(|T|\) and the now unitary polar factor).
It is a two-sided inverse in \(U\).
Conversely, if \(T\) has a nonzero kernel projection, \(T p_{\ker T}=0\) in \(U\), ruling out an inverse.
Thus injectivity is equivalent to affiliated invertibility, at every matrix size.
This conclusion asserts no bounded inverse.

For clarity, Lemma 5.3 can also be proved exactly along the source's algebraic route.
If \(XY=1\) and \(Y=Y^*\), then \(YX^*=1\) and

\[
X^*=(XY)X^*=X(YX^*)=X,
\]

so \(YX=1\).
For general \(Y=V|Y|\), apply this argument to \((XV)|Y|=1\) to obtain \(|Y|XV=1\).
If \(e\) is the kernel projection of the bounded partial isometry \(V\), multiplication by \(e\) gives \(e=0\).
Finiteness of the trace makes \(V\) unitary.
Moreover \(|Y|\) already has two-sided inverse \(XV\).
Hence \(Y\) is invertible, with inverse \(X\).
Applying the same proof to \(M_N(U)\) establishes stable finiteness.
All identities here are identities in the affiliated algebra, avoiding unjustified multiplication on pointwise operator domains.

Definition 5.4 uses the **unnormalized** matrix trace:

\[
\operatorname{rank}(P)
=(\operatorname{Tr}_N\otimes\tau)(p_{\overline{\operatorname{im}P}})
=N-(\operatorname{Tr}_N\otimes\tau)(p_{\ker P}).
\]

Consequently \(0\le\operatorname{rank}(P)\le N\), and Lemma 5.5 states that equality with \(N\) is equivalent to invertibility in \(M_N(U)\).
The normalized trace used to make matrix amplifications probability spaces on p. 29 is not the trace used in this rank definition.

### Lemma 5.9: A Local Domain-Aware Proof

The source cites [33, Lemma 2.3] for invariance of analytic rank under multiplication by invertible affiliated matrices.
Here is a proof from the declared closure convention that avoids another uninspected external proof.

For affiliated matrices \(A,B\) of the same square size, every vector in the range of the natural composition belongs to \(\operatorname{im}A\).
Taking the graph closure therefore gives

\[
\overline{\operatorname{im}(AB)}\subseteq
\overline{\operatorname{im}A}.
\]

Also \(\ker B\subseteq\ker(AB)\): a kernel vector belongs to the natural composition domain, because its image is zero.
The trace rank formula then gives

\[
\operatorname{rank}(AB)\le\min\{\operatorname{rank}(A),\operatorname{rank}(B)\}.
\]

If \(Q\) is invertible in the affiliated algebra, apply these inequalities first to \(PQ\) and \(QP\), and then to \(P=(PQ)Q^{-1}=Q^{-1}(QP)\).
This yields

\[
\operatorname{rank}(P)=\operatorname{rank}(PQ)=\operatorname{rank}(QP).
\]

No boundedness of \(Q\) or \(Q^{-1}\) is used.
In particular, raw range inclusion need not be substituted for closure-of-range inclusion for a closed affiliated product.

### Theorem 5.6: Exact Equivalences

Let \(R=\mathbb C\langle x_1,\ldots,x_n\rangle\), \(F\) its free field, and \(\operatorname{ev}_X:R\to U\) polynomial evaluation.
The source proves equivalence of:

1. Every full affine linear square matrix over \(R\), of every size, evaluates to an invertible matrix over \(U\).
2. Every full square polynomial matrix, of every size, does so.
3. For every square polynomial matrix \(P\), \(\operatorname{rank}(P(X))=\rho_R(P)\).
4. Every \(r\in F\) has \(X\in\operatorname{dom}_U(r)\), and the consistent evaluation of Definition 4.5 is an injective unital homomorphism \(\operatorname{Ev}_X:F\hookrightarrow U\) extending polynomial evaluation.

When these hold, the extension is unique, and for every square matrix \(P\) over \(F\),

\[
\operatorname{rank}(P(X))=\rho_F(P)=\rho_U(P(X)).
\tag{5.2}
\]

For polynomial matrices \(\rho_R=\rho_F\) is a retained free-field theorem; for arbitrary rational matrices, the notation \(\rho_F\) is essential.

### Reconstruction of the Proof

The implication (2) to (1) is immediate, and (3) to (2) is Lemma 5.5.
For (4) to (3), diagonalize \(P\) over the division ring \(F\): there are invertible \(L,R_0\) with

\[
LP R_0=\operatorname{diag}(I_k,0),\qquad k=\rho_F(P).
\]

This is Lemma 4.13 with the pivot normalization repaired in U003.
Evaluation of a unital homomorphism preserves the inverses of \(L,R_0\); Lemma 5.9 then identifies the analytic rank with \(k\).
The same argument already works for every rational matrix \(P\).

For (1) to (4), Theorem 4.3 gives a full affine linear representation of each \(r\).
In fact every such representation has an invertible evaluation by (1).
Theorem 4.4 applies because \(U\) is stably finite, so these values agree.
The explicit sum and product constructions in U003 verify additivity and multiplicativity after evaluation; polynomial representations verify agreement with \(\operatorname{ev}_X\) and preservation of the identity.
A unital homomorphism from the division ring \(F\) to the nonzero algebra \(U\) has zero kernel: a nonzero kernel element would bring its inverse and hence 1 into the kernel.
This proves injectivity.

It remains to compare inner rank over \(U\) with analytic rank.
Write \(P(X)=AB\) through \(k=\rho_U(P(X))\) columns, and pad the rectangular factors to square matrices

\[
\widehat A=(A\ \ 0),\qquad \widehat B=\binom{B}{0}.
\]

The last \(N-k\) coordinate subspace lies in \(\ker\widehat A\), so \(\operatorname{rank}(\widehat A)\le k\).
By the preceding product inequality,

\[
\operatorname{rank}(P(X))\le k.
\]

On p. 32 the source writes \(\operatorname{im}(P(X))\subseteq\operatorname{im}(\widehat A)\).
With closed products, the sufficient precise statement is the inclusion between **closures** of these ranges, proved above.
This clarification preserves the entire inequality.
Conversely, any factorization over \(F\) evaluates to one over \(U\), so \(\rho_U(P(X))\le\rho_F(P)\).
Together with the rational-matrix diagonalization, this proves (5.2).

For uniqueness, the set on which two unital extensions agree is a subalgebra of \(F\) containing \(R\), and is closed under inverses of nonzero elements, because both maps preserve those inverses.
Since \(R\) generates \(F\) as a division ring, the agreement set is all of \(F\).
This completes all implications and the additional conclusions without importing minimal-realization uniqueness.

### Remarks 5.7-5.10 and the Ambient Boundary

Remark 5.7 follows by multiplying \(r(X)w=0\) by \(\operatorname{Ev}_X(r^{-1})\).
Nonzero rational elements are units of \(U\), so they have no nonzero left or right annihilator there, and in particular none in \(M\).
The full-matrix variant is identical.
This is affiliated invertibility, not a spectral gap around zero.

Remark 5.8 uses the formal involution with \(x_j^*=x_j\).
A representation \((u,A,v)\) transforms to \((v^*,A^*,u^*)\); fullness is preserved because transposing and taking adjoints reverses any factorization.
If the actual tuple is selfadjoint, the evaluated involution agrees and \(\operatorname{Ev}_X\) is a \(*\)-homomorphism.
For a merely normal tuple, the condition \(X_j=X_j^*\) is absent, and this conclusion does not apply to that formal involution.

For Remark 5.10 put \(B=\mathbb C\langle X\rangle\) and \(F_X=\operatorname{Ev}_X(F)\).
Then

\[
F_X=\operatorname{Div}_{U}(B)=\operatorname{Rat}_{U}(B).
\]

To check every inclusion, the division subring \(F_X\) contains \(B\) and is inverse closed in \(U\), so \(D=\operatorname{Div}_U(B)\subseteq F_X\).
For any nonzero \(d\in D\), the inverse exists in \(F_X\subset U\), hence lies in \(D\) by its definition.
Thus \(D\) itself is a division ring; Proposition 4.11 gives \(D=\operatorname{Rat}_U(B)\).
Conversely every element of \(F_X\) is a finite rational expression in \(B\), so lies in \(D\); alternatively the evaluated linear representation puts it directly in the rational closure.
The source's brief inference that the division closure is a division ring therefore has the requisite justification.

All three objects in this equality are computed inside \(U\).
The theorem does not identify \(F_X\cap M\) with \(\operatorname{Div}_M(B)\).
It also does not say that boundedness of \(uA(X)^{-1}v\) makes the entire affiliated inverse \(A(X)^{-1}\) bounded, or that a different bounded representation must exist.
The exact scalar-versus-matrix distinction and the additional steps needed for the user's proposed bounded-linearization route are recorded in U003.

### Remark 5.11: Commutative Comparison

For a commuting tuple, the analogous field is \(K=\mathbb C(x_1,\ldots,x_n)\).
Every nonzero scalar polynomial evaluating to a unit of \(U\) is equivalent to extension of polynomial evaluation to \(K\): fractions can be evaluated because their polynomial values commute.
A unital extension from this field is injective, and nonzero polynomial images are units.
Diagonalization over \(K\), followed by Lemma 5.9, gives the equivalent matrix statement

\[
\operatorname{rank}(P(X))=\rho_K(P)
\quad(P\text{ a square polynomial matrix}).
\]

The inner rank here is over the **commutative fraction field**.
The source explicitly warns that polynomial-ring inner rank is not generally preserved in more than two commuting variables; its cited general ring-theoretic classification is retained as a reported background fact, not needed to prove the three-way equivalence just checked.
The commutative comparison supplies no bounded inverse theorem.

### Supplement for the Arbitrary-Domain Aside on p. 36

The paragraph after Theorem 5.14 also asserts, without the maximal-Delta hypotheses, that whenever a rational matrix has a defined affiliated evaluation,

\[
\operatorname{rank}(P(X))\le\rho_U(P(X))\le\rho_F(P).
\tag{A}
\]

The first inequality holds for every affiliated matrix by the padded-factorization argument above.
The cited proof of Theorem 5.6 does not by itself establish the second inequality at such an arbitrary tuple: factors in a free-field rank factorization may acquire new denominators undefined at \(X\).
Here is a repair, with the extra operator-algebra foundation identified explicitly.

Choose defined linear representations of the finitely many entries and assemble them into \(P=VA^{-1}W\), where \(A\) is a full affine linear polynomial matrix of size \(m\), \(A(X)\) is invertible over \(U\), and \(V,W\) are constant rectangular matrices.
The polynomial bordered matrix

\[
L=\begin{pmatrix}0&V\\W&A\end{pmatrix}
\]

has \(\rho_R(L)=\rho_F(L)=m+\rho_F(P)\).
Its polynomial rank factorization does evaluate at \(X\), giving \(\operatorname{rank}(L(X))\le m+\rho_F(P)\).
Affiliated Schur elimination, using the known inverse \(A(X)^{-1}\), gives \(\operatorname{rank}(L(X))=m+\operatorname{rank}(P(X))\).
Thus

\[
\operatorname{rank}(P(X))\le\rho_F(P)
\tag{B}
\]

without any new external foundation.
This already proves the direct spectral inclusion \(\sigma^{\rm full}(P)\subseteq\sigma_U(P(X))\) after replacing \(P\) by \(P-\lambda I\).

To recover the full intermediate inner-rank assertion in (A), retain additionally the standard finite-von-Neumann-algebra projection comparison theorem: with the unnormalized center-valued trace on \(M_N(M)\), \(p\precsim q\) exactly when the center-valued trace of \(p\) is bounded above by that of \(q\).
This foundational theorem is stated here as an additional input; its general proof is not re-audited.

Let \(k=\rho_F(P)\) and \(p=p_{\overline{\operatorname{im}P(X)}}\).
For every nonzero central projection \(z\in M\), compress the preceding Schur-polynomial argument to \(zM\), with normalized trace \(\tau(\cdot)/\tau(z)\).
Central compression preserves the existing inverse of \(A(X)\), so the argument applies and yields

\[
(\operatorname{Tr}_N\otimes\tau)(zp)\le k\tau(z).
\]

These inequalities for all central \(z\) imply that the center-valued trace of \(p\) is at most \(k1\).
Projection comparison therefore gives \(p\precsim\operatorname{diag}(I_k,0)\).
Choose a bounded rectangular partial isometry \(V_0\in M_{N,k}(M)\) with \(V_0V_0^*=p\).
Then

\[
P(X)=V_0\bigl(V_0^*P(X)\bigr)
\]

is a factorization over \(U\) through \(k\) columns.
It proves \(\rho_U(P(X))\le k\), completing (A).
For \(k=0\), (B) directly gives \(P(X)=0\).
This supplement distinguishes the fully local analytic estimate from the stronger assertion using projection comparison.
It does not replace an affiliated inverse by a bounded inverse.

### Fixed bounded-rank consequence

The complete local equality rho_M(C)=rho_U(C), polar-decomposition proof and bounded-border application are retained in [C_F9](../../../claims/Yin_C_F0009_v1.md#statement).
That project consequence retains its 2026-09-09 author/contributor checks and algebraic-control limitation; it is not an additional theorem quoted from MSY23, a new independent review or a claim about polynomial-algebra factors.

### Checks, Dependencies, and Handoff

The main proof uses only the affiliated \(*\)-algebra/polar-decomposition foundation, the free-field foundation in U003, the repaired division-ring elimination lemma, and the fully reconstructed evaluation theorem.
Lemma 5.9's external citation is replaced here by a local closure-domain proof.
The p. 36 supplement separately identifies its additional projection-comparison input, needed only for the stronger arbitrary-domain inner-rank statement.
No normalization or adjoint convention was transferred from a different version.
Theorem 5.6 is source-independent of \(\Delta\) or dual systems; combining it with Theorem 3.1 requires that earlier unit's audit, and Corollary 5.12 is handed to the subsequent spectral unit.
No claim of formal verification, exhaustive external-errata search, or bounded-intersection resolution is made.
Initial unit, 2026-09-08.

Independent review, 2026-09-08, the main unit reviewing agent: read the main unit against published pp. 28-34, together with its Section 4 dependencies.
Verified affiliated product range-closure and kernel inclusions, the resulting rank inequalities, stable finiteness, every Theorem 5.6 implication, rational-matrix rank preservation, uniqueness, and the fixed affiliated ambient in Remark 5.10.
No circular use of Delta or bounded-intersection equality was found.
This review was completed before the separately labeled p. 36 supplement was added and does not by itself certify that supplement.

### Independent Review of the p. 36 Supplement and Its Comparison Input

Date and reviewer: 2026-09-09, the main unit reviewing agent, independent of the supplement's author.
The supplement passes with the following explicit source interface and checks.

The required primary statement is [AP18, author-hosted draft](https://www.math.ucla.edu/~popa/Books/IIun.pdf), **Proposition 9.1.8, printed p. 142 / PDF p. 148**: in a tracial von Neumann algebra, projections satisfy p subequivalent to q exactly when their normal center-valued traces have that order.
Proposition 9.1.6 on the same page supplies the faithful normal center-valued trace as the trace-preserving expectation onto the center.
Definition 2.4.3, printed pp. 36-37 / PDF pp. 42-43, fixes subequivalence by a partial isometry w with w*w=p and ww*<=q.
These exact statements and surrounding conventions were checked in the 338-page primary PDF; the general projection-comparison foundations were not recursively audited.
Section 9.1 has the finite tracial hypotheses needed here; the separability restriction introduced later in Section 9.2 is not used.
No local PDF, new version date, or full AP18 audit is claimed.

The decisive independent calculations are:

1. Entrywise defined representations combine by a finite block direct sum into a single defined pencil A.
Every inverse used in this construction was already defined at X; it does not evaluate the potentially undefined factors in a free-field rank factorization of P.
Over the free field, the Schur border L is equivalent to diag(-P,A), so its formal inner rank is m+k.
Its polynomial rank factorization can therefore be evaluated at X.
The affiliated Schur operations are invertible in that same ambient algebra and give analytic rank(L(X))=m+rank(P(X)).
This proves (B), including the correct Schur sign.
2. For nonzero central z, polynomial evaluation in zM is unital with scalar c represented by cz.
Restricting the known inverse A(X)^{-1} gives the inverse of A(zX) on the central summand.
The range projection of the evaluated matrix in that summand is zp.
Repeating the same argument with the faithful normalized trace tau_z=tau/tau(z) yields the displayed estimate for every central projection.
No measurable choice of free-field factorizations is involved.
3. Put T_N=Tr_N tensor E_Z, the unnormalized center-valued trace; thus T_N(I_N)=N and tau(T_N(zp))=(Tr_N tensor tau)(zp).
If T_N(p)<=k failed, some central spectral projection z of T_N(p) above k+epsilon would be nonzero.
Faithfulness would give tau(z)>0 and contradict the central-corner estimate.
Hence T_N(p)<=k.
Applying Proposition 9.1.8 in M_N(M) is legitimate: its normalized center-valued trace is T_N/N, so comparison with q=diag(I_k,0) is unchanged by the normalization.
4. Comparison supplies w in M_N(M) with w*w=p and ww*<=q.
Since w*=w*q, w* has zero columns after column k.
Let V_0 be its first k columns.
Then V_0V_0*=p, as required; V_0*V_0 need only be a projection below I_k.
Finally pP(X)=P(X) as an affiliated identity, so V_0(V_0*P(X)) is an actual affiliated factorization through k columns.
The zero-rank case follows from faithful analytic rank separately.

Consequently the full arbitrary-defined-domain chain (A) is verified with this declared comparison theorem as an accepted external input.
Scalar trace alone would not justify projection comparison in an arbitrary finite algebra; the checks on every central summand are the step that supplies the needed stronger information.
The resulting factorization has bounded V_0 but its second factor may be unbounded, so this supplement adds no bounded-pencil or bounded scalar-division conclusion.
No numerical or proof-assistant verification was used.

## Source and inspection

Source edition: MSY23 / MSY23, the user-supplied 50-page published article in Journal of Functional Analysis 285 (2023), article 110016, DOI 10.1016/j.jfa.2023.110016. Printed pages equal PDF pages. The separate 37-page arXiv v2 was not compared in full; other works retain their own versions and inspection limits in the body.

Passages: Section 5.1, published pp. 28-34 through Remark 5.11; the separately reviewed arbitrary-domain aside after Theorem 5.14 on p. 36. The bounded-border refinement dated 2026-09-09 is a local deduction, not an additional source quotation.

Inspection: 2026-09-08: the main unit was reconstructed and independently reviewed; that review does not cover the later p. 36 supplement. The supplement has its own 2026-09-09 independent review accepting AP18 Propositions 9.1.6 and 9.1.8 and Definition 2.4.3 at the exact recorded locations in the 338-page draft. General affiliated-algebra and projection-comparison foundations were not recursively audited; no new AP18 version date or full-book audit is claimed. The separate bounded-border refinement retains its distinct author/reviewer relationship. No bounded-pencil descent or formal verification is inferred.
