---
author: Yin
---

# G0001 Citation Applications

The current TeX under `progress/` is authoritative for the citation uses recorded here.
The mapped document is the 11 October 2026 English progress report entered through `progress/main.tex`; its five section files are `overview.tex`, `entropy.tex`, `growth.tex`, `determinants.tex` and `arithmetic.tex`.
The current source contains 23 citation commands and 12 canonical keys, all covered below; grouped citations have a separate row under each cited work.
Each row is one source-specific use in the current TeX, not an inventory of consulted works or uncited bibliography entries.

The canonical bibliography `mathematics/literature/references.bib` owns bibliographic fields and persisted keys.
The linked source units own source statements, inspected editions, proof-inspection limits and located corrections; this map does not copy them or substitute for them.
The [editorial source map](progress/source-map.md) owns the project's strategy and responsible-mathematics correspondence, and the [manuscript review](progress/review.md) owns its recorded review scope.
This map keeps only the forward manuscript applications: what each citation supports in this report, why the source setting and normalization match, what it does not support, and any unresolved evidence point.

The report's recorded Task pause belongs to its historical scope; this map adds no mathematical result, source audit, review or Task resumption.

## `ABR01`

Source evidence: the [selected Poisson attribution](../../../audits/literature/ABR01/readme.md#selected-poisson-attribution) records the inspection of printed pp.12--15 / PDF pp.20--23 of the retained author edition, including formulas 1.15--1.16, Theorem 1.17, Proposition 1.20 and Theorem 1.21.
It records that on the unit disk the Poisson kernel is positive with total mass one and reproduces continuous harmonic functions from boundary data, and that this is a classical-method attribution rather than a whole-book audit.
The polynomial square majorant, exterior-root reversal, signed autocorrelation and arithmetic bundle application remain proved in the report.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/arithmetic.tex`, Section 5.1.3, "Angular control and signed auxiliary bundles", proof of Theorem `ar:bundle-bound` | `\cite[Chapter~1]{ABR01}` | Owns the normalization and reproduction property of the disk Poisson kernel used to obtain the polynomial majorant (equation `ar:poisson-square`): \(K_r\) is a positive probability kernel with Fourier coefficients \(r^{|h|}\), so \(|F(rz)|^2\le E_F+2\operatorname{Re}\sum_{h=1}^T A_h(F)r^hz^h\) for the report's polynomial \(F\). The setting matches the unit disk, the \(0\le r\le1\), \(|z|=1\) convention, and the source's positive unit-mass kernel. Limits: this is a chapter-level method/terminology attribution; the recorded inspection covers the selected printed pp.12--15 / PDF pp.20--23 (Poisson-kernel positivity, total mass one and reproduction of boundary data), and the rest of Chapter 1 was not separately inspected. No general subharmonic theorem, arithmetic-projection result or other Chapter 1 content is attributed to the source. |

## `BV04`

Source evidence: the [bounded weak-duality attribution](../../../audits/literature/BV04/readme.md#selected-weak-duality-attribution) records Section 5.1.3, printed p.216 / PDF p.230, equation (5.2) with its complete displayed proof, together with the Lagrangian definitions from Sections 5.1.1--5.1.2.
It records that each feasible dual lower bound lies below every feasible primal objective for nonnegative inequality multipliers and unrestricted equality multipliers, that convexity is not required, and that no strong duality, attainment or solver claim is adopted.
The [BV04 scope note](../../../audits/literature/BV04/Yin_U002.md#scope-and-actual-inspection) records Appendix A.5.5, printed pp.650--651 / PDF pp.664--665, deriving Schur elimination of a variable from a quadratic form, with the sign fixed by the negative Hessian in that variable, and states that positivity and global conclusions need separate argument.
The report proves its block-determinant calculation and finite weak-duality inequality locally.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/entropy.tex`, Section 2.2.3, "Changing the bulk: neutral cells still have costly couplings", derivation of equation `str:closed` | `\cite[Appendix~A.5.5]{BV04}` | Attributes the Schur-complement block-elimination method illustrated by the source's quadratic-form calculation. The report eliminates the whole endpoint-path block of a matrix pencil over \(\mathbb Q(t)\), obtaining the reduced block determinant with factor \(C_k\), and retains a polynomial identity after clearing denominators. No maximizing variable or negative-Hessian hypothesis is imposed on this pencil. Limits: the retained source inspection concerns quadratic forms; the report supplies its own algebraic calculation, including signs, corner terms and denominator restoration, rather than importing an optimization theorem or a source theorem over \(\mathbb Q(t)\). |
| `progress/sections/arithmetic.tex`, Section 5.1.5, "Finite optimization: true surplus and sufficient budgets", paragraph after the proof of Proposition `ar:finite-certificate` | `\cite[Section~5.1.3, equation~(5.2)]{BV04}` | Attributes the elementary weak-duality principle: each feasible dual objective is a lower bound for every primal feasible value. The setting matches the standard-form inequality/equality structure with unrestricted equality multipliers; the report constructs its own rational witnesses and checks feasibility, the objective equality and the rejected lag-9 dual locally. Limits: no convexity, strong duality, attainment, simplex correctness, solver termination or floating-point certificate is adopted; failure to find witnesses proves no obstruction. The visible locator is the inspected Section 5.1.3, printed p.216 / PDF p.230, equation (5.2) and its proof; the broader printed Section 5.2 was not separately inspected and is not attributed. |

## `BV20`

Source evidence: [BV20-U001](../../../audits/literature/BV20/Yin_U001.md#bv20-u001) records the inspected arXiv:1510.04043v4 (23 April 2021) Theorem 5, pp.3--4: there is an absolute \(c_0>0\) with \(c_0\min\{1,\log_2M_\lambda\}\le h_\lambda\le\min\{1,\log_2M_\lambda\}\) for every algebraic \(\lambda\), with the fair-sign entropy rate \(h_\lambda\), and records Remark 6's algebraic-unit hypothesis and digit-law scope.
The published article is *J. Anal. Math.* 140 (2020), 443--481; the unit concerns v4, not automatically the journal bytes.
[BV20-U003](../../../audits/literature/BV20/Yin_U003.md#bv20-u003) records Conjecture 3 and Theorem 4, pp.2--3, and the complete Section 4, pp.23--30, for the qualitative growth-gap/Lehmer reduction, retaining the uniform-Tits and Jordan structural inputs.
The definition registration for finite-walk entropy and support rates is [BV20-U001 entropy conventions](../../../definitions/index.md#group-growth-and-bernoulli-entropy).

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/growth.tex`, Section 3, paragraph after Proposition `gr:gap-equivalence` | `\citet[Theorem~4]{BV20}` | Supports the structural reduction identifying \(\mathfrak L>0\) with a fixed-\(r\) uniform exponential growth gap: for each fixed \(r\ge1\) there is \(\delta_r>0\) such that every nonempty finite \(S\subset GL_r(\mathbb C)\) satisfies \(\rho(S)=0\) or \(\rho(S)\ge\delta_r\). The setting matches complex linear groups at fixed matrix dimension and the source's subgroup/finite-set quantifiers; the source's Mahler constant \(M_\lambda\) converts to the report's \(\mathfrak L\), and its eigenrate to the report's word-growth rate \(\rho(S)\). Limits: the equivalence is qualitative; the retained external structural inputs are not re-audited and no effective constant is claimed. |
| `progress/sections/growth.tex`, Section 3, paragraph after Proposition `gr:entropy-comparison` | `\cite[Theorem~5]{BV20}` | Supports the lower bound \(c\min\{m,\log2\}\le h_1\) for the report's binary rates. The setting matches Theorem 5's every-algebraic-\(\lambda\) scope; the report replaces fair signs by binary digits using an invertible affine transformation so the fibers are the same, and converts the source's base-2 logarithmic normalization \(\log_2M_\lambda\) to the report's natural-log \(m\) and rate \(h_1\). Limits: the source constant is absolute but not explicit, and the report states its own unspecified absolute \(c\); no numerical constant, positivity lower bound or unit-only scope is transferred from Remark 6. |

## `DGB16`

Source evidence: [DGB16-U001](../../../audits/literature/DGB16/Yin_U001.md#dgb16-u001) records the finite-subset entropy conventions and Sections 2--4: nonempty finite subsets, natural logarithms, directed-union Proposition 2.8(c), and the located corrections to literal statements.
[DGB16-U002](../../../audits/literature/DGB16/Yin_U002.md#dgb16-u002) records Theorem 1.1 and Section 5's Addition Theorem, including the directed-continuity and direct-product addition interfaces used here, over the retained external inputs.
[DGB16-U004](../../../audits/literature/DGB16/Yin_U004.md#dgb16-u004) records Theorems 1.5 and 1.7, Definition 1.6 and the Mahler normalization, together with the located source corrections that must accompany reuse.
The corresponding definitions are registered at [algebraic entropy and flows](../../../definitions/index.md#algebraic-entropy-and-flows).

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/entropy.tex`, Section 2, paragraph after Definition `fo:algebraic-entropy` | `\citet{DGB16}` | Adopts the finite-subset algebraic entropy convention \(h_{\rm alg}(\phi)=\sup_F H(\phi,F)\) over nonempty finite sets \(F\), which need not be subgroups. The setting matches discrete abelian groups and the report's discrete ring \(\mathcal O=\Z[\alpha]\), and the natural logarithms match. Limits: this is a convention attribution; the source's corrected literal assertions (torsion/integrality issues recorded in DGB16-U001) are not imported here. |
| `progress/sections/entropy.tex`, Proposition `fo:entropy-bridge` statement | `\cite[Theorem~1.5]{DGB16}` | Supports the equality of the positive entropy infimum over all abelian groups and endomorphisms with the Mahler-gap constant \(\mathfrak L\) (equation `fo:gap`). The source normalization \(m(f)=\log|a_n|+\sum_{|\alpha_i|>1}\log|\alpha_i|\) matches the report's total Mahler measure, and the infimum statement rather than value-set equality is the one used. Limits: the source proof's external spectral input is retained as reported; the theorem is used only with the corrections recorded nearby in DGB16-U004. |
| `progress/sections/entropy.tex`, Proposition `fo:attainment-implication` statement | `\cite[Theorem~1.7]{DGB16}` | Supports: if \(\mathfrak L>0\), every discrete abelian flow of finite algebraic entropy admits a nonempty finite \(F\subset G\) with \(H(\phi,F)=h_{\rm alg}(\phi)\). The setting matches the same endomorphism and the report's finite subset, not attainment by a different flow with the same value. Limits: the equivalence is not a solution to Lehmer's problem; zero entropy has the trivial \(F=\{0\}\) witness; the local source corrections recorded in DGB16-U004 are retained. |
| `progress/sections/entropy.tex`, Section 2, paragraph after Proposition `fo:attainment-implication` (direct-sum construction) | `\citet{DGB16}` | Attributes the addition and directed-continuity properties used to sum the entropies of the constructed irreducible companion flows and to see that every finite set lies in finitely many summands with a positive tail left over. The setting matches direct sums of abelian flows with extended nonnegative addition and no subtraction of infinities; the directed-union and direct-product addition interfaces are recorded in DGB16-U001 and DGB16-U002. Limits: the companion-flow construction and the direct-sum conclusion are the report's local deduction. |
| `progress/sections/entropy.tex`, Section 2.1.3, "A conditional critical regularity theorem", compact-dual setup before Definition of \(T\) | `\citet{DGB16}` | Points to the compact/Pontryagin-dual picture used for the character torus: the report identifies \(\widehat{\mathcal O}=\operatorname{Hom}(\mathcal O,\R/\Z)\) with the \(d\)-torus and uses normalized Haar/Lebesgue measure. The report's own project convention is stated at [L G0084](../../../ledger/Yin_L_G0084_v1.md#faithful-high-moment-arithmetic-interface). Limits: convention and notation only; no theorem-level support is drawn from this mention. Unresolved point: the registered DGB16 units record the finite-subset entropy and flow conventions but no specific DGB16 Pontryagin-dual passage, so this remains a convention pointer without an audited source locator. |

## `Dim19`

Source evidence: the retained arXiv:1912.12545v1 artifact has 27 PDF pages, with printed and PDF pages coinciding.
Its rendered identity and Theorem 1 on p.1 were read: \(\operatorname{house}(\alpha)\ge2^{1/(4d)}\) for noncyclotomic monic irreducible polynomials of degree \(d>1\).
It records that the original proof and the later accepted 2026 text were not audited or compared, and that the key follows the first public-release year.
[Smy08-U001](../../../audits/literature/Smy08/Yin_U001.md#smy08-house) records the house-scale interface and states explicitly that this resolves only the house-scale problem, not Lehmer's gap.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/arithmetic.tex`, Section 5.1.3, "Angular control and signed auxiliary bundles", proof of Lemma `ar:angular` | `\cite[Theorem~1]{Dim19}` | Supports the house bound \(\max_j|\beta_j|\ge2^{1/(4D)}\) for the powered element \(\beta=\alpha^h\) at its actual minimal-polynomial degree \(D\). The setting matches: \(\beta\) is a nontorsion algebraic unit, so its monic irreducible minimal polynomial is noncyclotomic and of degree \(D>1\); the source degree \(d\) converts to the report's actual \(D\), and the report derives \(v\ge c_0/D^2\) locally. Limits: statement-level acceptance only; the source proof and the revised accepted text are not audited, and the bound alone gives no uniform Mahler gap. Unresolved point: there is no dedicated Dim19 source unit; the evidence is the statement reading recorded here and the Smy08-U001 house interface, so this row is a statement-scope acceptance rather than a U-level source audit. |

## `GBV15`

Source evidence: [GBV15-U001](../../../audits/literature/GBV15/Yin_U001.md#gbv15-u001) records the inspected arXiv:1111.1287v3 (19 February 2013) Theorem 4.17, pp.23--24, and the introductory formula: for the monic rational characteristic polynomial \(\chi_\phi\), with \(s\) the least positive denominator-clearing integer, \(p_\phi=s\chi_\phi\) is primitive integral and \(h(\phi)=m(p_\phi)=\log s+\sum_{|\lambda_i|>1}\log|\lambda_i|\), with no invertibility or nonzero-determinant assumption.
It also records the finite-set realization interface and that the original p-adic proof was not audited.
The definition registration for the logarithmic Mahler measure and its normalization is [DGB16-U004](../../../audits/literature/DGB16/Yin_U004.md#dgb16-mahler-measure).

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/entropy.tex`, Proposition `fo:yuzvinski-formula` statement | `\cite[Theorem~4.17 in the consulted preprint]{GBV15}` | Supports the rational algebraic Yuzvinski formula \(h_{\rm alg}(A)=m(\chi_{A,\Z})\) for a rational linear map \(A\) on \(\Q^d\). The report's \(\chi_{A,\Z}\), the primitive integer associate with positive leading coefficient, is the source's \(p_\phi=s\chi_\phi\); clearing denominators contributes \(\log s\), which is why a sum over expanding archimedean eigenvalues alone is incomplete. The setting matches a rational endomorphism of \(\Q^d\) with the discrete topology and natural logarithms. Limits: the consulted preprint is v3; DGB16's reference to a published Theorem 4.18 is matched to v3 Theorem 4.17 by content, not by a verified edition comparison, and the upstream p-adic lemmas are not re-audited. |

## `GK78`

Source evidence: [GK78-U001](../../../audits/literature/GK78/Yin_U001.md#gk78-u001) records the selected inspection of Section 9, printed pp.74--76 / PDF pp.27--28: for Hilbert-space vectors of norm at least \(a>0\), a set of diameter strictly less than \(a\) contains at most \(\binom{N}{\lfloor N/2\rfloor}\) indexed subset sums, with no dimension dependence.
It records the strict-diameter convention and that the inspected artifact is the published 1978 chapter coauthored by the theorem's author, not the inaccessible 1970 article.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/growth.tex`, Section 3.1.2, "A necessary diffusion scale for stationary laws", paragraph after Proposition `ret:stationary-radius` | `\cite[Section~9]{GK78}` | Supports the dimension-free separated-sum argument behind the displayed ball bound \(\Prob\{\sum_j\eta_jv_j\in\overline B(c,r)\}\le\min\{1,\sqrt{(24+96r^2/a^2)/n}\}\) for deterministic vectors of common norm \(a\). The setting matches a real Hilbert space (the complex case by realification) and the source's geometric block transfer; the report supplies the independent-block grouping and the explicit constants, and maintains the source's strict comparison between coefficient norms and the tested radius. Limits: equality endpoints are not inferred; the source's Section 3 enumeration was not separately audited; no whole-chapter or 1970-article audit is claimed. |

## `Li26`

Source evidence: [Li26-U001](../../../audits/literature/Li26/Yin_U001.md#li26-positive-order-comparison) records the inspected arXiv:2609.01529v2 definitions and equation (1.1) on p.1: \(H_q(S)\) for \(q>0\), \(q\ne1\), with natural logarithms, \(H_1\) the Shannon entropy, \(H_\infty\) the min-entropy and \(H_0=\log|\operatorname{supp}S|\); it also records the checked Theorem 1.4 and that the endpoint Conjecture 1.1 is not adopted.
The definition registration for the Rényi conventions is [Li26-U001](../../../definitions/index.md#group-growth-and-bernoulli-entropy).

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/entropy.tex`, Section 2.1, Definition `fo:binary-law` | `\cite[p.~1]{Li26}` | Adopts the standard Rényi support, Shannon and collision entropies for the finite laws \(\mu_n\) of \(S_n=\sum_{j=0}^{n-1}\varepsilon_j\alpha^j\): \(H_0=\log|\operatorname{supp}\mu_n|\), \(H_1=-\sum_x\mu_n(x)\log\mu_n(x)\), \(H_2=-\log\sum_x\mu_n(x)^2\). The setting matches finite-support laws and natural logarithms, and the report's \(H_0,H_1,H_2\) coincide with the source's \(q=0,1,2\) formulas. Limits: definitions only; the source's positive-order comparison Theorem 1.4 and its endpoint conjecture are neither cited nor used here. |

## `Luc22`

Source evidence: [Luc22-U001](../../../audits/literature/Luc22/Yin_U001.md#luc22-von-neumann-dimension) records the inspected arXiv:1901.00827v2 (16 September 2020) Sections 0--5 and 9 and Appendix 14: the canonical group trace \(\tau_G(T)=\langle T(e),e\rangle\), the matrix trace \(\operatorname{Tr}_r\otimes\tau_G\) as a sum not divided by \(r\), the weak-isomorphism convention "injective with dense image", and the kernel-removed Fuglede--Kadison determinant Definition 14.14 integrating \(\log\lambda\) over \((0,\infty)\) with the zero atom discarded.
It records the Fourier identification \(\mathcal N(\Z^d)=L^\infty(\mathbb T^d)\) with Haar probability and that the kernel-removed determinant of a nonzero Laurent polynomial equals its ordinary Mahler measure.
The inspected object is the v2 preprint, not a presumed identical journal rendering.
The definitions are registered at [group trace, von Neumann dimension and weak isomorphism](../../../definitions/index.md#group-growth-and-bernoulli-entropy).

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/determinants.tex`, Section 4, opening paragraphs | `\cite{Luc22}` | Attributes the weak-isomorphism/determinant perspective and the warning that other groups, singular operators and rectangular matrices require their own comparison, so their determinant constants cannot be substituted for the classical cyclic one. The report's Fourier identification \(\mathcal N(\Z)=L^\infty(S^1)\) and its determinant formula are stated locally. Limits: this is structural context and a caution, not a transferred theorem across groups. |
| `progress/sections/determinants.tex`, Section 4, paragraph after the determinant definition | `\citet{Luc22}` | Adopts the source's weak-isomorphism convention (injective and dense image) and its unnormalized matrix-trace convention (\(\operatorname{Tr}_r\otimes\tau_G\), no division by \(r\)): hence the report's determinant uses the circle trace and the matrix trace \(\operatorname{tr}_r(B)=\sum_jB_{jj}\) and integrates only over \((0,\infty)\), removing the kernel. The setting matches the source's \(\mathcal N(G)\) convention specialized to \(G=\Z\) via Fourier, and the source notation \(r_A\), \(\operatorname{Tr}_r\) converts to the report's \(A\), \(\operatorname{tr}_r\). Limits: the scalar-return identity \(\log\det_{\mathcal N(\Z)}(A)=m(\det A)\) is proved in the report, not imported. Unresolved point: the inspected source is arXiv v2, not the journal rendering. |

## `Mer13`

Source evidence: [Mer13-U001](../../../audits/literature/Mer13/Yin_U001.md#mer13-u001) records the published Numdam PDF and Proposition 4.23 with proof, printed pp.458--462 / PDF pp.37--41: for the real expanding root \(\beta\) of \(t^4-2t^3+t^2-2t+1\), the monoid generated by \(x\mapsto\beta x\) and \(x\mapsto\beta x+1\) is not strongly automatic.
The result is accepted for the original alphabet \(\{0,1\}\) at that one beta; the interval table, asserted complete 76-state enumeration and computer verification were not rerun.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/growth.tex`, Section 3.1.1, "An infinite core for the original Lehmer number", theorem `ret:lehmer-core` proof paragraph | `\cite[Proposition~4.23]{Mer13}` | Attributes the earlier descent and finite-residue method and its fixed quartic \(t^4-2t^3+t^2-2t+1\). The setting matches the source's original digit alphabet and the report's difference-recurrence convention (the negative sign is absorbed by the symmetric alphabet, as recorded in the unit), and the role is comparison and attribution only: the report explicitly does not transfer that numerical certificate to its different polynomial \(P_L\). Limits: no computation, enumeration or interval table is rerun, and no all-Salem or Lehmer conclusion is drawn. |

## `Pri11`

Source evidence: [Pri11-U001](../../../audits/literature/Pri11/Yin_U001.md#pri11-u001) records the accepted Theorem 3.1 on p.7 and equation (3.2) on p.2 of the retained arXiv:1307.5734v1 (22 July 2013): for integer \(Q\) with simple zeros of degree \(N\ge55\) and a real \(A\)-Lipschitz function supported in radius \(R\),
\[
\left|\frac1N\sum_j\varphi(\beta_j)-\int\varphi\,d\mu\right|\le A(2R+1)\sqrt{\frac{\log(\max\{N,M(Q)\})}{N}},
\]
with \(M(Q)\) the ordinary multiplicative Mahler measure including the leading coefficient, normalized arclength \(\mu\) and natural logarithms.
The unit records that the acceptance is at statement/applicability scope, that no degree preservation or lower bound on \(N\) is supplied, and that the source supplies no arithmetic norm income.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/arithmetic.tex`, Section 5.1.1, proof of Proposition `ar:cyclic-cost` | `\cite[Theorem~3.1]{Pri11}` | Supplies the discrepancy estimate for the monic minimal polynomial of \(\beta=\alpha^n\), whose roots are simple. The report's displayed bound \(A(2R_0+1)\sqrt{\max\{\log D/D,h\}}\) follows because \(M(Q)=\exp(Dh)\) and \(\log(\max\{D,M\})/D=\max\{\log D/D,h\}\); the report's test function has support radius \(2R\), so the source's radius factor is \(2R+1=2R_0+1\) with \(R_0=2R\), i.e. \(4R+1\). The setting matches: \(D\ge55\) is checked, \(\varphi\) is real, globally Lipschitz and compactly supported, \(\mu\) is normalized arclength, and logarithms are natural. Limits: statement/applicability acceptance only; the potential-theory proof and its external inputs are not audited, and the report's truncation, circle-mean and radial-tail costs are local. Unresolved point: the inspected artifact is the arXiv v1, not journal pagination. |

## `Smy08`

Source evidence: [Smy08-U001](../../../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) records the inspected arXiv:math/0701397v2 (28 January 2008) Sections 1--4: the Mahler measure integral and product formula with natural logarithms, the primitive integer minimal polynomial with positive leading coefficient, the absolute logarithmic height \(h_{\rm abs}=m(P_\alpha)/d\), and the corrected Kronecker characterization on p.322.
[Smy08-U002](../../../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number) records Section 5.1, equation (15): Smyth's theorem \(M(\alpha)\ge\theta_0\) for nonzero nonreciprocal algebraic integers, with \(\theta_0>1\) and \(\theta_0^3-\theta_0-1=0\), alongside the reciprocity conventions.
[Smy08-U003](../../../audits/literature/Smy08/Yin_U003.md#smy08-salem-number) records the Section 8 Salem-number definition and the finite-search domain.
The inspected object is the author preprint, not an independently compared copy of the published chapter.
The definitions are registered at [Mahler measure, arithmetic heights and the house](../../../definitions/index.md#mahler-heights-and-house).

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `progress/sections/overview.tex`, Section 1, paragraph after Definition `sec:formulations` | `\citet[\S1]{Smy08}` | Adopts the survey's Mahler-measure convention: natural logarithms, roots counted with multiplicity, \(M(P)=|a_d|\prod_i\max\{1,|\alpha_i|\}\) and \(m(P)=\log M(P)\), with total rather than degree-normalized measure. The setting matches nonzero integer polynomials, and the report explicitly distinguishes \(m(P)\) from the degree-normalized height \(m(P)/d\). Limits: convention attribution; the report's target and quantifiers are its own. |
| `progress/sections/arithmetic.tex`, Section 5, opening paragraph on the reciprocal reduction | `\citet[\S5.1]{Smy08}` | Attributes the classical nonreciprocal lower bound reducing a possible sequence with \(m\to0^+\) to reciprocal noncyclotomic units: the source's Section 5.1, equation (15), reports Smyth's theorem \(M(\alpha)\ge\theta_0>1\) for nonzero nonreciprocal algebraic integers. The setting matches the report's primitive irreducible polynomials and its unit terminology; the report's reciprocal reduction is stated locally. Limits: the survey reports this as an author statement; the original 1971 proof is not audited. |
| `progress/sections/arithmetic.tex`, Section 5.1.1, proof of Proposition `ar:cyclic-cost` | `\cite[p.~322]{Smy08}` | Supports Kronecker's theorem in the precise p.322 form: for an irreducible minimal polynomial the measure-one cases are exactly the zero root and roots of unity, so every noncyclotomic member has positive height and a fixed-degree family has a positive lower height bound, forcing the actual degree \(D\to\infty\). The setting matches the report's noncyclotomic unit \(\beta=\alpha^h\); the corrected product-with-multiplicities form recorded in the unit is the one used. Limits: convention/precision guard, not a proof audit; the report's finite-count argument and degree consequence are local. |
| `progress/sections/entropy.tex`, Section 2.2.2, "A family where every repeated local change has linear cost", paragraph following Theorem `str:uniform-cost` | `\cite{Smy08}` | Uses the exact Mahler integral \(M(P)=\exp(\int_0^1\log|P(e^{2\pi it})|\,dt)\) to pay the radial expense: the report's circle \(|t|=r>1\), the per-factor negative-integral estimate and the resulting \((4k+1)\log r\) term follow the source's integral identity with natural logarithms and roots counted with multiplicity. The setting matches Laurent/polynomial characteristic factors; no specific theorem beyond the integral formula is used. Limits: formula/convention use; the survey's reported results and their original proofs are outside this row. |
| `progress/sections/growth.tex`, Section 3.1.1, "An infinite core for the original Lehmer number", paragraph before Definition `ret:return-core` | `\cite[\S8]{Smy08}` | Supports the Salem-number definition: a real algebraic integer \(\tau>1\) of degree at least four whose conjugates are \(\tau^{-1}\) and points of the unit circle, with \(M(\tau)=\tau\). The report adds "unit" and "at least one unit-circle conjugate" explicitly; the setting matches the source's Section 8 convention, and the report's \(P_L\) expanding root satisfies it. Limits: definition and terminology only; the source's finite-search coverage, enumeration claims and conjectures were read as reports and not rerun. |
