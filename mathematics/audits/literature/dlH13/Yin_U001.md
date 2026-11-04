---
author: Yin
---

<a id="dlh13-u001"></a>
# dlH13-U001: Whitehead Torsion and the Determinant with Kernel Removed

## Source and inspection

Source edition: Pierre de la Harpe, *The Fuglede-Kadison determinant, theme and variations*, arXiv:1107.1059v2, dated 7 July 2012, 30 pages; [retained PDF](../../../literature/pdf/dlH13.pdf). No transfer of these findings to an uninspected journal edition is implied.

Passages: Complete Sections 7–8, printed/PDF pp. 21–26; especially the basis convention and (23)–(26), p. 22; analytic torsion display (27), p. 25; singular determinant (28), p. 25; and L2-torsion display (29), p. 26.

Inspection: 2026-10-06, agent working for the bound author Yin; all assigned text read, the displayed algebraic constructions and spectral formula checked, and rendered PDF pp. 22, 25, and 26 inspected. Explicit finite-dimensional tests check the basis/sign and additive/multiplicative defects. Original proofs of the cited topological invariance, s-cobordism, analytic torsion, and L2 determinant theorems are not audited. This is self-review, with no formal-verification or independent-review claim.


Coverage: **Questioned for the incompatible torsion conventions and the literal displays identified below; the distinction between the two singular determinants is checked within scope.**
Sections 7–8 are an introductory survey, and their references to “appropriate hypotheses” do not provide a complete analytic-torsion theorem ready for direct application.

## Algebraic torsion: data and conventions

<a id="dlh13-whitehead-torsion"></a>
Section 7.1 assumes a unital ring $R$ with invariant basis number: two finite free modules of different ranks are not isomorphic.
Take a bounded complex of finite free $R$-modules

\[
0\longrightarrow C_n\xrightarrow{d_n}C_{n-1}\longrightarrow\cdots
\xrightarrow{d_1}C_0\longrightarrow0,
\]

whose homology modules $H_i$ are free, together with bases $c_i$ of the chain modules and bases $h_i$ of the homology.
If each boundary module $B_i=\operatorname{im}d_{i+1}$ is free with basis $b_i$, lift $h_i$ into cycles and $b_{i-1}$ into $C_i$ to obtain a basis denoted $b_i h_i b_{i-1}$.
Equation (24) forms the alternating sum of its transition classes relative to $c_i$ in $\overline K_1(R)$.

Changing lifts gives block triangular elementary transitions; changing a boundary basis contributes in two adjacent degrees with opposite signs.
This explains the independence from those auxiliary choices.
Homology bases and chain bases are part of the input, not disposable choices.
If the $B_i$ are not free, the cited extension uses stable freeness.
The basic splitting mechanism can be checked inductively: $C_0\to H_0$ splits, and the exact sequences with $H_i$ and already projective $B_{i-1}$ split at each successive degree.
The stable-free extension of the torsion invariant itself remains a cited construction from Miln–66.

When the complex is acyclic, the same splittings give a chain contraction $\delta$ with $d\delta+\delta d=1$.
The map

\[
(d+\delta)|_{\rm odd}:C_{\rm odd}\longrightarrow C_{\rm even}
\]

is invertible.
For a chosen contraction with $\delta^2=0$, its inverse is the even part of $d+\delta$.
More generally, $(d+\delta)^2=1+\delta^2$ is invertible because $\delta^2$ raises degree and is nilpotent in a bounded complex.
The source's equality between its class and Equation (24) has the basis-convention problem detailed below; the existence of this isomorphism is unaffected.

Section 7.2 applies this to a finite connected CW-pair $(K,L)$ with $L$ a deformation retract of $K$.
Write $\Gamma=\pi_1(L)\cong\pi_1(K)$.
The acyclic relative cellular complex of their compatible universal covers is finite free over $\mathbb Z[\Gamma]$.
Orienting cells and choosing one lift of each cell of $K\setminus L$ gives bases.
Changes of orientation/lift contribute classes of $\pm\gamma$, so the quotient

\[
\operatorname{Wh}(\Gamma)=K_1(\mathbb Z[\Gamma])/\langle\pm1,\Gamma\rangle
\]

