---
author: Yin
---

<a id="den09-u002"></a>
# Den09-U002: determinant approximation, finite sections and marked groups

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Den09, [retained PDF](../../../literature/pdf/Den09.pdf), arXiv:0905.0604v1, 5 May 2009, 25 pages. Only this version's proofs and problem formulations are assessed.

Passages: Sections 2--4 in full, pp.3--23, and references pp.23--25. Complete printed proofs of Lemmas 3/8, Proposition 7/9, Corollaries 10--12/23, Examples 15/16 and Theorems 17/22; all other statements and the stated dependency interfaces in these sections.

Inspection: 2026-10-06, human author Yin; assigned AI source-review agent directly read the passages and self-checked the record, with rendered pp.7,10--11,17--20 inspected for formulas, limsup bars and Question 21. No independent human reviewer or formal verification is asserted. Foundational definitions and Section 1 are recorded in U001.


The distinct original2026-10-07 coordinator reading recorded in [L_G50](../../../ledger/Yin_L_G0050_v1.md) rechecked the Theorem14/Example15 statement on retained printed p12: arbitrary integer specialization vectors, the sup-norm relation parameter and the full polynomial limit including zeros.
That original statement recheck is separate from the2026-10-06 inspection table and does not audit Lawton’s original proof.
The complete current local application is [C_G271](../../../claims/Yin_C_G0271_v1.md#essential-family-measure-obstruction); the present maintenance readback of the original record makes no new PDF-inspection claim.

## Assessment and reuse boundary

**Audited within scope** for the printed finite-section linear algebra, the regularized upper estimate with the surrounding Følner hypotheses, and Theorems 17/22 with their marked-group consequences, using the precise determinant conventions in [Den09-U001](Yin_U001.md#den09-u001).
The Toeplitz limit theorem, the trace approximation underlying Theorem 4, Lawton's full theorem, and the Section 4 external results are accepted or read at the stated interface; their original proofs are not claimed to have been checked.

**Questioned for a proposed affirmative answer to Question 21 with the paper's unmodified determinant.**
The explicit integer group-ring example below gives a negative answer to its literal formulation.
This is a check of source wording, not a claim to have resolved the kernel-discarding determinant-approximation problem.
Theorem 17's invertible case and its general upper bound are unaffected.
The preprint's statements that questions were open are reports of its 2009 context, not assertions of current research status.

<a id="finite-section-determinant"></a>
## Finite sections and Toeplitz approximation

The canonical group trace has $\tau(I)=1$.
For finite nonempty $F\subset\Gamma$, let $i_F:\mathbb CF\to\ell^2\Gamma$ be inclusion, $p_F=i_F^*$ and $A_F=p_FAi_F$.
If $A\ge0$, then $A_F\ge0$.
If also $A$ is injective on the algebraic group ring $\mathbb C\Gamma$, then $A_F$ is positive definite: $\langle A_Fv,v\rangle=\|A^{1/2}v\|^2=0$ implies $Av=0$, hence $v=0$ (Lemma 3).
Injectivity on $\mathbb C\Gamma$ is weaker than bounded invertibility or injectivity on all of $\ell^2\Gamma$.

A right **Følner sequence** is a sequence of finite nonempty subsets $F_n$ with

$$\frac{|F_n\gamma\setminus F_n|}{|F_n|}\longrightarrow0
\quad\text{for each }\gamma\in\Gamma.$$

Theorem 4 assumes $\Gamma$ finitely generated amenable and $A\in\mathcal N\Gamma$ positive and invertible, and states

$$\Delta_{\mathcal N\Gamma}(A)=
\lim_{n\to\infty}(\det A_{F_n})^{1/|F_n|}.$$

The printed proof is a sketch retaining Schick's polynomial-trace approximation: normalized traces of polynomials in $A_{F_n}$ converge to $\tau(P(A))$.
Positive bounded invertibility gives a common compact spectral interval $[c,C]\subset(0,\infty)$ for $A$ and its compressions.
Uniform polynomial approximation of $\log$ on that interval then gives the determinant limit.
This uniform lower bound is the essential applicability check; positivity alone does not supply it.
The original [Den06, Theorem 3.2] and [Sch01] proofs were not reread.

For $A\ge0$ without invertibility, regularization and Theorem 4 give the upper estimate

$$\Delta_{\mathcal N\Gamma}(A)\ge
\limsup_{n\to\infty}(\det A_{F_n})^{1/|F_n|}.$$

Indeed $A_{F_n}+\varepsilon I$ has determinant at least $\det A_{F_n}$, while the regularized limit equals $\Delta(A+\varepsilon I)$, which decreases to $\Delta(A)$.
The displayed symbol in Proposition 7 is a **limsup**, not an asserted limit.
Its standalone wording omits the ambient amenable/Følner assumptions, but the proof explicitly uses them.
They must be carried into reuse.
Question 6 asks for the reverse bound in the noninvertible setting; it is not proved in this version.

For $\Gamma=\mathbb Z$, $F_n=\{0,\ldots,n-1\}$ and symbol $P\ge0$, the compression determinant is the Toeplitz determinant $D_n$ of Fourier coefficients $c_\nu=\int z^{-\nu}P(z)\,d\mu$.
Theorem 1 treats continuous strictly positive $P$.
Theorem 2 retains the stronger classical result for $P\in L^\infty(\mathbb T)$, $P\ge0$, positive on a set of positive measure: every $D_n>0$ and $D_n^{1/n}\to M(P)$, which may be zero.
Positivity follows because a nonzero trigonometric polynomial cannot vanish on that entire positive-measure set; the limit uses [Sim05, Theorem 2.7.14].
Its cited original proof is uninspected.

## Orthogonalization and determinant ratios

For positive $A$ injective on $\mathbb C\Gamma$, define $\langle u,v\rangle_A=\langle Au,v\rangle$ on that algebraic space.
For finite $F\subset F'$, the source's

$$\psi=i_FA_F^{-1}p_FAi_{F'}$$

is the $A$-orthogonal projection from $\mathbb CF'$ onto $\mathbb CF$ (Proposition 9).
Direct inspection verifies $\psi^2=\psi$, its range, and $A$-selfadjointness.
The Schur-complement formula for the block decomposition $\mathbb CF'=\mathbb CF\oplus\mathbb C(F'\setminus F)$ supplies the determinant ratio.
When $F'=F\sqcup\{\gamma\}$ and $\Phi_\gamma=(I-\psi)\delta_\gamma$,

$$\frac{\det A_{F'}}{\det A_F}=\|\Phi_\gamma\|_A^2
=\tau(A)-\langle A_F^{-1}s,s\rangle,
\qquad s=p_FA\delta_\gamma.$$

Thus $0<\|\Phi_\gamma\|_A^2\le\tau(A)$, with equality at the upper bound exactly when $s=0$, equivalently when the new coordinate decouples as a block with diagonal entry $\tau(A)$ (Corollaries 10/11).
Iterating gives the determinant as the product of squared residual norms; each residual is defined relative to the preceding coordinates in the chosen ordering.

Jensen's inequality for the probability spectral measure proves $\Delta(B)\le\|B\|_2$, where $\|B\|_2=\tau(B^*B)^{1/2}$.
Multiplicativity applied to $A^{1/2}B$, with $B=r(\widetilde\Phi_\gamma)$ and coefficient inversion $\widetilde{\ }$ as in U001, gives Corollary 12:

$$\Delta(A)\,\Delta(r(\widetilde\Phi_\gamma))^2
\le\frac{\det A_{F'}}{\det A_F}.$$

The argument and all nonzero denominators were checked.
The classical unit-circle residual-polynomial zero-location result used in Remark 13 is retained from [Sim05], not independently proved here.
The paper does not establish $\Delta(r(\widetilde\Phi_\gamma))\ge1$ for general groups, so that bound cannot be inserted into the noncommutative argument.

<a id="marked-groups"></a>
## Marked groups, kernel convergence and pushforward

A $d$-marked group is a group generated by an ordered $d$-tuple, allowing repetitions, up to isomorphism preserving the tuple.
Convergence in $X_d$ means that every fixed finite collection of words eventually has the same trivial/nontrivial evaluations; equivalently, sufficiently large bounded-radius labelled Cayley balls agree.
Relations are words in formal generator positions, even if marked generators coincide.

For homomorphisms $\varphi_n:\Gamma\to\Gamma_n$, write $K_n\to e$ if each nonidentity $\gamma\in\Gamma$ belongs to only finitely many $K_n=\ker\varphi_n$.
Equivalently $K_n\cap Q\subset\{e\}$ eventually for every finite $Q$.
For surjections from a fixed finitely generated marked group this is precisely convergence of the quotient markings (Example 16).
Neither nesting nor finite-index kernels are necessary.

For a homomorphism $\varphi$, define the contractive unital Banach $*$-algebra map

$$\varphi_*f(\gamma')=\sum_{\gamma\in\varphi^{-1}(\gamma')}f_\gamma,
\qquad\|\varphi_*f\|_1\le\|f\|_1.$$

Absolute summability justifies regrouping.
Surjectivity is unnecessary.
Theorem 17 concerns countable groups, $f\in\ell^1\Gamma$ and $f_n=\varphi_{n*}f$.
If $K_n\to e$, then

$$\Delta_\Gamma(f)\ge\limsup_n\Delta_{\Gamma_n}(f_n).$$

If **$f$ is invertible in the Banach algebra $\ell^1\Gamma$**, then

$$\Delta_\Gamma(f)=\lim_n\Delta_{\Gamma_n}(f_n).$$

No amenability assumption enters this theorem.
Mere nonzeroness, injectivity of $r(f)$ or bounded invertibility in $\mathcal N\Gamma$ is not the asserted substitute for $\ell^1$-invertibility.
The source discusses settings with inverse-closed $\ell^1$ algebras, such as virtually nilpotent groups, using retained external Wiener/symmetry theorems; those original proofs were not checked.

## Inspected proof of Theorem 17 and its extension

For every $g\in\ell^1\Gamma$,

$$\tau_{\Gamma_n}(g_n)=\sum_{\gamma\in K_n}g_\gamma\longrightarrow g_e
=\tau_\Gamma(g).$$

To verify this, choose a finite set outside which the $\ell^1$ tail is below $\varepsilon$, then use eventual kernel avoidance on that set.
Apply this also to each polynomial in $f$.
For a general, possibly nonnormal $f$, first replace it by $f^*f$ and use $\Delta(f^*f)=\Delta(f)^2$; $*$-pushforward preserves this replacement.
This avoids assuming arbitrary complex spectra lie on the real axis.

In the invertible case, pushforward preserves inverses and bounds their norms by $\|f^{-1}\|_1$.
After the positive reduction, the spectra of all operators lie in one compact interval separated from zero.
Polynomial approximation of $\log$, trace convergence and the common approximation error establish equality.
The inverse is required in the original $\ell^1$ algebra precisely to get a uniform lower bound across the different quotient operators.

Without invertibility, the spectra still have a common upper bound.
The source constructs decreasing polynomial majorants $P_k\downarrow\log$ on that compact interval, with value tending to $-\infty$ at zero: continuous cutoffs $\varphi_k(x)=1/k+\log\max\{x,1/k\}$ are separated uniformly from $\varphi_{k+1}$, so Weierstrass approximation places $P_k$ strictly between them.
Spectral monotone convergence gives $\tau(P_k(f))\downarrow\log\Delta(f)$.
For every fixed $k$, this majorizes the limsup of the quotient logarithmic determinants.
Taking $k\to\infty$ proves the bound, including determinant zero.
The expressions $\tau(\log f_n)$ here mean extended spectral integrals, not necessarily traces of bounded logarithm operators.

Theorem 22 replaces the maps by a fixed common covering group $\Gamma\leftarrow\widetilde\Gamma\to\Gamma_n$, with kernels $K,K_n$.
Assume membership in $K_n$ eventually agrees with membership in $K$ for every group element.
For $\widetilde f\in\ell^1\widetilde\Gamma$, put $f=\varphi_*\widetilde f$ and $f_n=\varphi_{n*}\widetilde f$.
Then the same limsup inequality holds, and equality holds if **the common lift $\widetilde f$ is invertible in $\ell^1\widetilde\Gamma$**.
The trace difference is bounded by $\sum_{\gamma\in K\triangle K_n}|\widetilde f_\gamma|$, reducing the proof to the same finite-tail argument.
The proof's real spectral intervals must be read after replacing the common lift by $\widetilde f^*\widetilde f$.

For finitely generated common groups and surjections, kernel convergence is equivalent to marked-group convergence (Corollary 23).
Taking the common group to be the free group $F_d$ gives Corollary 24: the trace function on $X_d$ associated with any fixed $\widetilde f\in\ell^1F_d$ is continuous; its determinant function is continuous for a fixed **invertible** $\widetilde f$.
No assertion of continuity for an arbitrary varying element, or merely an invertible image in one quotient, follows.

## Specializations and remaining source reports

| Passage | Exact statement/use and retained boundary |
| --- | --- |
| Theorem 14; Example 15 | For a Laurent polynomial $P$ in $d$ variables and $P_r(z)=P(z^{r_1},\ldots,z^{r_d})$, Lawton gives $M(P_r)\to M(P)$ as $q(r)=\min\{\|\nu\|_\infty:0\ne\nu\in\mathbb Z^d,\nu\cdot r=0\}\to\infty$ (empty minimum interpreted as infinity). The checked relation argument shows $(\gcd(r_1,\ldots,r_d)\mathbb Z,r_1,\ldots,r_d)\to(\mathbb Z^d,e_1,\ldots,e_d)$. The original Lawton proof, including its control near zeros, is retained rather than audited. |
| Example 19 | For countable residually finite $\Gamma$ and finite-index normal $K_n\to e$, Theorem 17 gives $\Delta_\Gamma(f)=\lim\lvert\det r(f_n)\rvert^{1/\lvert\Gamma/K_n\rvert}$ for $f\in(\ell^1\Gamma)^\times$. The normalization follows from the finite-group canonical trace. |
| Example 20 | For a continuous torus function with absolutely summable Fourier coefficients and no zeros, Wiener's theorem gives an invertible $\ell^1\mathbb Z^d$ element, so the preceding result recovers the nonvanishing case of Lawton. The full theorem for polynomials with zeros uses the separately retained Lawton input. |
| Section 4, pp.21--23 | The source discusses determinant lower bounds for suitable integer group-ring operators, classification of determinant-one elements, positivity for certain nonunits, and continuity in a complex parameter. These are source-reported results/questions; their external entropy, direct-finiteness and zero-divisor proofs were not reviewed. The nonzero-kernel exclusion for applying the unmodified determinant is essential. |
| Theorem 27 and Brown-potential paragraph | The source cites Boyd for continuity of $z\mapsto M(z-P)$ for Laurent-polynomial $P$. It cites Brown for subharmonicity of $z\mapsto\log\Delta(z-A)$; hence upper semicontinuity, with ordinary continuity off the Brown-measure support. These cited original proofs were not checked. The paragraph does not prove global continuity of $z\mapsto\Delta(z-A)$ for arbitrary bounded $A$. |

<a id="question21-counterexample"></a>
## Finding F1 — P2: Question 21 has a negative answer as literally formulated

**Substantive convention obstruction; v1 pp.18--19, first recorded here on 2026-10-06.**
Question 21 asks for the equality in Theorem 17 for arbitrary $f\in\mathbb Z\Gamma$, even without $\ell^1$-invertibility, when $K_n\to e$.
The determinant defined on p.2 includes zero spectral mass.
The p.18 remark explicitly distinguishes Lück's modified determinant that discards the zero eigenspace; it does not redefine the paper's determinant.

Let $\Gamma=\mathbb Z=\langle t\rangle$, let $\Gamma_n=\mathbb Z/n\mathbb Z$ via the quotient maps, and take $f=1-t\in\mathbb Z\Gamma$.
Then $K_n=n\mathbb Z\to0$, and the Mahler identity/Jensen formula gives

$$\Delta_{\mathcal N\mathbb Z}(1-t)=M(1-z)=1.$$

For every $n$, the nonzero constant vector in $\mathbb C[\Gamma_n]$ is killed by $r(f_n)=I-r(t_n)$.
Thus

$$\Delta_{\mathcal N\Gamma_n}(f_n)=|\det(I-r(t_n))|^{1/n}=0,$$

so the proposed equality is $1=\lim_n0$, which is false.
The infinite-group operator itself is injective on $\ell^2\mathbb Z$, because multiplication by $1-z$ vanishes only on a Haar-null set.
Thus adding injectivity only for the limiting operator would not fix the question.

This also shows why the preceding all-$f$ discussion of finite periodic-point counts needs a hypothesis ruling out the relevant roots of unity or a changed invariant.
The identity toral automorphism corresponding to $1-z$ has infinitely many fixed points, so its fixed-point count is not the zero finite determinant.
The note does not inspect the original [Lin84] or [Sch95] statements and does not attribute their omission to those sources.

**Recommendation for reuse:** retain Theorem 17's $\ell^1$-invertible version.
A kernel-discarding approximation question must be formulated with a different determinant on each finite quotient and checked separately.
In this example the product of the nonzero singular values of $I-r(t_n)$ is $n$, so its modified normalized determinant is $n^{1/n}\to1$; this illustrates exactly the convention difference.
No general modified-determinant theorem is inferred from the example.

## Finding F2 — P3: a multiplicative identity is mistyped in Theorem 17's proof

**Local algebraic typo; p.17, first line.**
The printed identity is $2\det_{\mathcal N\Gamma}f=\det_{\mathcal N\Gamma}(f^*f)$.
It already fails for $f=I$, with left side $2$ and right side $1$.
Replace it by $\det(f)^2=\det(f^*f)$, or by $2\log\det(f)=\log\det(f^*f)$ in the extended logarithmic form.
The proof's positive reduction uses precisely the corrected multiplicative identity and is otherwise valid at this step.

## Scope qualifications needed for the finite-section statements

**Proposition 7, p.7:** the sequence must be Følner in the surrounding amenable setting.
Dropping this condition makes the bound false even in $\mathbb Z$: for $A=3I-r(t)-r(t)^{*}>0$ and the constant singleton sequence $F_n=\{e\}$, the finite-section determinant is $3$, but $\Delta(A)=(3+\sqrt5)/2<3$ by the one-variable Mahler formula.
This is a hypothesis clarification of a statement that inherits its context, not a refutation under its intended Følner assumptions.

**Example 5, p.7:** obtaining the measurable version from Theorem 4 requires an essential positive lower bound.
Pointwise strict positivity of a bounded measurable $P$ alone does not ensure invertibility of its multiplication operator: take $P(z)=|1-z|$ away from $z=1$ and define $P(1)=1$.
The broader Szegő conclusion remains supplied by Theorem 2, but cannot be deduced from Theorem 4 without the lower bound.
The isolated “question 5” reference following Question 6 points to Question 6.

## Coverage and downstream effects

All Section 2--4 text and printed proofs were read; the equations and counterexample-sensitive passages were checked visually.
The core finite-dimensional linear algebra and the trace/polynomial proofs of Theorems 17/22 were examined directly, with exact hypotheses and singular limits exposed above.
Externally cited proofs were not recursively audited, and the journal version has not inherited this proof review.

F1 prevents any consumer from using the literal proposed Question 21 extension with ordinary determinants; F2 requires the displayed algebraic correction.
These findings do not weaken the checked invertible approximation or marked-group continuity statements.
No project Claim or Task is changed, and no current answer to the other source-dated research questions is asserted.

### Additional targeted review, 2026-10-06

A separate assigned AI reviewer read these draft findings, then rechecked the source definitions and rendered pp.2,18--19, and independently recomputed the cyclic-quotient example and trace factors.
The coordinator also read both units and independently checked the key examples.
This is targeted scrutiny with the proposed finding supplied, not a blind or second full-paper review.

**F3 — P3, p.18, final display:** the finite-dimensional logarithm needs an absolute value around the ordinary determinant, as already used in the paper's equation (6).
For example, take the integer Laurent polynomial f(t)=t^2-3t+1, with reciprocal roots a=(3+sqrt(5))/2 and a^-1.
Its determinant on the n-cycle is (a^n-1)(a^-n-1), which is negative for every n.
Thus the real logarithm of that determinant is undefined, while the logarithm of its absolute value is correct.
This source-existing omission was located during the targeted review; all finite-group formulas retained above already use the absolute value.
The repair is separate from the zero-kernel obstruction in F1.
