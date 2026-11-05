---
author: Yin
---
# Independent whole review of the universal raw p=2 floor

Review act: 2026-11-04T20:58 UTC.
The human record author is Yin.
This is a separately organized independent agent review of the complete [C0855v2 statement](../../claims/Yin_C_G0855_v2.md#statement), Parts A--D, and its [complete argument](../../claims/Yin_C_G0855_v2.md#argument), SC1--SC23.
The reviewer had no role in substantive proof development and received no proof-generation dialogue, proposing-agent mathematical explanation, temporary candidate or generation notes.
The candidate's own provenance paragraphs were visible but supplied no review evidence.
The fixed statement and argument were read directly and their obligations were reconstructed before consulting the relevant earlier dependency finding.
No rolling Draft was consulted and no substantive repair was supplied.
The candidate had no selected assessment during this review.

## Review object and earlier evidence

The core obligations were the common-disk capacity comparison, single-valued continuation of every original branch, the precise shifted-Hankel capacity limit, unconditional integral nonrational input, the reciprocal square-mass estimate, ordinary-norm descent at actual degrees, finite-place normalization, and the restricted FM13 operator identity.
Part C additionally requires the same determinant and the complete supplied arithmetic hypotheses of C0860v4 Part C.
Part D requires checking both concentration implications without asserting their hypothesis uniformly.
The retained [C0855v1](../../claims/Yin_C_G0855_v1.md#statement) is a different, unassessed restricted-support argument and is neither a premise nor an independently reviewed result of this finding.
A targeted search found no earlier formal whole-family review of C0855 to reuse for the new proof.

The adopted [C0860v4 Part C](../../claims/Yin_C_G0860_v4.md#statement) and its [supplied-center argument](../../claims/Yin_C_G0860_v4.md#supplied-center-comparison) were read at the exact interface used here.
After forming initial findings, the [R1076v3 independent finding](Yin_R_G1076_v3.md#fixed-center-whole) was read to confirm the retained coverage of its exact slope and finite-place coefficient.
Its general rank theorem is reused at that accepted scope, not claimed as a new complete audit here.
Its unrelated precision-budget conclusions are not inputs to the present proof.
The required C0231 descent and C0858 arithmetic/Hankel portions were read and their new invocations were checked directly.
The inspected erratum contained no current objection affecting these inputs.

<a id="raw-p2-whole"></a>
## Whole raw p=2 finding

**Finding:** no unresolved mathematical gap was found in the entire C0855v2 statement A--D and complete argument SC1--SC23 under its exact hypotheses and accepted-source limits.
The proof establishes the universal raw bound \(\mathcal M_2(\alpha)\ge1/\sqrt{10}\), the stronger nonunit bound, the exact norm-descent identity, and the stated FM13 consequence on \(\mathcal S\).
It also establishes the original-root capacity/determinant comparison and the precise conditional total-Mahler consequences.
The latter do not resolve the unrestricted [G0001 contract](../../tasks/Yin_T_G0001_v1.md#lehmer-entropy-growth).
This finding selects no Claim assessment or Task decision and makes no novelty, optimal-constant or formal-verification claim.

### Single slit, topology and Green comparison: SC1--SC5

For the unit disk with one positive real slit, the Joukowski map is one-to-one on the exterior and sends the removed radial interval to \([2,e^v+e^{-v}]\).
Together with the original \([-2,2]\), the image is the interval of length \(2+e^v+e^{-v}\).
The map has leading coefficient one at infinity, so the interval capacity gives exactly \(\cosh^2(v/2)\), including \(v=0\).
Rotation and scaling give SC1 with the stated factor \(r\).

For finitely many slits attached to the same positive-radius disk, inversion produces a disk with radial slits entering from its outer boundary.
Radial contraction toward zero stays inside that domain, which verifies simple connectivity on the sphere, including the point at infinity in the original exterior.
The circle arcs and finite slit sides and tips are regular for this exterior Dirichlet problem.
Repeated directions, equal endpoints and zero-length slits cause no extra boundary component.
The boundary values used in SC2 are therefore legitimate.

The difference \(g_\nu-g_0\) has no logarithmic singularity at infinity and extends harmonically there.
Its boundary values are nonpositive, so the maximum principle applies without presupposing an inequality of capacities.
On the common exterior, every boundary point belongs to at least one of the individual hulls.
That term contributes \(g_0\) to \(\sum(g_0-g_\nu)\), while all others are nonnegative and \(g=0\).
Thus \(H\ge0\) on the whole boundary.
At infinity its value is \(\sum_\nu\log(\operatorname{cap}K_\nu/r)-\log(\operatorname{cap}K/r)\), giving the direction asserted in SC2.
The common disk is essential to this proof; unrestricted capacity subadditivity is not assumed.

The slit lengths in SC4 are exactly \((t+2u_i)_+\) and \((t+4u_i)_+\) for each used rotation.
Each single-slit logarithmic cost is twice the indicated \(\log\cosh\), giving SC5 with factor \(2s\).
Every original embedding is counted, including both complex embeddings of a nonreal pair.
A neutral root contributes twice when \(t>0\), and a contracting endpoint contributes precisely when it lies outside the disk.
Repeated slits only weaken this upper bound.

### Branch continuation and the identical determinants: SC6--SC8

After \(x=1/z\), each radicand has all zeros and poles in the constructed hull, is nonvanishing and holomorphic in the exterior, and has value one at infinity.
Simple connectivity gives its unique holomorphic square root based there.
All terms of the finite orbit sum extend on the same domain; no degree of an algebraic cover enters this continuation.
The possible point \(z=0\) is inside the positive-radius disk and introduces no omitted singularity in the domain.
The same reasoning applies to the product radicand used for the unconditional comparison.

For a fixed analytic contour in this exterior, the coefficient integral extracts precisely \(a_{n+1}\).
Expanding the two Vandermonde determinants and permuting integration variables yields SC6 with its factor \(1/h!\) and squared Vandermonde.
The resulting absolute bound has exponent \(h(h-1)\) on the transfinite diameter and only \(h\log A_\Gamma-\log h!\) in the remaining logarithm.
Division by \(h^2\) gives the asserted capacity coefficient.
For the normalized exterior conformal map \(\phi(w)=cw+O(1)\), the image of \(|w|=R\) is analytic and Jordan, and its exterior is parametrized by \(\phi(Rw)\).
Its capacity is therefore \(Rc\), justifying the contour limit to \(\operatorname{cap}K_t\).
The input and contour remain fixed as \(h\to\infty\); this limit requires no degree-uniform contour estimate.
Zero determinants are harmless under the stated negative-infinity convention.

For the optional strengthening, C0860v4 Part C gives two-adically integral rational approximants at each required precision, with the stabilizer loss paid and rank \(K_{\rm pole}t+O(1)\).
Its all-level elementary-divisor sum supplies the quadratic coefficient \(a/(2K_{\rm pole})\) for the same shifted leading determinants of the same original orbit sum.
The positive slope, all-place arithmetic identity, fixed center and nonempty orbit hypotheses remain present.
Along the infinitely many nonzero integral determinants, this gives the lower logarithmic coefficient \(a\log2/(2K_{\rm pole})\).
Comparison with SC7 for each fixed radius gives SC8 and then its infimum form.
The analytic continuation depends on the original radicands, so poles introduced only in rational approximants require no extra slits for the original function.
The new comparison supplies neither centers nor masks nor a reduction of the actual slope.

### Integral nonrational germ and reciprocal optimization: SC9--SC15

The fixed congruence \(P_4-P_2\in4\mathbb Z[x]\) applies to the reversed powered polynomials used here.
Their constant coefficients are one, so \(W/P_2\in x\mathbb Z[[x]]\).
The displayed scaled-binomial formula is twice a signed Catalan integer and is valid for every \(n\ge1\), including the initial coefficient.
Composition is a well-defined formal substitution, proving integrality of \(F=P_2\sqrt{1+4W/P_2}\).

Power stability makes the roots within each powered polynomial simple.
An equality between a squared and a fourth-powered conjugate would equate positive absolute heights \(2h(\alpha)\) and \(4h(\alpha)\), which is impossible.
Thus \(P_2P_4\) has simple zeros and its square root cannot be rational.
The shifted Kronecker criterion applies to \((F-F(0))/x\), so infinitely many of the exact leading determinants used in SC7 are nonzero integers.
Their absolute values are at least one, proving SC9 for every \(t\) and its infimum.
This uses a complete original integral conjugate set, without a realizability assumption for arbitrary radial data.

The inequality \(\log\cosh x\le x^2/2\) and the positive-part inequality in SC10 give the coefficients \(d/2\), \(3m\) and \(5E_2\) exactly.
Under the stated strict condition \(3sm<1\), the minimizing choice for SC11 is positive and admissible.
For the reciprocal pairing, the two cases \(a\le t\) and \(a>t\) give the stated pair inequality, including \(a=0\).
Summing it for powers two and four gives \((s/4)(2dt^2+40E_2)\), hence SC14.
Its minimizing radius parameter is \(1/(ds)\), and the minimum upper bound is \(10sE_2-1/(2ds)\).
Using SC9 at \(s=1\) gives \(dE_2\ge1/20\).
The reciprocal identity \(\sum_i u_i^2=2E_2\) then gives the exact constant \(1/\sqrt{10}\).

Under the separately supplied condition \(dE_2\le Cm^2\), SC11 gives \(\sqrt{10C}\,m\ge1-3m\) when \(m<1/3\).
For \(m\ge1/3\) the same final lower bound already holds.
SC14 supplies the second bound \(m\ge1/\sqrt{20C}\).
These are two simultaneous conditional consequences for every \(C>0\), not an unconditional claim about concentration.
For Salem inputs the two nonzero radial coordinates are \(m\) and \(-m\), so \(E_2=m^2\) and the displayed concentration ratio is indeed \(d\).

### Actual-degree norm descent and finite places: SC16--SC22

The place weights in SC16 give one summand per real embedding and two per complex place, yielding SC17 exactly for units.
In C0231's ordinary relative-norm construction, all \(e\) extensions of an embedding of \(L\) have the same modulus because their \(n\)-th powers agree.
The logarithm of the norm therefore equals \(e\log r_\tau\), and every embedding of \(\mathbb Q(\gamma)\) is repeated \(f\) times among those of \(L\).
The square sum changes by \(e/f\), while the actual degree changes by \(1/(ef)\).
Their product changes by \(1/f^2\), establishing SC18 with no normalized norm or radical substitution.
The norm is a nontorsion unit, as also follows from \(\gamma^n=(\alpha^n)^e\).
Strict descent of positive integer degree terminates, and \(f\ge1\) gives SC19.
This is an existence argument and does not require deciding the all-power condition algorithmically.

A nontorsion reciprocal endpoint has monic reciprocal minimal polynomial with constant term one and satisfies the full original-input hypotheses for SC15.
The possible anti-reciprocal constant-term sign would force the root one in an irreducible polynomial and hence cannot occur at such an endpoint.
For a nonreciprocal endpoint, Smyth's accepted algebraic-integer theorem applies because the endpoint remains a unit.
Cauchy--Schwarz gives \(\mathcal M_2\ge\sum_i|u_i|=2m\).
The polynomial \(x^3-x-1\) is increasing for \(x\ge1\) and is negative at \(5/4\); thus \(\theta_0>5/4\).
The integral of \(1/x\) from one to \(5/4\) exceeds \(1/5\), so the stated nonreciprocal lower constant exceeds \(2/5>1/\sqrt{10}\).
Reciprocity need not be preserved during descent because both endpoint cases are covered.

For a nonunit, some finite integer valuation is nonzero.
With the stipulated rational absolute values, its logarithm is \(-\operatorname{ord}_v(\alpha)\log p/e_v\), and its contribution to the squared raw quantity is \(df_v\operatorname{ord}_v(\alpha)^2(\log p)^2/e_v\).
The local-degree identity gives \(e_vf_v\le d\), in particular \(e_v\le d\), so this is at least \((\log2)^2\).
The sign of the valuation does not matter and nonintegral numbers are included.
Combining this with the unit descent proves the full domain of SC22, with torsion excluded as stated.

### FM13 and the original p=1 boundary: SC23

The retained 2013 FM13 normalization is \(h_p(\alpha)=\|f_\alpha\|_p\) with all places and \(m_p(\alpha)=\deg(\alpha)h_p(\alpha)\).
The function is invariant under torsion, but the original degree need not be.
Choosing a minimal-degree representative realizes \(d(f)\), and membership in \(\mathcal U\) makes that representative an algebraic unit.
Nonzero \(f\) means it is nontorsion.
On the exact set \(\mathcal S=\mathcal R\cap\mathcal P\cap\mathcal U\), representability gives \(d(f)=\delta(f)\) and the accepted Proposition 4.5 gives \(Mf=\delta(f)f\).
This proves the identity and lower bound in SC23 from the raw theorem.
No reversal of the general upper comparison is used.
A positive norm minimum on the entire divisible unit space is not asserted and would be incompatible with rational scaling.
The source's Theorem 4 identifies the two positive-floor formulations at its retained statement/applicability scope.

For units, the total Mahler logarithm is half the unweighted absolute-log sum.
A lower bound on the degree-weighted square norm alone gives no degree-independent lower bound on that sum by the inequalities used here.
The exact additional condition SC12 supplies a restricted return; it is not proved for all original inputs.
Accordingly this is a p=2 result and a conditional p=1 interface, not a completion of G0001.

### Original-source checks and limits

The local [Dim19 original](../../literature/pdf/Dim19.pdf), arXiv:1912.12545v1, was text-read at printed pages 3--4 and 12--16.
This covers Lemma 2.1 and its finite symmetric-power proof, Proposition 2.2, the capacity/transfinite-diameter and exterior-map normalization in Section 3, the determinant mechanism and rationality statement in Section 4, and the Theorem 1 application.
The reversed-polynomial convention and the precise shifted determinant are compatible with the present proof.
The classical capacity identities are accepted as established inputs at this scope; the direct contour and Green comparisons in C0855v2 were checked above.
Neither the original Dubinin proof nor the complete Bertrandias proof was independently re-audited.

The local [BNZ22 original](../../literature/pdf/BNZ22.pdf), retained arXiv v3, was text-read at printed pages 5--6: the Hankel definitions, Lemma 2.1, Corollary 2.2 and Corollary 2.3.
For the series \((f-f(0))/x\), its \(\Delta_{0,h-1}\) is exactly the present \(\Delta_h\).
The finite Pade argument and eventual-vanishing equivalence were checked at that scope, without a whole-paper review.

The retained [FM13 May 6, 2013 author manuscript](../../literature/pdf/FM13--author-2013.pdf) was text-read at pages 3--5, 19--20, 22--23 and 26--28 for the definitions, minimal degree, restricted arithmetic set, Proposition 4.5 and Theorem 4 interfaces.
The source inspection and original decomposition-proof limits in [FM13 U001](../literature/FM13/Yin_U001.md#fm13-u001) remain in force.
The 2010 or earlier arXiv manuscript was not substituted.
The local [Smy08 original](../../literature/pdf/Smy08.pdf), printed page 328 / PDF page 7, was checked for equation (15), matching the nonreciprocal theorem retained in [Smy08 U002](../literature/Smy08/Yin_U002.md#smy08-u002).
The 1971 original proof was not newly audited.

For the candidate's comparison-only source paragraphs, the published [Calegari--Dimitrov--Tang Theorem 2.0.1](https://www.math.uchicago.edu/~fcale/papers/UDC.pdf#page=9), printed page 635, was read and retains its strict expanding-derivative hypothesis.
It is not a premise of SC1--SC23.
The published [van Ittersum--Ringeling--Zudilin paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8B96145B989139A2E44CF7ABE8D4EA92/S0004972721000654a.pdf/hedgehogs_in_lehmers_problem.pdf), Section 2, printed pages 237--239, was read at its geometric-question and Theorems 3--4 scope.
Its unconstrained small-product hedgehogs do not supply integer conjugate sets or the concentration condition used here.
No complete proof review of either comparison theorem or exhaustive novelty search was performed.

No numerical experiment, floating-point capacity calculation, native computation output or proof-assistant certificate is a proof premise of this finding.
The original-source checks and accepted dependency reuse do not imply independent re-audit of every ancestor theorem.
C0855v1 remains unassessed at its prior scope, and all assessments and the G0001 decision remain the responsibility of their own materials.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole raw p=2 finding](#raw-p2-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole raw p=2 finding](#raw-p2-whole) | [C0855v2 statement](../../claims/Yin_C_G0855_v2.md#statement) | Entire A--D, universal nonzero nontorsion domain, nonunit floor, exact descent, restricted operator set, original roots, rotations, capacity and conditional concentration consequences. |
| [Whole raw p=2 finding](#raw-p2-whole) | [C0855v2 complete argument](../../claims/Yin_C_G0855_v2.md#argument) | Entire SC1--SC23, topology and Green comparison, branch continuation, exact Hankel limit, arithmetic input, optimization, all-degree descent, finite places and source/Task boundaries. |
| [Whole raw p=2 finding](#raw-p2-whole) | [C0855v2 raw-norm extension](../../claims/Yin_C_G0855_v2.md#raw-p-two-norm-descent) | SC16--SC23 with actual field degrees, all embeddings, ordinary relative norm, both endpoint cases, nonintegral inputs and precise FM13 identity. |
| [Whole raw p=2 finding](#raw-p2-whole) | [C0855v2 source interfaces](../../claims/Yin_C_G0855_v2.md#sources-and-proof-interfaces) | Exact Dim19 capacity and integrality passages and accepted normalization, direct contour proof, comparison-only published statements and retained source limits. |
| [Whole raw p=2 finding](#raw-p2-whole) | [C0231 ordinary norm descent](../../claims/Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Unit and nontorsion preservation, equal-modulus embedding fibers, actual degree d/(ef), strictly decreasing existence descent; the new square-norm identity is checked in C0855v2. |
| [Whole raw p=2 finding](#raw-p2-whole) | [C0858 original branches and Hankel mechanism](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) | Original powered/rotated noncollision, private branch points, nonrationality and finite elementary-divisor implication; BNZ22 shifted leading-Hankel criterion checked against original pp. 5--6. |
| [Whole raw p=2 finding](#raw-p2-whole) | [C0860v2 modulo-four input](../../claims/Yin_C_G0860_v2.md#statement) | Only P4-P2 in 4 Z[x] on the original monic reciprocal input, checked against Dim19 v1 Lemma 2.1 and Proposition 2.2; unrelated M1--M9 not newly reviewed. |
| [Whole raw p=2 finding](#raw-p2-whole) | [C0860v4 supplied finite-place statement](../../claims/Yin_C_G0860_v4.md#statement) | Only complete Part C hypotheses, positive actual pole-rank slope, supplied residual depth, same original orbit sum and all-level determinant valuation coefficient. |
| [Whole raw p=2 finding](#raw-p2-whole) | [C0860v4 supplied-center argument](../../claims/Yin_C_G0860_v4.md#supplied-center-comparison) | R3--R13 interface, full Galois/stabilizer loss, integral approximants, fixed-input rank and precision limits; accepted rank theorem reused at R1076v3 scope. |
| [Whole raw p=2 finding](#raw-p2-whole) | [FM13 source unit](../literature/FM13/Yin_U001.md#fm13-u001) | Only retained 2013 all-place normalization, minimal representative degree, R/P/U definitions, Proposition 4.5 and Theorem 4 at accepted statement/applicability scope, with original selected pages checked. |
| [Whole raw p=2 finding](#raw-p2-whole) | [FM13 restricted arithmetic set](../literature/FM13/Yin_U001.md#restricted-arithmetic-set) | Equality of operator and minimal raw norms only on S; general upper comparison not reversed and whole divisible unit space excluded. |
| [Whole raw p=2 finding](#raw-p2-whole) | [FM13 p=1 boundary](../literature/FM13/Yin_U001.md#p-two-and-classical-gap-boundary) | Factor-two total Mahler convention and one-way p=1 to p=2 implication; historical unresolved p=2 source commentary is not a mathematical premise for the new proof. |
| [Whole raw p=2 finding](#raw-p2-whole) | [Smy08 source unit](../literature/Smy08/Yin_U002.md#smy08-u002) | Only accepted nonreciprocal algebraic-integer threshold from equation (15), original printed p. 328 checked; original 1971 proof not newly audited. |
| [Whole raw p=2 finding](#raw-p2-whole) | [Smy08 nonreciprocal interface](../literature/Smy08/Yin_U002.md#smy08-reciprocal-number) | Application to the nontorsion nonreciprocal unit endpoint and exact total-measure normalization, without invoking unrelated survey conclusions. |
| [Whole raw p=2 finding](#raw-p2-whole) | [G0001 contract](../../tasks/Yin_T_G0001_v1.md#lehmer-entropy-growth) | Original unrestricted total Mahler-gap objective compared for scope only; no Task completion review or p=1 conclusion. |