removes those changes.
The source's sentence naming $\widetilde K,\widetilde L$ reverses the names of the covered spaces once on p. 23; the relative complex and the definitions require $\widetilde K$ to cover $K$ and $\widetilde L$ to cover $L$.

The geometric invariance and classification statements were read with their actual scope:

- Topological invariance of Whitehead torsion is cited to Chap–74, not proved in the survey.
- The realization/classification of smooth h-cobordisms uses a closed incoming manifold of dimension at least $5$, equivalently cobordism dimension at least $6$.
  The standard compact smooth h-cobordism and relative-boundary setting is required; it is not a classification of arbitrary noncompact cobordisms.
- The s-cobordism statement is relative to the incoming boundary and has the same dimension restriction.
  Its simply connected specialization uses $\operatorname{Wh}(1)=0$.
- The homotopy-sphere discussion is a reported application and historical account.
  The original topology proofs and lower-dimensional Poincare results were not re-audited.

## Reidemeister torsion and the analytic formula boundary

Section 7.4 uses a representation $h:\Gamma\to\operatorname{GL}_k(\mathbb R)$ to map $K_1(\mathbb Z[\Gamma])$ to $K_1(\mathbb R)\cong\mathbb R^*$, then to reduced $\overline K_1(\mathbb R)\cong\mathbb R_{>0}$ by absolute determinant.
For an orthogonal representation, $|\det h(\gamma)|=1$ for every $\gamma$, so the map factors through $\operatorname{Wh}(\Gamma)$.
The positive number called $\tau_h(C)$ in that paragraph is multiplicative torsion.

For a finite-dimensional acyclic real Hilbert chain complex with orthonormal chain bases, let $s_k$ be the product of the nonzero singular values of $d_k$, with empty product $1$.
With the **literal inverse transition convention of Equation (24)** explained in the finding below, direct linear algebra gives

\[
\log\tau_h(C)=\sum_k(-1)^k\log s_k
=\frac12\sum_k(-1)^k\log\det{}'(d_k^*d_k)
=\frac12\sum_k(-1)^k k\log\det{}'(L_k),
\]

where $L_k=d_k^*d_k+d_{k+1}d_{k+1}^*$ and the prime omits zero eigenvalues.
Indeed the orthogonal boundary decomposition makes the positive spectrum of $L_k$ the union of the positive spectra of $d_k^*d_k$ and $d_{k+1}^*d_{k+1}$; adjacent coefficients then telescope.
This checks the relative sign of the **two right-hand sums** in (27).
Choosing the reciprocal convention for multiplicative torsion negates both logarithmic sums.

This finite-dimensional calculation is not an analytic torsion theorem for differential forms.
For a compact Riemannian manifold with a suitable flat metric bundle, a de Rham complex is infinite dimensional, the relevant determinant is a reduced zeta-regularized spectral determinant, and homology/harmonic data and boundary conditions have to be specified.
The survey does not spell out these hypotheses at (27), and this unit does not infer them or claim a proof of analytic/combinatorial torsion equality from its citation to RaSi–71.
The zero-removal and logarithm corrections below are needed even before that analytic interface can be used.

## The singular determinant that omits the kernel

<a id="dlh13-kernel-removed-determinant"></a>
Use a finite von Neumann algebra $\mathcal N$ with a finite positive normal trace $\tau$ (faithful in the standard faithful-trace realization).
Let $x\in\mathcal N$ be bounded, $|x|=(x^*x)^{1/2}$, and $\nu_x(B)=\tau(1_B(|x|))$.
Equation (28) is

\[
\det{}^{\rm FKL}_\tau(x)
=\exp\left(\int_{(0,\infty)}\log\lambda\,d\nu_x(\lambda)\right),
\]

where an integral of $-\infty$ gives determinant $0$.
The lower endpoint is **$0^+$**, so any atom at $0$ is excluded.
Since $x$ is bounded and the trace finite, the positive part of this logarithmic integral is finite; only the negative part can diverge.
This determinant does not condition the spectral distribution to have total mass $1$ after removing the kernel.

This must be distinguished from the analytic extension $\det{}^{\rm FK}_\tau$ in Section 3, which includes the zero spectral mass and vanishes when a nonzero kernel projection has positive trace.
In particular:

| Operator, with a faithful trace | Analytic FK extension | Kernel-removed FKL extension |
| --- | --- | --- |
| Invertible $x$ | $\exp(\tau(\log\lvert x\rvert))$ | The same value. |
| Projection $p\ne1$ | $0$ if its complementary projection is nonzero | $1$, since every nonzero singular value is $1$. |
| Zero operator | $0$ on a nonzero traced space | $1$, the exponential of the empty integral. |
| $\operatorname{diag}(x,0)$, $x$ invertible | $0$ | $\det{}^{\rm FK}_\tau(x)$ with the unnormalized matrix-trace extension. |

For matrices the last identity uses $\tau_2=\operatorname{Tr}_2\otimes\tau$, as in Section 6.
If one independently normalized the matrix trace by $1/2$, the nonzero block contribution would instead be raised to the power $1/2$.
The source's same-symbol use of $\tau$ does not authorize switching between these normalizations.

For a finite-dimensional operator with the ordinary trace, $\det{}^{\rm FKL}$ is the product of **nonzero** singular values.
It is not the ordinary determinant of a singular matrix.
On a corner or a finitely generated projective Hilbert module, inherit the ambient unnormalized trace rather than renormalizing the support projection.
Determinant class means that the logarithmic integral over positive spectral values is finite, equivalently $\det{}^{\rm FKL}>0$; nontrivial kernel does not by itself violate determinant class.

The source reports from Luck–02, Theorem 3.14, multiplicativity when $x$ is injective and $y$ has dense image.
These exact hypotheses must be preserved.
Multiplicativity is not automatic for arbitrary singular operators: with the ordinary trace in $M_2(\mathbb C)$, let $p$ project onto $e_1$ and $q$ project onto $(e_1+e_2)/\sqrt2$.
Then

\[
\det{}^{\rm FKL}(p)=\det{}^{\rm FKL}(q)=1,
\qquad
\det{}^{\rm FKL}(pq)=2^{-1/2}.
\]

The last value is the single nonzero singular value of $pq$.
This explicit calculation checks why an unrestricted multiplication rule cannot be borrowed from the invertible FK determinant.
The original general multiplicativity theorem is retained as cited, not re-proved here.

## L2-torsion: exact data needed for Equation (29)

<a id="dlh13-l2-torsion"></a>
Section 8.2 considers a bounded complex of finitely generated projective modules, interpreted with the Hilbert $\mathcal N$-module structures required to form adjoints, spectral projections, and closures of images.
Its hypotheses are:

1. The chain modules have finite von Neumann dimension and the differentials are bounded adjointable module maps.
2. The complex is weakly acyclic: $\overline{\operatorname{im}d_j}=\ker d_{j-1}$ for every $j$.
   Ordinary algebraic exactness or closed range is not required.
3. Every differential has determinant class with the kernel omitted, using the module trace just described.

Reading the dummy index in (29) consistently as $k$, the source's convention is

\[
\rho^{(2)}_{\rm source}(C)
=\sum_{k=0}^n(-1)^k\log\det{}^{\rm FKL}_\tau(|d_k|)
=\frac12\sum_{k=0}^n(-1)^k\log\det{}^{\rm FKL}_\tau(d_k^*d_k).
\]

The second equality follows from the spectral substitution $\lambda\mapsto\lambda^2$ and uses the same support and trace in both terms.
Under the finite, determinant-class assumptions just stated, every logarithm is finite and the sum lies in $\mathbb R$.
The larger codomain $\{-\infty\}\sqcup\mathbb R$ printed in (29) is unnecessary under those assumptions; it must not be used to license arbitrary non-determinant-class complexes, where signs can produce $+\infty$ or an undefined combination of infinities.

Keep the displayed source sign separate from other authors' conventions until the exact comparison has been checked.
The source itself has the (24)/(26) inversion inconsistency below, so its pointer to an L2 analogue of (26) does not settle that sign.
Section 8.3 is expressly speculation about future singular extensions of Banach-algebra determinants, not an existence theorem for such extensions.

## Actionable findings in the inspected artifact

Every item here is newly recorded in this audit and pre-existing in arXiv v2; the cited locations were checked in rendered pages.

### P2 — Basis-change convention and the contraction formula disagree (p. 22)

The opening definition denotes by $[b/a]$ the class of $x$ with $a_j=\sum_kx_{jk}b_k$.
This is the inverse of the convention that expresses the new basis $b$ in the old basis $a$.
Under the printed convention, consider the acyclic based complex

\[
0\longrightarrow\mathbb R\xrightarrow{\;2\;}\mathbb R\longrightarrow0,
\qquad c_1=c_0=(1).
\]

Choose $b_0=(1)$ and lift it to $(1/2)$ in $C_1$.
In degree zero the transition class is zero.
In degree one, $[\,(1/2)/(1)\,]$ is the class of $2$, since $1=2(1/2)$.
Equation (24) therefore gives $-[2]=[1/2]\in\overline K_1(\mathbb R)$.
But the ordinary matrix of $(d+\delta)|_{\rm odd}:C_1\to C_0$ is $[2]$, as asserted in (26).
These classes differ, since their absolute determinants are $1/2$ and $2$.

For reuse, either reverse the initial transition-matrix convention and retain (26), or retain that initial convention and put a minus sign in front of the class in (26).
State which convention is chosen throughout the torsion-to-determinant comparison.
This is a concrete inconsistency between the displayed conventions, not a refutation of the underlying Whitehead torsion theorem.

### P2 — Equation (27) identifies positive torsion with its logarithmic expression (p. 25)

Section 7.4 defines $\tau_h(C)\in\mathbb R_{>0}$, but (27) sets it equal to sums of logarithms.
Even the unit acyclic complex $0\to\mathbb R\xrightarrow{1}\mathbb R\to0$ has multiplicative torsion $1$ and logarithmic expression $0$.
Thus the left side must be $\log\tau_h(C)$, or the right side must be exponentiated, after fixing the overall sign convention.

The determinants in (27) also need a convention that removes zero modes; $d_k^*d_k$ is usually singular in a complex, even when the complex is acyclic.
For finite-dimensional complexes the primed formulas above are explicit.
In the analytic de Rham setting, an appropriately defined reduced regularized determinant and full theorem hypotheses are required.
A bare ordinary infinite-dimensional determinant is not supplied by the survey.
The two right-hand alternating sums have the same sign with the displayed lowering differential convention, so no additional relative-sign error is alleged there.

### P3 — Equation (29) uses an unbound differential index (p. 26)

The sum is indexed by $k$, but its summand contains $(d_j^*d_j)^{1/2}$.
Replace both occurrences of $j$ by $k$.
If read with a fixed $j$, the expression would repeatedly count one differential and would not define torsion of the complex.
This index repair does not resolve the separate global sign convention discussed above.

## External inputs and actual review boundary

| Passage/input | Inspected here | Not supplied by this inspection |
| --- | --- | --- |
| Miln–66 / Cohe–73, Sections 7.1–7.2 | The survey's data, basis/lift mechanism, and explicit contraction interface; finite scalar counterexample to their printed convention match. | Original stable-free torsion construction and all geometric/algebraic equivalence proofs. |
| Chap–74, Kerv–65, Smal–61/62 and related topology | Statements and dimension/relative-boundary scope as reported in the survey. | Original proofs of topological invariance, h-/s-cobordism, sphere classification, or low-dimensional topology. |
| RaSi–71 and the analytic-torsion passage | The need for logarithm, reduced spectrum, and analytic regularization; finite-dimensional determinant identity checked directly. | A verified full analytic/combinatorial torsion equality theorem under specified manifold, bundle, boundary, and homology hypotheses. |
| Luck–02, Theorem 3.14 and Section 3.3.2 | The singular determinant definition and the exact multiplicativity hypotheses reported by dlH13; elementary matrix checks and trace conventions. | Original general multiplicativity proof, exact original torsion sign normalization, or general L2-topological invariance results. |

On 2026-10-06 a bounded search for “Lück Definition 3.29 torsion determinant” located a university-hosted copy of the cited book and related primary-source leads.
It was not acquired/read as a separate audited artifact by this unit; search snippets are not used to assert an original-book convention.
The current record stops at the direct internal consistency checks and leaves that exact external sign comparison explicit rather than recursively auditing the cited book.
The coordinating [source record](readme.md) owns the acquisition and edition history.

No project Claim or Task is selected here.
The reusable output is the kernel-removal/normalization distinction, the exact finite and weak-acyclicity assumptions, and the located convention failures.
Neither the singular determinant definition nor the topological survey paragraphs alone prove a Brown-measure, entropy, or manifold-volume formula.
